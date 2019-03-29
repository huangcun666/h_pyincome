# encoding=utf8
from handlers.base import BaseHandler
import logging
import json
import tornado.web
import urllib2
import tornado.httpclient
import sys, re, uuid
import urllib, os
import datetime
from tornado.options import define, options
reload(sys)
sys.setdefaultencoding('utf8')
from Pagination import Pagination
logger = logging.getLogger('boilerplate.' + __name__)


#客户
class FinanceHandler(BaseHandler):
    @tornado.web.authenticated
    def get(self):
        tag = self.get_argument("tag", "list")
        uid = self.get_secure_cookie("uid")
        uid_name = self.get_secure_cookie("name")

        if tag=="list":
            sql = ""
            sql1=''
            qtype = self.get_argument("qtype","my")
            state=self.get_argument('state','')
            keyword = self.get_argument("keyword","")
            page = int(self.get_argument("page", 1))
            if qtype=="my":
                sql = " and (e.acc_uid=%s or sale.member_id=%s)"%(uid,uid)
            pre_page = 20


            banjie_sql='''
                	left join  (select count(*) count,project_id from t_projects_member 
                     where team_id=38 and last_milepost_id!=167 and last_milepost_id!=162 and last_milepost_id!=0 group by project_id) h 
                    on h.project_id=b.id and h.count=(select count(*) count 
                    from t_projects_member where team_id=38 and project_id=b.id)
                '''
            if state=='1':    
                sql1=' where aaaa.sum_count=aaaa.sum_project '
            elif state=='2':
                sql1=' where aaaa.sum_count!=aaaa.sum_project '
              
            count = self.db.get('''
      select count(*) count,sum(all_income-dd) sum_qk
                        from 
                        (select 
                        acc_uid_name,customer_company,id,guid, bid, sale_id, sale_name,
                         all_income,
                     aa,  dd, sum_count,sum_project,sum_count1
                     
                     from 
                        ( select acc_uid_name,customer_company,e.id,e.guid,b.id bid,sale.member_id sale_id,sale.member_name sale_name,
                        ifnull(sum(all_income),0) all_income,
                        ifnull(sum(aa),0) aa, ifnull(sum(dd),0) dd 
                        ,sum(if(h.count>0,1,0)) sum_count,count(*) sum_project,sum(if(hh.count>0,-1,0)+if(h.count>0,1,0)) sum_count1
                        from  t_projects b
                    
                             	left join  (select count(*) count,project_id from t_projects_member 
                     where team_id=38 and (last_milepost_id=167 or last_milepost_id=162 or last_milepost_id=0) group by project_id) hh 
                    on hh.project_id=b.id
                                	left join  (select count(*) count,project_id from t_projects_member 
                     where team_id=38 and last_milepost_id!=167 and last_milepost_id!=162 and last_milepost_id!=0 group by project_id) h 
                    on h.project_id=b.id and h.count=(select count(*) count 
                    from t_projects_member where team_id=38 and project_id=b.id)  
                                    left join (select aa.project_id,ifnull(sum(income_money),0)  aa from t_projects_income aa
                                                                            ,t_projects_income_title bb 
                                                                            where aa.parent_id=bb.id and
                                                                            income_uid > 0 and income_id >43 group by aa.project_id) f
                                                                            on  b.id=f.project_id                                                   
                        
                                    left join ( select   aa.project_id,ifnull(sum(income_money),0)  dd from t_projects_income aa
                                                                    ,t_projects_income_title bb 
                                                                    where aa.parent_id=bb.id  and
                                                                    income_uid > 0 and income_id <=43  group by aa.project_id)  g  on 
                                                                            b.id=g.project_id 
    
                        left join t_projects_member sale on b.id=sale.project_id and sale.team_id=34 and sale.member_id!=0
                                    inner
                        join db_customer.t_customer e  on b.customer_company=e.company
                                                    where    customer_company!="" and (all_income -dd) > 0 
                                                         
                                                    '''
                                      + sql + '''
                                                    
                                                    group by customer_company,e.id,e.guid,acc_uid_name)aaaa
                                                    '''+sql1+'''
                                                    )aaaaa ''')
            pagination = Pagination(page, pre_page, count.count, self.request)
            startpage = (page - 1) * pre_page

            customers = self.db.query("""
                    select 
                        acc_uid_name,customer_company,id,guid, bid, sale_id, sale_name,
                         all_income,
                     aa,  dd, sum_count,sum_project,sum_count1
                        
                     from ( select acc_uid_name,customer_company,e.id,e.guid,b.id bid,sale.member_id sale_id,sale.member_name sale_name,
                        ifnull(sum(all_income),0) all_income,
                        ifnull(sum(aa),0) aa, ifnull(sum(dd),0) dd,sum(if(h.count>0,1,0)) sum_count,count(*) sum_project
                        ,sum(if(hh.count>0,-1,0)+if(h.count>0,1,0)) sum_count1
                        from  t_projects b
                        left join  (select count(*) count,project_id from t_projects_member 
                            where team_id=38 and (last_milepost_id=167 or last_milepost_id=162 or last_milepost_id=0) group by project_id) hh 
                            on hh.project_id=b.id
                        
                        left join  (select count(*) count,project_id from t_projects_member 
                            where team_id=38 and last_milepost_id!=167 and last_milepost_id!=162 and last_milepost_id!=0 group by project_id) h 
                            on h.project_id=b.id and h.count=(select count(*) count 
                            from t_projects_member where team_id=38 and project_id=b.id)  

                                    left join (select aa.project_id,ifnull(sum(income_money),0)  aa from t_projects_income aa
                                                                            ,t_projects_income_title bb 
                                                                            where aa.parent_id=bb.id and
                                                                            income_uid > 0 and income_id >43 group by aa.project_id) f
                                                                            on  b.id=f.project_id                                                   
                        
                                    left join ( select   aa.project_id,ifnull(sum(income_money),0)  dd from t_projects_income aa
                                                                    ,t_projects_income_title bb 
                                                                    where aa.parent_id=bb.id  and
                                                                    income_uid > 0 and income_id <=43  group by aa.project_id)  g  on 
                                                                            b.id=g.project_id 
                     
                        left join t_projects_member sale on b.id=sale.project_id and sale.team_id=34 and sale.member_id!=0
                                    inner
                        join db_customer.t_customer e  on b.customer_company=e.company
                                                    where    customer_company!="" and (all_income -dd) > 0 
                                                          
                                                    """
                                      + sql + """
                                                    
                                                    group by customer_company,e.id,e.guid,acc_uid_name)aaaa
                                                    """+sql1+"""
                                                    limit %s,%s
            """, startpage, pre_page)
            self.render(
                'c/finace/finance_list.html',
                keyword=keyword,
                customers=customers,
                state=state,
                pagination=pagination,
                tag=tag,
                count=count,
                qtype=qtype)
        
        elif tag=="show_customer_exchange":
            customer_id=self.get_argument('customer_id')
            show_more=''
            t_customer_exchange = self.db_customer.query(
                """select *  from t_customer_exchange where customer_id=%s and etype=3
                order by created_at desc """,
                customer_id)
            self.render('c/customer/show_customer_exchange.html',
                t_customer_exchange=t_customer_exchange,
                customer_id=customer_id,show_more=show_more)
    
    @tornado.web.authenticated
    def post(self):
        tag = self.get_argument("tag", "list")
        uid = self.get_secure_cookie("uid")
        uid_name = self.get_secure_cookie("name")    
        dt = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        if tag=="customer_exchange":
            msg=self.get_argument('msg')
            customer_id=self.get_argument('customer_id')
            etype=self.get_argument('etype')
            self.db_customer.execute('''
                insert into  t_customer_exchange(msg,customer_id,created_at,uid,uid_name,etype)
                values(%s,%s,%s,%s,%s,%s)''', msg,customer_id,dt,uid,uid_name, etype)

            t_customer_exchange = self.db_customer.query(
                """select *  from t_customer_exchange where customer_id=%s and etype=3 order by created_at desc """,
                customer_id)
            return self.render('c/customer/show_customer_exchange.html',
            t_customer_exchange=t_customer_exchange,
            show_more='1',
            customer_id=customer_id)
