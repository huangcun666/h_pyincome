# -*- coding: utf-8 -*-
from handlers.base import BaseHandler
import json
import datetime
import time
import logging
import tornado
import tornado.httpclient
import os
import random
import string
import uuid,xlwt
from tornado.options import define, options
from Pagination import Pagination
logger = logging.getLogger('boilerplate.' + __name__)


class AddrHandler(BaseHandler):
    @tornado.web.authenticated
    def get(self):

        tag = self.get_argument("tag", "all")
        uid = self.get_secure_cookie("uid")
        role = self.get_secure_cookie("role")
        uid_name = self.get_secure_cookie("name")
        is_check=self.get_secure_cookie('is_check')
        is_manager=self.get_secure_cookie('is_manager')
        kj_manage=self.get_secure_cookie('kj_manage')
        ctype = self.get_argument("ctype","")
        act_id = self.get_argument("act_id", "")

        if tag =="all":
            company = self.get_argument("company", "")
            cq_uid=self.get_argument('cq_uid','')
            newtype=self.get_argument('newtype','')
            add_ctype_sql = ""
            act_id_sql=""
            left_sql="left"
            order_column = " rent_end  "
            expired_count = 0
            company_sql=""
            gs_sql=''
            gs_sql1=''

            if ctype =="expired":
                order_column = " rent_end  "
                add_ctype_sql = " where DATE_FORMAT(rent_end,'%%Y-%%m-01') <=DATE_ADD( DATE_FORMAT(now(),'%%Y-%%m-01'), INTERVAL 1 Month)  and act_id=0"  #小于一个月

            elif ctype == "expired_customer":
                add_ctype_sql = " where DATE_FORMAT(rent_end,'%%Y-%%m-01') <=DATE_ADD( DATE_FORMAT(now(),'%%Y-%%m-01'), INTERVAL -2 Month)  "  #小于2个月
                order_column = " b.created_at desc "
       

            if company:
                if add_ctype_sql or add_ctype_sql:
                    company_sql = " and "
                else:
                    company_sql = " where "
                company_sql += '  a.company like "%%' + company + '%%" '
                if cq_uid:
                    company_sql+=' and a.cq_uid=%s '%cq_uid
            if cq_uid and not company:
                if add_ctype_sql or add_ctype_sql:
                    company_sql = " and "
                else:
                    company_sql = " where "
                company_sql += '  a.cq_uid=%s '%cq_uid
            if role=='9':
                if add_ctype_sql or add_ctype_sql or company_sql:
                    gs_sql = " and "
                else:
                    gs_sql=" where "
                gs_sql+=' a.cq_uid=%s '%uid
                gs_sql1=' and a.cq_uid=%s '%uid

            if act_id:
                left_sql=" inner "
                act_id_sql += "  and  act_id=%s" % (act_id)  #小于一个月
            if not ctype and not act_id and not newtype and not company and not cq_uid and role!='9':
                new_addr_sql=' where a.new_addr=0 '
            else:
                new_addr_sql=' and a.new_addr=0 '
            if ctype=='biangeng':
                new_addr_sql+=" where addr_tag=1 "
            elif ctype=='zhuxiao':
                new_addr_sql+=" where addr_tag=2 "
            else:
                new_addr_sql+=' and addr_tag=0 '

            expired_count = self.db_company.get(
                '''  select count(*) count from t_addr_manager a 
                left
                join t_addr_manager_req b on a.id =b.addr_id  where DATE_FORMAT(rent_end,'%%Y-%%m-01') <=DATE_ADD( DATE_FORMAT(now(),'%%Y-%%m-01'), INTERVAL 1 Month)  and act_id=0 and a.new_addr=0 and addr_tag=0  '''+gs_sql1
            )
            custoemr_expired_count = self.db_company.get(
                '''  select count(*) count from t_addr_manager a
              left
                 join t_addr_manager_req b on a.id =b.addr_id  where DATE_FORMAT(rent_end,'%%Y-%%m-01') <=DATE_ADD( DATE_FORMAT(now(),'%%Y-%%m-01'), INTERVAL -2 Month)  and act_id=0  and a.new_addr=0 and addr_tag=0  '''+gs_sql1
            )
            all_count = self.db_company.get(
                '''  select count(*) count from t_addr_manager a left join t_addr_manager_req b on a.id =b.addr_id  where 1=1 and a.new_addr=0 and addr_tag=0 '''+gs_sql1 )
            biangeng_count=self.db_company.get(
                '''  select count(*) count from t_addr_manager a  where a.addr_tag=1 '''+gs_sql1 )
            zhuxiao_count=self.db_company.get(
                '''  select count(*) count from t_addr_manager a  where a.addr_tag=2 '''+gs_sql1 )
            pre_page = 12
            page = int(self.get_argument("page", 1))


            project_type = self.db_company.query(
                """select *,ifnull(b.c,0) cc from t_type a left  join 
                (            select act_id,count(*) c
                 from t_addr_manager a left join t_addr_manager_req b on a.id =b.addr_id 

                    where a.act_id <> 0  and a.new_addr=0 and addr_tag=0 """+gs_sql1+""" 
                    group by act_id) b on a.order_int=b.act_id
                
                
                 where type_category='地址管理' order by order_int""")

            t_user_teams = self.db.query(
                "select a.*,b.team_id from t_user a inner join t_user_teams b on a.id=b.uid"
            )
            if role=='9':
                new_sql=' and a_follow_uid=%s '%uid
            else:
                new_sql=''
            new_addr_count=self.db_company.get('''
             select count(*) a,
             (select count(*) from t_addr_manager where new_addr=1 and addr_arr is not null and rent_start is null '''+new_sql+''' )b,
               (select count(*) from t_addr_manager where new_addr=1 and addr_arr is not null and rent_start is not null '''+new_sql+''')c,
            (select count(*) from t_addr_manager where new_addr=0 and is_new=1 and addr_arr is not null and rent_start is not null '''+new_sql+''')d
              from t_addr_manager where new_addr=1 and addr_arr is null and rent_start is null '''+new_sql)
            if newtype:
                if newtype=='addr_al_arrange':
                    new_sql+=' and addr_arr is not null and rent_start is null and new_addr=1 '
                elif newtype=='addr_check':
                    new_sql+=' and addr_arr is not null and rent_start is not null and new_addr=1 '
                elif newtype=='addr_pass':
                    new_sql+=' and new_addr=0 and is_new=1  and addr_arr is not null and rent_start is not null '
                else:
                    new_sql+=' and addr_arr is null and rent_start is null and new_addr=1 '
                
                if company_sql or gs_sql:
                    sql=' and is_new=1 '
                else:
                    sql=' where is_new=1 '

                count=self.db_company.get('''
                    select count(*) count from t_addr_manager a
                '''+company_sql +gs_sql+sql+new_sql)
                pagination = Pagination(page, pre_page, count.count, self.request)
                startpage = (page-1) * pre_page
                t_addr_manager=self.db_company.query('''
                    select * from t_addr_manager a '''+company_sql +gs_sql+sql+new_sql+''' order by created_at desc limit %s,%s
                ''',startpage,pre_page)
            else:
                count = self.db_company.get(
                    '''  select count(*) count from t_addr_manager a ''' + left_sql
                    + ''' join t_addr_manager_req b on a.id =b.addr_id ''' +
                    add_ctype_sql + act_id_sql + company_sql+gs_sql+new_addr_sql)
                pagination = Pagination(page, pre_page, count.count, self.request)
                startpage = (page-1) * pre_page
                t_addr_manager = self.db_company.query(
                    '''select a.*,b.req_act_id_name,b.req_now_addr,b.req_remark,created_by,b.created_at bcreated_at
                    from t_addr_manager a ''' + left_sql +
                    ''' join t_addr_manager_req b on a.id =b.addr_id   ''' +
                    add_ctype_sql + act_id_sql + company_sql +gs_sql+new_addr_sql+''' order by ''' +
                    order_column + '''  
                    limit %s,%s 
                    ''', startpage, pre_page)
            print     '''select a.*,b.req_act_id_name,b.req_now_addr,b.req_remark,created_by,b.created_at bcreated_at
                 from t_addr_manager a ''' + left_sql +  ''' join t_addr_manager_req b on a.id =b.addr_id  
                 ''' + add_ctype_sql + act_id_sql + company_sql +gs_sql+new_addr_sql+''' order by ''' + order_column



            cq_names=self.db.query(' select * from  t_user where role=9 ')

            return self.render(
                'addr/addr_list.html',
                zhuxiao_count=zhuxiao_count,
                biangeng_count=biangeng_count,
                new_addr_count=new_addr_count,
                newtype=newtype,
                cq_names=cq_names,
                expired_count=expired_count.count,
                custoemr_expired_count=custoemr_expired_count.count,
                all_count=all_count.count,
                t_user_teams=t_user_teams,
                company=company,
                act_id=act_id,
                cq_uid=cq_uid,
                project_type=project_type,
                t_addr_manager=t_addr_manager,
                pagination=pagination,
                search_key='',
                tag=tag,
                ctype=ctype)
        elif tag == "addr_list_sales":
            pre_page = 12
            page = int(self.get_argument("page", 1))
            act_id = self.get_argument("act_id", "")
            ctype = self.get_argument("ctype","")
            act_id_sql = ""
            if act_id:

                act_id_sql += "  and  act_id=%s" % (act_id)  #小于一个月



            expired_count = self.db_company.get(
                '''  select count(*) count from t_addr_manager a 
                inner join t_addr_manager_req b on a.id =b.addr_id  where DATE_FORMAT(rent_end,'%%Y-%%m-01') <=DATE_ADD( DATE_FORMAT(now(),'%%Y-%%m-01'), INTERVAL 1 Month) 
                 and act_id=0  and follow_uid=%s ''', uid)
            custoemr_expired_count = self.db_company.get(
                '''  select count(*) count from t_addr_manager a inner join 
                t_addr_manager_req b on a.id =b.addr_id  where DATE_FORMAT(rent_end,'%%Y-%%m-01')
                 <=DATE_ADD( DATE_FORMAT(now(),'%%Y-%%m-01'), INTERVAL -2 Month)  and act_id=0   and follow_uid=%s ''',
                uid)
            all_count = self.db_company.get(
                '''  select count(*) count from t_addr_manager a inner join t_addr_manager_req b on a.id =b.addr_id   and follow_uid=%s ''',uid)

            count = self.db_company.get(
                '''  select count(*) count from t_addr_manager a inner join t_addr_manager_req b on a.id=b.addr_id and a.req_id=b.id
                 where   follow_uid=%s ''' + act_id_sql, uid)

            pagination = Pagination(page, pre_page, count.count, self.request)
            startpage = (page - 1) * pre_page
            t_addr_manager = self.db_company.query('''
                select a.id addr_id ,a.*,a.req_id,b.finish_type_id,b.finish_type_name,b.finish_uid_at from t_addr_manager a inner join t_addr_manager_req b on a.id=b.addr_id and a.req_id=b.id where 
            follow_uid=%s ''' + act_id_sql + ''' order by b.created_at desc
                limit %s,%s 
                ''', uid, startpage, pre_page)
            project_type = self.db_company.query(
                """select *,ifnull(b.c,0) cc from t_type a left  join 
                (            select act_id,count(*) c
                 from t_addr_manager a left join t_addr_manager_req b on a.id =b.addr_id 

                    where a.act_id <> 0 and follow_uid=%s 
                    group by act_id) b on a.order_int=b.act_id
                
                
                 where type_category='地址管理' order by order_int""", uid)

            return self.render(
                'addr/addr_list_sales.html',
                expired_count=expired_count.count,
                custoemr_expired_count=custoemr_expired_count.count,
                all_count=all_count.count,
                project_type=project_type,
                t_addr_manager=t_addr_manager,
                pagination=pagination,
                search_key='',
                ctype=ctype,
                act_id=act_id,
            )
        elif tag == "show":
            addr_id = self.get_argument("addr_id")
            company_guid = self.get_argument("guid")
            search_key = self.get_argument("search_key", "")
            tag_type = self.get_argument("tag_type", "")
            from_tag = self.get_argument("from_tag","")
            if not addr_id:
                self.write("not companyid or guid")
            else:
                t_addr_manager = self.db_company.get(
                    """select * from t_addr_manager 
                     where id=%s
                     """, addr_id)
                if not t_addr_manager:
                    return self.write("not t_addr_manager")
                t_addr_manager_req  = self.db_company.get(
                    "select * from t_addr_manager_req where id=%s",t_addr_manager.req_id)
                if not t_addr_manager:
                    self.write("not t_addr_manager")
                else:
                    sql_tag_type = ""
                    if tag_type:
                        sql_tag_type = ''' and tag_type  like "%%''' + tag_type + '''%%"'''

                    t_company_msg = self.db_company.query(
                        "select * from t_company_msg where rel_id=%s  and btype_id=2"
                        + sql_tag_type + " order by created_at desc", addr_id)
                    print t_company_msg, "t_company_msg"
                    t_company_tag_group = self.db_company.query("""
                       select tag_category,GROUP_CONCAT(tag_name,"_",id) gc from t_company_tag group by tag_category

                    """)
                    t_type = self.db_company.query(
                        "select * from t_type where type_category='销售计划'")
                    t_plan = self.db_company.query(
                        "select * from t_plan where rel_id=%s", addr_id)
                    t_type_finish = self.db_company.query(
                        "select * from t_type where type_category='地址办结'")
                    t_type_finish_type = self.db_company.query(
                        "select * from t_type where type_category='地址审批'")
                    t_addr_manager_upload = 0
                    if t_addr_manager_req:
                        t_addr_manager_upload = self.db_company.query(
                            "select * from t_addr_manager_upload where req_id=%s and up_type='跟进人反馈'",
                            t_addr_manager_req.id)

                    return self.render(
                        'addr/addr_show.html',
                        t_type_finish_type=t_type_finish_type,
                        t_type_finish=t_type_finish,
                        t_addr_manager_req=t_addr_manager_req,
                        t_addr_manager_upload=t_addr_manager_upload,
                        search_key=search_key,
                        t_plan=t_plan,
                        t_type=t_type,
                        t_addr_manager=t_addr_manager,
                        t_company_tag_group=t_company_tag_group,
                        t_company_msg=t_company_msg,
                        from_tag=from_tag)

    @tornado.web.authenticated
    def post(self):
        tag = self.get_argument("tag")
        uid_name = self.get_secure_cookie("name")
        role = self.get_secure_cookie("role")
        uid = self.get_secure_cookie("uid")
        dt = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        if tag =="delete_addr":
            addr_id = self.get_argument("addr_id")
            if not addr_id:
                return self.write("not addr_id")
            elif (role =="8") or (role=="7"):
                self.db_company.execute("""
                    delete from t_addr_manager where id=%s
                """, addr_id)
                self.db_company.execute("""
                    delete from t_addr_manager_req where addr_id=%s
                """, addr_id)
                self.write("0")
            else:
                return self.write("您不能操作操作删除!")


        elif tag=="add_req":
            cq_addr_now = self.get_argument("cq_addr_now", "")
            cq_addr_remark = self.get_argument("cq_addr_remark", "")
            addr_id = self.get_argument("addr_id")
            if not addr_id:
                return self.write("not id")
            project_type = self.db_company.get(
                "select * from t_type where type_category='地址管理' and order_int=1"
            )

            t_addr_manager = self.db_company.get(
                "select * from t_addr_manager where id=%s", addr_id)
            if not t_addr_manager:
                return self.write("数据不存在哦")
            req_id = self.db_company.execute(
                "insert into t_addr_manager_req(addr_id,req_now_addr,req_remark,created_at ,created_by,created_uid,req_act_id,req_act_id_name,req_act_at,req_act_uid,req_act_uid_name) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                addr_id, cq_addr_now, cq_addr_remark, dt, uid_name, uid,
                project_type.order_int, project_type.type_name, dt, uid, uid_name)
            if req_id:
                self.db_company.execute(
                    "update t_addr_manager set act_id=%s,act_id_name=%s,act_id_at=%s,act_by_uid=%s,act_by_uid_name=%s,act_by_uid_at=%s,req_id=%s where id=%s",
                    project_type.order_int, project_type.type_name, dt, uid,
                    uid_name, dt, req_id, addr_id)
                msg_text = "发起到期收款"
                self.db_company.execute("""
                            insert into t_company_msg(uid,uid_name,message,created_at,company_name,tag_type,btype_id,rel_id,ext_id)
                            values(%s,%s,%s,%s,%s,%s,%s,%s,%s)
                            """, uid, uid_name, msg_text, dt,
                                        t_addr_manager.company, "操作记录", 2,
                                        addr_id, req_id)
        elif tag=="ass":
            follow_uid_name = self.get_argument("follow_uid_name")
            ass_remark = self.get_argument("ass_remark", "")
            addr_id = self.get_argument("addr_id")
            req_id = self.get_argument("req_id")

            if not follow_uid_name:
                return self.write("没有选择跟进人")
            t_user = self.db.get("select name,id from t_user where name=%s",follow_uid_name)
            if not t_user:
                return self.write("跟进人不存在!")
            t_addr_manager = self.db_company.get(
                "select * from t_addr_manager where id=%s", addr_id)
            if not t_addr_manager:
                return self.write("数据不存在哦")

            project_type = self.db_company.get(
                "select * from t_type where type_category='地址管理' and order_int=2"
            )
            result = self.db_company.execute(
                "update t_addr_manager set act_id=%s,act_id_name=%s,act_by_uid=%s,act_by_uid_name=%s,act_by_uid_at=%s,a_follow_uid=%s,a_follow_uid_name=%s,a_follow_uid_at=%s where id=%s",
                project_type.order_int, project_type.type_name, uid, uid_name,
                dt, t_user.id, t_user.name,dt, addr_id)
            if result==0:
                result = self.db_company.execute(
                    """
                    update t_addr_manager_req set follow_uid=%s,follow_uid_name=%s,ass_remark=%s,
                    ass_uid=%s,ass_uid_name=%s,ass_uid_at=%s,req_act_id=%s,req_act_id_name=%s,req_act_at=%s,req_act_uid=%s,req_act_uid_name=%s,req_act_uid_at=%s
                     where id=%s
                """, t_user.id, t_user.name, ass_remark,
                 uid, uid_name, dt,
                    project_type.order_int, project_type.type_name,dt,uid,uid_name,dt, req_id)

                msg_text = "分配%s跟进" % (t_user.name)
                self.db_company.execute("""
                            insert into t_company_msg(uid,uid_name,message,created_at,company_name,tag_type,btype_id,rel_id,ext_id)
                            values(%s,%s,%s,%s,%s,%s,%s,%s,%s)
                            """, uid, uid_name, msg_text, dt,
                                        t_addr_manager.company, "操作记录", 2,
                                        addr_id, req_id)

            self.write(str(result))
        elif tag=='back_addr':
            addr_id = self.get_argument("addr_id")
            req_id = self.get_argument("req_id")
            t_addr_manager = self.db_company.get(
                    """select * from t_addr_manager where id=%s""", addr_id)
            self.db_company.execute('''
            update t_addr_manager set act_id=0,act_id_name=null where id=%s
            ''',addr_id)
            self.db_company.execute('''
            delete from  t_addr_manager_req where id=%s
            ''',req_id)
            self.db_company.execute("""
            insert into t_company_msg(uid,uid_name,message,created_at,company_name,tag_type,btype_id,rel_id,ext_id)
            values(%s,%s,%s,%s,%s,%s,%s,%s,%s)""", uid, uid_name, '撤回待安排', dt,
                                        t_addr_manager.company, "操作记录", 2,addr_id, req_id)

        elif tag == "leader":
            leader_type_id = self.get_argument("leader_type_id")
            leader_type_id_name = self.get_argument("leader_type_id_name")
            leader_remark = self.get_argument("leader_remark", "")
            addr_id = self.get_argument("addr_id")
            req_id = self.get_argument("req_id")

            t_addr_manager = self.db_company.get(
                "select * from t_addr_manager where id=%s", addr_id)
            if not t_addr_manager:
                return self.write("数据不存在哦")

            project_type = self.db_company.get(
                "select * from t_type where type_category='地址管理' and order_int=5"
            )
            result = self.db_company.execute(
                "update t_addr_manager set act_id=%s,act_id_name=%s,act_by_uid=%s,act_by_uid_name=%s,act_by_uid_at=%s where id=%s",
                project_type.order_int, project_type.type_name, uid, uid_name,
                dt, addr_id)
            if result == 0:
                result = self.db_company.execute(
                    """
                    update t_addr_manager_req set leader_type_id=%s,leader_type_id_name=%s,leader_uid=%s,leader_uid_name=%s,leader_remark=%s,leader_uid_at=%s, req_act_id=%s,req_act_id_name=%s,req_act_at=%s,req_act_uid=%s,req_act_uid_name=%s,req_act_uid_at=%s
                     where id=%s
                """, leader_type_id, leader_type_id_name, uid, uid_name,
                    leader_remark, dt, project_type.order_int,
                    project_type.type_name, dt, uid, uid_name, dt, req_id)

                msg_text = "标记部续费办结审核:%s" % (leader_type_id_name)
                self.db_company.execute("""
                            insert into t_company_msg(uid,uid_name,message,created_at,company_name,tag_type,btype_id,rel_id,ext_id)
                            values(%s,%s,%s,%s,%s,%s,%s,%s,%s)
                            """, uid, uid_name, msg_text, dt,
                                        t_addr_manager.company, "操作记录", 2,
                                        addr_id, req_id)

            self.write(str(result))
        elif tag=="finish":
            t_type_finish_id=self.get_argument('t_type_finish_id')
            t_type_finish_name=self.get_argument('t_type_finish_name')
            project_id = self.get_argument("project_id",0)
            req_id=self.get_argument('req_id')
            addr_id = self.get_argument("addr_id")
            follow_uid_remark=self.get_argument('follow_uid_remark','')
            project_type = self.db_company.get(
                "select * from t_type where type_category='地址管理' and order_int=4"
            )
            t_addr_manager_req = self.db_company.get(
                "select * from t_addr_manager_req where id=%s", req_id)

            t_addr_manager = self.db_company.get(
                "select * from t_addr_manager where id=%s", addr_id)

            if not t_addr_manager:
                return self.write("数据不存在哦")
            elif not project_id:
                return self.write("确认单编号不能为空哦")
            elif not t_addr_manager_req:
                return self.write("没有t_addr_manager_req")
            elif t_addr_manager_req.follow_uid != uid:
                file_list = ""
                file1 = self.request.files.get("uploaderInput")
                up_type = self.get_argument("up_type")
                if file1:
                    for item in file1:
                        if item:
                            ori_filename = item["filename"]

                            filename_full = options.upload_path + "/addr/%s/" % (
                                addr_id)
                            url_path = "/static/addr/%s/" % (addr_id)
                            try:
                                os.makedirs(filename_full)
                            except OSError:
                                if not os.path.isdir(filename_full):
                                    raise
                            extension = os.path.splitext(ori_filename)[1]

                            uuid_str = str(uuid.uuid4())
                            fname = "{0}_{1}{2}".format(uuid_str, addr_id, extension)

                            save_full_path = filename_full + fname
                            url_fname = "{0}{1}".format(url_path, fname)

                            output_file = open(save_full_path, 'w')
                            output_file.write(item["body"])
                            file_path = url_fname
                            fresult = self.db_company.execute("""
                                    INSERT INTO t_addr_manager_upload
                                (
                                `file_name`,
                                `created_at`,
                                `uid`,
                                `uid_name`,
                                `addr_id`,
                                `req_id`,
                                `remark`,`up_type`)
                                VALUES
                                (
                                %s,
                                    %s,
                                    %s,
                                %s,
                                    %s,
                                    %s,
                                    %s,%s);

                                    """, file_path, dt, uid, uid_name, addr_id,
                                                    req_id, "", up_type)
                            if fresult:
                                file_list = file_list + url_fname + ","

                if file_list:
                    file_list = file_list[:-1]
                result = self.db_company.execute(
                    "update t_addr_manager set act_id=%s,act_id_name=%s,act_by_uid=%s,act_by_uid_name=%s,act_by_uid_at=%s ,project_id=%s where id=%s",
                    project_type.order_int, project_type.type_name, uid, uid_name,
                    dt,project_id, addr_id)
                if result == 0:
                    result = self.db_company.execute("""
                        update t_addr_manager_req set finish_type_id=%s,
                        finish_type_name=%s,finish_remark=%s,finish_uid=%s,finish_uid_name=%s,finish_uid_at=%s,
                        
                        req_act_id=%s,req_act_id_name=%s,req_act_at=%s,req_act_uid=%s,req_act_uid_name=%s,req_act_uid_at=%s,project_id=%s
                        where id=%s
                    """,t_type_finish_id,t_type_finish_name,follow_uid_remark,uid,uid_name, dt, project_type.order_int, project_type.type_name,
                                                     dt, uid, uid_name, dt,project_id,
                                                     req_id)
                    if not follow_uid_remark:
                        follow_uid_remark="无"
                    msg_text = "%s标记办结: %s 备注:%s " % (uid_name, t_type_finish_name,
                                                follow_uid_remark)
                    self.db_company.execute("""
                                insert into t_company_msg(uid,uid_name,message,created_at,company_name,tag_type,btype_id,rel_id,ext_id,file_list,project_id)
                                values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
                                """, uid, uid_name, msg_text, dt,
                                            t_addr_manager.company, "操作记录", 2,
                                            addr_id, req_id, file_list,
                                            project_id)
                self.write(str(result))
            else:
                self.write("您不是跟进人.无法确认哦.")



        elif tag == "confirm_follow":
            addr_id = self.get_argument("addr_id")
            req_id = self.get_argument("req_id")
            if not addr_id and not  req_id:
                return self.write("addr_id/ req_id is null")
            project_type = self.db_company.get(
                "select * from t_type where type_category='地址管理' and order_int=3"
            )
            t_addr_manager = self.db_company.get(
                "select * from t_addr_manager where id=%s", addr_id)
            if not t_addr_manager:
                return self.write("数据不存在哦")

            t_addr_manager_req = self.db_company.get(
                "select * from t_addr_manager_req where id=%s", req_id)
            if not t_addr_manager_req:
                return self.write("没有t_addr_manager_req")
            elif t_addr_manager_req.follow_uid != uid:
                result = self.db_company.execute(
                    "update t_addr_manager set act_id=%s,act_id_name=%s,act_by_uid=%s,act_by_uid_name=%s,act_by_uid_at=%s where id=%s",
                    project_type.order_int, project_type.type_name, uid, uid_name,
                    dt, addr_id)
                if result == 0:
                    result = self.db_company.execute("""
                        update t_addr_manager_req set follow_uid_confirm=%s,req_act_id=%s,req_act_id_name=%s,req_act_at=%s,req_act_uid=%s,req_act_uid_name=%s,req_act_uid_at=%s
                        where id=%s
                    """, dt, project_type.order_int, project_type.type_name,
                                                     dt, uid, uid_name, dt,
                                                     req_id)
                    msg_text = "%s确认跟进" % (t_addr_manager_req.follow_uid_name)
                    self.db_company.execute("""
                                insert into t_company_msg(uid,uid_name,message,created_at,company_name,tag_type,btype_id,rel_id,ext_id)
                                values(%s,%s,%s,%s,%s,%s,%s,%s,%s)
                                """, uid, uid_name, msg_text, dt,
                                            t_addr_manager.company, "操作记录", 2,
                                            addr_id, req_id)
                self.write(str(result))
            else:
                self.write("您不是跟进人.无法确认哦.")
        elif tag=="modify":
            #     leader_type_id=$('input[name=ok_leader_type_id]:checked').val()
            # leader_type_id_name=$('input[name=ok_leader_type_id]:checked').attr("type_name")
            # leader_remark = $("#ok_leader_remark").val()

            addr_id = self.get_argument("addr_id")
            req_id = self.get_argument("req_id")
            company = self.get_argument("company", "")
            company_uid = self.get_argument("company_uid", "")
            customer_tel = self.get_argument("customer_tel", "")
            rent_by = self.get_argument("rent_by","")
            addr_type = self.get_argument("addr_type", "")
            addr_con = self.get_argument("addr_con", "")
            addr_arr = self.get_argument("addr_arr", "")
            rent_start = self.get_argument("rent_start", "")
            rent_end = self.get_argument("rent_end", "")
            addr_manager = self.get_argument("addr_manager", "")
            old_addr = self.get_argument("old_addr", "")
            now_addr = self.get_argument("now_addr", "")
            customer_remark = self.get_argument("customer_remark", "")
            addr_id = self.get_argument("addr_id")
            addr_tag=self.get_argument('addr_tag','0')
            act_id=self.get_argument('act_id','')

            if not addr_id and not req_id:
                return self.write("addr_id/ req_id is null")
            elif not company:
                return self.write("company name is null")
            else:
                if not  rent_start:
                    rent_start=None
                if not rent_end:
                    rent_end=None
                project_type = self.db_company.get(
                "select * from t_type where type_category='地址管理' and order_int=7"
                 )
                up_msg = ""
                t_addr_manager = self.db_company.get("select * from t_addr_manager where id=%s",addr_id)
                if not t_addr_manager:
                    return self.write("not t_addr_manager")

                if t_addr_manager.company!=company:
                    up_msg += "公司名称:%s 改为 %s\n" % (t_addr_manager.company,company)
                if t_addr_manager.company_uid!=company_uid:
                    up_msg += "企业代码:%s 改为 %s\n" % (t_addr_manager.company_uid,
                                                  company_uid)
                if t_addr_manager.customer_tel!=customer_tel:
                    up_msg += "客户电话:%s 改为 %s\n" % (t_addr_manager.customer_tel,
                                                  customer_tel)
                if t_addr_manager.rent_by!=rent_by:
                    up_msg += "承租人:%s 改为 %s\n" % (t_addr_manager.rent_by,
                                                 rent_by)
                if t_addr_manager.addr_type!=addr_type:
                    up_msg += "地址性质:%s 改为 %s\n" % (t_addr_manager.addr_type,
                                                  addr_type)
                if t_addr_manager.addr_con!=addr_con:
                    up_msg += "地址性质类型:%s 改为 %s\n" % (t_addr_manager.addr_con,
                                                    addr_con)
                if str(t_addr_manager.addr_arr)!=addr_arr:
                    up_msg += "安排时间:%s 改为 %s\n" % (t_addr_manager.addr_arr,addr_arr)
                if str(t_addr_manager.rent_start)!=rent_start:
                    up_msg += "租赁开始时间:%s 改为 %s\n" % (t_addr_manager.rent_start,
                                                    rent_start)
                if str(t_addr_manager.rent_end)!=rent_end:
                    up_msg += "租赁结束时间:%s 改为 %s\n" % (t_addr_manager.rent_end,
                                                    rent_end)
                if t_addr_manager.addr_manager!=addr_manager:
                    up_msg += "物业安排:%s 改为 %s\n" % (t_addr_manager.addr_manager,
                                                  addr_manager)
                if t_addr_manager.old_addr!=old_addr:
                    up_msg += "原挂靠地址:%s 改为 %s\n" % (
                        t_addr_manager.old_addr, old_addr)
                if t_addr_manager.now_addr!=now_addr:
                    up_msg += "现执照地址:%s 改为 %s\n" % (t_addr_manager.now_addr,
                                                   now_addr)
                if t_addr_manager.customer_remark != customer_remark:
                    up_msg += "客户备注内容:%s 改为 %s\n" % (
                        t_addr_manager.customer_remark, customer_remark)
                if t_addr_manager.addr_tag!=int(addr_tag):
                    if t_addr_manager.addr_tag==0:
                        if addr_tag=='1':
                            up_msg+="标签:改为 变更\n"
                        elif addr_tag=='2':
                            up_msg+='标签:改为 注销\n'
                    elif t_addr_manager.addr_tag==1:
                            up_msg+='标签:变更 改为 注销\n'
                    elif t_addr_manager.addr_tag==2:
                        up_msg+='标签:注销 改为 变更\n'
                
                if act_id:
                    project_type = self.db_company.get(
                "select * from t_type where type_category='地址管理' and order_int=6")       
                    sql=' ,act_id=%s,act_id_name="%s" '%(project_type.order_int,project_type.type_name)
                    self.db_company.execute(
                    """
                    update t_addr_manager_req set  
                    leader_type_id=1,leader_type_id_name='通过',leader_uid=%s,leader_uid_name=%s
                    ,req_act_id=%s,req_act_id_name=%s,req_act_at=%s,req_act_uid=%s,req_act_uid_name=%s,req_act_uid_at=%s
                     where id=%s""",uid,uid_name,project_type.order_int,project_type.type_name,dt,uid,uid_name,dt,req_id)
                else:
                    sql=''
                result = self.db_company.execute(
                    """
                    UPDATE `t_addr_manager`
                        SET
                       `addr_tag`=%s,
                        `company` =%s,
                        `company_uid` = %s,
                        `rent_by` =%s,
                        `addr_type` = %s,
                        `addr_con` =%s,
                        `rent_start` = %s,
                        `rent_end` = %s,
                        `addr_manager` = %s,
                        `old_addr` =%s,
                        `now_addr` =%s,
                        `customer_tel` =%s,
                        `addr_arr` = %s,
                        `customer_remark` =%s
                        """+sql+"""
                        WHERE `id` = %s

                """,addr_tag, company, company_uid, rent_by, addr_type, addr_con,
                    rent_start, rent_end, addr_manager, old_addr, now_addr,
                    customer_tel, addr_arr, customer_remark, addr_id)
                if result==0:
                    pass


                    # leader_remark=%s,
                    # leader_type_id=%s,
                    # leader_type_id_name=%s,
                    # leader_uid=%s,
                    # leader_uid_name=%s,
                    # leader_uid_at=%s ,leader_remark,leader_type_id,leader_type_id_name,uid,uid_name,dt
                if up_msg:
                    msg_text = "确认续期及信息修改:%s" % (up_msg)
                    self.db_company.execute("""
                                    insert into t_company_msg(uid,uid_name,message,created_at,company_name,tag_type,btype_id,rel_id,ext_id)
                                    values(%s,%s,%s,%s,%s,%s,%s,%s,%s)
                                    """, uid, uid_name, msg_text, dt,
                                                t_addr_manager.company, "操作记录", 2,
                                                addr_id, req_id)
                if act_id:
                    self.db_company.execute("""
                            insert into t_company_msg(uid,uid_name,message,created_at,company_name,tag_type,btype_id,rel_id,ext_id)
                            values(%s,%s,%s,%s,%s,%s,%s,%s,%s)
                            """, uid, uid_name,'标记部续费办结审核:通过', dt,
                                        t_addr_manager.company, "操作记录", 2,
                                        addr_id, req_id)

                self.write(str(result))

        elif tag=='new_addr_manage':
            company=self.get_argument('company','')
            rent_by=self.get_argument('rent_by','')
            addr_type=self.get_argument('addr_type','')
            newtype=self.get_argument('newtype','')
            addr_arr=self.get_argument('addr_arr','')
            addr_manager=self.get_argument('addr_manager','')
            rent_start=self.get_argument('rent_start','')
            rent_end=self.get_argument('rent_end','')
            old_addr=self.get_argument('old_addr','')
            addr_id=self.get_argument('addr_id','')
            delete_addr_id=self.get_argument('delete_addr_id','')
            is_inner=self.get_argument('is_inner','')
            addr_con=self.get_argument('addr_con','')
            if not addr_arr:
                addr_arr=None
            if not rent_start:
                rent_start=None
            if not rent_end:
                rent_end=None
            
            if  delete_addr_id:
                self.db_company.execute('''
                    delete from t_addr_manager where id=%s
                ''',delete_addr_id)
            elif is_inner:
                result=self.db_company.execute('''
                update t_addr_manager set addr_con=%s,rent_by=%s,addr_type=%s,a_follow_uid=%s,a_follow_uid_name=%s,
                new_addr=1,act_id=0,act_id_name=null,is_new=1,rent_start=null,rent_end=null,addr_arr=null,
                addr_manager=null,old_addr=null,is_inside=%s,cq_uid=%s,cq_uid_name=%s where id=%s
                ''',addr_con,rent_by,addr_type,uid,uid_name,is_inner,uid,uid_name,addr_id)
                if result==0:
                    self.db_company.execute("""
            insert into t_company_msg(uid,uid_name,message,created_at,company_name,tag_type,btype_id,rel_id,ext_id)
            values(%s,%s,%s,%s,%s,%s,%s,%s,0)""", uid, uid_name, '标记为内部变更', dt,
                                        company, "操作记录", 2,addr_id)
            elif not newtype:
                result=self.db_company.execute('''
            insert into t_addr_manager(company,created_at,
            rent_by,addr_type,a_follow_uid,a_follow_uid_name,new_addr,act_id,cq_uid_at,cq_uid,cq_uid_name,is_new,addr_con)
             values(%s,%s,%s,%s,%s,%s,1,0,null,%s,%s,1,%s)
            ''',company,dt,rent_by,addr_type,uid,uid_name,uid,uid_name,addr_con)
                if result>0:
                    self.db_company.execute("""
            insert into t_company_msg(uid,uid_name,message,created_at,company_name,tag_type,btype_id,rel_id,ext_id)
            values(%s,%s,%s,%s,%s,%s,%s,%s,0)""", uid, uid_name, '创建新待安排', dt,
                                        company, "操作记录", 2,result)
            elif addr_id: 
                if newtype=='addr_arrange':
                    result=self.db_company.execute('''
                update t_addr_manager set company=%s,rent_by=%s,addr_type=%s,addr_arr=%s,addr_manager=%s,addr_con=%s where id=%s
                ''',company,rent_by,addr_type,addr_arr,addr_manager,addr_con,addr_id)
                    if result==0:
                        self.db_company.execute("""
            insert into t_company_msg(uid,uid_name,message,created_at,company_name,tag_type,btype_id,rel_id,ext_id)
            values(%s,%s,%s,%s,%s,%s,%s,%s,0)""", uid, uid_name, '填写安排时间,物业安排', dt,
                                        company, "操作记录", 2,addr_id)
                elif newtype=='addr_al_arrange':
                    result=self.db_company.execute('''
                update t_addr_manager set addr_con=%s,company=%s,rent_by=%s,addr_type=%s,addr_arr=%s,addr_manager=%s,rent_start=%s,rent_end=%s,old_addr=%s where id=%s
                ''',addr_con,company,rent_by,addr_type,addr_arr,addr_manager,rent_start,rent_end,old_addr,addr_id)
                    if result==0:
                        self.db_company.execute("""
            insert into t_company_msg(uid,uid_name,message,created_at,company_name,tag_type,btype_id,rel_id,ext_id)
            values(%s,%s,%s,%s,%s,%s,%s,%s,0)""", uid, uid_name, '填写租凭时间,原挂靠地址', dt,
                                        company, "操作记录", 2,addr_id)
                elif newtype=='addr_check':
                    result=self.db_company.execute('''
                update t_addr_manager set addr_con=%s,company=%s,rent_by=%s,addr_type=%s,addr_arr=%s,addr_manager=%s,rent_start=%s,rent_end=%s,old_addr=%s, new_addr=0 where id=%s
                ''',addr_con,company,rent_by,addr_type,addr_arr,addr_manager,rent_start,rent_end,old_addr,addr_id)
                    if result==0:
                        self.db_company.execute("""
            insert into t_company_msg(uid,uid_name,message,created_at,company_name,tag_type,btype_id,rel_id,ext_id)
            values(%s,%s,%s,%s,%s,%s,%s,%s,0)""", uid, uid_name,'审核通过', dt,
                                        company, "操作记录", 2,addr_id)
        
        elif tag=="is_exist_company":
            company=self.get_argument('company')
            exist_jd_company=self.db_company.query('''
            select a.*
                 from t_addr_manager a  inner  join t_addr_manager_req b on a.id =b.addr_id
                   and  (act_id=2 or act_id=3) and a.new_addr=0  and addr_tag=0 and company=%s limit 1
            ''',company)
            # 待接单，已接单
            exist_company=self.db_company.query('''
            select * from t_addr_manager where company=%s limit 1
            ''',company)
            if exist_jd_company:
                self.write({'result':'-1','gendan':exist_jd_company[0].a_follow_uid_name,'addr_id':exist_jd_company[0].id})
            elif exist_company:
                self.write({'result':'-2','gendan':exist_company[0].a_follow_uid_name,'addr_id':exist_company[0].id})
            
        elif tag=='export_data':
            company = self.get_argument("company", "")
            cq_uid=self.get_argument('cq_uid','')
            newtype=self.get_argument('newtype','')
            ctype=self.get_argument('ctype','')
            act_id=self.get_argument('act_id','')
            add_ctype_sql = ""
            act_id_sql=""
            left_sql="left"
            order_column = " rent_end  "
            expired_count = 0
            company_sql=""
            gs_sql=''
            gs_sql1=''

            if ctype =="expired":
                order_column = " rent_end  "
                add_ctype_sql = " where DATE_FORMAT(rent_end,'%%Y-%%m-01') <=DATE_ADD( DATE_FORMAT(now(),'%%Y-%%m-01'), INTERVAL 1 Month)  and act_id=0"  #小于一个月

            elif ctype == "expired_customer":
                add_ctype_sql = " where DATE_FORMAT(rent_end,'%%Y-%%m-01') <=DATE_ADD( DATE_FORMAT(now(),'%%Y-%%m-01'), INTERVAL -2 Month)  "  #小于2个月
                order_column = " b.created_at desc "
       

            if company:
                if add_ctype_sql or add_ctype_sql:
                    company_sql = " and "
                else:
                    company_sql = " where "
                company_sql += '  a.company like "%%' + company + '%%" '
                if cq_uid:
                    company_sql+=' and a.cq_uid=%s '%cq_uid
            if cq_uid and not company:
                if add_ctype_sql or add_ctype_sql:
                    company_sql = " and "
                else:
                    company_sql = " where "
                company_sql += '  a.cq_uid=%s '%cq_uid
            if role=='9':
                if add_ctype_sql or add_ctype_sql or company_sql:
                    gs_sql = " and "
                else:
                    gs_sql=" where "
                gs_sql+=' a.cq_uid=%s '%uid
                gs_sql1=' and a.cq_uid=%s '%uid

            if act_id:
                left_sql=" inner "
                act_id_sql += "  and  act_id=%s" % (act_id)  #小于一个月
            if not ctype and not act_id and not newtype and not company and not cq_uid and role!='9':
                new_addr_sql=' where a.new_addr=0 '
            else:
                new_addr_sql=' and a.new_addr=0 '
            if ctype=='biangeng':
                new_addr_sql+=" where addr_tag=1 "
            elif ctype=='zhuxiao':
                new_addr_sql+=" where addr_tag=2 "
            else:
                new_addr_sql+=' and addr_tag=0 '
    
            if role=='9':
                new_sql=' and a_follow_uid=%s '%uid
            else:
                new_sql=''
            if newtype:
                if newtype=='addr_al_arrange':
                    new_sql+=' and addr_arr is not null and rent_start is null and new_addr=1 '
                elif newtype=='addr_check':
                    new_sql+=' and addr_arr is not null and rent_start is not null and new_addr=1 '
                elif newtype=='addr_pass':
                    new_sql+=' and new_addr=0 and is_new=1  and addr_arr is not null and rent_start is not null '
                else:
                    new_sql+=' and addr_arr is null and rent_start is null and new_addr=1 '
                
                if company_sql or gs_sql:
                    sql=' and is_new=1 '
                else:
                    sql=' where is_new=1 '
                t_addr_manager=self.db_company.query('''
                    select * from t_addr_manager a '''+company_sql +gs_sql+sql+new_sql+''' order by created_at desc''')
            else:
                t_addr_manager = self.db_company.query(
                    '''select a.*,b.req_act_id_name,b.req_now_addr,b.req_remark,created_by,b.created_at bcreated_at
                    from t_addr_manager a ''' + left_sql +
                    ''' join t_addr_manager_req b on a.id =b.addr_id   ''' +
                    add_ctype_sql + act_id_sql + company_sql +gs_sql+new_addr_sql+''' order by ''' +
                    order_column 
                  )
            if t_addr_manager:
                wb = xlwt.Workbook()
                sh = wb.add_sheet(u'地址管理表')
                # 按位置添加数据a
                if newtype:
                    sh.write(0, 0, u"日期")
                    sh.write(0, 1, u"企业名称")
                    sh.write(0, 2, u"承租人")
                    sh.write(0, 3 , u"地址性质")
                    sh.write(0, 4, u"跟单员")
                    sh.write(0, 5, u"安排时间")
                    sh.write(0, 6, u"物业安排")
                    sh.write(0, 7, u"租凭开始时间")
                    sh.write(0,8,u"租凭结束时间")
                    sh.write(0, 9, u"地址性质类型")
                    sh.write(0, 10, u"原挂靠地址")

                    for idx,item in enumerate(t_addr_manager):
                        idx=idx+1
                        sh.write(idx, 0, item.created_at.strftime("%Y-%m-%d"))
                        if item.is_inside==1:
                            sh.write(idx,1,item.company+u'(内部变更)')
                        else:
                            sh.write(idx,1,item.company)
                        sh.write(idx,2,item.rent_by)
                        sh.write(idx,3,item.addr_type)
                        sh.write(idx,4,item.a_follow_uid_name)
                        sh.write(idx,5,item.addr_arr)
                        sh.write(idx,6,item.addr_manager)
                        sh.write(idx,7,item.rent_start)
                        sh.write(idx,8,item.rent_end)
                        sh.write(idx,9,item.addr_con)
                        sh.write(idx,10,item.old_addr)
                else:
                    sh.write(0, 0, u"编号")
                    sh.write(0, 1, u"最新动态")
                    sh.write(0, 2, u"跟单人")
                    sh.write(0, 3 , u"企业名称")
                    sh.write(0, 4, u"企业代码")
                    sh.write(0, 5, u"承租人")
                    sh.write(0, 6, u"地址性质")
                    sh.write(0, 7, u"地址性质类型")
                    sh.write(0,8,u"工商专员")
                    sh.write(0, 9, u"安排时间")
                    sh.write(0, 10, u"租凭开始时间")
                    sh.write(0, 11, u"租凭结束时间")
                    sh.write(0, 12, u"物业安排")
                    sh.write(0, 13, u"原挂靠地址")
                    sh.write(0, 14, u"现执照地址")
                    sh.write(0, 15, u"联系电话")
                    sh.write(0, 16, u"客服顾问")
                    sh.write(0, 17, u"销售顾问")

                    for idx,item in enumerate(t_addr_manager):
                        idx=idx+1
                        sh.write(idx,0,item.id)
                        str_act=''
                        if item.act_id_name:
                            str_act=item.act_id_name
                        if item.act_by_uid_name:
                            str_act+=item.act_by_uid_name
                        sh.write(idx,1,str_act)
                        if item.a_follow_uid_name:
                            sh.write(idx,2,item.a_follow_uid_name)
                        else:
                            sh.write(idx,2,u'无')
                        if item.is_inside==1:
                            sh.write(idx,3,item.company+u'(内部变更)')
                        else:
                            sh.write(idx,3,item.company)
                        if item.company_uid:
                            sh.write(idx,4,item.company_uid)
                        else:
                            sh.write(idx,4,u'')
                        sh.write(idx,5,item.rent_by)
                        sh.write(idx,6,item.addr_type)
                        sh.write(idx,7,item.addr_con)
                        sh.write(idx,8,item.cq_uid_name)
                        if item.addr_arr:
                            sh.write(idx,9,item.addr_arr.strftime('%Y-%m-%d'))
                        else:
                            sh.write(idx,9,u'')
                        if item.rent_start:
                            sh.write(idx,10,item.rent_start.strftime('%Y-%m-%d'))
                        else:
                            sh.write(idx,10,u'')
                        if item.rent_end:
                            sh.write(idx,11,item.rent_end.strftime('%Y-%m-%d'))
                        else:
                            sh.write(idx,11,u'')
                        sh.write(idx,12,item.addr_manager) 
                        sh.write(idx,13,item.old_addr)
                        sh.write(idx,14,item.now_addr)
                        sh.write(idx,15,item.customer_tel)
                        sh.write(idx,16,item.gw_uid_name)
                        sh.write(idx,17,item.xs_uid_name)

                wb.save('media/output/地址管理(%s).xls'%(uid_name))
                self.write({'output_path':'static/output/地址管理(%s).xls'%(uid_name)})    









       