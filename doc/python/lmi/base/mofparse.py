# Copyright (C) 2012 Red Hat, Inc.  All rights reserved.
#
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301  USA
#
# Authors: Jan Safranek <jsafrane@redhat.com>
# -*- coding: utf-8 -*-
"""
Simple parser of MOF files. The only thing that is parsed out is list of
included files. This list is composed recursively, i.e. a MOF file can
include another MOF file, which can then include another one.
"""
# Based on pywbem.mof_compiler.py, (C) Copyright 2006-2007 Novell, Inc.

from pywbem import lex
from pywbem import yacc
from pywbem.lex import TOKEN
import os

class MOFLexer:
    """ Lexer for MOF files. """
    def __init__(self, **kwargs):
        self.lexer = lex.lex(module=self, **kwargs)

    reserved = {
        'pragma':'PRAGMA',
        'false': 'FALSE',
        'true': 'TRUE',
        'null': 'NULL'
        }

    tokens = reserved.values() + [
            'IDENTIFIER',
            'stringValue',
            'floatValue',
            'charValue',
            'binaryValue',
            'octalValue',
            'decimalValue',
            'hexValue',
        ]

    literals = '#(){};[],$:='

    # UTF-8 (from Unicode 4.0.0 standard):
    # Table 3-6. Well-Formed UTF-8 Byte Sequences Code Points
    # 1st Byte 2nd Byte 3rd Byte 4th Byte
    # U+0000..U+007F     00..7F
    # U+0080..U+07FF     C2..DF   80..BF
    # U+0800..U+0FFF     E0       A0..BF   80..BF
    # U+1000..U+CFFF     E1..EC   80..BF   80..BF
    # U+D000..U+D7FF     ED       80..9F   80..BF
    # U+E000..U+FFFF     EE..EF   80..BF   80..BF
    # U+10000..U+3FFFF   F0       90..BF   80..BF   80..BF
    # U+40000..U+FFFFF   F1..F3   80..BF   80..BF   80..BF
    # U+100000..U+10FFFF F4       80..8F   80..BF   80..BF

    utf8_2 = r'[\xC2-\xDF][\x80-\xBF]'
    utf8_3_1 = r'\xE0[\xA0-\xBF][\x80-\xBF]'
    utf8_3_2 = r'[\xE1-\xEC][\x80-\xBF][\x80-\xBF]'
    utf8_3_3 = r'\xED[\x80-\x9F][\x80-\xBF]'
    utf8_3_4 = r'[\xEE-\xEF][\x80-\xBF][\x80-\xBF]'
    utf8_4_1 = r'\xF0[\x90-\xBF][\x80-\xBF][\x80-\xBF]'
    utf8_4_2 = r'[\xF1-\xF3][\x80-\xBF][\x80-\xBF][\x80-\xBF]'
    utf8_4_3 = r'\xF4[\x80-\x8F][\x80-\xBF][\x80-\xBF]'

    utf8Char = r'(%s)|(%s)|(%s)|(%s)|(%s)|(%s)|(%s)|(%s)' % (utf8_2, utf8_3_1,
            utf8_3_2, utf8_3_3, utf8_3_4, utf8_4_1, utf8_4_2, utf8_4_3)

    def t_COMMENT(self, t):
        r'//.*'
        pass

    def t_MCOMMENT(self, t):
        r'/\*(.|\n)*?\*/'
        t.lineno += t.value.count('\n')


    t_binaryValue = r'[+-]?[01]+[bB]'
    t_octalValue = r'[+-]?0[0-7]+'
    t_decimalValue = r'[+-]?([1-9][0-9]*|0)'
    t_hexValue = r'[+-]?0[xX][0-9a-fA-F]+'
    t_floatValue = r'[+-]?[0-9]*\.[0-9]+([eE][+-]?[0-9]+)?'

    simpleEscape = r"""[bfnrt'"\\]"""
    hexEscape = r'x[0-9a-fA-F]{1,4}'
    escapeSequence = r'[\\]((%s)|(%s))' % (simpleEscape, hexEscape)
    cChar = r"[^'\\\n\r]|(%s)" % escapeSequence
    sChar = r'[^"\\\n\r]|(%s)' % escapeSequence
    charValue = r"'%s'" % cChar

    t_stringValue = r'"(%s)*"' % sChar

    identifier_re = r'([a-zA-Z_]|(%s))([0-9a-zA-Z_]|(%s))*' % (utf8Char, utf8Char)

    @TOKEN(identifier_re)
    def t_IDENTIFIER(self, t):
        t.type = self.reserved.get(t.value.lower(), 'IDENTIFIER')  # check for reserved word
        return t

    # Define a rule so we can track line numbers
    def t_newline(self, t):
        r'\n+'
        t.lexer.lineno += len(t.value)
        t.lexer.linestart = t.lexpos

    t_ignore = ' \r\t'

    # Error handling rule
    def t_error(self, t):
        msg = "Illegal character '%s' " % t.value[0]
        msg += "Line %d" % (t.lineno)
        t.lexer.parser.log(msg)
        t.lexer.skip(1)

