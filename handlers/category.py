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
from datetime import datetime
logger = logging.getLogger('boilerplate.' + __name__)


class CategoryHandler(BaseHandler):
    @tornado.web.authenticated
    def post(self):
        tag = self.get_argument("tag")
        uid = self.get_secure_cookie('uid')

        if tag =="add":
            category_name = self.get_argument('category_name')
            order_int = self.get_argument('order_int',0)
            is_business=self.get_argument('is_business','0')

            if not category_name:
                self.write("not category name")
            else:
                result = self.db.execute("insert into t_projects_category(category_name,uid,order_int,is_business) values(%s,%s,%s,%s)",
                category_name,uid, order_int,is_business)
                all_categorys=self.db.query('''
           select * from  t_projects_category  where uid=%s  order by order_int desc,id desc 
        ''',uid)
                self.write({'all_categorys':all_categorys,'id':result})

        elif tag=='update_category':
            numarr=self.get_argument('numarr')
            numarr=numarr.split(',')
            for item in numarr[::3]:
                self.db.execute('''
                    update t_projects_category set category_name=%s,order_int=%s where id=%s
                ''',numarr[numarr.index(item)+1],numarr[numarr.index(item)+2],int(item))

        elif tag=='delete_category':
            id=self.get_argument('id')
            is_business=self.get_argument('is_business','')

            self.db.execute('''
                    delete from t_projects_category where id=%s
                ''',id)
            if is_business:
                self.db.execute('''
                delete from business_develop_manage_category where  category_id=%s
                ''',id)
            else:
                self.db.execute(
                            "update t_projects_member set b_category_id=0 , b_category_id_name=null where member_id=%s and  b_category_id=%s",
                            uid,id)




        elif tag == "set_project_category":
            category_name = self.get_argument('category_name')
            category_id = self.get_argument("category_id")
            mid = self.get_argument("mid")
            project_ids=self.get_argument('project_ids')
 
            if not category_id:
                self.write("not category_id")
            elif not mid:
                self.write("not mid ")
            else:
                result = 1
                for item in project_ids.split(","):
                    result =self.db.execute(
                "update t_projects set category_id=%s , category_id_name=%s where id=%s and guid=%s",
                category_id, category_name, item.split('|')[0],item.split('|')[1])

                for item in mid.split(","):
                    result = self.db.execute(
                        "update t_projects_member set b_category_id=%s , b_category_id_name=%s where mid=%s ",
                        category_id, category_name, item)
                self.write(str(result))


class InsertCategoryHandler(BaseHandler):
    @tornado.web.authenticated
    def post(self):
        uid=self.get_secure_cookie('uid')
        category=self.get_argument('category')
        role=int(self.get_argument('role'))
        print(role)
        category_id=self.db.execute('''
            insert into t_projects_category(category_name,uid,role) values(%s,%s,%s)
        ''',category,int(uid),role)

        self.write({'category_id':category_id})


class InsertUpdateProjectCategoryHandler(BaseHandler):
    @tornado.web.authenticated
    def post(self):
        category_id=self.get_argument('category_id')
        id=self.get_argument('id')
        category_name=self.db.get('select category_name from t_projects_category where id=%s',int(category_id))
        uid=self.get_secure_cookie('uid')
        project_categorys=self.db.get('select * from t_projects_category_list where project_id=%s',int(id))
        if project_categorys:
            self.db.execute('''
                    update t_projects_category_list set category_id=%s,uid=%s,category_name=%s where project_id=%s
                ''',int(category_id),int(uid),category_name['category_name'],int(id))
            self.write({'category_name':category_name['category_name']})
        else:
            dt=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            self.db.execute('''
                insert into t_projects_category_list(project_id,
                uid,category_id,category_name,created_at) values(%s,%s,%s,%s,%s)
            ''',int(id),int(uid),int(category_id),category_name['category_name'],dt)
            self.write({'category_name':category_name['category_name']})

