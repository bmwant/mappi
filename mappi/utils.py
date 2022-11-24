import logging

logging.disable(level=logging.CRITICAL)

# if config.DEBUG:
if True:
    logging.disable(logging.NOTSET)
    logging.basicConfig(level=logging.DEBUG)


logger = logging.getLogger(__package__)