class MOFParseError(ValueError):
    pass

class MOFParser:
    """ Parser of '#pragma include' directivers in MOF files."""
    tokens = MOFLexer.tokens

    def __init__(self, **kwargs):
        self.lexer = MOFLexer()
        self.parser = yacc.yacc(module=self, debug=0, write_tables=0, **kwargs)
        self.files = []

    def p_error(self, p):
        ex = MOFParseError('Parse error at line %d' % (p.lineno))
        if p is None:
            ex.args = ('Unexpected end of file',)
            raise ex
        ex.file = self.filename
        ex.lineno = p.lineno
        raise ex


    def p_mofSpecification(self, p):
        """mof : mofItemList"""

    def p_mofItemList(self, p):
        """mofItemList : empty
                         | mofItemList mofItem
                       """

    def p_mofItem(self, p):
        """mofItem : pragma
                     | IDENTIFIER
                     | literal
                     | value
                     """


    def p_pragma(self, p):
        """pragma : '#' PRAGMA pragmaName '(' pragmaParameter ')'"""
        directive = p[3].lower()
        param = p[5]
        if directive == 'include':
            fname = param
            fname = os.path.dirname(self.filename) + '/' + fname
            self._parse_file(fname)

    def p_pragmaName(self, p):
        """pragmaName : identifier"""
        p[0] = p[1]

    def p_pragmaParameter(self, p):
        """pragmaParameter : stringValue"""
        p[0] = self._fixStringValue(p[1])

    def _fixStringValue(self, s):
        s = s[1:-1]
        rv = ''
        esc = False
        i = -1
        while i < len(s) - 1:
            i += 1
            ch = s[i]
            if ch == '\\' and not esc:
                esc = True
                continue
            if not esc:
                rv += ch
                continue

            if ch == '"'   : rv += '"'
            elif ch == 'n' : rv += '\n'
            elif ch == 't' : rv += '\t'
            elif ch == 'b' : rv += '\b'
            elif ch == 'f' : rv += '\f'
            elif ch == 'r' : rv += '\r'
            elif ch == '\\': rv += '\\'
            elif ch in ['x', 'X']:
                hexc = 0
                j = 0
                i += 1
                while j < 4:
                    c = s[i + j];
                    c = c.upper()
                    if not c.isdigit() and not c in 'ABCDEF':
                        break;
                    hexc <<= 4
                    if c.isdigit():
                        hexc |= ord(c) - ord('0')
                    else:
                        hexc |= ord(c) - ord('A') + 0XA
                    j += 1
                rv += chr(hexc)
                i += j - 1

            esc = False

        return rv

    def p_value(self, p):
        """value : integerValue
                 | floatValue
                 | charValue
                 | stringValue
                 | booleanValue
                 | nullValue
                 """

    def p_literal(self, p):
        """literal : '('
                  | ')'
                  | '{'
                  | '}'
                  | ';'
                  | '['
                  | ']'
                  | ','
                  | '$'
                  | ':'
                  | '='
                  """

    def p_integerValue(self, p):
        """integerValue : binaryValue
                        | octalValue
                        | decimalValue
                        | hexValue
                        """

    def p_booleanValue(self, p):
        """booleanValue : FALSE
                        | TRUE
                        """
    def p_nullValue(self, p):
        """nullValue : NULL"""

    def p_identifier(self, p):
        """identifier : IDENTIFIER
                      """
        p[0] = p[1]

    def p_empty(self, p):
        'empty :'


    def _parse_file(self, fname):
        f = open(fname, 'r')
        mof = f.read()
        f.close()

        self.files.append(fname)

        old_filename = self.filename
        self.filename = fname

        # we must use fresh lexer so the old one can continue with parsing the
        # old file
        lex = self.lexer.lexer.clone()
        lex.parser = self.parser
        self.parser.parse(mof, lexer=lex)
        self.filename = old_filename


    def parse_includes(self, fnames):
        """
        Parse given MOF files and return array with all parsed files,
        including the included ones.
        """
        self.filename = '__main__'
        self.files = []

        for fname in fnames:
            if fname[0] != '/':
                fname = os.path.curdir + '/' + fname
            self._parse_file(fname)

        return self.files
