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
import uuid
from captcha.image import ImageCaptcha
import datetime
logger = logging.getLogger('boilerplate.' + __name__)
dt = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")


class LogoutHandler(BaseHandler):
    @tornado.web.authenticated
    def get(self):
        mobile = self.get_argument("mobile","")
        self.clear_all_cookies()
        if mobile:
            self.redirect("/login?mobile=1")
        else:
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
        error_forbid=self.get_argument('error_forbid','')
        show_verification=False
        error=None
        log_in_again=None
        ver_str=''
        if ok:
            log_in_again='修改成功，请重新登录'
        tmp_html = "login.html"

        if mobile:
            tmp_html = "mobile/accounts/mobile_login.html"

        if( not re.match('localhost:\d{4}',self.request.host) and not re.match('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}:\d{4}',self.request.host) ):
            show_verification=True
            _letter_cases = "abcdefghjkmnpqrstuvwxy"                        # 小写字母
            _upper_cases = "ABCDEFGHJKLMNPQRSTUVWXY"                        # 大写字母
            _numbers = "1234567890"    
            ver_str=''.join((_letter_cases,_upper_cases,_numbers))
            ver_str=random.sample(ver_str,4)
            img=ImageCaptcha()
            image=img.generate_image(ver_str)
            image.save('media/verify.jpg')
        self.render(
            tmp_html,error=error,error_forbid=error_forbid,
            log_in_again=log_in_again
            ,mobile=mobile,show_verification=show_verification,
            ver_str=hash(''.join(ver_str).lower()))

    def post(self):
        f_email = self.get_argument("username",None)
        f_password = self.get_argument("password",None)
        mobile = self.get_argument("mobile", "")
        ver_str1=self.get_argument('ver_str1','')
        input_ver_str=self.get_argument('input_ver_str','')
        show_verification=self.get_argument('show_verification','')
        _letter_cases = "abcdefghjkmnpqrstuvwxy"                        # 小写字母
        _upper_cases = "ABCDEFGHJKLMNPQRSTUVWXY"                        # 大写字母
        _numbers = "1234567890"    
        ver_str=''.join((_letter_cases,_upper_cases,_numbers))
        ver_str=random.sample(ver_str,4)
        img=ImageCaptcha()
        image=img.generate_image(ver_str)
        image.save('media/verify.jpg')
        tmp_html = "login.html"
        
        if mobile:
            tmp_html = "mobile/accounts/mobile_login.html"
        error=None
        error_forbid=None
        log_in_again=None

        if not f_email:
            error="帐户不能为空."
        # elif not self.validate(f_email):
        # 	error="您的帐户格式不正确."
        elif not f_password:
            error="密码不能为空."
        elif show_verification and str(hash(input_ver_str.lower()))!=str(ver_str1):
 
            error='验证码输入错误'

        elif self.authenticate(f_email,f_password):
            t_user = self.get_user_info(f_email)
            if t_user:
                if t_user.is_lock==1:
                    self.write("抱歉,该用户被锁定,有疑问请管理员联系!")

                else:
                    if( not re.match('localhost:\d{4}',self.request.host) and not re.match('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}:\d{4}',self.request.host) ):
             
                        if t_user.forbid_outer_net==0:
                            self.set_secure_cookie("uid",str(t_user.id), expires_days=1)
                        else:
                            tmp_html = "login.html"
                            if mobile:
                                tmp_html = "mobile/accounts/mobile_login.html"
                        
                            return  self.render(tmp_html,error_forbid='已被禁止外网访问',error='',log_in_again='',mobile=mobile,
                            show_verification=show_verification,ver_str=hash(''.join(ver_str).lower()))                        
                    else:
                        self.set_secure_cookie("uid",str(t_user.id), expires_days=1)
                    self.set_secure_cookie("name",str(t_user.name.encode("utf8")), expires_days=1)
                    self.set_secure_cookie("role",str(t_user.role),expires_days=1)
                    self.set_secure_cookie('is_check',str(t_user.is_check),expires_days=1)
                    self.set_secure_cookie('is_manager', str(t_user.is_manager), expires_days=1)
                    self.set_secure_cookie('is_bj_manage',str(t_user.is_bj_manage),expires_days=1)
                    self.set_secure_cookie('is_gy_manage',str(t_user.is_gy_manage),expires_days=1)
                    self.set_secure_cookie('department_name',str(t_user.department_name),expires_days=1)
                    self.set_secure_cookie('is_xz_manage',str(t_user.is_xz_manage),expires_days=1)
                    self.set_secure_cookie('kj_manage', str(t_user.kj_manage), expires_days=1)
                    self.set_secure_cookie('all_manage', str(t_user.all_manage), expires_days=1)
                    self.set_secure_cookie(
                        'is_developer', str(t_user.is_developer), expires_days=1)
                    self.set_secure_cookie('sh_manage', str(t_user.sh_manage), expires_days=1)
                    self.set_secure_cookie('kf_manage', str(t_user.kf_manage), expires_days=1)
                    self.set_secure_cookie('express_manage', str(t_user.express_manage), expires_days=1)
                    self.set_secure_cookie('role_list',str(t_user.role_list) or '',expires_days=1)
                    x_real_ip = self.request.headers.get("X-Real-IP")
                    ip = x_real_ip or self.request.remote_ip
                    self.db.execute('''
                    insert into t_login_log values(default,%s,%s,%s,%s,%s)
                    ''',ip,self.request.host,t_user.name,t_user.id,dt)
                    exists= self.db.get("""
                    select uid_name,role from t_statis_kf where uid_name=%s limit 1
                    """,t_user.name)
                    if exists:
                        self.set_secure_cookie('show_statis_kf','1',expires_days=1)

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

        self.render(tmp_html, error=error,error_forbid=error_forbid, log_in_again=log_in_again,mobile=mobile,
         show_verification=show_verification,ver_str=hash(''.join(ver_str).lower())
         
        )

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

