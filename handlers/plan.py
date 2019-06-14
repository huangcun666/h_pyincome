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
from Pagination import Pagination
logger = logging.getLogger('boilerplate.' + __name__)
import datetime

#客户
class PlanHandler(BaseHandler):
    @tornado.web.authenticated
    def get(self):
        tag = self.get_argument("tag", "list_company")
        uid = self.get_secure_cookie("uid")
        uid_name = self.get_secure_cookie("name")
        my = self.get_argument("my",'')
        page  = self.get_argument("page",1)
        search_key= ""

        if tag == "list_plan":
            todo=self.get_argument('todo','')
            params = {

                "my": my
            }
            pre_page=20
            sql=''
            if todo=='1':
                sql+=' and datediff(reminder_at,now())>=0 and is_read=0 and is_read_at is null '
            elif todo=='2':
                sql+=' and is_read=1 and is_read_at is not null '
            elif todo=='3':
                sql+=' and datediff(reminder_at,now())<0 and is_read=0 and is_read_at is null '
        
            if my:
                sums=self.db_company.get('''
                select count(*) a,
                (select count(*) count from t_plan where uid=%s and datediff(reminder_at,now())>=0 and is_read=0 and is_read_at is null) b,
                (select count(*) count from t_plan where uid=%s and is_read=1 and is_read_at is not null ) c,
                (select count(*) count from t_plan where uid=%s and datediff(reminder_at,now())<0 and is_read=0 and is_read_at is null ) d
                 from t_plan  where uid=%s
            ''',uid,uid,uid,uid)
                count = self.db_company.get(
                    '''SELECT count(*) count FROM t_plan where   uid=%s ''',
                    uid)

                pagination = Pagination(page, pre_page, count.count, self.request)
                startpage = (page-1) * pre_page
                t_plan = self.db_company.query(
                    '''select *,datediff(reminder_at,now()) dq from t_plan where
                     uid=%s '''+sql+'''order by created_at desc  limit %s,%s ''', uid,
                    startpage, pre_page)
            else:
                sums=self.db_company.get('''
                select count(*) a,
                (select count(*) count from t_plan where datediff(reminder_at,now())>=0 and is_read=0 and is_read_at is null) b,
                (select count(*) count from t_plan where is_read=1 and is_read_at is not null ) c,
                (select count(*) count from t_plan where datediff(reminder_at,now())<0 and is_read=0 and is_read_at is null ) d
                 from t_plan  ''')
                if sql:
                    sql=' where '+sql[4:]
                count = self.db_company.get('''
                        SELECT count(*) count FROM t_plan
                ''')

                pagination = Pagination(page, pre_page, count.count, self.request)
                startpage = (page-1) * pre_page
                t_plan = self.db_company.query(
                    '''select *,datediff(reminder_at,now()) dq from t_plan
                  '''+sql+'''order by created_at desc  limit %s,%s ''',
                    startpage, pre_page)

            return self.render(
                'plan/plan_list.html',
                my=my,
                sums=sums,
                params=params,
                search_key=search_key,
                pagination=pagination,
                t_plan=t_plan,
                todo=todo,
                form_tag=tag)

        elif tag =="show":
            company_id = self.get_argument("id")
            company_guid = self.get_argument("guid")
            search_key = self.get_argument("search_key","")
            tag_type = self.get_argument("tag_type","")
            if not company_id or not company_guid:
                self.write("not companyid or guid")
            else:
                t_company = self.db_company.get(
                    "select * from t_company where id=%s and company_guid=%s",
                    company_id, company_guid)
                if not t_company:
                    self.write("not company")
                else:
                    sql_tag_type = ""
                    if tag_type:
                        sql_tag_type = ''' and tag_type  like "%%'''+tag_type+'''%%"'''

                    t_company_msg = self.db_company.query(
                        "select * from t_company_msg where company_id=%s "+sql_tag_type+" order by created_at desc",
                        company_id)

                    t_company_tag_group = self.db_company.query("""
                       select tag_category,GROUP_CONCAT(tag_name,"_",id) gc from t_company_tag group by tag_category

                    """)
                    t_plan = self.db_company.query("select * from t_plan where rel_id=%s",company_guid)

                    return self.render(
                        'company/company_show.html',
                        t_plan=t_plan,
                        search_key=search_key,
                        t_company=t_company,
                        t_company_tag_group=t_company_tag_group,
                        t_company_msg=t_company_msg,
                        form_tag=tag)

    @tornado.web.authenticated
    def post(self):
        tag = self.get_argument("tag", "list")
        uid = self.get_secure_cookie("uid")
        uid_name = self.get_secure_cookie("name")
        dt=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        if tag=="add":
            plan_type_id_name = self.get_argument('plan_type_id_name','')
            plan_type_id = self.get_argument("plan_type_id",'')
            plan_body = self.get_argument('plan_body','')
            reminder_at = self.get_argument('reminder_at','')
            rtype = self.get_argument('rtype','')
            rtype_name = self.get_argument("rtype_name","传统商机")
            rel_id = self.get_argument('rel_id','0')
            plan_title = self.get_argument("plan_title",'')
            rel_url = self.get_argument("rel_url",'')
            plan_id=self.get_argument('plan_id','')
            business_id=self.get_argument('business_id','')
            if not  rel_id  and not business_id:
                self.write(" not rel_id and not business_id ")
            else:
                if business_id:
                    result = self.db_company.execute(
                            """
                        INSERT INTO `t_plan` ( `plan_type_id_name`, `plan_type_id`,
                        `plan_body`, `created_at`, `reminder_at`, `rtype`, `rel_id`,
                        `is_read`,`is_hide`, `uid`, `uid_name`,`plan_title`,`rel_url`,`rtype_name`,`business_id`)
                                VALUES
                        (%s, %s,
                        %s, %s, %s, %s, %s,
                        0, 0, %s, %s,%s,%s,%s,%s);
                                """, plan_type_id_name, plan_type_id, plan_body, dt,
                            reminder_at, rtype, rel_id, uid, uid_name, plan_title,
                            rel_url, rtype_name,business_id)
                    self.db.execute("""
                        insert into business_develop_manage_msg(uid,uid_name,message,created_at,business_id,tag_type,btype_id)
                        values(%s,%s,%s,%s,%s,%s,%s)
                        """, uid, uid_name,plan_type_id+'_'+plan_type_id_name+'_'+plan_body+'_'+reminder_at, dt, business_id, "销售计划",'4')
                else:
                    if plan_id:
                        self.db_company.execute('''
                            update t_plan set is_read=1,is_read_at=%s where id=%s
                        ''',dt,plan_id)
                    else:
                        result = self.db_company.execute(
                            """
                        INSERT INTO `t_plan` ( `plan_type_id_name`, `plan_type_id`,
                        `plan_body`, `created_at`, `reminder_at`, `rtype`, `rel_id`,
                        `is_read`,`is_hide`, `uid`, `uid_name`,`plan_title`,`rel_url`,`rtype_name`)
                                VALUES
                        (%s, %s,
                        %s, %s, %s, %s, %s,
                        0, 0, %s, %s,%s,%s,%s);
                                """, plan_type_id_name, plan_type_id, plan_body, dt,
                            reminder_at, rtype, rel_id, uid, uid_name, plan_title,
                            rel_url, rtype_name)
                        self.db_company.execute('''
                        insert into t_company_msg(uid,uid_name,message,created_at,company_id,tag_type)
                        values(%s,%s,%s,%s,%s,'销售计划')
                        ''',uid,uid_name,str(result)+'_'+plan_type_id_name+'_'+plan_body+'_'+str(reminder_at),dt,rel_id)
                        self.db_company.execute('''
                            update t_company set last_updated=%s,last_updated_msg=%s,last_updated_type='销售计划' where id=%s
                        ''',dt,plan_body,rel_id)
                        self.write(str(result))