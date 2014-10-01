# Copyright (C) 2012-2014 Peter Hatina <phatina@redhat.com>
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, see <http://www.gnu.org/licenses/>.


class LMIObjectFactory(object):
    """
    Object factory class. Used to avoid circular import dependencies between
    several LMI classes. The class implements a singleton design pattern.

    Example of usage:

    .. code-block:: python

        LMIObjectFactory().register(SomeClass)
        some_obj = LMIObjectFactory().SomeClass(*args, **kwargs)
    """
    # Singleton instance
    _instance = None

    def __getattr__(self, name):
        """
        Returns either a class member or a new instance of registered classes.

        :param string name: member name, which should be returned
        """
        if name in self._classes:
            return self._classes[name]
        raise AttributeError(name)

    def __new__(cls):
        """
        Creates a new :py:class:`.LMIObjectFactory` instance, if not created,
        and returns the singleton instance object.
        """
        if not cls._instance:
            cls._instance = super(LMIObjectFactory, cls).__new__(cls)
            cls._instance._classes = {}
        return cls._instance

    def register(self, reg_class):
        """
        Registers a class into the factory.
        """
        LMIObjectFactory._instance._classes[reg_class.__name__] = reg_class
