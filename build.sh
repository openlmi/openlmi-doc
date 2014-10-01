#!/bin/bash -x
#
# Copyright (C) 2014 Red Hat, Inc.
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

# This script prepares the doc/ directory in order to generate OpenLMI
# documentation out of it. It expects _ext/ is populated with git
# repositories, as created by setup.sh

function usage()
{
    cat <<_EOF_
Usage:  build.sh [-P] [-b]
    -P          Do not refresh the repositories in _ext/ with 'git pull'.
    -b          Build the populated doc/ directory with sphinx.
_EOF_
    exit $1
}


DO_PULL=1
DO_BUILD=0
while getopts "Pbh" opt; do
    case $opt in
        P)
            DO_PULL=0
            ;;
        b)
            DO_BUILD=1
            ;;
        h)
            usage 0
            ;;
        \?)
            echo "Invalid option"
            usage 1
            ;;
    esac
done

# Crash on first error!
set -e

if [ $DO_PULL == "1" ]; then
    # Update the submodules to the latest HEAD
    for i in _ext/openlmi-providers _ext/openlmi-networking _ext/openlmi-storage _ext/openlmi-tools _ext/openlmi-scripts; do
        pushd $i
        git pull
        popd
    done
fi

# Prepare directories
rm -rf _build/providers _build/networking _build/mof
mkdir _build/providers _build/networking _build/mof

#######################################################
# openlmi-providers
#######################################################
# Generate rst and pictures
pushd _build/providers
cmake ../../_ext/openlmi-providers
make doc-prep
popd

# Copy docs to the right place
# (copy all directories except CMakeFiles)
find _build/providers/doc/admin -maxdepth 1 -type d ! -name "CMakeFiles" ! -name "admin" -exec cp -rv {} doc/openlmi-providers \;

# Copy MOF files to the right place
cp -v _ext/openlmi-providers/mof/*.mof _build/mof/
cp -v _build/providers/mof/60_LMI_Software.mof _build/mof/
# Remove provider-specific classes
rm -v _build/mof/60_LMI_Service-legacy.mof
# Remove useless classes and instances
rm -v _build/mof/*MethodParameters* _build/mof/*IndicationFilters*

# install python sources
export PYTHONPATH=$PWD/_build/python:$PYTHONPATH
pushd _ext/openlmi-providers/src/python
python setup.py install --root=../../../../_build/python
popd

#######################################################
# openlmi-networking
#######################################################

# Copy docs to the right place
cp -v _ext/openlmi-networking/doc/admin/*.rst doc/openlmi-networking
mkdir -p doc/openlmi-networking/pic
cp -v _ext/openlmi-networking/doc/admin/pic/*.svg doc/openlmi-networking/pic


# Copy MOF files to the right place
cp -v _ext/openlmi-networking/mof/60_LMI_Networking.mof _build/mof/


#######################################################
# openlmi-storage
#######################################################
# Generate pictures
export PATH=$PWD/_ext/openlmi-providers/tools:$PATH
pushd _ext/openlmi-storage/doc/admin
make generated figures
popd

# Copy docs to the right place
cp -rv _ext/openlmi-storage/doc/admin/{*.rst,generated,pic} doc/openlmi-storage
find doc/openlmi-storage/ -name .gitignore -exec rm {} \;

# Copy MOF files to the right place, excluding the master 60_* one
cp -v _ext/openlmi-storage/mof/LMI_Storage*.mof _build/mof/

# Remove useless classes and instances
rm -v _build/mof/*MethodParameters*
# Remove classes.rst, we have class reference on the top level
rm -v doc/openlmi-storage/classes.rst

#######################################################
# openlmi-scripts - prep
#######################################################
# link it to openlmi-tools
ln -sf $PWD/_ext/openlmi-scripts _ext/openlmi-tools/doc/

#######################################################
# openlmi-tools
#######################################################

pushd _ext/openlmi-tools/
find . -name "*.skel" -exec touch {} \;
touch doc/src/genapi.sh
make setup
popd

pushd _ext/openlmi-tools/doc/src
OPENLMI_SCRIPTS_DIR=$PWD/../openlmi-scripts WITH_COMMANDS=1 make deps-rtd index-rtd
popd

# Copy docs to the right place
rsync -avL _ext/openlmi-tools/doc/src/* doc/openlmi-tools/ --exclude=Makefile --exclude="*.py" --exclude="*.skel" --exclude="*.sh"

# install python sources
export PYTHONPATH=$PWD/_build/python:$PWD/_build/python/lmi:$PYTHONPATH
pushd _ext/openlmi-tools/cli
make
python setup.py install --root=../../../_build/python
popd

#######################################################
# openlmi-scripts - cont.
#######################################################
pushd _ext/openlmi-scripts
make setup-all
for i in commands/*; do
    if [ -d $i ]; then
        pushd $i
        python setup.py install --root=../../../../_build/python/
        popd
    fi
done
popd

cp -vr _build/python/usr/lib/py*/site-packages/lmi doc/python
touch doc/python/lmi/__init__.py doc/python/lmi/scripts/__init__.py

#######################################################
# pywbem
#######################################################
# We need pywbem to be available in git, it's not on readthedocs.org
# Ignore error when the package is already installed
pip -v install -I -t  doc/python/ --allow-external pywbem   pywbem || :


#######################################################
# Update image hyperlinks
#######################################################
# Every provider is in its own subdirectory. We need to
# update all links to images to add '../'
find doc/openlmi-storage -name "*.rst" -exec sed -i -e 's!\(\:target\:.*\)_images!\1../_images!' {} \;
find doc/openlmi-providers -name "*.rst" -exec sed -i -e 's!\(\:target\:.*\)_images!\1../../_images!' {} \;

#######################################################
# Generate it
#######################################################

# generate class reference
pushd doc/mof
PATH=../../_ext/openlmi-providers/tools:$PATH make
popd

if [ "$DO_BUILD" == "1" ]; then
    pushd doc
    rm -rf _build
    PYTHONPATH=python/:$PYTHONPATH make html
    popd
fi