class CheckProjectCategoryHandler(BaseHandler):
    @tornado.web.authenticated
    def get(self):
        page = int(self.get_argument("page", 1))
        tag=self.get_argument('tag',None)
        pre_page = 20
        startpage = (page - 1) * pre_page
        count = self.db.get(
                '''
                SELECT count(*) count FROM t_projects_category_list
                ''')
        pagination = Pagination(page, pre_page, count.count, self.request)
        startpage = (page - 1) * pre_page
        projectcategorylist=self.db.query(
            '''
                select * from t_projects_category_list order by created_at desc limit %s,%s
            ''',startpage,pre_page)
        categorys=self.db.query('select * from t_projects_category')

        allprojectcategorys=[]
        if tag:
            for category in categorys:
                if category.category_name==tag:
                    projectcategorylist=self.db.query('''
                    select * from t_projects_category_list where category_name=%s 
                    order by created_at desc limit %s,%s''',tag,startpage,pre_page)
                    for i in range(len(projectcategorylist)):
                        project_name=self.db.query('select project_name from t_projects where id=%s',int(projectcategorylist[i]['project_id']))
                        created_name=self.db.query('select name from t_user where id=%s',int(projectcategorylist[i]['uid']))
                        category_name=self.db.query('select category_name from t_projects_category_list where category_name=%s',projectcategorylist[i]['category_name'])
                        order_int=self.db.query('select order_int from t_projects_category_list where order_int=%s',int(projectcategorylist[i]['order_int']))
                        created_at=self.db.query('select created_at from t_projects_category_list where created_at=%s',projectcategorylist[i]['created_at'])
                        allprojectcategorys.append([project_name[0]['project_name'],created_name[0]['name'],
                        category_name[0]['category_name'],order_int[0]['order_int'],created_at[0]['created_at']])

        else:
            for i in range(len(projectcategorylist)):
                project_name=self.db.query('select project_name from t_projects where id=%s',int(projectcategorylist[i]['project_id']))
                created_name=self.db.query('select name from t_user where id=%s',int(projectcategorylist[i]['uid']))
                category_name=self.db.query('select category_name from t_projects_category_list where category_name=%s',projectcategorylist[i]['category_name'])
                order_int=self.db.query('select order_int from t_projects_category_list where order_int=%s',int(projectcategorylist[i]['order_int']))
                created_at=self.db.query('select created_at from t_projects_category_list where created_at=%s',projectcategorylist[i]['created_at'])
                allprojectcategorys.append([project_name[0]['project_name'],created_name[0]['name'],
                category_name[0]['category_name'],order_int[0]['order_int'],created_at[0]['created_at']])

        self.render('project/project_category_list.html',
                                tag=tag,
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
                                allprojectcategorys=allprojectcategorys,
                                categorys=categorys)

class ProjectCategoryHandler(BaseHandler):
    @tornado.web.authenticated
    def get(self):
        page = int(self.get_argument("page", 1))
        pre_page = 20
        startpage = (page - 1) * pre_page
        count = self.db.get(
                '''SELECT count(*) count FROM t_projects 
                ''')
        pagination = Pagination(page, pre_page, count.count, self.request)
        startpage = (page - 1) * pre_page
        projects=self.db.query('select * from t_projects limit %s,%s',startpage,pre_page)
        project_categorys=self.db.query('select project_id,category_name from t_projects_category_list')
        project_categorys_uids=[]
        project_categorys_name=[]
        for i in range(len(project_categorys)):
            project_categorys_uids.append(int(project_categorys[i]['project_id']))
            project_categorys_name.append(project_categorys[i]['category_name'])
        categorys=self.db.query('select * from t_projects_category')
        self.render('project/project_category.html',
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
                                projects=projects,
                                project_categorys_uids=project_categorys_uids,
                                project_categorys_name=project_categorys_name,
                                categorys=categorys
                    )