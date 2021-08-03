__author__ = 'Sudhir'

'''
Purpose : Initialization of the Logger
'''

import logging
import datetime
import os

cur_time = datetime.datetime.now()
fpath = "database/logs/"

if not os.path.exists(fpath):
	os.makedirs(fpath)

LOG_FILENAME = fpath+cur_time.strftime('%Y-%m-%d %H:%M:%S')+'_LOG.log'

FORMAT = '%(asctime)s %(name)s %(funcName)s Line:%(lineno)d %(levelname)s - %(message)s'
logging.basicConfig(filename = LOG_FILENAME, filemode='a' ,level = logging.ERROR, format = FORMAT, datefmt='%m/%d/%Y %I:%M:%S %p')
#In the above line set level to DEBUG while testing locally, in Prod the level should always be ERROR

#initialize the logger
logger = logging.getLogger(__name__)
