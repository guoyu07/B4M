#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -*- author: chat@jat.email -*-

import os
import logging

from flask import safe_join, current_app


def filter_cofig(config):
    return {k.replace('-', '_').upper(): v for k, v in config.items()}


def set_log(log_level, log_file):
    stream_handler = logging.StreamHandler()
    file_handler = logging.FileHandler(log_file, 'a', 'utf-8')

    formatter = logging.Formatter(
        '%(levelname)s %(asctime)s %(name)s %(message)s', '%Y-%m-%d %H:%M:%S')

    stream_handler.setFormatter(formatter)
    file_handler.setFormatter(formatter)

    logger = logging.getLogger()

    logger.addHandler(stream_handler)
    logger.addHandler(file_handler)

    logger.setLevel({
        'CRITICAL': logging.CRITICAL,
        'ERROR': logging.ERROR,
        'WARNING': logging.WARNING,
        'DEBUG': logging.DEBUG,
    }.get(log_level.upper(), logging.INFO))


def path_join(*path):
    return os.path.join(current_app.root_path, *path)


def safe_path_join(directory, filename):
    filename = safe_join(directory, filename)
    if not os.path.isabs(filename):
        filename = path_join(filename)

    return filename
