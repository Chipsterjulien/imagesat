# -*-coding: utf-8 -*-

"""
Imagesat: Daemon can download satellite images
Copyright (C) 2013 Julien Freyermuth
All Rights Reserved
This file is part of Imagesat.

See the file LICENSE for copying permission.
"""

import sys
import os

from Imagesat.number import is_number
from Imagesat.mylog import logging


class Img_info:
    """
    This class store data of each picture
    """

    def __init__(self):
        self.base    = str() # Définit la chaine à rajouter à la recherche
        self.url     = str() # Contient l'adresse internet
        self.search  = str() # Définit la chaine à rechercher
        self._path   = str() # Définit l'emplacement pour la sauvegarde
        self._time   = int() # Définit le temps avant la mise à jour
        self._crop   = [] # Tableau contenant les dimensions à découper
        self._resize = [] # Tableau contenant les nouvelles dimensions de l'image

# Getter
    def _get_crop(self):
        return self._crop

    def _get_path(self):
        return self._path

    def _get_resize(self):
        return self._resize

    def _get_time(self):
        return self._time

# Setter
    def _set_crop(self, c):
        for val in c.split('x'):
            if is_number(val):
                self._crop.append(int(val))
            else:
                logging.critical("In " + self._path + " \"crop: " + c
                                 + "\" is incorrect !")
                sys.exit(2)

    def _set_path(self, p):
        (path, f) = os.path.split(p)
        if path == "":
            path = os.path.expanduser('~')

        if not os.access(path, os.W_OK):
            logging.critical("You don't have write permissions on \""
                             + self._path + "\" !")
            sys.exit(2)

        self._path = os.path.join(path, f)

    def _set_resize(self, r):
        for val in r.split('x'):
            if is_number(val):
                self._resize.append(int(val))
            else:
                logging.critical("In " + self._path + " \"resize: " + r
                                 + "\" is incorrect !")
                sys.exit(2)

    def _set_time(self, t):
        if is_number(t):
            self._time = t
        else:
            logging.critical("\"" + t + "\" is not a number gretter than 0 !")
            sys.exit(2)


    crop   = property(_get_crop, _set_crop)
    path   = property(_get_path, _set_path)
    resize = property(_get_resize, _set_resize)
    time   = property(_get_time, _set_time)
