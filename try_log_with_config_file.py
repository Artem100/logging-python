import logging
import logging.config
import os
from datetime import datetime

now = datetime.now()
name_file_log = str(now.strftime("%d %b %Y - %H %M %S"))+" test_log.txt"

logging.config.fileConfig(fname='config.ini',
                          defaults={'logfilename': (os.path.join(os.path.dirname(os.path.realpath(__file__)), 'logs_files', name_file_log))},
                          disable_existing_loggers=False)
# Get the logger specified in the file
logger = logging.getLogger("Mine")
logger.info('This is a debug message')