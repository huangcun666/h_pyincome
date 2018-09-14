# -*- coding: utf-8 -*-
from handlers.base import BaseHandler
import urllib
import json
import datetime
import time
import logging
import tornado
import tornado.httpclient
import os
import random
import string
import re
import hashlib
logger = logging.getLogger('boilerplate.' + __name__)
from Pagination import Pagination

class GuestBookHandler(BaseHandler):
    # @tornado.web.authenticated
    # def get(self):
    #     page= int(self.get_argument("page",1))
    #     pre_page=10
    #     count =self.db.get('''SELECT count(*) count FROM t_user
    #        ''')
    #     pagination = Pagination(page, pre_page, count.count, self.request)
    #     startpage = (page-1) * pre_page
    #     t_user_sites = self.db.query('''
    #         SELECT  *  FROM t_user_site
    #         order by created_at desc limit %s,%s
    #         ''',startpage,pre_page)

    #     t_temp = self.db.query("""
    #         select * from t_temp order by order_int desc
    #         """)

    #     return self.render('admin/sites.html',pagination=pagination,t_user_sites=t_user_sites,
    #         t_temp=t_temp)

    def post(self):
        #uid = self.get_secure_cookie("site_id")
        site_id = self.get_argument("site_id")
        name = self.get_argument("name")
        email = self.get_argument("email")
        msg = self.get_argument("msg")
        id = self.db.execute("""
           INSERT INTO `t_guest_book` ( `name`, `email`, `msg`, `created_at`, `site_id`)
           VALUES
                (%s, %s, %s, now(), %s);
            """,name,email,msg,site_id )

        self.write("1")