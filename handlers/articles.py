# -*- coding: utf-8 -*-
from handlers.base import BaseHandler
import tornado
import tornado.httpclient
from Pagination import Pagination
import uuid




class NewsHandler(BaseHandler):
    def get(self,site_id,page=1):
        page =int(page)
        pre_page=12
        count =self.db.get('''SELECT count(*) count FROM t_article where site_id=%s
           ''',site_id)
        pagination = Pagination(page, pre_page, count.count, self.request)
        startpage = (page-1) * pre_page
        articles = self.db.query('''
            SELECT  *  FROM t_article where site_id=%s
            order by created_at desc limit %s,%s
            ''',site_id,startpage,pre_page)

        articles_random = self.db.query('''
            SELECT  *  FROM t_article where site_id=%s
             ORDER BY RAND()  limit 12
            ''',site_id)
        articles_new = self.db.query('''
            SELECT  *  FROM t_article where site_id=%s
             ORDER BY created_at  limit 12
            ''',site_id)
        t_user_site = self.db.get('select * from t_user_site where id=%s',site_id)
        return self.render('theme/default/news.html',pagination=pagination,articles=articles,t_user_site=t_user_site,articles_random=articles_random,articles_new=articles_new)

class NewsDetailHandler(BaseHandler):
    def get(self,id):

        item = self.db.get('select * from t_article where id=%s',id)
        t_user_site = self.db.get('select * from t_user_site where id=%s',item.site_id)
        articles_random = self.db.query('''
            SELECT  *  FROM t_article where site_id=%s
             ORDER BY RAND()  limit 12
            ''',item.site_id)
        articles_new = self.db.query('''
            SELECT  *  FROM t_article where site_id=%s
             ORDER BY created_at  limit 12
            ''',item.site_id)
        return self.render('theme/default/detail.html',t_user_site=t_user_site,item=item,articles_random=articles_random,articles_new=articles_new)


class ArticleHandler(BaseHandler):
    @tornado.web.authenticated
    def get(self):
        tag = self.get_argument("tag","list")
        site_id = self.get_argument("site_id")
        if tag =="list":
            page= int(self.get_argument("page",1))
            pre_page=10
            count =self.db.get('''SELECT count(*) count FROM t_article where site_id=%s
               ''',site_id)
            pagination = Pagination(page, pre_page, count.count, self.request)
            startpage = (page-1) * pre_page
            articles = self.db.query('''
                SELECT  *  FROM t_article where site_id=%s
                order by created_at desc limit %s,%s
                ''',site_id,startpage,pre_page)

            site = self.db.get('select * from t_user_site where id=%s',site_id)


            return self.render('articles/article_list.html',pagination=pagination,articles=articles,site=site)
        elif tag=="new":
            site = self.db.get('select * from t_user_site where id=%s',site_id)
            name = self.get_cookie("name")
            return self.render('articles/article_new.html',site=site,name=name)
        elif tag=="edit":
            id = self.get_argument("articleid")

            site = self.db.get('select * from t_user_site where id=%s',site_id)
            item = self.db.get('select * from t_article where id=%s',id)
            msg = ""
            return self.render('articles/article_edit.html',site=site,item=item,msg=msg)

    def post(self):
        tag = self.get_argument("tag","list")
        site_id = self.get_argument("site_id")
        if tag=="new":
            title = self.get_argument("title")
            keyword = self.get_argument("keyword","")
            description = self.get_argument("description","")
            content = self.get_argument("content")
            published =self.get_argument("published")
            post_by = self.get_argument("post_by","admin")
            if not title:
                self.write("not title")
            elif not content:
                self.write('not content')
            elif not site_id :
                self.write("not site id")
            else:
                result =  self.db.execute("""
                        INSERT INTO `t_article` (`title`, `content`, `published`, `created_at`, `update_at`, `keyword`, `description`, `site_id`,  `guid`,`post_by`)
                        VALUES
                            (%s, %s, %s, now(), now(), %s, %s, %s, %s,%s);

                    """,title,content,published,keyword,description,site_id,uuid.uuid4(),post_by)



                self.redirect("/articles?site_id=%s&result=%s"%(site_id,result))
        elif tag=="delete":
            articleid = self.get_argument("articleid")
            if not  articleid:
                self.write('2')
            else:
                result = self.db.execute("delete from t_article where id=%s",articleid)
                self.write(str(result))
        elif tag=="edit":
            title = self.get_argument("title")
            keyword = self.get_argument("keyword","")
            description = self.get_argument("description","")
            content = self.get_argument("content")
            published =self.get_argument("published")
            articleid = self.get_argument("articleid")
            site_id = self.get_argument("site_id")
            post_by = self.get_argument("post_by","admin")
            msg = ""
            if not title:
                self.write("not title")
            elif not content:
                self.write('not content')
            elif not site_id :
                self.write("not site id")
            elif not articleid:
                self.write("not articleid")
            else:
                result =  self.db.execute("""
                         update `t_article` set  `title`=%s, `content`=%s, `published`=%s,`update_at`=now(), `keyword`=%s, `description`=%s,
                         post_by=%s
                        where id=%s

                    """,title,content,published,keyword,description,post_by,articleid)



            site = self.db.get('select * from t_user_site where id=%s',site_id)
            item = self.db.get('select * from t_article where id=%s',articleid)
            return self.render('articles/article_edit.html',site=site,item=item,msg="保存成功")

