# encoding=utf8
from handlers.base import BaseHandler
from Pagination import Pagination
import logging
import json,datetime
import tornado.web
import urllib2
import tornado.httpclient
import sys, re,os,uuid
import urllib,datetime
import events
reload(sys)
from tornado.options import define, options
sys.setdefaultencoding('utf8')

logger = logging.getLogger('boilerplate.' + __name__)


class MTransitionHandler(BaseHandler):
    @tornado.web.authenticated
    def get(self):
        tag = self.get_argument("tag")
        uid = self.get_secure_cookie("uid")
        uid_name=self.get_secure_cookie('name')
        todo=self.get_argument('todo','')
        page=int(self.get_argument('page',1))
        pre_page=20
        sql=''
        if tag =="list":
            t_projects_transition = self.db.query('''
                        select a.*,b.project_name,b.customer_company,b.customer_name from t_projects_transition a , t_projects b 
                         where a.project_id=b.id and rec_by_uid=%s order by a.created_at desc
                    ''', uid)
            self.render(
                'mobile/transition/list.html',
                t_projects_transition=t_projects_transition)
        elif tag=="list_todo":
            nums=self.db.get(
                """
                select count(*) count, 

                 (select count(*) c from t_todo_arrange_status aa inner join t_todo_arrange aa1
                  on aa.todo_id=aa1.id where aa.created_at is  null and aa.updated_at is null
                  and (aa1.responsible_per=%s or aa1.banshi_per=%s)) a,
                (select count(*) c from t_todo_arrange_status bb inner join t_todo_arrange cc 
                 on bb.todo_id=cc.id
                where bb.created_at is not null and bb.updated_at is null
                 and (cc.responsible_per=%s or cc.banshi_per=%s)
                )
                b,(select count(*) c from t_todo_arrange_status dd inner join t_todo_arrange ee 
                 on ee.id=dd.todo_id where dd.created_at is not null and dd.updated_at is not null
                 and (ee.responsible_per=%s or ee.banshi_per=%s)
                )
                c
                from t_todo_arrange a inner join t_user b
                 on a.responsible_per=b.name
                 left join t_user c on a.banshi_per=c.name
                  inner join t_todo_arrange_status d
                   on a.id=d.todo_id
                   where (a.responsible_per=%s or a.banshi_per=%s)
                """,uid_name,uid_name,uid_name,uid_name,uid_name,uid_name,uid_name,uid_name)

            if todo=='1':
                sql='and d.created_at is NULL and d.updated_at is NULL '
            elif todo=='2':
                sql='and d.created_at is not NULL and d.updated_at is NULL '
            elif todo=='3':
                sql='and d.created_at is not NULL and d.updated_at is not NULL '

            count=self.db.get(
                    """
                select count(*) count
                from t_todo_arrange a inner join t_user b
                 on a.responsible_per=b.name
                 left join t_user c on a.banshi_per=c.name
                  inner join t_todo_arrange_status d
                   on a.id=d.todo_id
                   where (a.responsible_per=%s or a.banshi_per=%s) """+sql+""" 
                    order by a.created_at desc""",uid_name,uid_name
                )
            pagination = Pagination(page, pre_page, count.count, self.request)
            startpage = (page - 1) * pre_page
            todo_arranges=self.db.query(
                """
                select a.*,b.phone phone_fz ,b.department_name,c.phone phone_bs,
                 d.created_at bs_created_at,d.updated_at fz_updated_at
                from t_todo_arrange a inner join t_user b
                 on a.responsible_per=b.name
                 left join t_user c on a.banshi_per=c.name
                  inner join t_todo_arrange_status d
                   on a.id=d.todo_id
                   where (a.responsible_per=%s or a.banshi_per=%s) """+sql+""" 
                    order by a.created_at desc limit %s,%s """,uid_name,uid_name,startpage,pre_page)
            self.render(
                'mobile/transition/todo_list.html',
                todo_arranges=todo_arranges,
                pagination=pagination,
                page1=page,
                nums=nums,
                todo=todo)

        elif tag=="search_todo":
            result=self.get_argument('result','')
            company=self.get_argument('company','')
            bs_area=self.get_argument('bs_area','')
            bs_address=self.get_argument('bs_addr','')
            start_time=self.get_argument('start','')
            end_time=self.get_argument('end','')
            project_name=self.get_argument('project','')
            department_name=self.get_argument('department','')
            fz_name=self.get_argument('fz_per','')
            bs_name=self.get_argument('bs_per','')
            sql=''
            todo_arranges=''
            area_type=''
            departments=''
            pagination=''
            params={
                'bs_address':bs_address,
                'bs_area':bs_area,
                'fz_name':fz_name,
                'bs_name':bs_name,
                'department_name':department_name,
                'company':company,
                'start_time':start_time,
                'end_time':end_time,
                'project_name':project_name
            }
            nums=self.db.get(
                """
                select count(*) count, 
                 (select count(*) c from t_todo_arrange_status aa inner join t_todo_arrange aa1
                  on aa.todo_id=aa1.id where aa.created_at is  null and aa.updated_at is null
                  and (aa1.responsible_per=%s or aa1.banshi_per=%s)) a,
                (select count(*) c from t_todo_arrange_status bb inner join t_todo_arrange cc 
                 on bb.todo_id=cc.id
                where bb.created_at is not null and bb.updated_at is null
                 and (cc.responsible_per=%s or cc.banshi_per=%s)
                )
                b,(select count(*) c from t_todo_arrange_status dd inner join t_todo_arrange ee 
                 on ee.id=dd.todo_id where dd.created_at is not null and dd.updated_at is not null
                 and (ee.responsible_per=%s or ee.banshi_per=%s)
                )
                c 
                  from t_todo_arrange a inner join t_user b
                 on a.responsible_per=b.name
                 left join t_user c on a.banshi_per=c.name
                  inner join t_todo_arrange_status d
                   on a.id=d.todo_id
                   where (a.responsible_per=%s or a.banshi_per=%s)
                """,uid_name,uid_name,uid_name,uid_name,uid_name,uid_name,uid_name,uid_name)
            if result:
                if bs_area:
                    sql+=' and a.bs_area="%s"'%bs_area
                if bs_address:
                    sql+=' and a.bs_address like "%%'+bs_address+'%%"'
                if fz_name:
                    sql+=' and a.responsible_per="%s"'%fz_name
                if bs_name:
                    sql+=' and a.banshi_per="%s"'%bs_name
                if department_name:
                    sql+=' and b.department_name="%s"'%department_name
                if project_name:
                    sql+=' and a.project_name like "%%'+project_name+'%%"'
                if company:
                    sql+=' and a.company like "%%'+company+'%%"'
                if start_time and end_time:
                    sql+=' and a.bl_date between "%s" and "%s"'%(start_time,end_time)

                count=self.db.get(
                    """
                    select count(*) count
                    from t_todo_arrange a inner join t_user b
                    on a.responsible_per=b.name
                    left join t_user c on a.banshi_per=c.name
                    inner join t_todo_arrange_status d
                    on a.id=d.todo_id where (a.responsible_per=%s or a.banshi_per=%s) """+sql+"""
                     order by a.created_at desc""",uid_name,uid_name)
                pagination = Pagination(page, pre_page, count.count, self.request)
                startpage = (page - 1) * pre_page
                todo_arranges=self.db.query(
                    """
                    select a.*,b.phone phone_fz ,b.department_name,c.phone phone_bs,
                    d.created_at bs_created_at,d.updated_at fz_updated_at
                    from t_todo_arrange a inner join t_user b
                    on a.responsible_per=b.name
                    left join t_user c on a.banshi_per=c.name
                    inner join t_todo_arrange_status d
                    on a.id=d.todo_id where (a.responsible_per=%s or a.banshi_per=%s) """+sql+"""
                    order by a.created_at desc limit %s,%s""",uid_name,uid_name,startpage,pre_page)

            else:
                departments=self.db.query(
                """
                select name from t_user_department where parent_id=0
                """)

                area_type=self.db.query(
                """
                select income_name from t_projects_type where income_category='区域'
                """)

            self.render(
                "mobile/transition/search_todo.html",
                tag=tag,
                page1=page,
                pagination=pagination,
                result=result,
                params=params,
                nums=nums,
                area_type=area_type,
                departments=departments,
                todo_arranges=todo_arranges)

    @tornado.web.authenticated
    def post(self):
        tag = self.get_argument("tag")
        uid = self.get_secure_cookie("uid")
        dt_now=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        if tag =="confirm_rec":
            pt_id = self.get_argument("pt_id")
            project_id = self.get_argument("project_id")
            print "pt_id", pt_id, "project_id", project_id
            if not pt_id:
                self.write("not pt_id")
            else:
                result = self.db.execute("""
                    update t_projects_transition set 
                    rec_by_uid_at=%s where id=%s and project_id=%s
                """, dt_now,pt_id,project_id)

                self.write(str(result))

        elif tag == 'delete_tran':
            transition_id = self.get_argument('transition_id')
            project_id = self.get_argument('project_id')

            if not id:
                self.write("transition_id is null")
            elif not project_id:
                self.write("project is null")
            else:
                result = self.db.execute('''
                    delete from t_projects_transition where id=%s and project_id=%s
                    ''', transition_id, project_id)
                self.write(str(result))


