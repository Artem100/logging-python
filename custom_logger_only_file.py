import logging
import pathlib

logger = logging.getLogger(__name__)
logger.propagate = False
logger.setLevel(logging.DEBUG)
f_handler = logging.FileHandler(f'{pathlib.Path(__file__).parent.resolve()}\\lalalalala.log')
f_handler.setLevel(logging.DEBUG)
logger.addHandler(f_handler)


logger.debug("hello!")