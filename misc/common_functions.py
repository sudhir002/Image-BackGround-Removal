__author__ = 'Sudhir'
__date__ = "Aug 3 - 2021"

'''
Purpose : kafka producer.
'''


'''
Purpose : Common functions used in the application.
'''

import sys
import json
import logging
import appsetup.dataconnect as dc
from kafka import KafkaProducer

#initialize the logger
logger = logging.getLogger("common_functions.py")
host = "http://localhost:5000/"
producer = KafkaProducer(bootstrap_servers=['localhost:9092'], value_serializer=lambda x: json.dumps(x).encode('utf-8'))
def add_img_to_queue(imgname):
	try:
		collection = dc.mongodb()["bg_removal"]
		nosql_format = []
		for each in imgname:
			nosql_format.append({"input_image_path": "/database/static/inputimg/{}".format(each),
								 "output_image_path": "/database/static/outputimg/op_{}".format(each.rsplit(".", 1)[0]+".png"),
								 "status": "pending"})
		x = collection.insert_many(nosql_format)
		processid = [str(i) for i in x.inserted_ids]
		producer.send('input_img_data_pipeline', value=processid)
	except Exception as e:
		logger.error("Exception in add_img_to_queue:" + str(repr(e)) + " line number " + str(sys.exc_info()[-1].tb_lineno))
		return "error"


def processesdata():
	try:
		collection = dc.mongodb()["bg_removal"]
		data = list(collection.find({}, {"_id":0}))
		res = []
		for x in data:
			x["input_image_path"] = x["input_image_path"].rsplit("/", 1)[1]
			x["output_image_path"] = host + "imageserve?p=outputimg&n={}".format(x["output_image_path"].rsplit("/", 1)[1])
			res.append(x)
		return res[::-1]
	except Exception as e:
		logger.error("Exception in misc.processesdata:" + str(repr(e)) + " line number " + str(sys.exc_info()[-1].tb_lineno))
		return "error"