# logger_config.py
import logging

log_format = "%(levelname)s [%(asctime)s] - %(name)s - %(message)s"
logging.basicConfig(level=logging.INFO, format=log_format)


def get_logger(name):
    return logging.getLogger(name)
