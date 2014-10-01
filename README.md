OpenLMI documentation generator
===============================

Here you can find set of scripts, which take documentation from various OpenLMI
repositories and generate an overall document with all the docs.

The docs are stored in this git repository, so readthedocs.org can pull them
easily.


Prerequisities
--------------

During the processing, various cmake and make targets are called. Therefore
it's necessary to have all installed packages, that OpenLMI depends on.
Following list was gathered using ``yum-builddeps *.spec`` on Fedora 21:

* cmake
* plantuml
* graphviz
* tar
* dia
* cim-schema
* dbus-devel
* glib2-devel
* json-glib-devel
* konkretcmpi-devel
* konkretcmpi-python
* libselinux-devel
* libsemanage-devel
* libsss_simpleifp-devel
* systemd-devel
* libuser-devel
* libxml2-devel
* lm_sensors-devel
* pciutils-devel
* python-setuptools
* python-sphinx
* python-sphinx_rtd_theme
* python-devel
* sblim-cmpi-devel
* systemd-devel
* openlmi-providers (for class2rst and mof files in /usr/share/mof)
* python-IPy
* openwsman-python

Setup
-----

Run ``setup.sh``. It clones necessary repositories into ``_ext/``.

Usage
-----

Run ``build.sh``. It refreshes the repositories in ``_ext/`` directory
(``git pull``), reorganizes whatever is necesary (using ``_build/``) directory
and produces (huge) tree of .rst files in ``doc/``.

All changes in ``doc/``, incl. new files, must be checked into the repository,
so readthedocs.org can find it there.


Details
-------

* ``doc/python/`` is populated with python libraries we want to document
  (lmishell, openlmi-scripts, ...) and their dependencies (pywbem; it is not
  available on readthedocs.org builders).

* Links to figures in original .rst files are translated to appropriate parent
  directories. In other words, following is perfectly OK and it will be updated
  to point to the right file::


    .. figure:: pic/my.svg 
       :target: _static/my.svg

