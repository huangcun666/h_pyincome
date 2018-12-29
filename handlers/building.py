# -*- coding: utf-8 -*-
from handlers.base import BaseHandler
import logging
import tornado
import tornado.httpclient
import os
import random
import string
import re
import hashlib
from Pagination import Pagination
from datetime import datetime
logger = logging.getLogger('boilerplate.' + __name__)


class BuidlingHandler(BaseHandler):
    @tornado.web.authenticated
    def get(self):
        tag = self.get_argument("tag")
        if tag == "show":
            customer_id = self.get_argument("customer_id")
            customer_name = self.get_argument("customer_name","")
            print customer_name, customer_id
            if  customer_id:
                t_customer = self.db_building.get(
                    "select a.*,b.name uid_name from t_customer a , t_user b where a.uid=b.id and qid=%s ",
                    customer_id)
            elif customer_name:
                t_customer = self.db_building.get(
                    "select a.*,b.name uid_name from t_customer a , t_user b where a.uid=b.id and company=%s ",
                    customer_name)


            if not t_customer:
                return self.write("0")
            else:
                t_customer_state = self.db_building.query(
                    "select a.*,b.name updated_uid_name from t_customer_state a inner join t_user b  on a.updated_uid=b.id  where customer_id=%s order by created_at ",
                    t_customer.id)

            return self.render(
                "building/show_to_income.html", t_customer_state=t_customer_state)
