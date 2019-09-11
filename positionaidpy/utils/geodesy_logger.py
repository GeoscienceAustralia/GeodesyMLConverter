"""
Module: Geodesy Logger
"""

from os import path

import logging
import logging.config


class GeodesyLogger(object):

    logger = None
    config_file = path.join(path.dirname(path.abspath(__file__)), '.geodesy_logger.conf')
    logging_name = 'geodesy'

    @classmethod
    def setup(cls, config_file=None, logging_name=None):
        if cls.logger is None:
            the_config_file = cls.config_file if config_file is None else config_file
            the_logging_name = cls.logging_name if logging_name is None else logging_name

            logging.config.fileConfig(the_config_file)
            cls.logger = logging.getLogger(the_logging_name)
