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
# to wrote this script
#------------------------


try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup, find_packages


from Imagesat import *


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


DATA_FILES = [('config', ['cfg/imagesat_example.conf']),
              ('/usr/lib/systemd/system', ['cfg/system_d'])]
#DATA = [(join('share', 'habilitation') + sep + item[0], item[1]) for item in files('data')]
#DATA = [('bitmaps', [
#    'data/Images/Cadenas.png',
#    'data/Images/Casque.png',
#       ])]
#PACKAGES      = [ 'habilitation', ]
#
SCRIPTS = ['imagesat', ]

setup(
    name             = NAME,
    version          = VERSION,
    description      = DESCRIPTION,
    long_description = LONG_DESCRIPTION,
    author           = AUTHOR,
    author_email     = AUTHOR_EMAIL,
    url              = URL,
    license          = LICENSE,
    platforms        = PLATFORMS,
    data_files       = DATA_FILES,
#    data_files       = DATA,
#    packages_data    = {'habilitation': ['data/Images/*']},
#    packages         = PACKAGES,
    packages         = find_packages(),
    include_package_data = True,
    scripts          = SCRIPTS,
    requires         = ['requests', 'yaml', 'imaging', 'python (>=3.3)'],
    classifiers      = CLASSIFIERS,
)
