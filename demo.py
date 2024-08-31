from US_visa.logger import logging
from US_visa.exception import USvisaException
import sys


# logging.info("Welcome to US visa project")

try:
    a = 1/0
except Exception as e:
    logging.info(e)
    raise USvisaException(e, sys)