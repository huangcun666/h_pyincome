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
from Pagination import Pagination
logger = logging.getLogger('boilerplate.' + __name__)


class DisplayListHandler(BaseHandler):
    def get(self):

        tag = self.get_argument("tag", "all")
        uid = self.get_secure_cookie("uid")
        role = self.get_secure_cookie("role")
        uid_name = self.get_secure_cookie("name")

        if tag =="list":
            pre_page = 12
            page = int(self.get_argument("page", 1))

            count = self.db_ext.get(
                '''  select count(*) count from displaylist_articles
            ''')

            pagination = Pagination(page, pre_page, count.count, self.request)
            startpage = (page-1) * pre_page
            displaylist_articles = self.db_ext.query('''
                select * from displaylist_articles
                limit %s,%s 
                ''', startpage, pre_page)
            displaylist_node = self.db_ext.query(
                "select * from displaylist_node order by order_int")
            displaylist_category = self.db_ext.query(
                "select * from displaylist_category order by order_int")
            return self.render(
                'displaylist/list.html',
                pagination=pagination,
                displaylist_node=displaylist_node,
                displaylist_category=displaylist_category,
                displaylist_articles=displaylist_articles,
                search_key='',
            )
