# -*- coding: utf-8 -*-
import json
import tornado.web

import logging,datetime
logger = logging.getLogger(__name__)


class BaseHandler(tornado.web.RequestHandler):
    """A class to collect common handler methods - all other handlers should
    subclass this one.
    """
    def render(self, template, **kwargs):
        # add any variables we want available to all templates
        #         zone  = self.get_secure_cookie("zone")
        # if not zone:
        #     self.set_secure_cookie("zone","北京")
        kwargs['name'] = self.get_secure_cookie("name")
        kwargs['uid'] = self.get_secure_cookie("uid")
        kwargs['role'] = self.get_secure_cookie("role")
        kwargs['is_check'] = self.get_secure_cookie("is_check")
        kwargs['is_manager'] = self.get_secure_cookie("is_manager")
        kwargs['is_bj_manage'] = self.get_secure_cookie("is_bj_manage")
        kwargs['is_gy_manage']=self.get_secure_cookie("is_gy_manage")
        kwargs['department_name']=self.get_secure_cookie("department_name")
        kwargs['is_xz_manage']=self.get_secure_cookie('is_xz_manage')
        kwargs['kj_manage'] = self.get_secure_cookie('kj_manage')
        kwargs['all_manage']=self.get_secure_cookie('all_manage')
        kwargs['is_developer'] = self.get_secure_cookie('is_developer')
        kwargs['kf_manage']=self.get_secure_cookie('kf_manage')
        kwargs['sh_manage']=self.get_secure_cookie('sh_manage')
        kwargs['express_manage']=self.get_secure_cookie('express_manage')
        kwargs['show_statis_kf']=self.get_secure_cookie('show_statis_kf')
        kwargs['is_hr']=self.get_secure_cookie('is_hr')
        if self.get_secure_cookie('role_list'):
            kwargs['role_list']=self.get_secure_cookie('role_list').split(',')
        else:
            kwargs['role_list']=[]

        today_exchange_ids=[]
        today_exchange=self.db_customer.query('''
            select id from t_customer_exchange where TO_DAYS(msg_time)<=TO_DAYS(now()) and uid=%s and summary is null
        ''',self.get_secure_cookie("uid"))
        for item in today_exchange:
            today_exchange_ids.append(item.id)
        kwargs['today_exchange_ids']=today_exchange_ids
        liuzhuan_reject_count=''
        banli_reminder=''
        if self.get_secure_cookie("department_name")=='工商部':
            liuzhuan_reject=self.db.get('''
          select count(*) count from t_projects a inner join 
                t_projects_transfile b on a.id=b.project_id and b.is_ok=1 and mtype=1 and fback_remark is not null
                inner join t_projects_milepost c on a.id=c.project_id and order_int=4 and confirm_at is null  and b.pm_id=c.member_id 
                where c.uid_name=%s and b.cq_uid_at is null
        ''',self.get_secure_cookie("name"))
            if liuzhuan_reject:
                liuzhuan_reject_count=liuzhuan_reject.count
            banli_reminder=self.db.query('''
            select c.id,c.guid,datediff(now(),b.created_at) msg_day,datediff(now(),a.created_at) member_day   from t_projects_member a
                left join t_projects_state_msg b on a.project_id=b.project_id and b.uid=a.member_id
                and b.id=(select max(id) from t_projects_state_msg where a.project_id=project_id and uid=a.member_id)
                inner join t_projects c on a.project_id=c.id and (c.busniess_from_id!=4 or c.busniess_from_id=4 and a.btype_id!=155 )
                where team_id=38 and a.member_id=%s and (a.last_milepost_id=167 or a.last_milepost_id=162) and a.is_cancel_confirm_at is null
                 limit 1
            ''',self.get_secure_cookie("uid"))
            if banli_reminder:
                
                if banli_reminder[0].msg_day>7 or (banli_reminder[0].msg_day==None and banli_reminder[0].member_day>7):
                    pass

                else:
                    banli_reminder=''
        kwargs['banli_reminder']=banli_reminder
        kwargs['liuzhuan_reject_count']=liuzhuan_reject_count
        

        
        x_real_ip = self.request.headers.get("X-Real-IP")
        ip = x_real_ip or self.request.remote_ip
        dt = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        logger.info("%s : %s  - %s://%s%s  IP:%s " %
                     (dt, self.get_secure_cookie("name"),
                      self.request.protocol, self.request.host,
                      self.request.uri, ip))

        super(BaseHandler, self).render(template, **kwargs)

    def load_json(self):
        """Load JSON from the request body and store them in
        self.request.arguments, like Tornado does by default for POSTed form
        parameters.

        If JSON cannot be decoded, raises an HTTPError with status 400.
        """
        try:
            self.request.arguments = json.loads(self.request.body)
        except ValueError:
            msg = "Could not decode JSON: %s" % self.request.body
            logger.debug(msg)
            raise tornado.web.HTTPError(400, msg)

    def get_json_argument(self, name, default=None):
        """Find and return the argument with key 'name' from JSON request data.
        Similar to Tornado's get_argument() method.
        """
        if default is None:
            default = self._ARG_DEFAULT
        if not self.request.arguments:
            self.load_json()
        if name not in self.request.arguments:
            if default is self._ARG_DEFAULT:
                msg = "Missing argument '%s'" % name
                logger.debug(msg)
                raise tornado.web.HTTPError(400, msg)
            logger.debug("Returning default argument %s, as we couldn't find "
                    "'%s' in %s" % (default, name, self.request.arguments))
            return default
        arg = self.request.arguments[name]
        logger.debug("Found '%s': %s in JSON arguments" % (name, arg))
        return arg

    @property
    def db(self):
        return self.application.db

    @property
    def db_customer(self):
        return self.application.db_customer

    # @property
    # def db_building(self):
    #     return self.application.db_building

    @property
    def db_company(self):
        return self.application.db_company

    @property
    def db_ext(self):
        return self.application.db_ext



    def get_current_user(self):
        return self.get_secure_cookie("uid")

    def get_current_role(self):
        return self.get_secure_cookie("role")

    def checkUserIn(self,members,uid):
        for item in members:
            if item:
                if item.member_id==int(uid):
                    return True
        return False

    def checkUserArrIn(self, members, uid):
        for item in members:
            if item:
                if int(item) == int(uid):
                    return True
        return False

    # def checkUserIn(self,members,uid):
    #     for item in members:
    #         if item:
    #             if item.member_id==int(uid):
    #                 return True
    #     return False
    def checkRoleIn(self, roles, role):
        for item in roles:
            if item == role:
                return True
        return False

    def checkAccIn(self, t_customer, uid):
        if t_customer:
            if t_customer.acc_uid == int(uid):
                return True
        return False

    # @property
    # def xsrf_token(self):
    #     token = super().xsrf_token
    #     self.set_cookie("_xsrf",token,expire_days=30)
    #     return token