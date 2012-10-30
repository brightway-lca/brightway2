# -*- coding: utf-8 -*
from . import config
import datetime
import logging
from logging.handlers import RotatingFileHandler
import os


def get_logger(name, add_datetime=True, level=logging.INFO):
    now = datetime.datetime.now()
    filename = "%s-%s.log" % (name, now.strftime("%d-%B-%Y-%I-%M%p"))
    handler = RotatingFileHandler(os.path.join(config.dir, 'logs', filename),
        maxBytes=50000, encoding='utf-8', backupCount=5)
    formatter = logging.Formatter(
        "%(asctime)s %(levelname)s %(lineno)d %(message)s")
    logger = logging.getLogger("name")
    logger.setLevel(level)
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    return logger
