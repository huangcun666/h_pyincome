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
class ContractHandler(BaseHandler):
    @tornado.web.authenticated
    def post(self):
        tag = self.get_argument("tag", "list")
        uid = self.get_secure_cookie("uid")
        uid_name = self.get_secure_cookie("name")
        result = -10
        if tag == "add":
            contract_id = int(self.get_argument("contract_id",0))
            title = self.get_argument("contract_title")
            customer_id = self.get_argument("customer_id")
            print "customer_id", customer_id
            start_time = self.get_argument("contract_start_time", "")
            end_time = self.get_argument("contract_end_time", "")
            state_id = self.get_argument("state_id")
            contract_remark = self.get_argument("state_id", "")
            if not title:
                self.write("合同名称不能为空")
            else:
                if contract_id > 0:
                    result = self.db_customer.execute("""
                            update t_contract set
                         `title`=%s,
                        `contract_remark`=%s,
                        `start_time`=%s,
                        `end_time`=%s,
                        `updated_at`=%s,
                        `state_id`=%s,
                        `uid`=%s,
                        `uid_name`=%s


                            where id=%s
                    
                    
                    """,title, contract_remark, start_time,
                                            end_time, state_id, uid, uid_name,contract_id)

                else:
                    result = self.db_customer.execute("""
                        INSERT INTO `t_contract`
                        (
                        `customer_id`,`guid`,
                        `title`,
                        `contract_remark`,
                        `start_time`,
                        `end_time`,
                        `updated_at`,
                        `state_id`,
                        `uid`,
                        `uid_name`)
                        VALUES
                        ( %s,
                        uuid(),
                        %s,
                        %s,
                        %s,
                        %s,
                        now(),
                        %s,
                        %s,
                        %s);
                        """, customer_id, title, contract_remark, start_time,
                                            end_time, state_id, uid, uid_name)


            self.write(str(result))

        elif tag =="delete":
            contract_id = self.get_argument("contract_id")
            customer_id = self.get_argument("customer_id")

            if not id:
                self.write("id")
            else:
                result = self.db_customer.execute(
                    "delete from t_contract where id=%s and customer_id=%s",
                    contract_id, customer_id)
                self.write(str(result))