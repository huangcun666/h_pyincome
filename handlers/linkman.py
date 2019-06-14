# encoding=utf8
from handlers.base import BaseHandler
import logging
import json,datetime
import tornado.web
import urllib2
import tornado.httpclient
import events
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
        dt=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        result = -10
        if tag == "add":

            name = self.get_argument("name")
            customer_id = self.get_argument("customer_id")
            tel = self.get_argument("tel","")
            remark = self.get_argument("remark","")
            gender = self.get_argument("gender")
            linkman_id=self.get_argument('linkman_id','')
            is_first=self.get_argument('is_first','0')
            txt=''
            if not name:
                self.write("联系人的名字不能为空")
            else:
                if linkman_id:
                    t_linkman=self.db_customer.get('''
                        select * from t_linkman where id=%s
                    ''',linkman_id)
                    self.db_customer.execute(
                    """update t_linkman set is_first=%s, name=%s,tel=%s,gender=%s,remark=%s,acc_uid=%s,acc_uid_name=%s,updated_at=%s
                    where id=%s
                    """,is_first, name, tel,
                    gender, remark, uid, uid_name,dt,linkman_id)
             
                    if t_linkman.is_first!=int(is_first):
                        if is_first=='1':
                            txt+=',添加为首要联系人'
                    if t_linkman.name!=name:
                        txt+=',客户姓名:'+t_linkman.name+' 修改为 '+name
                    if t_linkman.tel!=tel:
                        txt+=',电话:'+t_linkman.tel+' 修改为 '+tel
                    if txt:
                        events.add_project_event(self,'0', "修改联系人",txt[1:],
                                         uid, uid_name,customer_id)
                else:
                    result = self.db_customer.execute(
                    """insert into t_linkman (is_first,name,tel,gender,remark,acc_uid,acc_uid_name,created_at,updated_at,guid,customer_id)
                
                values(%s,%s,%s,%s,%s,%s,%s,%s,%s,uuid(),%s)""",is_first,name, tel,
                    gender, remark, uid, uid_name,dt,dt, customer_id)
                    if result>0:
                        txt='联系人:'+name+',联系电话:'+tel
                        events.add_project_event(self,'0', "创建联系人", txt,
                                         uid, uid_name,customer_id)


                self.write(str(result))

        elif tag =="delete":
            id = self.get_argument("id")
            guid = self.get_argument("guid")

            if not id:
                self.write("id")
            else:
                result = self.db_customer.execute("delete from t_linkman where id=%s and guid=%s",id,guid)
                self.write(str(result))