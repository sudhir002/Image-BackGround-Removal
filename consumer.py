import logging
import json, sys, os
from kafka import KafkaConsumer
import appsetup.dataconnect as dc
from json import loads
from bson import ObjectId
from rembg.bg import remove
import numpy as np
import io
from PIL import Image


logger = logging.getLogger("app.py")
collection = dc.mongodb()["bg_removal"]


def bgremoval(id):
    try:
        data = list(collection.find({"_id": ObjectId(id)}, {"output_image_path":1, "input_image_path":1, "_id":0}))
        input_path = os.path.abspath("") + data[0]["input_image_path"]
        output_path = os.path.abspath("") + data[0]["output_image_path"]
        f = np.fromfile(input_path)
        result = remove(f)
        img = Image.open(io.BytesIO(result)).convert("RGBA")
        img.save(output_path)
        return "success"
    except Exception as e:
        logger.error("Exception in consumer:" + str(repr(e)) + " line number " + str(sys.exc_info()[-1].tb_lineno))
        return "error"

try:
    consumer = KafkaConsumer(
        'input_img_data_pipeline',
         bootstrap_servers=['localhost:9092'],
         auto_offset_reset='earliest',
         enable_auto_commit=True,
         group_id='my-group',
         value_deserializer=lambda x: loads(x.decode('utf-8')))
    for msg in consumer:
        message = msg.value
        for x in message:
            sts = bgremoval(x)
            if sts != "error":
                collection.update_one({"_id": ObjectId(x)}, { "$set": {"status": "completed"}})
            else:
                collection.update_one({"_id": ObjectId(x)}, { "$set": {"status": "error"}})
except Exception as e:
    logger.error("Exception in consumer:" + str(repr(e)) + " line number " + str(sys.exc_info()[-1].tb_lineno))
