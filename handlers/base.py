# -*- coding: utf-8 -*-
import json
import tornado.web

import logging,datetime
logger = logging.getLogger('boilerplate.' + __name__)


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
        x_real_ip = self.request.headers.get("X-Real-IP")
        ip = x_real_ip or self.request.remote_ip
        dt = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        logger.info("%s : %s  - %s://%s%s  IP:%s " %
                    (dt, self.get_secure_cookie("name"),
                     self.request.protocol, self.request.host,
                     self.request.uri,ip))

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

    @property
    def db_building(self):
        return self.application.db_building

    @property
    def db_company(self):
        return self.application.db_company





    def get_current_user(self):
        return self.get_secure_cookie("uid")

    def get_current_role(self):
        return self.get_secure_cookie("role")
    # @property
    # def xsrf_token(self):
    #     token = super().xsrf_token
    #     self.set_cookie("_xsrf",token,expire_days=30)
    #     return token