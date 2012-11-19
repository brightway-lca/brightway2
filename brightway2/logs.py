# -*- coding: utf-8 -*-
from . import config
from logging.handlers import RotatingFileHandler
from utils import random_string
import codecs
import datetime
import logging
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


def get_io_logger(name):
    """Build a logger that records only relevent data for display later as HTML."""
    dirname = config.request_dir("logs")
    assert dirname, "No logs directory found"

    filepath = os.path.join(dirname, "%s.%s.log" % (name, random_string(6)))
    handler = logging.StreamHandler(codecs.open(filepath, "w", "utf-8"))
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    handler.setFormatter(logging.Formatter(u"%(message)s"))
    logger.addHandler(handler)
    return logger, filepath
