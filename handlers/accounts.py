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
from Pagination import Pagination
logger = logging.getLogger('boilerplate.' + __name__)


class LogoutHandler(BaseHandler):
    @tornado.web.authenticated
    def get(self):
        self.clear_all_cookies()
        self.redirect('/login')

# class ApiHandler(BaseHandler):
#     @tornado.web.authenticated
#     def get(self):
#         response = []
#         for i in range(4):
#             response.append(term + str(random.random())[2:])
#         self.write(tornado.escape.json_encode(response))

class LoginHandler(BaseHandler):
    def get(self):
        ok = self.get_argument("ok",None)
        mobile= self.get_argument("mobile","")
        error=None
        log_in_again=None
        if ok:
            log_in_again='修改成功，请重新登录'
        tmp_html = "login.html"

        if mobile:
            tmp_html = "mobile/accounts/mobile_login.html"


        self.render(tmp_html,error=error,log_in_again=log_in_again)

    def post(self):
        f_email = self.get_argument("username",None)
        f_password = self.get_argument("password",None)
        mobile = self.get_argument("mobile", "")
        tmp_html = "login.html"

        if mobile:
            tmp_html = "mobile/accounts/mobile_login.html"
        error=None
        log_in_again=None

        if not f_email:
            error="帐户不能为空."
        # elif not self.validate(f_email):
        # 	error="您的帐户格式不正确."
        elif not f_password:
            error="密码不能为空."

        elif self.authenticate(f_email,f_password):
            t_user = self.get_user_info(f_email)
            if t_user:
                self.set_secure_cookie("uid",str(t_user.id), expires_days=30)
                self.set_secure_cookie("name",str(t_user.name.encode("utf8")), expires_days=30)
                self.set_secure_cookie("role",str(t_user.role),expires_days=30)
                self.set_secure_cookie('is_check',str(t_user.is_check),expires_days=30)
                self.set_secure_cookie(
                    'is_manager', str(t_user.is_manager), expires_days=30)
                self.set_secure_cookie('is_bj_manage',str(t_user.is_bj_manage),expires_days=30)
                self.set_secure_cookie('is_gy_manage',str(t_user.is_gy_manage),expires_days=30)
                self.set_secure_cookie('department_name',str(t_user.department_name),expires_days=30)
                self.set_secure_cookie('is_xz_manage',str(t_user.is_xz_manage),expires_days=30)
                self.set_secure_cookie('kj_manage', str(t_user.kj_manage), expires_days=30)
                self.set_secure_cookie('all_manage', str(t_user.all_manage), expires_days=30)
                self.set_secure_cookie(
                    'is_developer', str(t_user.is_developer), expires_days=30)
                self.set_secure_cookie('sh_manage', str(t_user.sh_manage), expires_days=30)
                self.set_secure_cookie('kf_manage', str(t_user.kf_manage), expires_days=30)
                self.set_secure_cookie('express_manage', str(t_user.express_manage), expires_days=30)
                self.set_secure_cookie('role_list',str(t_user.role_list) or '',expires_days=30)


                t_role = self.db.get("select * from t_user_group where id=%s",t_user.role)
                if t_user.is_first==1:
                    self.redirect('/allchangepassword?is_first=1')

                if not t_role:
                    self.write("还没有分配用户组")
                else:
                    if mobile=="1":
                        self.redirect("/mobile?tag=home")
                    else:
                        self.redirect(
                            self.get_argument('next', t_role.to_url), permanent=True)
            else:
                error="登录帐户已经过期,请与我们联系."
        else:
            error="登录帐户信息不正确,请效验后再重试."

        self.render(tmp_html, error=error, log_in_again=log_in_again)

    def get_user_info(self,name):

        t_user = self.db.get('''
				SELECT * FROM t_user WHERE name=%s limit 1
			''',name)
        return t_user
    def validate(self, f_email):
        regex = re.compile(r'^[\w\.=-]+@[\w\.-]+\.[\w]{2,3}$')
        return regex.match(f_email)

    def authenticate(self,username,password):
        # logger.info( username,password)
        user=self.db.get('SELECT * FROM t_user WHERE name = %s', username)
        # print(user)
        hashPassword = self.db.get('SELECT pass user_pass FROM t_user WHERE name = %s', username)
        if hashPassword:
            return hashlib.md5(password).hexdigest() == hashPassword.user_pass

