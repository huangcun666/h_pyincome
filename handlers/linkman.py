# encoding=utf8
from handlers.base import BaseHandler
import logging
import json
import tornado.web
import urllib2
import tornado.httpclient
import sys, re
import urllib
reload(sys)
sys.setdefaultencoding('utf8')

logger = logging.getLogger('boilerplate.' + __name__)


#客户
class LinkmanHandler(BaseHandler):
    @tornado.web.authenticated
    def post(self):
        tag = self.get_argument("tag", "list")
        uid = self.get_secure_cookie("uid")
        uid_name = self.get_secure_cookie("name")
        result = -10
        if tag == "add":

            name = self.get_argument("name")
            customer_id = self.get_argument("customer_id")
            tel = self.get_argument("tel","")
            remark = self.get_argument("remark","")
            gender = self.get_argument("gender")
            if not name:
                self.write("联系人的名字不能为空")
            else:
                result = self.db_customer.execute(
                    """insert into t_linkman (name,tel,gender,remark,acc_uid,acc_uid_name,created_at,updated_at,guid,customer_id)
                
                values(%s,%s,%s,%s,%s,%s,now(),now(),uuid(),%s)""", name, tel,
                    gender, remark, uid, uid_name, customer_id)


            self.write(str(result))

        elif tag =="delete":
            id = self.get_argument("id")
            guid = self.get_argument("guid")

            if not id:
                self.write("id")
            else:
                result = self.db_customer.execute("delete from t_linkman where id=%s and guid=%s",id,guid)
                self.write(str(result))