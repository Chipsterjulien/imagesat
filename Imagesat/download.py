# -*- coding: utf-8 -*-

"""
Imagesat: Daemon can download satellite images
Copyright (C) 2013 Julien Freyermuth
All Rights Reserved
This file is part of Imagesat.

See the file LICENSE for copying permission.
"""

import os
import requests
import time


def download(url):
    """
    This function dowload an url who's given in parameter
    """

    page = str()
    try:
        page = requests.get(url)
    except requests.exceptions.ConnectionError:
        time.sleep(10)
        # The only way to reinitalize correctly the internet connection
        os.execl('/usr/bin/imagesat', 'imagesat')

    return page
