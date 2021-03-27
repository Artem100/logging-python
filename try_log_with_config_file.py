import logging
import logging.config
import os
from datetime import datetime

def logging_1():
    now = datetime.now()
    name_file_log = str(now.strftime("%d %b %Y - %H %M %S"))+" test_log1.txt"

    logging.config.fileConfig(fname='config.ini',
                              defaults={'logfilename': (os.path.join(os.path.dirname(os.path.realpath(__file__)), 'logs_files', name_file_log))},
                              disable_existing_loggers=False)
    # Get the logger specified in the file
    logger = logging.getLogger("Mine")
    logger.info('This is a debug message 1')

def logging_2():
    now = datetime.now()
    name_file_log = str(now.strftime("%d %b %Y - %H %M %S"))+" test_log2.txt"

    logging.config.fileConfig(fname='config.ini',
                              defaults={'logfilename': (os.path.join(os.path.dirname(os.path.realpath(__file__)), 'logs_files', name_file_log))},
                              disable_existing_loggers=False)
    # Get the logger specified in the file
    logger = logging.getLogger("Mine")
    logger.info('This is a debug message 2')

l1 = logging_1()
l2 = logging_2()