class AdminChangePasswordHandler(BaseHandler):
    @tornado.web.authenticated
    def get(self,id):
        error=None
        change_user=self.db.get('select * from t_user where id=%s',int(id))
        cur_id=self.get_secure_cookie('uid')
        is_admin_user=self.db.get('select is_admin from t_user where id=%s',int(cur_id))
        if is_admin_user['is_admin']==1:
            self.render('accounts/admin_change_pass.html',
                        change_user=change_user,
                        error=error,
                        search_key='',
                        t_income_type='',
                        t_company='',
                        t_building='',
                        t_users_kf='',
                        t_business_channel='',
                        t_sign_type='',
                        t_talk_type='',
                        t_rec_contarct_type=''
            )
    @tornado.web.authenticated
    def post(self,id):
        new_password=self.get_argument('newpassword')
        change_user=self.db.get('select * from t_user where id=%s',int(id))
        cur_id=self.get_secure_cookie('uid')
        is_admin_user=self.db.get('select is_admin from t_user where id=%s',int(cur_id))
        if is_admin_user['is_admin']==1:
            if new_password!='':
                hash_password=hashlib.md5(new_password).hexdigest()
                self.db.execute('update t_user set pass=%s where id=%s',hash_password,int(id))
                self.render('accounts/admin_change_pass.html',
                            change_user=change_user,
                            error='修改密码成功',
                            search_key='',
                            t_income_type='',
                            t_company='',
                            t_building='',
                            t_users_kf='',
                            t_business_channel='',
                            t_sign_type='',
                            t_talk_type='',
                            t_rec_contarct_type=''
                )
            else:
                self.render('accounts/admin_change_pass.html',
                           change_user=change_user,
                           error='密码不能为空',
                           search_key='',
                           t_income_type='',
                           t_company='',
                           t_building='',
                           t_users_kf='',
                           t_business_channel='',
                           t_sign_type='',
                           t_talk_type='',
                           t_rec_contarct_type=''
                )

class ChangePasswordHandler(BaseHandler):
    @tornado.web.authenticated
    def get(self):
        is_first=self.get_argument('is_first',None)
        error=None
        if is_first:
            error='修改密码-管理员要求'
        change_success=None
        cur_id=self.get_secure_cookie('uid')
        is_admin_user=self.db.get('select is_admin from t_user where id=%s',int(cur_id))
        self.render('accounts/change_pass.html',
        error=error,
        change_success=change_success,
        search_key='',
        t_income_type='',
        t_company='',
        t_building='',
        t_users_kf='',
        t_business_channel='',
        t_sign_type='',
        t_talk_type='',
        t_rec_contarct_type='')

    def post(self):
        error=None
        f_password = self.get_argument("currentpassword")
        new_password=self.get_argument('newpassword')
        id=self.get_secure_cookie('uid')
        if self.authenticate(id,f_password):
            hashPassword=hashlib.md5(new_password).hexdigest()
            self.db.execute("""
                update  t_user  set pass=%s,is_first=%s where id=%s
                """,hashPassword,0,int(id))
            self.clear_all_cookies()
            self.redirect('/login?ok=1',permanent=True)


        else:
            self.render('accounts/change_pass.html',
                error='密码错误',
                change_success='',
                search_key='',
                t_income_type='',
                t_company='',
                t_building='',
                t_users_kf='',
                t_business_channel='',
                t_sign_type='',
                t_talk_type='',
                t_rec_contarct_type='')


    def authenticate(self,id,password):
        hashPassword = self.db.get('SELECT pass user_pass FROM t_user WHERE id = %s', int(id))
        if hashPassword:
            return hashlib.md5(password).hexdigest() == hashPassword.user_pass