class GetNewverify(BaseHandler):
    def get(self):
 
        _letter_cases = "abcdefghjkmnpqrstuvwxy"                        
        _upper_cases = "ABCDEFGHJKLMNPQRSTUVWXY"                        
        _numbers = "1234567890"    
        ver_str=''.join((_letter_cases,_upper_cases,_numbers))
        ver_str=random.sample(ver_str,4)
        img=ImageCaptcha()
        image=img.generate_image(ver_str)

        image.save('media/verify.jpg')
        self.write({'ver_str1':str(hash(''.join(ver_str).lower())),'img_src':'/static/verify.jpg'})
class AdminChangePasswordHandler(BaseHandler):
    @tornado.web.authenticated
    def get(self,id):
        error=None
        role=self.get_secure_cookie('role')
        change_user=self.db.get('select * from t_user where id=%s',int(id))
        cur_id=self.get_secure_cookie('uid')
        if self.get_secure_cookie('role_list'):
            role_list=self.get_secure_cookie('role_list').split(',')
        else:
            role_list=[]
        is_admin_user=self.db.get('select is_admin from t_user where id=%s',int(cur_id))
        if is_admin_user['is_admin']==1 or '277' in role_list:
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
        role=self.get_secure_cookie('role')
        change_user=self.db.get('select * from t_user where id=%s',int(id))
        cur_id=self.get_secure_cookie('uid')
        if self.get_secure_cookie('role_list'):
            role_list=self.get_secure_cookie('role_list').split(',')
        else:
            role_list=[]
        is_admin_user=self.db.get('select is_admin from t_user where id=%s',int(cur_id))
        if is_admin_user['is_admin']==1 or '277' in role_list:
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
                error='与原始密码不能一致哦.'
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
        tag=self.get_argument('tag','manageuser')

        if tag=='manageuser' or tag=='kj_manage' or tag=='login_log':
            page = int(self.get_argument("page", 1))
            user_name=self.get_argument('user_name','')
            phone=self.get_argument('phone','')
            forbid_outer_net=self.get_argument('forbid_outer_net','')
            login_name=self.get_argument('login_name','')
            login_at_start=self.get_argument("login_at_start",'')
            login_at_end=self.get_argument('login_at_end','')
            statistics=self.get_argument('statistics','')
            sql=''
            pre_page = 20
            params={
                'user_name':user_name,
                'phone':phone,
                'forbid_outer_net':forbid_outer_net,
                'login_name':login_name,
                'login_at_start':login_at_start,
                'login_at_end':login_at_end,
                'statistics':statistics
            }
            id=self.get_secure_cookie('uid')
            is_admin_user=self.db.get('select is_admin from t_user where id=%s',int(id))
            department_names=self.db.query(' select department_name,department_id from t_user_relation group by department_name,department_id ')
            #用户查询
            if user_name:
                sql+=' and a.name="%s" '%user_name
            if phone:
                sql+=' and a.phone=%s '%phone
            if forbid_outer_net:
                sql+=' and a.forbid_outer_net=%s '%forbid_outer_net
            #登录查询
            if login_name:
                sql+=' and uid_name="%s" '%login_name
            if login_at_start and login_at_end:
                sql+=' and created_at between "%s" and "%s" '%(login_at_start,login_at_end)
            elif tag=='login_log':
                sql+=' and TIMESTAMPDIFF(MONTH,created_at,CURDATE())=0 '
           
            if tag=='kj_manage':
                count=self.db.get(' select count(*) count from t_user_relation')
                pagination = Pagination(page, pre_page, count.count, self.request)
                startpage = (page - 1) * pre_page
                all_users=self.db.query(' select * from t_user_relation order by id desc limit %s,%s ',startpage,pre_page)
            elif tag=='login_log':
                if sql:
                    sql=' where '+sql[4:]

                if statistics:
                    count=self.db.get('''
                    select count(*) count from(
                    select df from(
                    SELECT date_format(created_at,'%%Y-%%m-%%d') df,uid_name,count(*) count 
                     FROM t_login_log '''+sql+''' group by uid_name,df order by df desc)a 
                      group by df)b  
                    ''')
                    pagination = Pagination(page, pre_page, count.count, self.request)
                    startpage = (page - 1) * pre_page
                    all_users=self.db.query('''
                    select df, group_concat(uid_name,'|',count order by count desc)gc,sum(count) sc from(
                    SELECT date_format(created_at,'%%Y-%%m-%%d') df,uid_name,count(*) count 
                     FROM t_login_log '''+sql+''' group by uid_name,df order by df desc,count desc)a 
                      group by df desc limit %s,%s
                    ''',startpage,pre_page)
                else:
                    count=self.db.get(' select count(*) count from t_login_log '+sql)
                    pagination=Pagination(page,pre_page,count.count,self.request)
                    startpage=(page-1)*pre_page
                    all_users=self.db.query(' select * from t_login_log '+sql+' order by created_at desc limit %s,%s ',startpage,pre_page)

            else:
                count = self.db.get(
                        '''SELECT count(*) count FROM t_user a  where  0=0
                        '''+sql)
                pagination = Pagination(page, pre_page, count.count, self.request)
                startpage = (page - 1) * pre_page
                all_users =self.db.query('''SELECT a.*,b.name role_name FROM t_user a 
                inner join t_user_group b on a.role=b.id  where 0=0 '''+sql+''' order by reg_time desc limit %s,%s''',startpage,pre_page)
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
                params=params,
                page1=page,
                tag=tag,
                department_names=department_names,
                is_admin_user=str(is_admin_user['is_admin'])
            )
        elif tag=='find_kj':
            department_id=self.get_argument('department_id','')
            t_user_relation=self.db.query('''
            select * from t_user_relation where  department_id=%s order by is_leader desc        
            ''',department_id)
            return self.write({'kj':t_user_relation})
        elif tag=='detail_login':
            created_at=self.get_argument('created_at','')
            login_name=self.get_argument('login_name','')
            t_login_log=self.db.query(' select rea_ip,url,uid_name,date_format(created_at,"%%Y-%%m-%%d %%H:%%I:%%S") created_at from t_login_log where date_format(created_at,"%%Y-%%m-%%d")=%s and uid_name=%s  order by created_at desc ',
            created_at,login_name)
            self.write({'t_login_log':t_login_log})

    @tornado.web.authenticated
    def post(self):
        tag=self.get_argument('tag','')
        if tag=='kj_manage':
            kj_name=self.get_argument('kj_name','')
            department_id=self.get_argument('department_id','')
            department_name=self.get_argument('department_name','')
            title_name=self.get_argument('title_name','')
            relation_id=self.get_argument('relation_id','')
            delete_id=self.get_argument('delete_id','')
            t_user=self.db.get(' select * from t_user where name=%s',kj_name)
            t_user_relation=self.db.get(' select * from t_user_relation where uid_name=%s ',kj_name)
            is_leader=0
            if not t_user and not relation_id and not delete_id:
                return self.write('-1')
            elif t_user_relation and not relation_id and not delete_id:
                return self.write('-2')
            if '经理' in title_name or  '主管' in title_name:
                is_leader=1
            if relation_id:
                self.db.execute(''' 
                update t_user_relation set department_name=%s,
                department_id=%s,title_name=%s,is_leader=%s where id=%s
                 ''',department_name,department_id,title_name,is_leader,relation_id)
            elif delete_id:
                self.db.execute(' delete from t_user_relation where id=%s ',delete_id)
            else:
                result=self.db.execute(''' 
                insert into t_user_relation
                (department_name,department_id,uid_name,uid,work_tel,per_tel,title_name,is_leader)
                values(%s,%s,%s,%s,%s,%s,%s,%s)
                ''',department_name,department_id,t_user.name,t_user.id,t_user.phone,t_user.person_phone,title_name,is_leader)
                self.write({'result':result})
