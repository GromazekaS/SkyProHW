import logging
from logging import Logger


def logger_setup(filename: str) -> Logger:
    logger = logging.getLogger(filename)
    file_handler = logging.FileHandler(f"../logs/{filename}.log", "w", encoding="utf-8")
    file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s: %(message)s")
    file_handler.setFormatter(file_formatter)
    logger.addHandler(file_handler)
    logger.setLevel(logging.DEBUG)
    return logger


