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
class CompanyHandler(BaseHandler):
    @tornado.web.authenticated
    def get(self):
        tag = self.get_argument("tag", "list_company")
        uid = self.get_secure_cookie("uid")
        uid_name = self.get_secure_cookie("name")
        if tag == "list_company":
            start = self.get_argument("start","")
            end = self.get_argument("end","")
            page= int(self.get_argument("page",1))
            search_key = self.get_argument("search_key","")
            my = self.get_argument("my","")
            keyword = self.get_argument("keyword","")
            action = self.get_argument("action","")
            rank = self.get_argument("rank","")
            bystaff = self.get_argument('bystaff', "")
            last_updated = self.get_argument("last_updated","")
            last_updated_type = self.get_argument("last_updated_type","")
            sales_uid_name=self.get_argument('sales_uid_name','')
            update_start=self.get_argument('update_start','')
            update_end=self.get_argument('update_end','')
            params = {
                "action": action,
                "search_key": search_key,
                "my": my,
                "keyword": keyword,
                "start": start,
                "end": end,
                "rank": rank,
                "my": my,
                "bystaff": bystaff,
                "last_updated": last_updated,
                "last_updated_type": last_updated_type,
                "sales_uid_name":sales_uid_name,
                "update_start":update_start,
                "update_end":update_end
            }
            pre_page=20
            my_sql=""
            sql_keyword = ""
            sql_keyword_rank = ""
            last_updated_sql = ""
            bystaff_sql = ""
            sales_uid_name_sql=""
            last_updated_sql=""
            if bystaff:
                bystaff_sql += "  and sales_uid > 0 "
            if last_updated:
                bystaff_sql += "  and last_updated is not null"
            if last_updated:
                last_updated_type += " and  last_updated_type ='"+last_updated_type+"'"
            print bystaff_sql, "bystaff_sql"
            if rank and rank !="0":
                sql_keyword_rank = "and rank = '%s'"%(rank)
            if start and end:
                sql_keyword += " and creater between '" + start + "' and  '" + end + "'"

            if keyword:
                sql_keyword += ''' and (entName  like "%%''' + keyword + '''%%")''' + ''' or (reg_addr  like "%%''' + keyword + '''%%")''' + ''' or (email  like "%%''' + keyword + '''%%")''' + ''' or (phone  like "%%''' + keyword + '''%%")'''
            if sales_uid_name:
                sales_uid_name_sql=''' and sales_uid_name="%s" '''%sales_uid_name
            if update_start and update_end:
                last_updated_sql=''' and last_updated between '%s' and '%s' '''%(update_start,update_end)
            if my:
                my_sql = " and  sales_uid =%s"%(uid)
                if my=="2":
                    my_sql+= " and is_close=2"

                count = self.db_company.get(
                    '''SELECT count(*) count FROM t_company where is_close=0 '''
                    +sales_uid_name_sql+last_updated_sql+my_sql + sql_keyword + bystaff_sql)

                pagination = Pagination(page, pre_page, count.count, self.request)
                startpage = (page-1) * pre_page
                t_company = self.db_company.query(
                    '''select * from t_company where phone is not  null  and  is_close=0 '''
                    +sales_uid_name_sql+last_updated_sql+my_sql + sql_keyword + bystaff_sql +
                    ''' order by last_updated desc  limit %s,%s ''', startpage,
                    pre_page)
            elif bystaff_sql:

                if sql_keyword:
                    count = self.db_company.get(
                        '''SELECT count(*) count FROM t_company where is_close=0 '''
                        +sales_uid_name_sql+last_updated_sql+ sql_keyword + sql_keyword_rank + bystaff_sql)


                    pagination = Pagination(page, pre_page, count.count, self.request)
                    startpage = (page-1) * pre_page
                    t_company = self.db_company.query('''
                        select * from t_company where phone is not  null  and   is_close=0 and sales_uid =0 '''
                          +sales_uid_name_sql+last_updated_sql+ sql_keyword +sql_keyword_rank+bystaff_sql+ '''
                    limit %s,%s''', startpage, pre_page)

                else:
                    count = self.db_company.get(
                        '''SELECT count(*) count FROM t_company where is_close=0 '''
                         +sales_uid_name_sql+last_updated_sql+ bystaff_sql)

                    pagination = Pagination(page, pre_page, count.count, self.request)
                    startpage = (page-1) * pre_page
                    t_company = self.db_company.query(
                        '''select * from t_company where phone is not  null  and  is_close=0 '''
                         +sales_uid_name_sql+last_updated_sql+ bystaff_sql +
                        ''' order by last_updated desc  limit %s,%s ''', startpage,
                        pre_page)
                return self.render(
                'company/company_timeline.html',
                params=params,
                search_key=search_key,
                pagination=pagination,
                t_company=t_company,
                form_tag=tag)
            else:

                if sql_keyword:
                    count = self.db_company.get(
                        '''SELECT count(*) count FROM t_company where is_close=0 '''
                        + sql_keyword + sql_keyword_rank )


                    pagination = Pagination(page, pre_page, count.count, self.request)
                    startpage = (page-1) * pre_page
                    t_company = self.db_company.query('''
                        select * from t_company where phone is not  null  and   is_close=0 and sales_uid =0 '''
                                                      + sql_keyword +sql_keyword_rank+ '''
 limit %s,%s                        ''', startpage, pre_page)

                else:
                    count = self.db_company.get(
                        '''SELECT 20 count
                    ''')

                    pagination = Pagination(page, pre_page, count.count, self.request)
                    startpage = (page-1) * pre_page
                    t_company = self.db_company.query(
                        '''
                        select * from t_company where phone is not  null  and   is_close=0 and sales_uid =0 '''
                        + sql_keyword_rank + ''' ORDER BY RAND()
                        limit 20
                        ''')

            return self.render(
                'company/company_list.html',
                params=params,
                search_key=search_key,
                pagination=pagination,
                t_company=t_company,
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
                    t_type = self.db_company.query("select * from t_type where type_category='销售计划'")
                    t_plan = self.db_company.query(
                        "select * from t_plan where rel_id=%s", company_id)

                    return self.render(
                        'company/company_show.html',
                        search_key=search_key,
                        t_plan=t_plan,
                        t_type=t_type,
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
        if tag=="save_tags":
            company_tags = self.get_argument('company_tags', '')
            company_guid = self.get_argument("company_guid")
            company_id=self.get_argument('company_id','')

            if company_id:
                self.db_company.execute('''
                update t_company set customer_tag=%s,last_updated=%s , last_updated_type=%s,last_updated_msg=%s where id=%s and company_guid=%s
            ''', company_tags, dt, "操作标签", company_tags,company_id,
                                        company_guid)
                self.db_company.execute("""
                insert into t_company_msg(uid,uid_name,message,created_at,company_id,tag_type)
                values(%s,%s,%s,%s,%s,%s)
                """, uid, uid_name, company_tags, dt, company_id, "操作标签")

        elif tag=="add_to_me":
            company_guid = self.get_argument("company_guid")
            company_id = self.get_argument('company_id', '')
            if not company_id or not company_guid:
                self.write("not companyid or guid")
            else:
                t_company = self.db_company.get(
                    "select * from t_company where id=%s",company_id)
                if not t_company:
                    self.write("公司不存在")
                elif t_company.sales_uid:
                    self.write("该客户已经被标记私有")
                else:
                    count = self.db_company.get(
                    '''SELECT count(*) count FROM t_company where is_close=0  and sales_uid =%s''',uid)
                    print(count.count)
                    if count.count>=600:
                        self.write('-1')
                    else:
                        msg = u"该客户被(%s)标记私有" % (uid_name)
                        result = self.db_company.execute(
                            "update t_company set sales_uid=%s , sales_uid_name=%s, sales_uid_at=%s,last_updated=%s,last_updated_type=%s,last_updated_msg=%s where id=%s and company_guid=%s",
                            uid, uid_name, dt, dt, "客户分配", msg, company_id,
                            company_guid)
                        self.db_company.execute("""
                            insert into t_company_msg(uid,uid_name,message,created_at,company_id,tag_type)
                            values(%s,%s,%s,%s,%s,%s)
                            """, uid, uid_name, msg, dt, company_id, "客户分配")

                        self.write(str(result))
        elif tag=="edit_sales_name":
            companys=self.get_argument('companys','')
            companys=companys.split(',')
            sales_uid_name=self.get_argument('sales_uid_name')
            t_user=self.db.get('select * from t_user where name=%s limit 1',sales_uid_name)
            if not t_user:
                self.write('-1')
            else:
                for item in  companys[::2]:
                    msg = u"%s修改归属人为%s"%(uid_name,sales_uid_name)
                    result = self.db_company.execute(
                        "update t_company set sales_uid=%s , sales_uid_name=%s,last_updated_msg=%s  where id=%s and company_guid=%s",
                        t_user.id,t_user.name,msg,item,companys[companys.index(item)+1])

                    self.db_company.execute("""
                        insert into t_company_msg(uid,uid_name,message,created_at,company_id,tag_type)
                        values(%s,%s,%s,%s,%s,%s)
                        """, uid, uid_name, msg, dt, item, "客户分配")

        elif tag == "free_to_me":
            company_guid = self.get_argument("company_guid",'')
            company_id = self.get_argument('company_id', '')
            companys=self.get_argument('companys','')
            if companys:
                companys=companys.split(',')
                for item in  companys[::2]:
                    msg = u"该客户被(%s)放回公有池"%(uid_name)
                    result = self.db_company.execute(
                        "update t_company set sales_uid=0 , sales_uid_name=NULL,last_updated_msg=%s  where id=%s and company_guid=%s",
                        msg,item,companys[companys.index(item)+1])

                    self.db_company.execute("""
                        insert into t_company_msg(uid,uid_name,message,created_at,company_id,tag_type)
                        values(%s,%s,%s,%s,%s,%s)
                        """, uid, uid_name, msg, dt, item, "客户分配")
                
            elif not company_id or not company_guid:
                self.write("not companyid or guid")
            else:
                msg = u"该客户被(%s)放回公有池"%(uid_name)

                result = self.db_company.execute(
                    "update t_company set sales_uid=0 , sales_uid_name=NULL,last_updated_msg=%s  where id=%s and company_guid=%s",
                    msg,company_id, company_guid)

                self.db_company.execute("""
                    insert into t_company_msg(uid,uid_name,message,created_at,company_id,tag_type)
                    values(%s,%s,%s,%s,%s,%s)
                    """, uid, uid_name, msg, dt, company_id, "客户分配")
                self.write(str(result))



        elif tag == "company_msg":
            msg = self.get_argument('msg', '')
            company_guid = self.get_argument("company_guid")
            company_id=self.get_argument('company_id','')

            if company_id:
                self.db_company.execute("""
                insert into t_company_msg(uid,uid_name,message,created_at,company_id,tag_type)
                values(%s,%s,%s,%s,%s,%s)
                """, uid, uid_name, msg, dt, company_id, "跟进记录")

                self.db_company.execute("update t_company set last_updated=%s,last_updated_msg=%s where id=%s",dt,msg,company_id)
