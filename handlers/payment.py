# encoding=utf8
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


class PaymentHandler(BaseHandler):
    def compare_date(self, dt1, dt2):
        print dt1.strftime("%Y-%m"), dt2.strftime("%Y-%m")
        if dt1.date() <= dt2:
            return True
        else:
            return False

    @tornado.web.authenticated
    def get(self):
        tag = self.get_argument("tag", "list")
        uid = self.get_secure_cookie("uid")
        uid_name = self.get_secure_cookie("name")
        curr = self.get_argument("curr", "confirm")
        req_state = int(self.get_argument("req_state", "0"))
        page = int(self.get_argument("page", 1))
        pre_page = 20
        if tag == "get_last_payment":
            customer_id = self.get_argument("customer_id", "")
            payment_id = int(self.get_argument("payment_id", 0))
            customer = None
            psql = ""
            if not customer_id:
                return self.write("not customer_id")
            else:
                if payment_id:
                    psql = " and a.id < " + str(payment_id)

                t_customer = self.db_customer.get(
                    """select a.*,b.paytype_id_name customer_paytype_id_name,a.id payment_id,
                    b.service_amount customer_service_amount ,
                    b.service_amount_month customer_service_amount_month,
                    b.book_amount customer_book_amount,
                    b.fee
                    from 
                    t_customer_payment a ,t_customer b  where a.customer_id=b.id and 
                    customer_id=%s """ + psql +
                    """   order by created_at desc limit 1""", customer_id)
                if not t_customer:
                    code = 0
                else:
                    code = 1
                    acc_end = None
                    acc_book_end = None
                    next_pay_acc_end_book = None
                    next_pay_acc_end_book_start = None
                    if t_customer.acc_book_end:
                        print "hi", t_customer.acc_book_end
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
                    print "t_customer.acc_end", t_customer.acc_end, " t_customer.acc_book_end", t_customer.acc_book_end
                    if t_customer.acc_end:
                        next_pay_acc_end_start = t_customer.acc_end - relativedelta(
                            months=-1)
                        next_pay_acc_end = t_customer.acc_end - relativedelta(
                            months=-t_customer.fee)
                        next_pay_acc_end_start = next_pay_acc_end_start.strftime(
                            "%Y-%m")
                        next_pay_acc_end = next_pay_acc_end.strftime("%Y-%m")
                        acc_end = t_customer.acc_end.strftime("%Y-%m")

                    t_customer = {
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
                        t_customer.payment_id
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
                        a.guid,a.company,c.updated_at pay_updated_at,c.uid_name pay_uid_name,
                        c.pay_typeid_name pay_pay_typeid_name,c.service_amount pay_service_amount,
                                                                c.service_month_amount pay_service_amount_month, c.book_amount pay_book_amount
                                                                FROM  t_customer a
                                                                    INNER JOIN t_customer_payment c
                                                                        ON a.id = c.customer_id
                                                                  
            

                """ + sql + """
                order by pay_updated_at desc
            """)

            t_payment_type = self.db_customer.query(
                "select * from t_type where tag='付费方式'")
            t_customer_exchange = self.db_customer.query(
                """select * from t_customer_exchange where customer_id=%s and etype=2 order by created_at desc""",
                customer_id)
            self.render(
                'c/payment/customer.html',
                t_customer_exchange=t_customer_exchange,
                customers=customers,
                t_payment_type=t_payment_type,
                customer=customer,
                pagination=pagination,
                to_tag=to_tag,
                tag=tag,
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
            print "req_state_sql", req_state_sql
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
            page = int(self.get_argument("page", 1))
            company = self.get_argument('company', '')
            pre_page = 20
            if company:
                sql = ' where a.company like "%%' + company + '%%" '
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
               ''' + sql)
            pagination = Pagination(page, pre_page, count.count, self.request)
            startpage = (page - 1) * pre_page
            customers = self.db_customer.query("""
                    SELECT  *,c.updated_at pay_updated_at,c.uid_name pay_uid_name,c.wait_pay_amount,
                    c.pay_typeid_name pay_pay_typeid_name,c.service_amount pay_service_amount,c.service_month_amount pay_service_amount_month, c.book_amount pay_book_amount,
                    a.acc_uid_name 
                    FROM  t_customer a
                        INNER JOIN t_customer_payment c
                            ON a.id = c.customer_id
                        INNER JOIN
                        (
                            SELECT `customer_id`, MAX(id) max_id
                            FROM t_customer_payment
                            GROUP BY customer_id
                        ) b ON c.customer_id = b.customer_id AND
                                b.max_id = c.id """ + sql + """
                        order by req_at desc
                        limit %s,%s
            """, startpage, pre_page)
            t_payment_type = self.db_customer.query(
                "select * from t_type where tag='付费方式'")

            self.render(
                'c/payment/payment_list.html',
                customers=customers,
                pagination=pagination,
                t_payment_type=t_payment_type,
                tag=tag)

        elif tag == "list_company":
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
                sql1 = ' and c.customer_company like "%%' + company + '%%" '
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
                select  d.service_id,service_name,customer_company,service_money,project_name,d.created_at,
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
                    and c.reg_state =1
                    and a.project_id=d.project_id
                    and  service_id=10
                    and project_income_id=e.id """ + sql1 + """

                    
              order by d.created_at desc
                        limit %s,%s
            """, startpage, pre_page)
            t_payment_type = self.db_customer.query(
                "select * from t_type where tag='付费方式'")

            self.render(
                'c/payment/list_company.html',
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

            page = int(self.get_argument("page", 1))
            pre_page = 20
            company = self.get_argument('company', '')
            if pay_project_id == 0:
                hand_sql = " and  is_handler=0 "
                sql_reg = "and reg_state <> 1"
            else:
                hand_sql = " and  is_handler=1 "
            if company:
                sql += ' and a.company like "%%' + company + '%%" '
            if state:
                pay_sql = "        inner join " + options.mysql_database_customer + ".`t_customer_payment` g on a.id=g.customer_id  and cp_title_id > 0 and payment_confirm_state=1"

            count = self.db.get(
                """
                select 
                count(*) count
                          
               from  """ + options.mysql_database_customer + """.`t_customer` a 
                  inner join """ + options.mysql_database_customer +
                """.`t_customer_payment` g on a.id=g.customer_id
                    inner join t_projects b on a.company = b.customer_company   """
                + sql_reg + """
          
                    inner join t_projects_income_title e  on e.project_id=b.id and fi_confirm_uid > 0  and cp_title_id > 0 """
                + hand_sql + """
                          inner join t_projects_income c  on c.project_id=b.id and c.parent_id=e.id
                    inner join (select title_id, GROUP_CONCAT(concat( service_name,"|",service_money)) pay_list from t_projects_income_detail d where
                    (d.`service_id`=10 or d.service_id=204 or d.service_id=131)
                    group by title_id) d on e.id=d.title_id and b.id=e.project_id
            """ + sql)

            pagination = Pagination(page, pre_page, count.count, self.request)
            startpage = (page - 1) * pre_page
            customers = self.db.query("""
                    select 
a.acc_uid_name,income_list,
                    pay_list,e.is_handler_uid_name is_handler_uid_name,is_handler_at,
                    customer_company,b.project_name,income_num,b.id project_id,e.id cp_title_id,e.created_at title_created_at,
                    a.id a_customer_id,a.paytype_id customer_pay_type_id, a.service_amount customer_service_amount,a.service_amount_month customer_service_amount_month,


                    a.book_amount customer_book_amount,a.guid a_customer_guid, a.paytype_id_name customer_paytype_id_name
                    

                    from  """ + options.mysql_database_customer +
                                      """.`t_customer` a 
                    """ + pay_sql + """
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
                    inner join (select title_id, GROUP_CONCAT(concat( service_name,"|",service_money)) pay_list from t_projects_income_detail d where
                    (d.`service_id`=10 or d.service_id=204 or d.service_id=131)
                    group by title_id) d on e.id=d.title_id and b.id=e.project_id
            """ + sql + """


                    order by is_handler_at desc
                        limit %s,%s
            """, startpage, pre_page)
            print """ select 
a.acc_uid_name,
                    pay_list,e.uid title_uid_name,
                    customer_company,b.project_name,income_num,b.id project_id,e.id cp_title_id,e.created_at title_created_at,
                    a.id a_customer_id,a.paytype_id customer_pay_type_id, a.service_amount customer_service_amount,a.service_amount_month customer_service_amount_month,


                    a.book_amount customer_book_amount,a.guid a_customer_guid, a.paytype_id_name customer_paytype_id_name,
                    g.acc_end,g.acc_book_end,g.id payment_id,g.al_remark,g.pb_remark,g.payment_confirm_remark

                    from  """ + options.mysql_database_customer + """.`t_customer` a 
                  left join """ + options.mysql_database_customer + """.`t_customer_payment` g on a.id=g.customer_id  
                    inner join t_projects b on a.company = b.customer_company   """ + sql_reg + """
                    inner join t_projects_income c  on c.project_id=b.id
                    inner join t_projects_income_title e  on e.project_id=b.id and fi_confirm_uid > 0  """ + hand_sql + """
                    inner join (select title_id, GROUP_CONCAT(concat( service_name,"|",service_money)) pay_list from t_projects_income_detail d where
                    (d.`service_id`=10 or d.service_id=204 or d.service_id=131)
                    group by title_id) d on e.id=d.title_id and b.id=e.project_id
            """ + sql
            t_payment_type = self.db_customer.query(
                "select * from t_type where tag='付费方式'")

            self.render(
                'c/payment/list_company_in_customer.html',
                customers=customers,
                company=company,
                pagination=pagination,
                t_payment_type=t_payment_type,
                pay_project_id=pay_project_id,
                state=state,
                tag=tag)

        elif tag == "list_company_in_customer_req":
            pay_project_id = int(self.get_argument("pay_project_id", 0))
            sql = ""
            sql_reg = ""
            sql_hand = ""
            page = int(self.get_argument("page", 1))
            pre_page = 20
            company = self.get_argument('company', '')
            state = int(self.get_argument("state", 0))

            if company:
                sql += ' and a.company like "%%' + company + '%%" '

            sql += " and payment_confirm_state=" + str(state)
            sql_hand = " and  is_handler=1"

            print sql
            count = self.db.get(
                """
                select 
                count(*) count
                        from  """ + options.mysql_database_customer +
                """.`t_customer` a 
                    inner join """ + options.mysql_database_customer +
                """.`t_customer_payment` g on a.id=g.customer_id
                    inner join t_projects b on a.company = b.customer_company   """
                + sql_reg +
                """inner join t_projects_income c  on c.project_id=b.id
                    inner join t_projects_income_title e  on e.project_id=b.id and fi_confirm_uid > 0
                    """ + sql_hand + """
                    inner join (select title_id, GROUP_CONCAT(concat( service_name,"|",service_money)) pay_list from t_projects_income_detail d where
   (d.`service_id`=10 or d.service_id=204 or d.service_id=131 ) 
  group by title_id) d 
                    on e.id=d.title_id


                         """ + sql + """

               """)
            pagination = Pagination(page, pre_page, count.count, self.request)
            startpage = (page - 1) * pre_page

            print    """
                  select 
                  
                  a.id c_customer_id,
                  a.acc_uid_name,payment_confirm_state,income_list,
                    pay_list,e.uid_name title_uid_name,is_handler_uid_name,payment_confirm_uid_name,is_handler_uid_name,
                    is_handler_at,

                    customer_company,b.project_name,income_num,b.id project_id,e.id income_title_id,
                    e.created_at title_created_at,
                    a.id a_customer_id,a.paytype_id customer_pay_type_id, a.service_amount customer_service_amount,
                    a.service_amount_month customer_service_amount_month,
                    a.book_amount customer_book_amount,a.guid a_customer_guid, a.paytype_id_name customer_paytype_id_name,
                    g.acc_end,g.acc_book_end,g.id payment_id,g.al_remark,g.pb_remark,g.payment_confirm_remark
                    from  """ + options.mysql_database_customer + """.`t_customer` a 
                    inner join """ + options.mysql_database_customer + """.`t_customer_payment` g on a.id=g.customer_id and g.cp_title_id > 0
                    inner join t_projects b on a.company = b.customer_company   """ + sql_reg + """ 
                    inner join t_projects_income_title e  on e.project_id=b.id and fi_confirm_uid > 0  """ + sql_hand + """

                       INNER join        (select parent_id,income_num,
                      GROUP_CONCAT(concat( income_name,"|",income_money)) 
                      income_list from t_projects_income dd 
                     
                     group by parent_id,income_num
                      
                     ) c on c.parent_id=e.id
          
                    inner join (select title_id, GROUP_CONCAT(concat( service_name,"|",service_money)) pay_list from t_projects_income_detail d where
   (d.`service_id`=10 or d.service_id=204 or d.service_id=131 ) 
  group by title_id) d 
                    on e.id=d.title_id


                         """ + sql + """

                    order by title_created_at desc


                        limit %s,%s
            """


            customers = self.db.query(
                """
                  select 
                  
                  a.id c_customer_id,
                  a.acc_uid_name,payment_confirm_state,income_list,
                    pay_list,e.uid_name title_uid_name,is_handler_uid_name,payment_confirm_uid_name,is_handler_uid_name,
                    is_handler_at,

                    customer_company,b.project_name,income_num,b.id project_id,e.id income_title_id,
                    e.created_at title_created_at,
                    a.id a_customer_id,a.paytype_id customer_pay_type_id, a.service_amount customer_service_amount,
                    a.service_amount_month customer_service_amount_month,
                    a.book_amount customer_book_amount,a.guid a_customer_guid, a.paytype_id_name customer_paytype_id_name,
                    g.acc_end,g.acc_book_end,g.id payment_id,g.al_remark,g.pb_remark,g.payment_confirm_remark
                    from  """ + options.mysql_database_customer +
                """.`t_customer` a 
                    inner join """ + options.mysql_database_customer +
                """.`t_customer_payment` g on a.id=g.customer_id and g.cp_title_id > 0
                    inner join t_projects b on a.company = b.customer_company   """
                + sql_reg + """ 
                    inner join t_projects_income_title e  on e.project_id=b.id and fi_confirm_uid > 0  """
                + sql_hand + """

                       INNER join        (select parent_id,income_num,
                      GROUP_CONCAT(concat( income_name,"|",income_money)) 
                      income_list from t_projects_income dd 
                     
                     group by parent_id,income_num
                      
                     ) c on c.parent_id=e.id
          
                    inner join (select title_id, GROUP_CONCAT(concat( service_name,"|",service_money)) pay_list from t_projects_income_detail d where
   (d.`service_id`=10 or d.service_id=204 or d.service_id=131 ) 
  group by title_id) d 
                    on e.id=d.title_id


                         """ + sql + """

                    order by title_created_at desc


                        limit %s,%s
            """, startpage, pre_page)

            t_payment_type = self.db_customer.query(
                "select * from t_type where tag='付费方式'")

            self.render(
                'c/payment/list_company_in_customer_req.html',
                customers=customers,
                pagination=pagination,
                t_payment_type=t_payment_type,
                pay_project_id=pay_project_id,
                state=state,
                company=company,
                tag=tag)
        elif tag == "expire_customer":
            print "hello"

            sql = ""
            page = int(self.get_argument("page", 1))
            date = self.get_argument("date", "2")
            pre_page = 20
            company = self.get_argument('company', '')
            show_tag = self.get_argument("show_tag", "1")
            show_sql = ""
            if show_tag == "2":
                show_sql = " and req_uid  > 0"
            else:
                show_sql = " and req_uid  =0"

            dt_next = datetime.date.today() - relativedelta(months=0)

            sql = """
                    where 
                             
                  ( YEAR(c.acc_end) = YEAR(now()) and MONTH(c.acc_end) <= MONTH(now())
and 

 YEAR(c.acc_book_end) = YEAR(now()) and MONTH(c.acc_book_end) <= MONTH(now())
    
                   )
                   
                 """ + show_sql

            if company:
                sql += ' and a.company like "%%' + company + '%%"'

            print """ SELECT  DATE_ADD(c.acc_end, INTERVAL 1 MONTH) next_pay_acc_start , a.acc_uid_name,cp_title_id,
                        DATE_ADD(c.acc_end, INTERVAL a.fee MONTH) next_pay_acc_end, 
                        DATE_ADD(c.acc_book_end, INTERVAL 1 MONTH) next_pay_acc_book_start , 
                        DATE_ADD(c.acc_book_end, INTERVAL a.fee MONTH) next_pay_acc_book_end, c.*,
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

                                          """ + sql
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

                                          
                             
               ''' + sql)
            pagination = Pagination(page, pre_page, count.count, self.request)
            startpage = (page - 1) * pre_page



            customers = self.db_customer.query("""
                       SELECT  DATE_ADD(c.acc_end, INTERVAL 1 MONTH) next_pay_acc_start , a.acc_uid_name,cp_title_id,
                        DATE_ADD(c.acc_end, INTERVAL a.fee MONTH) next_pay_acc_end, 
                        DATE_ADD(c.acc_book_end, INTERVAL 1 MONTH) next_pay_acc_book_start , 
                        DATE_ADD(c.acc_book_end, INTERVAL a.fee MONTH) next_pay_acc_book_end, c.*,
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

                                          """ + sql + """ 
                             order by c.acc_end desc
                        limit %s,%s
            """, startpage, pre_page)


            t_payment_type = self.db_customer.query(
                "select * from t_type where tag='付费方式'")

            self.render(
                'c/payment/expire_customer.html',
                date=date,
                dt_next=dt_next,
                customers=customers,
                pagination=pagination,
                t_payment_type=t_payment_type,
                show_tag=show_tag,
                compare_date=self.compare_date,
                company=company,
                tag=tag)

        elif tag == "acc_customer_payment":
            sql = ""
            page = int(self.get_argument("page", 1))
            show_tag = self.get_argument("show_tag", "1")
            pre_page = 20

            company = self.get_argument('company', '')

            dt_next = datetime.date.today() - relativedelta(months=-1)
            if show_tag == "1":
                sql = """
                    where acc_uid=%s       
                """
            elif show_tag == "2":
                sql = """
                      where  acc_uid=%s   and (pb_remark <> '' )  and  req_close=0
                """
            elif show_tag == "3":
                sql = """
                    where  acc_uid=%s   and (pb_remark ='' or pb_remark is null or req_close=1)
                """

            if company:
                sql += ' and a.company like "%%' + company + '%%"'

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
 
                                       
                             
               ''' + sql, uid)

            pagination = Pagination(page, pre_page, count.count, self.request)
            startpage = (page - 1) * pre_page
            customers = self.db_customer.query("""
                       SELECT  DATE_ADD(c.acc_end, INTERVAL 1 MONTH) next_pay_acc_start , acc_uid_name,
                        DATE_ADD(c.acc_end, INTERVAL a.fee MONTH) next_pay_acc_end, 
                        DATE_ADD(c.acc_book_end, INTERVAL 1 MONTH) next_pay_acc_book_start , 
                        DATE_ADD(c.acc_book_end, INTERVAL a.fee MONTH) next_pay_acc_book_end, c.*,
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
 """ + sql + """
                order by req_at desc             
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
                tag=tag)

        elif tag == "reminders_plan":
            show_tag = self.get_argument('show_tag', '1')
            page = int(self.get_argument('page', 1))
            pre_page = 20
            sql = ''
            if show_tag == '2':
                sql = ' and summary is null '
            if show_tag == '3':
                sql = ' and summary is not null'
            count = self.db_customer.get(
                """select count(*) count from t_customer_exchange where uid=%s and etype=2 and  msg_time is not null  """
                + sql, uid)
            pagination = Pagination(page, pre_page, count.count, self.request)
            startpage = (page - 1) * pre_page
            t_customer_exchange = self.db_customer.query(
                """select * from t_customer_exchange where uid=%s and etype=2 and  msg_time is not null """
                + sql + """
                order by TO_DAYS(msg_time)=TO_DAYS(now()) desc, msg_time
                limit %s,%s""", uid, startpage, pre_page)
            self.render(
                'c/payment/reminders_plan.html',
                t_customer_exchange=t_customer_exchange,
                tag=tag,
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
                    update t_customer_payment set payment_confirm_remark=%s , payment_confirm_state=%s ,

                    payment_confirm_uid=%s , payment_confirm_uid_name=%s,payment_confirm_at=%s
                    where id=%s and customer_id=%s 
                """, payment_confirm_remark, payment_confirm_state, uid,
                                                  uid_name, dt, payment_id,
                                                  customer_id)
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
            cp_title_id = self.get_argument("cp_title_id", 0)
            result = 0
            dt = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            if not customer_id and not pay_id:
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
                    print "confirm_income", confirm_income, t_project.all_income
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
                            print "acc_end", acc_end
                            if acc_end:
                                acc_end = acc_end + "-01"
                            else:
                                return self.write("记账到期时间要填写哦.")

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
                            print "acc_end", acc_end
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
                                `updated_at`, `uid`, `uid_name`, `remark`, `fee`, `pb_remark`, `al_remark`, `project_id`, `cp_title_id`)
                                VALUES
                                (%s, %s, %s,
                                %s, %s, %s, %s, %s, %s,
                                %s, %s, %s, %s, %s, %s, %s, %s, %s);

                                """, customer_id, pay_typeid, pay_typeid_name,
                                service_month_amount, service_amount,
                                book_amount, acc_end, acc_book_end, dt, dt,
                                uid, uid_name, remark, fee, pb_remark,
                                al_remark, project_id, cp_title_id)
                        if cp_title_id > 0:
                            self.db.execute(
                                "update t_projects_income_title set is_handler=1,is_handler_at=%s,is_handler_uid=%s,is_handler_uid_name=%s where id=%s",
                                dt, uid, uid_name, cp_title_id)
                        self.write(str(result))

        elif tag == "reminders_plan":
            id = self.get_argument('id')
            summary = self.get_argument('summary')
            self.db_customer.execute('''
                update t_customer_exchange set summary=%s where id=%s
            ''', summary, id)
