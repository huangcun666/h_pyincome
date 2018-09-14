# encoding=utf8
from handlers.base import BaseHandler
import logging
import json
import tornado.web
import urllib2
import tornado.httpclient
import sys, re,uuid
import urllib, os
from tornado.options import define, options
import qrcode
reload(sys)
sys.setdefaultencoding('utf8')
from Pagination import Pagination
logger = logging.getLogger('boilerplate.' + __name__)


#确认单
class MobileHandler(BaseHandler):
    def get(self):
        tag = self.get_argument("tag")
        name = self.get_secure_cookie("name")
        uid = self.get_secure_cookie("uid")
        if not name:
            self.redirect("/login?mobile=1")
        if tag == "uploader_trans":

            id  = self.get_argument("id")
            guid = self.get_argument("guid")
            trans_id=self.get_argument('trans_id')
            t_customer = self.db.get("select * from t_projects where id =%s",id )

            self.render("mobile/uploader_trans.html", t_customer=t_customer,trans_id=trans_id,)

        elif tag =="home":

            self.render(
                "mobile/home.html",
            )
        elif tag == "tel":
            t_company = self.db_company.query("select * from t_company where sales_uid=%s order by sales_uid_at desc limit 15",uid)
            self.render("mobile/tel.html", t_company=t_company)


#客户管理MobileHandler
class CustomerMobileHandler(BaseHandler):
    def get(self):
        tag = self.get_argument("tag")
        name = self.get_secure_cookie("name")
        if not name:
            self.redirect("/login?mobile=1")

        if tag == "uploader_trans":
            id = self.get_argument("id")
            guid = self.get_argument("guid")
            trans_id = self.get_argument('trans_id')
            t_customer = self.db.get("select * from t_customer where id =%s",
                                     id)

            self.render(
                "mobile/uploader_trans.html",
                t_customer=t_customer,
                trans_id=trans_id,
            )
