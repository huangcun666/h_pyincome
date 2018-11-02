# -*- coding: utf-8 -*-
#coding=utf8
from Pagination import Pagination
import tornado
from handlers.base import BaseHandler
import uuid,os,datetime
from tornado.options import define, options
import msg
import qrcode
import json
import xlwt
import sys
reload(sys)
sys.setdefaultencoding('utf8')

class BusinessHandler(BaseHandler):

    @tornado.web.authenticated
    def get(self):
        tag = self.get_argument("tag","")
        uid = self.get_secure_cookie("uid")
        role = self.get_secure_cookie("role")
        all_manage=self.get_secure_cookie('all_manage') or ''
        uid_name = self.get_secure_cookie("name")
        page=self.get_argument('page',1)
        pre_page=20

        if tag=="business_develop":
            distribution=self.get_argument('distribution','')
            sums=''
            if '商机' in all_manage:
                sums=self.db.get('''
                    select count(*) count,
                    (select count(*) c from business_develop where is_distribution=1 and kf_guwen='') a,
                    (select count(*) c from business_develop where is_distribution=1 and kf_guwen!='') b
                    from business_develop
                ''')
                if distribution=='1':
                    count=self.db.get('select count(*) count from business_develop where is_distribution=1 and kf_guwen=""')
                    pagination=Pagination(page,pre_page,count.count,self.request)
                    start_page=(page-1)*pre_page
                    business_develop=self.db.query('''
                    select * from business_develop where is_distribution=1 and kf_guwen=''  order by created_at desc limit %s,%s
                ''',start_page,pre_page)
                elif distribution=='2':
                    count=self.db.get('select count(*) count from business_develop where is_distribution=1 and kf_guwen!=""')
                    pagination=Pagination(page,pre_page,count.count,self.request)
                    start_page=(page-1)*pre_page
                    business_develop=self.db.query('''
                    select * from business_develop where is_distribution=1 and kf_guwen!=''  order by created_at desc limit %s,%s
                ''',start_page,pre_page)
                else:
                    count=self.db.get('select count(*) count from business_develop')
                    pagination=Pagination(page,pre_page,count.count,self.request)
                    start_page=(page-1)*pre_page
                    business_develop=self.db.query('''
                    select * from business_develop order by created_at desc limit %s,%s
                ''',start_page,pre_page)
            else:
                count=self.db.get('''
                select count(*) count 
                from business_develop where uid=%s or online_kf_id=%s or kf_guwen_id=%s''',uid,uid,uid)
                pagination=Pagination(page,pre_page,count.count,self.request)
                start_page=(page-1)*pre_page
                business_develop=self.db.query('''
                select * from business_develop where uid=%s 
                or online_kf_id=%s or kf_guwen_id=%s
                order by created_at desc limit %s,%s
                ''',uid,uid,uid,start_page,pre_page)

            
            t_income_type = self.db.query("""
                select * from t_projects_type where income_category='业务来源' order by order_int desc
                """)
            t_talk_type = self.db.query(
                "select * from t_projects_type where income_category='沟通方式' order by order_int desc "
            )
            self.render('business/business_develop.html',
            business_develop=business_develop,
            distribution=distribution,
            pagination=pagination,
            t_income_type=t_income_type,
            t_talk_type=t_talk_type,
            search_key='',
            sums=sums)
        elif tag=="show":
            guid=self.get_argument('guid')
            id=self.get_argument('id')
            tag_type=self.get_argument('tag_type','')
            message_sql=''
            if tag_type:
                message_sql+=' and tag_type="%s"'%tag_type
            business_develop=self.db.get('''
            select a.*,b.role  from business_develop a
             inner join t_user b on a.uid=b.id
             where a.id=%s and a.guid=%s order by created_at desc
            ''',id,guid)
            if not business_develop:
                self.write('该项不存在！'+id+guid)
            else:
                linkmans=self.db.query('''
                select * from business_develop_linkman where business_id=%s order by created_at desc
                ''',id)
                link_records=self.db.query('''
                    select * from business_develop_link_record where business_id=%s order by created_at desc
                ''',id)
                cj_content=self.db.query('''
                select * from business_develop_cj_content where business_id=%s order by created_at desc
                ''',id)
                message=self.db.query('''
                select * from business_develop_message where business_id=%s '''+message_sql+''' order by created_at desc
                ''',id)
                t_income_type = self.db.query("""
                select * from t_projects_type where income_category='业务来源' order by order_int desc
                """)
                t_talk_type = self.db.query(
                "select * from t_projects_type where income_category='沟通方式' order by order_int desc "
                )
                business_develop_tag_group=self.db.query("""
                    select tag_category,GROUP_CONCAT(tag_name,'_',id) gc from business_develop_tag group by tag_category
                    order by id
                """)
                self.render('business/business_show.html',
                linkmans=linkmans,
                business_develop_tag_group=business_develop_tag_group,
                message=message,
                link_records=link_records,
                cj_content=cj_content,
                business_develop=business_develop,
                t_income_type=t_income_type,
                t_talk_type=t_talk_type,
                search_key=''
                )

    
    @tornado.web.authenticated
    def post(self):
        tag = self.get_argument("tag","")
        uid = self.get_secure_cookie("uid")
        role = self.get_secure_cookie("role")
        uid_name = self.get_secure_cookie("name")
        dt=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        if tag=="business_develop":
            company=self.get_argument('company','')
            customer_name=self.get_argument('customer_name','')
            customer_tel=self.get_argument('customer_tel','')
            source_qd=self.get_argument('source_qd','')
            source_way=self.get_argument('source_way','')
            source_key=self.get_argument('source_key','')
            customer_introducer=self.get_argument('customer_introducer','')
            inner_introducer=self.get_argument('inner_introducer','')
            status=self.get_argument('status','')
            id=self.get_argument('id','')
            delete_id=self.get_argument('delete_id','')
            online_kf=self.get_argument('online_kf','')
            kf_guwen=self.get_argument('kf_guwen','')
            is_distribution=self.get_argument('is_distribution','')
            t_user_online_kf=self.db.get('select id from t_user where name=%s',online_kf)
            if t_user_online_kf:
                online_kf_id=t_user_online_kf.id 
            else:
                online_kf_id=0
            t_user_kf_guwen=self.db.get('select id from t_user where name=%s',kf_guwen)
            if t_user_kf_guwen:
                kf_guwen_id=t_user_kf_guwen.id
            else:
                kf_guwen_id=0
            if id:
                self.db.execute('''
                    update business_develop set updated_at=now(),company=%s,customer_name=%s,customer_tel=%s,source_qd=%s,
                    source_way=%s,source_key=%s,customer_introducer=%s,inner_introducer=%s,online_kf=%s,online_kf_id=%s,kf_guwen=%s,kf_guwen_id=%s,status=%s where id=%s
                ''',company,customer_name,customer_tel,source_qd,source_way, source_key,
                customer_introducer,inner_introducer,online_kf,online_kf_id,kf_guwen,kf_guwen_id,status,id)
            elif delete_id:
                self.db.execute('''
                delete from business_develop where id=%s
                ''',delete_id)
            else:
                guid = uuid.uuid4()
                self.db.execute('''
                insert into business_develop
                 (is_distribution,company,customer_name,customer_tel,uid_name,uid,created_at,source_qd,
                source_way,source_key,customer_introducer,inner_introducer,online_kf,online_kf_id,kf_guwen,kf_guwen_id,guid,status)
                values(%s,%s,%s,%s,%s,%s,now(),%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
            ''',is_distribution,company,customer_name,customer_tel,uid_name,uid,source_qd,source_way,
                source_key,customer_introducer,inner_introducer,online_kf,online_kf_id,kf_guwen,kf_guwen_id,guid,'已创建订单')

        elif tag=="business_linkman":
            linkman=self.get_argument('linkman')
            tel=self.get_argument('tel','')
            business_id=self.get_argument('business_id','')
            linkman_id=self.get_argument('linkman_id','')
            if linkman_id:
                self.db.execute('''
                update business_develop_linkman set linkman=%s,tel=%s where id=%s
                ''',linkman,tel,linkman_id)
            else:
                self.db.execute('''
            insert into business_develop_linkman(linkman,tel,business_id,created_at,uid_name,uid)
             values(%s,%s,%s,now(),%s,%s)''',linkman,tel,business_id,uid_name,uid)
        
        elif tag=="business_cj_content":
            title=self.get_argument('title','')
            sell_counselor=self.get_argument('sell_counselor','')
            cj_content_id=self.get_argument('cj_content_id','')
            business_id=self.get_argument('business_id','')
            if cj_content_id:
                self.db.execute('''
                update business_develop_cj_content set title=%s,sell_counselor=%s where id=%s
                ''',title,sell_counselor,cj_content_id)
            else:
                self.db.execute('''
                    insert into business_develop_cj_content(title,created_at,sell_counselor,business_id)
                    values(%s,now(),%s,%s)''',title,sell_counselor,business_id)

        elif tag=="business_link_record":
            detail_record=self.get_argument('detail_record','')
            link_at=self.get_argument('link_at',"")
            link_man=self.get_argument('link_man','')
            business_id=self.get_argument('business_id','')
            id=self.get_argument('id','')
            if id:
                self.db.execute('''
                update business_develop_link_record set detail_record=%s,link_at=%s,link_man=%s where id=%s
            ''',detail_record,link_at,link_man,id)
            else:
                self.db.execute('''
                insert into business_develop_link_record(kf,kf_uid,detail_record,link_at,link_man,business_id)
                values(%s,%s,%s,%s,%s,%s)
            ''',uid_name,uid,detail_record,link_at,link_man,business_id)
        
        elif tag=="business_message":
            message=self.get_argument('message','')
            business_id=self.get_argument('business_id','')
            id=self.get_argument('id','')
            delete_id=self.get_argument('delete_id','')
            if id:
                self.db.execute('''
                update business_develop_message set message=%s,updated_at=now() where id=%s
                ''',message,id)
            elif delete_id:
                self.db.execute('''
                delete from business_develop_message where id=%s
                ''',delete_id)
            else:
                self.db.execute('''
                insert into business_develop_message(message,uid,uid_name,created_at,business_id,tag_type)
                values(%s,%s,%s,%s,%s,%s)''',message,uid,uid_name,dt,business_id,'跟进记录')
            
        
        elif tag=="save_tags":
            business_tags = self.get_argument('business_tags','')
            business_guid = self.get_argument("business_guid")
            business_id=self.get_argument('business_id','')

            if business_id:
                self.db.execute('''
                    update business_develop set business_tag=%s where id=%s and guid=%s
                ''',business_tags,business_id,business_guid)
                self.db.execute('''
                 insert business_develop_message(uid,uid_name,message,created_at,business_id,tag_type)
                 values(%s,%s,%s,%s,%s,"操作标签")
                ''',uid,uid_name,business_tags,dt,business_id)
