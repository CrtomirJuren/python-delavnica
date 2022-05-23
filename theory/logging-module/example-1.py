import sys
import logging

# create logger object
logger = logging.getLogger(__name__)

# set logger level
# logger.setLevel(logging.CRITICAL) # only shows critical
# logger.setLevel(logging.WARNING)  # doesnt show debug, info
# logger.setLevel(logging.INFO)     # doesnt show debug
logger.setLevel(logging.DEBUG)     # shows all messages

# set logger print formatting
date_strftime_format = "%H:%M:%S"
message_format = "%(asctime)s - %(levelname)s - %(message)s"
logging.basicConfig(format= message_format, datefmt= date_strftime_format, stream=sys.stdout)

if __name__ == "__main__":
    logger.info("Hello info")
    logger.critical("Hello critical")
    logger.warning("Hello warning")
    logger.debug("Hello debug")