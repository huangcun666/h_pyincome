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


def insert_new(self, uid, txt, msg_type=1):

    self.db.execute(
        "insert into t_user_msg(uid,txt,created_at,read_at,is_read,msg_type) values(%s,%s,now(),now(),0,%s)",
        uid, txt,msg_type)


def insert_new_group(self,  txt, msg_type, role):

    self.db.execute(
        """insert into t_user_msg(uid,txt,created_at,read_at,is_read,msg_type) 
        select  id,%s,now(),now(),0,%s from t_user where role=%s and is_lock=0""",
         txt, msg_type, role)


class MsgHandler(BaseHandler):
    @tornado.web.authenticated
    def get(self):
        tag = self.get_argument("tag", "list")
        uid = self.get_secure_cookie("uid")
        uid_name = self.get_secure_cookie("name")
        role = self.get_secure_cookie("role")
        if tag == "list":
            tmp_html="msg/msg_list.html"
            page = int(self.get_argument("page", 1))
            pre_page = 30
            count = self.db.get(
                '''SELECT count(*) count FROM t_user_msg a , t_user b where a.uid=b.id and uid=%s
               ''', uid)
            pagination = Pagination(page, pre_page, count.count, self.request)
            startpage = (page - 1) * pre_page
            t_user_msg = self.db.query('''
                SELECT  a.* , b.name  FROM t_user_msg a , t_user b where a.uid=b.id and uid=%s
                order by created_at desc limit %s,%s
                ''',uid, startpage, pre_page)
         
            self.db.execute("update t_user_notify set msg_count=0 where uid=%s",uid)
            return self.render(
                tmp_html,
                pagination=pagination,
                t_user_msg=t_user_msg,
                form_tag="list",search_key="")

        elif tag == "group":
            page = int(self.get_argument("page", 1))
            pre_page = 30

            count = self.db.get(
                '''SELECT count(*) count FROM t_user_msg a , t_user b where a.uid=b.id and uid=%s and msg_type=2
               ''', role)
            pagination = Pagination(page, pre_page, count.count, self.request)
            startpage = (page - 1) * pre_page
            t_user_msg = self.db.query('''
                SELECT  a.* , b.name  FROM t_user_msg a , t_user b where a.uid=b.id and uid=%s and msg_type=2
                order by created_at desc limit %s,%s
                ''', role, startpage, pre_page)

            self.db.execute(
                "update t_user_notify set msg_count=0 where uid=%s and msg_type=2",
                role)
            return self.render(
                'msg/msg_list.html',
                pagination=pagination,
                t_user_msg=t_user_msg,
                form_tag="list",
                search_key="")

        elif tag =="getnotify":


            msg_count = self.db.get("select msg_count from t_user_notify where uid=%s ",uid)
            if msg_count:
                self.write(str(msg_count.msg_count))
            else:
                self.write("0")