class AllChangePasswordHandler(BaseHandler):
    @tornado.web.authenticated
    def get(self):
        is_first=self.get_argument('is_first',None)
        error=None
        if is_first:
            error='修改密码-管理员要求'
        change_success=None
        admin=False
        cur_id=self.get_secure_cookie('uid')
        is_admin_user=self.db.get('select is_admin from t_user where id=%s',int(cur_id))
        if is_admin_user['is_admin']==1:
            admin=True
        self.render('accounts/all_change_pass.html',
        error=error,
        change_success=change_success,
        search_key='',
        t_income_type='',
        t_company='',
        t_building='',
        t_users_kf='',
        t_business_channel='',
        t_sign_type='',
        t_talk_type='',
        t_rec_contarct_type='',
        admin=admin)

    def post(self):
        error=None
        cur_id=self.get_secure_cookie('uid')
        is_admin_user=self.db.get('select is_admin,is_first from t_user where id=%s',int(cur_id))
        if is_admin_user['is_admin']==1 and is_admin_user['is_first']==0:
            f_username=self.get_argument('admin_change_user')
            new_password=self.get_argument('admin_new_password')
            hashPassword=hashlib.md5(new_password).hexdigest()
            user= self.db.get('SELECT * FROM t_user WHERE name=%s',f_username)
            if f_username:
                if user:
                    if new_password:
                        self.db.execute("""
                        update  t_user  set pass=%s where id=%s
                        """,hashPassword,user.id)
                        error=error
                        change_success='修改成功'
                        admin=True
                    else:
                        error='密码不能为空'
                        change_success=''
                        admin=True

                else:
                    error='用户名不存在'
                    change_success=''
                    admin=True
            else:
                error='请输入用户名'
                change_success=''
                admin=True
        elif is_admin_user['is_admin']==0 or (is_admin_user['is_admin']==1 and is_admin_user['is_first']==1):
            f_password = self.get_argument("currentpassword")
            new_password=self.get_argument('newpassword')
            id=self.get_secure_cookie('uid')
            if f_password==new_password:
                error='与当前密码不能一致哦.'
                change_success=''
                admin=False
            else:
                if self.authenticate(id,f_password):
                    hashPassword=hashlib.md5(new_password).hexdigest()
                    self.db.execute("""
                        update  t_user  set pass=%s,is_first=%s where id=%s
                        """,hashPassword,0,int(id))
                    self.clear_all_cookies()
                    self.redirect('/login?ok=1',permanent=True)


                else:
                    error='当前密码错误哦,如果找不到密码,联系管理员.'
                    change_success=''
                    admin=False

        self.render('accounts/all_change_pass.html',
                error=error,
                change_success=change_success,
                search_key='',
                t_income_type='',
                t_company='',
                t_building='',
                t_users_kf='',
                t_business_channel='',
                t_sign_type='',
                t_talk_type='',
                t_rec_contarct_type='',
                admin=admin)
    def authenticate(self,id,password):
        hashPassword = self.db.get('SELECT pass user_pass FROM t_user WHERE id = %s', int(id))
        if hashPassword:
            return hashlib.md5(password).hexdigest() == hashPassword.user_pass


class ManageUserHandler(BaseHandler):
    @tornado.web.authenticated
    def get(self):
        page = int(self.get_argument("page", 1))
        pre_page = 20
        startpage = (page - 1) * pre_page
        id=self.get_secure_cookie('uid')
        is_admin_user=self.db.get('select is_admin from t_user where id=%s',int(id))
        all_users =self.db.query('SELECT * FROM t_user order by reg_time desc limit %s,%s',startpage,pre_page)
        count = self.db.get(
                '''SELECT count(*) count FROM t_user 
                ''')
        pagination = Pagination(page, pre_page, count.count, self.request)
        startpage = (page - 1) * pre_page
        self.render('accounts/manageuser.html',
        search_key='',
        t_income_type='',
        t_company='',
        t_building='',
        t_users_kf='',
        t_business_channel='',
        t_sign_type='',
        t_talk_type='',
        t_rec_contarct_type='',
        pagination=pagination,
        all_users=all_users,
        is_admin_user=str(is_admin_user['is_admin'])
        )

class LockUserhandler(BaseHandler):
    @tornado.web.authenticated
    def get(self,id):
        cur_id=self.get_secure_cookie('uid')
        is_admin_user=self.db.get('select is_admin from t_user where id=%s',int(cur_id))
        if is_admin_user['is_admin']==1:
            self.db.execute("""
            update  t_user  set is_lock=%s where id=%s
        """,int(1),int(id))

class UnlockUserHandler(BaseHandler):
    @tornado.web.authenticated
    def get(self,id):
        cur_id=self.get_secure_cookie('uid')
        is_admin_user=self.db.get('select is_admin from t_user where id=%s',int(cur_id))
        if is_admin_user['is_admin']==1:
            self.db.execute("""
            update  t_user  set is_lock=%s where id=%s
        """,int(0),int(id))

class InsertUserHandler(BaseHandler):
    @tornado.web.authenticated
    def get(self):
        error=None
        self.render('accounts/insertuser.html',
        error=error,
        search_key='',
        t_income_type='',
        t_company='',
        t_building='',
        t_users_kf='',
        t_business_channel='',
        t_sign_type='',
        t_talk_type='',
        t_rec_contarct_type='')
    @tornado.web.authenticated
    def post(self):
        cur_id=self.get_secure_cookie('uid')
        is_admin_user=self.db.get('select is_admin from t_user where id=%s',int(cur_id))
        if is_admin_user['is_admin']==1:
            name=self.get_argument('name')
            exist_user=self.db.get('select * from t_user where name=%s',name)
            if exist_user:
                self.render('accounts/insertuser.html',
                            error='用户已存在',
                            search_key='',
                            t_income_type='',
                            t_company='',
                            t_building='',
                            t_users_kf='',
                            t_business_channel='',
                            t_sign_type='',
                            t_talk_type='',
                            t_rec_contarct_type='')
            password=self.get_argument('password')
            hashPassword=hashlib.md5(password).hexdigest()
            f_email=self.get_argument('email')
            phone=self.get_argument('phone')
            is_lock=self.get_argument('is_lock')
            role=self.get_argument('role')
            remark=self.get_argument('remark')
            is_admin=self.get_argument('is_admin') or 0
            qc=self.get_argument('qc')
            self.db.execute('''
                insert into t_user(name,pass,email,phone,is_lock,role,reg_time,
                remark,is_admin,qc) values(%s,%s,%s,%s,%s,%s,UTC_TIMESTAMP(),%s,%s,%s)
                ''',name,hashPassword,f_email,phone,int(is_lock),int(role),remark,int(is_admin),int(qc))

        self.redirect('/manageuser')

