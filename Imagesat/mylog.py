#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
My log file:
It saves in log files and display them to console

Thanks to http://sametmax.com/ecrire-des-logs-en-python/
"""

import logging
from logging.handlers import RotatingFileHandler

# Create the log object
logger = logging.getLogger()
# Set the level to DEBUG
logger.setLevel(logging.DEBUG)

# Create a design for log format
formatter = logging.Formatter('%(asctime)s :: %(levelname)s :: %(message)s')
# Create a file handler in append mode with 1 backup and 1Mo for max size
#file_handler = RotatingFileHandler('activity.log', 'a', 1000000, 1)
# Set the level to DEBUG
#file_handler.setLevel(logging.DEBUG)
# Applying formatter
#file_handler.setFormatter(formatter)
# Append to logger object
#logger.addHandler(file_handler)

# Create a 2nde file handler
steam_handler = logging.StreamHandler()
# Set the level to DEBUG
steam_handler.setLevel(logging.DEBUG)
# Append to logger object
logger.addHandler(steam_handler)
