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

class PaymentHandler(BaseHandler):
    @tornado.web.authenticated
    def get(self):
        tag = self.get_argument("tag", "list")
        uid = self.get_secure_cookie("uid")
        uid_name = self.get_secure_cookie("name")
        curr = self.get_argument("curr","confirm")
        req_state = int(self.get_argument("req_state","0"))
        if tag=="customer":
            customer_id = int(self.get_argument("customer_id"))
            to_tag = self.get_argument("to_tag","")
            sql = ""
            if not customer_id:
                return self.write("customer_id is null")
            customer = self.db_customer.get(
                "select * from t_customer where id=%s", customer_id)
            if not customer:
                return self.write("errer customer %s",customer_id)
            if customer_id:
                sql=" and  a.id='%s' "%(customer_id)
            page = int(self.get_argument("page", 1))
            pre_page = 200
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
                         SELECT *,c.updated_at pay_updated_at,c.uid_name pay_uid_name,
            c.pay_typeid_name pay_pay_typeid_name,
            c.service_amount pay_service_amount,c.service_month_amount
            pay_service_amount_month, c.book_amount pay_book_amount
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
                order by pay_updated_at desc
            """)
            self.render(
                'c/payment/customer.html',
                customers=customers,
                customer=customer,
                pagination=pagination,
                to_tag=to_tag,
                tag=tag)
        elif tag=="project_customer_list":
            sql = ""
            page = int(self.get_argument("page", 1))
            pre_page = 20
            req_state_sql=""
            if req_state:
                req_state_sql = " in "
            else:
                req_state_sql =" not in "
            count = self.db_customer.get('''
        select count(*) count
                FROM  t_customer
                where id '''+req_state_sql+''' (
                select customer_id from  t_customer_payment where  customer_type_name like '%%记账%%'
 group by customer_id
                )  and  customer_type_name like '%%记账%%'

               ''')
            pagination = Pagination(page, pre_page, count.count, self.request)
            startpage = (page - 1) * pre_page
            customers = self.db_customer.query("""
            SELECT  *            FROM  t_customer
                where id """+req_state_sql+""" (
                select customer_id from  t_customer_payment where  customer_type_name like '%%记账%%'
 group by customer_id
                )  and  customer_type_name like '%%记账%%'

                order by created_at desc
 limit %s,%s
            """, startpage, pre_page)
            t_payment_type = self.db_customer.query("select * from t_type where tag='付费方式'")
            self.render(
                'c/payment/project_customer_list.html',
                t_payment_type=t_payment_type,
                customers=customers,
                pagination=pagination,
                req_state=req_state,
                tag=tag,curr=curr)
        elif tag=="project_payment_list":
            sql = ""
            page = int(self.get_argument("page", 1))
            pre_page = 20
            req_state_sql=""
            if req_state:
                req_state_sql = " and c.id  in( select income_id from t_customer_payment where income_id > 0 )"
            else:
                req_state_sql ="and c.id not in( select income_id from t_customer_payment where income_id > 0)"
            count = self.db_customer.get('''
        select count(*) count
        from t_customer a inner join db_income2.t_projects b on a.company=b.customer_company
        inner join db_income2.t_projects_income_title c  on  c.project_id=a.id and income_uid  > 0
        left join t_customer_payment_req d on d.income_id= c.id
where customer_type_name like '%%记账%%'
               '''+req_state_sql)

            pagination = Pagination(page, pre_page, count.count, self.request)
            startpage = (page - 1) * pre_page
            print "req_state_sql",req_state_sql
            customers = self.db_customer.query(
                """
                   select  *, c.uid_name add_by,c.id income_title_id,b.id project_id,b.guid project_guid,a.id a_customer_id,
                   a.paytype_id customer_pay_type_id,service_amount customer_service_amount,
                   service_month_amount customer_service_amount_month,
                   book_amount customer_book_amount,
                   a.fee customer_fee,
                   a.guid a_customer_guid from t_customer a inner join db_income2.t_projects b on a.company=b.customer_company
inner join db_income2.t_projects_income_title c  on  c.project_id=a.id and income_uid  > 0
where customer_type_name like '%%记账%%'

""" + req_state_sql + """

                                                    limit %s,%s
            """, startpage, pre_page)
            t_payment_type = self.db_customer.query("select * from t_type where tag='付费方式'")

            self.render(
                'c/payment/project_payment_list.html',
                t_payment_type=t_payment_type,
                customers=customers,
                pagination=pagination,
                req_state=req_state,
                tag=tag,curr=curr)


        elif tag=="list":
            sql = ""
            page = int(self.get_argument("page", 1))
            pre_page = 20
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
            SELECT  *,c.updated_at pay_updated_at,c.uid_name pay_uid_name,

            c.pay_typeid_name pay_pay_typeid_name,c.service_amount pay_service_amount,c.service_month_amount pay_service_amount_month, c.book_amount pay_book_amount
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


                order by pay_updated_at desc

                  limit %s,%s
            """, startpage, pre_page)
            t_payment_type = self.db_customer.query("select * from t_type where tag='付费方式'")

            self.render(
                'c/payment/payment_list.html',
                customers=customers,
                pagination=pagination,
                t_payment_type=t_payment_type,
                tag=tag)


    def post(self):
        tag = self.get_argument("tag")
        uid_name = self.get_secure_cookie("name")
        role = self.get_secure_cookie("role")
        uid = self.get_secure_cookie("uid")
        if tag=="add":
            service_amount = self.get_argument("service_amount","0")
            fee = self.get_argument("fee","0")
            pay_typeid = self.get_argument("pay_typeid","0")
            pay_typeid_name = self.get_argument("pay_typeid_name","")
            service_month_amount =self.get_argument("service_month_amount","0")
            book_amount =self.get_argument("book_amount","0")
            acc_end =self.get_argument("acc_end",None)
            acc_book_end =self.get_argument("acc_book_end",None)
            con_start =self.get_argument("con_start",None)
            con_end = self.get_argument("con_end",None)
            remark =self.get_argument("remark","")
            pb_remark= self.get_argument("pb_remark","")
            al_remark = self.get_argument("al_remark","")
            customer_id = self.get_argument("customer_id")
            project_id = self.get_argument("project_id",0)
            income_id = self.get_argument("income_id",0)
            if not customer_id:
                self.write("customer_id")
            else:
                if not acc_end:
                    acc_end= None
                if not acc_book_end:
                    acc_book_end = None
                if not con_start:
                    con_start = None
                if not con_end:
                    con_end = None
                result = self.db_customer.execute("""
                    INSERT INTO `t_customer_payment` ( `customer_id`, `pay_typeid`, `pay_typeid_name`,
                    `service_month_amount`, `service_amount`, `book_amount`, `acc_end`, `acc_book_end`, `created_at`,
                     `updated_at`, `uid`, `uid_name`, `remark`, `fee`, `pb_remark`, `al_remark`, `project_id`, `income_id`)
                    VALUES
                     (%s, %s, %s,
                     %s, %s, %s, %s, %s, now(),
                      now(), %s, %s, %s, %s, %s, %s, %s, %s);

                    """,customer_id,pay_typeid,pay_typeid_name,
                    service_month_amount,service_amount,book_amount,acc_end,acc_book_end,uid,uid_name,remark,fee,pb_remark,al_remark,
                    project_id,income_id
                    )
                self.write(str(result))
