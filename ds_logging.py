import logging
import sys

logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
#stream = logging.StreamHandler(sys.stdout)
#logger.addHandler(stream)
#formatter = logging.Formatter('[%message]s')
#stream.setFormatter(formatter)

