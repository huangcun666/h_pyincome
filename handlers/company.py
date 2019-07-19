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
import events
reload(sys)
sys.setdefaultencoding('utf8')
from Pagination import Pagination
logger = logging.getLogger('boilerplate.' + __name__)
import datetime

#客户
class CompanyHandler(BaseHandler):
    def get_projects(self,project_ids):
        return self.db.query(' select id,guid from t_projects where find_in_set(id,%s) ',project_ids)
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
            category_id = self.get_argument("category_id", "")
            ntag=self.get_argument('ntag','')
            business_from_id=self.get_argument('business_from_id','')
            search_key=self.get_argument('search_key','')
            genjin_days_start=self.get_argument('genjin_days_start','')
            genjin_days_end=self.get_argument('genjin_days_end','')
            genjin_count_start=self.get_argument('genjin_count_start','')
            genjin_count_end=self.get_argument('genjin_count_end','')
            customer_tag=self.get_argument('customer_tag','')
            genjin_name=self.get_argument('genjin_name','')
            is_valid_business=self.get_argument('is_valid_business','')
            created_name=self.get_argument('created_name','')
            referrer_name=self.get_argument('referrer_name','')
            deal_type=self.get_argument('deal_type','1')
            check_type=self.get_argument('check_type','all')
            create_time=self.get_argument('create_time','')
            created_name_start=self.get_argument('created_name_start','')
            created_name_end=self.get_argument('created_name_end','')
            project_id=self.get_argument('project_id','')
            customer_name=self.get_argument('customer_name','')
            customer_tel=self.get_argument('customer_tel','')
            show_tag=self.get_argument('show_tag','')
            pre_page=20
            params={
                'business_from_id':business_from_id,
                'search_key':search_key,
                'genjin_days_start':genjin_days_start,
                'genjin_days_end':genjin_days_end,
                'genjin_count_start':genjin_count_start,
                'genjin_count_end':genjin_count_end,
                'customer_tag':customer_tag,
                'genjin_name':genjin_name,
                'is_valid_business':is_valid_business,
                'created_name':created_name,
                'referrer_name':referrer_name,
                'deal_type':deal_type,
                'check_type':check_type,
                'create_time':create_time,
                'created_name_start':created_name_start,
                'created_name_end':created_name_end,
                'step':step,
                'category_id':category_id,
                'project_id':project_id,
                'customer_name':customer_name,
                'customer_tel':customer_tel,
                'ntag':ntag,
                'show_tag':show_tag
            }
            business_from_name=''
            if business_from_id=='294':
                business_from_name='推广商机'
            elif business_from_id=='295':
                business_from_name='反馈商机'
            customer_tag_name=''
            if customer_tag:
                for item in customer_tag.split(','):
                    customer_tag_name+=item.split('_')[1]+',' if item else ''
            search_created_time=create_time
            if create_time=='自定义':
                search_created_time=created_name_start+'至'+created_name_end
            search_params={
                '反馈人':referrer_name,
                '创建时间:':search_created_time,
                '创建人:':created_name,
                '业务标签:':customer_tag_name,
                '联系方式:':customer_tel,
                '客户姓名:':customer_name,
                '确认单:':project_id,
                '编号/客户/电话/公司:':search_key,
                '商机类型:':business_from_name
            }
          
            sql=' and a.is_invalid_business=0 '
            count_sql=''
            count_sql1=''
            genjin_count_sql=' where 0=0  '
            if step=='1':
                sql=' and a.is_invalid_business=0 and b.assigner_at is null and b.be_assigner_ids="" and b.banjie_at is null and b.checked_at is null '
            
            elif step=='2':
                if '283' not in role_list and '284' not in role_list and '300' not in role_list:
                    sql=' and a.is_invalid_business=0 and b.assigner_at is not null and if(a.uid='+uid+', b.jiedan_at is null and b.banjie_at is null and b.checked_at is null,not find_in_set("'+uid+'_'+uid_name+'",b.be_assigner_confirm_ids) )  '
                else:
                    sql=' and a.is_invalid_business=0 and b.assigner_at is not null and b.jiedan_at is null and b.banjie_at is null and b.checked_at is null '
            elif step=='3':
                sql=' and a.is_invalid_business=0 and b.assigner_at is not null and b.jiedan_at is not null and b.banjie_at is null and b.checked_at is null '
            elif step=='4':
                sql=' and a.is_invalid_business=0 and b.assigner_at is not null and b.jiedan_at is not null and b.banjie_at is not null and b.checked_at is null '
            elif step=='5':
                sql=' and a.is_invalid_business=0 and b.assigner_at is not null and b.jiedan_at is not null and b.banjie_at is not null and b.checked_at is not null and b.checked_status=1 and b.banjie_typle=1 '
            elif step=='6':
                sql='  and b.assigner_at is not null and b.jiedan_at is not null and b.banjie_at is not null and b.checked_at is not null and b.checked_status=2 '
            elif step=='7':
                sql=' and a.is_invalid_business=0 and b.assigner_at is not null and b.jiedan_at is not null and b.banjie_at is not null and b.checked_at is not null  and b.banjie_typle=2 '
            elif step=='anomaly':
                sql=''' and a.is_invalid_business=0 inner join '''+options.mysql_database_customer+'''.t_customer aa 
                 on a.company=aa.company  inner join '''+options.mysql_database_customer+'''
                   .t_linkman aaa on aa.id=aaa.customer_id and a.phone=aaa.tel and a.feedback_type_id=4
                '''
            elif step=='invalid_business':
                sql=' and a.is_invalid_business=1 '

            if business_from_id:
                sql+=' and a.business_from_id=%s '%business_from_id
            if create_time=='今天':
                sql+=' and date_format(a.created_at,"%%Y-%%m-%%d")=date_format(now(),"%%Y-%%m-%%d") '
            elif create_time=='昨天':
                sql+=' and TIMESTAMPDIFF(DAY,date_format(a.created_at,"%%Y-%%m-%%d"),date_format(now(),"%%Y-%%m-%%d"))=1 '
            elif create_time=='最近7天':
                sql+=' and TIMESTAMPDIFF(DAY,date_format(a.created_at,"%%Y-%%m-%%d"),date_format(now(),"%%Y-%%m-%%d"))<7 '
            elif create_time=='最近30天':
                sql+=' and TIMESTAMPDIFF(DAY,date_format(a.created_at,"%%Y-%%m-%%d"),date_format(now(),"%%Y-%%m-%%d"))<30 '
            elif create_time=='自定义':
                if created_name_start and created_name_end:
                    sql+=' and a.created_at between "%s" and "%s" '%(created_name_start,created_name_end)
            if search_key:
                sql_add=''
                if search_key.isdigit():
                    sql_add=' or  a.id='+search_key
                sql+=' and (a.first_link_name="'+search_key+\
                '" or if(a.business_from_id=295 and (a.feedback_type_id=2 or a.feedback_type_id=3),be_referrer_company,a.company) like "%%'\
                +search_key+'%%" or  a.first_link_phone="'+search_key+'" '+sql_add+')'
            if genjin_days_start and genjin_days_end:
                sql+=''' and 
            datediff(DATE_FORMAT(if(banjie_at is null,now(),banjie_at), '%%Y-%%m-%%d'),DATE_FORMAT(assigner_at,'%%Y-%%m-%%d'))
              between "'''+genjin_days_start+'''" and "'''+genjin_days_end+'''"
                '''
            if is_valid_business:
                sql+=' and is_valid_business=%s '%is_valid_business
            if step=='3':
                if deal_type=='1':
                    sql+=' and length(b.be_assigner_ids)-length(REPLACE (b.be_assigner_ids, ",", ""))>=1  '
                elif deal_type=='2':
                    sql+=' and length(b.be_assigner_ids)-length(REPLACE (b.be_assigner_ids, ",", ""))>1  '
                elif deal_type=='3':
                    sql+=' and a.uid=%s '%uid
            if check_type=='1':
                sql+=' and b.banjie_typle=1 '
            elif check_type=='2':
                sql+=' and b.banjie_typle=2 '
            if customer_tag:
                for item in customer_tag.split(','):
                    if item:
                        if item.split('_')[2]=='成交（业务）':
                            genjin_count_sql+=' and  find_in_set("%s",ts.service_names) '%item
                        else:
                            sql+=' and (find_in_set("%s",customer_tag) or find_in_set("%s",project_request)) '%(item,item)


            if genjin_count_start and genjin_count_end:    
                genjin_count_sql+=' and ee.genjin_count between "'+genjin_count_start+'" and "'+genjin_count_end+'" '
            if project_id.isdigit():
                genjin_count_sql+=' and find_in_set(%s,a.project_id) '%project_id
            if customer_name:
                genjin_count_sql+=' and t.customer_name="%s" '%customer_name
            if customer_tel:
                genjin_count_sql+=' and t.customer_tel="%s" '%customer_tel

            if genjin_name:
                sql+=' and b.jiedan_name="%s" '%genjin_name
            if referrer_name:
                sql+=' and a.referrer="%s" '%referrer_name
            if created_name:
                sql+=' and a.uid_name="%s" '%created_name
            
            
            t_user_relation=self.db.get('''
                select group_concat(a.uid) gc from t_user_relation a
                inner join t_user_relation b on
                    find_in_set(a.department_name,b.department_name)
                and b.uid=%s and b.is_leader<>0
                where a.uid!=b.uid and a.is_leader=0
            ''',uid)
            if uid=='161':
                t_user_relation=self.db.get('''
                select group_concat(id) gc from t_user where role=10 and id!=%s 
            ''',uid)
            if show_tag=="subordinate" and t_user_relation.gc!=None:
                if step!='7':
                    sql+=' and find_in_set(a.uid,"%s") '%str(t_user_relation.gc)
                count_sql=' and find_in_set(a.uid,"%s") '%str(t_user_relation.gc)
                count_sql1=' and find_in_set(a.uid,"%s") '%str(t_user_relation.gc)
                
                if step!='2' and step and step!='1' and step!='7':
                    sql+=' and find_in_set(a.uid,"%s") '%str(t_user_relation.gc)
        
            elif '283' not in role_list and '284' not in role_list and '300' not in role_list:
                if step!='7':
                    sql+=' and (a.uid=%s or find_in_set(%s,b.be_assigner_ids)) '%(uid,uid)
                count_sql=' and (a.uid='+uid+' or find_in_set('+uid+',b.be_assigner_ids)) and if(a.uid='+uid+',a.uid='+uid+', find_in_set("'+uid+'_'+uid_name+'",b.be_assigner_confirm_ids) ) '
                count_sql1=' and (a.uid=%s or find_in_set(%s,b.be_assigner_ids)) '%(uid,uid)
                
                if step!='2' and step and step!='1' and step!='7':
                    sql+=' and if(a.uid='+uid+',a.uid='+uid+', find_in_set("'+uid+'_'+uid_name+'",b.be_assigner_confirm_ids) )  ' 
            
            # else:
            #     if step=='2':
            #         sql+=' or (find_in_set(%s,b.be_assigner_ids) and not find_in_set("%s",b.be_assigner_confirm_ids)) '%(uid,(uid+'_'+uid_name))
         
            t_talk_type = self.db.query(
            "select * from t_projects_type where income_category='沟通方式' order by order_int desc "
                )
            t_business_channel = self.db.query("""
                select * from t_projects_type where income_category='推广来源渠道'
                
                 order by id 
                """)
            t_income_type = self.db.query("""
                select * from t_projects_type where income_category='商机来源'
                """)
            t_port_type=self.db.query('''
                 select * from t_projects_type where income_category='来源端口'
            ''')
            t_categories = self.db.query(
                """
                select a.*,b.count from t_projects_category a
                left join(
                    select count(*) count,c.category_id,c.uid 
                     from business_develop_manage_category c
                    inner join business_develop_manage a on c.business_id=a.id
            inner join business_develop_manage_milepost b on a.id=b.business_id """+sql+"""
                      group by category_id,uid
                )b on a.id=b.category_id and a.uid=b.uid
                 where a.uid=%s  and a.is_business=1 order by a.order_int,a.id """,
                uid)
            if ntag=='ungroup':
                sql+='''  and not find_in_set(a.id,if((select group_concat(business_id) 
                from business_develop_manage_category where uid=%s group by uid ) is null,'',
                (select group_concat(business_id) 
                from business_develop_manage_category where uid=%s group by uid )
                )) '''%(uid,uid)
            elif category_id:
                sql+='''
                    inner join business_develop_manage_category f on a.id=f.business_id
                    and f.category_id=%s
                '''%category_id
            count=self.db.get('''
            select count(*) count,
            (
                select count(*) from business_develop_manage a
            inner join business_develop_manage_milepost b on a.id=b.business_id and a.is_invalid_business=0 '''+count_sql1+'''
            )count1,
             (
                select count(*) from business_develop_manage a
            inner join business_develop_manage_milepost b on a.id=b.business_id and 
             a.is_invalid_business=0 and b.assigner_at is null and b.be_assigner_ids="" 
              and b.banjie_at is null and b.checked_at is null '''+count_sql1+'''
            )count2,
            (
                select count(*) from business_develop_manage a
            inner join business_develop_manage_milepost b on a.id=b.business_id 
            and a.is_invalid_business=0 and b.assigner_at is not null 
             and if(a.uid=%s, b.jiedan_at is null and b.banjie_at is null 
              and b.checked_at is null,not find_in_set("'''+uid+'_'+uid_name+'''",b.be_assigner_confirm_ids) )
              and (a.uid=%s or find_in_set(%s,b.be_assigner_ids)) 
            )count31,
            (
                select count(*) from business_develop_manage a
            inner join business_develop_manage_milepost b on a.id=b.business_id 
            and a.is_invalid_business=0 and b.assigner_at is not null and b.jiedan_at is null
            and b.banjie_at is null and b.checked_at is null '''+count_sql1+'''
            )count32,
            (
                select count(*) from business_develop_manage a
            inner join business_develop_manage_milepost b on a.id=b.business_id 
            and a.is_invalid_business=0 and b.assigner_at is not null and b.jiedan_at is not null 
             and b.banjie_at is null and b.checked_at is null '''+count_sql+'''
            )count4,
            (
                select count(*) from business_develop_manage a
            inner join business_develop_manage_milepost b on a.id=b.business_id 
            and a.is_invalid_business=0 and b.assigner_at is not null and b.jiedan_at is not null 
             and b.banjie_at is not null and b.checked_at is null '''+count_sql+'''
            )count5,
            (
                select count(*) from business_develop_manage a
            inner join business_develop_manage_milepost b on a.id=b.business_id 
            and a.is_invalid_business=0 and b.assigner_at is not null and b.jiedan_at is not null 
             and b.banjie_at is not null and b.checked_at is not null and b.checked_status=1 and b.banjie_typle=1 '''+count_sql+'''
            )count6,
            (
                select count(*) from business_develop_manage a
            inner join business_develop_manage_milepost b on a.id=b.business_id 
            and b.assigner_at is not null and b.jiedan_at is not null 
             and b.banjie_at is not null and b.checked_at is not null and b.checked_status=2 '''+count_sql+'''
            )count7,
            (
            select count(*) from business_develop_manage a
            inner join business_develop_manage_milepost b on a.id=b.business_id 
            and a.is_invalid_business=0 and b.assigner_at is not null and b.jiedan_at is not null 
            and b.banjie_at is not null and b.checked_at is not null  and b.banjie_typle=2
            )count8,
            (
                select count(*) from business_develop_manage a
            inner join business_develop_manage_milepost b on a.id=b.business_id '''+count_sql+'''
            and a.is_invalid_business=0 inner join '''+options.mysql_database_customer+'''.t_customer aa 
                 on a.company=aa.company  inner join '''+options.mysql_database_customer+'''
                   .t_linkman aaa on aa.id=aaa.customer_id and a.phone=aaa.tel and a.feedback_type_id=4 
            )count9,
            (
                select count(*) from business_develop_manage a
            inner join business_develop_manage_milepost b on a.id=b.business_id and a.is_invalid_business=1 '''+count_sql+'''
            )count10
             from business_develop_manage a
            inner join business_develop_manage_milepost b on a.id=b.business_id 
            '''+sql+''' left join (
            select count(*) genjin_count,e.business_id,e.uid from 
             ( select uid,business_id from business_develop_manage_msg where btype_id=3 group by 
             DATE_FORMAT(created_at,'%%Y-%%m-%%d'),uid,business_id
              ) e  group by business_id,uid) ee on ee.uid=b.jiedan_id and ee.business_id=a.id
              left join (select group_concat(service_id,'_',service_name,'_','成交（业务）') service_names,project_id 
             from t_projects_service_income where service_money <> 0 or is_free=1  group by project_id) ts on a.project_id=ts.project_id 
            left join t_projects t on a.project_id=t.id
              '''+genjin_count_sql+'''
            ''',uid,uid,uid)
            pagination = Pagination(page, pre_page, count.count, self.request)
            startpage = (page-1) * pre_page
            business_develop_manage=self.db.query('''
            select a.*,b.be_assigner_ids,concat(if(a.project_request is not null and a.project_request!='',concat(a.project_request,','),'')
            ,if(ts.service_names is not null and ts.service_names!='',ts.service_names,'') ,if(a.customer_tag is not null and a.customer_tag!='',a.customer_tag,'')) customer_tag,b.id business_milepost_id,
            b.jiedan_name,b.be_assigner_names,c.uid_name  msg_uid_name,c.message,c.btype_id,c.created_at msg_created_at,ee.genjin_count,
            if(assigner_at,
            datediff(DATE_FORMAT(if(banjie_at is null,now(),banjie_at), '%%Y-%%m-%%d'),DATE_FORMAT(assigner_at,'%%Y-%%m-%%d')),
            ''
            ) gen_jin_days,
            g.category_name,g.id business_category_id,
if(ff.created_at is not null,datediff(DATE_FORMAT(now(),'%%Y-%%m-%%d'),DATE_FORMAT(ff.created_at,'%%Y-%%m-%%d')),null) new_genjin_day
             from business_develop_manage a
            inner join business_develop_manage_milepost b on a.id=b.business_id '''+sql+'''
             left join (select group_concat(service_id,'_',service_name,'_','成交（业务）') service_names,project_id 
             from t_projects_service_income where service_money <> 0 or is_free=1  group by project_id) ts on a.project_id=ts.project_id 
             left join business_develop_manage_msg  c
             on c.business_id=a.id
            and c.id=(select max(id) id from  business_develop_manage_msg where business_id=a.id ) 
            left join business_develop_manage_category g on a.id=g.business_id and g.uid=%s
                
             left join (
            select count(*) genjin_count,e.business_id,e.uid from 
             ( select uid,business_id from business_develop_manage_msg where btype_id=3 group by 
             DATE_FORMAT(created_at,'%%Y-%%m-%%d'),uid,business_id
              ) e  group by business_id,uid) ee on ee.uid=b.jiedan_id and ee.business_id=a.id
             left join (select business_id,max(created_at) created_at from 
              business_develop_manage_msg f1 where f1.btype_id=3 
              and find_in_set(f1.uid,(select be_assigner_ids from business_develop_manage_milepost 
               where business_id=f1.business_id)) group by business_id) ff on a.id=ff.business_id 
              '''+genjin_count_sql+'''
             order by c.created_at desc,a.created_at desc limit %s,%s
            ''',uid,startpage,pre_page)
            t_company_tag_group = self.db_company.query("""
                       select tag_category,GROUP_CONCAT(tag_name,"_",id) gc from t_company_tag where is_hide=1 group by tag_category
                        order by order_int
                    """)
            t_projects_type=self.db.query(' SELECT * FROM t_projects_type where income_category="业务类型" ')
            self.render('company/business_develop_manage.html',
            search_key="",
            tag=tag,
            t_user_relation=t_user_relation,
            step=step,
            ntag=ntag,
            count=count,
            get_projects=self.get_projects,
            t_company_tag_group=t_company_tag_group,
            t_projects_type=t_projects_type,
            t_categories=t_categories,
            category_id=category_id,
            pagination=pagination,
            business_develop_manage=business_develop_manage,
            t_talk_type=t_talk_type,
            t_business_channel=t_business_channel,
            t_income_type=t_income_type,
            t_port_type=t_port_type,
            params=params,
            search_params=search_params
            )

        elif tag=="show_business":
            guid=self.get_argument('guid')
            id=self.get_argument('id')
            step=self.get_argument('step','')
            category_id = self.get_argument("category_id", "")
            ntag=self.get_argument('ntag','')
            business_from_id=self.get_argument('business_from_id','')
            search_key=self.get_argument('search_key','')
            genjin_days_start=self.get_argument('genjin_days_start','')
            genjin_days_end=self.get_argument('genjin_days_end','')
            genjin_count_start=self.get_argument('genjin_count_start','')
            genjin_count_end=self.get_argument('genjin_count_end','')
            customer_tag=self.get_argument('customer_tag','')
            genjin_name=self.get_argument('genjin_name','')
            is_valid_business=self.get_argument('is_valid_business','')
            created_name=self.get_argument('created_name','')
            referrer_name=self.get_argument('referrer_name','')
            deal_type=self.get_argument('deal_type','1')
            check_type=self.get_argument('check_type','all')
            create_time=self.get_argument('create_time','')
            created_name_start=self.get_argument('created_name_start','')
            created_name_end=self.get_argument('created_name_end','')
            page=int(self.get_argument('page','1'))
            pre_page=1
            params={
                'business_from_id':business_from_id,
                'search_key':search_key,
                'genjin_days_start':genjin_days_start,
                'genjin_days_end':genjin_days_end,
                'genjin_count_start':genjin_count_start,
                'genjin_count_end':genjin_count_end,
                'customer_tag':customer_tag,
                'genjin_name':genjin_name,
                'is_valid_business':is_valid_business,
                'created_name':created_name,
                'referrer_name':referrer_name,
                'deal_type':deal_type,
                'check_type':check_type,
                'create_time':create_time,
                'created_name_start':created_name_start,
                'created_name_end':created_name_end,
                'step':step,
                'category_id':category_id,
                'ntag':ntag
            }
            sql=' and a.is_invalid_business=0 '
            genjin_count_sql=''
            business_develop_manage=self.db.get('''
            select *,a.id business_id,b.id business_milpost_id,b.jiedan_name,b.banjie_at,
            concat(if(a.project_request is not null and a.project_request!='',concat(a.project_request,','),''),
            if(a.customer_tag is not null and a.customer_tag!='',a.customer_tag,'')) customer_tags,
            find_in_set(%s,be_assigner_ids) is_be_assigner,find_in_set(%s,be_assigner_confirm_ids) is_be_assigner_confirm,
            if(assigner_at,
            datediff(DATE_FORMAT(if(banjie_at is null,now(),banjie_at), '%%Y-%%m-%%d'),DATE_FORMAT(assigner_at,'%%Y-%%m-%%d')),
            '') gen_jin_days,ee.genjin_count
             from business_develop_manage a
             inner join business_develop_manage_milepost b on a.id=b.business_id
              left join (
            select count(*) genjin_count,e.business_id,e.uid from 
             ( select uid,business_id from business_develop_manage_msg where btype_id=3 group by 
             DATE_FORMAT(created_at,'%%Y-%%m-%%d'),uid,business_id
              ) e  group by business_id,uid) ee on ee.uid=b.jiedan_id and ee.business_id=a.id
              where a.id=%s and a.guid=%s
            ''',uid,uid+'_'+uid_name,id,guid)

            if step=='invalid_business':
                sql=' and a.is_invalid_business=1 '
            elif step=='anomaly':
                sql=''' and a.is_invalid_business=0 inner join '''+options.mysql_database_customer+'''.t_customer aa 
                 on a.company=aa.company  inner join '''+options.mysql_database_customer+'''
                   .t_linkman aaa on aa.id=aaa.customer_id and a.phone=aaa.tel and a.feedback_type_id=4
                '''
            
            elif step=='invalid_business':
                sql=' and a.is_invalid_business=1 '
            elif step:
                if business_develop_manage.assigner_at:
                    sql+=' and b.assigner_at is not null '
                else:
                    sql+=' and b.assigner_at is null '
                if not business_develop_manage.be_assigner_ids:
                    sql+=' and b.be_assigner_ids="" '
                if business_develop_manage.jiedan_at:
                    sql+=' and b.jiedan_at is not null '
                else:
                    sql+=' and b.jiedan_at is null '
                if business_develop_manage.banjie_at:
                    sql+=' and b.banjie_at is not null '
                else:
                    sql+=' and b.banjie_at is null '
                if business_develop_manage.checked_at:
                    sql+=' and b.checked_at is not null '
                else:
                    sql+=' and b.checked_at is null '
                sql+=' and b.checked_status=%s '%business_develop_manage.checked_status
                
                if business_develop_manage.banjie_typle:
                    sql+=' and b.banjie_typle=%s '%business_develop_manage.banjie_typle
                else:
                    sql+=' and b.banjie_typle is null '

            if '283' not in role_list and '284' not in role_list and '300' not in role_list:
                if step and step!='invalid_business' and step!='anomaly':
                    if uid+'_'+uid_name in business_develop_manage.be_assigner_confirm_ids:
                        sql+=' and find_in_set("'+uid+'_'+uid_name+'",b.be_assigner_confirm_ids) '
                    elif uid+'_'+uid_name not in business_develop_manage.be_assigner_confirm_ids:
                        sql=' and a.is_invalid_business=0 and b.assigner_at is not null \
                             and (not find_in_set("'+uid+'_'+uid_name+'",b.be_assigner_confirm_ids) \
                                  or a.uid=%s and b.jiedan_at is null and b.banjie_at is null and b.checked_at is null) '%uid

                sql+=' and (a.uid=%s or find_in_set(%s,b.be_assigner_ids)) '%(uid,uid)
            
            if business_from_id:
                sql+=' and a.business_from_id=%s '%business_from_id
            if create_time=='今天':
                sql+=' and date_format(a.created_at,"%%Y-%%m-%%d")=date_format(now(),"%%Y-%%m-%%d") '
            elif create_time=='昨天':
                sql+=' and TIMESTAMPDIFF(DAY,date_format(a.created_at,"%%Y-%%m-%%d"),date_format(now(),"%%Y-%%m-%%d"))=1 '
            elif create_time=='最近7天':
                sql+=' and TIMESTAMPDIFF(DAY,date_format(a.created_at,"%%Y-%%m-%%d"),date_format(now(),"%%Y-%%m-%%d"))<7 '
            elif create_time=='最近30天':
                sql+=' and TIMESTAMPDIFF(DAY,date_format(a.created_at,"%%Y-%%m-%%d"),date_format(now(),"%%Y-%%m-%%d"))<30 '
            elif create_time=='自定义':
                if created_name_start and created_name_end:
                    sql+=' and a.created_at between "%s" and "%s" '%(created_name_start,created_name_end)
            if search_key:
                sql_add=''
                if search_key.isdigit():
                    sql_add=' or  a.id='+search_key
                sql+=' and (a.first_link_name="'+search_key+\
                '" or if(a.business_from_id=295 and (a.feedback_type_id=2 or a.feedback_type_id=3),be_referrer_company,a.company) like "%%'\
                +search_key+'%%" or  a.first_link_phone="'+search_key+'" '+sql_add+')'
            if genjin_days_start and genjin_days_end:
                sql+=''' and 
            datediff(DATE_FORMAT(if(banjie_at is null,now(),banjie_at), '%%Y-%%m-%%d'),DATE_FORMAT(assigner_at,'%%Y-%%m-%%d'))
              between "'''+genjin_days_start+'''" and "'''+genjin_days_end+'''"
                '''
            if is_valid_business:
                sql+=' and is_valid_business=%s '%is_valid_business
            if step=='3':
                if deal_type=='1':
                    sql+=' and length(b.be_assigner_ids)-length(REPLACE (b.be_assigner_ids, ",", ""))>=1  '
                elif deal_type=='2':
                    sql+=' and length(b.be_assigner_ids)-length(REPLACE (b.be_assigner_ids, ",", ""))>1  '
                elif deal_type=='3':
                    sql+=' and a.uid=%s '%uid
            if check_type=='1':
                sql+=' and b.banjie_typle=1 '
            elif check_type=='2':
                sql+=' and b.banjie_typle=2 '
            if customer_tag:
                for item in customer_tag.split(','):
                    if item:
                        sql+=' and (find_in_set("%s",customer_tag) or find_in_set("%s",project_request)) '%(item,item)


            if genjin_count_start and genjin_count_end:    
                genjin_count_sql=' where ee.genjin_count between "'+genjin_count_start+'" and "'+genjin_count_end+'" '
            if genjin_name:
                sql+=' and b.jiedan_name="%s" '%genjin_name
            if referrer_name:
                sql+=' and a.referrer="%s" '%referrer_name
            if created_name:
                sql+=' and a.uid_name="%s" '%created_name

            if ntag=='ungroup':
                sql+='''  and not find_in_set(a.id,if((select group_concat(business_id) 
                from business_develop_manage_category where uid=%s group by uid ) is null,'',
                (select group_concat(business_id) 
                from business_develop_manage_category where uid=%s group by uid )
                )) '''%(uid,uid)
            elif category_id:
                sql+='''
                    inner join business_develop_manage_category f on a.id=f.business_id
                    and f.category_id=%s
                '''%category_id


            t_project=''
            t_talk_type = self.db.query(
            "select * from t_projects_type where income_category='沟通方式' order by order_int desc "
                )
            t_business_channel = self.db.query("""
                select * from t_projects_type where income_category='推广来源渠道'
                 and (id=64 or id=65 or id=67 or id=66 or id=311)
                 order by order_int desc
                """)
            t_income_type = self.db.query("""
                select * from t_projects_type where income_category='商机来源'
                """)
            t_port_type=self.db.query('''
                 select * from t_projects_type where income_category='来源端口'
            ''')
            t_company_tag_group = self.db_company.query("""
                       select tag_category,GROUP_CONCAT(tag_name,"_",id) gc from t_company_tag where is_hide=1 group by tag_category order by order_int 

                    """)
            business_develop_manage_msg=self.db.query('''
            select *,date_format(created_at,"%%Y-%%m-%%d")=date_format(now(),"%%Y-%%m-%%d") is_current_day  from business_develop_manage_msg where business_id=%s order by created_at desc
            ''',id)
            print(sql)
            business_develop_manage_all=self.db.query('''
            select a.id,a.guid
             from business_develop_manage a
            inner join business_develop_manage_milepost b on a.id=b.business_id '''+sql+'''
              '''+genjin_count_sql+'''
            left join business_develop_manage_msg  c
             on c.business_id=a.id
            and c.id=
                 (select max(id) id from  business_develop_manage_msg where business_id=a.id group by business_id  
             ) 
             order by c.created_at desc,a.created_at desc 
            ''')
            next_business=''
            pre_business=''
            if {'guid':guid,'id':long(id)} in business_develop_manage_all:
                current_num=business_develop_manage_all.index({'guid':guid,'id':long(id)})
                next_num=current_num+1
                pre_num=current_num-1
                if next_num<=len(business_develop_manage_all)-1:
                    next_business=business_develop_manage_all[next_num]
                if pre_num>=0:
                    pre_business=business_develop_manage_all[pre_num]
            t_type = self.db_company.query("select * from t_type where type_category='销售计划'")
            t_plan = self.db_company.query(
                        "select * from t_plan where business_id=%s",id)
            if business_develop_manage.project_id:
                t_project=self.db.query(''' 
                select a.*,if(b.service_names is null,'',b.service_names)service_names from t_projects a 
                left join ( select group_concat(service_name) service_names,project_id
                from t_projects_service_income where (service_money <> 0 or is_free=1) group by project_id ) b on a.id=b.project_id 
                where find_in_set(a.id,%s) '''
                ,business_develop_manage.project_id)
            phone_related_business=self.db.query('''
            select b.*,a.guid
            from business_develop_manage a inner join 
            business_develop_manage_milepost b on a.id=b.business_id
            inner join business_develop_manage c on
            if(a.business_from_id=295 and a.feedback_type_id in (2,3),a.be_referrer_phone,a.phone)=if(c.business_from_id=295 and c.feedback_type_id in (2,3),c.be_referrer_phone,c.phone)  where c.id=%s and a.id!=c.id and if(c.business_from_id=295 and c.feedback_type_id in (2,3),c.be_referrer_phone<>'',c.phone<>'')
            ''',id)
            business_develop_manage_linkman=self.db.query(' select * from business_develop_manage_linkman where business_id=%s order by is_first desc',id)
            customers=self.db_customer.query("""
                SELECT  d.is_check,d.id assist_id,d.summary,
                    TIMESTAMPDIFF(MONTH,c.acc_end, DATE_FORMAT(now(), "%%Y-%%m-%%d")) tsm,
                     datediff(DATE_FORMAT(now(),'%%Y-%%m-%%d'),DATE_FORMAT(d.check_at, '%%Y-%%m-%%d')) wj_day,
                        d.*,d.sale_id assist_sale_id,d.id assist_id, DATE_ADD(c.acc_end, INTERVAL 1 MONTH) next_pay_acc_start , a.acc_uid_name a_acc_uid_name ,
                            DATE_ADD(c.acc_end, INTERVAL a.fee MONTH) next_pay_acc_end,
                            DATE_ADD(c.acc_book_end, INTERVAL 1 MONTH) next_pay_acc_book_start ,
                            DATE_ADD(c.acc_book_end, INTERVAL a.fee MONTH) next_pay_acc_book_end, c.*,
                            a.id customer_id,a.guid,a.company,c.updated_at pay_updated_at,c.uid_name pay_uid_name,
                            c.pay_typeid_name pay_pay_typeid_name,c.service_amount pay_service_amount,
                            a.last_cuikuan_at,a.last_cuikuan_msg,a.sale_last_cuikuan_at,a.sale_last_cuikuan_msg,
                                c.service_month_amount pay_service_amount_month, c.book_amount pay_book_amount,
                                f.member_name sale_man,e.member_name kf_man,c.sale_man sale_man1,c.kf_man kf_man1, g.id sale_cuikuan_id
                                                                    FROM  t_customer_payment_assist d
                                                                      inner join t_customer a on d.customer_id=a.id
                                                                        INNER JOIN t_customer_payment c
                                                                            ON a.id = c.customer_id
                                                                        left join """+options.mysql_database+""".t_projects_member f on
                                                                        c.project_id=f.project_id and f.team_id=34
                                                                        left join """+options.mysql_database+""".t_projects_member e on
                                                                                c.project_id=e.project_id and e.team_id=36
                                                                   left join t_customer_exchange g on a.id=g.customer_id and  g.isvisible=2
                                                                    and g.id=(select MAX(gg.id) g_id from t_customer_exchange gg where a.id=gg.customer_id and gg.isvisible=2 )
                                                                        INNER JOIN
                                                                        (
                                                                            SELECT `customer_id`, MAX(id) max_id,acc_end
                                                                            FROM t_customer_payment
                                                                            GROUP BY customer_id
                                                                        ) b ON c.customer_id = b.customer_id AND
                                                                                b.max_id = c.id where d.is_bad_debts=1 and d.id=%s""",business_develop_manage.assist_id)
            if not business_develop_manage:
                self.write('订单'+id+'不存在')
            
            else:
                self.render('company/show_business.html',
                params=params,
                search_key='',
                t_talk_type=t_talk_type,
                t_type=t_type,
                t_plan=t_plan,
                t_project=t_project,
                customers=customers,
                business_develop_manage_linkman=business_develop_manage_linkman,
                t_company_tag_group=t_company_tag_group,
                t_business_channel=t_business_channel,
                t_income_type=t_income_type,
                t_port_type=t_port_type,
                phone_related_business=phone_related_business,
                business_develop_manage=business_develop_manage,
                business_develop_manage_msg=business_develop_manage_msg,
                next_business=next_business,
                pre_business=pre_business
                )   

        elif tag=="business_develop_manage_statistics":
            my=self.get_argument('my','')
            page=int(self.get_argument('page','1'))
            search_referrer=self.get_argument('search_referrer','')
            statistics_type=self.get_argument('statistics_type','fankui')
            invalid=self.get_argument('invalid','')
            fenpei_type=self.get_argument('fenpei_type','new_tuiguang')
            start_time=self.get_argument('start_time','')
            end_time=self.get_argument('end_time','')
            way=self.get_argument('way','')
            pre_page=20
            sql=''
            sql_date=''
            params={
                'my':my,
                'search_referrer':search_referrer,
                'statistics_type':statistics_type,
                'invalid':invalid,
                'fenpei_type':fenpei_type,
                'start_time':start_time,
                'end_time':end_time,
                'way':way
            }
            select_name=''
            inner_sql=''
            date_sql=' created_at '
            if start_time and end_time:
                sql_date= ' and created_at between "%s" and "%s" '%(start_time,end_time)
            
            date_format_sql="'%%Y-%%m-%%d'"
            if way=='day':
                date_format_sql="'%%Y-%%m-%%d'"
            elif way=='month':
                date_format_sql="'%%Y-%%m'"
            elif way=='week':
                date_format_sql="'%%Y-%%m-%%u'"

            if statistics_type=='fankui':
                if my:
                    sql+=' and referrer_id="%s" '%uid
                if search_referrer:
                    sql+=' and referrer="%s" '%search_referrer
                select_name='referrer'
                sql+=' and referrer <> "" and a.business_from_id=295 '
                inner_sql=''
            elif statistics_type=='tuiguang':
                if my:
                    sql+=' and uid=%s '%uid
                if search_referrer:
                    sql+=' and uid_name="%s" '%search_referrer
                select_name='uid_name'
                if invalid:
                    sql+=' and a.business_from_id=294 and  a.is_invalid_business=1 '
                else:
                    sql+=' and  a.business_from_id=294 and  a.is_invalid_business!=1  '
                inner_sql=' inner join business_develop_manage_milepost b on a.id=b.business_id  '
            elif statistics_type=='fenpei':
                inner_sql=' inner join business_develop_manage_milepost b on a.id=b.business_id   '
                if fenpei_type=='new_tuiguang' or fenpei_type=='new_fankui':
                    if my:
                        sql+=' and substring_index(b.be_assigner_ids,",",1)="%s" '%uid
                    if search_referrer:
                        sql+=' and substring_index(b.be_assigner_names,",",1)="%s" '%search_referrer
                    select_name=' substring_index(b.be_assigner_names,",",1) '
                    date_sql=' assigner_at '
                    if start_time and end_time:
                        sql_date= ' and assigner_at between "%s" and "%s" '%(start_time,end_time)

                    if fenpei_type=='new_tuiguang':
                        sql+=' and  a.business_from_id=294 '
                    elif fenpei_type=='new_fankui':
                        sql+=' and  a.business_from_id=295 '                        
                    sql+='  and  a.is_invalid_business!=1  and b.be_assigner_names<>""  '
                elif fenpei_type=='fq_tuiguang' or fenpei_type=='fq_fankui':
                    if my:
                        sql+=' and banjie_id=%s '%uid
                    if search_referrer:
                        sql+=' and banjie_name="%s" '%search_referrer
                    select_name=' banjie_name '
                    date_sql=' banjie_at '
                    if start_time and end_time:
                        sql_date= ' and banjie_at between "%s" and "%s" '%(start_time,end_time)
                    if fenpei_type=='fq_tuiguang':
                        sql+=' and a.business_from_id=294 '
                    elif fenpei_type=='fq_fankui':
                        sql+=' and a.business_from_id=295 '
                    sql+=' and  a.is_invalid_business!=1  and b.banjie_typle=2 '
                elif fenpei_type=='transfer_tuiguang' or fenpei_type=='transfer_fankui':
                    if my:
                        sql+=' and raw_jiedan_id=%s '%uid
                    if search_referrer:
                        sql+=' and raw_jiedan_name="%s" '%search_referrer
                    select_name=' raw_jiedan_name '
                    date_sql=' b.created_at '
                    if start_time and end_time:
                        sql_date= ' and b.created_at between "%s" and "%s" '%(start_time,end_time)

                    if fenpei_type=='transfer_tuiguang':
                        sql+=' and a.business_from_id=294 '
                    elif fenpei_type=='transfer_fankui':
                        sql+=' and a.business_from_id=295 '
                    inner_sql=' inner join business_develop_manage_transfer b on a.id=b.business_id   '
            count=self.db.get('''
                select count(*) count,sum(sc) ssc,
                (
                select group_concat(name,'|',count) from
                (select '''+select_name+''' name,count(*) count from 
                business_develop_manage a '''+inner_sql+''' where 0=0'''+sql+''' group by name order by count desc)a
                ) every_count
                from (
                select group_concat(name,'|',count),df,sum(count) sc from (
                select '''+select_name+''' name,date_format('''+date_sql+''','''+date_format_sql+''') df,count(*)  count
                from business_develop_manage a '''+inner_sql+''' where 0=0 '''+sql+sql_date+''' group by '''+select_name+''',df)aa
                group by df)aaa
            ''')
            pagination=Pagination(page,pre_page,count.count,self.request)
            startpage=(page-1)*pre_page
            datas=self.db.query('''
                select group_concat(name,'|',count) gc,df,sum(count) sc from (
                select '''+select_name+''' name,date_format('''+date_sql+''','''+date_format_sql+''') df,count(*)  count
                from business_develop_manage a '''+inner_sql+''' where 0=0 '''+sql+sql_date+''' group by name,df)aa
                group by df order by df desc limit %s,%s
            ''',startpage,pre_page)
            print('''
              select group_concat(name,'|',count) gc,df,sum(count) sc from (
                select '''+select_name+''' name,date_format('''+date_sql+''','''+date_format_sql+''') df,count(*)  count
                from business_develop_manage a '''+inner_sql+''' where 0=0 '''+sql+sql_date+''' group by name,df)aa
                group by df order by df desc
            ''')
            self.render(
            'company/business_develop_manage_statistics.html',
            search_key='',
            datas=datas,
            tag=tag,
            params=params,
            pagination=pagination,
            count=count)

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
                    where  (service_money > 0 or is_free=1 ) and  service_id=272 and aaaa.project_id=a.id) or a.is_economic_census=1 ) '''+ add_sql)
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
                    where  (service_money > 0 or is_free=1 )  and  service_id=272 and aaaa.project_id=a.id)
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
            company=self.get_argument('company','')
            t_customer=self.db_customer.get(' select id from t_customer where company="%s" '%company)
            if t_customer:
                customer_id=t_customer.id
            else:
                customer_id=0
            if is_business_tag:
                if company_id:
                    business_develop_manage=self.db.get(
                    ' select * from business_develop_manage where id=%s and guid=%s '
                    ,company_id,company_guid)
                    result=self.db.execute('''
                    update business_develop_manage set customer_tag=%s where id=%s and guid=%s
                    ''',company_tags,company_id,company_guid)
                    if (business_develop_manage.customer_tag if business_develop_manage.customer_tag else '')!=company_tags:
                        customer_tags=''
                        customer_tags1=''
                        if business_develop_manage.customer_tag:
                            for item in business_develop_manage.customer_tag.split(','):
                                customer_tags+=item.split('_')[1]+','
                        if company_tags:
                            for item in company_tags.split(','):
                                customer_tags1+=item.split('_')[1]+','
                        events.add_project_event(self,'0','客户标签(商机开发)',
                        customer_tags[:-1]+' 修改为 '+customer_tags1[:-1] 
                        ,uid,uid_name,customer_id,company_id)
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
            friend_introduce=self.get_argument('friend_introduce','0')
            feedback_type=self.get_argument('feedback_type','')
            business_from_id=busniess_from.split('|')[0]
            business_from_name=busniess_from.split('|')[1]
            link_gender=self.get_argument('link_gender','1')
            not_company=self.get_argument('not_company','0')
            txt=''
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
            if feedback_type:
                feedback_type_id=feedback_type.split('|')[0]
                feedback_type_name=feedback_type.split('|')[1]
            else:
                feedback_type_id=0
                feedback_type_name=''
            if business_from_id=='295' and (feedback_type_id!='4' and friend_introduce=='0'):
                t_customer = self.db_customer.get(
                        "select * from t_customer where company=%s",
                        company)
                if not t_customer and  not_company=='0' :
                    return self.write("-1")
                elif not_company=='1':
                    company='无'
            t_user=self.db.get(' select * from t_user where name=%s ',referrer)
            if t_user:
                referrer=t_user.name
                referrer_id=t_user.id
            else:
                referrer_id=0
                referrer=''
            if business_id and business_guid:
                self.db.execute('''
                    update business_develop_manage set business_from_id=%s,business_from_name=%s,
                    feedback_type_id=%s,
                    feedback_type_name=%s,
                customer_name=%s,company=%s,phone=%s,project_request=%s,source_keyword=%s,source_way_name=%s,source_way_id=%s,
                    source_place_name=%s,source_place_id=%s,source_port_name=%s,source_port_id=%s,remark=%s,referrer=%s,be_referrer_company=%s,
                    be_referrer_name=%s,be_referrer_phone=%s,friend_introduce=%s,referrer_id=%s,not_company=%s where id=%s and guid=%s
                ''',business_from_id,business_from_name,feedback_type_id,feedback_type_name,
                customer_name,company,phone,project_request[:-1],source_keyword,source_way_name,source_way_id,
                    source_place_name,source_place_id,source_port_name,source_port_id,remark,referrer,be_referrer_company,
                    be_referrer_name,be_referrer_phone,friend_introduce,referrer_id,not_company,business_id,business_guid)
        
            else:
                if business_from_id=='295' and feedback_type_id in ['2','3']:
                    link_name=be_referrer_name
                    link_tel=be_referrer_phone
                else:
                    link_name=customer_name
                    link_tel=phone
                result=self.db.execute('''
                    insert into business_develop_manage(business_from_id,business_from_name,
                    customer_name,company,phone,project_request,source_keyword,source_way_name,source_way_id,
                    source_place_name,source_place_id,source_port_name,source_port_id,remark,referrer,be_referrer_company,
                    be_referrer_name,be_referrer_phone,guid,created_at,uid,uid_name,friend_introduce,feedback_type_id,
                    feedback_type_name,referrer_id,first_link_name,first_link_phone,not_company) 
                    values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
                ''',business_from_id,business_from_name,
                    customer_name,company,phone,project_request[:-1],source_keyword,source_way_name,source_way_id,
                    source_place_name,source_place_id,source_port_name,source_port_id,remark,referrer,be_referrer_company,
                    be_referrer_name,be_referrer_phone,guid,dt,uid,uid_name,friend_introduce,feedback_type_id,
                    feedback_type_name,referrer_id,link_name,link_tel,not_company)
                if result>0:
                    self.db.execute("""
                                    insert into business_develop_manage_msg(uid,uid_name,message,created_at,business_id,tag_type,btype_id)
                                    values(%s,%s,%s,%s,%s,%s,%s)
                                    """, uid, uid_name,uid_name+'创建商机', dt,result, "操作记录",'2')
                    if link_tel:
                        self.db.execute('''
                            insert into business_develop_manage_linkman
                            (link_name,link_gender,link_tel,business_id,uid,uid_name,created_at,is_first)
                            values(%s,%s,%s,%s,%s,%s,%s,%s)
                        ''',link_name,link_gender,link_tel,result,uid,uid_name,dt,'1')
                    t_customer=self.db_customer.get(' select id from t_customer where company="%s" '%company)
                    if t_customer:
                        customer_id=t_customer.id
                    else:
                        customer_id=0
                    events.add_project_event(self,'0','创建商机开发(商机开发)',uid_name+'创建商机开发('+business_from_name+')',uid,uid_name,customer_id,result)
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
            businessid_milepostid_company=self.get_argument('businessid_milepostid_company','')
            company=self.get_argument('company','')
            banjie_type=self.get_argument('banjie_type','')
            project_id=self.get_argument('project_id','0')
            give_up_reason=self.get_argument('give_up_reason','')
            is_transfer=self.get_argument('is_transfer','')
            reallocate=self.get_argument('reallocate','')
            is_valid_business=self.get_argument('is_valid_business','0')
            is_invalid_business=self.get_argument('is_invalid_business','')
            referrer=self.get_argument('referrer','')
            business_from_id=self.get_argument('business_from_id','')
            add_project=self.get_argument('add_project','')
            t_customer=self.db_customer.get(' select id from t_customer where company="%s" '%company)
            if t_customer:
                customer_id=t_customer.id
            else:
                customer_id=0
            if step=='1':
                t_user=self.db.get(' select * from t_user  where name=%s',gendan_name)
                if not t_user and not is_invalid_business:
                    self.write('-1')
                else:
                    if businessid_milepostid_company:
                        for item in businessid_milepostid_company.split(','):
                            t_customer=self.db_customer.get(' select id from t_customer where company="%s" '%item.split('_')[2])
                            if t_customer:
                                customer_id=t_customer.id
                            else:
                                customer_id=0
                    
                            if is_transfer:
                                result=self.db.execute('''
                            update  business_develop_manage_milepost set  
                            be_assigner_names=replace(be_assigner_names,%s,%s),be_assigner_ids=replace(be_assigner_ids,%s,%s),
                            be_assigner_confirm_ids=replace(be_assigner_confirm_ids,%s,'') where id=%s
                            ''',uid_name+',',t_user.name+',',uid+',',str(t_user.id)+',',uid+'_'+uid_name+',',item.split('_')[1])
                            elif is_invalid_business:
                                result=self.db.execute('''
                                update business_develop_manage set is_invalid_business=%s where id=%s
                                ''',is_invalid_business,item.split('_')[0])
                                self.db.execute('''
                                update business_develop_manage_milepost set  assigner_name=%s, assigner_id=%s,assigner_at=%s
                                where id=%s
                                ''',uid_name,uid,dt,item.split('_')[1])
                            else:
                                if reallocate=='1':
                                    result=self.db.execute('''
                            update  business_develop_manage_milepost set  assigner_name=%s, assigner_id=%s,assigner_at=%s,
                            be_assigner_names=%s,be_assigner_ids=%s, be_assigner_confirm_ids="",jiedan_id=null,jiedan_at=null,banjie_at=null,checked_at=null,checked_name=null,
                            checked_id=null,checked_status=0,banjie_typle=null,give_up_reason=null,project_id=null where id=%s
                            ''',uid_name,uid,dt,t_user.name+',',str(t_user.id)+',',item.split('_')[1])
                                else:
                                    exist_gendan=self.db.get(' select * from business_develop_manage_milepost where find_in_set(%s,be_assigner_ids) and id=%s ',t_user.id,item.split('_')[1])
                                    if not exist_gendan:
                                        result=self.db.execute('''
                                    update  business_develop_manage_milepost set  assigner_name=%s, assigner_id=%s,assigner_at=if(assigner_at is null,%s,assigner_at),
                                    be_assigner_names=concat(be_assigner_names,%s),be_assigner_ids=concat(be_assigner_ids,%s) where id=%s
                                    ''',uid_name,uid,dt,t_user.name+',',str(t_user.id)+',',item.split('_')[1])
                                    else:
                                        result=-1
                            if result==0:
                                title='分配跟单人(商机开发)'
                                txt='设置'
                                if is_transfer:
                                    self.db.execute('''
                                insert into business_develop_manage_transfer
                                (business_id,milepost_id,raw_jiedan_id,raw_jiedan_name,transfer_id,transfer_name,created_at)
                                values(%s,%s,%s,%s,%s,%s,%s)
                                ''',item.split('_')[0],item.split('_')[1],uid,uid_name,t_user.id,t_user.name,dt)
                                    title='转让跟单人(商机开发)'
                                    txt='转让'
                                elif reallocate=='1':
                                    title='跟单人重新分配(商机开发)'
                                    txt='重新分配'
                                if is_invalid_business:
                                    events.add_project_event(self,'0','设置为反馈无效商机(商机开发)',uid_name+'设置为反馈无效商机',uid,uid_name,customer_id,item.split('_')[0])
                                    self.db.execute("""
                                    insert into business_develop_manage_msg(uid,uid_name,message,created_at,business_id,tag_type,btype_id)
                                    values(%s,%s,%s,%s,%s,%s,%s)
                                    """, uid, uid_name,uid_name+'设置为反馈无效商机', dt,item.split('_')[0], "操作记录",'2')
                                else:
                                    events.add_project_event(self,'0',title,'跟单人'+txt+'为'+t_user.name,uid,uid_name,customer_id,item.split('_')[0])
                                    self.db.execute("""
                                    insert into business_develop_manage_msg(uid,uid_name,message,created_at,business_id,tag_type,btype_id)
                                    values(%s,%s,%s,%s,%s,%s,%s)
                                    """, uid, uid_name,'跟进人'+txt+'为'+t_user.name, dt,item.split('_')[0], "操作记录",'2')
                      
                        if is_transfer:
                            self.write({'transfer':'1'})
                    else:
                        if is_invalid_business:
                            result=self.db.execute('''
                                update business_develop_manage set is_invalid_business=%s where id=%s
                                ''',is_invalid_business,business_id)
                            self.db.execute('''
                                update business_develop_manage_milepost set  assigner_name=%s, assigner_id=%s,assigner_at=%s
                                where id=%s
                                ''',uid_name,uid,dt,business_milepost_id)
                        elif reallocate=='1':
                                result=self.db.execute('''
                            update  business_develop_manage_milepost set  assigner_name=%s, assigner_id=%s,assigner_at=%s,
                            be_assigner_names=%s,be_assigner_ids=%s, be_assigner_confirm_ids="",jiedan_id=null,jiedan_at=null,banjie_at=null,checked_at=null,checked_name=null,
                            checked_id=null,checked_status=0,banjie_typle=null,give_up_reason=null,project_id=null where id=%s
                            ''',uid_name,uid,dt,t_user.name+',',str(t_user.id)+',',business_milepost_id)
                        else:
                            exist_gendan=self.db.get(' select * from business_develop_manage_milepost where find_in_set(%s,be_assigner_ids) and id=%s ',t_user.id,business_milepost_id)
                            if not exist_gendan:
                                result=self.db.execute('''
                                update  business_develop_manage_milepost set  assigner_name=%s, assigner_id=%s,assigner_at=%s,
                                be_assigner_names=concat(be_assigner_names,%s),be_assigner_ids=concat(be_assigner_ids,%s) where id=%s
                                ''',uid_name,uid,dt,t_user.name+',',str(t_user.id)+',',business_milepost_id)
                            else:
                                return self.write('跟单人已有')
                        if result==0:
                            if is_invalid_business:
                                events.add_project_event(self,'0','设置为反馈无效商机(商机开发)',uid_name+'设置为反馈无效商机',uid,uid_name,customer_id,business_id)
                                self.db.execute("""
                                insert into business_develop_manage_msg(uid,uid_name,message,created_at,business_id,tag_type,btype_id)
                                values(%s,%s,%s,%s,%s,%s,%s)
                                """, uid, uid_name,uid_name+'设置为反馈无效商机', dt,business_id, "操作记录",'2')
                            else:
                                title='分配跟单人(商机开发)'
                                txt='设置跟单人为'
                                if reallocate=='1':
                                    title='跟单人重新分配(商机开发)'
                                    txt='重新分配跟单人为'
                                events.add_project_event(self,'0',title,txt+t_user.name,uid,uid_name,customer_id,business_id)
                                self.db.execute("""
                                insert into business_develop_manage_msg(uid,uid_name,message,created_at,business_id,tag_type,btype_id)
                                values(%s,%s,%s,%s,%s,%s,%s)
                                """, uid, uid_name,txt+t_user.name, dt, business_id, "操作记录",'2')
            
            elif step=='2':
                result=self.db.execute('''
                    update  business_develop_manage_milepost set jiedan_at=if(jiedan_at is null,%s,jiedan_at),
                    jiedan_name=if(jiedan_name is null,%s,jiedan_name),
                    jiedan_id=if(jiedan_id is null,%s,jiedan_id),be_assigner_confirm_ids=concat(be_assigner_confirm_ids,%s) where id=%s
                    ''',dt,uid_name,uid,uid+'_'+uid_name+',',business_milepost_id)
                if result==0:
                    events.add_project_event(self,'0','接单(商机开发)','跟单人'+uid_name+'接单',uid,uid_name,customer_id,business_id)
                    self.db.execute("""
                        insert into business_develop_manage_msg(uid,uid_name,message,created_at,business_id,tag_type,btype_id)
                        values(%s,%s,%s,%s,%s,%s,%s)
                        """, uid, uid_name,uid_name+'已接单', dt, business_id, "操作记录",'2')
            
            elif step=='3':
                is_banjie=self.db.get('''
                select * from business_develop_manage_milepost where id=%s and banjie_at is not null
                ''',business_milepost_id)
                checked_status=is_banjie.checked_status if is_banjie else 0
                banjie_typle=is_banjie.banjie_typle if is_banjie else 0

                t_project=self.db.get('''
                     select id,recommend_staff from t_projects where id=%s
                    ''',project_id)
                if not t_project and banjie_type=='1':
                    return self.write({'project_id':'-1'})
                elif t_project and banjie_type=='1':
                    if referrer and business_from_id=='295' and (referrer!=t_project.recommend_staff or \
                        not t_project.recommend_staff or t_project.recommend_staff=='无推荐人' or t_project.recommend_staff=='无'):
                        return self.write({'project_id':'-2'})
                    elif business_from_id=='294' and t_project.recommend_staff and t_project.recommend_staff!='无推荐人' and t_project.recommend_staff!='无':
                        return self.write({'project_id':'-3'})
                if not is_banjie or checked_status==2 and banjie_typle==1:      
                    result=self.db.execute('''
                        update  business_develop_manage_milepost set banjie_at=%s,banjie_typle=%s,give_up_reason=%s,
                        project_id=%s,banjie_name=%s,banjie_id=%s,checked_at=null,checked_name=null,checked_id=null,checked_status=0 where id=%s
                        ''',dt,banjie_type,give_up_reason,project_id,uid_name,uid,business_milepost_id)
                    self.db.execute('''
                        update  business_develop_manage set 
                        
                        project_id=%s where id=%s
                        ''',project_id,business_id)
                    if result==0:
                        if banjie_type=='1':
                            txt=' 办结类型:已成交,确认单号:'+project_id
                        elif banjie_type=='2':
                            txt=' 办结类型:放弃,放弃理由:'+give_up_reason
                        events.add_project_event(self,'0','办结(商机开发)','跟单人'+uid_name+'办结'+txt,
                        uid,uid_name,customer_id,business_id)
                        self.db.execute("""
                            insert into business_develop_manage_msg(uid,uid_name,message,created_at,business_id,tag_type,btype_id)
                            values(%s,%s,%s,%s,%s,%s,%s)
                            """, uid, uid_name,'跟单人'+uid_name+'办结'+txt, dt, business_id, "操作记录",'2')
                else:
                    if add_project:
                        is_exist=self.db.get(''' select id from business_develop_manage where id=%s and find_in_set(%s,project_id) ''',business_id,project_id)
                        if is_exist:
                            return self.write({'project_id':'-4'})
                        result=self.db.execute('''
                        update  business_develop_manage_milepost set
                        project_id=CASE 
                            when project_id is not null and right(project_id,1)=',' then concat(project_id,%s)
                            when project_id is not null and right(project_id,1)!=',' then concat(project_id,%s)
                            end
                            where id=%s
                        ''',project_id+',',','+project_id+',',business_milepost_id)
                        self.db.execute('''
                        update  business_develop_manage set 
                            project_id=CASE 
                            when project_id is not null and right(project_id,1)=',' then concat(project_id,%s)
                            when project_id is not null and right(project_id,1)!=',' then concat(project_id,%s)
                            end
                            where id=%s
                        ''',project_id+',',','+project_id+',',business_id)
                        if result==0:
                            events.add_project_event(self,'0','添加确认单(商机开发)','跟单人'+uid_name+'添加确认单'+project_id,
                            uid,uid_name,customer_id,business_id)
                            self.db.execute("""
                                insert into business_develop_manage_msg(uid,uid_name,message,created_at,business_id,tag_type,btype_id)
                                values(%s,%s,%s,%s,%s,%s,%s)
                                """, uid, uid_name,'跟单人'+uid_name+'添加确认单'+project_id, dt, business_id, "操作记录",'2')
                    else:
                        self.write({'is_banjie':1,'banjie_name':is_banjie.banjie_name})

            elif step=='4':
                reallocate_name=self.get_argument('reallocate_name','')
                if checked_status=='3':
                    t_user=self.db.get(''' select * from t_user where name=%s ''',reallocate_name)
                    if not t_user:
                        return self.write('-1')
                    result=self.db.execute('''
                        update  business_develop_manage_milepost set  assigner_name=%s, assigner_id=%s,assigner_at=%s,
                        be_assigner_names=%s,be_assigner_ids=%s, be_assigner_confirm_ids="",jiedan_id=null,jiedan_at=null,banjie_at=null,checked_at=null,checked_name=null,
                        checked_id=null,checked_status=0,banjie_typle=null,give_up_reason=null,project_id=null where id=%s
                        ''',uid_name,uid,dt,t_user.name+',',str(t_user.id)+',',business_milepost_id)
                else:
                    result=self.db.execute('''
                        update  business_develop_manage_milepost set checked_at=%s,checked_name=%s,checked_id=%s,
                        checked_status=%s,is_valid_business=%s where id=%s
                        ''',dt,uid_name,uid,checked_status,is_valid_business,business_milepost_id)
                if result==0:
                    if checked_status=='1':
                        if is_valid_business!='0':
                            message=uid_name+'审核通过'+('(有效商机)' if is_valid_business=='1' else '(无效商机)')
                        else:
                            message=uid_name+'审核通过'

                    elif checked_status=='2':
                        message=uid_name+'审核不通过'
                    elif checked_status=='3':
                        message=uid_name+'审核:重新分配跟单人为'+reallocate_name
                    events.add_project_event(self,'0','审核(商机开发)',message,uid,uid_name,customer_id,business_id)
                    self.db.execute("""
                        insert into business_develop_manage_msg(uid,uid_name,message,created_at,business_id,tag_type,btype_id)
                        values(%s,%s,%s,%s,%s,%s,%s)
                        """, uid, uid_name,message, dt, business_id, "操作记录",'2')
            elif step=='5':
                be_change_id=self.get_argument('be_change_id')
                be_change_name=self.get_argument('be_change_name')
                change_name=self.get_argument('change_name')
                t_user=self.db.get(''' select * from t_user where name=%s ''',change_name)
                if not t_user:
                    return self.write('-1')
                result=self.db.execute(''' 
                    update  business_develop_manage_milepost set  
                    be_assigner_names=replace(be_assigner_names,%s,%s),be_assigner_ids=replace(be_assigner_ids,%s,%s),
                    be_assigner_confirm_ids=replace(be_assigner_confirm_ids,%s,'') where id=%s
                ''',be_change_name+',',t_user.name+',',be_change_id+',',str(t_user.id)+',',be_change_id+'_'+be_change_name+',',business_milepost_id)
                if result==0:
                    self.db.execute("""
                        insert into business_develop_manage_msg(uid,uid_name,message,created_at,business_id,tag_type,btype_id)
                        values(%s,%s,%s,%s,%s,%s,%s)
                        """, uid, uid_name,uid_name+'将跟进人'+be_change_name+'更改为'+t_user.name, dt, business_id, "操作记录",'2')
            elif step=='6':
                for item in businessid_milepostid_company.split(','):
                    result=self.db.execute('''
                    update  business_develop_manage_milepost set assigner_at=%s,
                    be_assigner_names=%s,be_assigner_ids=%s, be_assigner_confirm_ids=%s,jiedan_id=%s,
                    jiedan_at=%s,banjie_at=null,checked_at=null,checked_name=null,
                    checked_id=null,checked_status=0,banjie_typle=null,give_up_reason=null,project_id=null where id=%s
                    ''',dt,uid_name+',',uid+',',uid+'_'+uid_name+',',uid,dt,item.split('_')[1])
                    if result==0:
                        self.db.execute("""
                            insert into business_develop_manage_msg(uid,uid_name,message,created_at,business_id,tag_type,btype_id)
                            values(%s,%s,%s,%s,%s,%s,%s)
                            """, uid, uid_name,uid_name+'认领商机',dt, item.split('_')[0], "操作记录",'2')
            elif step=='7':
                delete_assistant_id=self.get_argument('delete_assistant_id','')
                delete_assistant_name=self.get_argument('delete_assistant_name','')
                result=self.db.execute(''' 
                    update  business_develop_manage_milepost set  
                    be_assigner_names=replace(be_assigner_names,%s,''),be_assigner_ids=replace(be_assigner_ids,%s,''),
                    be_assigner_confirm_ids=replace(be_assigner_confirm_ids,%s,'') where id=%s
                ''',delete_assistant_name+',',delete_assistant_id+',',delete_assistant_id+'_'+delete_assistant_name+',',business_milepost_id)
                if result==0:
                    self.db.execute("""
                        insert into business_develop_manage_msg(uid,uid_name,message,created_at,business_id,tag_type,btype_id)
                        values(%s,%s,%s,%s,%s,%s,%s)
                        """, uid, uid_name,uid_name+'删除协助人'+delete_assistant_name,dt,business_id, "操作记录",'2')
        elif tag=="business_develop_manage_genjin":
            txt_msg=self.get_argument('txt_msg')
            business_id=self.get_argument('business_id')
            company=self.get_argument('company','')
            t_customer=self.db_customer.get(' select id from t_customer where company="%s" '%company)
            if t_customer:
                customer_id=t_customer.id
            else:
                customer_id=0
            file_path=None
            is_upload = False
            try:
                file1 = self.request.files['file'][0]
                is_upload = True
            except:
                pass
            if is_upload:
                ori_filename = file1["filename"]
                filename_full = options.upload_path + "/business_manage/%s/" % (
                    business_id)
                url_path = "/static/business_manage/%s/" % (business_id)
                try:
                    os.makedirs(filename_full)
                except OSError:
                    if not os.path.isdir(filename_full):
                        raise
                extension = os.path.splitext(ori_filename)[1]

                fname =ori_filename

                save_full_path = filename_full + fname
                url_fname = "{0}{1}".format(url_path, fname)

                output_file = open(save_full_path, 'w')
                output_file.write(file1["body"])
                file_path = url_fname
            events.add_project_event(self,'0','跟单人跟进(商机开发)',txt_msg,uid,uid_name,customer_id,business_id)
            self.db.execute("""
                    insert into business_develop_manage_msg(uid,uid_name,message,created_at,business_id,tag_type,btype_id,file_path)
                    values(%s,%s,%s,%s,%s,%s,%s,%s)
                    """, uid, uid_name,txt_msg, dt, business_id, "跟进记录",'3',file_path)

        elif tag=="business_group_category":
            businessid_milepostid_company=self.get_argument('businessid_milepostid_company')
            category_id=self.get_argument('category_id')
            category_name=self.get_argument('category_name')
            for item in businessid_milepostid_company.split(','):
                if item.split('_')[3]:
                    self.db.execute('''
                        update business_develop_manage_category set category_id=%s,category_name=%s where id=%s
                    ''',category_id,category_name,item.split('_')[3])
                else:
                    self.db.execute('''
                    insert into business_develop_manage_category(category_id,category_name,uid,uid_name,created_at,business_id)
                    values(%s,%s,%s,%s,%s,%s)
                    ''',category_id,category_name,uid,uid_name,dt,item.split('_')[0])

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

        elif tag=="business_transfer":
            transfer_name=self.get_argument('transfer_name','')
            t_users=self.db.query('''
                select id,name from t_user where name like "%%'''+transfer_name+'''%%"
            ''')
            self.write({'t_users':t_users})
        
        elif tag=="delete_business_msg":
            msg_id=self.get_argument('msg_id')
            edit_msg=self.get_argument('edit_msg','')
            msg=self.get_argument('msg','')
            if edit_msg:
                self.db.execute(''' update business_develop_manage_msg set message=%s where id=%s ''',msg,msg_id)
            else:
                self.db.execute(' delete from business_develop_manage_msg where id=%s ',msg_id)
        
        elif tag=="business_linkman":
            link_name=self.get_argument('link_name','')
            link_gender=self.get_argument('link_gender','')
            link_tel=self.get_argument('link_tel','')
            link_remark=self.get_argument('link_remark','')
            business_id=self.get_argument('business_id','')
            linkman_id=self.get_argument('linkman_id','')
            is_first=self.get_argument('is_first','0')
            if not linkman_id:
                self.db.execute('''
                insert into business_develop_manage_linkman
                (link_name,link_gender,link_tel,link_remark,business_id,uid,uid_name,created_at,is_first)
                values(%s,%s,%s,%s,%s,%s,%s,%s,%s)
            ''',link_name,link_gender,link_tel,link_remark,business_id,uid,uid_name,dt,is_first)
            elif linkman_id:
                if  is_first=='1':
                    self.db.execute('''
                    update business_develop_manage_linkman set is_first=0 where business_id=%s ''',business_id) 
                self.db.execute('''
                update business_develop_manage_linkman set link_name=%s,link_gender=%s,
                link_tel=%s,link_remark=%s,uid=%s,uid_name=%s,is_first=%s where id=%s
                ''',link_name,link_gender,link_tel,link_remark,uid,uid_name,is_first,linkman_id)
            if is_first=='1':
                self.db.execute('''
                update business_develop_manage set first_link_name=%s,first_link_phone=%s
                    where id=%s ''',link_name,link_tel,business_id) 

