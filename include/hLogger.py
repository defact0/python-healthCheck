#!/usr/local/bin/python

import logging


def initLog():
    logger = logging.getLogger("log")
    logger.setLevel(logging.DEBUG)

    # logging.Formatter('%(asctime)s:%(module)s:%(levelname)s:%(message)s', '%Y-%m-%d %H:%M:%S')
    formatter = logging.Formatter('%(asctime)s:%(message)s', '%Y-%m-%d %H:%M:%S')

    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    file_debug_handler = logging.FileHandler('./healthCheck.log')
    file_debug_handler.setLevel(logging.DEBUG)
    file_debug_handler.setFormatter(formatter)
    logger.addHandler(file_debug_handler)

    return logger
