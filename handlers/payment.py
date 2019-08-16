#encoding=utf8
from handlers.base import BaseHandler
import logging
import json
import tornado.web
import urllib2
import tornado.httpclient
import sys, re, uuid
import urllib, os, datetime
from tornado.options import define, options
reload(sys)
sys.setdefaultencoding('utf8')
from Pagination import Pagination
from dateutil.relativedelta import relativedelta
import xlwt,datetime

def time_transition(date):
    end= datetime.datetime.now()
    result=end-date
    days, seconds = result.days, result.seconds
    hours = days * 24 + seconds // 3600
    minutes = (seconds % 3600) // 60
    seconds = seconds % 60
    if days>0:
        if days==1:
            return '昨天'
        elif days==2:
            return '前天'
        else:
            return str(days)+'天前'
    elif hours>0:
        return str(hours)+'小时前'
    elif minutes>0:
        return str(minutes)+'分钟前'
    else:
        return '刚刚'


class PaymentHandler(BaseHandler):
    def show_project(self,project_id):
        t_project=self.db.get(' select id,guid from t_projects where id=%s  ',project_id)
        if t_project:
            return '<a href="project?tag=show&guid=%s&id=%s">'%(t_project.guid,t_project.id),'</a>'
        return '',''
    def compare_date(self, dt1, dt2):
        # print dt1.strftime("%Y-%m"), dt2.strftime("%Y-%m")
        if dt1.date() <= dt2:
            return True
        else:
            return False
    def show_sb(self,customer_id):
        return self.db_customer.get('''
            select ss_num from t_customer_other_data where
             customer_id=%s
        ''',customer_id)
    def adjusted_option(self,customer_id):
        return self.db_customer.get('''
        select adjusted_option from t_customer_other_data where customer_id=%s
        ''',customer_id)
    def get_assist_linkman(self,customer_id):
        return self.db_customer.get('''
            select name,tel,remark,acc_uid_name,date_format(created_at,'%%Y-%%m-%%d') df  from t_linkman where customer_id=%s order by id desc limit 1
            ''',customer_id)
    
    def get_assist_category(self,assist_id):
        result=self.db_customer.get('''
        select category_id from t_customer_payment_assist_group where assist_id=%s and uid=%s
        ''',assist_id,self.get_secure_cookie("uid"))
        if not result:
            return ''
        return result.category_id

    @tornado.web.authenticated
    def get(self):
        dt = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        tag = self.get_argument("tag", "list")
        uid = self.get_secure_cookie("uid")
        uid_name = self.get_secure_cookie("name")
        role=self.get_secure_cookie('role')
        is_manager= self.get_secure_cookie("is_manager")
        curr = self.get_argument("curr", "confirm")
        req_state = int(self.get_argument("req_state", "0"))
        department_name=self.get_secure_cookie("department_name")
        if self.get_secure_cookie('role_list'):
            role_list=self.get_secure_cookie('role_list').split(',')
        else:
            role_list=[]
        page = int(self.get_argument("page", 1))
        pre_page = 20
        if tag=="output":
            sql = ""
            by_tag_sql = ""
            page = int(self.get_argument("page", 1))
            company = self.get_argument('company', '')
            acc_end_start=self.get_argument('acc_end_start','')
            acc_end_end=self.get_argument('acc_end_end','')
            acc_book_end_start=self.get_argument('acc_book_end_start','')
            acc_book_end_end=self.get_argument('acc_book_end_end','')
            is_general=self.get_argument('is_general','')
            by_tag = self.get_argument("by_tag", "")
            kf = self.get_argument("kf", "")
            order_by_colunm = " a.id "
            pre_page = 20
            if company:
                sql = ' and a.company like "%%' + company + '%%" '
            if kf:
                sql += ' and a.acc_uid_name like "%%' + kf + '%%" '

            if acc_end_start and acc_end_end:
                sql+=' and c.acc_end between "%s"  and  "%s" '%(acc_end_start,acc_end_end)
            if acc_book_end_start and acc_book_end_end:
                sql+=' and c.acc_book_end between "%s" and "%s" '%(acc_book_end_start,acc_book_end_end)
            if is_general:
                sql+=' and a.is_general=1 '

            if by_tag == "正常":
                by_tag_sql = " and a.id not in  (select id from t_customer where  customer_type_name  like '%%解约%%' or customer_type_name  like '%%停账%%' or customer_type_name  like '%%注销%%' or customer_type_name  like '%%取消%%' or customer_type_name  like '%%逾期%%') "
            elif by_tag:
                by_tag_sql = " and  customer_type_name like '%%" + by_tag + "%%'"
            customers = self.db_customer.query("""
                    SELECT  *,c.updated_at pay_updated_at,c.uid_name pay_uid_name,c.wait_pay_amount,
                    c.pay_typeid_name pay_pay_typeid_name,c.service_amount pay_service_amount,c.service_month_amount pay_service_amount_month, c.book_amount pay_book_amount,
                    a.acc_uid_name,a.remark t_remark
                    FROM  t_customer a
                        INNER JOIN t_customer_payment c
                            ON a.id = c.customer_id
                        INNER JOIN
                        (
                            SELECT `customer_id`, MAX(id) max_id
                            FROM t_customer_payment
                            GROUP BY customer_id
                        ) b ON c.customer_id = b.customer_id AND
                                b.max_id = c.id  where 1=1 """ + sql + by_tag_sql + """
                      order by id""")
            wb = xlwt.Workbook()
            # 新增一个表单
            sh = wb.add_sheet(u'业绩表')
            # 按位置添加数据a
            sh.write(0, 0, u"客户编号")
            sh.write(0, 1, u"公司")
            sh.write(0, 2, u"会计")
            sh.write(0, 3, u"付款方式")
            sh.write(0, 4, u"服务费")
            sh.write(0, 5, u"月服务费")
            sh.write(0, 6, u"标签")
            sh.write(0, 7, u"账册费")
            sh.write(0, 8, u"成立日期")
            sh.write(0, 9, u"记账费到期时间")
            sh.write(0, 10, u"账册费到期时间")
            sh.write(0, 11, u"已收明细")
            sh.write(0, 12, u"未收明细")
            sh.write(0, 13, u"待收金额")
            sh.write(0,14,u'备注')


            for idx, item in enumerate(customers):
                idx = idx + 1
                sh.write(idx, 0, item.customer_id)
                sh.write(idx, 1, item.company)
                sh.write(idx, 2, item.acc_uid_name)
                sh.write(idx, 3, item.pay_pay_typeid_name)
                sh.write(idx, 4, item.pay_service_amount)
                sh.write(idx, 5, item.pay_service_amount_month)
                if item.customer_type_name:
                    if item.customer_type_name[-1]==',':
                        sh.write(idx,6,item.customer_type_name[:-1])
                    else:
                        sh.write(idx,6,item.customer_type_name)
                else:
                    sh.write(idx,6,u'')
                sh.write(idx, 7, item.pay_book_amount)
                if item.reg_date:
                    sh.write(idx, 8, item.reg_date.strftime("%Y-%m"))
                else:
                    sh.write(idx, 8, "")

                if item.acc_end:
                    sh.write(idx, 9, item.acc_end.strftime("%Y-%m"))
                else:
                    sh.write(idx, 9, "")
                if item.acc_book_end:
                    sh.write(idx, 10, item.acc_book_end.strftime("%Y-%m"))
                else:
                    sh.write(idx, 10, "")
                sh.write(idx, 11, item.al_remark)
                sh.write(idx, 12, item.pb_remark)
                sh.write(idx, 13, item.wait_pay_amount)
                if item.t_remark:
                    sh.write(idx,14,item.t_remark)
                else:
                    sh.write(idx,14,u'')

            # sh.write(idx, 1, item.created_at.strftime("%Y-%m-%d"))

            # sh.write(0, 18+af_num, u"在线客服")
            # 保存文件
            wb.save('media/output/payment_%s.xls' % (dt))
            self.write(
                "<a href='%s'>下载</a>" % ('static/output/payment_%s.xls' % (dt)))

        elif tag == "get_last_payment":
            customer_id = self.get_argument("customer_id", "")
            payment_id = int(self.get_argument("payment_id", 0))
            pay_id=self.get_argument('pay_id','')
            customer = None
            psql = ""
            if not customer_id:
                return self.write("not customer_id")
            else:
                if payment_id:
                    psql = " and a.id < " + str(payment_id)
                if pay_id:
                    psql=" and a.id=%s "%pay_id
                t_customer = self.db_customer.get(
                    """select a.*,b.paytype_id_name customer_paytype_id_name,a.id payment_id,
                    b.service_amount customer_service_amount ,
                    b.service_amount_month customer_service_amount_month,
                    b.book_amount customer_book_amount,
                    b.fee
                    from
                    t_customer_payment a ,t_customer b  where a.customer_id=b.id and
                    customer_id=%s """ + psql +  """   order by created_at desc limit 1""", customer_id)


                t_customer_limit1 = self.db_customer.get(
                    """select a.*,b.paytype_id_name customer_paytype_id_name,a.id payment_id,
                    b.service_amount customer_service_amount ,
                    b.service_amount_month customer_service_amount_month,
                    b.book_amount customer_book_amount,
                    b.fee
                    from
                    t_customer_payment a ,t_customer b  where a.customer_id=b.id and
                    customer_id=%s """ + psql +  """   order by created_at desc limit 1,1""", customer_id)


                if not t_customer:
                    code = 0
                else:
                    code = 1
                    acc_end = None
                    acc_book_end = None
                    next_pay_acc_end_book = None
                    next_pay_acc_end_book_start = None
                    next_pay_acc_end=None
                    next_pay_acc_end_start=None
                    if t_customer.acc_book_end:
                        # print "hi", t_customer.acc_book_end
                        next_pay_acc_end_book = t_customer.acc_book_end - relativedelta(
                            months=-t_customer.fee)
                        next_pay_acc_end_book = next_pay_acc_end_book.strftime(
                            "%Y-%m")
                        next_pay_acc_end_book_start = t_customer.acc_book_end - relativedelta(
                            months=-1)
                        next_pay_acc_end_book_start = next_pay_acc_end_book_start.strftime(
                            "%Y-%m")
                        acc_book_end = t_customer.acc_book_end.strftime(
                            "%Y-%m")
                    # print "t_customer.acc_end", t_customer.acc_end, " t_customer.acc_book_end", t_customer.acc_book_end
                    if t_customer.acc_end:
                        next_pay_acc_end_start = t_customer.acc_end - relativedelta(
                            months=-1)
                        next_pay_acc_end = t_customer.acc_end - relativedelta(
                            months=-t_customer.fee)
                        next_pay_acc_end_start = next_pay_acc_end_start.strftime(
                            "%Y-%m")
                        next_pay_acc_end = next_pay_acc_end.strftime("%Y-%m")
                        acc_end = t_customer.acc_end.strftime("%Y-%m")
                    old_al_remark = ""
                    old_pb_remark = ""
                    old_wait_pay_amount= ""
                    old_acc_end,old_acc_book_end=None,None
                    if t_customer_limit1:
                        old_al_remark = t_customer_limit1.al_remark
                        old_pb_remark = t_customer_limit1.pb_remark
                        old_wait_pay_amount = t_customer_limit1.wait_pay_amount
                        old_acc_book_end = t_customer_limit1.acc_book_end
                        old_acc_end = t_customer_limit1.acc_end
                    t_customer = {
                        "old_acc_end":str(old_acc_end.strftime("%Y-%m")) if old_acc_end else str(old_acc_end),
                        "old_acc_book_end":str(old_acc_book_end.strftime("%Y-%m")) if old_acc_book_end else str(old_acc_book_end),
                        "old_wait_pay_amount":str(old_wait_pay_amount),
                        "old_pb_remark":old_pb_remark,
                        "old_al_remark":old_al_remark,
                        "service_amount":
                        str(t_customer.service_amount),
                        "book_amount":
                        str(t_customer.book_amount),
                        "service_month_amount":
                        str(t_customer.service_month_amount),
                        "acc_end":
                        acc_end,
                        "acc_book_end":
                        acc_book_end,
                        "al_remark":
                        t_customer.al_remark,
                        "pb_remark":
                        t_customer.pb_remark,
                        "customer_paytype_id_name":
                        t_customer.customer_paytype_id_name,
                        "customer_service_amount":
                        str(t_customer.customer_service_amount),
                        "customer_service_amount_month":
                        str(t_customer.customer_service_amount_month),
                        "customer_book_amount":
                        str(t_customer.customer_book_amount),
                        "fee":
                        str(t_customer.fee),
                        "next_pay_acc_end":
                        next_pay_acc_end,
                        "next_pay_acc_end_book":
                        next_pay_acc_end_book,
                        "next_pay_acc_end_start":
                        next_pay_acc_end_start,
                        "next_pay_acc_end_book_start":
                        next_pay_acc_end_book_start,
                        "payment_id":
                        t_customer.payment_id,
                        "wait_pay_amount":str(t_customer.wait_pay_amount)
                    }
                self.write(
                    tornado.escape.json_encode({
                        "code": code,
                        "customer": t_customer
                    }))

        elif tag == "process_status":
            status = self.get_argument("status", "")
            params = {"status": status}
            sql = ""
            if status:
                sql = " and b.order_int >2"
            else:
                sql = " and b.order_int <=2"

            count = self.db.get('''
               select   count(*) count
                from t_projects_member a ,
                t_projects_type b,
                t_projects c ,
                t_projects_income_detail d,
                t_projects_income e
                where  c.id=a.project_id
                and team_id=38
                and a.last_milepost_id=b.id
                    and a.btype_id=155

                    and a.project_id=d.project_id
                    and  service_id=10
                    and project_income_id=e.id
            ''' + sql + ''' order by d.created_at desc''')
            pagination = Pagination(page, pre_page, count.count, self.request)
            startpage = (page - 1) * pre_page

            customers = self.db.query("""
                select  d.service_id,service_name,customer_company,service_money,project_name,d.created_at,
                a.project_id project_id,
                c.guid project_guid
                ,d.uid_name add_by_uid
                from t_projects_member a ,
                t_projects_type b,
                t_projects c ,
                t_projects_income_detail d,
                t_projects_income e
                where  c.id=a.project_id
                and team_id=38
                and a.last_milepost_id=b.id
                    and a.btype_id=155

                    and a.project_id=d.project_id
                    and  service_id=10
                    and project_income_id=e.id
            """ + sql + " order by d.created_at desc")
            t_payment_type = self.db_customer.query(
                "select * from t_type where tag='付费方式'")
            self.render(
                'c/payment/process_status.html',
                customers=customers,
                pagination=pagination,
                t_payment_type=t_payment_type,
                params=params,
                tag=tag)

        elif tag == "customer":
            customer_id = int(self.get_argument("customer_id"))
            to_tag = self.get_argument("to_tag", "")
            old_tag=self.get_argument('old_tag','')
            customer_guid=self.get_argument('customer_guid','')
            dt_next = datetime.date.today() - relativedelta(months=-1)

            sql = ""
            if not customer_id:
                return self.write("customer_id is null")
            customer = self.db_customer.get(
                "select * from t_customer where id=%s", customer_id)
            if not customer:
                return self.write("errer customer %s", customer_id)
            if customer_id:
                sql = " and  a.id='%s' " % (customer_id)
            pre_page = 200
            count = self.db_customer.get('''
               select count(*) count
            FROM  t_customer a
            INNER JOIN t_customer_payment c
                ON a.id = c.customer_id
               ''' + sql)
            pagination = Pagination(page, pre_page, count.count, self.request)
            startpage = (page - 1) * pre_page

            customers = self.db_customer.query("""
                       SELECT  DATE_ADD(c.acc_end, INTERVAL 1 MONTH) next_pay_acc_start ,
                        DATE_ADD(c.acc_end, INTERVAL a.fee MONTH) next_pay_acc_end,
                        DATE_ADD(c.acc_book_end, INTERVAL 1 MONTH) next_pay_acc_book_start ,
                        DATE_ADD(c.acc_book_end, INTERVAL a.fee MONTH) next_pay_acc_book_end, c.*,
                        a.guid,a.company,c.updated_at pay_updated_at,c.uid_name pay_uid_name,a.remark customer_remark,
                        c.pay_typeid_name pay_pay_typeid_name,c.service_amount pay_service_amount,
                                                                c.service_month_amount pay_service_amount_month, c.book_amount pay_book_amount
                                                                FROM  t_customer a
                                                                
                                                                    INNER JOIN t_customer_payment c
                                                                        ON a.id = c.customer_id



                """ + sql + """
                order by created_at desc
            """)

            t_payment_type = self.db_customer.query(
                "select * from t_type where tag='付费方式'")

            sel_sql=''
            # if department_name!='销售部' and role!='8':
            #     sel_sql=' ,if(isvisible=2,"*** (未协助完不可见)",msg) as msg '
            t_customer_exchange = self.db_customer.query(
                """select * from t_customer_exchange 
                 where customer_id=%s and (etype=2 or etype=4) order by created_at desc"""
                ,customer_id)
            t_customer_payment_max_assist=self.db_customer.get('''
                select id from t_customer_payment_assist where customer_id=%s and sale_id=%s  order by id desc limit 1
                ''',customer_id,uid)
            t_linkman = self.db_customer.query(
                        "select * from t_linkman where customer_id=%s order by is_first desc,id ",
                        customer_id)

            self.render(
                'c/payment/customer.html',
                t_customer_payment_max_assist=t_customer_payment_max_assist,
                t_customer_exchange=t_customer_exchange,
                customers=customers,
                t_payment_type=t_payment_type,
                customer=customer,
                pagination=pagination,
                to_tag=to_tag,
                t_linkman=t_linkman,
                tag=tag,
                old_tag=old_tag,
                customer_guid=customer_guid,
                dt_next=dt_next)
        elif tag == "project_customer_list":
            sql = ""
            page = int(self.get_argument("page", 1))
            pre_page = 20
            req_state_sql = ""
            if req_state:
                req_state_sql = " in "
            else:
                req_state_sql = " not in "
            count = self.db_customer.get('''
        select count(*) count
                FROM  t_customer
                where id ''' + req_state_sql + ''' (
                select customer_id from  t_customer_payment where  customer_type_name like '%%记账%%'
 group by customer_id
                )

               ''')
            pagination = Pagination(page, pre_page, count.count, self.request)
            startpage = (page - 1) * pre_page
            customers = self.db_customer.query("""
            SELECT  *  FROM  t_customer
                where id """ + req_state_sql + """ (
                select customer_id from  t_customer_payment where  customer_type_name like '%%记账%%'
 group by customer_id
                )

                order by created_at desc
 limit %s,%s
            """, startpage, pre_page)
            t_payment_type = self.db_customer.query(
                "select * from t_type where tag='付费方式'")
            self.render(
                'c/payment/project_customer_list.html',
                t_payment_type=t_payment_type,
                customers=customers,
                pagination=pagination,
                req_state=req_state,
                tag=tag,
                curr=curr)
        elif tag == "project_payment_list":
            sql = ""
            page = int(self.get_argument("page", 1))
            pre_page = 10
            req_state_sql = ""
            if req_state:
                req_state_sql = " and c.id  in( select income_id from t_customer_payment where income_id > 0 )"
            else:
                req_state_sql = "and c.id not in( select income_id from t_customer_payment where income_id > 0)"
            count = self.db_customer.get('''
        select count(*) count
        from t_customer a inner join db_income2.t_projects b on a.company=b.customer_company
        inner join db_income2.t_projects_income_title c  on  c.project_id=a.id and income_uid  > 0  and busniess_from_id=203
        left join t_customer_payment_req d on d.income_id= c.id
where customer_type_name like '%%记账%%'
               ''' + req_state_sql)

            pagination = Pagination(page, pre_page, count.count, self.request)
            startpage = (page - 1) * pre_page
            # print "req_state_sql", req_state_sql
            customers = self.db_customer.query("""
                   select  *, c.uid_name add_by,c.id income_title_id,b.id project_id,b.guid project_guid,a.id a_customer_id,
                   a.paytype_id customer_pay_type_id,service_amount customer_service_amount,
                   service_amount_month customer_service_amount_month,
                   book_amount customer_book_amount,
                   a.fee customer_fee,
                   a.guid a_customer_guid from t_customer a inner join db_income2.t_projects b on a.company=b.customer_company
inner join db_income2.t_projects_income_title c  on  c.project_id=a.id and income_uid  > 0  and busniess_from_id=203
where customer_type_name like '%%记账%%'

""" + req_state_sql + """ order by a.created_at desc

                                                    limit %s,%s
            """, startpage, pre_page)
            t_payment_type = self.db_customer.query(
                "select * from t_type where tag='付费方式'")

            self.render(
                'c/payment/project_payment_list.html',
                t_payment_type=t_payment_type,
                customers=customers,
                pagination=pagination,
                req_state=req_state,
                tag=tag,
                curr=curr)
        elif tag == "list":
            sql = ""
            by_tag_sql = ""
            page = int(self.get_argument("page", 1))
            company = self.get_argument('company', '')
            by_tag = self.get_argument("by_tag","")
            kf = self.get_argument("kf", "")
            acc_end_start=self.get_argument('acc_end_start','')
            acc_end_end=self.get_argument('acc_end_end','')
            acc_book_end_start=self.get_argument('acc_book_end_start','')
            acc_book_end_end=self.get_argument('acc_book_end_end','')
            is_general=self.get_argument('is_general','')
            small_amount=self.get_argument('small_amount','')
            big_amount=self.get_argument('big_amount','')
            output = self.get_argument("output","")
            if is_manager=="1":
                pass
            elif role!="8" and role!="3" and role!="5" :
                kf=uid_name

            order_by_colunm = " req_at desc"
            pre_page = 20
            params={
                'company':company,
                'kf':kf,
                'acc_end_start':acc_end_start,
                'acc_end_end':acc_end_end,
                'acc_book_end_start':acc_book_end_start,
                'acc_book_end_end':acc_book_end_end,
                'is_general':is_general,
                "small_amount":small_amount,
                "big_amount":big_amount
            }
            if company:
                sql += """ 
                        and (a.id = '""" + company + """'
                         or a.company like '%%""" + company + """%%' or a.company_reguid like '%%""" + company + """%%' 
                          or a.id in (select customer_id  from t_company_name where name like '%%""" + company + """%%' )
                         )
                
                
                """
            if kf:
                sql += ' and a.acc_uid_name like "%%' + kf + '%%" '
            if small_amount and big_amount:
                by_tag_sql = " and a.id  in  (select id from t_customer where  service_amount_month >= "+small_amount+"  and service_amount_month <="+big_amount+") "
            if acc_end_start and acc_end_end:
                sql+=' and c.acc_end between "%s"  and  "%s" '%(acc_end_start+'-01',acc_end_end+'-01')
            if acc_book_end_start and acc_book_end_end:
                sql+=' and c.acc_book_end between "%s" and "%s" '%(acc_book_end_start+'-01',acc_book_end_end+'-01')
            if is_general:
                sql+=' and a.is_general=1 '
            if by_tag =="正常":
                by_tag_sql = " and a.id not in  (select id from t_customer where  customer_type_name  like '%%解约%%' or customer_type_name  like '%%停账%%' or customer_type_name  like '%%注销%%' or customer_type_name  like '%%取消%%' or customer_type_name  like '%%逾期%%') "
            elif by_tag=='楼盘':
                by_tag_sql=' and a.is_building=1 '
            elif by_tag=='汇算清缴':
                by_tag_sql=' and a.is_clearly=1 '
            elif by_tag=='工商年检':
                by_tag_sql=' and a.is_year=1 '
            elif by_tag:
                by_tag_sql = " and  tag_id_name='%s' "%by_tag
                order_by_colunm = " c.wait_pay_amount  desc"

            count = self.db_customer.get('''
                    select count(*) count
                            FROM  t_customer a
                                INNER JOIN t_customer_payment c
                                    ON a.id = c.customer_id
                                INNER JOIN
                                (
                                    SELECT `customer_id`, MAX(id) max_id
                                    FROM t_customer_payment
                                    GROUP BY customer_id
                                ) b ON c.customer_id = b.customer_id AND
                                        b.max_id = c.id where 1=1
               ''' + sql+by_tag_sql)

            total = self.db_customer.get('''
                    select ifnull(sum(wait_pay_amount),0) wait_pay_total
                            FROM  t_customer a
                                INNER JOIN t_customer_payment c
                                    ON a.id = c.customer_id
                                INNER JOIN
                                (
                                    SELECT `customer_id`, MAX(id) max_id
                                    FROM t_customer_payment
                                    GROUP BY customer_id
                                ) b ON c.customer_id = b.customer_id AND
                                        b.max_id = c.id where 1=1
               ''' + sql + by_tag_sql)


            pagination = Pagination(page, pre_page, count.count, self.request)
            startpage = (page - 1) * pre_page
            limit_sql=""
            if   output:
                order_by_colunm = " a.id "
            else:
                limit_sql=" limit {},{}".format(startpage, pre_page)

                
            # print """
            #         SELECT  *,c.id payment_id,

            #         c.updated_at pay_updated_at,c.uid_name pay_uid_name,c.wait_pay_amount,
            #         c.pay_typeid pay_pay_typeid_id, c.pay_typeid_name pay_pay_typeid_name,
            #         c.service_amount pay_service_amount,c.service_month_amount pay_service_amount_month,
            #          c.book_amount pay_book_amount,
            #         a.acc_uid_name,a.remark t_remark
            #         FROM  t_customer a
            #             INNER JOIN t_customer_payment c
            #                 ON a.id = c.customer_id
            #             INNER JOIN
            #             (
            #                 SELECT `customer_id`, MAX(id) max_id
            #                 FROM t_customer_payment
            #                 GROUP BY customer_id
            #             ) b ON c.customer_id = b.customer_id AND
            #                     b.max_id = c.id """ + sql + by_tag_sql + """
            #             order by """ + order_by_colunm + """ desc
                      
            # """+limit_sql
            customers = self.db_customer.query("""
                    SELECT *, a.company , c.id payment_id,a.id a_customer_id,guid,
                    a.paytype_id_name customer_paytype_id_name,
                    a.promo_id_name customer_promo_id_name,
                    a.promo_id customer_promo_id,
                    a.is_general customer_is_general,
                    a.service_amount customer_service_amount,
                    a.service_amount_month customer_service_amount_month,
                    a.book_amount customer_book_amount,
                    a.customer_type customer_customer_type,
                    a.tag_id customer_tag_id,
                    a.tag_id_name customer_tag_id_name,
                    a.tag_parent_id customer_tag_parent_id,
                    a.tag_parent_id_name customer_tag_parent_id_name,
                    a.is_building customer_is_building,
                    a.is_clearly customer_is_clearly,
                    a.is_year customer_is_year,c.project_id payment_project_id,
                    c.updated_at pay_updated_at,c.uid_name pay_uid_name,c.wait_pay_amount,
                    c.pay_typeid pay_pay_typeid_id, c.pay_typeid_name pay_pay_typeid_name,
                    c.service_amount pay_service_amount,c.service_month_amount pay_service_amount_month,
                     c.book_amount pay_book_amount,
                    a.acc_uid_name,a.remark t_remark
                    FROM  t_customer a
                        INNER JOIN t_customer_payment c
                            ON a.id = c.customer_id
                        INNER JOIN
                        (
                            SELECT `customer_id`, MAX(id) max_id
                            FROM t_customer_payment
                            GROUP BY customer_id
                        ) b ON c.customer_id = b.customer_id AND
                                b.max_id = c.id """ + sql + by_tag_sql + """
                        order by """ + order_by_colunm +limit_sql)
            t_payment_type = self.db_customer.query(
                "select * from t_type where tag='付费方式'")
            t_customer_type = self.db_customer.query(
                "select * from t_type where tag='客户标签' and is_show=1  order by `order` ")

            t_promo_types = self.db.query(
                """select * from t_projects_type where income_category='套餐' order by order_int  """
            )
            t_type_new_parents=self.db_customer.query('''
                    select * from t_type where tag='客户标签1'
                    ''')
            t_type_new=self.db_customer.query('''
                    select * from t_type where tag='客户标签' and parent_id in (1,2) and name!='楼盘'
                    ''')
            if output:
                wb = xlwt.Workbook()
                # 新增一个表单
                sh = wb.add_sheet(u'业绩表')
                # 按位置添加数据a
                sh.write(0, 0, u"客户编号")
                sh.write(0, 1, u"公司")
                sh.write(0, 2, u"会计")
                sh.write(0, 3, u"付款方式")
                sh.write(0, 4, u"服务费")
                sh.write(0, 5, u"月服务费")
                sh.write(0, 6, u"标签")
                sh.write(0, 7, u"账册费")
                sh.write(0, 8, u"成立日期")
                sh.write(0, 9, u"记账费到期时间")
                sh.write(0, 10, u"账册费到期时间")
                sh.write(0, 11, u"已收明细")
                sh.write(0, 12, u"未收明细")
                sh.write(0, 13, u"待收金额")
                sh.write(0,14,u'备注')


                for idx, item in enumerate(customers):
                    idx = idx + 1
                    sh.write(idx, 0, item.customer_id)
                    sh.write(idx, 1, item.company)
                    sh.write(idx, 2, item.acc_uid_name)
                    sh.write(idx, 3, item.pay_pay_typeid_name)
                    sh.write(idx, 4, item.pay_service_amount)
                    sh.write(idx, 5, item.pay_service_amount_month)
                    tags=""
                    if item.tag_parent_id_name!=item.tag_id_name:
                        tags=item.tag_parent_id_name+","
                    if item.tag_id_name:
                        tags+=item.tag_id_name+","
                    if item.is_building:
                        tags+=u"楼盘,"
                    if item.is_year:
                        tags+=u"工商年检,"
                    if item.is_clearly:
                        tags+=u"汇算清缴,"
                    sh.write(idx,6,tags)                            
                    sh.write(idx, 7, item.pay_book_amount)
                    if item.reg_date:
                        sh.write(idx, 8, item.reg_date.strftime("%Y-%m"))
                    else:
                        sh.write(idx, 8, "")

                    if item.acc_end:
                        sh.write(idx, 9, item.acc_end.strftime("%Y-%m"))
                    else:
                        sh.write(idx, 9, "")
                    if item.acc_book_end:
                        sh.write(idx, 10, item.acc_book_end.strftime("%Y-%m"))
                    else:
                        sh.write(idx, 10, "")
                    sh.write(idx, 11, item.al_remark)
                    sh.write(idx, 12, item.pb_remark)
                    sh.write(idx, 13, item.wait_pay_amount)
                    if item.t_remark:
                        sh.write(idx,14,item.t_remark)
                    else:
                        sh.write(idx,14,u'')

                # sh.write(idx, 1, item.created_at.strftime("%Y-%m-%d"))

                # sh.write(0, 18+af_num, u"在线客服")
                # 保存文件
                wb.save('media/output/payment_%s.xls' % (dt))
                return self.write(
                    "<a href='%s'>下载</a>" % ('static/output/payment_%s.xls' % (dt)))
            self.render(
                'c/payment/payment_list.html',
                t_promo_types=t_promo_types,
                t_customer_type=t_customer_type,
                show_project=self.show_project,
                t_type_new_parents=t_type_new_parents,
                t_type_new=t_type_new,
                by_tag=by_tag,
                total=total,
                customers=customers,
                pagination=pagination,
                t_payment_type=t_payment_type,
                params=params,
                adjusted_option=self.adjusted_option,
                tag=tag)

        elif tag == "list_company":
            kf = self.get_argument("kf", "")
            state = self.get_argument("state", "")
            sql = ""
            sql1 = ""
            page = int(self.get_argument("page", 1))
            pre_page = 20
            company = self.get_argument('company', '')
            if state:
                sql = "  and b.order_int > 2 "
            else:
                sql = " and b.order_int <=2  "
            if company:
                sql1 += """ 
                        and (a.project_id = '""" + company + """'
                         or c.customer_company like '%%""" + company + """%%' or c.company_uid like '%%""" + company + """%%' 
                         
                         )
                
                
                """
            if kf:
                sql1 += ' and a.acc_uid_name like "%%' + kf + '%%" '



            count = self.db.get('''
                select  count(*) count
                                from t_projects_member a ,
                                t_projects_type b,
                                t_projects c ,
                                t_projects_income_detail d,
                                t_projects_income e
                                where  c.id=a.project_id
                                and team_id=38
                                and last_milepost_id=b.id
                                    and a.btype_id=155

                                    and a.project_id=d.project_id
                                    and  service_id=10
                                    and project_income_id=e.id

               ''' + sql + sql1)
            pagination = Pagination(page, pre_page, count.count, self.request)
            startpage = (page - 1) * pre_page
            customers = self.db.query("""
                select  d.service_id,service_name,customer_company,service_money,project_name,d.created_at,company_uid,
                a.project_id project_id,
                c.guid project_guid,
                b.order_int ,b.income_name,
                d.service_money
                from t_projects_member a ,
                t_projects_type b,
                t_projects c ,
                t_projects_income_detail d,
                t_projects_income e
                where  c.id=a.project_id
                and team_id=38
                and last_milepost_id=b.id
                    and a.btype_id=155

                    and a.project_id=d.project_id
                    and  service_id=10
                    and project_income_id=e.id """ +sql+sql1 + """


              order by d.created_at desc
                        limit %s,%s
            """, startpage, pre_page)
            t_payment_type = self.db_customer.query(
                "select * from t_type where tag='付费方式'")

            self.render(
                'c/payment/list_company.html',
                kf=kf,
                state=state,
                company=company,
                customers=customers,
                pagination=pagination,
                t_payment_type=t_payment_type,
                tag=tag)

        elif tag == "list_company_in_customer":
            pay_project_id = int(self.get_argument("pay_project_id", 0))
            sql = ""
            hand_sql = ""
            sql_reg = ""
            pay_sql = ""
            state = int(self.get_argument("state", 0))
            kf = self.get_argument("kf", "")
            page = int(self.get_argument("page", 1))
            pre_page = 20
            company = self.get_argument('company', '')
            o = self.get_argument("o","")
            order_by_colunm =" e.created_at "
            special = self.get_argument("special","")
            add_column =""
            if pay_project_id == 0:
                hand_sql = " and  is_handler=0 "
                sql_reg = "and reg_state <> 1"
            else:
                hand_sql = " and  is_handler=1 "

                pay_sql = "   inner join " + options.mysql_database_customer + ".`t_customer_payment` g on a.id=g.customer_id  and  cp_title_id =e.id and cp_title_id > 0 and payment_confirm_state=" + str(
                    state)
                order_by_colunm = " e.is_handler_at "
                add_column = " payment_confirm_remark,payment_confirm_at,payment_confirm_uid_name, pb_remark , al_remark,wait_pay_amount e_wait_pay_amount ,g.acc_end e_acc_end,g.acc_book_end e_acc_book_end,g.id payment_id, "
                if state:
                    order_by_colunm =" pay_handler_at "
                 

            if company:
                sql += """ 
                        and (a.id = '""" + company + """'
                         or a.company like '%%""" + company + """%%' or a.company_reguid like '%%""" + company + """%%' 
                          or a.id in (select customer_id  from """+options.mysql_database_customer+""".t_company_name where name like '%%""" + company + """%%' )
                         )
                
                
                """

            if kf:
                sql += ' and a.acc_uid_name like "%%' + kf + '%%" '
            special_sql = ""
            if  not special:
                pay_project_id_sql=""
                if pay_project_id==1:
                    pay_project_id_sql="""
                     and d.service_id=9 or d.service_id=87 or d. project_id in (   select id from t_projects where project_name   like '%%注销%%'  or   project_name   like '%%解约%%')
                    
                    """
                    o="desc"
                special_sql="""
                          inner join (select title_id, GROUP_CONCAT(concat( service_name,"|",service_money)) pay_list from t_projects_income_detail d where
                    (d.`service_id`=10 or d.service_id=204 or d.service_id=131  """+pay_project_id_sql+""" )
                    group by title_id) d on e.id=d.title_id and b.id=e.project_id
                
                """
            else:
                 special_sql="""
                          inner join (select title_id, GROUP_CONCAT(concat( service_name,"|",service_money)) pay_list from t_projects_income_detail d where
                    ( d.service_id=9 or d.service_id=87) or d. project_id in (
                        select id from t_projects where project_name   like '%%注销%%'  or   project_name   like '%%解约%%'
                    )
                    group by title_id) d on e.id=d.title_id and b.id=e.project_id
                
                """               
                 sql +="  and tag_parent_id_name='记账' "
                 o ="desc"
            pay_sql_column =""
            count = self.db.get("""
                select
                count(*) count


                     from  """ + options.mysql_database_customer +
                """.`t_customer` a
                    inner join t_projects b on a.company = b.customer_company   """
                + sql_reg + """
                    inner join t_projects_income_title e  on e.project_id=b.id and fi_confirm_uid > 0  """
                + hand_sql + """
                					inner join
                     (select parent_id,income_num,
                      GROUP_CONCAT(concat( income_name,"|",income_money))
                      income_list from t_projects_income dd

                     group by parent_id,income_num

                     ) c on c.parent_id=e.id

            """+special_sql +pay_sql+ sql )

            pagination = Pagination(page, pre_page, count.count, self.request)
            startpage = (page - 1) * pre_page
            customers = self.db.query(
                """
                    select 
                    a.*,
                     a.paytype_id_name customer_paytype_id_name,a.remark t_remark,
                      a.promo_id customer_promo_id,
                    a.promo_id_name customer_promo_id_name,
                    a.is_general customer_is_general,
                    a.service_amount customer_service_amount,
                    a.service_amount_month customer_service_amount_month,
                    a.book_amount customer_book_amount,
                    a.customer_type customer_customer_type,
                    a.tag_id customer_tag_id,
                    a.tag_id_name customer_tag_id_name,
                    a.tag_parent_id customer_tag_parent_id,
                    a.tag_parent_id_name customer_tag_parent_id_name,
                    a.is_building customer_is_building,
                    a.is_clearly customer_is_clearly,
                    a.is_year customer_is_year,
                    company_reguid,a.remark customer_remark,customer_type_name, a.id customer_id,a.promo_id,a.promo_id_name,a.is_general,a.paytype_id_name
                     pay_pay_typeid_name,a.service_amount pay_service_amount,service_amount_month
                     pay_service_amount_month,a.book_amount pay_book_amount,a.guid,customer_type ,"""
                + add_column +
                """ a.acc_uid_name,income_list ,pay_list,e.is_handler_uid_name is_handler_uid_name,is_handler_at,
                    customer_company,b.project_name,income_num,b.id project_id,e.id cp_title_id,e.created_at title_created_at,
                    a.id a_customer_id,a.paytype_id customer_pay_type_id, a.service_amount customer_service_amount,a.service_amount_month customer_service_amount_month,


                    a.book_amount customer_book_amount,a.guid a_customer_guid, a.paytype_id_name customer_paytype_id_name,
                    a.tag_id,a.tag_id_name,a.tag_parent_id,a.tag_parent_id_name,a.is_building,a.is_clearly,a.is_year

                    from  """ + options.mysql_database_customer +
                """.`t_customer` a
                    inner join t_projects b on a.company = b.customer_company   """
                + sql_reg + """
                    inner join t_projects_income_title e  on e.project_id=b.id and fi_confirm_uid > 0  """
                + hand_sql + """
                					inner join
                     (select parent_id,income_num,
                      GROUP_CONCAT(concat( income_name,"|",income_money))
                      income_list from t_projects_income dd

                     group by parent_id,income_num

                     ) c on c.parent_id=e.id
          
            """+special_sql +pay_sql+ sql + """


                    order by """ + order_by_colunm +o+ """ 
                        limit %s,%s
            """, startpage, pre_page)

            t_payment_type = self.db_customer.query(
                "select * from t_type where tag='付费方式'")
            t_customer_type = self.db_customer.query(
                "select * from t_type where tag='客户类型'")
            t_promo_types = self.db.query(
                """select * from t_projects_type where income_category='套餐' order by order_int  """
            )


            t_customer_type = self.db_customer.query(
                "select * from t_type where tag='客户类型' and is_show=1")
            t_type_new_parents=self.db_customer.query('''
                    select * from t_type where tag='客户标签1'
                    ''')
            t_type_new=self.db_customer.query('''
                    select * from t_type where tag='客户标签' and parent_id in (1,2) and name!='楼盘'
                    ''')
            self.render(
                'c/payment/list_company_in_customer.html',
                customers=customers,
                kf=kf,
                special=special,
                t_type_new_parents=t_type_new_parents,
                t_type_new=t_type_new,
                t_promo_types=t_promo_types,
                company=company,
                t_customer_type=t_customer_type,
                pagination=pagination,
                t_payment_type=t_payment_type,
                pay_project_id=pay_project_id,
                adjusted_option=self.adjusted_option,
                state=state,
                tag=tag,
                o=o)

        elif tag == "list_company_in_customer_req":
            pay_project_id = int(self.get_argument("pay_project_id", 0))
            from_customer = self.get_argument("from_customer","")
            sql = ""
            sql_reg = ""
            sql_hand = ""
            page = int(self.get_argument("page", 1))
            pre_page = 20
            company = self.get_argument('company', '')
            state = int(self.get_argument("state", 0))
            kf = self.get_argument("kf", "")
            is_handler_uid_name=self.get_argument('is_handler_uid_name','')
            order_by_colunm="is_handler_at"
            if state:
                order_by_colunm = "payment_confirm_at"

            if company:
                sql += """ 
                        and (a.id = '""" + company + """'
                         or a.company like '%%""" + company + """%%' or a.company_reguid like '%%""" + company + """%%'
                          or a.id in (select customer_id  from """+options.mysql_database_customer +""".t_company_name where name like '%%""" + company + """%%' )
                          )
                
                
                """
            if kf:
                sql += ' and a.acc_uid_name like "%%' + kf + '%%"'
            sql += " and payment_confirm_state=" + str(state)
            sql_hand = " and  is_handler=1"
            if is_handler_uid_name:
                sql+=' and is_handler_uid_name like "%%'+is_handler_uid_name+'%%" '
            count = self.db.get(
                """
                select
                count(*) count
                              from  """ + options.mysql_database_customer +
                """.`t_customer` a
                    inner join """ + options.mysql_database_customer +
                """.`t_customer_payment` g on a.id=g.customer_id and g.cp_title_id > 0
                    inner join t_projects b on a.company = b.customer_company   """
                + sql_reg + """
                    inner join t_projects_income_title e  on e.project_id=b.id and fi_confirm_uid > 0  """
                + sql_hand + """  and g.cp_title_id = e.id

                       INNER join        (select parent_id,income_num,
                      GROUP_CONCAT(concat( income_name,"|",income_money))
                      income_list from t_projects_income dd

                     group by parent_id,income_num

                     ) c on c.parent_id=e.id

                    inner join (select title_id, GROUP_CONCAT(concat( service_name,"|",service_money)) pay_list from t_projects_income_detail d where
   (d.`service_id`=10 or d.service_id=204 or d.service_id=131   and d.service_id=9 or d.service_id=87 or d. project_id in (   select id from t_projects where project_name   like '%%注销%%'  or   project_name   like '%%解约%%'))
  group by title_id) d
                    on e.id=d.title_id


                         """ + sql + """

               """)
            pagination = Pagination(page, pre_page, count.count, self.request)
            startpage = (page - 1) * pre_page
            customers = self.db.query(
                """
                    SELECT a.company , a.remark t_remark,
                    a.paytype_id_name customer_paytype_id_name,
                    a.promo_id_name customer_promo_id_name,
                    a.is_general customer_is_general,
                    a.service_amount customer_service_amount,
                    a.service_amount_month customer_service_amount_month,
                    a.book_amount customer_book_amount,
                    a.customer_type customer_customer_type,
                    a.tag_id customer_tag_id,
                    a.tag_id_name customer_tag_id_name,
                    a.tag_parent_id customer_tag_parent_id,
                    a.tag_parent_id_name customer_tag_parent_id_name,
                    a.is_building customer_is_building,
                    a.is_clearly customer_is_clearly,
                     a.promo_id customer_promo_id,
                    a.is_year customer_is_year,  company_reguid,a.remark customer_remark,customer_type_name,payment_confirm_remark,payment_confirm_at,payment_confirm_uid_name, pb_remark , al_remark,wait_pay_amount e_wait_pay_amount ,g.acc_end e_acc_end,g.acc_book_end e_acc_book_end,g.id payment_id,a.id customer_id,a.promo_id,a.promo_id_name,a.is_general,a.paytype_id_name
                     pay_pay_typeid_name,a.service_amount pay_service_amount,service_amount_month
                     pay_service_amount_month,a.book_amount pay_book_amount,a.guid,customer_type ,
pfi_confirm_remark,payment_confirm_at,

                  a.acc_uid_name,payment_confirm_state,income_list,
                    pay_list,e.uid_name title_uid_name,is_handler_uid_name,payment_confirm_uid_name,is_handler_uid_name,
                    is_handler_at,

                    customer_company,b.project_name,income_num,b.id project_id,e.id income_title_id,
                    e.created_at title_created_at,
                    a.id customer_id,a.paytype_id customer_pay_type_id, a.service_amount customer_service_amount,
                    a.service_amount_month customer_service_amount_month,g.payment_confirm_last_state,
                    a.book_amount customer_book_amount,a.guid a_customer_guid, a.paytype_id_name customer_paytype_id_name,
                    g.acc_end,g.acc_book_end,g.id payment_id,g.al_remark,g.pb_remark,g.payment_confirm_remark,
                    a.tag_id,a.tag_id_name,a.tag_parent_id,a.tag_parent_id_name,a.is_building,a.is_clearly,a.is_year
                    from  """ + options.mysql_database_customer +
                """.`t_customer` a
                    inner join """ + options.mysql_database_customer +
                """.`t_customer_payment` g on a.id=g.customer_id and g.cp_title_id > 0
                    inner join t_projects b on a.company = b.customer_company   """
                + sql_reg + """
                    inner join t_projects_income_title e  on e.project_id=b.id and fi_confirm_uid > 0  """
                + sql_hand + """  and g.cp_title_id = e.id

                       INNER join        (select parent_id,income_num,
                      GROUP_CONCAT(concat( income_name,"|",income_money))
                      income_list from t_projects_income dd

                     group by parent_id,income_num

                     ) c on c.parent_id=e.id

                    inner join (select title_id, GROUP_CONCAT(concat( service_name,"|",service_money)) pay_list from t_projects_income_detail d where
   (d.`service_id`=10 or d.service_id=204 or d.service_id=131  and d.service_id=9 or d.service_id=87) or d. project_id in (   select id from t_projects where project_name   like '%%注销%%'  or   project_name   like '%%解约%%')
  group by title_id) d
                    on e.id=d.title_id


                         """ + sql + """

                    order by """ + order_by_colunm + """ desc


                        limit %s,%s
            """, startpage, pre_page)

            t_payment_type = self.db_customer.query(
                "select * from t_type where tag='付费方式'")
            t_promo_types = self.db.query(
                """select * from t_projects_type where income_category='套餐' order by order_int  """
            )

            t_customer_type = self.db_customer.query(
                "select * from t_type where tag='客户类型' and is_show=1")
            t_type_new_parents=self.db_customer.query('''
                    select * from t_type where tag='客户标签1'
                    ''')
            t_type_new=self.db_customer.query('''
                    select * from t_type where tag='客户标签' and parent_id in (1,2) and name!='楼盘'
                    ''')
            self.render(
                'c/payment/list_company_in_customer_req.html',
                customers=customers,
                adjusted_option=self.adjusted_option,
                t_type_new_parents=t_type_new_parents,
                t_type_new=t_type_new,
                t_customer_type=t_customer_type,
                t_promo_types=t_promo_types,
                from_customer=from_customer,
                pagination=pagination,
                t_payment_type=t_payment_type,
                pay_project_id=pay_project_id,
                state=state,
                kf=kf,
                is_handler_uid_name=is_handler_uid_name,
                company=company,
                tag=tag)

        elif tag == "expire_customer":

            kf = self.get_argument("kf", "")

            sql = ""
            page = int(self.get_argument("page", 1))
            date = self.get_argument("date", "2")
            pre_page = 20
            company = self.get_argument('company', '')
            show_tag = self.get_argument("show_tag", "1")
            by_tag = self.get_argument("by_tag","")
            from_expire = self.get_argument("from_expire","")
            export=self.get_argument('export','')
            by_tag_sql =""
            order_by_colunm = " c.acc_end "
           
            if by_tag =="正常":
                by_tag_sql = " and a.id not in  (select id from t_customer where  customer_type_name  like '%%解约%%' or customer_type_name  like '%%停账%%' or customer_type_name  like '%%注销%%' or customer_type_name  like '%%取消%%' or customer_type_name  like '%%逾期%%') "
            elif by_tag=='楼盘':
                by_tag_sql=' and a.is_building=1 '
            elif by_tag=='汇算清缴':
                by_tag_sql=' and a.is_clearly=1 '
            elif by_tag=='工商年检':
                by_tag_sql=' and a.is_year=1 '
            elif by_tag:
                by_tag_sql = " and  tag_id_name='%s' "%by_tag
                order_by_colunm = " c.wait_pay_amount "

            show_sql = ""
            if show_tag == "2":
                #and pb_remark is null or pb_remark=''
                show_sql = " and (req_uid  > 0 )"
                order_by_colunm = " c.req_at "
            else:
                show_sql = " and (req_uid  =0) "

            dt_next = datetime.date.today() - relativedelta(months=0)

            sql = """
                    where

                  ( YEAR(c.acc_end) <= YEAR(now()) and MONTH(c.acc_end) <= MONTH(now())
or

 YEAR(c.acc_book_end) <= YEAR(now()) and MONTH(c.acc_book_end) <= MONTH(now())

 or YEAR(c.acc_end)<YEAR(now()) or YEAR(c.acc_book_end)<YEAR(now())

                   )

                 """ + show_sql

            if company:
                sql += """ 
                        and (a.id = '""" + company + """'
                         or a.company like '%%""" + company + """%%' or a.company_reguid like '%%""" + company + """%%' 
                          or a.id in (select customer_id  from t_company_name where name like '%%""" + company + """%%' )
                         )
                
                
                """
            if kf:
                sql += ' and a.acc_uid_name like "%%' + kf + '%%"'


            count = self.db_customer.get('''
                    select count(*) count
                                FROM  t_customer a
                                                                    INNER JOIN t_customer_payment c
                                                                        ON a.id = c.customer_id
                                                                    INNER JOIN
                                                                    (
                                                                        SELECT `customer_id`, MAX(id) max_id
                                                                        FROM t_customer_payment
                                                                        GROUP BY customer_id
                                                                    ) b ON c.customer_id = b.customer_id AND
                                                                            b.max_id = c.id



               ''' + sql + by_tag_sql)
            total = self.db_customer.get('''
                    select ifnull(sum(wait_pay_amount),0) wait_pay_total
                            FROM  t_customer a
                                INNER JOIN t_customer_payment c
                                    ON a.id = c.customer_id
                                INNER JOIN
                                (
                                    SELECT `customer_id`, MAX(id) max_id
                                    FROM t_customer_payment
                                    GROUP BY customer_id
                                ) b ON c.customer_id = b.customer_id AND
                                        b.max_id = c.id
               ''' + sql + by_tag_sql)


            pagination = Pagination(page, pre_page, count.count, self.request)
            startpage = (page - 1) * pre_page
            
      
            limit_sql='' if export else  " limit %s,%s"%(startpage, pre_page)    

            customers = self.db_customer.query("""
                       SELECT  a.company , c.id payment_id,a.remark t_remark,
                    a.paytype_id_name customer_paytype_id_name,
                    a.promo_id_name customer_promo_id_name,
                    a.is_general customer_is_general,
                    a.service_amount customer_service_amount,
                    a.service_amount_month customer_service_amount_month,
                    a.book_amount customer_book_amount,
                    a.customer_type customer_customer_type,
                     a.promo_id customer_promo_id,
                    a.tag_id customer_tag_id,
                    a.tag_id_name customer_tag_id_name,
                    a.tag_parent_id customer_tag_parent_id,
                    a.tag_parent_id_name customer_tag_parent_id_name,
                    a.is_building customer_is_building,
                    a.is_clearly customer_is_clearly,
                    a.is_year customer_is_year,
                     company_reguid,a.remark customer_remark,customer_type_name,DATE_ADD(c.acc_end, INTERVAL 1 MONTH) next_pay_acc_start , a.acc_uid_name,cp_title_id,a.promo_id,is_general,
            customer_type,promo_id_name,a.tag_id,a.tag_id_name,a.tag_parent_id,a.tag_parent_id_name,a.is_building,a.is_clearly,a.is_year,
                        DATE_ADD(c.acc_end, INTERVAL a.fee MONTH) next_pay_acc_end,
                        DATE_ADD(c.acc_book_end, INTERVAL 1 MONTH) next_pay_acc_book_start ,
                        DATE_ADD(c.acc_book_end, INTERVAL 12 MONTH) next_pay_acc_book_end, c.*,
                        a.guid,a.company,c.updated_at pay_updated_at,c.uid_name pay_uid_name,
                        c.pay_typeid_name pay_pay_typeid_name,c.service_amount pay_service_amount,
                                                                c.service_month_amount pay_service_amount_month, c.book_amount pay_book_amount
                                                                FROM  t_customer a
                                                                    INNER JOIN t_customer_payment c
                                                                        ON a.id = c.customer_id
                                                                       INNER JOIN
                                                                    (
                                                                        SELECT `customer_id`, MAX(id) max_id
                                                                        FROM t_customer_payment
                                                                        GROUP BY customer_id
                                                                    ) b ON c.customer_id = b.customer_id AND
                                                                            b.max_id = c.id

                                          """ + sql + by_tag_sql + """
                             order by """+order_by_colunm+""" desc """+limit_sql)
                
            if export:
                wb=xlwt.Workbook(encoding='utf-8')
                sh=wb.add_sheet(u'即将到期客户费用列表')

                first_col = sh.col(0)
                first_col.width = 100 * 150  # Set the column width
                sh.write(0,0,u'公司名称')
                sh.write(0,1,u'会计')
                sh.write(0,2,u'付款方式')
                sh.write(0,3,u'总服务费')
                sh.write(0,4,u'月服务费')
                sh.write(0,5,u'帐册费')
                sh.write(0,6,u'记账到期')
                sh.write(0,7,u'账册到期')
                sh.write(0,8,u'最新收款明细')
                sh.write(0,9,u'待收明细')
                sh.write(0,10,u'待收金额')
                for idx,row in enumerate(customers):
                    idx+=1
                    company=row.company
                    if row.is_general:
                        company+=u'\n一般纳税人'
                    if row.tag_parent_id_name!=row.tag_id_name:
                        company+=u'\n'+row.tag_parent_id_name
                    
                    if row.tag_id_name:
                        company+=u' '+row.tag_id_name
                    if row.is_building:
                        company+=u' 楼盘'
                    if row.is_year:
                        company+=u' 工商年检'
                    if row.is_clearly:
                        company+=u' 汇算清缴'
                        
                    if row.company_reguid:
                        company+=u'\n'+row.company_reguid
                    if self.adjusted_option(row.customer_id):
                        if self.adjusted_option(row.customer_id).adjusted_option:
                            company+=u'\n'+self.adjusted_option(row.customer_id).adjusted_option
                    company+=u'\n付款方式:'+row.customer_paytype_id_name+u' '+\
                    str(row.customer_service_amount)+u' （总）/'+str(row.customer_service_amount_month)+u'（月）'+\
                    str(row.customer_book_amount)+u'(帐册费)'
                    sh.write(idx,0,company)
                

                    sh.write(idx,1,row.acc_uid_name)
                    sh.write(idx,2,row.pay_pay_typeid_name)
                    sh.write(idx,3,row.pay_service_amount)
                    sh.write(idx,4,row.pay_service_amount_month)
                    sh.write(idx,5,row.pay_book_amount)
                    if row.acc_end:
                        sh.write(idx,6,row.acc_end.strftime("%Y-%m"))
                    else:
                        sh.write(idx,6,u'')

                    if row.acc_book_end:
                        sh.write(idx,7,row.acc_book_end.strftime("%Y-%m"))
                    else:
                        sh.write(idx,7,u'')
                    if row.al_remark:
                        sh.write(idx,8,row.al_remark)
                    else:
                        sh.write(idx,8,u'')
                    if row.pb_remark:
                        sh.write(idx,9,row.pb_remark)
                    else:
                        sh.write(idx,9,u'')

                    sh.write(idx,10,row.wait_pay_amount)
                    sh.row(idx).height_mismatch = True
                    sh.row(idx).height = 30 * 40 

                wb.save('media/output/即将到期客户费用列表.xls')

                return self.write({'output_path':'static/output/即将到期客户费用列表.xls'})

            # print """
            #            SELECT  a.remark customer_remark,DATE_ADD(c.acc_end, INTERVAL 1 MONTH) next_pay_acc_start , a.acc_uid_name,cp_title_id,a.promo_id,is_general,
            # customer_type,promo_id_name,
            #             DATE_ADD(c.acc_end, INTERVAL a.fee MONTH) next_pay_acc_end,
            #             DATE_ADD(c.acc_book_end, INTERVAL 1 MONTH) next_pay_acc_book_start ,
            #             DATE_ADD(c.acc_book_end, INTERVAL 12 MONTH) next_pay_acc_book_end, c.*,
            #             a.guid,a.company,c.updated_at pay_updated_at,c.uid_name pay_uid_name,
            #             c.pay_typeid_name pay_pay_typeid_name,c.service_amount pay_service_amount,
            #                                                     c.service_month_amount pay_service_amount_month, c.book_amount pay_book_amount
            #                                                     FROM  t_customer a
            #                                                         INNER JOIN t_customer_payment c
            #                                                             ON a.id = c.customer_id
            #                                                            INNER JOIN
            #                                                         (
            #                                                             SELECT `customer_id`, MAX(id) max_id
            #                                                             FROM t_customer_payment
            #                                                             GROUP BY customer_id
            #                                                         ) b ON c.customer_id = b.customer_id AND
            #                                                                 b.max_id = c.id

            #                               """ + sql + by_tag_sql + """
            #                  order by """+order_by_colunm+""" desc
            #             limit %s,%s
            # """
            t_payment_type = self.db_customer.query(
                "select * from t_type where tag='付费方式'")
            t_promo_types = self.db.query(
                """select * from t_projects_type where income_category='套餐' order by order_int  """
            )

            t_customer_type = self.db_customer.query(
                "select * from t_type where tag='客户标签' and is_show=1  order by `order` ")
            t_type_new_parents=self.db_customer.query('''
                    select * from t_type where tag='客户标签1'
                    ''')
            t_type_new=self.db_customer.query('''
                    select * from t_type where tag='客户标签' and parent_id in (1,2) and name!='楼盘'
                    ''')
            self.render(
                'c/payment/expire_customer.html',
                from_expire=from_expire,
                t_type_new_parents=t_type_new_parents,
                t_type_new=t_type_new,
                date=date,
                total=total,
                kf=kf,
                adjusted_option=self.adjusted_option,
                t_customer_type=t_customer_type,
                t_promo_types=t_promo_types,
                by_tag=by_tag,
                dt_next=dt_next,
                customers=customers,
                pagination=pagination,
                t_payment_type=t_payment_type,
                show_tag=show_tag,
                compare_date=self.compare_date,
                company=company,
                tag=tag)
        elif tag == "expire_customer_req":

            kf = self.get_argument("kf", "")
            from_expire = self.get_argument("from_expire","")
            sql = ""
            page = int(self.get_argument("page", 1))
            date = self.get_argument("date", "2")
            pre_page = 20
            company = self.get_argument('company', '')
            req_uid_name=self.get_argument('req_uid_name','')
            show_tag = self.get_argument("show_tag", "2")
            by_tag = self.get_argument("by_tag", "")
            by_tag_sql = ""
            order_by_colunm = " c.req_at "
            if by_tag == "正常":
                by_tag_sql = " and a.id not in  (select id from t_customer where  customer_type_name  like '%%解约%%' or customer_type_name  like '%%停账%%' or customer_type_name  like '%%注销%%' or customer_type_name  like '%%取消%%' or customer_type_name  like '%%逾期%%') "
            elif by_tag:
                by_tag_sql = " and  customer_type_name like '%%" + by_tag + "%%'"

            show_sql = ""
            if show_tag == "2":
                #and pb_remark is null or pb_remark=''
                show_sql = " and (req_uid  > 0 and pfi_confirm_state=2 )"
                order_by_colunm = " c.pfi_confirm_at "
            elif show_tag=='-1000':
                show_sql=" and req_uid>0 and TIMESTAMPDIFF(MONTH,c.acc_end, DATE_FORMAT(now(), '%%Y-%%m-%%d'))>=1 and wait_pay_amount>0 "
            elif show_tag=="1":
                show_sql = " and (req_uid  > 0 and pfi_confirm_state=1)"
                order_by_colunm = " c.pfi_confirm_at "
            else:
                show_sql = " and (req_uid  > 0  and pfi_confirm_state=0)  "

            dt_next = datetime.date.today() - relativedelta(months=0)
            sql +=show_sql
            #             sql = """
            #                     where

            #                   ( YEAR(c.acc_end) = YEAR(now()) and MONTH(c.acc_end) <= MONTH(now())
            # or

            #  YEAR(c.acc_book_end) = YEAR(now()) and MONTH(c.acc_book_end) <= MONTH(now())

            #                    )

            #                  """ + show_sql
            if company:
                sql += """ 
                        and (a.id = '""" + company + """'
                         or a.company like '%%""" + company + """%%' or a.company_reguid like '%%""" + company + """%%' 
                         or a.id in (select customer_id  from t_company_name where name like '%%""" + company + """%%' )
                         )
                
                
                """
            if kf:
                sql += ' and a.acc_uid_name like "%%' + kf + '%%"'
            if req_uid_name:
                sql+=' and c.req_uid_name like "%%'+req_uid_name+'%%" '
            count = self.db_customer.get('''
                    select count(*) count
                                FROM  t_customer a
                                                                    INNER JOIN t_customer_payment c
                                                                        ON a.id = c.customer_id
                                                                    INNER JOIN
                                                                    (
                                                                        SELECT `customer_id`, MAX(id) max_id
                                                                        FROM t_customer_payment
                                                                        GROUP BY customer_id
                                                                    ) b ON c.customer_id = b.customer_id AND
                                                                            b.max_id = c.id



               ''' + sql + by_tag_sql)
            total = self.db_customer.get('''
                    select ifnull(sum(wait_pay_amount),0) wait_pay_total
                            FROM  t_customer a
                                INNER JOIN t_customer_payment c
                                    ON a.id = c.customer_id
                                INNER JOIN
                                (
                                    SELECT `customer_id`, MAX(id) max_id
                                    FROM t_customer_payment
                                    GROUP BY customer_id
                                ) b ON c.customer_id = b.customer_id AND
                                        b.max_id = c.id
               ''' + sql + by_tag_sql)

            pagination = Pagination(page, pre_page, count.count, self.request)
            startpage = (page - 1) * pre_page

            customers = self.db_customer.query("""
                         SELECT a.company , c.id payment_id,a.remark  t_remark,
                    a.paytype_id_name customer_paytype_id_name,
                    a.promo_id_name customer_promo_id_name,
                    a.is_general customer_is_general,
                    a.service_amount customer_service_amount,
                    a.service_amount_month customer_service_amount_month,
                    a.book_amount customer_book_amount,
                    a.customer_type customer_customer_type,
                    a.tag_id customer_tag_id,
                    a.tag_id_name customer_tag_id_name,
                    a.tag_parent_id customer_tag_parent_id,
                    a.tag_parent_id_name customer_tag_parent_id_name,
                    a.is_building customer_is_building,
                    a.is_clearly customer_is_clearly,
                    a.is_year customer_is_year,
                        a.promo_id customer_promo_id,
                        company_reguid,a.remark customer_remark,customer_type_name, DATE_ADD(c.acc_end, INTERVAL 1 MONTH)
                       next_pay_acc_start , a.acc_uid_name,cp_title_id,a.promo_id,is_general,
            customer_type,promo_id_name,a.tag_id,a.tag_id_name,a.tag_parent_id,a.tag_parent_id_name,a.is_building,a.is_clearly,a.is_year,
                        DATE_ADD(c.acc_end, INTERVAL a.fee MONTH) next_pay_acc_end,
                        DATE_ADD(c.acc_book_end, INTERVAL 1 MONTH) next_pay_acc_book_start ,
                        DATE_ADD(c.acc_book_end, INTERVAL 12 MONTH) next_pay_acc_book_end, c.*,
                        a.guid,a.company,c.updated_at pay_updated_at,c.uid_name pay_uid_name,
                        c.pay_typeid_name pay_pay_typeid_name,c.service_amount pay_service_amount,
                      c.service_month_amount pay_service_amount_month, c.book_amount pay_book_amount,c.fee payment_fee,
                      c.id pay_id1,pfi_confirm_state,pfi_confirm_remark
                                                                FROM  t_customer a
                                                                    INNER JOIN t_customer_payment c
                                                                        ON a.id = c.customer_id
                                                                       INNER JOIN
                                                                    (
                                                                        SELECT `customer_id`, MAX(id) max_id
                                                                        FROM t_customer_payment
                                                                        GROUP BY customer_id
                                                                    ) b ON c.customer_id = b.customer_id AND
                                                                            b.max_id = c.id

                                          """ + sql + by_tag_sql + """
                             order by """ + order_by_colunm + """ desc
                        limit %s,%s
            """, startpage, pre_page)
            t_payment_type = self.db_customer.query(
                "select * from t_type where tag='付费方式'")
            t_promo_types = self.db.query(
                """select * from t_projects_type where income_category='套餐' order by order_int  """
            )

            t_customer_type = self.db_customer.query(
                "select * from t_type where tag='客户类型'")
            t_type_new_parents=self.db_customer.query('''
                    select * from t_type where tag='客户标签1'
                    ''')
            t_type_new=self.db_customer.query('''
                    select * from t_type where tag='客户标签' and parent_id in (1,2) and name!='楼盘'
                    ''')
            self.render(
                'c/payment/expire_customer_req.html',
                date=date,
                t_type_new_parents=t_type_new_parents,
                t_type_new=t_type_new,
                from_expire=from_expire,
                total=total,
                kf=kf,
                adjusted_option=self.adjusted_option,
                req_uid_name=req_uid_name,
                t_customer_type=t_customer_type,
                t_promo_types=t_promo_types,
                by_tag=by_tag,
                dt_next=dt_next,
                customers=customers,
                pagination=pagination,
                t_payment_type=t_payment_type,
                show_tag=show_tag,
                compare_date=self.compare_date,
                company=company,
                tag=tag)

        elif tag=="assist_list":
            sql=''
            page = int(self.get_argument("page", 1))
            pre_page = 20
            show_tag=self.get_argument('show_tag','')
            dt_next = datetime.date.today() - relativedelta(months=-1)
            order_int=' d.created_at desc '
            department_name=self.get_secure_cookie("department_name")
            count_sql=''
            company_sql=self.get_argument('company_sql','')
            kf_kuaiji=self.get_argument('kf_kuaiji','')
            sale_man=self.get_argument('sale_man','')
            kf_man=self.get_argument('kf_man','')
            genjin_man=self.get_argument('genjin_man','')
            status=self.get_argument('status','')
            bad_debts=self.get_argument('bad_debts','')
            ass_day=self.get_argument('ass_day','')
            ass_day_end=self.get_argument('ass_day_end','')
            ass_num=self.get_argument('ass_num','')
            ass_num_end=self.get_argument('ass_num_end','')
            category_id=self.get_argument('category_id','')
            no_ass_day=self.get_argument('no_ass_day','')
            no_ass_day_end=self.get_argument('no_ass_day_end','')
            acc_end_start=self.get_argument('acc_end_start','')
            acc_end_end=self.get_argument('acc_end_end','')
            acc_book_end_start=self.get_argument('acc_book_end_start','')
            acc_book_end_end=self.get_argument('acc_book_end_end','')
            wait_pay_amount=self.get_argument('wait_pay_amount','')
            ssql=''
            sql_bad=''
            group_sql=''
            if show_tag=='-1000' or show_tag=='-2000':
                search_sql=' and a.id not in (select customer_id from t_customer_payment_assist where customer_id=a.id  and is_bad_debts=1 )  '
            elif show_tag: 
                search_sql=' and d.is_bad_debts=0 '
            else:
                search_sql=''
            if company_sql:
                if (department_name=='销售部' and '250' not in role_list or '302' in role_list) and show_tag=='2' or \
                    ('302' in role_list or '250' in role_list or role=='3' ) and show_tag=='3' :
                    search_sql+='''
                    and (a.id=(select customer_id from t_linkman where name="'''+company_sql+'''" and customer_id=a.id ) or 
                    a.company like "%%'''+company_sql+'''%%")
                    '''
                else:
                    search_sql+='  and a.company like "%%'+company_sql+'%%" '

            if kf_kuaiji:
                search_sql+=' and a.acc_uid_name="%s" '%kf_kuaiji
            if sale_man:
                search_sql+=' and (f.member_name="%s" or c.sale_man="%s") '%(sale_man,sale_man)
            if kf_man:
                search_sql+=' and (e.member_name="%s" or  c.kf_man="%s") '%(kf_man,kf_man)
            if genjin_man:
                search_sql+=' and d.sale_name="%s" '%genjin_man
            if status:
                search_sql+=' and d.status=%s '%status
            if ass_num.isdigit() and ass_num_end.isdigit():
                search_sql+=' and d.sale_genjin_count between "%s" and "%s" '%(ass_num,ass_num_end)
            if ass_day.isdigit() and ass_day_end.isdigit():
                search_sql+=" and d.jd_at is not null and datediff(DATE_FORMAT(now(), '%%Y-%%m-%%d'),DATE_FORMAT(d.distribute_at,'%%Y-%%m-%%d'))  between '"+ass_day+"' and '"+ ass_day_end+"'"
            if no_ass_day.isdigit() and no_ass_day_end.isdigit():
                search_sql+=" and d.jd_at is not null and datediff(DATE_FORMAT(now(), '%%Y-%%m-%%d'),DATE_FORMAT(h.created_at,'%%Y-%%m-%%d'))  between '"+no_ass_day+"' and '"+no_ass_day_end+"'"
            if acc_end_start and acc_end_end:
                search_sql+=' and DATE_FORMAT(c.acc_end,"%%Y-%%m")  between "'+acc_end_start+'" and "'+acc_end_end+'"'
            if acc_book_end_start and acc_book_end_end:
                search_sql+=' and DATE_FORMAT(c.acc_book_end,"%%Y-%%m")  between "'+acc_book_end_start+'" and "'+acc_book_end_end+'"'
            if wait_pay_amount:
                search_sql+=' and c.wait_pay_amount<>0.00 '
            params={
                'company_sql':company_sql,
                'kf_kuaiji':kf_kuaiji,
                'sale_man':sale_man,
                'kf_man':kf_man,
                'genjin_man':genjin_man,
                'status':status,
                'ass_num':ass_num,
                'ass_num_end':ass_num_end,
                'ass_day':ass_day,
                'ass_day_end':ass_day_end,
                'category_id':category_id,
                'no_ass_day':no_ass_day,
                'no_ass_day_end':no_ass_day_end,
                'acc_end_start':acc_end_start,
                'acc_end_end':acc_end_end,
                'acc_book_end_start':acc_book_end_start,
                'acc_book_end_end':acc_book_end_end,
                'wait_pay_amount':wait_pay_amount
            }
            if category_id=='ungroup':
                search_sql+=' and d.id not in (select assist_id from t_customer_payment_assist_group where d.id=assist_id and uid=%s) '%uid
            elif category_id:
                group_sql+=' inner join t_customer_payment_assist_group ag on d.id=ag.assist_id and category_id=%s  and uid=%s '%(category_id,uid)


            if department_name=='销售部' and '250' not in role_list or '302' in role_list:
                sql=' where d.sale_id=%s and d.is_bad_debts=0 '%uid
                sql_bad=' and sale_id=%s '%uid
                count_sql=' and d.sale_id=%s '%uid
                if show_tag=='1':
                    sql+=' and d.jd_at is null '
                elif show_tag=='2':
                    sql+='  and d.jd_at is not null and d.sale_end_at is null '
                    order_int=' h.created_at desc '
                elif show_tag=='3':
                    sql+='  and d.jd_at is not null and d.sale_end_at is not null and d.is_check=0 '
                elif show_tag=='4':
                    sql+=' and d.is_check=2  and d.jd_at is not null and d.sale_end_at is not null '
                elif show_tag=='5':
                    sql+=''' and d.is_check=1  and d.jd_at is not null and d.sale_end_at is not null
                     and  (TIMESTAMPDIFF(MONTH,c.acc_end, DATE_FORMAT(now(), "%%Y-%%m-%%d"))<1
                      or  datediff(DATE_FORMAT(now(),'%%Y-%%m-%%d'),DATE_FORMAT(d.check_at, '%%Y-%%m-%%d'))<=14) '''
                
            elif '250' in role_list or role=='3':
                sql=' and d.is_bad_debts=0 '
                if show_tag=='1':

                    sql+=' and d.distribute_at is null '
                elif show_tag=='2':
                    sql+=' and d.distribute_at  is not null and d.jd_at is null '
                    order_int=' d.distribute_at desc '
                elif show_tag=='3':
                    sql+='  and d.jd_at is not null and d.sale_end_at is null '
                    order_int=' h.created_at desc '
                elif show_tag=='4':
                    sql+=' and d.sale_end_at is not null and  d.is_check=0 '
                    order_int=' d.sale_end_at desc '
                elif show_tag=='5':
                    sql+=' and d.is_check=2  and d.jd_at is not null and d.sale_end_at is not null '
                elif show_tag=='6':
                    sql+=''' and d.is_check=1  and d.jd_at is not null and d.sale_end_at is not null
                     and (TIMESTAMPDIFF(MONTH,c.acc_end, DATE_FORMAT(now(), "%%Y-%%m-%%d"))<1
                      or  datediff(DATE_FORMAT(now(),'%%Y-%%m-%%d'),DATE_FORMAT(d.check_at, '%%Y-%%m-%%d'))<=14)
                      '''
                    order_int=' pb_remark desc,req_close '

            if (show_tag=='-1000' or show_tag=='-2000' or not show_tag) and ((department_name=='销售部' and '250' in role_list) or '250' in role_list or role=='3'):
                sel_sql=''
                if show_tag=='-1000':
                    sel_sql=' h.sale_name, '
                    ssql=""" and (a.id not in ( select customer_id from t_customer_payment_assist)
                     or a.id in ( select i.customer_id from t_customer_payment_assist i where i.is_check=1 and i.is_bad_debts=0
                     and  datediff(DATE_FORMAT(now(),'%%Y-%%m-%%d'),DATE_FORMAT(i.check_at, '%%Y-%%m-%%d'))>14
                     and i.id=(select max(ii.id)
                    from t_customer_payment_assist ii where i.customer_id=ii.customer_id)
                     )  )
                    and TIMESTAMPDIFF(MONTH,c.acc_end, DATE_FORMAT(now(), '%%Y-%%m-%%d'))>=1
                    left join t_customer_payment_assist h on a.id=h.customer_id and h.id=(select max(hh.id)
                    from t_customer_payment_assist hh where h.customer_id=hh.customer_id)

                    """
                    order_int=' c.acc_end desc '
                elif show_tag=='-2000':
                    ssql=""" 
                        and a.id not in ( select customer_id from t_customer_payment_assist) 
                        and TIMESTAMPDIFF(MONTH,c.acc_end, DATE_FORMAT(now(), '%%Y-%%m-%%d'))<=0 
                        """
                    
                    order_int=' c.acc_end desc '
                elif not show_tag:
                    sel_sql=''' h.created_at sale_created_at,d.created_at assist_created_at,d.is_check,d.id assist_id,d.summary,d.sale_id assist_sale_id,
                    TIMESTAMPDIFF(MONTH,c.acc_end, DATE_FORMAT(now(), "%%Y-%%m-%%d")) tsm,
                     datediff(DATE_FORMAT(now(),'%%Y-%%m-%%d'),DATE_FORMAT(d.check_at, '%%Y-%%m-%%d')) wj_day,
                     if(d.sale_end_at,datediff(DATE_FORMAT(d.sale_end_at, '%%Y-%%m-%%d'),DATE_FORMAT(d.distribute_at,'%%Y-%%m-%%d')),
                             datediff(DATE_FORMAT(now(), '%%Y-%%m-%%d'),DATE_FORMAT(d.distribute_at,'%%Y-%%m-%%d'))) genjin_day,
                     '''
                    ssql=''' left join t_customer_payment_assist d on d.customer_id=a.id

                           and d.id=(select max(dd.id)
                            from t_customer_payment_assist dd where d.customer_id=dd.customer_id and dd.is_bad_debts=0 )
                        left join t_customer_exchange h on a.id=h.customer_id 
                            and h.id=(select MAX(gg.id) g_id from t_customer_exchange gg where a.id=gg.customer_id 
                                and d.sale_id=gg.uid and h.created_at>=d.created_at )

                     '''
                    search_sql+='''
                    and a.id not in (
                        select customer_id from  t_customer_payment_assist d where d.customer_id=a.id

                           and d.id=(select max(dd.id)
                            from t_customer_payment_assist dd where d.customer_id=dd.customer_id and dd.is_bad_debts=1)
                    )
                    '''
                    order_int=order_int+',c.acc_end desc '
                count = self.db_customer.get('''
                        select count(*) count ,ifnull(sum(c.wait_pay_amount),0) sw,
                        (select count(*)
                                FROM  t_customer a
                                    INNER JOIN t_customer_payment c
                                        ON a.id = c.customer_id
                                    INNER JOIN
                                    (
                                        SELECT `customer_id`, MAX(id) max_id
                                        FROM t_customer_payment
                                        GROUP BY customer_id
                                    ) b ON c.customer_id = b.customer_id AND
                                            b.max_id = c.id
                                    where  wait_pay_amount<>0.00
                                         and (a.id not in ( select customer_id from t_customer_payment_assist)
                     or a.id in ( select i.customer_id from t_customer_payment_assist i where i.is_check=1
                      and  datediff(DATE_FORMAT(now(),'%%Y-%%m-%%d'),DATE_FORMAT(i.check_at, '%%Y-%%m-%%d'))>14
                        and i.id=(select max(ii.id)
                    from t_customer_payment_assist ii where i.customer_id=ii.customer_id)
                     ) )
                    and TIMESTAMPDIFF(MONTH,c.acc_end, DATE_FORMAT(now(), '%%Y-%%m-%%d'))>=1
                            )ff,
                                    (select count(*)
                                FROM  t_customer a
                                    INNER JOIN t_customer_payment c
                                        ON a.id = c.customer_id
                                    INNER JOIN
                                    (
                                        SELECT `customer_id`, MAX(id) max_id
                                        FROM t_customer_payment
                                        GROUP BY customer_id
                                    ) b ON c.customer_id = b.customer_id AND
                                            b.max_id = c.id
                                    where TIMESTAMPDIFF(MONTH,c.acc_end, DATE_FORMAT(now(), '%%Y-%%m-%%d'))<=0 and wait_pay_amount<>0.00
                                   and a.id not in ( select customer_id from t_customer_payment_assist)
                            )fff,
                        (
                            select count(*)
                                FROM  t_customer a
                                    INNER JOIN t_customer_payment c
                                        ON a.id = c.customer_id
                                    INNER JOIN
                                    (
                                        SELECT `customer_id`, MAX(id) max_id
                                        FROM t_customer_payment
                                        GROUP BY customer_id
                                    ) b ON c.customer_id = b.customer_id AND
                                            b.max_id = c.id
                                    where  wait_pay_amount<>0.00
                                     and a.id not in (
                        select customer_id from  t_customer_payment_assist d where d.customer_id=a.id

                           and d.id=(select max(dd.id)
                            from t_customer_payment_assist dd where d.customer_id=dd.customer_id and dd.is_bad_debts=1)
                    )

                         ) aa,
                                                    (select count(*) from t_customer_payment_assist a
                                INNER JOIN(
                                        SELECT `customer_id`, MAX(id) max_id,acc_end
                                        FROM t_customer_payment
                                        GROUP BY customer_id) b
                                        on a.customer_id=b.customer_id

                            where distribute_at is null '''+count_sql+''')bb,
                            (select count(*) from t_customer_payment_assist where distribute_at  is not null and jd_at is null '''+count_sql+''') cc,
                            (select count(*) from t_customer_payment_assist where  jd_at is not null and is_bad_debts=0 and sale_end_at is null '''+count_sql+''') dd,
                            (select count(*) from t_customer_payment_assist where jd_at is not null and sale_end_at is not null  and is_check=0 '''+count_sql+''') ee,
                            (select count(*) from t_customer_payment_assist where jd_at is not null and sale_end_at is not null and is_check=2 and  is_bad_debts=0  '''+count_sql+''') gg,
                            (select count(*) from t_customer_payment_assist a
                            				inner join ( select max(id) id,customer_id from t_customer_payment_assist
                                group by customer_id
                                )aa on a.customer_id=aa.customer_id and a.id=aa.id
                        inner join t_customer_payment c on  a.customer_id=c.customer_id
                        and
                         (TIMESTAMPDIFF(MONTH,c.acc_end, DATE_FORMAT(now(), "%%Y-%%m-%%d"))<1
                      or  datediff(DATE_FORMAT(now(),'%%Y-%%m-%%d'),DATE_FORMAT(a.check_at, '%%Y-%%m-%%d'))<=14)
                           INNER JOIN
                                                (
                                                    SELECT `customer_id`, MAX(id) max_id,acc_end
                                                    FROM t_customer_payment
                                                    GROUP BY customer_id
                                                ) b ON c.customer_id = b.customer_id AND
                                                        b.max_id = c.id
                         where jd_at is not null and sale_end_at is not null and is_check=1 '''+count_sql+''') hh,
                         (select count(*)
                                FROM  t_customer_payment_assist
                               where is_bad_debts=1)ii
                                FROM  t_customer a
                                    INNER JOIN t_customer_payment c
                                        ON a.id = c.customer_id
                                    INNER JOIN
                                    (
                                        SELECT `customer_id`, MAX(id) max_id
                                        FROM t_customer_payment
                                        GROUP BY customer_id
                                    ) b ON c.customer_id = b.customer_id AND
                                            b.max_id = c.id
                                '''+ssql+'''
                                  left join '''+options.mysql_database+'''.t_projects_member f on
                                    c.project_id=f.project_id and f.team_id=34
                            left join '''+options.mysql_database+'''.t_projects_member e on
                                    c.project_id=e.project_id and e.team_id=36

                                    where  wait_pay_amount<>0.00

                '''+search_sql)
                pagination = Pagination(page, pre_page, count.count, self.request)
                startpage = (page - 1) * pre_page
                customers = self.db_customer.query("""
                        SELECT  *,"""+sel_sql+""" c.id payment_id,a.id customer_id,
                        g.id sale_cuikuan_id,c.acc_end,c.acc_book_end,a.guid customer_guid,
                        c.updated_at pay_updated_at,c.uid_name pay_uid_name,c.wait_pay_amount,
                        c.pay_typeid pay_pay_typeid_id, c.pay_typeid_name pay_pay_typeid_name,
                        c.service_amount pay_service_amount,c.service_month_amount pay_service_amount_month,
                        c.book_amount pay_book_amount,c.sale_man sale_man1,c.kf_man kf_man1,
                        a.acc_uid_name,f.member_name sale_man,e.member_name kf_man,a.remark customer_remark,
                        DATE_ADD(c.acc_end, INTERVAL a.fee MONTH) next_pay_acc_end,
                                DATE_ADD(c.acc_book_end, INTERVAL 1 MONTH) next_pay_acc_book_start ,
                                DATE_ADD(c.acc_book_end, INTERVAL a.fee MONTH) next_pay_acc_book_end,
                                DATE_ADD(c.acc_end, INTERVAL 1 MONTH) next_pay_acc_start,
                                TIMESTAMPDIFF(MONTH,DATE_FORMAT(c.acc_book_end, '%%Y-%%m-%%d'), DATE_FORMAT(now(), '%%Y-%%m-%%d')) acc_book_end_expire
                        FROM  t_customer a
                            INNER JOIN t_customer_payment c
                                ON a.id = c.customer_id
                            INNER JOIN
                            (
                                SELECT `customer_id`, MAX(id) max_id
                                FROM t_customer_payment
                                GROUP BY customer_id
                            ) b ON c.customer_id = b.customer_id AND
                                    b.max_id = c.id
                            """+ssql+"""
                            left join """+options.mysql_database+""".t_projects_member f on
                                    c.project_id=f.project_id and f.team_id=34
                            left join """+options.mysql_database+""".t_projects_member e on
                                    c.project_id=e.project_id and e.team_id=36
                        left join t_customer_exchange g on a.id=g.customer_id and  g.isvisible=2
                        and g.id=(select MAX(gg.id) g_id from t_customer_exchange gg where a.id=gg.customer_id and gg.isvisible=2 )
                                    
                                    where
                                    wait_pay_amount<>0.00
                                     
                                     """+search_sql+"""
                            order by """+order_int+"""
                            limit %s,%s
                """, startpage, pre_page)
                # print("""
                #         SELECT  *,"""+sel_sql+""" c.id payment_id,a.id customer_id,
                #         g.id sale_cuikuan_id,c.acc_end,c.acc_book_end,a.guid customer_guid,
                #         c.updated_at pay_updated_at,c.uid_name pay_uid_name,c.wait_pay_amount,
                #         c.pay_typeid pay_pay_typeid_id, c.pay_typeid_name pay_pay_typeid_name,
                #         c.service_amount pay_service_amount,c.service_month_amount pay_service_amount_month,
                #         c.book_amount pay_book_amount,c.sale_man sale_man1,c.kf_man kf_man1,
                #         a.acc_uid_name,f.member_name sale_man,e.member_name kf_man,a.remark customer_remark,
                #         DATE_ADD(c.acc_end, INTERVAL a.fee MONTH) next_pay_acc_end,
                #                 DATE_ADD(c.acc_book_end, INTERVAL 1 MONTH) next_pay_acc_book_start ,
                #                 DATE_ADD(c.acc_book_end, INTERVAL a.fee MONTH) next_pay_acc_book_end,
                #                 DATE_ADD(c.acc_end, INTERVAL 1 MONTH) next_pay_acc_start,
                #                 TIMESTAMPDIFF(MONTH,DATE_FORMAT(c.acc_book_end, '%%Y-%%m-%%d'), DATE_FORMAT(now(), '%%Y-%%m-%%d')) acc_book_end_expire
                #         FROM  t_customer a
                #             INNER JOIN t_customer_payment c
                #                 ON a.id = c.customer_id
                #             INNER JOIN
                #             (
                #                 SELECT `customer_id`, MAX(id) max_id
                #                 FROM t_customer_payment
                #                 GROUP BY customer_id
                #             ) b ON c.customer_id = b.customer_id AND
                #                     b.max_id = c.id
                #             """+ssql+"""
                #             left join """+options.mysql_database+""".t_projects_member f on
                #                     c.project_id=f.project_id and f.team_id=34
                #             left join """+options.mysql_database+""".t_projects_member e on
                #                     c.project_id=e.project_id and e.team_id=36
                #         left join t_customer_exchange g on a.id=g.customer_id and  g.isvisible=2
                #         and g.id=(select MAX(gg.id) g_id from t_customer_exchange gg where a.id=gg.customer_id and gg.isvisible=2 )
                                    
                #                     where
                #                     wait_pay_amount<>0.00
                                     
                #                      """+search_sql)
            else:
                if department_name=='销售部' and '250' not in role_list or '302' in role_list :
                    ssql='''
                         (select count(*) from t_customer_payment_assist a
                            INNER JOIN(
                                       SELECT `customer_id`, MAX(id) max_id,acc_end
                                       FROM t_customer_payment
                                       GROUP BY customer_id) b
                                       on a.customer_id=b.customer_id
                                       and TIMESTAMPDIFF(MONTH,b.acc_end, DATE_FORMAT(now(), '%%Y-%%m-%%d'))>=1

                         where distribute_at is null '''+count_sql+''') ff
                    '''
                elif '250'  in role_list or role=='3' :
                    ssql='''
                    (select count(*)
                         FROM  t_customer a
                                INNER JOIN t_customer_payment c
                                    ON a.id = c.customer_id
                                INNER JOIN
                                (
                                    SELECT `customer_id`, MAX(id) max_id
                                    FROM t_customer_payment
                                    GROUP BY customer_id
                                ) b ON c.customer_id = b.customer_id AND
                                        b.max_id = c.id where wait_pay_amount<>0.00
                                         and (a.id not in ( select customer_id from t_customer_payment_assist)
                                        or a.id in ( select i.customer_id from t_customer_payment_assist i where i.is_check=1
                                           and  datediff(DATE_FORMAT(now(),'%%Y-%%m-%%d'),DATE_FORMAT(i.check_at, '%%Y-%%m-%%d'))>14
                                             and i.id=(select max(ii.id)
                    from t_customer_payment_assist ii where i.customer_id=ii.customer_id)
                                        ) )
                                        and TIMESTAMPDIFF(MONTH,c.acc_end, DATE_FORMAT(now(), '%%Y-%%m-%%d'))>=1
                                        and a.id not in (select customer_id from t_customer_payment_assist where customer_id=a.id  and is_bad_debts=1 )
                                        )ff,
                      (select count(*)
                         FROM  t_customer a
                                INNER JOIN t_customer_payment c
                                    ON a.id = c.customer_id
                                INNER JOIN
                                (
                                    SELECT `customer_id`, MAX(id) max_id
                                    FROM t_customer_payment
                                    GROUP BY customer_id
                                ) b ON c.customer_id = b.customer_id AND
                                        b.max_id = c.id where TIMESTAMPDIFF(MONTH,c.acc_end, DATE_FORMAT(now(), '%%Y-%%m-%%d'))<=0 and  wait_pay_amount<>0.00
                                         and a.id not in ( select customer_id from t_customer_payment_assist)

                                        )fff


                    '''

                count = self.db_customer.get('''
                        select count(*) count,ifnull(sum(c.wait_pay_amount),0) sw,
                            (
                            select count(*)
                                FROM  t_customer a
                                    INNER JOIN t_customer_payment c
                                        ON a.id = c.customer_id
                                    INNER JOIN
                                    (
                                        SELECT `customer_id`, MAX(id) max_id
                                        FROM t_customer_payment
                                        GROUP BY customer_id
                                    ) b ON c.customer_id = b.customer_id AND
                                            b.max_id = c.id
                                    where  wait_pay_amount<>0.00
                         and a.id not in (
                        select customer_id from  t_customer_payment_assist d where d.customer_id=a.id

                           and d.id=(select max(dd.id)
                            from t_customer_payment_assist dd where d.customer_id=dd.customer_id and dd.is_bad_debts=1)
                    )

                         ) aa,
                         ( select count(*)
                              FROM  t_customer_payment_assist d
                              '''+group_sql+'''
                               inner join ( select max(id) id,customer_id from t_customer_payment_assist
                                                                    group by customer_id
                                                                    )dd on d.customer_id=dd.customer_id and d.id=dd.id
                                                inner join t_customer a on d.customer_id=a.id
                                                INNER JOIN t_customer_payment c
                                                    ON a.id = c.customer_id
                                                      left join '''+options.mysql_database+'''.t_projects_member f on
                                                                        c.project_id=f.project_id and f.team_id=34
                                                                        left join '''+options.mysql_database+'''.t_projects_member e on
                                                                                c.project_id=e.project_id and e.team_id=36
                                                INNER JOIN
                                                (
                                                    SELECT `customer_id`, MAX(id) max_id,acc_end
                                                    FROM t_customer_payment
                                                    GROUP BY customer_id
                                                ) b ON c.customer_id = b.customer_id AND
                                                        b.max_id = c.id  where d.sale_id=%s
                         )aaa,
                                                (select count(*) from t_customer_payment_assist a
                            INNER JOIN(
                                       SELECT `customer_id`, MAX(id) max_id,acc_end
                                       FROM t_customer_payment
                                       GROUP BY customer_id) b
                                       on a.customer_id=b.customer_id

                         where distribute_at is null '''+count_sql+''')bb,
                        (select count(*) from t_customer_payment_assist d where d.distribute_at  is not null and d.jd_at is null '''+count_sql+''') cc,
                        (select count(*) from t_customer_payment_assist d where d.jd_at is not null and d.is_bad_debts=0 and d.sale_end_at is null '''+count_sql+''') dd,
                        (select count(*) from t_customer_payment_assist d where d.jd_at is not null and d.sale_end_at is not null  and d.is_check=0 '''+count_sql+''') ee,
                        (select count(*) from t_customer_payment_assist d  where d.jd_at is not null and d.sale_end_at is not null and d.is_check=2 and  d.is_bad_debts=0  and  d.is_bad_debts=0  '''+count_sql+''') gg,
                        (select count(*) from t_customer_payment_assist d
                        				inner join ( select max(id) id,customer_id from t_customer_payment_assist
                            group by customer_id
                            )dd on d.customer_id=dd.customer_id and d.id=dd.id
                        inner join t_customer_payment c on  d.customer_id=c.customer_id

                           INNER JOIN
                                                (
                                                    SELECT `customer_id`, MAX(id) max_id
                                                    FROM t_customer_payment
                                                    GROUP BY customer_id
                                                ) b ON c.customer_id = b.customer_id AND
                                                        b.max_id = c.id
                         where  jd_at is not null and sale_end_at is not null and is_check=1
                           and  (TIMESTAMPDIFF(MONTH,c.acc_end, DATE_FORMAT(now(), "%%Y-%%m-%%d"))<1
                      or  datediff(DATE_FORMAT(now(),'%%Y-%%m-%%d'),DATE_FORMAT(d.check_at, '%%Y-%%m-%%d'))<=14)
                          '''+count_sql+''') hh,
                          (select count(*)
                                FROM  t_customer_payment_assist
                               where is_bad_debts=1 '''+sql_bad+''') ii,
                        '''+ssql+'''
                                FROM  t_customer_payment_assist d
                                 inner join ( select max(id) id,customer_id from t_customer_payment_assist
                                        group by customer_id
                                        )dd on d.customer_id=dd.customer_id and d.id=dd.id
                                                inner join t_customer a on d.customer_id=a.id
                                                left join t_customer_exchange h on a.id=h.customer_id 
                                                 and h.id=(select MAX(gg.id) g_id from t_customer_exchange gg where a.id=gg.customer_id  and d.sale_id=gg.uid and h.created_at>=d.created_at )
                                                INNER JOIN t_customer_payment c
                                                    ON a.id = c.customer_id
                                                      left join '''+options.mysql_database+'''.t_projects_member f on
                                                                        c.project_id=f.project_id and f.team_id=34
                                                                        left join '''+options.mysql_database+'''.t_projects_member e on
                                                                                c.project_id=e.project_id and e.team_id=36
                                                INNER JOIN
                                                (
                                                    SELECT `customer_id`, MAX(id) max_id,acc_end
                                                    FROM t_customer_payment
                                                    GROUP BY customer_id
                                                ) b ON c.customer_id = b.customer_id AND
                                                        b.max_id = c.id
                                            
                                                        

                ''' + sql+search_sql,uid)
                pagination = Pagination(page, pre_page, count.count, self.request)
                startpage = (page - 1) * pre_page
                customers = self.db_customer.query("""
                        SELECT d.*,d.created_at assist_created_at,d.sale_id assist_sale_id,d.id assist_id, DATE_ADD(c.acc_end, INTERVAL 1 MONTH) next_pay_acc_start , a.acc_uid_name a_acc_uid_name ,
                            DATE_ADD(c.acc_end, INTERVAL a.fee MONTH) next_pay_acc_end,a.remark customer_remark,
                             if(d.sale_end_at,datediff(DATE_FORMAT(d.sale_end_at, '%%Y-%%m-%%d'),DATE_FORMAT(d.distribute_at,'%%Y-%%m-%%d')),
                             datediff(DATE_FORMAT(now(), '%%Y-%%m-%%d'),DATE_FORMAT(d.distribute_at,'%%Y-%%m-%%d'))) genjin_day,
                            DATE_ADD(c.acc_book_end, INTERVAL 1 MONTH) next_pay_acc_book_start ,
                            DATE_ADD(c.acc_book_end, INTERVAL a.fee MONTH) next_pay_acc_book_end, 
                            TIMESTAMPDIFF(MONTH,DATE_FORMAT(c.acc_book_end, '%%Y-%%m-%%d'), DATE_FORMAT(now(), '%%Y-%%m-%%d')) acc_book_end_expire,
                            c.*,
                            a.guid customer_guid,a.company,c.updated_at pay_updated_at,c.uid_name pay_uid_name,
                            c.pay_typeid_name pay_pay_typeid_name,c.service_amount pay_service_amount,
                            a.last_cuikuan_at,a.last_cuikuan_msg,a.sale_last_cuikuan_at,a.sale_last_cuikuan_msg,
                                c.service_month_amount pay_service_amount_month, c.book_amount pay_book_amount,
                                f.member_name sale_man,e.member_name kf_man,c.sale_man sale_man1,c.kf_man kf_man1, g.id sale_cuikuan_id,
                                h.created_at sale_created_at
                                                                    FROM  t_customer_payment_assist d
                                                                    """+group_sql+"""
                                                                    inner join ( select max(id) id,customer_id from t_customer_payment_assist
                                                                    group by customer_id
                                                                    )dd on d.customer_id=dd.customer_id and d.id=dd.id
                                                                      inner join t_customer a on d.customer_id=a.id
                                                                        INNER JOIN t_customer_payment c
                                                                            ON a.id = c.customer_id
                                                                        left join """+options.mysql_database+""".t_projects_member f on
                                                                        c.project_id=f.project_id and f.team_id=34
                                                                        left join """+options.mysql_database+""".t_projects_member e on
                                                                                c.project_id=e.project_id and e.team_id=36
                                                                   left join t_customer_exchange g on a.id=g.customer_id and  g.isvisible=2
                                                                    and g.id=(select MAX(gg.id) g_id from t_customer_exchange gg where a.id=gg.customer_id and gg.isvisible=2 )
                                                                      left join t_customer_exchange h on a.id=h.customer_id 
                                                                    and h.id=(select MAX(gg.id) g_id from t_customer_exchange gg where a.id=gg.customer_id  and d.sale_id=gg.uid and h.created_at>=d.created_at )
                                                                        INNER JOIN
                                                                        (
                                                                            SELECT `customer_id`, MAX(id) max_id,acc_end
                                                                            FROM t_customer_payment
                                                                            GROUP BY customer_id
                                                                        ) b ON c.customer_id = b.customer_id AND
                                                                                b.max_id = c.id
                                                                               
                                                                        """ + sql +search_sql+ """
                                                                                        order by """+order_int+"""
                                                                                                limit %s,%s
                
                                                                                    """, startpage, pre_page)
                # print("""
                #                         SELECT d.*,d.created_at assist_created_at,d.sale_id assist_sale_id,d.id assist_id, DATE_ADD(c.acc_end, INTERVAL 1 MONTH) next_pay_acc_start , a.acc_uid_name a_acc_uid_name ,
                #             DATE_ADD(c.acc_end, INTERVAL a.fee MONTH) next_pay_acc_end,a.remark customer_remark,
                #              if(d.sale_end_at,datediff(DATE_FORMAT(d.sale_end_at, '%%Y-%%m-%%d'),DATE_FORMAT(d.distribute_at,'%%Y-%%m-%%d')),
                #              datediff(DATE_FORMAT(now(), '%%Y-%%m-%%d'),DATE_FORMAT(d.distribute_at,'%%Y-%%m-%%d'))) genjin_day,
                #             DATE_ADD(c.acc_book_end, INTERVAL 1 MONTH) next_pay_acc_book_start ,
                #             DATE_ADD(c.acc_book_end, INTERVAL a.fee MONTH) next_pay_acc_book_end, 
                #             TIMESTAMPDIFF(MONTH,DATE_FORMAT(c.acc_book_end, '%%Y-%%m-%%d'), DATE_FORMAT(now(), '%%Y-%%m-%%d')) acc_book_end_expire,
                #             c.*,
                #             a.guid,a.company,c.updated_at pay_updated_at,c.uid_name pay_uid_name,
                #             c.pay_typeid_name pay_pay_typeid_name,c.service_amount pay_service_amount,
                #             a.last_cuikuan_at,a.last_cuikuan_msg,a.sale_last_cuikuan_at,a.sale_last_cuikuan_msg,
                #                 c.service_month_amount pay_service_amount_month, c.book_amount pay_book_amount,
                #                 f.member_name sale_man,e.member_name kf_man,c.sale_man sale_man1,c.kf_man kf_man1, g.id sale_cuikuan_id,
                #                 h.created_at sale_created_at
                #                                                     FROM  t_customer_payment_assist d
                #                                                     """+group_sql+"""
                #                                                     inner join ( select max(id) id,customer_id from t_customer_payment_assist
                #                                                     group by customer_id
                #                                                     )dd on d.customer_id=dd.customer_id and d.id=dd.id
                #                                                       inner join t_customer a on d.customer_id=a.id
                #                                                         INNER JOIN t_customer_payment c
                #                                                             ON a.id = c.customer_id
                #                                                         left join """+options.mysql_database+""".t_projects_member f on
                #                                                         c.project_id=f.project_id and f.team_id=34
                #                                                         left join """+options.mysql_database+""".t_projects_member e on
                #                                                                 c.project_id=e.project_id and e.team_id=36
                #                                                    left join t_customer_exchange g on a.id=g.customer_id and  g.isvisible=2
                #                                                     and g.id=(select MAX(gg.id) g_id from t_customer_exchange gg where a.id=gg.customer_id and gg.isvisible=2 )
                #                                                       left join t_customer_exchange h on a.id=h.customer_id 
                #                                                     and h.id=(select MAX(gg.id) g_id from t_customer_exchange gg where a.id=gg.customer_id  and d.sale_id=gg.uid and h.created_at>=d.created_at )
                #                                                         INNER JOIN
                #                                                         (
                #                                                             SELECT `customer_id`, MAX(id) max_id,acc_end
                #                                                             FROM t_customer_payment
                #                                                             GROUP BY customer_id
                #                                                         ) b ON c.customer_id = b.customer_id AND
                #                                                                 b.max_id = c.id
                                                                               
                #                                                         """ + sql +search_sql+ """
                #                                                                         order by """+order_int
                # )
            t_user_sales=self.db.query('''
                select * from t_user where department_name='销售部' or find_in_set('302',role_list) 
            ''')
            acc_uid_names=self.db_customer.query('''
            select a.acc_uid_name FROM  t_customer a
            INNER JOIN t_customer_payment c
                ON a.id = c.customer_id
            INNER JOIN
            (
                SELECT `customer_id`, MAX(id) max_id
                FROM t_customer_payment
                GROUP BY customer_id
            ) b ON c.customer_id = b.customer_id AND
                    b.max_id = c.id where a.acc_uid_name!=''
                    group by a.acc_uid_name
            ''')
            sale_mans1=self.db_customer.query("""
                                select sale_man from  t_customer_payment
               where sale_man <>'' and
               sale_man is not null and sale_man not in (select member_name from """+options.mysql_database+""".t_projects_member a
                inner join t_customer_payment b on a.project_id=b.project_id
                where a.team_id=34 and member_name is not null and member_name!='' group by member_name )   group by sale_man
            """)
            sale_mans2=self.db.query('''
                select member_name sale_man from t_projects_member a
                inner join '''+options.mysql_database_customer+'''.t_customer_payment b on a.project_id=b.project_id
                where a.team_id=34 and member_name is not null and member_name!='' group by member_name
            ''')
            kf_mans1=self.db_customer.query("""
                                select kf_man from  t_customer_payment
               where kf_man <>'' and
               kf_man is not null and kf_man not in (select member_name from """+options.mysql_database+""".t_projects_member a
                inner join t_customer_payment b on a.project_id=b.project_id
                where a.team_id=36 and member_name is not null and member_name!='' group by member_name )   group by kf_man
            """)

            kf_mans2=self.db.query('''
                select member_name kf_man from t_projects_member a
                inner join '''+options.mysql_database_customer+'''.t_customer_payment b on a.project_id=b.project_id
                where a.team_id=36 and member_name is not null and member_name!='' group by member_name
            ''')

            sale_mans=sale_mans1+sale_mans2
            kf_mans=kf_mans1+kf_mans2
            all_categorys=self.db_customer.query('''
           select * from  t_customer_payment_assist_category  where uid=%s order by order_int desc,id desc
        ''',uid)
            
            self.render(
                'c/payment/assist_list.html',
                tag=tag,
                all_categorys=all_categorys,
                get_assist_linkman=self.get_assist_linkman,
                sale_mans=sale_mans,
                count=count,
                params=params,
                show_sb=self.show_sb,
                get_assist_category=self.get_assist_category,
                t_user_sales=t_user_sales,
                acc_uid_names=acc_uid_names,
                kf_mans=kf_mans,
                show_tag=show_tag,
                dt_next=dt_next,
                pagination=pagination,
                customers=customers,
                time_transition=time_transition,
            )

        elif tag=="bad_debts_list":
            sql=''
            search_sql=''
            bad_debts=self.get_argument('bad_debts','')
            company_sql=self.get_argument('company_sql','')
            kf_kuaiji=self.get_argument('kf_kuaiji','')
            sale_man=self.get_argument('sale_man','')
            kf_man=self.get_argument('kf_man','')
            genjin_man=self.get_argument('genjin_man','')
            other_tag=self.get_argument('other_tag','')
            page = int(self.get_argument("page", 1))
            pre_page = 20
            sql=' and (d.sale_id=%s or a.acc_uid=%s )'%(uid,uid)
            sql_count=' and (sale_id=%s or acc_uid=%s) '%(uid,uid)
            if company_sql:
                search_sql+=' and a.company like "%%'+company_sql+'%%" '
            if kf_kuaiji:
                search_sql+=' and a.acc_uid_name="%s" '%kf_kuaiji
            if sale_man:
                search_sql+=' and (f.member_name="%s" or c.sale_man="%s") '%(sale_man,sale_man)
            if kf_man:
                search_sql+=' and (e.member_name="%s" or  c.kf_man="%s") '%(kf_man,kf_man)
            if genjin_man:
                search_sql+=' and d.sale_name="%s" '%genjin_man

            params={
                'company_sql':company_sql,
                'kf_kuaiji':kf_kuaiji,
                'sale_man':sale_man,
                'kf_man':kf_man,
                'genjin_man':genjin_man,
                'bad_debts':bad_debts,
                'other_tag':other_tag
            }
            if  '250'  in role_list or '285'  in role_list or '286'  in role_list:
                sql=''
                sql_count=''

            if bad_debts=='1':
                sql+=' and  d.bad_debts_sale_checked_at is null and (d.bad_debts_sale_checked_status=0 or d.bad_debts_kj_reject_at is not null) '
            elif bad_debts=='2':
                sql+=' and d.bad_debts_sale_checked_status=1 and d.bad_debts_kj_at is null '
            elif bad_debts=='3':
                sql+=' and d.bad_debts_sale_checked_status=1 and d.bad_debts_kj_at is not null and d.bad_debts_caiwu_checked_at is null '
            elif bad_debts=='4':
                sql+=' and d.bad_debts_caiwu_checked_at is not null and d.bad_debts_caiwu_checked_status=1 '
            elif bad_debts=='5':
                 sql+=' and  d.bad_debts_sale_checked_at is not null and d.bad_debts_sale_checked_status=2 '
            elif bad_debts=='6':
                sql+=' and d.bad_debts_caiwu_checked_at is not null and d.bad_debts_caiwu_checked_status=2 '
            count = self.db_customer.get("""
                        SELECT  count(*) count,sum(wait_pay_amount) sw,
                            (select count(*)
                                FROM  t_customer_payment_assist
                               where is_bad_debts=1 """+sql_count+"""
                            ) a,
                                 (select count(*)
                                FROM  t_customer_payment_assist
                               where is_bad_debts=1 and  bad_debts_sale_checked_at is null and (bad_debts_sale_checked_status=0  or bad_debts_kj_reject_at is not null)
                            """+sql_count+""") b,
                                (select count(*)
                                FROM  t_customer_payment_assist
                               where is_bad_debts=1 and bad_debts_sale_checked_status=1 and bad_debts_kj_at is null 
                            """+sql_count+""") c,
                                (select count(*)
                                FROM  t_customer_payment_assist
                               where is_bad_debts=1 and bad_debts_sale_checked_status=1 and bad_debts_kj_at is not null and bad_debts_caiwu_checked_at is null
                            """+sql_count+""") d,
                                (select count(*)
                                FROM  t_customer_payment_assist
                               where is_bad_debts=1 and bad_debts_caiwu_checked_at is not null and bad_debts_caiwu_checked_status=1
                            """+sql_count+""") e,
                                (select count(*)
                                FROM  t_customer_payment_assist
                               where is_bad_debts=1 and  bad_debts_sale_checked_at is not null and bad_debts_sale_checked_status=2
                            """+sql_count+""") f,
                                (select count(*)
                                FROM  t_customer_payment_assist
                               where is_bad_debts=1 and bad_debts_caiwu_checked_at is not null and bad_debts_caiwu_checked_status=2
                            """+sql_count+""") g
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
                                        b.max_id = c.id where d.is_bad_debts=1
                            """ + sql +search_sql)
            pagination = Pagination(page, pre_page, count.count, self.request)
            startpage = (page - 1) * pre_page
            customers = self.db_customer.query("""
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
                                                                                b.max_id = c.id where d.is_bad_debts=1

                                                                   """ + sql +search_sql+""" limit %s,%s """,startpage,pre_page)
            t_user_sales=self.db.query('''
                select * from t_user where department_name='销售部'
            ''')
            acc_uid_names=self.db_customer.query('''
            select a.acc_uid_name FROM  t_customer a
            INNER JOIN t_customer_payment c
                ON a.id = c.customer_id
            INNER JOIN
            (
                SELECT `customer_id`, MAX(id) max_id
                FROM t_customer_payment
                GROUP BY customer_id
            ) b ON c.customer_id = b.customer_id AND
                    b.max_id = c.id where a.acc_uid_name!=''
                    group by a.acc_uid_name
            ''')
            sale_mans1=self.db_customer.query("""
                                select sale_man from  t_customer_payment
               where sale_man <>'' and
               sale_man is not null and sale_man not in (select member_name from """+options.mysql_database+""".t_projects_member a
                inner join t_customer_payment b on a.project_id=b.project_id
                where a.team_id=34 and member_name is not null and member_name!='' group by member_name )   group by sale_man
            """)
            sale_mans2=self.db.query('''
                select member_name sale_man from t_projects_member a
                inner join '''+options.mysql_database_customer+'''.t_customer_payment b on a.project_id=b.project_id
                where a.team_id=34 and member_name is not null and member_name!='' group by member_name
            ''')
            kf_mans1=self.db_customer.query("""
                                select kf_man from  t_customer_payment
               where kf_man <>'' and
               kf_man is not null and kf_man not in (select member_name from """+options.mysql_database+""".t_projects_member a
                inner join t_customer_payment b on a.project_id=b.project_id
                where a.team_id=36 and member_name is not null and member_name!='' group by member_name )   group by kf_man
            """)

            kf_mans2=self.db.query('''
                select member_name kf_man from t_projects_member a
                inner join '''+options.mysql_database_customer+'''.t_customer_payment b on a.project_id=b.project_id
                where a.team_id=36 and member_name is not null and member_name!='' group by member_name
            ''')
            sale_mans=sale_mans1+sale_mans2
            kf_mans=kf_mans1+kf_mans2
            self.render('c/payment/bad_debts_list.html',
                params=params,
                customers=customers,
                bad_debts=bad_debts,
                count=count,
                t_user_sales=t_user_sales,
                acc_uid_names=acc_uid_names,
                pagination=pagination,
                sale_mans=sale_mans,
                kf_mans=kf_mans,
                tag=tag,
                other_tag=other_tag
            )

        elif tag == "acc_customer_payment":
            sql = ""
            page = int(self.get_argument("page", 1))
            show_tag = self.get_argument("show_tag", "1")
            pre_page = 20

            company = self.get_argument('company', '')
            check_under=self.get_argument('check_under','')
            dt_next = datetime.date.today() - relativedelta(months=-1)
            check_kj=self.get_argument("check_kj",'')
            acc_uids=[]
            assist_sql=''
            assist_sel_sql=''
            order_int=' req_at '
            if show_tag == "2":
                sql = """
                         and (pb_remark <> '' )  and  req_close=0
                        and timestampdiff(MONTH,c.acc_end,date_format(now(),"%%Y-%%m-%%d"))<1
                """
                assist_sel_sql=' ,d.id assist_id '
                assist_sql="""
                    left join t_customer_payment_assist d on a.id=d.customer_id
                """
            if show_tag=="-2000":
                sql = """
                         and (pb_remark <> '' )  and  req_close=0
                        and timestampdiff(MONTH,c.acc_end,date_format(now(),"%%Y-%%m-%%d"))>=1
                """
                assist_sel_sql=' ,d.id assist_id '
                assist_sql="""
                    left join t_customer_payment_assist d on a.id=d.customer_id
                """
            elif show_tag == "3":
                sql = """
                      and (pb_remark ='' or pb_remark is null or req_close=1)
                """
            elif show_tag=="-1000":
                assist_sel_sql=' ,d.assist_msg '
                assist_sql="""
                    right join t_customer_payment_assist d on a.id=d.customer_id
                """
                order_int=' d.created_at '

            if company:
                sql += ' and a.company like "%%' + company + '%%"'
            if check_kj:
                sql+=' and a.acc_uid_name="%s"  '%check_kj
            t_user_relation=self.db.query('''
                    select a.* from t_user_relation a
                    inner join t_user_relation b on
                        find_in_set(a.department_name,b.department_name)
                    and b.uid=%s and b.is_leader<>0
                    where a.uid!=b.uid and a.is_leader=0
                ''',uid)
            if t_user_relation and check_under:
                for item in t_user_relation:
                    acc_uids.append(int(item.uid))
                acc_uids=tuple(acc_uids)
                count = self.db_customer.get('''
                        select count(*) count
                                FROM  t_customer a
                                                INNER JOIN t_customer_payment c
                                                    ON a.id = c.customer_id
                                                INNER JOIN
                                                (
                                                    SELECT `customer_id`, MAX(id) max_id,acc_end
                                                    FROM t_customer_payment
                                                    GROUP BY customer_id
                                                ) b ON c.customer_id = b.customer_id AND
                                                        b.max_id = c.id '''+assist_sql+''' where a.acc_uid in '''+str(acc_uids)+'''



                ''' + sql)

                pagination = Pagination(page, pre_page, count.count, self.request)
                startpage = (page - 1) * pre_page
                customers = self.db_customer.query("""
                        SELECT  DATE_ADD(c.acc_end, INTERVAL 1 MONTH) next_pay_acc_start , a.acc_uid_name,g.id sale_cuikuan_id,
                            DATE_ADD(c.acc_end, INTERVAL a.fee MONTH) next_pay_acc_end,
                            DATE_ADD(c.acc_book_end, INTERVAL 1 MONTH) next_pay_acc_book_start ,
                            DATE_ADD(c.acc_book_end, INTERVAL a.fee MONTH) next_pay_acc_book_end, c.*,
                            a.guid,a.company,c.updated_at pay_updated_at,c.uid_name pay_uid_name,
                            c.pay_typeid_name pay_pay_typeid_name,c.service_amount pay_service_amount,
                            a.last_cuikuan_at,a.last_cuikuan_msg,a.sale_last_cuikuan_at,a.sale_last_cuikuan_msg,
                                                                    c.service_month_amount pay_service_amount_month, c.book_amount pay_book_amount
                                                                    """+assist_sel_sql+"""
                                                                    FROM  t_customer a
                                                                        INNER JOIN t_customer_payment c
                                                                            ON a.id = c.customer_id
                                                                left join t_customer_exchange g on a.id=g.customer_id and  g.isvisible=2
                                                                            and g.id=(select MAX(gg.id) g_id from t_customer_exchange gg where a.id=gg.customer_id and gg.isvisible=2 )
                                                                        INNER JOIN
                                                                        (
                                                                            SELECT `customer_id`, MAX(id) max_id,acc_end
                                                                            FROM t_customer_payment
                                                                            GROUP BY customer_id
                                                                        ) b ON c.customer_id = b.customer_id AND
                                                                                b.max_id = c.id """+assist_sql+""" where a.acc_uid in """+str(acc_uids)+"""
    """ + sql + """
                    order by req_at desc
                            limit %s,%s
                """, startpage, pre_page)
            else:
                count = self.db_customer.get('''
                        select count(*) count
                                FROM  t_customer a
                                                INNER JOIN t_customer_payment c
                                                    ON a.id = c.customer_id
                                                INNER JOIN
                                                (
                                                    SELECT `customer_id`, MAX(id) max_id,acc_end
                                                    FROM t_customer_payment
                                                    GROUP BY customer_id
                                                ) b ON c.customer_id = b.customer_id AND
                                                        b.max_id = c.id '''+assist_sql+''' where a.acc_uid=%s



                ''' + sql, uid)

                pagination = Pagination(page, pre_page, count.count, self.request)
                startpage = (page - 1) * pre_page
                customers = self.db_customer.query("""
                        SELECT  DATE_ADD(c.acc_end, INTERVAL 1 MONTH) next_pay_acc_start , a.acc_uid_name,    g.id sale_cuikuan_id,
                            DATE_ADD(c.acc_end, INTERVAL a.fee MONTH) next_pay_acc_end,
                            DATE_ADD(c.acc_book_end, INTERVAL 1 MONTH) next_pay_acc_book_start ,
                            DATE_ADD(c.acc_book_end, INTERVAL a.fee MONTH) next_pay_acc_book_end, c.*,
                            a.guid,a.company,c.updated_at pay_updated_at,c.uid_name pay_uid_name,
                            c.pay_typeid_name pay_pay_typeid_name,c.service_amount pay_service_amount,
                            a.last_cuikuan_at,a.last_cuikuan_msg,a.sale_last_cuikuan_at,a.sale_last_cuikuan_msg,
                                                                    c.service_month_amount pay_service_amount_month, c.book_amount pay_book_amount
                                                                    """+assist_sel_sql+"""
                                                                    FROM  t_customer a
                                                                        INNER JOIN t_customer_payment c
                                                                            ON a.id = c.customer_id
                                                                            left join t_customer_exchange g on a.id=g.customer_id and  g.isvisible=2
                                                                            and g.id=(select MAX(gg.id) g_id from t_customer_exchange gg where a.id=gg.customer_id and gg.isvisible=2 )
                                                                        INNER JOIN
                                                                        (
                                                                            SELECT `customer_id`, MAX(id) max_id,acc_end
                                                                            FROM t_customer_payment
                                                                            GROUP BY customer_id
                                                                        ) b ON c.customer_id = b.customer_id AND
                                                                                b.max_id = c.id """+assist_sql+""" where a.acc_uid=%s
    """ + sql + """
                    order by """+order_int+""" desc
                            limit %s,%s
                """, uid, startpage, pre_page)
            t_payment_type = self.db_customer.query(
                "select * from t_type where tag='付费方式'")

            self.render(
                'c/payment/acc_customer_payment.html',
                show_tag=show_tag,
                dt_next=dt_next,
                customers=customers,
                pagination=pagination,
                t_payment_type=t_payment_type,
                company=company,
                check_under=check_under,
                t_user_relation=t_user_relation,
                check_kj=check_kj,
                tag=tag)

        elif tag == "reminders_plan":
            show_tag = self.get_argument('show_tag', '1')
            page = int(self.get_argument('page', 1))
            pre_page = 20
            state=self.get_argument('state','0')
            check_under=self.get_argument('check_under','')
            acc_uids=[]
            sql = ''
            t_user_relation=self.db.query('''
                    select a.* from t_user_relation a
                    inner join t_user_relation b on a.department_id=b.department_id and b.uid=%s and b.is_leader<>0
                    where a.uid!=b.uid and a.is_leader=0
                ''',uid)
            if t_user_relation and check_under:
                for item in t_user_relation:
                    acc_uids.append(int(item.uid))
                acc_uids=tuple(acc_uids)
            if state=='0':
                if show_tag == '2':
                    sql = ' and summary is null '
                if show_tag == '3':
                    sql = ' and summary is not null'

                if acc_uids!=[]:
                    sql='  and uid in '+str(acc_uids)
                else:
                    sql=' and uid=%s '%uid

                count = self.db_customer.get(
                    """select count(*) count from t_customer_exchange where  etype=2 and  msg_time is not null  """
                    + sql)
                pagination = Pagination(page, pre_page, count.count, self.request)
                startpage = (page - 1) * pre_page
                t_customer_exchange = self.db_customer.query(
                    """select *  from t_customer_exchange where etype=2 and  msg_time is not null """
                    + sql + """
                    order by TO_DAYS(msg_time)=TO_DAYS(now()) desc, msg_time
                    limit %s,%s""",startpage, pre_page)
            elif state=='1':
                if acc_uids!=[] and role!='8':
                    sql='  and a.uid in '+str(acc_uids)
                elif role!='8':
                    sql=' and a.uid=%s '%uid
                count = self.db_customer.get(
                    """select count(*) count from t_customer_exchange a
                        inner join t_customer b on a.customer_id=b.id
                    where a.etype=2  """+sql
                   )
                pagination = Pagination(page, pre_page, count.count, self.request)
                startpage = (page - 1) * pre_page
                t_customer_exchange = self.db_customer.query(
                    """select a.*,b.acc_uid_name,b.company from t_customer_exchange a
                        inner join t_customer b on a.customer_id=b.id
                    where a.etype=2 """+sql+"""
                        order by a.created_at desc
                    limit %s,%s""", startpage, pre_page)
            self.render(
                'c/payment/reminders_plan.html',
                t_customer_exchange=t_customer_exchange,
                tag=tag,
                t_user_relation=t_user_relation,
                check_under=check_under,
                state=state,
                show_tag=show_tag,
                pagination=pagination)



    def post(self):
        tag = self.get_argument("tag")
        uid_name = self.get_secure_cookie("name")
        role = self.get_secure_cookie("role")
        uid = self.get_secure_cookie("uid")
        dt = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        if tag == "save_payment":
            payment_id = self.get_argument("payment_id")
            pb_remark = self.get_argument("pb_remark", "")
            req_close = self.get_argument("req_close")
            wait_pay_amount = self.get_argument("wait_pay_amount")
            if not payment_id:
                return self.write("not payment_id")
            else:
                # print "payment_id",payment_id
                self.db_customer.execute(
                    "update t_customer_payment set pb_remark=%s,req_uid=%s,req_uid_name=%s,req_at=%s,req_close=%s,wait_pay_amount=%s  where id=%s",
                    pb_remark, uid, uid_name, dt, req_close, wait_pay_amount,
                    payment_id)
        elif tag == "payment_confirm":
            customer_id = self.get_argument("customer_id")
            project_id = self.get_argument("project_id")
            payment_id = self.get_argument("payment_id")
            payment_confirm_state = self.get_argument("payment_confirm_state")
            payment_confirm_remark = self.get_argument(
                "payment_confirm_remark", "")
            if not customer_id:
                return self.write("not customer_id")
            elif not payment_id:
                return self.write("not payment_id")
            else:
                result = self.db_customer.execute("""
                    update t_customer_payment set payment_confirm_remark=%s , payment_confirm_state=%s ,payment_confirm_last_state=%s,

                    payment_confirm_uid=%s , payment_confirm_uid_name=%s,payment_confirm_at=%s
                    where id=%s and customer_id=%s
                """, payment_confirm_remark, payment_confirm_state,payment_confirm_state, uid,
                                                  uid_name, dt, payment_id,
                                                  customer_id)
                self.write(str(result))
        elif tag=="edit":

            acc_end = self.get_argument("acc_end", None)
            acc_book_end = self.get_argument("acc_book_end", None)
            pb_remark = self.get_argument("pb_remark", "")
            al_remark = self.get_argument("al_remark", "")
            payment_confirm_state = self.get_argument("payment_confirm_state",
                                                      0)
            #  pfi_confirm_remark = self.get_argument("pfi_confirm_remark", "")
            wait_pay_amount = self.get_argument("wait_pay_amount", 0)
            payment_id  = self.get_argument("payment_id", 0)
            if payment_id :
                if not acc_end:
                    acc_end = None
                if not acc_book_end:
                    acc_book_end = None
                if acc_end:
                    acc_end = acc_end + "-01"
                else:
                    return self.write("-100")
                if acc_book_end:
                    acc_book_end = acc_book_end + "-01"
                result = self.db_customer.execute("""
                update t_customer_payment set acc_end=%s,
                    acc_book_end=%s,
                    updated_at=%s,
                    payment_confirm_state=%s,pay_handler_at=%s
                    ,pb_remark=%s,al_remark=%s,wait_pay_amount=%s where id=%s
                """, acc_end, acc_book_end, dt, payment_confirm_state, dt,
                                                  pb_remark, al_remark,
                                                  wait_pay_amount, payment_id)
                self.write(str(result))

        elif tag == "edit_curr":

            acc_end = self.get_argument("acc_end", None)
            acc_book_end = self.get_argument("acc_book_end", None)
            pb_remark = self.get_argument("pb_remark", "")
            al_remark = self.get_argument("al_remark", "")
            wait_pay_amount = self.get_argument("wait_pay_amount", 0)
            payment_id = self.get_argument("payment_id", 0)
            if payment_id:
                if not acc_end:
                    acc_end = None
                if not acc_book_end:
                    acc_book_end = None
                if acc_end:
                    acc_end = acc_end + "-01"
                else:
                    return self.write("-100")
                if acc_book_end:
                    acc_book_end = acc_book_end + "-01"
                result = self.db_customer.execute("""
                update t_customer_payment set acc_end=%s,
                    acc_book_end=%s,
                    updated_at=%s,
                    updated_uid=%s
                    ,pb_remark=%s,al_remark=%s,wait_pay_amount=%s where id=%s
                """, acc_end, acc_book_end, dt, uid,
                                                  pb_remark, al_remark,
                                                  wait_pay_amount, payment_id)
                self.write(str(result))

        elif tag == "reset_edit":

            acc_end = self.get_argument("acc_end", None)
            acc_book_end = self.get_argument("acc_book_end", None)
            pb_remark = self.get_argument("pb_remark", "")
            al_remark = self.get_argument("al_remark", "")
            payment_confirm_state = self.get_argument("payment_confirm_state",
                                                      0)
            wait_pay_amount = self.get_argument("wait_pay_amount", 0)
            payment_id = self.get_argument("payment_id", 0)
            if payment_id:
                if not acc_end:
                    acc_end = None
                if not acc_book_end:
                    acc_book_end = None
                if acc_end:
                    acc_end = acc_end + "-01"
                else:
                    return self.write("-100")
                if acc_book_end:
                    acc_book_end = acc_book_end + "-01"
                result = self.db_customer.execute("""
                update t_customer_payment set acc_end=%s,
                    acc_book_end=%s,
                    updated_at=%s,
                    payment_confirm_state=%s,pay_handler_at=%s
                    ,pb_remark=%s,al_remark=%s,wait_pay_amount=%s where id=%s
                """, acc_end, acc_book_end, dt, payment_confirm_state, dt,
                                                  pb_remark, al_remark,
                                                  wait_pay_amount, payment_id)
                self.write(str(result))

        elif tag == "add":
            acc_end = self.get_argument("acc_end", None)
            acc_book_end = self.get_argument("acc_book_end", None)
            # //  con_start =self.get_argument("con_start",None)
            #//  con_end = self.get_argument("con_end",None)
            remark = self.get_argument("remark", "")
            pb_remark = self.get_argument("pb_remark", "")
            al_remark = self.get_argument("al_remark", "")
            customer_id = self.get_argument("customer_id", '')
            project_id = self.get_argument("project_id", 0)
            #   income_id = self.get_argument("income_id",0)
            pay_id = self.get_argument("pay_id", '')
            pay_id1 = self.get_argument("pay_id1", '')
            pay_id2 = self.get_argument("pay_id2",'')
            cp_title_id = self.get_argument("cp_title_id", 0)
            pfi_confirm_state = self.get_argument("pfi_confirm_state", 0)
            pfi_confirm_remark= self.get_argument("pfi_confirm_remark","")
            wait_pay_amount = self.get_argument("wait_pay_amount",0)
            fee=self.get_argument('fee','')
            pay_typeid=self.get_argument('pay_typeid','')
            pay_typeid_name=self.get_argument('pay_typeid_name','')
            service_amount=self.get_argument('service_amount','0')
            service_amount_month=self.get_argument('service_amount_month','0')
            book_amount=self.get_argument('book_amount','0')
            is_review = self.get_argument("is_review","")
            result = 0

            if pay_id1:
                if not acc_end:
                    acc_end = None
                if not acc_book_end:
                    acc_book_end = None

                # print "acc_end", acc_end
                if acc_end:
                    acc_end = acc_end + "-01"
                else:
                    return self.write("-100")
                if acc_book_end:
                    acc_book_end = acc_book_end + "-01"
                    # acc_book_end=' acc_book_end="%s",'%acc_book_end
                update_not_review_sql =""
                if  not is_review:
                    update_not_review_sql = " ,fee=%s,pay_typeid=%s,pay_typeid_name='%s', service_amount=%s,service_month_amount=%s,book_amount=%s "%(
                        fee,pay_typeid,pay_typeid_name,
                                         service_amount,service_amount_month,book_amount,
                    )



                self.db_customer.execute("""
                update t_customer_payment set acc_end=%s,
                  acc_book_end=%s,

               updated_at=%s,pfi_confirm_uid=%s,pfi_confirm_uid_name=%s,
               pfi_confirm_at=%s,pfi_confirm_remark=%s,pfi_confirm_state=%s
               ,pb_remark=%s,al_remark=%s,wait_pay_amount=%s """+update_not_review_sql+""" where id=%s
                """, acc_end, acc_book_end, dt, uid, uid_name, dt,
                                         pfi_confirm_remark, pfi_confirm_state,
                                         pb_remark, al_remark, wait_pay_amount,pay_id1)
            elif pay_id2:
                if not acc_end:
                    acc_end = None
                if not acc_book_end:
                    acc_book_end = None

                if acc_end:
                    acc_end = acc_end + "-01"
                else:
                    return self.write("-100")
                if acc_book_end:
                    acc_book_end = acc_book_end + "-01"
                self.db_customer.execute("""
                update t_customer_payment set acc_end=%s,
               acc_book_end=%s,

               updated_at=%s,uid=%s,uid_name=%s,
               pfi_confirm_remark=%s,pfi_confirm_state=%s
               ,pb_remark=%s,al_remark=%s,wait_pay_amount=%s where id=%s
                """, acc_end, acc_book_end, dt, uid, uid_name,
                                         pfi_confirm_remark, pfi_confirm_state,
                                         pb_remark, al_remark,
                                        wait_pay_amount, pay_id2)


            elif not customer_id and not pay_id:
                self.write("customer_id")


            else:
                t_project = self.db.get(
                    "select * from t_projects where id=%s ", project_id)
                t_customer = self.db_customer.get(
                    "select * from t_customer where id=%s", customer_id)
                if not t_project:
                    return self.write("not project")
                elif not t_customer:
                    return self.write("not customer")
                else:
                    confirm_income = self.db.get(
                        """select sum(service_money) total from t_projects_income_detail
                    a , t_projects_income_title b
                    where a.title_id=b.id and  a.project_id=%s and fi_confirm_uid > 0""",
                        project_id)
                    # print "confirm_income", confirm_income, t_project.all_income
                    if not pb_remark and confirm_income.total != t_project.all_income:
                        return self.write("-1")
                    else:
                        service_amount = t_customer.service_amount
                        pay_typeid = t_customer.paytype_id
                        pay_typeid_name = t_customer.paytype_id_name
                        service_month_amount = t_customer.service_amount_month
                        book_amount = t_customer.book_amount
                        fee = t_customer.fee
                        if not acc_end:
                            acc_end = None
                        if not acc_book_end:
                            acc_book_end = None
                        if pay_id:

                            # print "acc_end", acc_end
                            if acc_end:
                                acc_end = acc_end + "-01"
                            else:
                                return self.write("-100")

                            if acc_book_end:
                                acc_book_end = acc_book_end + "-01"

                            self.db_customer.execute(
                                """
                            update t_customer_payment set pay_typeid=%s,pay_typeid_name=%s,service_month_amount=%s,
                            service_amount=%s,book_amount=%s,acc_end=%s,acc_book_end=%s,updated_at=%s,uid=%s,uid_name=%s,remark=%s,
                            fee=%s,pb_remark=%s,al_remark=%s where id=%s
                            """, pay_typeid, pay_typeid_name,
                                service_month_amount, service_amount,
                                book_amount, acc_end, acc_book_end,dt, uid,
                                uid_name, remark, fee, pb_remark, al_remark,
                                pay_id)
                        else:
                            if not acc_end:
                                acc_end = None
                            if not acc_book_end:
                                acc_book_end = None
                            # print "acc_end", acc_end
                            if acc_end:
                                acc_end = acc_end + "-01"
                            else:
                                return self.write("-100")

                            if acc_book_end:
                                acc_book_end = acc_book_end + "-01"
                            result = self.db_customer.execute(
                                """
                                INSERT INTO `t_customer_payment` ( `customer_id`, `pay_typeid`, `pay_typeid_name`,
                                `service_month_amount`, `service_amount`, `book_amount`, `acc_end`, `acc_book_end`, `created_at`,
                                `updated_at`, `uid`, `uid_name`, `remark`, `fee`, `pb_remark`, `al_remark`, `project_id`, `cp_title_id`,wait_pay_amount,pay_handler_at)
                                VALUES
                                (%s, %s, %s,
                                %s, %s, %s, %s, %s, %s,
                                %s, %s, %s, %s, %s, %s, %s, %s, %s,%s,%s);

                                """, customer_id, pay_typeid, pay_typeid_name,
                                service_month_amount, service_amount,
                                book_amount, acc_end, acc_book_end, dt, dt,
                                uid, uid_name, remark, fee, pb_remark,
                                al_remark, project_id, cp_title_id,
                                wait_pay_amount,dt)
                        if cp_title_id > 0:
                            self.db.execute(
                                "update t_projects_income_title set is_handler=1,is_handler_at=%s,is_handler_uid=%s,is_handler_uid_name=%s where id=%s",
                                dt, uid, uid_name, cp_title_id)
                        self.write(str(result))

        elif tag == "reminders_plan":
            id = self.get_argument('id')
            summary = self.get_argument('summary')
            self.db_customer.execute('''
                update t_customer_exchange set summary=%s,updated_at=%s where id=%s
            ''', summary,dt,id)

        elif tag=="edit_basic_data":
            customer_id=self.get_argument('customer_id')
            promo_id_str=self.get_argument('promo_id','')
            is_general=self.get_argument('is_general',0)
            customer_type=self.get_argument('customer_type','')
            customer_type_name=self.get_argument('customer_type_name','')
            guid=self.get_argument('guid')
            pay_type_id=self.get_argument('pay_type_id','')
            pay_typeid_name=self.get_argument('pay_typeid_name','')
            service_amount=self.get_argument('service_amount','')
            service_amount_month=self.get_argument('service_amount_month','')
            book_amount=self.get_argument('book_amount','')
            fee=self.get_argument('fee','')
            tag_parent_id=self.get_argument('tag_parent_id','')
            tag_parent_name=self.get_argument('tag_parent_name','')
            tag_id=self.get_argument('tag_id','')
            tag_name=self.get_argument('tag_name','')
            is_building=self.get_argument('is_building','0')
            is_clearly=self.get_argument('is_clearly','0')
            is_year=self.get_argument('is_year','0')
            adjusted_option=self.get_argument('adjusted_option','')
            # print service_amount,service_amount_month,book_amount
            promo_id =0,
            promo_id_name =""
            if promo_id_str and promo_id_str!="0":
                promo_id = promo_id_str.split("|")[0]
                promo_id_name = promo_id_str.split("|")[1]
            self.db_customer.execute(
                            """
                        update  `t_customer`
                                set is_general=%s,
                               customer_type=%s,customer_type_name=%s,
                                `updated_at`=%s,
                               promo_id=%s,promo_id_name=%s,
                                service_amount_month=%s,service_amount=%s,book_amount=%s,paytype_id=%s,paytype_id_name=%s,fee=%s
                                ,tag_id=%s,tag_id_name=%s,
                tag_parent_id=%s,tag_parent_id_name=%s,is_building=%s,is_clearly=%s,is_year=%s
                                where id=%s and guid=%s;

                        """,is_general,customer_type,customer_type_name,dt
                        ,promo_id,promo_id_name,service_amount_month,service_amount,book_amount,pay_type_id,pay_typeid_name,fee,
                        tag_id,tag_name,tag_parent_id,tag_parent_name,is_building,is_clearly,is_year,
                        customer_id,guid)
            t_customer_other_data=self.db_customer.get('''
            select * from t_customer_other_data where customer_id=%s
            ''',customer_id)
            if t_customer_other_data:
                self.db_customer.execute('''
                    update t_customer_other_data set adjusted_option=%s where customer_id=%s
                ''',adjusted_option,customer_id)
            else:
                self.db_customer.execute('''
                    insert into t_customer_other_data(adjusted_option,customer_id,update_at)
                    values(%s,%s,%s)
                ''',adjusted_option,customer_id,dt)
            # self.db_customer.execute('''
            #     update t_customer_payment set pay_typeid=%s,pay_typeid_name=%s,
            #     service_month_amount=%s,service_amount=%s,book_amount=%s where customer_id=%s
            # ''',pay_type_id,pay_typeid_name,service_amount_month,service_amount,book_amount,customer_id)
        elif tag == "delete_payment":
            payment_id = self.get_argument("payment_id")
            if payment_id:
                payment = self.db_customer.get("select * from t_customer_payment where id=%s",payment_id)
                if not payment:
                    self.write("找不到相关记录")
                else:
                    if payment.cp_title_id:
                        self.db.execute(
                            "update t_projects_income_title set is_handler=0, is_handler_at=%s,is_handler_uid=0,is_handler_uid_name=NULL where id=%s ",
                            dt,payment.cp_title_id)

                    result = self.db_customer.execute(
                        "delete from t_customer_payment where id=%s", payment_id)
                    self.write(str(result))

        elif tag=="ask_assist":
            customer_id=self.get_argument('customer_id','')
            assist_msg=self.get_argument('assist_msg','')
            step=self.get_argument('step','')
            sale_name=self.get_argument('sale_name','')
            sale_id=self.get_argument('sale_id','')
            assist_id=self.get_argument('assist_id','')
            summary=self.get_argument('summary','')
            status=self.get_argument('status','')
            is_check=self.get_argument('is_check','')
            check_remark=self.get_argument('check_remark','')
            customer_ids=self.get_argument('customer_ids','')
            assist_ids_and_sales=self.get_argument('assist_ids_and_sales','')
            if step=='1':
                self.db_customer.execute('''
                    update t_customer_payment_assist set sale_name=%s,sale_id=%s,assist_msg=%s,
                    distribute_at=%s,distribute_name=%s,distribute_id=%s
                    where id=%s
                    ''',sale_name,sale_id,assist_msg,dt,uid_name,uid,assist_id)
                t_remind=self.db.get('''
                    select * from t_remind where uid=%s
                ''',sale_id)
                if t_remind:
                    self.db.execute('''
                        update t_remind set xiezhu_num=xiezhu_num+1 where id=%s
                    ''',t_remind.id)
                else:
                    self.db.execute('''
                    insert into t_remind(uid,uid_name,xiezhu_num)
                    values(%s,%s,xiezhu_num+1)
                ''',sale_id,sale_name)
            elif step=='2':
                self.db_customer.execute('''
                    update t_customer_payment_assist set jd_at=%s
                    where id=%s
                    ''',dt,assist_id)
            elif step=='3':
                if status=='3':
                    self.db_customer.execute('''
                    update t_customer_payment_assist set is_bad_debts=1,bad_debts_fq_at=%s
                    where id=%s
                    ''',dt,assist_id)
                else:
                    self.db_customer.execute('''
                        update t_customer_payment_assist set summary=%s,status=%s,sale_end_at=%s,is_check=0
                        where id=%s
                        ''',summary,status,dt,assist_id)
                    self.db_customer.execute('''
                    update t_customer_exchange set isvisible=1 where customer_id=%s and uid=%s
                    ''',customer_id,uid)
                    self.db_customer.execute('''
                    insert into t_customer_exchange set msg=%s,customer_id=%s,uid=%s,uid_name=%s,etype=2,created_at=%s
                    ''',summary,customer_id,uid,uid_name,dt)
            elif step=='4':
                t_customer=self.db_customer.get('''
                    select acc_uid_name,acc_uid from t_customer where id=%s
                ''',customer_id)
                if t_customer:
                    self.db_customer.execute('''
                    insert into t_customer_payment_assist(acc_uid,acc_uid_name,customer_id,created_at,sale_name,sale_id,assist_msg,distribute_at,is_manage)
                    values(%s,%s,%s,%s,%s,%s,%s,%s,1)
                ''',t_customer.acc_uid,t_customer.acc_uid_name,customer_id,dt,sale_name,sale_id,assist_msg,dt)
                    self.db_customer.execute('''
                        insert into  t_customer_exchange(msg_time,msg,customer_id,created_at,uid,uid_name,etype)
                        values(%s,%s,%s,%s,%s,%s,%s)''',dt,'分配销售为'+sale_name,customer_id,dt, uid,
                                            uid_name,'2')
                    
                    t_remind=self.db.get('''
                        select * from t_remind where uid=%s
                    ''',sale_id)
                    if t_remind:
                        self.db.execute('''
                            update t_remind set xiezhu_num=xiezhu_num+1 where id=%s
                        ''',t_remind.id)
                    else:
                        self.db.execute('''
                        insert into t_remind(uid,uid_name,xiezhu_num)
                        values(%s,%s,xiezhu_num+1)
                    ''',sale_id,sale_name)

            elif step=='5':
                self.db_customer.execute('''
                    update t_customer_payment_assist set is_check=%s,check_remark=%s,check_at=%s, check_name=%s,check_id=%s
                    where id=%s
                    ''',is_check,check_remark,dt,uid_name,uid,assist_id)
            elif step=='6':

                if assist_ids_and_sales:
                    t_remind1=self.db.get('''
                                select * from t_remind where uid=%s
                            ''',sale_id)
                    for item in assist_ids_and_sales.split(','):
                        t_remind=self.db.get('''
                                select * from t_remind where uid=%s
                            ''',item.split('|')[1])
                        t_customer_payment_assist=self.db_customer.get('''
                            select  customer_id from t_customer_payment_assist where id=%s
                        ''',item.split('|')[0])
                        self.db_customer.execute('''
                        insert into  t_customer_exchange(msg_time,msg,customer_id,created_at,uid,uid_name,etype)
                        values(%s,%s,%s,%s,%s,%s,%s)''',dt,'分配销售为'+sale_name, t_customer_payment_assist.customer_id,dt, uid,
                                            uid_name,'2')
                        self.db_customer.execute('''
                        update t_customer_payment_assist set sale_name=%s,sale_id=%s,distribute_at=%s,summary=null,
                        status=0,sale_end_at=null,is_check=0,check_remark=null,check_at=null,check_name=null,
                        check_id=null,is_manage=1,jd_at=null where id=%s
                        ''',sale_name,sale_id,dt,item.split('|')[0])
                        if t_remind:
                            self.db.execute('''
                                    update t_remind set xiezhu_num=xiezhu_num-1 where id=%s
                                ''',t_remind.id)
                        if t_remind1:
                            self.db.execute('''
                                    update t_remind set xiezhu_num=xiezhu_num+1 where id=%s
                                ''',t_remind1.id)


                else:
                    for customer_id in customer_ids.split(','):
                        t_customer=self.db_customer.get('''
                        select acc_uid_name,acc_uid from t_customer where id=%s
                    ''',customer_id)

                        if t_customer:
                            self.db_customer.execute('''
                            insert into t_customer_payment_assist(acc_uid,acc_uid_name,customer_id,created_at,sale_name,sale_id,assist_msg,distribute_at,is_manage)
                            values(%s,%s,%s,%s,%s,%s,%s,%s,1)
                        ''',t_customer.acc_uid,t_customer.acc_uid_name,customer_id,dt,sale_name,sale_id,assist_msg,dt)
                            self.db_customer.execute('''
                                insert into  t_customer_exchange(msg_time,msg,customer_id,created_at,uid,uid_name,etype)
                                values(%s,%s,%s,%s,%s,%s,%s)''',dt,'分配销售'+sale_name,customer_id,dt, uid,
                                                    uid_name,'2')
                            t_remind=self.db.get('''
                                select * from t_remind where uid=%s
                            ''',sale_id)
                            if t_remind:
                                self.db.execute('''
                                    update t_remind set xiezhu_num=xiezhu_num+1 where id=%s
                                ''',t_remind.id)
                            else:
                                self.db.execute('''
                                insert into t_remind(uid,uid_name,xiezhu_num)
                                values(%s,%s,xiezhu_num+1)
                            ''',sale_id,sale_name)
            else:
                self.db_customer.execute('''
                insert into t_customer_payment_assist(customer_id,assist_msg,acc_uid,acc_uid_name,created_at)
                values(%s,%s,%s,%s,%s)
            ''',customer_id,assist_msg,uid,uid_name,dt)

        elif tag=="assist_linkman":
            customer_id=self.get_argument('customer_id')
            linkman=self.db_customer.query('''
            select name,tel,remark,acc_uid_name,date_format(created_at,'%%Y-%%m-%%d') df  from t_linkman where customer_id=%s order by id desc
            ''',customer_id)

            self.write({'linkman':linkman})
        elif tag=="edit_customer_remark":
            customer_id=self.get_argument('customer_id')
            t_remark=self.get_argument('t_remark','')
            self.db_customer.execute('''
            update t_customer set remark=%s where id=%s
            ''',t_remark,customer_id)
        # elif tag=="update_acc_end":
        #     acc_end=self.get_argument('acc_end')
        #     customer_id=self.get_argument('customer_id')
        #     self.db_customer.execute('''
        #         update t_customer_payment set acc_end=%s where customer_id=%s
        #     ''',acc_end,customer_id)

        elif tag=="bad_debts_milepost":
            check_status=self.get_argument('check_status','')
            step=self.get_argument('step','')
            assist_id=self.get_argument('assist_id')
            kj_option=self.get_argument('kj_option','')
            customer_id=self.get_argument('customer_id','')
            kj_reject=self.get_argument('kj_reject','')
            if step=='1':
                self.db_customer.execute('''
                update  t_customer_payment_assist set  bad_debts_sale_checked_name=%s,bad_debts_sale_checked_uid=%s,
                bad_debts_sale_checked_at=%s,bad_debts_sale_checked_status=%s where  id=%s
            ''',uid_name,uid,dt,check_status,assist_id)
            elif step=='2':
                sql=''
                if kj_reject:
                    sql+=',bad_debts_sale_checked_status=0,bad_debts_sale_checked_at=NULL,bad_debts_kj_reject="%s",bad_debts_kj_reject_reason="%s",bad_debts_kj_reject_at="%s" '%(kj_reject,kj_option,dt)
                else:
                    sql+=''' ,bad_debts_kj_at="%s",bad_debts_kj_option='%s' '''%(dt,kj_option)
                self.db_customer.execute('''
                update  t_customer_payment_assist set  bad_debts_kj_name="%s",
                bad_debts_kj_uid=%s '''+sql+''' where  id=%s
            ''',uid_name,uid,assist_id)


            elif step=='3':
                t_type=self.db_customer.get('''
                select * from t_type where tag='客户类型' and name='坏账' and is_show=1
                ''')
                result=self.db_customer.execute('''
                update  t_customer_payment_assist set  bad_debts_caiwu_checked_name=%s,bad_debts_caiwu_checked_id=%s,
                bad_debts_caiwu_checked_at=%s,bad_debts_caiwu_checked_status=%s where  id=%s
            ''',uid_name,uid,dt,check_status,assist_id)
                if result==0 and check_status=='1' and customer_id:
                    self.db_customer.execute('''
                        update  t_customer set customer_type=concat(customer_type,if(right(customer_type,1)=',',%s,%s)),
                        customer_type_name=concat(customer_type_name,if(right(customer_type_name,1)=',',%s,%s)) where id=%s
                    ''',t_type.id,','+str(t_type.id),t_type.name,','+t_type.name,customer_id)

        elif tag=="add_business":
            assist_id=self.get_argument('assist_id','')
            customer_id=self.get_argument('customer_id','')
            guid=uuid.uuid4()
            t_customer=self.db_customer.get('''
            select a.id assist_id,b.company from  
             t_customer_payment_assist a
            inner join t_customer b on a.customer_id=b.id
            where a.id=%s
            ''',assist_id)
            t_linkman = self.db_customer.query(
            "select * from t_linkman where customer_id=%s order by is_first desc,id ",
            customer_id)
            link_name=''
            link_phone=''
            if t_linkman:
                link_name=t_linkman[0].name
                link_phone=t_linkman[0].tel
            result=self.db.execute('''
                    insert into business_develop_manage(business_from_id,business_from_name,
                    feedback_type_id,feedback_type_name,customer_name,company,phone,project_request
                    ,guid,created_at,uid,uid_name,first_link_name,first_link_phone,assist_id,remark) 
                    values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,'')
                ''','295','反馈商机','1','内部客户办理原公司业务',link_name,t_customer.company,link_phone,'214_坏账开发注销_特殊业务',
                guid,dt,uid,uid_name,link_name,link_phone,assist_id)
            if result>0:
                self.db.execute("""
                                insert into business_develop_manage_msg(uid,uid_name,message,created_at,business_id,tag_type,btype_id)
                                values(%s,%s,%s,%s,%s,%s,%s)
                                """, uid, uid_name,uid_name+'创建商机', dt,result, "操作记录",'2')
                if t_linkman:
                    for link_man in t_linkman:
                        self.db.execute('''
                            insert into business_develop_manage_linkman
                            (link_gender,link_name,link_tel,business_id,uid,uid_name,created_at,is_first,link_remark)
                            values(1,%s,%s,%s,%s,%s,%s,%s,'')
                        ''',link_man.name,link_man.tel,result,uid,uid_name,dt,link_man.is_first)
               
                self.db.execute('''
                    insert into business_develop_manage_milepost(business_id) values(%s)
                ''',result)
                self.db_customer.execute('''
                    update t_customer_payment_assist set add_business=1 where id=%s
                ''',assist_id)