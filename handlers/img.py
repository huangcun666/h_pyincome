# -*- coding: utf-8 -*-
from handlers.base import BaseHandler
import logging
logger = logging.getLogger('boilerplate.' + __name__)
import tornado
import re
import os
import random
import string
from tornado import template
import uuid,os
from datetime import datetime

class ImageHandler(BaseHandler):
    @tornado.web.authenticated
    def get(self):
        uid = self.get_secure_cookie("uid")
        imgs = self.db.query("""select * from t_img  where  uid=%s""",uid)
        self.render("img/imgs.html",imgs=imgs)
    @tornado.web.authenticated
    def post(self):
        dt = datetime.now().strftime("%Y%m%d")
        site_id = self.get_argument("site_id")
        file1 = self.request.files['file1'][0]
        save_path = "media/public/%s/%s/"%(site_id,dt)
        url_path = "static/public/%s/%s/"%(site_id,dt)
        original_fname = file1['filename']
        try:
            os.makedirs(save_path)
        except OSError:
            if not os.path.isdir(save_path):
                raise
        extension = os.path.splitext(original_fname)[1]
        fname = ''.join(random.choice(string.ascii_lowercase + string.digits) for x in range(6))
        final_filename= str(uuid.uuid4())+extension

        output_file = open(save_path + final_filename, 'w')
        output_file.write(file1['body'])
        self.finish({ "link": url_path + final_filename})




        # file = self.get_argument.files['file']
        # file_type= "photo"
        # extension = os.path.splitext(file.filename)[1]

        # if file_type is 'photo':
        #     type_list = ['.png','.jpg','.jpeg','.gif']
        # msg = "0"
        # file_name_full=""
        # if extension in type_list:
        #         file_name = ''.join(random.choice(string.ascii_lowercase + string.digits) for x in range(16))
        #         file_name_full =  file_name + extension
        #         output_file = open("media/public/" + file_name_full, 'wb')
        #         output_file.write(file.body)
        #         msg = "1"