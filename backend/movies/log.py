import logging

INFO = logging.INFO

logging.basicConfig(level=logging.INFO,
                    format='[%(asctime)s]\t[%(levelname)s]    \t - %(message)s')
logger = logging.getLogger('ghibli')
