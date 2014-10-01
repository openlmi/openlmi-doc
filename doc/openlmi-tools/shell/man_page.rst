Synopsis
========
**lmishell** [options] script [script-options]

Description
===========
LMIShell provides a (non)interactive or interactive way how to access CIM
objects provided by OpenPegasus or sblim-sfcb CIMOM.

LMIShell is based on a python interpreter and added logic, therefore what is
possible to do in pure python, it is possible in LMIShell. There are classes
added to manipulate with CIM classes, instance names, instances, etc.
Additional classes are added to fulfill wrapper pattern and expose only those
methods, which are necessary for the purpose of a shell.

Options
=======
The options may be given in any order before the first positional argument,
which stands for the script name.

    **-h, --help**
        Print summary of usage, command line options and exit.

    **-i, --interact**
        Enter interactive mode, when the script passed as the first positional
        argument is executed.

    **-v, --verbose**
        Print log messages to stderr.

    **-m, --more-verbose**
        Print all log messages to stderr.

    **-q, --quiet**
        Do not print any log messages to stderr.

    **-n, --noverify**
        Do not verify server's certificate, if SSL used. By default, the
        certificate validity check will be performed.

    By default, LMIShell prints out log messages with Error severity. Options
    **-v**, **-m** and **-q** are mutually exclusive and can not be used together.