class LockUserhandler(BaseHandler):
    @tornado.web.authenticated
    def get(self,id):
        cur_id=self.get_secure_cookie('uid')
        if self.get_secure_cookie('role_list'):
            role_list=self.get_secure_cookie('role_list').split(',')
        else:
            role_list=[]
        is_admin_user=self.db.get('select is_admin from t_user where id=%s',int(cur_id))
        if is_admin_user['is_admin']==1 or '277' in role_list:
            self.db.execute("""
            update  t_user  set is_lock=%s where id=%s
        """,int(1),int(id))

class UnlockUserHandler(BaseHandler):
    @tornado.web.authenticated
    def get(self):
        id=self.get_argument('id','')
        cur_id=self.get_secure_cookie('uid')
        if self.get_secure_cookie('role_list'):
            role_list=self.get_secure_cookie('role_list').split(',')
        else:
            role_list=[]
        is_admin_user=self.db.get('select is_admin from t_user where id=%s',int(cur_id))
        if is_admin_user['is_admin']==1 or '277' in role_list:
            self.db.execute("""
            update  t_user  set is_lock=%s where id=%s
        """,int(0),int(id))
    @tornado.web.authenticated
    def post(self):
        user_id=self.get_argument('user_id','')
        forbid_outer_net=self.get_argument('forbid_outer_net','')
        print(user_id)
        if forbid_outer_net=='1':
            forbid_outer_net='0'
        else:
            forbid_outer_net='1'
        self.db.execute('''
        update t_user set forbid_outer_net=%s where id=%s
        ''',forbid_outer_net,user_id)
