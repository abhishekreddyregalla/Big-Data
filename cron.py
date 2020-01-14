import os
import time
import logging
logging.basicConfig(filename="logfile.log", format='%(asctime)s %(message)s',filemode='w)
logger=logging.getLogger()
loggger.setLevel(logging.DEBUG)


logger.debug(print("Running"))
os.mkdir(str(int(time.time())))