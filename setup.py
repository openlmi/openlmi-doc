from setuptools import setup, find_packages
import os
import sys

setup(
    name='openlmi-doc',
    description='OpenLMI documentation',
    author='Jan Safranek',
    author_email='jsafrane@redhat.com',
    url='https://fedorahosted.org/openlmi/',
    version='0.7.1',
    package_dir={'': 'doc/python'},
    packages=find_packages('doc/python'),
    classifiers=[
        'License :: OSI Approved :: GNU Lesser General Public License v2 or later (LGPLv2+)',
        'Operating System :: POSIX :: Linux',
        'Topic :: System :: Systems Administration',
    ],
)
