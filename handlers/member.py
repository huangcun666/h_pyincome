# -*- coding: utf-8 -*-
from handlers.base import BaseHandler
import logging
import tornado
import tornado.httpclient
from Pagination import Pagination
from datetime import datetime
logger = logging.getLogger('boilerplate.' + __name__)

class MemberHandler(BaseHandler):
    @tornado.web.authenticated
    def post(self):
        tag = self.get_argument("tag")
        uid = self.get_secure_cookie('uid')
        if tag =="add":

            team_name = self.get_argument("team_name")
            member_id = self.get_argument("member_id")
            member_name = self.get_argument("memeber_name")
            project_id = self.get_argument("project_id")
            category_name = self.get_argument('category_name')
            order_int = self.get_argument('order_int',0)
            if not category_name:
                self.write("not category name")
            else:
                result = self.db.execute("insert into t_projects_category(category_name,uid,order_int) values(%s,%s,%s)",
                category_name,uid, order_int)
                all_categorys=self.db.query('''
                    select * from  t_projects_category  where uid=%s  order by order_int desc,id desc 
                    ''',uid)
                self.write({'all_categorys':all_categorys,'id':result})



