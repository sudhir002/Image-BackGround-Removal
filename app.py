__author__ = 'Sudhir'
__date__ = "Aug 3 - 2021"

'''
Purpose : defined the apis.
'''

import os
import sys
import json
import logging
from init_log import logger
from flask_config import application
from flask import request, send_file
import misc.common_functions as cf


logger = logging.getLogger("app.py")



@application.route('/imgbackremoval', methods=['POST'])
def background_removal():
    try:
        if request.method == "POST":
            input_img_folder = os.path.abspath("") + "/database/static/inputimg/"
            if not os.path.exists(input_img_folder):
                os.makedirs(input_img_folder)
            application.config['input_img_folder'] = input_img_folder
            images = request.files.getlist("myfiles")
            if not images[0].filename:
                return "not valid images"
            imgname = []
            for img in images:
                if img.filename.rsplit(".", 1)[1].lower() not in ['jpg', 'png', 'jpeg']:
                    return "not valid images"
                else:
                    imgname.append(img.filename)
            imgsave = [img.save(os.path.join(application.config['input_img_folder'], img.filename)) for img in images]
            cf.add_img_to_queue(imgname)
            return json.dumps({"code": 200, "msg": "data recorded"})
    except Exception as e:
        logger.error("Exception in background_removal:" + str(repr(e)) + " line number " + str(sys.exc_info()[-1].tb_lineno))
        return json.dumps({"code": 400, "msg": "something went wrong"})


@application.route('/processesdata', methods=['GET'])
def processesdata():
    try:
        data = cf.processesdata()
        return json.dumps({"code": 200, "data": data})
    except Exception as e:
        logger.error("Exception in processesdata:" + str(repr(e)) + " line number " + str(sys.exc_info()[-1].tb_lineno))
        return json.dumps({"code": 400, "msg": "something went wrong"})


@application.route('/imageserve', methods=['GET'])
def imageserve():
    try:
        folder = request.args.get("p")
        name = request.args.get("n")
        filename = os.path.abspath("") + "/database/static/{}/{}".format(folder, name)
        return send_file(filename, mimetype='image/gif')
    except Exception as e:
        logger.error("Exception in imageserve:" + str(repr(e)) + " line number " + str(sys.exc_info()[-1].tb_lineno))
        return json.dumps({"code": 400, "msg": "something went wrong"})


if __name__ == '__main__':
    # Development server
    application.run(host='0.0.0.0', port=5000, threaded=True)
