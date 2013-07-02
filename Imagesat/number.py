# -*- coding: utf-8 -*-

"""
Imagesat: Daemon can download satellite images
Copyright (C) 2013 Julien Freyermuth
All Rights Reserved
This file is part of Imagesat.

See the file LICENSE for copying permission.
"""


def is_number(number):
    """
    This function return True if the parameter is en integer otherwise False
    """

    try:
        s = int(number)
        if s < 0:
            return False
        else:
            return True
    except ValueError:
        return False
