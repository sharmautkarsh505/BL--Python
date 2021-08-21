import logging
import os

def set_logger():
    
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s:%(filename)s:%(levelname)s:%(message)s')

    if not os.path.exists('Logs'):
        os.makedirs('Logs')
    else:
        file_handler = logging.FileHandler('Logs/caldr.log')
        file_handler.setLevel(logging.INFO)
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

    return logger
