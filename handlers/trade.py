# encoding=utf8
from handlers.base import BaseHandler
from Pagination import Pagination
import logging
import json,datetime
import tornado.web
import urllib2
import tornado.httpclient
import sys, re,os,uuid
import urllib,datetime
import events
reload(sys)
from tornado.options import define, options
sys.setdefaultencoding('utf8')
import tools
logger = logging.getLogger('boilerplate.' + __name__)


class TradeHandler(BaseHandler):
    @tornado.web.authenticated
    def get(self):
        tag = self.get_argument("tag","list")
        uid = self.get_secure_cookie("uid")
        uid_name=self.get_secure_cookie('name')
        page=int(self.get_argument('page',1))
        my = self.get_argument("my","1")
        role = self.get_secure_cookie("role")
        search_key = self.get_argument("search_key",'')

        my_sql =""
        my_sql =""
        if role!="8":
            my_sql=" and uid=%s "%(uid)
        pre_page=20
        if tag =="list":
            page= int(self.get_argument("page",1))
            todo  = self.get_argument("todo","")
            pre_page=20
            count = self.db.get(''' SELECT count(*) count FROM t_trade   where  is_close=0 ''' + my_sql)
            pagination = Pagination(page, pre_page, count.count, self.request)
            startpage = (page-1) * pre_page
            t_trade = self.db.query('''
                SELECT  a.*,b.mbs,c.customer_name from   t_trade a left join 
                (select project_id,group_concat(team_name,"|",member_name)  mbs   from t_projects_member where member_id > 0 group by project_id) b
                on a.project_id=b.project_id
                left join t_projects c on a.project_id=c.id
                   where  is_close=0 '''+my_sql+'''
                order by created_at desc limit %s,%s
                ''',startpage,pre_page)

     
            return self.render('trade/trade_list.html',pagination=pagination,t_trade=t_trade,search_key=search_key,todo=todo,my=my,get_member=tools.get_member,
                                form_tag="list")
        elif tag=="show":
            id = self.get_argument("id")
            if not id:
                return self.write("id is null")
            t_trade = self.db.get("select * from t_trade where id=%s",id)
            t_project = None
            t_proejct_member_arr = None
            if t_trade.project_id:
                t_project = self.db.get('select * from t_projects where id=%s',t_trade.project_id)
                if t_project:
                    t_proejct_member = self.db.get('select project_id,group_concat(team_name,"|",member_name)  mbs   from t_projects_member where member_id > 0 and project_id=%s group by project_id ',t_project.id)
                    if t_proejct_member:
                        t_proejct_member_arr = t_proejct_member.mbs
            t_trade_msg = None
            t_trade_milepost_his = self.db.query("select * from t_trade_milepost_his where trade_id=%s",id)
            t_trade_file = self.db.query("select * from t_trade_file where trade_id=%s order by file_by_at desc",id)
            t_trade_milepost = self.db.query("select * from t_trade_milepost where trade_id=%s order by mile_id_order  ",id)
            return self.render('trade/trade_show.html',get_member=tools.get_member,t_trade=t_trade,search_key=search_key,t_project=t_project,t_trade_msg=t_trade_msg,t_proejct_member_arr=t_proejct_member_arr,
                                t_trade_milepost_his=t_trade_milepost_his,form_tag="list",t_trade_file=t_trade_file,t_trade_milepost=t_trade_milepost)
    def post(self):
        tag = self.get_argument("tag","")
        uid = self.get_secure_cookie("uid")
        uid_name=self.get_secure_cookie('name')
        page=int(self.get_argument('page',1))
        my = self.get_argument("my","1")
        role = self.get_secure_cookie("role")
        dt = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        if tag=="add":
            trade_name = self.get_argument("trade_name","")
            trade_number = self.get_argument("trade_number","")            
            trade_by = self.get_argument("trade_by","")            
            trade_regtype = self.get_argument("trade_regtype","")            
            trade_color = self.get_argument("trade_color","")            
            project_id = self.get_argument("project_id","")            
            trade_remark = self.get_argument("trade_remark","")     
         
            if not trade_name :
                return self.write("商标名称不能为空哦")
            result_id = self.db.execute("""insert into t_trade(trade_name,trade_number,trade_by,trade_regtype,trade_color,project_id,trade_remark,created_at,created_uid,created_uid_name)
            values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
            """,trade_name,trade_number,trade_by,trade_regtype,trade_color,project_id,trade_remark,dt,uid,uid_name)
            if result_id:
                self.db.execute("""
                    insert into t_trade_milepost(trade_id,mile_id_order,mile_id_name)
                    select %s,order_int,income_name from t_projects_type where income_category='商标'
                """,result_id)
            return self.write(str(result_id))

        elif tag=="set_milepost":
            trade_id = self.get_argument("trade_id")
            mile_id = self.get_argument("mile_id")
            state_id_remark = self.get_argument("state_id_remark","")
            state_id = self.get_argument("state_id","")
            state_id_name = self.get_argument("state_id_name","")
            his_id = self.get_argument("his_id",0)
            t_milepost = self.db.get("select * from t_trade_milepost where mile_id=%s",mile_id)
            if  not t_milepost:
                return self.write("not mile_Id")
            if (t_milepost.mile_id_order==2 or  t_milepost.mile_id_order==3)  and int(state_id) > 1:
                his_order=self.db.get("select count(*) c from t_trade_milepost_his where mile_id=%s",mile_id)
                self.db.execute("""
                    insert into t_trade_milepost_his(his_order,his_name,his_at,his_uid,his_uid_name,mile_id,trade_id,his_remark)
                    values(%s,%s,%s,%s,%s,%s,%s,%s)
                """,his_order.c+1,state_id_name,dt,uid,uid_name,mile_id,trade_id,state_id_remark)
            
            result = self.db.execute("""
                update t_trade_milepost set mile_by_at=%s,
                mile_by_uid=%s,mile_by_uid_name=%s,state_id_remark=%s,
                trade_id=%s,state_id=%s,state_id_name=%s where mile_id=%s
            """,dt,uid,uid_name,state_id_remark,trade_id,state_id,state_id_name,mile_id)
            if his_id:
                    self.db.execute("""update t_trade_milepost_his set 
                    state_id=%s,state_id_name=%s,state_id_at=%s,state_uid=%s,state_uid_name=%s  where his_id=%s
                    """,state_id,state_id_name,dt,uid,uid_name,his_id)
            self.write(str(result))
        elif tag=="save_trans":
            trade_id = self.get_argument("trade_id")
            mile_id = self.get_argument("mile_id")
            state_id_remark = self.get_argument("state_id_remark","")

            result = self.db.execute("""
                update t_trade_milepost set mile_by_at=%s,
                mile_by_uid=%s,mile_by_uid_name=%s,state_id_remark=%s,
                trade_id=%s where mile_id=%s
            """,dt,uid,uid_name,state_id_remark,trade_id,mile_id)
            self.write(str(result))

        elif tag=="cert":
            trade_id = self.get_argument("trade_id")
            mile_id = self.get_argument("mile_id")
            cert_remark = self.get_argument("cert_remark","")
            cert_at = self.get_argument("cert_at","")
            state_id_name = self.get_argument("state_id_name","")

            result = self.db.execute("""
                update t_trade_milepost set mile_by_at=%s,
                mile_by_uid=%s,mile_by_uid_name=%s,cert_remark=%s,
                trade_id=%s,cert_at=%s where mile_id=%s
            """,dt,uid,uid_name,cert_remark,trade_id,cert_at,mile_id)
            self.write(str(result))

        elif tag=="upload":
            is_upload = 0
            type_name = self.get_argument("type_name")
            trade_remark= self.get_argument("trade_remark","")
            trade_id = self.get_argument("trade_id","")
            mile_id = self.get_argument("mile_id",0)
            his_id = self.get_argument("his_id",0)
            tag_from =self.get_argument("tag_from","")

            for k,file1 in self.request.files.items():
        
                ori_filename = file1[0].filename
                filename_full = options.upload_path + "/customer/trade/%s/" % (
                        trade_id)
                print filename_full  
                url_path = "/static/customer/trade/%s/" % (trade_id)
                try:
                    os.makedirs(filename_full)
                except OSError:
                    if not os.path.isdir(filename_full):
                        raise
                extension = os.path.splitext(ori_filename)[1]

                uuid_str = str(uuid.uuid4())
                fname = "{0}_{1}{2}".format(uuid_str, trade_id,
                                                extension)

                save_full_path = filename_full + fname
                url_fname = "{0}{1}".format(url_path, fname)
                print save_full_path,save_full_path
                output_file = open(save_full_path, 'w')
                output_file.write(file1[0]["body"])
                is_upload= is_upload+1
                self.db.execute("""insert into t_trade_file(type_name,
                file_path,file_by,file_by_uid,file_by_at,trade_id,remark,source_name,mile_id,his_id)
                values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)""",
                type_name,url_fname,uid_name,uid,dt,trade_id,trade_remark,ori_filename,mile_id,his_id
                )
            if tag_from=="cert":
                cert_at = self.get_argument("cert_at")
                cert_remark = self.get_argument("cert_remark","")
                result = self.db.execute("""
                update t_trade_milepost set mile_by_at=%s,
                mile_by_uid=%s,mile_by_uid_name=%s,state_id_remark=%s,
                trade_id=%s,state_id=%s,state_id_name=%s where mile_id=%s
            """,dt,uid,uid_name,state_id_remark,trade_id,state_id,state_id_name,mile_id)

            data = {'result':is_upload}   
            return self.write(json.dumps(data))
  