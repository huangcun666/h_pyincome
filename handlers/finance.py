# encoding=utf8
from handlers.base import BaseHandler
import logging
import json
import tornado.web
import urllib2
import tornado.httpclient
import sys, re, uuid
import urllib, os,xlwt
import datetime
from tornado.options import define, options
reload(sys)
sys.setdefaultencoding('utf8')
from Pagination import Pagination
logger = logging.getLogger('boilerplate.' + __name__)


#客户
class FinanceHandler(BaseHandler):
    def RepresentsInt(self,s):
        try: 
            int(s)
            return True
        except ValueError:
            return False
    def get_member(self,mbs,team_name):
        if mbs:
            for r in mbs.split(","):
                if r:
                    mb = r.split("|")
                    if mb[0]==team_name:
                        return mb[1]
    @tornado.web.authenticated
    def get(self):
        tag = self.get_argument("tag", "list")
        uid = self.get_secure_cookie("uid")
        uid_name = self.get_secure_cookie("name")
        role = self.get_secure_cookie("role")
        export_data=self.get_argument('export_data','')
        if tag=="finance_project_list":
            sql = ""
            sql1=''
            qtype = self.get_argument("qtype","my")
            state=self.get_argument('state','')
            keyword = self.get_argument("keyword","")
            page = int(self.get_argument("page", 1))
            start = self.get_argument("start","")
            end = self.get_argument("end","")
            if role!="8" and role!="5" and role!="3":
                sql = " and (a.uid_name='%s')"%(uid_name)
            pre_page = 20
            if qtype=='my':
                sql+=' and a.uid=%s '%uid
            if keyword:
                id_sql=""
                if self.RepresentsInt(keyword):
                    id_sql = "  b.id='%s'"%(keyword) +" or "
                sql+= ''' and (''' +id_sql+''' a.customer_name like "%%''' + keyword + '''%%" or a.project_name like "%%''' + keyword + '''%%" or a.customer_tel like "%%''' + keyword +'''%%" or a.customer_company like "%%'''+keyword+'''%%")'''
            banjie_sql='''
                	left join  (select count(*) count,project_id from t_projects_member 
                     where team_id=38 and last_milepost_id!=167 and last_milepost_id!=162 and last_milepost_id!=0 group by project_id) h 
                    on h.project_id=b.id and h.count=(select count(*) count 
                    from t_projects_member where team_id=38 and project_id=b.id)
                '''
            if start and end:
                sql+="  and a.created_at between '%s' and '%s' "%(start,end)
            if not state:
                sql+='''
                    and a.id not in (select project_id from t_checked_finance_project 
                  where project_id=a.id and checked_status=1) and is_finance_project is null
                '''
            elif state=='1':    
                sql+='''
                and a.id not in (select project_id from t_checked_finance_project 
                  where project_id=a.id and checked_status=1) and is_finance_project=1
                '''
            elif state=='2':
                sql1='''
                inner join t_checked_finance_project f 
                 on a.id=f.project_id and f.checked_status=1 and 
                 f.id=(select max(id) from t_checked_finance_project 
                  where project_id=a.id group by project_id)
                '''
            if export_data=='export':
                customers = self.db.query("""
                                    select aa.* from (
                                    select is_finance_project,customer_name,guid,a.created_at,a.uid_name create_project_name,ifnull(daishou_money,0) daishou_money,mbs,a.id,all_income,ifnull(b.income_money,0) income_money,ifnull(other_money,0) other_money,
                                    ifnull(((all_income+ifnull(other_money,0)) -( ifnull(b.income_money,0)+ifnull(daishou_money,0))),0) qk,customer_company,project_name
                                    from t_projects a 
                                    left join (select b1.project_id,ifnull(sum(income_money),0) income_money from t_projects_income b1 ,t_projects_income_title b2 where
                                    b1.parent_id=b2.id and income_id <=43 and  income_uid > 0   group by b1.project_id) b 
                                    on a.id=b.project_id 
                                    left join (select project_id,ifnull(sum(income_money),0) other_money from t_projects_income_other  group by project_id) c 
                                    on a.id=c.project_id 
                                    left join (select project_id,group_concat(team_name,"|",member_name)  mbs from t_projects_member where member_id > 0 group by project_id ) d  
                                    on a.id=d.project_id  
                                    left join (select e1.project_id,ifnull(sum(income_money),0) daishou_money from t_projects_income e1,t_projects_income_title e2 where 
                                    e1.parent_id=e2.id and 
                                    income_id >43  and  income_uid > 0  group by e1.project_id) e 
                                    on a.id=e.project_id """+sql1+""" where 0=0 """+sql+"""
                                    group by a.id) aa where  qk <> 0 or is_finance_project=1""")
                wb = xlwt.Workbook()
                sh = wb.add_sheet(u'确认单应收表')
                sh.write(0, 0, u"编号")
                sh.write(0, 1, u"创建日期")
                sh.write(0, 2, u"业务名称")
                sh.write(0, 3, u"公司名称")
                sh.write(0, 4, u"联系人")
                sh.write(0, 5, u"总服务费")
                sh.write(0, 6, u"待收代收款")
                sh.write(0, 7, u"已收款")
                sh.write(0, 8, u"已收代收款")
                sh.write(0, 9, u"欠款")
                sh.write(0, 10, u"销售顾问")
                sh.write(0, 11, u"客服顾问")
                sh.write(0, 12, u"创建人")
                for idx,item in enumerate(customers):
                    idx+=1
                    sh.write(idx,0,item.id)
                    sh.write(idx,1,item.created_at.strftime('%Y-%m-%d'))
                    sh.write(idx,2,item.project_name)
                    sh.write(idx,3,item.customer_company)
                    sh.write(idx,4,item.customer_name)
                    sh.write(idx,5,item.all_income)
                    sh.write(idx,6,item.other_money)
                    sh.write(idx,7,item.income_money)
                    sh.write(idx,8,item.daishou_money)
                    sh.write(idx,9,item.qk)
                    sh.write(idx,10,(self.get_member(item.mbs,"销售顾问") if self.get_member(item.mbs,"销售顾问") else '').decode('utf-8'))
                    sh.write(idx,11,(self.get_member(item.mbs,"客服顾问") if self.get_member(item.mbs,"客服顾问") else '').decode('utf-8'))
                    sh.write(idx,12,item.create_project_name)
                wb.save('media/output/确认单应收(%s).xls'%(uid_name))
                self.write({'file_path':'static/output/确认单应收('+uid_name+').xls'}) 

            else:
                
                count = self.db.get("""select count(*) count,sum(qk) sum_qk
                                            from (
                                    select a.is_finance_project,a.uid_name create_project_name,ifnull(daishou_money,0) daishou_money,mbs,a.id,all_income,ifnull(b.income_money,0) income_money,ifnull(other_money,0) other_money,
                                    ifnull(((all_income+ifnull(other_money,0)) -( ifnull(b.income_money,0)+ifnull(daishou_money,0))),0)  qk,customer_company,project_name
                                    from t_projects a 
                                    left join (select b1.project_id,ifnull(sum(income_money),0) income_money from t_projects_income b1 ,t_projects_income_title b2 where
                                    b1.parent_id=b2.id and income_id <=43 and  income_uid > 0   group by b1.project_id) b 
                                    on a.id=b.project_id 
                                    left join (select project_id,ifnull(sum(income_money),0) other_money from t_projects_income_other  group by project_id) c 
                                    on a.id=c.project_id 
                                    left join (select project_id,group_concat(team_name,"|",member_name)  mbs from t_projects_member where member_id > 0 group by project_id ) d  
                                    on a.id=d.project_id  
                                    left join (select e1.project_id,ifnull(sum(income_money),0) daishou_money from t_projects_income e1,t_projects_income_title e2 where 
                                    e1.parent_id=e2.id and 
                                    income_id >43  and  income_uid > 0  group by e1.project_id) e 
                                    on a.id=e.project_id """+sql1+""" where 0=0 """+sql+"""
                                    group by a.id) aa where  qk <> 0                                                       
                                                            """)
                pagination = Pagination(page, pre_page, count.count, self.request)
                startpage = (page - 1) * pre_page
                customers = self.db.query("""
                                    select aa.* from (
                                    select a.is_finance_project,customer_name,guid,a.created_at,a.uid_name create_project_name,ifnull(daishou_money,0) daishou_money,mbs,a.id,all_income,ifnull(b.income_money,0) income_money,ifnull(other_money,0) other_money,
                                    ifnull(((all_income+ifnull(other_money,0)) -( ifnull(b.income_money,0)+ifnull(daishou_money,0))),0) qk,customer_company,project_name
                                    from t_projects a 
                                    left join (select b1.project_id,ifnull(sum(income_money),0) income_money from t_projects_income b1 ,t_projects_income_title b2 where
                                    b1.parent_id=b2.id and income_id <=43 and  income_uid > 0   group by b1.project_id) b 
                                    on a.id=b.project_id 
                                    left join (select project_id,ifnull(sum(income_money),0) other_money from t_projects_income_other  group by project_id) c 
                                    on a.id=c.project_id 
                                    left join (select project_id,group_concat(team_name,"|",member_name)  mbs from t_projects_member where member_id > 0 group by project_id ) d  
                                    on a.id=d.project_id  
                                    left join (select e1.project_id,ifnull(sum(income_money),0) daishou_money from t_projects_income e1,t_projects_income_title e2 where 
                                    e1.parent_id=e2.id and 
                                    income_id >43  and  income_uid > 0  group by e1.project_id) e 
                                    on a.id=e.project_id """+sql1+""" where 0=0 """+sql+"""
                                    group by a.id) aa where  qk <> 0 limit %s,%s
                """, startpage, pre_page)
                self.render(
                    'c/finace/finance_project_list.html',
                    get_member=self.get_member,
                    start=start,
                    end=end,
                    keyword=keyword,
                    customers=customers,
                    state=state,
                    pagination=pagination,
                    tag=tag,
                    count=count,
                    qtype=qtype)            
        elif tag=="list":
            sql = ""
            sql1=''
            qtype = self.get_argument("qtype","my")
            state=self.get_argument('state','')
            keyword = self.get_argument("keyword","")
            page = int(self.get_argument("page", 1))
            start = self.get_argument("start","")
            end = self.get_argument("end","")
            if qtype=="my":
                sql = " and (e.acc_uid=%s or sale.member_id=%s)"%(uid,uid)
            pre_page = 20

            if keyword:
                sql+= ''' and (b.project_name like "%%''' + keyword + '''%%" or b.customer_tel like "%%''' + keyword +'''%%" or b.customer_company like "%%'''+keyword+'''%%")'''
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
                         all_income,kf_id,kf_name,create_project_name,
                     aa,  dd, sum_count,sum_project,sum_count1,ifnull(sim,0) sim
                        
                     from ( select acc_uid_name,customer_company,e.id,e.guid,b.id bid,cc.sim,
                     sale.member_id sale_id,sale.member_name sale_name,
                     kf.member_id kf_id,kf.member_name kf_name,b.uid_name create_project_name,
                        ifnull(sum(all_income),0) all_income,
                        ifnull(sum(aa),0) aa, ifnull(sum(dd),0) dd,sum(if(h.count>0,1,0)) sum_count,count(*) sum_project
                        ,sum(if(hh.count>0,-1,0)+if(h.count>0,1,0)) sum_count1
                        from  t_projects b
                         left join ( select ifnull(sum(income_money),0) sim,project_id from t_projects_income_other  group by project_id) cc 
                         on cc.project_id=b.id
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
                        left join t_projects_member kf on b.id=kf.project_id and kf.team_id=36 and kf.member_id!=0
                       
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
                start=start,
                end=end,
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
        
        elif tag=="checked_finance":
            project_id=self.get_argument("project_id","")
            checked_status=self.get_argument("checked_status","")
            self.db.execute(''' insert into t_checked_finance_project
            (project_id,uid_name,uid,created_at,checked_status)
              values(%s,%s,%s,%s,%s) ''',project_id,uid_name,uid,dt,checked_status)
            if checked_status=='2':
                self.db.execute('''
                update t_projects set  is_finance_project=null where id=%s
                ''',project_id)