class ChangeUserHandler(BaseHandler):
    @tornado.web.authenticated
    def get(self,id):
        error=None
        f_user=self.db.get('select * from t_user where id=%s',int(id))
        self.render('accounts/changeuser.html',
        error=error,
        search_key='',
        t_income_type='',
        t_company='',
        t_building='',
        t_users_kf='',
        t_business_channel='',
        t_sign_type='',
        t_talk_type='',
        t_rec_contarct_type='',
        user=f_user)

    @tornado.web.authenticated
    def post(self,id):
        cur_id=self.get_secure_cookie('uid')
        change_user=self.db.get('select name from t_user where id=%s',int(id))
        is_admin_user=self.db.get('select is_admin from t_user where id=%s',int(cur_id))
        if is_admin_user['is_admin']==1:
            name=self.get_argument('name')
            if change_user['name']!=name:
                change_user=self.db.get('select * from t_user where name=%s',name)
                if change_user:
                    self.render('accounts/changeuser.html',
                           error='用户名已存在',
                           search_key='',
                           t_income_type='',
                           t_company='',
                           t_building='',
                           t_users_kf='',
                           t_business_channel='',
                           t_sign_type='',
                           t_talk_type='',
                           t_rec_contarct_type='',
                           user=change_user)
                else:
                    f_email=self.get_argument('email')
                    phone=self.get_argument('phone')
                    is_lock=self.get_argument('is_lock')
                    role=self.get_argument('role')
                    remark=self.get_argument('remark')
                    is_admin=self.get_argument('is_admin') or 0
                    qc=self.get_argument('qc')
                    is_first=self.get_argument('is_first')
                    self.db.execute('''
                        update  t_user set name=%s,email=%s,phone=%s,is_lock=%s,role=%s,
                        remark=%s,is_admin=%s,qc=%s,is_first=%s where id=%s
                        ''',name,f_email,phone,int(is_lock),int(role),remark,int(is_admin),int(qc),int(is_first),int(id))
            else:
                f_email=self.get_argument('email')
                phone=self.get_argument('phone')
                is_lock=self.get_argument('is_lock')
                role=self.get_argument('role')
                remark=self.get_argument('remark')
                is_admin=self.get_argument('is_admin') or 0
                qc=self.get_argument('qc')
                is_first=self.get_argument('is_first')
                self.db.execute('''
                    update  t_user set name=%s,email=%s,phone=%s,is_lock=%s,role=%s,
                    remark=%s,is_admin=%s,qc=%s,is_first=%s where id=%s
                    ''',name,f_email,phone,int(is_lock),int(role),remark,int(is_admin),int(qc),int(is_first),int(id))
        self.redirect('/manageuser')

class DemoHandler(BaseHandler):
    def get(self):
        self.render("demo/demo.html")


class uploadHandler(tornado.web.RequestHandler):
    def post(self):
        file = self.request.files["files"][0]
        callback = self.get_argument("CKEditorFuncNum")
        file_type= "photo"
        extension = os.path.splitext(file.filename)[1]

        if file_type is 'photo':
            type_list = ['.png','.jpg','.jpeg','.gif']
        elif file_type is 'attachment':
            type_list = ['.pdf','.doc','.docx','.xls']
        msg = "0"
        file_name_full=""
        if extension in type_list:
            file_name = ''.join(random.choice(string.ascii_lowercase + string.digits) for x in range(16))
            file_name_full =  file_name + extension
            output_file = open("media/public/" + file_name_full, 'wb')
            output_file.write(file.body)
            msg = "1"
        # self.write (file.filename + " has been uploaded."+msg)
        # self.write('<script>parent.ckeditorUpload("/static/public/'+file_name_full+'");</script>')
        output = "<script type=\"text/javascript\">parent.ckeditorUpload(\"/static/public/"+file_name_full+"\");"
        output =output+"window.parent.CKEDITOR.tools.callFunction(" + callback + ",'/static/public/" +file_name_full+ "','')"
        self.write(output+'</script>')


class FooHandler(BaseHandler):
    def get(self):
        self.render("base.html")

class DemoHandler(BaseHandler):
    def get(self):
        self.render("demo/demo.html")