class UploadPic(BaseHandler):
    @tornado.web.authenticated
    def get(self):
        error=self.get_argument('error','')
        self.render('mobile/uploadpic.html',error=error)

    @tornado.web.authenticated
    def post(self):
        tag = self.get_argument("tag", "")
        if tag=='add_pic':
            transition_id=self.get_argument('trans_id')
            is_upload = False
            try:
                file1 = self.request.files.get('uploaderInput')
                file1=file1[0]
                is_upload = True
            except:

                pass
            if is_upload:
                ori_filename = file1["filename"]
                filename_full = options.upload_path + "/customer/tran_%s/" % (
                        transition_id)
                url_path = "/static/customer/tran_%s/" % (transition_id)
                try:
                    os.makedirs(filename_full)
                except OSError:
                    if not os.path.isdir(filename_full):
                        raise
                extension = os.path.splitext(ori_filename)[1]

                uuid_str = str(uuid.uuid4())
                fname = "{0}_{1}{2}".format(uuid_str, transition_id,
                                                extension)

                save_full_path = filename_full + fname
                url_fname = "{0}{1}".format(url_path, fname)

                output_file = open(save_full_path, 'w')
                output_file.write(file1["body"])
                file_path = url_fname
                self.db.execute("""
                            update t_projects_transition set      
                                `file_name`=%s where id=%s
                        """,file_path,transition_id)
                self.redirect('/uploadpic')
            else:
                self.redirect('/uploadpic?error=-1')


