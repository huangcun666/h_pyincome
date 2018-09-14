# -*- coding: utf-8 -*-
from handlers.base import BaseHandler
import urllib
import json
import datetime
import time
import logging
import tornado
import tornado.httpclient
import os
import random
import string
import re
import hashlib
logger = logging.getLogger('boilerplate.' + __name__)
from Pagination import Pagination

class SiteHandler(BaseHandler):
    @tornado.web.authenticated
    def get(self):
        tag = self.get_argument("tag","list")
        if tag =="list":

            page= int(self.get_argument("page",1))
            pre_page=20
            count = self.db.get('''SELECT count(*) count FROM t_user_site a , t_user b where a.uid=b.id
               ''')
            pagination = Pagination(page, pre_page, count.count, self.request)
            startpage = (page-1) * pre_page
            t_user_sites = self.db.query('''
                SELECT  a.* , b.name  FROM t_user_site a , t_user b where a.uid=b.id
                order by created_at desc limit %s,%s
                ''',startpage,pre_page)

            t_temp = self.db.query("""
                select * from t_temp order by order_int desc
                """)

            return self.render('admin/sites.html',pagination=pagination,t_user_sites=t_user_sites,
                               t_temp=t_temp, form_tag="list")
        elif tag =="mysite":
            uid = self.get_secure_cookie("uid")
            page = int(self.get_argument("page", 1))
            pre_page=10
            count =self.db.get('''SELECT count(*) count FROM t_user_site where uid=%s
               ''', uid)
            pagination = Pagination(page, pre_page, count.count, self.request)
            startpage = (page-1) * pre_page
            t_user_sites = self.db.query('''
                SELECT  a.*,b.name  FROM t_user_site a , t_user  b where a.uid=b.id and  uid=%s
                order by created_at desc limit %s,%s
                ''',uid,startpage,pre_page)

            t_temp = self.db.query("""
                select * from t_temp order by order_int desc
                """)

            return self.render('admin/sites.html',pagination=pagination,t_user_sites=t_user_sites,
                               t_temp=t_temp, form_tag="mysite")
        elif tag=="new":
            form_tag = self.get_argument("form_tag")
            t_temp = self.db.query("""
                select * from t_temp order by order_int desc
                """)
            users = self.db.query("select * from t_user ")
            return self.render('site_new.html', t_temp=t_temp, users=users, form_tag=form_tag)
        elif tag=="edit":
            form_tag = self.get_argument("form_tag")
            site_id = self.get_argument("site_id")
            users = self.db.query("select * from t_user ")
            t_user_site = self.db.get("""
                select a.*,b.temp_name from t_user_site a , t_temp b where a.temp_id=b.id and a.id=%s order by order_int desc
                """,site_id)
            return self.render('site_edit.html', t_user_site=t_user_site, msg="", result=1, users=users, form_tag=form_tag)

        elif tag=="get":
            site_id = self.get_argument("site_id")
            t_temp_mod = self.db.query("""
                select a.id ms_id,mod_name ,mod_id,site_id,mod_type,bname  from t_temp_mod a inner join t_mod b on a.mod_id=b.id where site_id=%s  order by mod_sort
                """,site_id)

            return self.render("user_mod.html",t_temp_mods=t_temp_mod)
        elif tag=="nav":
            site_id = self.get_argument("site_id")
            t_mod_nav = self.db.query("""
                select *   from t_temp_nav where site_id=%s  order by nav_order
                """,site_id)
            site = self.db.get("select * from t_user_site where id =%s",site_id)
            return self.render("admin/nav_list.html",t_mod_nav=t_mod_nav,site=site,msg="")



    @tornado.web.authenticated
    def post(self):
        tag= self.get_argument("tag","add")
        uid = self.get_secure_cookie("uid")
        temp_id = self.get_argument("temp_id","")
        site_title = self.get_argument("site_title","")
        site_desc = self.get_argument("site_desc","")
        site_keyword = self.get_argument("site_keyword","")
        site_name = self.get_argument("site_name","","")
        site_domain = self.get_argument("site_domain","")
        site_uid = self.get_argument("uid",0)
        form_tag = self.get_argument("form_tag","mysite")

        if tag=="new":

            id = self.db.execute("""
                INSERT INTO `t_user_site` (`uid`, `temp_id`, `site_name`, `site_keyword`,
                 `site_desc`, `site_code`, `site_backup`, `created_at`, `updated_at`,
                 `site_title`, `site_domain`)
                    VALUES
                        (%s, %s, %s, %s,%s, NULL, NULL, now(), now(), %s, %s);
                """, site_uid, temp_id, site_name, site_keyword, site_desc, site_title, site_domain)


            ida = self.db.execute("""
                INSERT INTO `t_temp_mod` ( `mod_id`, `site_id`, `code`, `is_default`, `is_show_nav`, `mod_order`, `temp_id`)
                select mod_id,%s,code,0,is_show_nav,mod_order,temp_id from t_temp_mod where temp_id=%s and site_id=0;
                """,id,temp_id)
            self.db.execute("""
                INSERT INTO `t_temp_nav` ( `bname`, `site_id`, `is_show_nav`, `nav_order`, `temp_id`, `link`, `is_default`)
                select bname,%s,is_show_nav,nav_order,%s,link,0 from t_temp_nav where site_id=0 and is_default=1

                """,id,temp_id)
            # print "id",id,"idaida",ida,"temp_id","temp_id",temp_id
            self.redirect("/sites")

        elif tag =="edit":
            site_id = self.get_argument("site_id")
            temp_id = self.get_argument("temp_id")
            site_title = self.get_argument("site_title")
            site_desc = self.get_argument("site_desc")
            site_keyword = self.get_argument("site_keyword")
            site_name = self.get_argument("site_name")
            site_domain = self.get_argument("site_domain")
            msg=""
            result= 1
            result = self.db.execute("""
               update `t_user_site` set  `uid` =%s, `site_name`=%s, `site_keyword`=%s,
                 `site_desc`=%s,  `updated_at`=now(),
                 `site_title`=%s, `site_domain`=%s,uid=%s where id=%s
                """, uid, site_name, site_keyword, site_desc, site_title, site_domain, site_uid, site_id)
            if result==0:
                msg = "更新成功"
            t_user_site = self.db.get("""
                    select a.*,b.temp_name from t_user_site a , t_temp b where a.temp_id=b.id and a.id=%s order by order_int desc
                    """,site_id)
            users = self.db.query("select * from t_user ")

            return self.render('site_edit.html', t_user_site=t_user_site, msg=msg, result=result, users=users, form_tag=form_tag)
        elif tag=="nav":
            site_id = self.get_argument("site_id")
            bnames = self.get_arguments("bname")
            links = self.get_arguments("link")
            is_show_navs = self.get_arguments("is_show_nav")
            ids = self.get_arguments("ids")
            for row in  range(0,len(ids)):
                is_show_nav = 0
                bname = bnames[row]
                link = links[row]
                id = ids[row]
                self.db.execute("update t_temp_nav set bname=%s, link=%s where id =%s",bname,link,id)


            msg= "数据保存成功!"
            t_mod_nav = self.db.query("""
                select *   from t_temp_nav where site_id=%s  order by nav_order
                """,site_id)
            site = self.db.get("select * from t_user_site where id =%s",site_id)

            return self.render("admin/nav_list.html",t_mod_nav=t_mod_nav,site=site,msg=msg)

        elif tag=="set_nav_show":
            is_show_nav = self.get_argument("is_show_nav")
            nav_id = self.get_argument("nav_id")

            if not nav_id:
                self.write("not nav_id")
            else:
                result = self.db.execute("update t_temp_nav set is_show_nav=%s where id=%s",is_show_nav,nav_id)
                self.write(str(result))
