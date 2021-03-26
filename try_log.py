import logging
import os
from datetime import datetime

now = datetime.now()
name_file_log = str(now.strftime("%d %b %Y - %H %M %S"))+" test_log.txt"


logging.basicConfig(filename=(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'logs_files', name_file_log)),
                    filemode='w',
                    format='%(name)s - %(levelname)s - %(message)s')

logging.warning('This will get logged to a file')
logging.warning('This will get logged to a file2')
logging.error('This will get logged to a file2')
logging.info('This will get logged to a file23')