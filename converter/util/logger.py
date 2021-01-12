import logging


def create_logger(name, level=logging.DEBUG):
    logger = logging.getLogger(name)

    handler = logging.StreamHandler()
    formatter = logging.Formatter('%(asctime)s %(levelname)-8s %(message)s')
    handler.setFormatter(formatter)

    logger.addHandler(handler)
    logger.setLevel(level)

    return logger
