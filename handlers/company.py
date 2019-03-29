# encoding=utf8
from handlers.base import BaseHandler
import logging
import json
import os
import tornado.web
import urllib2
import tornado.httpclient
from tornado.options import define, options
import sys, re,uuid
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
        role_list=self.get_secure_cookie('role_list')
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
            type_id = int(self.get_argument("type_id",0))
            is_close = int(self.get_argument("close",0))
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
                "sales_uid_name": sales_uid_name,
                "update_start": update_start,
                "update_end": update_end,
                'type_id': type_id,
                "close": is_close
            }
            pre_page=20
            my_sql=""
            sql_keyword = ""
            sql_keyword_rank = ""
            last_updated_sql = ""
            bystaff_sql = ""
            sales_uid_name_sql=""
            last_updated_sql=""
            type_id_sql = ""
            if bystaff:
                bystaff_sql += "  and sales_uid > 0 "
            if last_updated:
                bystaff_sql += "  and last_updated is not null"
            if last_updated:
                last_updated_type += " and  last_updated_type ='"+last_updated_type+"'"
            if rank and rank !="0":
                sql_keyword_rank = "and rank = '%s'"%(rank)
            if start and end:
                sql_keyword += " and creater between '" + start + "' and  '" + end + "'"

            if keyword:
                sql_keyword += ''' and ((entName  like "%%''' + keyword + '''%%")''' + ''' or (reg_addr  like "%%''' + keyword + '''%%")''' + ''' or (email  like "%%''' + keyword + '''%%")''' + ''' or (phone  like "%%''' + keyword + '''%%"))'''
            if sales_uid_name:
                sales_uid_name_sql=''' and sales_uid_name="%s" '''%sales_uid_name
            if update_start and update_end:
                last_updated_sql=''' and last_updated between '%s' and '%s' '''%(update_start,update_end)

            if type_id:
                type_id_sql = " and type_id=%s "%(type_id)
            is_close_sql = ""
            if is_close==-100:
                type_id_sql += " and is_close > 0"
            else:
                type_id_sql += " and is_close = 0"
            
            if my:
                my_sql = " and  sales_uid =%s"%(uid)
                if my=="2":
                    my_sql+= " and is_close=2"

                count = self.db_company.get(
                    '''SELECT count(*) count FROM t_company where 0=0 '''
                    + sales_uid_name_sql + last_updated_sql + my_sql +
                    sql_keyword + bystaff_sql + type_id_sql)

                pagination = Pagination(page, pre_page, count.count, self.request)
                startpage = (page-1) * pre_page
                t_company = self.db_company.query(
                    '''select * from t_company where phone is not  null  and  0=0 '''
                    +sales_uid_name_sql+last_updated_sql+my_sql + sql_keyword + bystaff_sql +type_id_sql+
                    ''' order by last_updated desc  limit %s,%s ''', startpage,
                    pre_page)
            elif bystaff_sql:
                
                if sql_keyword:
                    count = self.db_company.get(
                        '''SELECT count(*) count FROM t_company where '''
                        + sales_uid_name_sql + last_updated_sql + sql_keyword +
                        sql_keyword_rank + bystaff_sql + type_id_sql)


                    pagination = Pagination(page, pre_page, count.count, self.request)
                    startpage = (page-1) * pre_page
                    t_company = self.db_company.query(
                        '''
                        select * from t_company where phone is not  null   and sales_uid =0 '''
                        + sales_uid_name_sql + last_updated_sql + sql_keyword +
                        sql_keyword_rank + bystaff_sql + type_id_sql + '''
                    limit %s,%s''', startpage, pre_page)

                else:
                    
                    count = self.db_company.get(
                        '''SELECT count(*) count FROM t_company where 0=0 '''
                        + sales_uid_name_sql + last_updated_sql + bystaff_sql +
                        type_id_sql)

                    pagination = Pagination(page, pre_page, count.count, self.request)
                    startpage = (page-1) * pre_page
                    t_company = self.db_company.query(
                        '''select * from t_company where phone is not  null  and  0=0 '''
                         +sales_uid_name_sql+last_updated_sql+ bystaff_sql +type_id_sql+
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
                        '''SELECT count(*) count FROM t_company where  phone is not  null and 0=0 and sales_uid =0 '''
                        + sql_keyword + sql_keyword_rank + type_id_sql)


                    pagination = Pagination(page, pre_page, count.count, self.request)
                    startpage = (page-1) * pre_page
                    t_company = self.db_company.query('''
                        select * from t_company where phone is not  null  and   0=0 and sales_uid =0 '''
                                                      + sql_keyword +sql_keyword_rank+type_id_sql+ '''
 limit %s,%s                        ''', startpage, pre_page)

                else:
                    count = self.db_company.get(
                        '''SELECT 20 count
                    ''')

                    pagination = Pagination(page, pre_page, count.count, self.request)
                    startpage = (page-1) * pre_page
                    t_company = self.db_company.query(
                        '''
                        select * from t_company where phone is not  null  and   0=0 and sales_uid =0 '''
                        + sql_keyword_rank + type_id_sql + ''' ORDER BY RAND()
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
                       select tag_category,GROUP_CONCAT(tag_name,"_",id) gc from t_company_tag where is_hide=0 group by tag_category

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

        elif tag=="business_develop_manage":
            page= int(self.get_argument("page",1))
            step=self.get_argument('step','')
            pre_page=20
            sql=''
            if step=='1':
                sql=' and b.assigner_at is null and b.jiedan_at is null and b.banjie_at is null and b.checked_at is null '
            elif step=='2':
                sql='  and b.assigner_at is not null and b.jiedan_at is null and b.banjie_at is null and b.checked_at is null '
            elif step=='3':
                sql='  and b.assigner_at is not null and b.jiedan_at is not null and b.banjie_at is null and b.checked_at is null '
            elif step=='4':
                sql='  and b.assigner_at is not null and b.jiedan_at is not null and b.banjie_at is not null and b.checked_at is null '
            elif step=='5':
                sql='  and b.assigner_at is not null and b.jiedan_at is not null and b.banjie_at is not null and b.checked_at is not null and b.checked_status=1 '
            elif step=='6':
                sql='  and b.assigner_at is not null and b.jiedan_at is not null and b.banjie_at is not null and b.checked_at is not null and b.checked_status=2 '
            if '283' not in role_list and '284' not in role_list:
                sql+=' and (a.uid=%s or b.jiedan_id=%s) '%(uid,uid)
            
            t_talk_type = self.db.query(
            "select * from t_projects_type where income_category='沟通方式' order by order_int desc "
                )
            t_business_channel = self.db.query("""
                select * from t_projects_type where income_category='推广来源渠道'
                 and (id=64 or id=65 or id=67)
                 order by order_int desc
                """)
            t_income_type = self.db.query("""
                select * from t_projects_type where income_category='业务来源'
                and (id=2 or id=3 or id=81)
                 order by order_int desc
                """)
            t_port_type=self.db.query('''
                 select * from t_projects_type where income_category='来源端口'
            ''')
            count=self.db.get('''
            select count(*) count from business_develop_manage a
            inner join business_develop_manage_milepost b on a.id=b.business_id
            '''+sql)
            pagination = Pagination(page, pre_page, count.count, self.request)
            startpage = (page-1) * pre_page
            business_develop_manage=self.db.query('''
            select a.*    from business_develop_manage a
            inner join business_develop_manage_milepost b on a.id=b.business_id '''+sql+'''
             order by a.created_at desc limit %s,%s
            ''',startpage,pre_page)
            self.render('company/business_develop_manage.html',
            search_key="",
            step=step,
            pagination=pagination,
            business_develop_manage=business_develop_manage,
            t_talk_type=t_talk_type,
            t_business_channel=t_business_channel,
            t_income_type=t_income_type,
            t_port_type=t_port_type
            )

        elif tag=="show_business":
            guid=self.get_argument('guid')
            id=self.get_argument('id')
            t_talk_type = self.db.query(
            "select * from t_projects_type where income_category='沟通方式' order by order_int desc "
                )
            t_business_channel = self.db.query("""
                select * from t_projects_type where income_category='推广来源渠道'
                 and (id=64 or id=65 or id=67)
                 order by order_int desc
                """)
            t_income_type = self.db.query("""
                select * from t_projects_type where income_category='业务来源'
                and (id=2 or id=3 or id=81)
                 order by order_int desc
                """)
            t_port_type=self.db.query('''
                 select * from t_projects_type where income_category='来源端口'
            ''')
            t_company_tag_group = self.db_company.query("""
                       select tag_category,GROUP_CONCAT(tag_name,"_",id) gc from t_company_tag where is_hide=1 group by tag_category

                    """)
            business_develop_manage_msg=self.db.query('''
            select * from business_develop_manage_msg where business_id=%s order by created_at desc
            ''',id)
            business_develop_manage=self.db.get('''
            select *,a.id business_id,b.id business_milpost_id from business_develop_manage a
             inner join business_develop_manage_milepost b on a.id=b.business_id
              where a.id=%s and a.guid=%s
            ''',id,guid)
            if not business_develop_manage:
                self.write('订单'+id+'不存在')
            else:
                self.render('company/show_business.html',
                search_key='',
                t_talk_type=t_talk_type,
                t_company_tag_group=t_company_tag_group,
                t_business_channel=t_business_channel,
                t_income_type=t_income_type,
                t_port_type=t_port_type,
                business_develop_manage=business_develop_manage,
                business_develop_manage_msg=business_develop_manage_msg
                )   

        elif tag=="economic_census":
            add_sql=''
            step=self.get_argument('step','')
            page=int(self.get_argument('page',1))
            company=self.get_argument('company','')
            ok=self.get_argument('ok','')
            pre_page =20
            if '288' in role_list:
                pass
            else:
                add_sql+=' and c.acc_uid=%s '%uid
            params={
                'step':step,
                'company':company,
                'ok':ok
            }
            if step=='1':
                add_sql+=' and d.id is null  '
            elif step=='2':
                add_sql+=' and d.jiedan_at is not null and d.banjie_at is null '
            elif step=='3':
                add_sql+=' and d.banjie_at is not null and d.kj_check_status=0'
            elif step=='4':
                add_sql+=' and d.kj_check_status=1 '
            elif step=='5':
                add_sql+=' and d.kj_check_status=2 '
            if company:
                add_sql+=' and a.customer_company like "%%'+company+'%%" '
            count = self.db.get(
                '''
                     SELECT count(*) count,(
                      select sum(all_income) from t_projects a where (is_lock=0
                      and a.id in (select project_id from t_projects_service_income aaaa
                    where  service_money > 0 and  service_id=272 and aaaa.project_id=a.id)
                     or  a.is_economic_census=1)
                       '''+ add_sql+'''
                  ) sum_income
                FROM t_projects a
                inner join '''+options.mysql_database_customer+'''.t_customer c
                on a.customer_company=c.company 
                left join t_projects_economic_census d on a.id=d.project_id 
                left join (select project_id,GROUP_CONCAT(concat(member_name,'|',team_id)) team_list
                from t_projects_member group by project_id )  b
				 on a.id=b.project_id
                   where   (is_lock=0   and a.id in (select project_id from t_projects_service_income aaaa
                    where  service_money > 0 and  service_id=272 and aaaa.project_id=a.id) or a.is_economic_census=1 ) '''+ add_sql)
            pagination = Pagination(page, pre_page, count.count, self.request)
            startpage = (page - 1) * pre_page
            datas = self.db.query('''
                     SELECT  a.*,d.*,a.id project_id, b.team_list,c.acc_uid,c.acc_uid_name,d.id  economic_census_id
                    
        
                FROM t_projects a
                inner join '''+options.mysql_database_customer+'''.t_customer c
                on a.customer_company=c.company 
                left join t_projects_economic_census d on a.id=d.project_id 
                left join (select project_id,GROUP_CONCAT(concat(member_name,'|',team_id)) team_list
                from t_projects_member group by project_id )  b
				 on a.id=b.project_id
                   where  (is_lock=0   and a.id in (select project_id from t_projects_service_income aaaa
                    where  service_money > 0 and  service_id=272 and aaaa.project_id=a.id)
                    or  a.is_economic_census=1)
                     '''+ add_sql+'''
                order by  a.economic_census_at desc,a.created_at desc limit %s,%s
                ''',startpage, pre_page)
            
            
            self.render(
            'common_milepost/economic_census.html',
            search_key='',
            tag=tag,
            datas=datas,
            pagination=pagination,
            params=params
            )

    @tornado.web.authenticated
    def post(self):
        tag = self.get_argument("tag", "list")
        uid = self.get_secure_cookie("uid")
        role=self.get_secure_cookie('role')
        uid_name = self.get_secure_cookie("name")
        dt=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        if tag=="save_tags":
            company_tags = self.get_argument('company_tags', '')
            company_guid = self.get_argument("company_guid")
            company_id=self.get_argument('company_id','')
            is_business_tag=self.get_argument('is_business_tag','')

            if is_business_tag:
                if company_id:
                    result=self.db.execute('''
                    update business_develop_manage set customer_tag=%s where id=%s and guid=%s
                    ''',company_tags,company_id,company_guid)
                    if result==0:
                        self.db.execute("""
                        insert into business_develop_manage_msg(uid,uid_name,message,created_at,business_id,tag_type,btype_id)
                        values(%s,%s,%s,%s,%s,%s,%s)
                        """, uid, uid_name,company_tags, dt, company_id, "操作标签",'1')

            else:
                if company_id:
                    self.db_company.execute('''
                    update t_company set customer_tag=%s,last_updated=%s , last_updated_type=%s,last_updated_msg=%s where id=%s and company_guid=%s
                ''', company_tags, dt, "操作标签", company_tags,company_id,
                                            company_guid)
                    self.db_company.execute("""
                    insert into t_company_msg(uid,uid_name,message,created_at,company_id,tag_type)
                    values(%s,%s,%s,%s,%s,%s)
                    """, uid, uid_name, company_tags, dt, company_id, "操作标签")
        elif tag == "close":
            company_id = self.get_argument('company_id', '')
            company_guid = self.get_argument("company_guid")
            close = self.get_argument("close")
            if company_id:
                if close=="1":
                    msg = "标记:无需求"
                elif close == "2":
                    msg = "标记:空号"
                self.db_company.execute('''
                update t_company set last_updated=%s , last_updated_type=%s,last_updated_msg=%s,is_close=%s,close_at=%s,close_uid=%s,close_uid_name=%s where id=%s and company_guid=%s
            ''', dt, "标记状态", msg, close,dt,uid,uid_name, company_id, company_guid)
                self.db_company.execute("""
                            insert into t_company_msg(uid,uid_name,message,created_at,company_id,tag_type)
                            values(%s,%s,%s,%s,%s,%s)
                            """, uid, uid_name, msg, dt, company_id, "标记状态")


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
                    if count.count>=600 and role!='15':
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
            company_id=self.get_argument('company_id',0)
            rel_id = self.get_argument("rel_id",0)
            ext_id = self.get_argument("ext_id",0)
            btype_id = self.get_argument("btype_id",0)

            if company_id:
                self.db_company.execute("""
                insert into t_company_msg(uid,uid_name,message,created_at,company_id,tag_type,rel_id,ext_id,btype_id)
                values(%s,%s,%s,%s,%s,%s,%s,%s,%s)
                """, uid, uid_name, msg, dt, company_id, "跟进记录",rel_id,ext_id,btype_id)

                self.db_company.execute("update t_company set last_updated=%s,last_updated_msg=%s where id=%s",dt,msg,company_id)
        
        elif tag=='business_develop_manage':
            guid=uuid.uuid4()
            busniess_from=self.get_argument('busniess_from','')
            customer_name=self.get_argument('customer_name','')
            company=self.get_argument('company','')
            phone=self.get_argument('phone','')
            project_request=self.get_argument('project_request','')
            source_keyword=self.get_argument('source_keyword','')
            source_way=self.get_argument('source_way','')
            source_place=self.get_argument('source_place','')
            source_port=self.get_argument('source_port','')
            remark=self.get_argument('remark','')
            referrer=self.get_argument('referrer','')
            be_referrer_company=self.get_argument('be_referrer_company','')
            be_referrer_name=self.get_argument('be_referrer_name','')
            be_referrer_phone=self.get_argument('be_referrer_phone','')
            business_guid=self.get_argument('business_guid','')
            business_id=self.get_argument('business_id','')
            business_from_id=busniess_from.split('|')[0]
            business_from_name=busniess_from.split('|')[1]
            if source_way:
                source_way_name=source_way.split('|')[1]
                source_way_id=source_way.split('|')[0]
            else:
                source_way_name=''
                source_way_id='0'
            
            if source_place:
                source_place_name=source_place.split('|')[1]
                source_place_id=source_place.split('|')[0]
            else:
                source_place_name=''
                source_place_id='0'
            if source_port:
                source_port_name=source_port.split('|')[1]
                source_port_id=source_port.split('|')[0]
            else:
                source_port_name=''
                source_port_id='0'
            
            if business_from_id!='2':
                t_customer = self.db_customer.get(
                        "select * from t_customer where company=%s",
                        company)
                if not t_customer:
                    return self.write("-1")
            if business_id and business_guid:
                self.db.execute('''
                    update business_develop_manage set business_from_id=%s,business_from_name=%s,
                customer_name=%s,company=%s,phone=%s,project_request=%s,source_keyword=%s,source_way_name=%s,source_way_id=%s,
                    source_place_name=%s,source_place_id=%s,source_port_name=%s,source_port_id=%s,remark=%s,referrer=%s,be_referrer_company=%s,
                    be_referrer_name=%s,be_referrer_phone=%s where id=%s and guid=%s
                ''',business_from_id,business_from_name,
                customer_name,company,phone,project_request,source_keyword,source_way_name,source_way_id,
                    source_place_name,source_place_id,source_port_name,source_port_id,remark,referrer,be_referrer_company,
                    be_referrer_name,be_referrer_phone,business_id,business_guid)
            else:
                
                result=self.db.execute('''
                    insert into business_develop_manage(business_from_id,business_from_name,
                customer_name,company,phone,project_request,source_keyword,source_way_name,source_way_id,
                    source_place_name,source_place_id,source_port_name,source_port_id,remark,referrer,be_referrer_company,
                    be_referrer_name,be_referrer_phone,guid,created_at,uid,uid_name) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
                ''',business_from_id,business_from_name,
                customer_name,company,phone,project_request,source_keyword,source_way_name,source_way_id,
                    source_place_name,source_place_id,source_port_name,source_port_id,remark,referrer,be_referrer_company,
                    be_referrer_name,be_referrer_phone,guid,dt,uid,uid_name)
                if result>0:
                    self.db.execute('''
                        insert into business_develop_manage_milepost(business_id) values(%s)
                    ''',result)

        elif tag=='business_develop_manage_milepost':
            business_id=self.get_argument('business_id','')
            step=self.get_argument('step','')
            gendan_name=self.get_argument('gendan_name','')
            business_milepost_id=self.get_argument('business_milepost_id','')
            msg = self.get_argument('msg', '')
            checked_status=self.get_argument('checked_status','')
        
            if step=='1':
                t_user=self.db.get(' select * from t_user  where name=%s',gendan_name)
                if not t_user:
                    self.write('-1')
                else:
                    result=self.db.execute('''
                    update  business_develop_manage_milepost set  assigner_name=%s, assigner_id=%s,assigner_at=%s,
                    jiedan_name=%s,jiedan_id=%s where id=%s
                    ''',uid_name,uid,dt,t_user.name,t_user.id,business_milepost_id)
                    if result==0:
                        self.db.execute("""
                        insert into business_develop_manage_msg(uid,uid_name,message,created_at,business_id,tag_type,btype_id)
                        values(%s,%s,%s,%s,%s,%s,%s)
                        """, uid, uid_name,'设置跟进人为'+t_user.name, dt, business_id, "操作记录",'2')
            
            elif step=='2':
                result=self.db.execute('''
                    update  business_develop_manage_milepost set jiedan_at=%s where id=%s
                    ''',dt,business_milepost_id)
                if result==0:
                    self.db.execute("""
                        insert into business_develop_manage_msg(uid,uid_name,message,created_at,business_id,tag_type,btype_id)
                        values(%s,%s,%s,%s,%s,%s,%s)
                        """, uid, uid_name,uid_name+'已接单', dt, business_id, "操作记录",'2')
            
            elif step=='3':
                result=self.db.execute('''
                    update  business_develop_manage_milepost set banjie_at=%s where id=%s
                    ''',dt,business_milepost_id)
                if result==0:
                    self.db.execute("""
                        insert into business_develop_manage_msg(uid,uid_name,message,created_at,business_id,tag_type,btype_id)
                        values(%s,%s,%s,%s,%s,%s,%s)
                        """, uid, uid_name,uid_name+'确认办结', dt, business_id, "操作记录",'2')

            elif step=='4':
                result=self.db.execute('''
                    update  business_develop_manage_milepost set checked_at=%s,checked_name=%s,checked_id=%s,
                    checked_status=%s where id=%s
                    ''',dt,uid_name,uid,checked_status,business_milepost_id)
                if result==0:
                    if checked_status=='1':
                        message=uid_name+'审核通过'
                    elif checked_status=='2':
                        message=uid_name+'审核不通过'
                    self.db.execute("""
                        insert into business_develop_manage_msg(uid,uid_name,message,created_at,business_id,tag_type,btype_id)
                        values(%s,%s,%s,%s,%s,%s,%s)
                        """, uid, uid_name,message, dt, business_id, "操作记录",'2')
        
        elif tag=="economic_census":
        
            step=self.get_argument('step')
            project_id=self.get_argument('project_id','')
            banjie_remark=self.get_argument('banjie_remark','')
            economic_census_id=self.get_argument('economic_census_id','')
            file_path1=self.get_argument('file_path','')
            
            len1=int(self.get_argument('len','0'))
            if step=='other_add':
                t_project=self.db.get('''
                select a.*,b.acc_uid_name,b.acc_uid
                 FROM t_projects a
                left join '''+options.mysql_database_customer+'''.t_customer b
                on a.customer_company=b.company 
                   where  a.id not in (select project_id from t_projects_service_income aaaa
                    where  service_money > 0 and  service_id=272 and aaaa.project_id=a.id) and a.id=%s
                ''',project_id)
                if not t_project:
                    self.write('-1')
                elif not t_project.acc_uid:
                    self.write('-2')
                else:
                    result=self.db.execute('''
                    update t_projects set is_economic_census=1,economic_census_at=%s where id=%s
                    ''',dt,project_id)
                    if result==0:
                        self.write('/company?tag=economic_census&step=1&ok=1')
                    else:
                        self.write('-3')
            elif step=='1':
                t=self.db.get(' select * from t_projects_economic_census where project_id=%s'%project_id)
                if not t:
                    self.db.execute('''
                        insert into t_projects_economic_census(jiedan_name,jiedan_id,jiedan_at,project_id)
                        values(%s,%s,%s,%s)
                    ''',uid_name,uid,dt,project_id)
            elif step=='3':
                print('长度'+str(len1))
                for i in range(len1):
                    file_path=''
                    try:
                        file1 = self.request.files['file'+str(i)][0]
                        is_upload = True
                    except:
                        pass
                    if is_upload:
                        ori_filename = file1["filename"]
                        filename_full = options.upload_path + "/economic_census/%s/" % (project_id)
                        url_path = "/static/economic_census/%s/" % (project_id)
                        try:
                            os.makedirs(filename_full)
                        except OSError:
                            if not os.path.isdir(filename_full):
                                raise

                        uuid_str = str(uuid.uuid4())
                        fname = "{0}".format(ori_filename)

                        save_full_path = filename_full + fname
                        url_fname = "{0}{1}".format(url_path, fname)

                        output_file = open(save_full_path, 'w')
                        output_file.write(file1["body"])
                        file_path += url_fname+'|'
                    if file_path:
                        self.db.execute('''
                            update t_projects_economic_census set banjie_at=%s,file_path=concat(%s,file_path),banjie_remark=%s where project_id=%s
                        ''',dt,file_path,banjie_remark,project_id)
            
            elif step=='4':
                self.db.execute('''
                    update t_projects_economic_census set  kj_check_at=%s,kj_check_name=%s,kj_check_id=%s,
                    kj_check_status=1 where project_id=%s
                ''',dt,uid_name,uid,project_id)
            elif step=='5':
                self.db.execute('''
                    update t_projects_economic_census set  kj_check_at=%s,kj_check_name=%s,kj_check_id=%s,
                    kj_check_status=2 where project_id=%s
                ''',dt,uid_name,uid,project_id)
            elif step=='7':
                result=self.db.execute('''
                update t_projects_economic_census set file_path=replace(file_path,%s,''),
                banjie_at=if(file_path='',null,banjie_at)
                 where id=%s
                ''',file_path1+'|',economic_census_id)
                if result==0:
                    path=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))+file_path1.replace('/static','/media')
                    os.remove(path)

                