# encoding=utf8
from handlers.base import BaseHandler
import logging
import json
import tornado.web
import urllib2
import tornado.httpclient
import sys, re
import urllib
import events
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
            txt=''
            if not title:
                self.write("合同名称不能为空")
            else:
                if contract_id > 0:
                    t_contract=self.db_customer.get(' select * from t_contract where id=%s ',contract_id)
                    result = self.db_customer.execute("""
                            update t_contract set
                         `title`=%s,
                        `contract_remark`=%s,
                        `start_time`=%s,
                        `end_time`=%s,
                        `updated_at`=now(),
                        `state_id`=%s,
                        `uid`=%s,
                        `uid_name`=%s


                            where id=%s
                    
                    
                    """,title, contract_remark, start_time,
                                            end_time, state_id, uid, uid_name,contract_id)
                    if t_contract.title!=title:
                        txt+=',合同内容:'+t_contract.title+' 修改为 '+title
                    if str(t_contract.start_time.strftime('%Y-%m-%d'))!=start_time:
                        txt+=',开始时间:'+str(t_contract.start_time.strftime('%Y-%m-%d'))+' 修改为 '+start_time
                    if str(t_contract.end_time.strftime('%Y-%m-%d'))!=end_time:
                        txt+=',开始时间:'+str(t_contract.end_time.strftime('%Y-%m-%d'))+' 修改为 '+end_time
                    if t_contract.state_id!=int(state_id):
                        if state_id=='1':
                            txt+=',状态:关闭 修改为 正常'
                        elif state_id=='0':
                            txt+=',状态:正常 修改为 关闭'
                    if txt:
                        events.add_project_event(self,0, "增加业务到期", txt[1:],
                        uid, uid_name,t_contract.customer_id)
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

                    if result>0:
                        txt='合同内容:'+title+',开始时间:'+start_time+',到期时间:'+end_time
                        if state_id=='1':
                            txt+=',状态:正常'
                        elif state_id=='0':
                            txt+=',状态:关闭'
                        events.add_project_event(self,0, "增加业务到期", txt,
                        uid, uid_name,customer_id)
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