class InsertUserHandler(BaseHandler):
    @tornado.web.authenticated
    def get(self):
        member_page=self.get_argument('member_page','')
        t_user_department=self.db.query('''
            select * from t_user_department 
        ''')
        if self.get_secure_cookie('role')=='8':
            t_user_group=self.db.query('''
        select * from t_user_group
        ''')
        else:
            t_user_group=self.db.query('''
        select * from t_user_group where is_hr=1
        ''')
        self.render('accounts/insertuser.html',
        error=None,
        t_user_group=t_user_group,
        t_user_department=t_user_department,
        t_user='',
        user_id='',
        member_page=member_page,
        search_key='')
    @tornado.web.authenticated
    def post(self):
        cur_id=self.get_secure_cookie('uid')
        tag=self.get_argument('tag','')
        role=self.get_secure_cookie('role')
        if self.get_secure_cookie('role_list'):
            role_list=self.get_secure_cookie('role_list').split(',')
        else:
            role_list=[]
        is_admin_user=self.db.get('select is_admin from t_user where id=%s',int(cur_id))
        guid = uuid.uuid4()
        if tag=='select_child':
            parent_id=self.get_argument('parent_id','')
            t_user_child=self.db.query('''
            select * from t_user_department where parent_id=%s
            ''',parent_id)
            self.write({'data':t_user_child})
        else:
            member_page=self.get_argument('member_page','')
            if is_admin_user['is_admin']==1 or '277' in role_list:
                name=self.get_argument('name')
                exist_user=self.db.get('select * from t_user where name=%s',name)
                if exist_user:
                    return self.write('-1')
                password=self.get_argument('password')
                hashPassword=hashlib.md5(password).hexdigest()
                f_email=self.get_argument('email')
                phone=self.get_argument('phone','')
                is_lock=self.get_argument('is_lock')
                role=self.get_argument('role')
                remark=self.get_argument('remark','')
                is_admin=self.get_argument('is_admin',0)
                qc=self.get_argument('qc','')
                person_phone=self.get_argument('person_phone','')
                department_name=self.get_argument('department_name')
                department_childs=self.get_argument('department_childs','')
                title_name=self.get_argument('title_name','')
                is_first=self.get_argument('is_first','')
                department_id=0
                department_child=None
                if department_childs:
                    department_id=department_childs.split('_')[0]
                    department_child=department_childs.split('_')[1]
                result=self.db.execute('''
                    insert into t_user(name,pass,email,phone,is_lock,role,reg_time,
                    remark,person_phone,department_name,department_id,department_child,title_name,guid)
                     values(%s,%s,%s,%s,%s,%s,UTC_TIMESTAMP(),%s,%s,%s,%s,%s,%s,%s)
                    ''',name,hashPassword,f_email,phone,int(is_lock),int(role),remark,
                    person_phone,department_name,department_id,department_child,title_name,guid)
                if result>0 and department_child:
                    self.db.execute('''
                        insert into t_user_relation
                        (department_name,department_id,uid_name,uid,work_tel,per_tel,is_leader,title_name)
                        values(%s,%s,%s,%s,%s,%s,0,%s)
                    ''',department_child,department_id,name,result,phone,person_phone,title_name)
            self.write('manageuser?page='+member_page)

