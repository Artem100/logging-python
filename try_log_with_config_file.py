import logging
import logging.config
import os
from datetime import datetime
from os.path import dirname, abspath


ROOT_DIR = dirname(abspath(__file__))

def logging_1():
    now = datetime.now()
    name_file_log = str(now.strftime("%d %b %Y - %H %M %S"))+" test_log1.txt"

    logging.config.fileConfig(fname='config.ini',
                              # defaults={'logfilename': (os.path.join(os.path.dirname(os.path.realpath(__file__)), 'logs_files', name_file_log))},
                              defaults={'logfilename': ROOT_DIR+name_file_log},
                              disable_existing_loggers=False)
    # Get the logger specified in the file
    logger = logging.getLogger("Mine")
    logger.info('This is a debug message 1')

def logging_2(name_log):
    now = datetime.now()
    name_file_log = str(now.strftime("%d %b %Y - %H %M %S"))+f" {name_log}.txt"

    logging.config.fileConfig(fname='config.ini',
                              defaults={'logfilename': (os.path.join(os.path.dirname(os.path.realpath(__file__)), 'logs_files', name_file_log))},
                              disable_existing_loggers=False)
    # Get the logger specified in the file
    logger = logging.getLogger("Mine")
    logger.info('This is a debug message 2')

# l1 = logging_1()
l2 = logging_2("dog")
l3 = logging_2("cat")