class TransitionUploadHandler(BaseHandler):
    @tornado.web.authenticated
    def post(self):
        tag = self.get_argument("tag", "list")
        uid = self.get_secure_cookie("uid")
        uid_name = self.get_secure_cookie("name")
        result = -10
        if tag == 'add_pic':
            transition_id = self.get_argument('trans_id')
            is_upload = False
            try:
                file1 = self.request.files['file'][0]
                is_upload = True
            except:

                pass
            if is_upload:
                ori_filename = file1["filename"]
                filename_full = options.upload_path + "/customer/tran_%s/" % (
                    transition_id)
                url_path = "/static/customer/tran_%s/" % (transition_id)
                try:
                    os.makedirs(filename_full)
                except OSError:
                    if not os.path.isdir(filename_full):
                        raise
                extension = os.path.splitext(ori_filename)[1]

                uuid_str = str(uuid.uuid4())
                fname = "{0}_{1}{2}".format(uuid_str, transition_id, extension)

                save_full_path = filename_full + fname
                url_fname = "{0}{1}".format(url_path, fname)

                output_file = open(save_full_path, 'w')
                output_file.write(file1["body"])
                file_path = url_fname
                self.db.execute("""
                            update t_transition set      
                                `file_name`=%s where id=%s
                        """, file_path, transition_id)
            else:
                self.write('-1')


