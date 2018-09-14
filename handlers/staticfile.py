# -*- coding: utf-8 -*-
from handlers.base import BaseHandler
import tornado
import tornado.httpclient
from Pagination import Pagination
import uuid



class StaticFile1Handler(BaseHandler):
    @tornado.web.authenticated
    def get(self):
        site_id = self.get_argument("site_id")
        tag = self.get_argument("tag","list")
        if tag == "list":
            page = self.get_argument("page",1)

            pre_page=12
            count =self.db.get('''SELECT count(*) count FROM t_static_file where site_id=%s
               ''',site_id)
            pagination = Pagination(page, pre_page, count.count, self.request)

            startpage = (page-1) * pre_page
            static_files = self.db.query('''
                SELECT  *  FROM t_static_file where site_id=%s
                order by created_at desc limit %s,%s
                ''',site_id,startpage,pre_page)
            t_user_site = self.db.get('select * from t_user_site where id=%s',site_id)


            return self.render('static_file/list.html',pagination=pagination,t_static_files=static_files,t_user_site=t_user_site)
        elif tag=="add":
            uqid = str(uuid.uuid4()).replace("-","")+".txt"
            t_user_site = self.db.get('select * from t_user_site where id=%s',site_id)

            return self.render("static_file/add.html",t_user_site=t_user_site,uqid=uqid)
        elif tag=="edit":
            sf_id = self.get_argument("sf_id")
            t_user_site = self.db.get('select * from t_user_site where id=%s',site_id)
            t_static_file = self.db.get('select * from t_static_file where id=%s',sf_id)

            return self.render("static_file/edit.html",t_user_site=t_user_site,t_static_file=t_static_file,msg="")


    @tornado.web.authenticated
    def post(self):
        site_id = self.get_argument("site_id")
        tag = self.get_argument("tag","list")
        uid = self.get_cookie("uid")

        if  tag=="add":
            fname = self.get_argument("fname")
            content = self.get_argument("content")
            fname_remark =self.get_argument("fname_remark","")
            if not fname:
                self.write("文件名为空")
            else:
                result = self.db.execute("""
                        INSERT INTO `t_static_file` (`fname`, `site_id`, `content`, `uid`, `created_at`, `update_at`,fname_remark)
                        VALUES
                            ( %s,%s,%s, %s, now(),now(),%s);
                    """,fname,site_id,content,0,fname_remark)
                return self.redirect("/static_file?site_id="+site_id)
            uqid = str(uuid.uuid4()).replace("-","")+".txt"
            t_user_site = self.db.get('select * from t_user_site where id=%s',site_id)

            return self.render("static_file/add.html",t_user_site=t_user_site,uqid=uqid)
        elif tag=="edit":
            sf_id = self.get_argument("sf_id")
            fname = self.get_argument("fname")
            content = self.get_argument("content")
            fname_remark =self.get_argument("fname_remark","")
            if not fname:
                self.write("文件名为空")
            else:
                self.db.execute("""
                        update t_static_file set
                        `fname`=%s, `content`=%s, `update_at`=now(),fname_remark=%s
                        where id=%s
                    """,fname,content,fname_remark,sf_id)
            msg = "更新成功"
            t_user_site = self.db.get('select * from t_user_site where id=%s',site_id)
            t_static_file = self.db.get('select * from t_static_file where id=%s',sf_id)
            return self.render("static_file/edit.html",t_user_site=t_user_site,t_static_file=t_static_file,msg=msg)

        elif tag=="delete":
            sf_id = self.get_argument("sf_id")


            result = self.db.execute("delete from t_static_file where id=%s",sf_id)
            self.write(str(result))