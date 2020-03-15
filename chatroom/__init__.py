import logging
from logging.handlers import SysLogHandler





FORMATTER = logging.Formatter('%(asctime)s %(name)s %(message)s', datefmt = '%m/%d/%Y %I:%M:%S %p')
logger = logging.getLogger(__name__)

logger.setLevel(logging.INFO)
file_handler = logging.handlers.RotatingFileHandler('./log/chatroom.log', maxBytes = 1000000, backupCount = 3)
# file_handler = SysLogHandler('/var/log')
file_handler.setFormatter(FORMATTER)

stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.INFO)
stream_handler.setFormatter(FORMATTER)

logger.addHandler(file_handler)
logger.addHandler(stream_handler)