#客户管理系统
class CustomerTransitionHandler(BaseHandler):
    @tornado.web.authenticated
    def post(self):
        tag = self.get_argument("tag", "list")
        uid = self.get_secure_cookie("uid")
        uid_name = self.get_secure_cookie("name")
        dt=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        result = -10
        if tag == "add":
            tran_at = self.get_argument("tran_at")
            customer_id = self.get_argument("customer_id")
            rec_by = self.get_argument("rec_by")
            remark = self.get_argument("remark", "")
            tran_by = self.get_argument("tran_by")
            transition_id = int(self.get_argument("transition_id", 0))
            txt=''
            file_path = None
            if not rec_by:
                self.write("接收方的名字不能为空")
            elif not customer_id:
                self.write("not customer_id")
            else:
                is_upload = False
                try:
                    file1 = self.request.files['file'][0]
                    is_upload = True
                except:
                    pass
                if is_upload:
                    ori_filename = file1["filename"]
                    filename_full = options.upload_path + "/customer/%s/" % (
                        customer_id)
                    url_path = "/static/customer/%s/" % (customer_id)
                    try:
                        os.makedirs(filename_full)
                    except OSError:
                        if not os.path.isdir(filename_full):
                            raise
                    extension = os.path.splitext(ori_filename)[1]

                    uuid_str = str(uuid.uuid4())
                    fname = "{0}_{1}{2}".format(uuid_str, customer_id,
                                                extension)

                    save_full_path = filename_full + fname
                    url_fname = "{0}{1}".format(url_path, fname)

                    output_file = open(save_full_path, 'w')
                    output_file.write(file1["body"])
                    file_path = url_fname
                if transition_id:
                    t_transition=self.db_customer.get(' select * from t_transition where id=%s ',transition_id)
                    result = self.db_customer.execute("""
                        update t_transition set 
                            `remark`=%s,
                            `file_name`=%s,
                            `tran_by`=%s,
                            `rec_by`=%s,
                            `tran_at`=%s,
                            uid=%s,
                            uid_name=%s where id=%s
                    """, remark, file_path, tran_by, rec_by, tran_at, uid,
                                             uid_name, transition_id)
                    if t_transition.tran_by!=tran_by:
                        txt+=',移交方:'+t_transition.tran_by+' 修改为 '+tran_by
                    if t_transition.rec_by!=rec_by:
                        txt+=',签收方:'+t_transition.rec_by+' 修改为 '+rec_by
                    if str(t_transition.tran_at.strftime('%Y-%m-%d'))!=tran_at:
                        txt+=',交接时间:'+str(t_transition.tran_at.strftime('%Y-%m-%d'))+' 修改为 '+tran_at
                    if t_transition.remark!=remark:
                        txt+=',备注:',t_transition.remark+' 修改为 '+remark
                    if txt:
                        events.add_project_event(self,'0','修改交接资料',txt[1:],uid,uid_name,customer_id)
                else:
                    result = self.db_customer.execute("""
                            INSERT INTO `t_transition`
                            (customer_id,
                            `remark`,
                            `file_name`,
                            `guid`,
                            `created_at`,
                            `tran_by`,
                            `rec_by`,
                            `tran_at`,uid,uid_name)
                            VALUES
                            (%s,
                                %s,
                                %s,
                            uuid(),
                            %s,
                            %s,
                            %s,
                            %s,%s,%s);
                    """, customer_id, remark, file_path,dt, tran_by, rec_by,
                                             tran_at, uid, uid_name)
                    if result>0:
                        txt='移交方:'+tran_by+',签收方:'+rec_by+',交接时间:'+tran_at+',备注:'+remark
                        events.add_project_event(self,'0','增加交接资料',txt,uid,uid_name,customer_id)
                self.write(str(result))

        elif tag == "delete":
            id = self.get_argument("transition_id")
            customer_id = self.get_argument("customer_id")

            if not id:
                self.write("id")
            else:
                result = self.db_customer.execute(
                    "delete from t_transition where id=%s and customer_id=%s",
                    id, customer_id)
                events.add_project_event(self,'0','删除交接资料','删除id为'+id+'交接资料',uid,uid_name,customer_id)
                self.write(str(result))


class CustomerUploadPic(BaseHandler):
    @tornado.web.authenticated
    def get(self):
        error = self.get_argument('error', '')
        self.render('mobile/uploadpic.html', error=error)

    @tornado.web.authenticated
    def post(self):
        tag = self.get_argument("tag", "")
        if tag == 'add_pic':
            transition_id = self.get_argument('trans_id')
            is_upload = False
            try:
                file1 = self.request.files.get('uploaderInput')
                file1 = file1[0]
                print(file1)
                is_upload = True
            except:

                pass
            if is_upload:
                ori_filename = file1["filename"]
                filename_full = options.upload_path + "/customer/tran_%s/" % (
                    transition_id)
                url_path = "/static/customer/tran_%s/" % (transition_id)
                try:
                    os.makedirs(filename_full)
                except OSError:
                    if not os.path.isdir(filename_full):
                        raise
                extension = os.path.splitext(ori_filename)[1]

                uuid_str = str(uuid.uuid4())
                fname = "{0}_{1}{2}".format(uuid_str, transition_id, extension)

                save_full_path = filename_full + fname
                url_fname = "{0}{1}".format(url_path, fname)

                output_file = open(save_full_path, 'w')
                output_file.write(file1["body"])
                file_path = url_fname
                self.db_customer.execute("""
                            update t_transition set      
                                `file_name`=%s where id=%s
                        """, file_path, transition_id)
                self.redirect('/uploadpic')
            else:
                self.redirect('/uploadpic?error=-1')
