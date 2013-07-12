#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Imagesat: Daemon can download satellite images
Copyright (C) 2013 Julien Freyermuth
All Rights Reserved
This file is part of Imagesat.

See the file LICENSE for copying permission.
"""


#------
# Used http://www.python.org/dev/peps/pep-0314/ and
# http://getpython3.com/diveintopython3/packaging.html
#
# https://pypi.python.org/pypi?%3Aaction=list_classifiers
#
# to wrote this script
#------------------------


try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup, find_packages


import Imagesat


CLASSIFIERS = [
    'Development Status :: 5 - Production/Stable',
    'Environment :: Console',
    'Intended Audience :: System Administrators',
    'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
    'Natural Language :: English',
    'Operating System :: POSIX :: Linux',
    'Programming Language :: Python :: 3',
    'Topic :: Internet',
]


DATA_FILES = [('/etc/imagesat', ['cfg/imagesat_example.conf']),
              ('/usr/lib/systemd/system', ['cfg/imagesat.service'])]
SCRIPTS = ['imagesat', ]


setup(
    name             = Imagesat.__name__,
    version          = Imagesat.__version__,
    description      = Imagesat.__description__,
    long_description = Imagesat.__long_description__,
    author           = Imagesat.__author__,
    author_email     = Imagesat.__author_email__,
    url              = Imagesat.__url__,
    license          = Imagesat.__license__,
    platforms        = Imagesat.__platforms__,
    data_files       = DATA_FILES,
    packages         = find_packages(),
    include_package_data = True,
    scripts          = SCRIPTS,
    requires         = ['requests', 'pyyaml', 'imaging', 'python (>=3.3)'],
    classifiers      = CLASSIFIERS,
)
