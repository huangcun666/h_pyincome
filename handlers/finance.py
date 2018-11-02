# encoding=utf8
from handlers.base import BaseHandler
import logging
import json
import tornado.web
import urllib2
import tornado.httpclient
import sys, re, uuid
import urllib, os
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
            qtype = self.get_argument("qtype","my")
            keyword = self.get_argument("keyword","")
            page = int(self.get_argument("page", 1))
            if qtype=="my":
                sql = " and e.acc_uid=%s "%(uid)
            pre_page = 20
            count = self.db.get('''
      select count(*) count
                        from  t_projects b 
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
                                    inner
                        join db_customer.t_customer e  on b.customer_company=e.company
                                                    where   customer_company!=""  and (all_income -dd) > 0
                                                    

               ''' + sql)
            pagination = Pagination(page, pre_page, count.count, self.request)
            startpage = (page - 1) * pre_page

            customers = self.db.query("""
                    select acc_uid_name,customer_company,e.id,e.guid,
                        ifnull(sum(all_income),0) all_income,
                        ifnull(sum(aa),0) aa, ifnull(sum(dd),0) dd 

                        from  t_projects b 
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
                                    inner
                        join db_customer.t_customer e  on b.customer_company=e.company
                                                    where    customer_company!="" and (all_income -dd) > 0  """
                                      + sql + """
                                                    
                                                    group by customer_company,e.id,e.guid,acc_uid_name

                                                    limit %s,%s
            """, startpage, pre_page)
            self.render(
                'c/finace/finance_list.html',
                keyword=keyword,
                customers=customers,
                pagination=pagination,
                tag=tag,
                qtype=qtype)
