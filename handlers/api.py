# -*- coding: utf-8 -*-
from handlers.base import BaseHandler
import logging
import tornado
import tornado.httpclient
import os
import random
import string
import re
import hashlib
logger = logging.getLogger('boilerplate.' + __name__)


class cAPiHandler(BaseHandler):
    def get(self):
        tag = self.get_argument("tag")
        if tag == "project":
            id = self.get_argument("id")
            project = self.db.get("select * from t_projects where id=%s",id)

            jproject = None
            code = 0
            if project:
                jproject = {
                    "id": project.id,
                    "customer_name": project.customer_name,
                    "project_name": project.project_name,
                    "customer_company": project.customer_company,
                    "all_income": str(project.all_income),
                    "craeted_at": str(project.created_at),
                    "income_name": "谢妙欣",
                    "sale_name": project.uid_name,
                    "kf_name":"甘雪莲",
                    "income_type":"支付宝"
                }
                code = 1


            self.write(
                tornado.escape.json_encode({
                    "code": code,
                    "customer": jproject
                }))


class ApiHandler(BaseHandler):
    @tornado.web.authenticated
    def post(self):
        tag = self.get_argument("tag","user")
        query= self.get_argument("query",'')
        if tag =="user":

            response = []
            if query:
                t_users = self.db.query("select * from t_user where name like  '%%"+query+"%%' ")

                for item in t_users:
                    response.append(item.name)

            self.write(tornado.escape.json_encode(response))
        elif tag == "userandid":
            response = []
            if query:
                t_users = self.db.query(
                    "select * from t_user where name like  '%%" + query + "%%' ")

                for item in t_users:
                    response.append(item.name+","+str(item.id))
            self.write(tornado.escape.json_encode(response))

        elif tag=="addr":
            response = []
            if query:
                t_users = self.db.query(u"select * from t_projects_type where income_category='地址类型' and  income_name like  '%%"+query+"%%' ")

                for item in t_users:
                    response.append(item.income_name)
            self.write(tornado.escape.json_encode(response))

        elif tag=='company':
            response = []
            if query:
                query = query.replace("（","(").replace("）",")") 
            if len(query)>0:
                t_users = self.db.query("select * from t_projects where customer_company like  '%%"+query+"%%' limit 20")
                for item in t_users:
                    response.append(item.customer_company)
            self.write(tornado.escape.json_encode(response))
        elif tag=='customer_company':
            if query:
                query = query.replace("（","(").replace("）",")") 
            response = []
            if len(query)>0:
                t_users = self.db_customer.query("select * from t_customer where company like  '%%"+query+"%%' limit 20 ")
                for item in t_users:
                    response.append(item.company)
            self.write(tornado.escape.json_encode(response))
        elif tag=='customer_company_guid':
            if query:
                query = query.upper()
            response = []
            if len(query)>0:
                t_users = self.db_customer.query("select * from t_customer where company like  '%%"+query+"%%' limit 20 ")
                for item in t_users:
                    response.append(item.company+"-"+item.company_reguid)
            self.write(tornado.escape.json_encode(response))
        elif tag=='customer_company_one':
            if len(query)>0:
                if query:
                    query = query.replace("（","(").replace("）",")") 
                t_customer = self.db_customer.get("select company_reguid from t_customer where company = %s  ",query)
                if t_customer:
                    self.write(t_customer.company_reguid)
                else:
                    self.write("")

        elif tag == 'customer_company_acc_uid':

            uid =self.get_secure_cookie("uid")
            response = []
            if len(query) > 0:
                t_users = self.db_customer.query(
                    "select * from t_customer where acc_uid =%s and company like  '%%"
                    + query + "%%' limit 20 ", uid)
                for item in t_users:
                    response.append(item.company)
            print response,"lllll"
            self.write(tornado.escape.json_encode(response))

        elif tag=="department":
            department=self.get_argument('department')
            responsible_pers=self.db.query('''
                select responsible_per  from t_todo_arrange a
                inner join t_user b on a.responsible_per=b.name and department_name=%s group by department_name
            ''',department)
            self.write({'responsible_pers':responsible_pers})




class OApiHandler(BaseHandler):
    # @tornado.web.authenticated
    # def post(self):
    #     tag = self.get_argument("tag", "user")
    #     query = self.get_argument("query")
    #     if tag == "user":
    #         response = []
    #         if query:
    #             t_users = self.db.query(
    #                 "select * from t_user where name like  '%%" + query +
    #                 "%%' ")

    #             for item in t_users:
    #                 response.append(item.name)
    #         self.write(tornado.escape.json_encode(response))

    def get(self):


        tag = self.get_argument("tag")
        if tag =="auth":
            f_email = self.get_argument("username", None)
            f_password = self.get_argument("password", None)

            error = None
            role = 0
            uid= 0
            is_manager = 0
            if not f_email:
                error = "登录帐户不能为空."
            # elif not self.validate(f_email):
            # 	error="您的帐户格式不正确."
            elif not f_password:
                error = "登录密码不能为空."

            elif self.authenticate(f_email, f_password):
                t_user = self.get_user_info(f_email)
                if t_user:
                    uid = t_user.id
                    is_manager= t_user.is_manager
                    t_role = self.db.get("select * from t_user_group where id=%s",
                                        t_user.role)
                    if not t_role:
                        error = "还没有分配用户组"
                    else:
                        error=""
                        role = t_role.name
                else:
                    error = "登录帐户已经过期,请与我们联系."
            else:
                error = "登录帐户信息不正确,请效验后再重试."

            response = {
                "error": error,
                "username": f_email,
                "role": role,
                "uid": uid,
                "is_manager": is_manager
            }
            self.write(tornado.escape.json_encode(response))

    def get_user_info(self, name):
        t_user = self.db.get('''
				SELECT * FROM t_user
				WHERE name=%s
			''', name)
        return t_user

    def validate(self, f_email):
        regex = re.compile(r'^[\w\.=-]+@[\w\.-]+\.[\w]{2,3}$')
        return regex.match(f_email)

    def authenticate(self, username, password):
        logger.info(username, password)
        hashPassword = self.db.get(
            'SELECT pass user_pass FROM t_user WHERE name = %s', username)
        if hashPassword:
            return hashlib.md5(password).hexdigest() == hashPassword.user_pass
