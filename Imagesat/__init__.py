# -*- coding: utf-8 -*-

######################################################################
# Copyright (C) 2013 Julien Freyermuth
# All Rights Reserved
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
######################################################################


__author__           = "Julien Freyermuth"
__author_email__     = "julien [dote] chipster [hate] gmail [dote] com"
__copyright__        = "Copyright (c) 2013, Julien Freyermuth"
__description__      = "Daemon can download satellite images"
__long_description__ = """It's a python's script who download some pictures  \
        into /tmp directory (see imagesat_example.conf) and you can display  \
        them with conky or conky like (dzen2, ...). This script can search,  \
        with regexp, a picture to download on html page, even name of  \
        picture change all the time"""
__license__          = "GPLv3"
__name__             = "imagesat"
__platforms__        = "GNU/Linux"
__url__              = "https://github.com/Chipsterjulien/imagesat"
__version__          = '0.3.1'
__version_info__     = (0, 3, 1, '', 0)


from .download import download
from .img_info import Img_info
from .mylog import *
from .number import is_number
