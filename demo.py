from hatespeech.logger import logging
from hatespeech.exception import CustomException
import sys

# logging.info("Welcome to our Project")

try:
    a = 7 / 2

except Exception as e:
    raise CustomException(e, sys) from e