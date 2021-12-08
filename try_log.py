import logging
import os
from datetime import datetime
from os.path import dirname, abspath


ROOT_DIR = dirname(abspath(__file__))
now = datetime.now()
name_file_log = str(now.strftime("%d %b %Y - %H %M %S"))+" test_log.log"


logging.basicConfig(filename=(ROOT_DIR+'\\logs_files\\' + name_file_log),
                    filemode='w',
                    format='%(name)s - %(levelname)s - %(message)s')

logging.warning('This will get logged to a file')
logging.warning('This will get logged to a file2')
logging.error('This will get logged to a file2')
logging.info('This will get logged to a file23')