class ChangeUserHandler(BaseHandler):
    @tornado.web.authenticated
    def get(self):
        error=None
        user_id=self.get_argument('user_id')
        member_page=self.get_argument('member_page','')
        t_user=self.db.get('''
        select * from t_user 
        
         where id=%s''',user_id)
        t_user_department=self.db.query('''
            select * from t_user_department 
        ''')
        t_user_group=self.db.query('''
        select * from t_user_group where id!=8
        ''')
        self.render('accounts/insertuser.html',
        error=error,
        search_key='',
        t_user=t_user,
        user_id=user_id,
        t_user_group=t_user_group,
        t_user_department=t_user_department,
        member_page=member_page)

    @tornado.web.authenticated
    def post(self):
        cur_id=self.get_secure_cookie('uid')
        user_id=self.get_argument('user_id','')
        role=self.get_secure_cookie('role')
        member_page=self.get_argument('member_page','')
        if self.get_secure_cookie('role_list'):
            role_list=self.get_secure_cookie('role_list').split(',')
        else:
            role_list=[]
        change_user=self.db.get('select name from t_user where id=%s',int(user_id))
        is_admin_user=self.db.get('select is_admin from t_user where id=%s',int(cur_id))
        if is_admin_user['is_admin']==1 or '277' in role_list:
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
                    phone=self.get_argument('phone','')
                    is_lock=self.get_argument('is_lock')
                    role=self.get_argument('role')
                    remark=self.get_argument('remark')
                    is_admin=self.get_argument('is_admin','') or '0'
                    qc=self.get_argument('qc','') or '0'
                    person_phone=self.get_argument('person_phone','')
                    department_name=self.get_argument('department_name')
                    department_childs=self.get_argument('department_childs','')
                    title_name=self.get_argument('title_name','')
                    is_first=self.get_argument('is_first','') or '0'
                    department_id=0
                    department_child=None
                    if department_childs:
                        department_id=department_childs.split('_')[0]
                        department_child=department_childs.split('_')[1]
                    
                    self.db.execute('''
                        update  t_user set name=%s,email=%s,phone=%s,is_lock=%s,role=%s,
                        remark=%s,person_phone=%s,department_name=%s,department_id=%s,
                        department_child=%s,title_name=%s
                         where id=%s
                        ''',name,f_email,phone,int(is_lock),int(role),remark,
                        person_phone,department_name,department_id,department_child,
                        title_name,user_id)
                    self.db.execute('''
                    update t_user_relation set 
                    department_name=%s,department_id=%s,uid_name=%s,work_tel=%s,per_tel=%s,title_name=%s
                    where uid=%s
                    ''',department_child,department_id,name,phone,person_phone,title_name,user_id)
                self.write('manageuser?page='+member_page)

            else:
                f_email=self.get_argument('email')
                phone=self.get_argument('phone','')
                is_lock=self.get_argument('is_lock')
                role=self.get_argument('role')
                remark=self.get_argument('remark')
                is_admin=self.get_argument('is_admin','') or '0'
                qc=self.get_argument('qc','') or '0'
                person_phone=self.get_argument('person_phone','')
                department_name=self.get_argument('department_name')
                department_childs=self.get_argument('department_childs','')
                title_name=self.get_argument('title_name','')
                is_first=self.get_argument('is_first','') or '0'
                department_id=0
                department_child=None
                if department_childs:
                    department_id=department_childs.split('_')[0]
                    department_child=department_childs.split('_')[1]
                self.db.execute('''
                    update  t_user set name=%s,email=%s,phone=%s,is_lock=%s,role=%s,
                    remark=%s,person_phone=%s,department_name=%s,department_id=%s,
                    department_child=%s,title_name=%s
                     where id=%s
                    ''',name,f_email,phone,int(is_lock),int(role),remark,
                    person_phone,department_name,department_id,department_child,title_name,user_id)
                self.db.execute('''
                    update t_user_relation set 
                    department_name=%s,department_id=%s,uid_name=%s,work_tel=%s,per_tel=%s,title_name=%s
                    where uid=%s
                    ''',department_child,department_id,name,phone,person_phone,title_name,user_id)
            self.write('manageuser?page='+member_page)

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
