# -*- coding: utf-8 -*-
import datetime
import json
import os
import sys
import uuid
from tornado.web import asynchronous, RequestHandler, Application
import qrcode
import tornado
import xlwt, hashlib
from tornado.options import define, options
import events
import msg
from handlers.base import BaseHandler
from Pagination import Pagination
import re
reload(sys)
sys.setdefaultencoding('utf-8')

class ProjectHandler(BaseHandler):
    def get_member(self,mbs,team_name):
        return_s = ""
        if mbs:
            for r in mbs.split(","):
                if r:
                    mb = r.split("|")
                    if mb[0]==team_name :
                        if mb[1] in return_s:
                            continue
                        if return_s :
                            return_s +=","
                        return_s+= mb[1]
                        

        return return_s
    def diff_date(self, dt1,project_id):
        if project_id:
            t_projects_logoff = self.db.get("select datediff(now(),finish_at) aa,finish_at from t_projects_logoff where type_id=1 and state_id=2 and   project_id=%s",project_id)
            t_projects_logoff1 = self.db.get("select datediff(now(),finish_at) aa,finish_at from t_projects_logoff where type_id=2 and state_id=2 and   project_id=%s",project_id)
 
            if  t_projects_logoff1 and t_projects_logoff:
                return "<span class='badge badge-pill badge-info'  style='font-size:13px;' >(执照银行完结)</span>".format((t_projects_logoff1.finish_at-t_projects_logoff.finish_at).days)
            elif t_projects_logoff:
                return "<span  class='badge badge-pill badge-success'  style='font-size:13px;'  >登报{}天</span>".format(t_projects_logoff.aa)

            else:
                return "<span class='badge badge-pill badge-danger'  style='font-size:13px;' >未登报</span>"

    def write_income(self,val,id):
        #  print "bs", val, "id", id,type(id)
        if val:
            for b in val.split(","):
                if b:
                    row = b.split("|")

                    if int(row[0]) == id:

                        return float(row[1])
        return 0

    def setCheckbox(self,val,id):
        if val:
            #   print "val", val, id
            for item in val.split(","):
                if item:
                    if int(item) ==id:
                        return True
        return False

    def getMemberNameByType(self,items,val):
        if items:
            for item in items:
                # print type(item["team_name"]),type(val.decode("utf8"))
                if item["team_name"] == val.decode("utf8"):
                    # print item["team_name"], item["member_name"]
                    return u"<span>%s: %s</span><span>时间:%s</span>" % (item["team_name"],

                        item["member_name"],
                        item["created_at"].strftime("%Y-%m-%d"))

        return "<span>%s: </span><span>时间:20  -  -  </span>" % (val)

    def getMemberName(self, items, val):
        if items:
            for item in items:
                if item["team_name"] == val.decode("utf8"):
                    return item["member_name"]
        return ""

    def getMemberId(self, items, val):
        if items:
            for item in items:
                if item["team_name"] == val.decode("utf8"):
                    return item["member_id"]
        return "0"


    def getMemberIdInProject(self, items, val,mid):
        if items:
            for item in items:

                if item["team_name"] == val.decode("utf8") :
                    if item["member_id"] ==int(mid):
                        return item["member_id"]
        return "0"


    def getMemberNameCQ(self, items, val):
        return_str = ""
        if items:

            for item in items:
                if item["team_name"] == val.decode(
                        "utf8") and item["team_id"] == 38:
                    return_str=return_str+ u"{0} {1} <br/>".format(
                        item["member_name"],
                        item["created_at"].strftime("%Y-%m-%d"))
        return return_str

    def getMemberNameCQ1(self, items, val):
        return_str = ""
        if items:
            return_str = ""
            for item in items:
                if item["team_name"] == val.decode(
                        "utf8") and item["team_id"] == 38:
                    return_str = return_str + u"{0}&nbsp;".format(
                        item["member_name"]
                      )
        return return_str

    def getFile(self, item, val):
        if item:
            if u"身份证1" == item.file_type_name:
                if not item['id_number']:
                    item['id_number'] = "_______________________"
                if not item["origin_num"]:
                    item["origin_num"] = "__"
                if not item["print_num"]:
                    item["print_num"] = "__"
                return u"""<span>01)&nbsp;&nbsp;身份证 %s
                            原件%s份、复印件%s份;</span>""" % (item['id_number'],
                                                       item["origin_num"],
                                                       item["print_num"])

            elif u"身份证2" == item["file_type_name"]:

                if not  item['id_number']:
                    item['id_number'] = "_______________________"
                if not item["origin_num"]:
                    item["origin_num"] = "__"
                if not item["print_num"]:
                    item["print_num"] = "__"

                return u"""<span>03)&nbsp;&nbsp;身份证 %s
                            原件%s份、复印件%s份;</span>""" % (item['id_number'],
                                                       item["origin_num"],
                                                       item["print_num"])
            elif u"营业执照" == item["file_type_name"]:
                # 正本副本复印件
                origin_num = None
                rec_num  = None
                print_num = None
                if item["origin_num"]:
                    origin_num = "checked"
                if item["print_num"]:
                    print_num = "checked"
                if item["rec_num"]:
                    rec_num = "checked"


                return u"""<span>02)%s &nbsp;&nbsp;<input type="checkbox"
                    %s>正本&nbsp;&nbsp;<input type="checkbox"  %s>副本&nbsp;&nbsp;<input type="checkbox" disabled %s>复印件</span>""" % (
                    item["file_type_name"], rec_num, origin_num, print_num)

            elif u"租赁合同" == item["file_type_name"]:
                # 正本副本复印件
                origin_num = None
                rec_num = None
                print_num = None
                if item["origin_num"]:
                    origin_num = "checked"
                if item["print_num"]:
                    print_num = "checked"
                if item["rec_num"]:
                    rec_num = "checked"

                return u"""<span>04)%s &nbsp;&nbsp;<input type="checkbox"
                    %s>正本&nbsp;&nbsp;<input type="checkbox"  %s>副本&nbsp;&nbsp;<input type="checkbox" disabled %s>复印件</span>""" % (
                    item["file_type_name"], rec_num, origin_num, print_num)

            elif u"房产证" == item["file_type_name"]:
                # 正本副本复印件
                origin_num = None
                rec_num = None
                print_num = None
                if item["origin_num"]:
                    origin_num = "checked"
                if item["print_num"]:
                    print_num = "checked"

                return u"""<span>05)%s&nbsp;&nbsp; <input type="checkbox" disabled  %s>原件&nbsp;&nbsp;<input type="checkbox" disabled %s>复印件</span>""" % (
                    item["file_type_name"], origin_num, print_num)

            elif u"房屋租赁证明" == item["file_type_name"]:
                # 正本副本复印件
                origin_num = None
                rec_num = None
                print_num = None
                if item["origin_num"]:
                    origin_num = "checked"
                if item["print_num"]:
                    print_num = "checked"

                return u"""<span>06)%s &nbsp;&nbsp; <input type="checkbox" disabled %s>原件&nbsp;&nbsp;<input type="checkbox" disabled  %s>复印件</span>""" % (
                    item["file_type_name"], origin_num, print_num)

            elif u"经营场所场地使用证明" == item["file_type_name"]:
                # 正本副本复印件
                origin_num = None
                rec_num = None
                print_num = None
                if item["origin_num"]:
                    origin_num = "checked"
                if item["print_num"]:
                    print_num = "checked"

                return u"""<span>07)%s&nbsp;&nbsp; <input type="checkbox" disabled  %s>原件&nbsp;&nbsp;<input type="checkbox" disabled %s>复印件</span>""" % (
                    item["file_type_name"], origin_num, print_num)

            elif u"公章" == item["file_type_name"]:
                # 公章
                if item['chop_num']==0:
                    item['chop_num'] ="__"


                return u"""&nbsp;&nbsp;<span>08)%s&nbsp; %s 枚</span>""" % (
                    item["file_type_name"], item["chop_num"])
            elif u"信息采集表" == item["file_type_name"]:
                # 信息采集表
                info_num = None
                if item["info_num"]:
                    info_num = "checked"


                return u"""&nbsp;&nbsp;<span>09)&nbsp;&nbsp;%s <input type="checkbox" disabled %s></span>""" % (
                    item["file_type_name"], info_num)

#02)&nbsp;营业执照&nbsp;&nbsp;&nbsp;&nbsp; <input type="checkbox">正本&nbsp;&nbsp;<input type="checkbox">&nbsp;&nbsp;<input type="checkbox">

        return ""


    def rmb_convert(self,n):
        units = ['', '万', '亿']
        nums = ['零', '壹', '贰', '叁', '肆', '伍', '陆', '柒', '捌', '玖']
        decimal_label = ['角', '分']
        small_int_label = ['', '拾', '佰', '仟']
        int_part, decimal_part = str(int(n)), str(n - int(n))[2:]  # 分离整数和小数部分

        res = []
        if decimal_part:
            res.append(''.join([
                nums[int(x)] + y for x, y in zip(decimal_part, decimal_label)
                if x != '0'
            ]))

        if int_part != '0':
            res.append('圆')
            while int_part:
                small_int_part, int_part = int_part[-4:], int_part[:-4]
                tmp = ''.join([
                    nums[int(x)] + (y if x != '0' else '')
                    for x, y in zip(small_int_part[::-1], small_int_label)[::-1]
                ])
                tmp = tmp.rstrip('零').replace('零零零', '零').replace('零零', '零')
                unit = units.pop(0)
                if tmp:
                    tmp += unit
                    res.append(tmp)
        return ''.join(res[::-1])

    def set_statis(self, project_id, str, dt):
        t_project = self.db.get("""
        select a.*,b.last_milepost_id from t_projects a
        left join t_projects_member b on a.id=b.project_id
        and  b.btype_id <> 0 and b.last_milepost_id=151 where id=%s""",project_id)
        statis = self.db.get("select * from t_statis where project_id =%s",project_id)
        if not statis:
            if t_project.last_milepost_id==151:
                self.db.execute("""
                    INSERT INTO `t_statis` ( `project_id`,customer_id, `btype`,  `start_date`,
                     `set_cq_day_date`, `req_day_date`, `check_name_day_date`, `addr_day_date`, `in_day_date`,
                     `get_day_date`, `kez_day_date`, `openaccount_day_date`, `endtime_day_date`, `updated_at`,
                     `is_close`,cq_uid_name,cq_uid,company,range_day_date,project_guid,get_openaccount_day_date)
                    VALUES
                        ( %s,0, 1,%s, NULL, NULL,NULL, NULL, NULL, NULL,NULL,NULL, NULL, now(), 0,NULL,0,NULL,NULL,NULL,%s);
                    """,t_project.id,t_project.created_at,datetime.datetime.now())
            else:
                self.db.execute("""
                    INSERT INTO `t_statis` ( `project_id`,customer_id, `btype`,  `start_date`,
                     `set_cq_day_date`, `req_day_date`, `check_name_day_date`, `addr_day_date`, `in_day_date`,
                     `get_day_date`, `kez_day_date`, `openaccount_day_date`, `endtime_day_date`, `updated_at`,
                     `is_close`,cq_uid_name,cq_uid,company,range_day_date,project_guid,get_openaccount_day_date)
                    VALUES
                        ( %s,0, 1,%s, NULL, NULL,NULL, NULL, NULL, NULL,NULL,NULL, NULL, now(), 0,NULL,0,NULL,NULL,NULL,NULL);
                    """,t_project.id,t_project.created_at)
        addsql =""
        if str == u"领取核名":  # check_name_item
            addsql = " check_name_day_date=%s"
        elif str == u"勾选经营范围":
            addsql = "range_day_date =%s"
        elif str == u"领取核名":
            addsql = "req_day_date =%s"
        elif str == u"执照受理":  # in_day_date
            addsql = " in_day_date =%s"
        elif str == u"领取执照":
            addsql = " get_day_date =%s"
        elif str == u"刻章备案":
            addsql = " kez_day_date =%s"
        elif str == u"银行开户":
            addsql = "openaccount_day_date =%s"
        elif str == u"领取基本户":
            addsql = "get_openaccount_day_date =%s"
        if addsql:
            if not  dt:
                last_statis = self.db.get("""
                    select created_at from t_projects_state_msg where
                 project_id=%s and state_id_name=%s
                 order by created_at desc
                 limit 1
                """,project_id,str)
                if last_statis:
                    dt = last_statis.created_at
            self.db.execute("""
                update t_statis set
                  """ + addsql + """
                where project_id=%s
                    """, dt,project_id)

    def get_filename_uuid4(self,filepath):
        pattern=re.compile(r'^[a-z0-9]+-[a-z0-9]+-[a-z0-9]+-[a-z0-9]+-[a-z0-9]+_')
        return pattern.sub('',filepath)

    @tornado.web.authenticated
    def get(self):
        dt = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        tag = self.get_argument("tag","my")
        uid = self.get_secure_cookie("uid")
        role = self.get_secure_cookie("role")
        uid_name = self.get_secure_cookie("name")
        is_check=self.get_secure_cookie('is_check')
        is_manager=self.get_secure_cookie('is_manager')
        kj_manage=self.get_secure_cookie('kj_manage')

        if self.get_secure_cookie('role_list'):
            role_list=self.get_secure_cookie('role_list').split(',')
        else:
            role_list=[]
        if tag=="get_trans_count":
            tcount = self.db.get("select count(*) c from t_projects_transition a ,t_projects b  where a.project_id=b.id and  rec_by_uid=%s and rec_by_uid_at is null",uid)
            return self.write(str(tcount.c))
        elif tag=='get_project_reject':
            step='1'
            txt='反馈'
            tcount=self.db.get(''' select count(*) count from t_projects_information_reject where handler_uid=%s 
            and handler_at is null ''',uid)
            if tcount.count==0:
                tcount=self.db.get(''' select count(*) count from t_projects_information_reject where handler_uid=%s 
            and confirm_at is not null and confirm_status=2 ''',uid)
                step='4'
                txt='驳回'

            return self.write({'c':str(tcount.count),'step':step,'txt':txt})

        elif tag=='get_trans_daijie_count':
            t_project=self.db.get('''
            SELECT  count(*) count, team_id
                     FROM t_projects
                    a inner join t_projects_member b on a.id=b.project_id and not_transition=0
                    
and btype_id > 0
                    where  is_cancel=0  and b.btype_id > 0   and last_milepost_id=167 and member_id=%s group by team_id
            ''',uid)
            if t_project:
                if role=='10':
                    url='/project?tag=projects_qc_milepost&last_milepost_id=167&from_tag_where=1'
                elif role=='9':
                    url='/project?tag=projects_qc_milepost&last_milepost_id=167'
                elif role=='7':
                    url='/project?tag=projects_state&last_milepost_id=167'
                elif role=='1' or role=='13':
                    url='/project?tag=projects_yw&last_milepost_id=167'
                return self.write({'count':t_project.count,'team_id':t_project.team_id,'url':url})

        elif tag=="project_logoff_list":
            page=int(self.get_argument('page',1))
            state_id=self.get_argument('state_id',"")
            start = self.get_argument("start","")
            end = self.get_argument("end","")
            member_id = self.get_argument("member_id", "")
            key=self.get_argument("key",'')
            count_type=self.get_argument('count_type','')
            type_id=self.get_argument('type_id','')
            count_way=self.get_argument('count_way','')
            output = self.get_argument("output",'')
            params={
                "end":end,
                "start":start,
                "state_id":state_id,
                "member_id":member_id,
                "key":key,
                'count_type':count_type,
                'count_way':count_way,
                'type_id':type_id}
            if count_type=='day':
                way_sql=" '%%Y-%%m-%%d' "
            elif count_type=='month':
                way_sql=" '%%Y-%%m' "
            elif count_type=='week':
                way_sql=" '%%Y-%%m-%%u' "
            pre_page = 20
            state_id_sql = ""
            count_sql=''
            sql_limit =""
            if state_id:
                state_id_sql = " and state_id=%s "%(state_id)
            if start and end :
                state_id_sql += " and finish_at between '%s' and '%s' "%(start,end)
            if member_id:
                state_id_sql += " and a.uid=%s "%(member_id)
            if type_id:
                state_id_sql+=' and type_id=%s '%type_id
            if key:
                id_sql=''
                if key.isdigit():
                    id_sql=' a.id=%s or'%key

                state_id_sql+="""
                    and ( """+id_sql+""" c.project_name like "%%"""+key+"""%%"
                    or c.customer_name='"""+key+"""' or  c.customer_company like "%%"""+key+"""%%" )
                """
            if role=='9':
                state_id_sql+=' and b.member_id=%s '%uid
                count_sql=' and aa.uid=%s '%uid
            if count_way:
                if count_way=='project':
                    gb_sql='a.uid_name'
                elif count_way=='gs':
                    gb_sql='a.type_id_name'
                count=self.db.get('''
                  select count(*) count,sum(sc) ssc,

                  (select group_concat(name_or_type,'|',count) gc from  (
                      select '''+gb_sql+''' name_or_type ,count(*) count from t_projects_logoff a

            inner  join  t_projects_member  b on a.mid=b.mid
            inner join t_projects c on c.id = a.project_id  where state_id=2 '''+state_id_sql+'''
				group by '''+gb_sql+'''
                  ) aa order by count desc)every_count
                from ( 
                select df,group_concat(name_or_type,'|',count) ,sum(count) sc from
                (select  count(*) count,'''+gb_sql+''' name_or_type,date_format(finish_at,'''+way_sql+''') df
                            from t_projects_logoff a

            inner  join  t_projects_member  b on a.mid=b.mid
            inner join t_projects c on c.id = a.project_id  where state_id=2 '''+state_id_sql+'''
				group by df,'''+gb_sql+'''
                       )aa group by df) aaa   
                ''')
                pagination = Pagination(page, pre_page, count.count, self.request)
                startpage = (page - 1) * pre_page

                if not output:
                    sql_limit = "limit %s,%s"%(startpage,pre_page)
                t_projects_logoff=self.db.query('''
                select df,group_concat(name_or_type,'|',count) gc,sum(count) sc from
 (select  count(*) count,'''+gb_sql+''' name_or_type,date_format(finish_at,'''+way_sql+''') df
            from t_projects_logoff a

            inner  join  t_projects_member  b on a.mid=b.mid
            inner join t_projects c on c.id = a.project_id  where state_id=2 '''+state_id_sql+'''
				group by df,'''+gb_sql+'''
                       )aa group by df  order
             by df desc
                '''+sql_limit)
      
            else:


                count = self.db.get('''
                select count(*) count
                    from t_projects_logoff a

                    inner  join  t_projects_member  b on a.mid=b.mid
                    inner join t_projects c on c.id = a.project_id  where 0=0
                ''' + state_id_sql)

                pagination = Pagination(page, pre_page, count.count, self.request)
                startpage = (page - 1) * pre_page
                if not output:
                    sql_limit = "limit %s,%s"%(startpage,pre_page)                
                t_projects_logoff = self.db.query('''
            select  a.*,c.guid project_guid,
                c.project_name,c.customer_name,c.customer_company,c.all_income
                from t_projects_logoff a

                inner  join  t_projects_member  b on a.mid=b.mid
                inner join t_projects c on c.id = a.project_id  where 0=0 ''' + state_id_sql + '''
                            order
                by finish_at desc 
                '''+sql_limit)
            logoff_type = self.db.query("""select a.*, (select count(*) cc from t_projects_logoff aa inner  join  t_projects_member  bb on aa.mid=bb.mid
            inner join t_projects cc on cc.id = aa.project_id  where aa.state_id=a.order_int """+count_sql+""")  cc from t_projects_type a where   income_category='注销审核'""")
            if  count_way=='project':
                t_logoff_type_gs=self.db.query(" SELECT * FROM t_projects_type where income_category='注销' ")
            else:
                t_logoff_type_gs=self.db.query(' select uid,uid_name from t_projects_logoff group by uid,uid_name ')
            t_projects_logoff_members = self.db.query('''
                    select  uid,uid_name
            from t_projects_logoff
                      group by uid,uid_name
                        ''',)
            if output:
                    wb = xlwt.Workbook()
                    # 新增一个表单
                    sh = wb.add_sheet(u'注销部办结')
                    sh.write(0, 0, u"编号")
                    sh.write(0, 1, u"业务名称")
                    sh.write(0, 2, u"公司名称")
                    sh.write(0, 3 , u"客户名称")
                    sh.write(0, 4, u"跟进人")
                    sh.write(0,5,u"总服务费")
                    sh.write(0, 6, u"办结时间")
                    sh.write(0, 7, u"办结业务")
                    for idx, item in enumerate(t_projects_logoff):
                        idx= idx+1
                        sh.write(idx, 0, item.id)
                        sh.write(idx, 1, item.project_name)
                        sh.write(idx, 2, item.customer_company)
                        sh.write(idx, 3 , item.customer_name)
                        sh.write(idx, 4, item.uid_name)
                        sh.write(idx, 5, item.all_income if item.all_income else 0)
                        sh.write(idx,6, item.finish_at.strftime("%Y-%m-%d"))
                        sh.write(idx,7, item.type_id_name)
                     
                    wb.save('media/output/logout_%s.xls'%(uid))
                    return self.redirect("/static/output/logout_%s.xls"%(uid))
            self.render('project/project_logoff_list.html',
                search_key="",
                tag=tag,
                t_projects_logoff=t_projects_logoff,
                pagination=pagination,
                logoff_type=logoff_type,
                state_id=state_id,
                params=params,
                t_projects_logoff_members=t_projects_logoff_members,
                t_logoff_type_gs=t_logoff_type_gs,
                count=count
                )
        elif tag =="print":
            guid = self.get_argument("project_guid")
            id = self.get_argument("project_id")
            title_id = self.get_argument("title_id")
            t_project = self.db.get(
                """select a.*,b.income_name contract_sign_type_name,c.name uid_name
                 from t_projects a, t_projects_type b,
                t_user c
                 where   a.uid=c.id and  a.contract_sign_type_id=b.id and  a.id=%s and a.guid=%s""",
                id, guid)



            t_project_note=self.db.query("""
                select * from t_projects_note where project_id=%s and  is_add_to_print=1
            """,id)
            t_project_members = self.db.query(
                """select a.*,b.name from t_projects_member a , t_user b  where a.member_id=b.id
                 and  project_id=%s order by created_at desc""",
                id)


            t_projects_members_bfrom = self.db.get(
                "select * from t_projects_member where project_id=%s and team_id='39'", id)

            t_project_income_title = self.db.get(
                "select * from t_projects_income_title where id=%s",
                title_id)
            t_project_income = self.db.query(
                """select a.*,b.pay_type_name,b.income_at income_at_a  from t_projects_income a
                ,t_projects_income_title b
                where a.parent_id=b.id  and  a.project_id=%s and
                  parent_id <=%s and income_uid > 0 order by created_at desc
            """, id, title_id)

            t_project_income_wait = self.db.get("""
                        select (
                        select ifnull(sum(income_money),0)  income_money from t_projects_income a
                                        ,t_projects_income_title b
                                        where a.parent_id=b.id  and  a.project_id={1} and
                                        parent_id <={0} and income_uid > 0 and income_id =40) aa ,
                        (
                        select ifnull(sum(income_money),0)  income_money from t_projects_income a
                                        ,t_projects_income_title b
                                        where a.parent_id=b.id  and  a.project_id={1} and
                                        parent_id <={0} and income_uid > 0 and income_id =43) bb     ,

                                            (
                        select ifnull(sum(income_money),0)  income_money from t_projects_income a
                                        ,t_projects_income_title b
                                        where a.parent_id=b.id  and  a.project_id={1} and
                                        parent_id <={0} and income_uid > 0 and income_id >43) cc,

                        (select ifnull(sum(income_money),0)  income_money from t_projects_income a
                                        ,t_projects_income_title b
                                        where a.parent_id=b.id  and  a.project_id={1} and
                                        parent_id <={0} and income_uid > 0 and income_id <=43) dd


            """.format(title_id, id))

            return self.render(
                "print.html",
                t_project_note=t_project_note,
                t_project_income_wait=t_project_income_wait,
                t_project_income_title=t_project_income_title,
                getFile=self.getFile,
                t_projects_members_bfrom=t_projects_members_bfrom,
                getMemberNameCQ=self.getMemberNameCQ,
                getMemberName=self.getMemberName,
                getMemberNameByType=self.getMemberNameByType,
                t_project=t_project,
                form_tag="print",
                t_project_members=t_project_members,
                t_project_income=t_project_income,
                created_at=datetime.datetime.now(),
                search_key="")


        elif tag =="qrcode":
            id = self.get_argument("id")
            guid = self.get_argument("guid")
            qtag = self.get_argument("qtag")
            url =""
            url_path= "1"
            if qtag=="trans":
                trans_id = self.get_argument("trans_id")
                url = "http://8.fayejituan.com:8080/mobile?tag=uploader_trans&id=%s&guid=%s&trans_id=%s" % (
                    id, guid, trans_id)

            if url:

                qr = qrcode.QRCode(
                    version=1,
                    error_correction=qrcode.constants.ERROR_CORRECT_L,
                    box_size=10,
                    border=4,
                )

                qr.add_data(url)
                qr.make(fit=True)

                img = qr.make_image()
                vp = "/qrcode/trans/" +id+guid +'.png'
                img.save(options.upload_path + vp)
                url_path = "/static/qrcode/trans/" + id + guid + '.png'
            self.write("<center><img src='%s' width='300'/></center>" % url_path)


        elif tag=="role_allot":
            role_projects_types=self.db.query(
                """
                select * from t_projects_type where income_category='权限模块'
                """
            )
            not_visible_addr=self.db.query(
                """
                select * from t_user where id not in (select uid from t_user_visible where type_id=
                (select id from t_projects_type where income_name='地址查看')
                )
                """
            )
            not_visible_gy=self.db.query(
                """
                select * from t_user where id not in (select uid from t_user_visible where type_id=
                (select id from t_projects_type where income_name='供应商')
                )
                """
            )
            visible_gy=self.db.query(
                """
                select a.* from t_user a inner join t_user_visible b
                on a.id=b.uid
                where b.type_id=(select id from t_projects_type where income_name='供应商')
                """
            )
            visible_addr=self.db.query(
                """
                select a.* from t_user a inner join t_user_visible b
                on a.id=b.uid
                where b.type_id=(select id from t_projects_type where income_name='地址查看')
                """
            )
            return self.render(
                "project/role_allot.html",
                search_key="",
                role_projects_types=role_projects_types,
                visible_gy=visible_gy,
                visible_addr=visible_addr,
                not_visible_addr=not_visible_addr,
                not_visible_gy=not_visible_gy

            )

        elif tag=="manage_addr":
            id=self.get_argument('id')
            project_manage_addr=self.db.query(
                """
                select * from t_projects_addr where project_id=%s
                """,id)
            return self.render(
                "project/project_manage_addr.html",
                search_key="",
                project_manage_addr=project_manage_addr,
                project_id=id
                )

        elif tag=='project_recode':
            id=self.get_argument('id')
            project_recode=self.db.query(
                """
                select * from t_projects_recode where project_id=%s
                """,id)
            return self.render(
                "project/project_recode.html",
                search_key="",
                project_recode=project_recode,
                project_id=id
                )

        elif tag=='query_project':
            key=self.get_argument("key")
            project_id=self.get_argument('project_id')
            if not key:
                self.write(u'请输入关键词！')
            else:
                search_project=self.db.get(
                    '''
                    select * from t_projects where id=%s
                    ''',key
                )

                if search_project:
                    if search_project.id==int(project_id):

                        self.write(u'不能查询当前订单！')

                    else:
                        return self.render(
                        "project/project_search1.html",
                        item=search_project,
                        key=key,
                        tag=tag
                        )
                else:
                    self.write(u'没找到订单！')

        elif tag == "print_to_customer_preview":
            guid = self.get_argument("project_guid")
            id = self.get_argument("project_id")
            title_id = self.get_argument("title_id")
            t_project = self.db.get(
                """select a.*,b.income_name contract_sign_type_name,c.name uid_name
                 from t_projects a, t_projects_type b,
                t_user c
                 where   a.uid=c.id and  a.contract_sign_type_id=b.id and  a.id=%s and a.guid=%s""",
                id, guid)

            t_project_members = self.db.query(
                """select a.*,b.name from t_projects_member a , t_user b  where a.member_id=b.id
                 and  project_id=%s order by created_at desc""", id)

            t_projects_members_bfrom = self.db.get(
                "select * from t_projects_member where project_id=%s and team_id='39'",
                id)

            t_project_income_title = self.db.get(
                "select * from t_projects_income_title where id=%s", title_id)
            t_project_income = self.db.query(
                """select a.*,b.pay_type_name,b.income_at income_at_a,b.fi_confirm_at fi_confirm_at  from t_projects_income a
                ,t_projects_income_title b
                where a.parent_id=b.id  and  a.project_id=%s and
                  parent_id <=%s and income_uid > 0 order by created_at desc
            """, id, title_id)

            t_project_income_wait = self.db.get("""
                        select (
                        select ifnull(sum(income_money),0)  income_money from t_projects_income a
                                        ,t_projects_income_title b
                                        where a.parent_id=b.id  and  a.project_id={1} and
                                        parent_id <={0} and income_uid > 0 and income_id =40) aa ,
                        (
                        select ifnull(sum(income_money),0)  income_money from t_projects_income a
                                        ,t_projects_income_title b
                                        where a.parent_id=b.id  and  a.project_id={1} and
                                        parent_id <={0} and income_uid > 0 and income_id =43) bb     ,

                                            (
                        select ifnull(sum(income_money),0)  income_money from t_projects_income a
                                        ,t_projects_income_title b
                                        where a.parent_id=b.id  and  a.project_id={1} and
                                        parent_id <={0} and income_uid > 0 and income_id >43) cc,

                        (select ifnull(sum(income_money),0)  income_money from t_projects_income a
                                        ,t_projects_income_title b
                                        where a.parent_id=b.id  and  a.project_id={1} and
                                        parent_id <={0} and income_uid > 0 and income_id <=43) dd


            """.format(title_id, id))
            income_print = self.db.get(
                "select * from t_projects_income_title_print where project_id=%s and title_id=%s",
                id, title_id)

            return self.render(
                "print_to_customer_preview.html",
                income_print= income_print,
                t_project_income_wait=t_project_income_wait,
                t_project_income_title=t_project_income_title,
                getFile=self.getFile,
                t_projects_members_bfrom=t_projects_members_bfrom,
                getMemberNameCQ=self.getMemberNameCQ,
                getMemberName=self.getMemberName,
                getMemberNameByType=self.getMemberNameByType,
                t_project=t_project,
                form_tag="print",
                t_project_members=t_project_members,
                t_project_income=t_project_income,
                created_at=datetime.datetime.now(),
                search_key="",
                rmb_convert=self.rmb_convert,
                title_id=title_id)
        elif tag == "print_to_customer":
            project_guid = self.get_argument("project_guid")
            id = self.get_argument("project_id")
            title_id = self.get_argument("title_id")
            if not project_guid:
                self.write('not project_guid')
            elif not id:
                self.write("not id")
            elif not title_id:
                self.write("not title_id")
            else:
                t_project = self.db.get(
                    """select a.*,b.income_name contract_sign_type_name,c.name uid_name
                    from t_projects a, t_projects_type b,
                    t_user c
                    where   a.uid=c.id and  a.contract_sign_type_id=b.id and  a.id=%s and a.guid=%s""",
                    id, project_guid)

                t_project_members = self.db.query(
                    """select a.*,b.name from t_projects_member a , t_user b  where a.member_id=b.id
                    and  project_id=%s order by created_at desc""", id)

                t_projects_members_bfrom = self.db.get(
                    "select * from t_projects_member where project_id=%s and team_id='39'",
                    id)

                t_project_income_title = self.db.get(
                    "select * from t_projects_income_title where id=%s", title_id)
                t_project_income = self.db.query(
                    """select a.*,b.pay_type_name,b.income_at income_at_a  from t_projects_income a
                    ,t_projects_income_title b
                    where a.parent_id=b.id  and  a.project_id=%s and
                    parent_id <=%s and income_uid > 0 order by created_at desc
                """, id, title_id)

                t_project_income_wait = self.db.get("""
                            select (
                            select ifnull(sum(income_money),0)  income_money from t_projects_income a
                                            ,t_projects_income_title b
                                            where a.parent_id=b.id  and  a.project_id={1} and
                                            parent_id <={0} and income_uid > 0 and income_id =40) aa ,
                            (
                            select ifnull(sum(income_money),0)  income_money from t_projects_income a
                                            ,t_projects_income_title b
                                            where a.parent_id=b.id  and  a.project_id={1} and
                                            parent_id <={0} and income_uid > 0 and income_id =43) bb     ,

                                                (
                            select ifnull(sum(income_money),0)  income_money from t_projects_income a
                                            ,t_projects_income_title b
                                            where a.parent_id=b.id  and  a.project_id={1} and
                                            parent_id <={0} and income_uid > 0 and income_id >43) cc,

                            (select ifnull(sum(income_money),0)  income_money from t_projects_income a
                                            ,t_projects_income_title b
                                            where a.parent_id=b.id  and  a.project_id={1} and
                                            parent_id <={0} and income_uid > 0 and income_id <=43) dd


                """.format(title_id, id))
                t_income_print = self.db.get(
                    "select * from t_projects_income_title_print where project_id=%s and title_id=%s",id,title_id)
                return self.render(
                    "print_to_customer.html",
                    t_income_print=t_income_print,
                    t_project_income_wait=t_project_income_wait,
                    t_project_income_title=t_project_income_title,
                    getFile=self.getFile,
                    t_projects_members_bfrom=t_projects_members_bfrom,
                    getMemberNameCQ=self.getMemberNameCQ,
                    getMemberName=self.getMemberName,
                    getMemberNameByType=self.getMemberNameByType,
                    t_project=t_project,
                    form_tag="print",
                    t_project_members=t_project_members,
                    t_project_income=t_project_income,
                    created_at=datetime.datetime.now(),
                    search_key="",
                    rmb_convert=self.rmb_convert,
                    title_id=title_id)

        elif tag == "income_detail":
            parent_id = self.get_argument("parent_id")
            if parent_id:
                incomes = self.db.query(
                    "select * from t_projects_income where parent_id=%s", parent_id)
                income_arr = []
                for item in incomes:
                    income_arr.append({
                        "parent_id": item.parent_id,
                        "remark": item.remark,
                        "income_money": str(item.income_money),
                        "income_num": item.income_num,
                        "income_id": item.income_id
                    })
                self.write(
                    tornado.escape.json_encode({
                        "code": len(incomes),
                        "incomes": income_arr
                    }))
        elif tag == "income_detail_by_project":
            project_id = self.get_argument("project_id")
            if project_id:
                incomes = self.db.query(
                    "select * from t_projects_income where project_id=%s",
                    project_id)
                income_arr = []
                for item in incomes:
                    # print "item",item.id
                    income_detail = self.db.query("""select id,title_id, service_id,service_name,service_money
                    from t_projects_income_detail where title_id=%s""",item.parent_id)
                    income_detail_arr = []
                    for row in income_detail:
                        income_detail_arr.append({
                            "detail_id":row.id,
                            "service_money":
                            str(row.service_money),
                            "title_id":
                            row.title_id,
                            "service_id":
                            row.service_id,
                            "service_name":
                            row.service_name
                        })

                    income_arr.append({
                        "income_name":item.income_name,
                        "income_money": str(item.income_money),
                        "income_num": item.income_num,
                        "income_id": item.income_id,
                        "remark": item.remark,
                        "parent_id": item.parent_id,
                        "income_detail":income_detail_arr
                    })
                self.write(
                    tornado.escape.json_encode({
                        "code": 0,
                        "incomes": income_arr
                    }))
        elif tag =="list":

            page= int(self.get_argument("page",1))
            pre_page=20
            count = self.db.get('''SELECT count(*) count FROM t_projects a , t_user b where a.uid=b.id
               ''')
            pagination = Pagination(page, pre_page, count.count, self.request)
            startpage = (page-1) * pre_page
            t_projects = self.db.query('''
                SELECT  a.* , b.name  FROM t_projects a , t_user b where a.uid=b.id
                order by created_at desc limit %s,%s
                ''',startpage,pre_page)
            t_project_bussniss = self.db.query(
                """select * from t_projects_type where income_category='业务类型' """
            )
            return self.render(
                'project/projects.html',
                t_project_bussniss=t_project_bussniss,
                pagination=pagination,
                t_projects=t_projects,
                form_tag=tag,
                search_key="")
        elif tag =="projects_cg":
            category_id = self.get_argument("category_id", "")
            last_milepost_id = self.get_argument("last_milepost_id","")
            false = self.get_argument("false","0")
            page= int(self.get_argument("page",1))
            sales = self.get_argument("sales","")
            cq = self.get_argument("cq", "")
            kefu = self.get_argument("kefu", "")
            building_id = self.get_argument("building_id", "")
            income_bussniss = self.get_argument("income_bussniss", "")
            from_id = self.get_argument("from_id", "")
            start = self.get_argument("start", "")
            end = self.get_argument("end", "")
            sales = self.get_argument("sales", "")
            qc_key = self.get_argument("qc_key","")
            ntag=self.get_argument('ntag','')
            params = {
                "sales": sales,
                "income_bussniss": income_bussniss,
                "cq": cq,
                "kefu": kefu,
                "from_id": from_id,
                "building_id": building_id,
                "start": start,
                "end": end,
                "last_milepost_id":last_milepost_id,
                "qc_key":qc_key,
                "category_id":category_id
            }
            pre_page=20

            add_sql = ""
            sql_income_bussniss = ""
            sql_cq = ""
            sql_kefu = ""
            sql_from_id = ""
            sql_building_id = ""
            sql_date = ""
            sql_sales = ""
            sql_qc_key = ""
            sql_cq_add = ""
            sql_category_id=""
            sql_last_milepost_id=""
            if income_bussniss and income_bussniss != "0":
                sql_income_bussniss = " and id in (select project_id from t_projects_service_income aaaa where  service_money > 0 and  service_id=%s and aaaa.project_id=a.id)  " % (
                    income_bussniss)
            if cq and cq != "0":
                sql_cq = " and  id in (select project_id from t_projects_member where  team_id=38 and member_id=%s)  " % (
                    cq)
                sql_cq_add = " and member_id='"+cq+"'"

            if kefu and kefu != "0":
                sql_kefu = "and  project_id in (select project_id from t_projects_member  where  team_id=39 and member_id=%s) " % (
                    kefu)
            if from_id and from_id != "0":
                sql_from_id = " and busniess_from_id=%s" % (from_id)
            if building_id and building_id != "0":
                sql_building_id = " and building_id=%s" % (building_id)
            if sales and sales != "0":
                sql_sales =" and project_id in (select project_id from t_projects_member where team_id=34 and member_id="+sales+") "
            if start and end:
                sql_date = " and a.created_at between '%s' and '%s'" % (start, end)
            if qc_key:
                sql_qc_key += ''' and (id like "%%'''+qc_key+'''%%" or project_name like   "%%''' + qc_key + '''%%"  or customer_name like   "%%''' + qc_key + '''%%"  or customer_tel like   "%%''' + qc_key + '''%%" or customer_company like   "%%''' + qc_key + '''%%")'''
            if category_id:
                sql_category_id+= " and category_id=" + category_id
            if last_milepost_id:
                sql_last_milepost_id += " and last_milepost_id="+last_milepost_id

            add_sql = sql_income_bussniss + sql_cq + sql_sales + sql_kefu + sql_from_id + sql_building_id + sql_date+sql_qc_key+sql_category_id+sql_last_milepost_id
            count = self.db.get(
                '''SELECT count(*) count FROM  t_projects a , t_projects_member b where a.id=b.project_id and btype_id <> 0
               ''' + add_sql)
            cancel_wait_count1 = self.db.get('''
            SELECT  count(*) count
                FROM t_projects a
                    inner join t_projects_member b on team_id=38
                    and  a.id=b.project_id and is_cancel=1 and is_cancel_confirm_at is null
                    ''')

            cancel_confirm_count1 = self.db.get('''
            SELECT  count(*) count
                FROM t_projects a
                    inner join t_projects_member b on team_id=38
                    and  a.id=b.project_id and is_cancel=1 and is_cancel_confirm_at is not null
                    ''')
            pagination = Pagination(page, pre_page, count.count, self.request)
            startpage = (page-1) * pre_page
            t_projects = self.db.query('''
                SELECT  a.* ,b.mid,b.member_name,b.btype_id_name,b.last_milepost_id_name,last_milepost_id_at,b.created_at cq_created_at
                 FROM t_projects
                a inner join t_projects_member b on a.id=b.project_id


                where  b.last_milepost_id <> 0  ''' + add_sql + '''
                                order by b.last_milepost_id_at desc limit %s,%s
                ''', startpage, pre_page)

            project_btypes = self.db.query(
                """select *,(select count(*)  from t_projects_member a ,t_projects b  where a.project_id=b.id and  last_milepost_id=a.id ) c
                from t_projects_type a where income_category='办结' order by order_int"""
            )
            t_user_sales = self.db.query(
                "SELECT * FROM t_user_teams a , t_user b where b.id=a.uid and team_id=1 "
            )
            if last_milepost_id:
                t_categories = self.db.query(
                    """
                   select *,(select count(*)  from t_projects aa
                    inner join t_projects_member bb
                    on aa.id=bb.project_id
                    where category_id=a.id
					and last_milepost_id=%s

                    )
                    c from t_projects_category a where uid=%s order by order_int,id  """,
                    last_milepost_id,
                    uid)

            elif ntag =="is_cancel":
                pre_page = 20
                count = cancel_wait_count1
                pagination = Pagination(page, pre_page, count.count,
                                        self.request)
                startpage = (page - 1) * pre_page
                sql = ""
                t_projects = self.db.query('''
                         SELECT a.*,member_name bsa

                FROM t_projects a
                    inner join t_projects_member b on team_id=38
                    and  a.id=b.project_id and is_cancel=1 and is_cancel_confirm_at is null
                    '''+add_sql+'''
                        order by a.created_at desc limit %s,%s
                        ''', startpage, pre_page)
            elif ntag == "is_cancel_confirm":
                pre_page = 20
                count = cancel_confirm_count1
                pagination = Pagination(page, pre_page, count.count,
                                        self.request)
                startpage = (page - 1) * pre_page
                sql = ""
                t_projects = self.db.query('''
                         SELECT a.*,member_name bsa
                FROM t_projects a
                    inner join t_projects_member b on team_id=38
                    and  a.id=b.project_id and is_cancel=1 and is_cancel_confirm_at is not  null
                    '''+add_sql+'''
                        order by a.created_at desc limit %s,%s
                        ''', startpage, pre_page)

            else:
                t_categories = self.db.query(
                    """select *,(select count(*)  from t_projects

                    where category_id=a.id

                    )
                    c from t_projects_category a where uid=%s order by order_int,id """,
                    uid)

            all_categorys = self.db.query('''
           select * from  t_projects_category  where uid=%s  order by order_int desc,id desc
        ''', uid)
            t_project_bussniss = self.db.query(
                """select * from t_projects_type where income_category='业务类型' order by order_int  """
            )
            t_user_cq = self.db.query("SELECT * FROM t_user  where role=9 ")
            t_users = self.db.query(
                "SELECT * FROM t_user_teams a , t_user b where b.id=a.uid ")
            t_income_type = self.db.query("""
                select * from t_projects_type where income_category='业务来源' order by order_int desc
                """)
            t_building = self.db.query(
                "select * from t_projects_type where income_category='楼盘' order by order_int desc "
            )
            return self.render(
                'project/projects_cg.html',
                ntag=ntag,
                cancel_wait_count1=cancel_wait_count1,
                cancel_confirm_count1=cancel_confirm_count1,
                params=params,
                tag=tag,
                t_income_type=t_income_type,
                t_building=t_building,
                t_user_cq=t_user_cq,
                t_users=t_users,
                t_project_bussniss=t_project_bussniss,
                all_categorys=all_categorys,
                t_categories=t_categories,
                t_user_sales=t_user_sales,
                project_btypes=project_btypes,
                last_milepost_id=last_milepost_id,
                pagination=pagination,
                t_projects=t_projects,
                form_tag=tag,
                search_key="")

        elif tag == "projects_manager":
            category_id = self.get_argument("category_id", "")
            last_milepost_id = self.get_argument("last_milepost_id","")
            false = self.get_argument("false","0")
            page= int(self.get_argument("page",1))
            sales = self.get_argument("sales","")
            params = {"sales": sales, "tag": tag,"category_id":category_id}
            pre_page=20
            cq = self.get_argument("cq", "")
            kefu = self.get_argument("kefu", "")
            building_id = self.get_argument("building_id", "")
            income_bussniss = self.get_argument("income_bussniss", "")
            from_id = self.get_argument("from_id", "")
            start = self.get_argument("start", "")
            end = self.get_argument("end", "")

            params = {
                "income_bussniss": income_bussniss,
                "cq": cq,
                "kefu": kefu,
                "from_id": from_id,
                "building_id": building_id,
                "start": start,
                "end": end,
                "sales":sales,
                "last_milepost_id":last_milepost_id

            }
            add_sql = ""
            sql_income_bussniss = ""
            sql_cq = ""
            sql_kefu = ""
            sql_from_id = ""
            sql_building_id = ""
            sql_date = ""
            if income_bussniss and income_bussniss != "0":
                sql_income_bussniss = " and a.id in (select project_id from t_projects_service_income aaaa where  service_money > 0 and  service_id=%s and aaaa.project_id=a.id)  " % (
                    income_bussniss)
            if cq and cq != "0":
                sql_cq = " and  a.id in (select project_id from t_projects_member aaaa where  team_id=38 and member_id=%s and aaaa.project_id=a.id)  " % (
                    cq)
            if kefu and kefu != "0":
                sql_kefu = "and  a.id in (select project_id from t_projects_member aaaa where  team_id=39 and member_id=%s and aaaa.project_id=a.id) " % (
                    kefu)
            if from_id and from_id != "0":
                sql_from_id = " and a.busniess_from_id=%s" % (from_id)
            if building_id and building_id != "0":
                sql_building_id = " and a.building_id=%s" % (building_id)
            if start and end:
                sql_date = " and a.created_at between '%s' and '%s'" % (start,
                                                                        end)

            sql = ""
            if sales:
                sql = " and project_id in (select project_id from t_projects_member where team_id=34 and member_id="+sales+") "
            if last_milepost_id:
                sql += " and last_milepost_id="+last_milepost_id
            if category_id:
                sql += " and category_id=" + category_id

            add_sql = sql_income_bussniss + sql_cq + sql_kefu + sql_from_id + sql_building_id + sql_date + sql

            count = self.db.get(
                '''SELECT count(*) count FROM  t_projects a , t_projects_member b where a.id=b.project_id and btype_id <> 0
               ''' + sql)
            pagination = Pagination(page, pre_page, count.count, self.request)
            startpage = (page-1) * pre_page
            t_projects = self.db.query('''
                SELECT  a.* ,b.mid,b.member_name,b.btype_id_name,b.last_milepost_id_name,last_milepost_id_at,b.created_at cq_created_at FROM t_projects
                a inner join t_projects_member b on a.id=b.project_id


                where  b.last_milepost_id <> 0  ''' + add_sql + '''
                                order by b.last_milepost_id_at desc limit %s,%s
                ''', startpage, pre_page)

            project_btypes = self.db.query(
                """select *,(select count(*)  from t_projects_member where last_milepost_id=a.id) c
                from t_projects_type a where income_category='办结' order by order_int"""
            )
            t_user_sales = self.db.query(
                "SELECT * FROM t_user_teams a , t_user b where b.id=a.uid and team_id=1 "
            )
            if last_milepost_id:
                t_categories = self.db.query(
                    """
                   select *,(select count(*)  from t_projects aa
                    inner join t_projects_member bb
                    on aa.id=bb.project_id
                    where category_id=a.id
					and last_milepost_id=%s

                    )
                    c from t_projects_category a where uid=%s order by order_int,id  """,
                    last_milepost_id,
                    uid)
            else:
                t_categories = self.db.query(
                    """select *,(select count(*)  from t_projects

                    where category_id=a.id

                    )
                    c from t_projects_category a where uid=%s order by order_int,id """,
                    uid)

            all_categorys = self.db.query('''
           select * from  t_projects_category  where uid=%s  order by order_int desc,id desc
        ''', uid)


            t_project_bussniss = self.db.query(
                """select * from t_projects_type where income_category='业务类型' order by order_int  """
            )

            t_income_type = self.db.query("""
                select * from t_projects_type where income_category='业务来源' order by order_int desc
                """)

            t_sign_type = self.db.query("""
                select * from t_projects_type where income_category='签约方式' order by order_int desc
                """)
            t_talk_type = self.db.query(
                "select * from t_projects_type where income_category='沟通方式' order by order_int desc "
            )
            t_company = self.db.query("""
                select * from t_projects_type where income_category='收入公司' order by order_int desc
                """)
            t_business_channel = self.db.query("""
                select * from t_projects_type where income_category='推广来源渠道' order by order_int desc
                """)
            t_building = self.db.query(
                "select * from t_projects_type where income_category='楼盘' order by order_int desc "
            )
            t_users_kf = self.db.query("select * from t_user  where role=6")
            t_rec_contarct_type = self.db.query(
                "select * from t_projects_type where income_category='合同确认' order by order_int desc "
            )
            t_user_group = self.db.query("select * from t_user_group")
            t_users = self.db.query(
                "SELECT * FROM t_user_teams a , t_user b where b.id=a.uid ")

            t_user_cq = self.db.query("SELECT * FROM t_user  where role=9 ")
            return self.render(
                'project/projects_manager.html',
                params=params,
                t_user_cq=t_user_cq,
                t_users=t_users,
                t_rec_contarct_type=t_rec_contarct_type,
                t_income_type=t_income_type,
                t_users_kf=t_users_kf,
                t_building=t_building,
                t_business_channel=t_business_channel,
                t_sign_type=t_sign_type,
                t_company=t_company,
                t_talk_type=t_talk_type,
                t_project_bussniss=t_project_bussniss,
                all_categorys=all_categorys,
                t_categories=t_categories,
                t_user_sales=t_user_sales,
                project_btypes=project_btypes,
                last_milepost_id=last_milepost_id,
                pagination=pagination,
                t_projects=t_projects,
                form_tag=tag,

                search_key="")
        elif tag == "projects_yw":
            ntag = self.get_argument("ntag","")
            last_milepost_id = self.get_argument("last_milepost_id","")
            category_id = self.get_argument("category_id","")

            sql=""
            pre_page = 20
            params = {"tag": tag,"category_id":category_id,"last_milepost_id":last_milepost_id}
            page = int(self.get_argument("page", 1))
            wait_count = self.db.get('''
             SELECT count(*) count
                FROM t_projects a
                    inner join (select project_id,GROUP_CONCAT(concat(member_name,' ')) bsa
                    from t_projects_member where btype_id > 0  group by project_id ) b
                    on a.id=b.project_id and bsa is null
                    inner join t_projects_member c
                    on c.project_id=a.id
                     where team_id=34 and member_id=%s
                    ''', uid)

            cancel_wait_count1 = self.db.get('''
            SELECT  count(*) count
                FROM t_projects a
                    inner join t_projects_member b on btype_id > 0
                    and  a.id=b.project_id and is_cancel=1 and is_cancel_confirm_at is null
                      inner join t_projects_member c
                    on c.project_id=a.id   where  c.member_id=%s
                    ''',uid)

            cancel_confirm_count1 = self.db.get('''
            SELECT  count(*) count
                FROM t_projects a
                    inner join t_projects_member b on btype_id > 0
                    and  a.id=b.project_id and is_cancel=1 and is_cancel_confirm_at is not null
                      inner join t_projects_member c
                    on c.project_id=a.id   where  c.member_id=%s
                    ''', uid)
            all_count =  self.db.get('''
                                      SELECT   count(*) count

                            FROM t_projects
                    a left join t_projects_member b on a.id=b.project_id and b.btype_id > 0 and last_milepost_id <> 0
                     inner join t_projects_member c on a.id=c.project_id and c.team_id=34


                    where  c.member_id=%s
                ''', uid)
            if ntag == "wait":

                count = wait_count
                pagination = Pagination(page, pre_page, count.count,
                                        self.request)
                startpage = (page - 1) * pre_page
                sql = ""
                t_projects = self.db.query('''
                            SELECT a.*,

                b.bsa,0 mid, "" member_name,"" last_milepost_id_name,
                "" btype_id_name,"" last_milepost_id_at,"" cq_created_at
                FROM t_projects a
                    inner join (select project_id,GROUP_CONCAT(concat(member_name,' ')) bsa
                    from t_projects_member where btype_id > 0  group by project_id ) b
                    on a.id=b.project_id and bsa is null
                    inner join t_projects_member c
                    on c.project_id=a.id
                     where team_id=34 and member_id=%s
                        order by a.created_at desc limit %s,%s
                        ''', uid, startpage, pre_page)

            elif   last_milepost_id:
                sql = " and b.last_milepost_id=" + last_milepost_id

                count = self.db.get(
                    '''                    SELECT  count(*) count
                            FROM t_projects
                    a left join t_projects_member b on a.id=b.project_id and b.btype_id > 0 and last_milepost_id <> 0
                     inner join t_projects_member c on a.id=c.project_id and c.team_id=34


                    where  c.member_id=%s  ''' + sql + '''
                ''', uid)
                pagination = Pagination(page, pre_page, count.count, self.request)
                startpage = (page - 1) * pre_page
                t_projects = self.db.query('''
                    SELECT  a.* ,b.mid,b.member_name,b.btype_id_name,
                    b.last_milepost_id_name,
                    b.last_milepost_id_at,b.created_at cq_created_at

                            FROM t_projects
                    a left join t_projects_member b on a.id=b.project_id and b.btype_id > 0 and last_milepost_id <> 0
                     inner join t_projects_member c on a.id=c.project_id and c.team_id=34


                    where  c.member_id=%s  ''' + sql + '''
                                    order by a.created_at desc limit %s,%s
                    ''', uid, startpage, pre_page)


            elif ntag =="is_cancel":
                pre_page = 20
                count = cancel_wait_count1
                pagination = Pagination(page, pre_page, count.count,
                                        self.request)
                startpage = (page - 1) * pre_page
                sql = ""
                t_projects = self.db.query('''
                    SELECT  a.* ,b.mid,b.member_name,b.btype_id_name,
                    b.last_milepost_id_name,
                    b.last_milepost_id_at,b.created_at cq_created_at
                    FROM t_projects a
                    inner join t_projects_member b on b.btype_id > 0
                    and  a.id=b.project_id and b.is_cancel=1 and b.is_cancel_confirm_at is null
                         inner join t_projects_member c
                    on c.project_id=a.id
                     where c.team_id=34 and c.member_id=%s
                        order by a.created_at desc limit %s,%s
                        ''', uid, startpage, pre_page)

            elif ntag == "is_cancel_confirm":
                pre_page = 20
                count = cancel_confirm_count1
                pagination = Pagination(page, pre_page, count.count,
                                        self.request)
                startpage = (page - 1) * pre_page
                sql = ""
                t_projects = self.db.query('''
                    SELECT  a.* ,b.mid,b.member_name,b.btype_id_name,
                    b.last_milepost_id_name,
                    b.last_milepost_id_at,b.created_at cq_created_at
                    FROM t_projects a
                    inner join t_projects_member b on b.btype_id > 0
                    and  a.id=b.project_id and b.is_cancel=1 and b.is_cancel_confirm_at is not  null
                       inner join t_projects_member c
                    on c.project_id=a.id
                     where c.team_id=34 and c.member_id=%s
                        order by a.created_at desc limit %s,%s
                        ''', uid, startpage, pre_page)
            else:

                count = all_count
                pagination = Pagination(page, pre_page, count.count, self.request)
                startpage = (page - 1) * pre_page
                t_projects = self.db.query('''
                       SELECT  a.* ,b.mid,b.member_name,b.btype_id_name,
                    b.last_milepost_id_name,
                    b.last_milepost_id_at,b.created_at cq_created_at

                            FROM t_projects
                    a left join t_projects_member b on a.id=b.project_id and b.btype_id > 0 and last_milepost_id <> 0
                     inner join t_projects_member c on a.id=c.project_id and c.team_id=34


                    where  c.member_id=%s
                                    order by a.created_at desc limit %s,%s
                    ''', uid, startpage, pre_page)



            project_btypes = self.db.query(
                    """
                    select aa.*,ifnull(vv,0) c from t_projects_type aa
                    left join  (    SELECT b.last_milepost_id, count(*) vv
                        FROM t_projects
                        a inner join t_projects_member b on a.id=b.project_id

                        inner  join t_projects_member c on c.member_id=%s and
                    c.team_id=34 and a.id =c.project_id  group by b.last_milepost_id
                ) bb on bb.last_milepost_id=aa.id where income_category='办结'  order by order_int""",
                uid)
            if last_milepost_id:
                t_categories = self.db.query(
                    """
                   select *,(select count(*)  from t_projects aa
                    inner join t_projects_member bb
                    on aa.id=bb.project_id
                    where category_id=a.id
					and last_milepost_id=%s

                    )
                    c from t_projects_category a where uid=%s order by order_int,id  """,
                    last_milepost_id,
                    uid)
            else:
                t_categories = self.db.query(
                    """select *,(select count(*)  from t_projects

                    where category_id=a.id

                    )
                    c from t_projects_category a where uid=%s order by order_int,id """,
                    uid)

            all_categorys = self.db.query('''
           select * from  t_projects_category  where uid=%s  order by order_int desc,id desc
        ''', uid)
            return self.render(
                'project/projects_yw.html',
                all_count=all_count,
                cancel_wait_count1=cancel_wait_count1,
                cancel_confirm_count1=cancel_confirm_count1,
                all_categorys=all_categorys,
                t_categories=t_categories,
                ntag=ntag,
                params=params,
                wait_count=wait_count,
                last_milepost_id=last_milepost_id,
                project_btypes=project_btypes,
                pagination=pagination,
                t_projects=t_projects,
                form_tag=tag,
                search_key="")
        elif tag == "projects_kfgw":
            ntag = self.get_argument("ntag","")
            last_milepost_id = self.get_argument("last_milepost_id","")
            sql=""
            pre_page = 20

            page = int(self.get_argument("page", 1))
            wait_count = self.db.get('''
             SELECT count(*) count
                FROM t_projects a
                    inner join (select project_id,GROUP_CONCAT(concat(member_name,' ')) bsa
                    from t_projects_member where btype_id > 0  group by project_id ) b
                    on a.id=b.project_id and bsa is null
                    inner join t_projects_member c
                    on c.project_id=a.id
                     where team_id=36 and member_id=%s
                    ''', uid)
            all_count =  self.db.get('''
                                      SELECT   count(*) count

                            FROM t_projects
                    a left join t_projects_member b on a.id=b.project_id and b.btype_id > 0 and last_milepost_id <> 0
                     inner join t_projects_member c on a.id=c.project_id and c.team_id=34


                    where  c.member_id=%s
                ''', uid)
            if ntag == "wait":

                count = wait_count
                pagination = Pagination(page, pre_page, count.count,
                                        self.request)
                startpage = (page - 1) * pre_page
                sql = ""
                t_projects = self.db.query('''
                            SELECT a.*,

                b.bsa,0 mid, "" member_name,"" last_milepost_id_name,
                "" btype_id_name,"" last_milepost_id_at,"" cq_created_at
                FROM t_projects a
                    inner join (select project_id,GROUP_CONCAT(concat(member_name,' ')) bsa
                    from t_projects_member where btype_id > 0  group by project_id ) b
                    on a.id=b.project_id and bsa is null
                    inner join t_projects_member c
                    on c.project_id=a.id
                     where team_id=36 and member_id=%s
                        order by a.created_at desc limit %s,%s
                        ''', uid, startpage, pre_page)

            elif   last_milepost_id:
                sql = " and b.last_milepost_id=" + last_milepost_id

                count = self.db.get(
                    '''SELECT count(*) count FROM  t_projects a , t_projects_member
                    b where a.id=b.project_id and last_milepost_id <> 0
                    and b.member_id=%s ''' + sql + '''
                ''', uid)
                pagination = Pagination(page, pre_page, count.count, self.request)
                startpage = (page - 1) * pre_page
                t_projects = self.db.query('''
                    SELECT  a.* ,b.mid,b.member_name,b.btype_id_name,
                    b.last_milepost_id_name,
                    b.last_milepost_id_at,b.created_at cq_created_at

                            FROM t_projects
                    a left join t_projects_member b on a.id=b.project_id and b.btype_id > 0 and last_milepost_id <> 0
                     inner join t_projects_member c on a.id=c.project_id and c.team_id=36


                    where  c.member_id=%s  ''' + sql + '''
                                    order by a.created_at desc limit %s,%s
                    ''', uid, startpage, pre_page)
            else:
                count = all_count
                pagination = Pagination(page, pre_page, count.count, self.request)
                startpage = (page - 1) * pre_page
                t_projects = self.db.query('''
                       SELECT  a.* ,b.mid,b.member_name,b.btype_id_name,
                    b.last_milepost_id_name,
                    b.last_milepost_id_at,b.created_at cq_created_at

                            FROM t_projects
                    a left join t_projects_member b on a.id=b.project_id and b.btype_id > 0 and last_milepost_id <> 0
                     inner join t_projects_member c on a.id=c.project_id and c.team_id=36


                    where  c.member_id=%s
                                    order by a.created_at desc limit %s,%s
                    ''', uid, startpage, pre_page)



            project_btypes = self.db.query(
                    """
                       select aa.*,ifnull(vv,0) c from t_projects_type aa
                    left join  (    SELECT b.last_milepost_id, count(*) vv
                        FROM t_projects
                        a inner join t_projects_member b on a.id=b.project_id

                        inner  join t_projects_member c on c.member_id=%s and
                    c.team_id=36 and a.id =c.project_id   group by b.last_milepost_id
                ) bb on bb.last_milepost_id=aa.id where income_category='办结'  order by order_int""",
                uid)

            return self.render(
                'project/projects_kfgw.html',
                all_count=all_count,
                ntag=ntag,
                wait_count=wait_count,
                last_milepost_id=last_milepost_id,
                project_btypes=project_btypes,
                pagination=pagination,
                t_projects=t_projects,
                form_tag=tag,

                search_key="")

        elif tag == "projects_qc_milepost":
            category_id = self.get_argument("category_id", "")
            last_milepost_id = self.get_argument("last_milepost_id","")
            msg1 = self.get_argument("msg","")
            p_state = self.get_argument("p_state","")
            keyword = self.get_argument("keyword","")
            sql=""
            ntag = self.get_argument("ntag","")
            page = int(self.get_argument("page", 1))
            cq = self.get_argument("cq", "")
            kefu = self.get_argument("kefu", "")
            building_id = self.get_argument("building_id", "")
            income_bussniss = self.get_argument("income_bussniss", "")
            from_id = self.get_argument("from_id", "")
            start = self.get_argument("start", "")
            end = self.get_argument("end", "")
            sales = self.get_argument("sales", "")
            key = self.get_argument("key","")
            qc_key = self.get_argument("qc_key","")
            department_id= int(self.get_argument("department_id",0))
            team_id = self.get_argument("team_id","38")
            from_tag_where = self.get_argument("from_tag_where","")
            check_under=self.get_argument("check_under",'')
            t_user_relation=self.db.query('''
                select a.* from t_user_relation a
                inner join t_user_relation b on
                find_in_set(a.department_name,b.department_name)
                and b.uid=%s and b.is_leader<>0
                where a.uid!=b.uid and a.is_leader=0
                ''',uid)
            member_uids=uid
            if t_user_relation and check_under:
                member_uids=''
                for item in t_user_relation:
                    member_uids+=str(item.uid)+','
            

                
            params = {
                "sales": sales,
                "income_bussniss": income_bussniss,
                "cq": cq,
                "kefu": kefu,
                "from_id": from_id,
                "building_id": building_id,
                "start": start,
                "end": end,
                "last_milepost_id": last_milepost_id,
                "category_id": category_id,
                "qc_key": qc_key,
                "p_state": p_state,
                "ntag":ntag,
                "department_id":department_id,
                "team_id":team_id,
                "from_tag_where":from_tag_where,
                "check_under":check_under

            }
            add_sql = ""
            sql_income_bussniss = ""
            sql_cq = ""
            sql_kefu = ""
            sql_from_id = ""
            sql_building_id = ""
            sql_date = ""
            sql_sales = ""
            if income_bussniss and income_bussniss != "0":
                sql_income_bussniss = " and a.id in (select project_id from t_projects_service_income aaaa where  service_money > 0 and  service_id=%s and aaaa.project_id=a.id)  " % (
                    income_bussniss)
            if cq and cq != "0":
                sql_cq = " and  a.id in (select project_id from t_projects_member aaaa where  team_id=38 and member_id=%s and aaaa.project_id=a.id)  " % (
                    cq)
            if kefu and kefu != "0":
                sql_kefu = "and  a.id in (select project_id from t_projects_member aaaa where  team_id=36 and member_id=%s and aaaa.project_id=a.id) " % (
                    kefu)
            if from_id and from_id != "0":
                sql_from_id = " and a.busniess_from_id=%s" % (from_id)
            if building_id and building_id != "0":
                sql_building_id = " and a.building_id=%s" % (building_id)
            if sales and sales != "0":
                sql_sales = "and  a.id in (select project_id from t_projects_member aaaa where  team_id=34 and member_id=%s and aaaa.project_id=a.id) " % (
                    sales)
            if start and end:
                sql_date = " and a.created_at between '%s' and '%s'" % (start,
                                                                        end)
            add_sql = sql_income_bussniss + sql_cq + sql_sales + sql_kefu + sql_from_id + sql_building_id + sql_date


            if last_milepost_id:
                sql = " and last_milepost_id=" + last_milepost_id
            if ntag=='dis_banjie':
                sql=" and last_milepost_id in (162,167) and  btype_id=155 "
            elif ntag=='is_banjie':
                sql=" and last_milepost_id not in (162,167) and  btype_id=155 "
            if ntag=="ungroup":
                sql += " and b_category_id=0"
            elif category_id:
                sql += " and b_category_id=" + category_id

            if qc_key:
                sql += ''' and (id like "%%'''+qc_key+'''%%" or project_name like   "%%''' + qc_key + '''%%"  or customer_name like   "%%''' + qc_key + '''%%"  or customer_tel like   "%%''' + qc_key + '''%%" or customer_company like   "%%''' + qc_key + '''%%")'''


            if p_state and p_state!="0":
                sql += " and project_id in (select project_id from t_projects_state_msg  where project_id= a.id and state_id_name='"+p_state+"') "
            

            add_sql = add_sql+sql
            page = int(self.get_argument("page", 1))
            pre_page = 20
            count = self.db.get(''' SELECT   count(*) count
    FROM t_projects
                    a inner join t_projects_member b on a.id=b.project_id and last_milepost_id > 0

                    where  b.last_milepost_id <> 0 and find_in_set(member_id,%s)  ''' +
                                        add_sql + '''  and is_cancel=0  and is_cancel_confirm_at is   null
               ''' ,member_uids)
            dis_banjie_count=self.db.get('''
                                                SELECT count(*) count

                FROM t_projects
                    a inner join t_projects_member b on a.id=b.project_id and last_milepost_id > 0  and btype_id >0

                    where  b.last_milepost_id <> 0 and  member_id=%s   and last_milepost_id in (162,167) and  btype_id=155   and is_cancel=0  and is_cancel_confirm_at is   null
            ''',member_uids)
            is_banjie_count=self.db.get('''
                    SELECT count(*) count
                    FROM t_projects
                    a inner join t_projects_member b on a.id=b.project_id and last_milepost_id > 0  and btype_id >0
                    where  b.last_milepost_id <> 0 and  member_id=%s   and last_milepost_id not in (162,167) and  btype_id=155  
                     and is_cancel=0  and is_cancel_confirm_at is   null
               
            ''',member_uids)
            cancel_wait_count1 = self.db.get('''
            SELECT  count(*) count
                FROM t_projects a
                    inner join t_projects_member b on btype_id > 0
                    and  a.id=b.project_id and is_cancel=1 and is_cancel_confirm_at is null
                    and  find_in_set(member_id,%s)
                    ''',member_uids)

            cancel_confirm_count1 = self.db.get('''
            SELECT  count(*) count
                FROM t_projects a
                    inner join t_projects_member b on btype_id > 0
                    and  a.id=b.project_id and is_cancel=1 and is_cancel_confirm_at is not null
                and find_in_set(member_id,%s)

                    ''' ,member_uids)

            if ntag =="is_cancel":
                pre_page = 20
                count = cancel_wait_count1
                pagination = Pagination(page, pre_page, count.count,
                                        self.request)
                startpage = (page - 1) * pre_page
                sql = ""
                t_projects = self.db.query('''
                          SELECT  a.* ,b.mid,b.member_name,b.btype_id_name,b_category_id,b_category_id_name,
                    b.last_milepost_id_name,b.last_milepost_id_at,b.created_at cq_created_at,b.last_state_msg,b.last_state_msg_at
    FROM t_projects
                    a inner join t_projects_member b on a.id=b.project_id and last_milepost_id > 0

                    where  b.last_milepost_id <> 0 and  find_in_set(member_id,%s)   and is_cancel=1 and is_cancel_confirm_at is null
                    '''+add_sql+'''
                        order by b.last_milepost_id_at desc limit %s,%s
                        ''', member_uids,startpage, pre_page)
            elif ntag == "is_cancel_confirm":

                pre_page = 20
                count = cancel_confirm_count1
                pagination = Pagination(page, pre_page, count.count,
                                        self.request)
                startpage = (page - 1) * pre_page
                sql = ""
                t_projects = self.db.query('''
                         SELECT  a.* ,b.mid,b.member_name,b.btype_id_name,b_category_id,b_category_id_name,
                    b.last_milepost_id_name,b.last_milepost_id_at,b.created_at cq_created_at,b.last_state_msg,b.last_state_msg_at
    FROM t_projects
                    a inner join t_projects_member b on a.id=b.project_id and last_milepost_id > 0

                    where  b.last_milepost_id <> 0 and  find_in_set(member_id,%s)  and  is_cancel=1
                    and
                    is_cancel_confirm_at is not  null
                    ''' + add_sql + '''
                        order by b.last_milepost_id_at desc limit %s,%s
                        ''', member_uids, startpage, pre_page)

            else:
                print '''
                                    SELECT  a.* ,b.mid,b.member_name,b.btype_id_name,b_category_id,b_category_id_name,b.zone_id_name,
                    b.last_milepost_id_name,b.last_milepost_id_at,b.created_at cq_created_at,
                    b.last_state_msg,b.last_state_msg_at,timestampdiff(day,b.created_at,now()) msg_created_day

                FROM t_projects
                    a inner join t_projects_member b on a.id=b.project_id and last_milepost_id > 0  and btype_id >0

                    where  b.last_milepost_id <> 0 and  member_id=%s  ''' +  add_sql + '''  and is_cancel=0  and is_cancel_confirm_at is   null
                
                '''
                pagination = Pagination(page, pre_page, count.count, self.request)
                startpage = (page - 1) * pre_page

                t_projects = self.db.query('''
                    SELECT  a.* ,b.mid,b.member_name,b.btype_id_name,b_category_id,b_category_id_name,b.zone_id_name,
                    b.last_milepost_id_name,b.last_milepost_id_at,b.created_at cq_created_at,
                    b.last_state_msg,b.last_state_msg_at,timestampdiff(day,b.created_at,now()) msg_created_day

                FROM t_projects
                    a inner join t_projects_member b on a.id=b.project_id and last_milepost_id > 0  and btype_id >0

                    where  b.last_milepost_id <> 0 and  find_in_set(member_id,%s)  ''' +
                                        add_sql + '''  and is_cancel=0   and is_cancel_confirm_at is   null

                                    order by last_milepost_id_at desc limit %s,%s
                    ''', member_uids, startpage, pre_page)


            project_btypes = self.db.query(
                """select *,(select count(*)  from t_projects_member a , t_projects b  where a.project_id=b.id and  last_milepost_id=a.id and  btype_id <> 0 and  find_in_set(member_id,%s)   and is_cancel=0  and is_cancel_confirm_at is   null)

                c from t_projects_type a where income_category='办结'  order by order_int """,
                member_uids)
            wait_group = self.db.get(
                """   select count(*) count from t_projects_member aa,t_projects bb where
                  b_category_id=0 and aa.project_id=bb.id and  last_milepost_id=%s
                    and find_in_set(member_id,%s) and is_cancel=0  and is_cancel_confirm_at is   null""",
                last_milepost_id,member_uids)



            t_categories = self.db.query(
                """
                select *,(select count(*)  from t_projects_member aa,t_projects bb
                where b_category_id=a.id and aa.project_id=bb.id and  last_milepost_id=%s
                and aa.is_cancel=0  and aa.is_cancel_confirm_at is null)
                c from t_projects_category a where find_in_set(uid,%s) and a.is_business=0 order by order_int,id """,
                last_milepost_id,member_uids)
            all_categorys=self.db.query('''
           select * from  t_projects_category  where find_in_set(uid,%s)  order by order_int desc,id desc
        ''',member_uids)
            t_projects_state = self.db.query("""
                select msg_txt from t_projects_state  group by msg_txt

            """)

            t_project_bussniss = self.db.query(
                """select * from t_projects_type where income_category='业务类型' order by order_int  """
            )

            t_income_type = self.db.query("""
                select * from t_projects_type where income_category='业务来源' order by order_int desc
                """)

            t_sign_type = self.db.query("""
                select * from t_projects_type where income_category='签约方式' order by order_int desc
                """)
            t_talk_type = self.db.query(
                "select * from t_projects_type where income_category='沟通方式' order by order_int desc "
            )
            t_company = self.db.query("""
                select * from t_projects_type where income_category='收入公司' order by order_int desc
                """)
            t_business_channel = self.db.query("""
                select * from t_projects_type where income_category='推广来源渠道' order by order_int desc
                """)
            t_building = self.db.query(
                "select * from t_projects_type where income_category='楼盘' order by order_int desc "
            )
            t_users_kf = self.db.query("select * from t_user  where role=6")
            t_rec_contarct_type = self.db.query(
                "select * from t_projects_type where income_category='合同确认' order by order_int desc "
            )
            t_user_group = self.db.query("select * from t_user_group")
            t_users = self.db.query(
                "SELECT * FROM t_user_teams a , t_user b where b.id=a.uid ")

            t_user_cq = self.db.query("SELECT * FROM t_user  where role=9 ")
            t_user_sales = self.db.query(
                "SELECT * FROM t_user_teams a , t_user b where b.id=a.uid and team_id=1 "
            )
            t_projects_type=self.db.query("""
                select id,income_name from t_projects_type where income_category='区域'
            """)
            return self.render(
                'project/projects_qc_milepost.html',
                cancel_wait_count1=cancel_wait_count1,
                cancel_confirm_count1=cancel_confirm_count1,
                wait_group=wait_group,
                params=params,
                t_user_cq=t_user_cq,
                t_users=t_users,
                t_user_group=t_user_group,
                t_user_sales=t_user_sales,
                t_talk_type=t_talk_type,
                t_income_type=t_income_type,
                t_building=t_building,
                tag=tag,
                msg=msg1,
                t_projects_type=t_projects_type,
                ntag=ntag,
                keyword=keyword,
                p_state=p_state,
                t_projects_state=t_projects_state,
                all_categorys=all_categorys,
                category_id=category_id,
                t_categories=t_categories,
                last_milepost_id=last_milepost_id,
                project_btypes=project_btypes,
                pagination=pagination,
                t_projects=t_projects,
                form_tag=tag,
                t_user_relation=t_user_relation,
                t_project_bussniss=t_project_bussniss,
                search_key="",
                dt=dt,
                dis_banjie_count=dis_banjie_count,
                is_banjie_count=is_banjie_count,
                diff_date=self.diff_date)

        elif tag == "projects_qc":
            uid = self.get_secure_cookie("uid")
            style = self.get_argument('style', '')
            page = int(self.get_argument("page", 1))
            cq = self.get_argument("cq", "")
            kefu = self.get_argument("kefu", "")
            building_id = self.get_argument("building_id", "")
            income_bussniss = self.get_argument("income_bussniss", "")
            from_id = self.get_argument("from_id", "")
            start = self.get_argument("start", "")
            end = self.get_argument("end", "")
            sales = self.get_argument("sales", "")
            key = self.get_argument("key","")
            ntag = self.get_argument("ntag","")
            params = {
                "sales": sales,
                "income_bussniss": income_bussniss,
                "cq": cq,
                "kefu": kefu,
                "from_id": from_id,
                "building_id": building_id,
                "start": start,
                "end": end,
                "ntag":ntag,
            }
            add_sql = ""
            sql_income_bussniss = ""
            sql_cq = ""
            sql_kefu = ""
            sql_from_id = ""
            sql_building_id = ""
            sql_date = ""
            sql_sales = ""
            if income_bussniss and income_bussniss != "0":
                sql_income_bussniss = " and a.id in (select project_id from t_projects_service_income aaaa where  service_money > 0 and  service_id=%s and aaaa.project_id=a.id)  " % (
                    income_bussniss)
            if cq and cq != "0":
                sql_cq = " and  a.id in (select project_id from t_projects_member aaaa where  team_id=38 and member_id=%s and aaaa.project_id=a.id)  " % (
                    cq)
            if kefu and kefu != "0":
                sql_kefu = "and  a.id in (select project_id from t_projects_member aaaa where  team_id=36 and member_id=%s and aaaa.project_id=a.id) " % (
                    kefu)
            if from_id and from_id != "0":
                sql_from_id = " and a.busniess_from_id=%s" % (from_id)
            if building_id and building_id != "0":
                sql_building_id = " and a.building_id=%s" % (building_id)
            if sales and sales != "0":
                sql_sales = "and  a.id in (select project_id from t_projects_member aaaa where  team_id=34 and member_id=%s and aaaa.project_id=a.id) " % (
                    sales)
            if start and end:
                sql_date = " and a.created_at between '%s' and '%s'" % (start,
                                                                        end)
            add_sql = sql_income_bussniss + sql_cq + sql_sales + sql_kefu + sql_from_id + sql_building_id + sql_date
            pre_page = 20
            if role=='9':
                categorys=self.db.query('''
                    select * from t_projects_category where role=9
                    ''')
            else:
                categorys=self.db.query('select * from t_projects_category')
            if key:
                search_sql = "%" + key + "%"
                count = self.db.get(
                    '''SELECT count(*) count FROM t_projects a  inner join t_projects_member b on a.id=b.project_id and b.team_id=38
                    where  member_id=%s and (project_name like "%''' + search_sql
                    + '''%" or customer_tel like "%''' + search_sql +
                    '''%" or customer_name like "%''' + search_sql + '''%")''',
                    uid)
                pagination = Pagination(page, pre_page, count.count,
                                        self.request)
                startpage = (page - 1) * pre_page
                sql_str = ""
                t_projects = self.db.query(
                    '''
                    SELECT a.*, b.member_name    FROM t_projects a  inner join t_projects_member b
                    on a.id=b.project_id and b.team_id=38
                    where   member_id=%s and (project_name like "%''' + search_sql +
                    '''%" or customer_tel like "%''' + search_sql +
                    '''%" or customer_name like "%''' + search_sql + '''%")
                        order by a.created_at desc limit %s,%s
                        ''', uid, startpage, pre_page)
            else:
                if style:
                    count = self.db.get(
                        ''' SELECT count(*) count  FROM t_projects a
                        inner join t_projects_member b on a.id=b.project_id and b.team_id=38
                        and member_id=%s
                        left join(select category_name,project_id from t_projects_category_list) c
                        on a.id=c.project_id where c.category_name=%s
                        ''' + add_sql, uid, style)
                    pagination = Pagination(page, pre_page, count.count, self.request)
                    startpage = (page - 1) * pre_page
                    sql_str = ""
                    t_projects = self.db.query('''
                        SELECT a.*, b.member_name,c.category_name  FROM t_projects a
                        inner join t_projects_member b on a.id=b.project_id and b.team_id=38
                        and member_id=%s
                        left join(select category_name,project_id from t_projects_category_list) c
                        on a.id=c.project_id where c.category_name=%s
                        ''' + add_sql + '''
                        order by a.created_at desc limit %s,%s
                        ''', uid, style, startpage, pre_page)
                else:
                    count = self.db.get(
                        '''SELECT count(*) count FROM t_projects a  inner join t_projects_member b on a.id=b.project_id and b.team_id=38
                        and member_id=%s
                        ''' + add_sql, uid)
                    pagination = Pagination(page, pre_page, count.count, self.request)
                    startpage = (page - 1) * pre_page
                    sql_str = ""
                    t_projects = self.db.query('''
                        SELECT a.*, b.member_name  FROM t_projects a
                        inner join t_projects_member b on a.id=b.project_id and b.team_id=38
                        and member_id=%s

                        ''' + add_sql + '''
                        order by a.created_at desc limit %s,%s
                        ''', uid, startpage, pre_page)
            t_project_bussniss = self.db.query(
                """select * from t_projects_type where income_category='业务类型' order by order_int  """
            )

            t_income_type = self.db.query("""
                select * from t_projects_type where income_category='业务来源' order by order_int desc
                """)

            t_sign_type = self.db.query("""
                select * from t_projects_type where income_category='签约方式' order by order_int desc
                """)
            t_talk_type = self.db.query(
                "select * from t_projects_type where income_category='沟通方式' order by order_int desc "
            )
            t_company = self.db.query("""
                select * from t_projects_type where income_category='收入公司' order by order_int desc
                """)
            t_business_channel = self.db.query("""
                select * from t_projects_type where income_category='推广来源渠道' order by order_int desc
                """)
            t_building = self.db.query(
                "select * from t_projects_type where income_category='楼盘' order by order_int desc "
            )
            t_users_kf = self.db.query("select * from t_user  where role=6")
            t_rec_contarct_type = self.db.query(
                "select * from t_projects_type where income_category='合同确认' order by order_int desc "
            )
            t_user_group = self.db.query("select * from t_user_group")
            t_users = self.db.query(
                "SELECT * FROM t_user_teams a , t_user b where b.id=a.uid ")

            t_user_cq = self.db.query("SELECT * FROM t_user  where role=9 ")
            t_user_sales = self.db.query("SELECT * FROM t_user_teams a , t_user b where b.id=a.uid and team_id=1 ")


            return self.render(
                'project/projects_qc.html',
                t_user_sales=t_user_sales,
                t_project_bussniss=t_project_bussniss,
                t_income_type=t_income_type,
                t_talk_type=t_talk_type,
                t_company=t_company,
                t_business_channel=t_business_channel,
                t_building=t_building,
                t_users_kf=t_users_kf,
                t_rec_contarct_type=t_rec_contarct_type,
                t_user_group=t_user_group,
                t_users=t_users,
                t_user_cq=t_user_cq,
                params=params,
                tag=tag,
                pagination=pagination,
                categorys=categorys,
                style=style,
                t_projects=t_projects,
                form_tag="list",
                search_key=key,
                loupan='')
        elif tag=="projects_qc_loupan":
            uid = self.get_secure_cookie("uid")
            style = self.get_argument('style', '')
            page = int(self.get_argument("page", 1))
            cq = self.get_argument("cq", "")
            kefu = self.get_argument("kefu", "")
            building_id = self.get_argument("building_id", "")
            income_bussniss = self.get_argument("income_bussniss", "")
            from_id = self.get_argument("from_id", "")
            start = self.get_argument("start", "")
            end = self.get_argument("end", "")
            sales = self.get_argument("sales", "")
            key = self.get_argument("key", "")
            params = {
                "sales": sales,
                "income_bussniss": income_bussniss,
                "cq": cq,
                "kefu": kefu,
                "from_id": from_id,
                "building_id": building_id,
                "start": start,
                "end": end
            }
            pre_page = 20
            count = self.db.get(
                        '''      SELECT count(*) count FROM t_projects a
                        inner join t_projects_member b on a.id=b.project_id
                        and member_id=%s
                        left join(select category_name,project_id from t_projects_category_list) c
                        on a.id=c.project_id where a.busniess_from_id_name='楼盘'
                        ''', uid)
            pagination = Pagination(page, pre_page, count.count, self.request)
            startpage = (page - 1) * pre_page
            sql_str = ""
            t_projects = self.db.query('''
                        SELECT a.*, b.member_name,c.category_name  FROM t_projects a
                        inner join t_projects_member b on a.id=b.project_id
                        and member_id=%s
                        left join(select category_name,project_id from t_projects_category_list) c
                        on a.id=c.project_id where a.busniess_from_id_name='楼盘'
                        order by a.created_at desc limit %s,%s
                        ''', uid, startpage, pre_page)
            t_project_bussniss = self.db.query(
                """select * from t_projects_type where income_category='业务类型' order by order_int  """
            )

            t_income_type = self.db.query("""
                select * from t_projects_type where income_category='业务来源' order by order_int desc
                """)

            t_sign_type = self.db.query("""
                select * from t_projects_type where income_category='签约方式' order by order_int desc
                """)
            t_talk_type = self.db.query(
                "select * from t_projects_type where income_category='沟通方式' order by order_int desc "
            )
            t_company = self.db.query("""
                select * from t_projects_type where income_category='收入公司' order by order_int desc
                """)
            t_business_channel = self.db.query("""
                select * from t_projects_type where income_category='推广来源渠道' order by order_int desc
                """)
            t_building = self.db.query(
                "select * from t_projects_type where income_category='楼盘' order by order_int desc "
            )
            t_users_kf = self.db.query("select * from t_user  where role=6")
            t_rec_contarct_type = self.db.query(
                "select * from t_projects_type where income_category='合同确认' order by order_int desc "
            )
            t_user_group = self.db.query("select * from t_user_group")
            t_users = self.db.query(
                "SELECT * FROM t_user_teams a , t_user b where b.id=a.uid ")

            t_user_cq = self.db.query("SELECT * FROM t_user  where role=9 ")
            t_user_sales = self.db.query(
                "SELECT * FROM t_user_teams a , t_user b where b.id=a.uid and team_id=1 "
            )

            return self.render(
                'project/projects_qc.html',
                t_user_sales=t_user_sales,
                t_project_bussniss=t_project_bussniss,
                t_income_type=t_income_type,
                t_talk_type=t_talk_type,
                t_company=t_company,
                t_business_channel=t_business_channel,
                t_building=t_building,
                t_users_kf=t_users_kf,
                t_rec_contarct_type=t_rec_contarct_type,
                t_user_group=t_user_group,
                t_users=t_users,
                t_user_cq=t_user_cq,
                params=params,
                tag=tag,
                pagination=pagination,
                style=style,
                t_projects=t_projects,
                form_tag="list",
                categorys='',
                search_key=key,
                loupan='lp')

        elif tag == "my":
            uid = self.get_secure_cookie("uid")
            role = self.get_secure_cookie("role")
            style = self.get_argument('style', '')
            page = int(self.get_argument("page", 1))
            cq = self.get_argument("cq", "")
            kfgw=self.get_argument("kfgw","")
            kefu = self.get_argument("kefu", "")
            building_id = self.get_argument("building_id", "")
            income_bussniss = self.get_argument("income_bussniss", "")
            from_id = self.get_argument("from_id", "")
            start = self.get_argument("start", "")
            end = self.get_argument("end", "")
            company_id=self.get_argument('company_id','')
            company_guid=self.get_argument('company_guid','')
            correlation_projects=self.get_argument('correlation_projects','')
            show_model=self.get_argument('show_model','')
            customer_company=self.get_argument('customer_company','')
            show_tag=self.get_argument('show_tag','')
            if company_id and company_guid:
                add_t_company = self.db_company.get(
                    "select * from t_company where id=%s and company_guid=%s",
                    company_id, company_guid)
                is_exit_t_company=self.db.get('''
                    select * from t_projects where rel_company_id=%s and rel_company_id_name=%s
                ''',company_id,add_t_company.entName)
                if not is_exit_t_company:
                    is_exit_t_company='-1'
                if not add_t_company:
                    self.write("not company")
            else:
                is_exit_t_company=''
                add_t_company=''
            params = {
                "income_bussniss": income_bussniss,
                "cq": cq,
                "kfgw":kfgw,
                "kefu": kefu,
                "from_id": from_id,
                "building_id": building_id,
                "start": start,
                "end": end,
                "correlation_projects":correlation_projects,
                "show_model":show_model,
                "customer_company":customer_company,
                "show_tag":show_tag
            }
            add_sql = ""
            sql_income_bussniss = ""
            sql_cq = ""
            sql_kfgw=""
            sql_kefu = ""
            sql_from_id = ""
            sql_building_id = ""
            sql_date = ""
            if income_bussniss and income_bussniss != "0":
                if show_tag=='history':
                    sql_income_bussniss = " and a.customer_company=(select customer_company from  t_projects where id=(select project_id from t_projects_service_income aaaa where  service_money > 0 and  service_id=%s and aaaa.project_id=a.id))  " % (
                        income_bussniss)
                else:
                    sql_income_bussniss = " and a.id in (select project_id from t_projects_service_income aaaa where  service_money > 0 and  service_id=%s and aaaa.project_id=a.id)  " % (
                    income_bussniss)
            if cq and cq != "0":
                sql_cq = " and  a.id in (select project_id from t_projects_member aaaa where  team_id=38 and member_id=%s and aaaa.project_id=a.id)  " % (
                    cq)
            if kfgw and kfgw !='0':
                sql_kfgw = "and  a.id in (select project_id from t_projects_member aaaa where  team_id=36 and member_id=%s and aaaa.project_id=a.id) " % (
                    kfgw)
            if kefu and kefu != "0":
                sql_kefu = "and  a.id in (select project_id from t_projects_member aaaa where  team_id=39 and member_id=%s and aaaa.project_id=a.id) " % (
                    kefu)
            if from_id and from_id != "0":
                sql_from_id = " and a.busniess_from_id=%s" % (from_id)
            if building_id and building_id != "0":
                sql_building_id = " and a.building_id=%s" % (building_id)
            if start and end:
                sql_date = " and a.created_at between '%s' and '%s'" % (start,
                                                                        end)
            add_sql = sql_income_bussniss + sql_cq + sql_kfgw + sql_kefu + sql_from_id + sql_building_id + sql_date
            if correlation_projects:
                correlation_sql='''
                    inner join
                '''+options.mysql_database_customer+'''
                .t_customer  c on a.customer_company=c.company and c.acc_uid=%s where a.uid!=%s
                '''%(uid,uid)
            else:
                correlation_sql=' where   a.uid=%s  '%uid
            pre_page = 10
            count = self.db.get('''
                  SELECT count(*) count
                FROM t_projects  a
                    '''+correlation_sql+ add_sql)
            pagination = Pagination(page, pre_page, count.count, self.request)
            startpage = (page - 1) * pre_page
            # if role=='1':
            #     categorys=self.db.query('''
            #         select * from t_projects_category where role=1''')
            # else:
            #     categorys=self.db.query('select * from t_projects_category')
            if style:
                t_projects = self.db.query('''
                      SELECT  a.*,b.member_name sale_name ,c.member_name promo_name,d.bs,f.member_name service_man,
                 g.bsa qc_name,h.category_name
                FROM t_projects a
                 left join (select member_name ,project_id from t_projects_member where team_id=36  ) b
                 on a.id=b.project_id
                 left join (select member_name ,project_id from t_projects_member where team_id=39  ) c
				 on a.id=c.project_id
                left join (select member_name ,project_id from t_projects_member where team_id=34  )  f
				 on a.id=f.project_id
                left join (select project_id,GROUP_CONCAT(concat(member_name,' ')) bsa
                from t_projects_member where team_id=38 group by project_id )  g
				 on a.id=g.project_id

                 left join (select project_id,GROUP_CONCAT(concat(a.service_id,'|',a.service_money)) bs from t_projects_service_income a

                    where service_money > 0
                    group by project_id) d
                 on  a.id=d.project_id
                 left join(select category_name,project_id from t_projects_category_list) h
                 on a.id=h.project_id
                 left join()
                   where   h.category_name=%s and a.uid=%s
                order by created_at desc limit %s,%s
                ''', style, uid, startpage, pre_page)
            else:
                t_projects = self.db.query('''
                     SELECT  a.*, b.team_list
                FROM t_projects a

                left join (select project_id,GROUP_CONCAT(concat(member_name,'|',team_id)) team_list
                from t_projects_member group by project_id )  b
				 on a.id=b.project_id '''+correlation_sql+ add_sql + '''
                order by a.created_at desc limit %s,%s
                ''', startpage, pre_page)
            t_project_bussniss = self.db.query(
                """select * from t_projects_type where income_category='业务类型' order by order_int  """
            )

            t_income_type = self.db.query("""
                select * from t_projects_type where income_category='业务来源' order by order_int desc
                """)

            t_sign_type = self.db.query("""
                select * from t_projects_type where income_category='签约方式' order by order_int desc
                """)
            t_talk_type = self.db.query(
                "select * from t_projects_type where income_category='沟通方式' order by order_int desc "
            )
            t_company = self.db.query("""
                select * from t_projects_type where income_category='收入公司' order by order_int desc
                """)
            t_business_channel = self.db.query("""
                select * from t_projects_type where income_category='推广来源渠道' order by order_int desc
                """)
            t_building = self.db.query(
                "select * from t_projects_type where income_category='楼盘' order by order_int desc "
            )
            t_users_kf = self.db.query("select * from t_user  where role=6")
            t_rec_contarct_type = self.db.query(
                "select * from t_projects_type where income_category='合同确认' order by order_int desc "
            )
            t_user_group = self.db.query("select * from t_user_group")
            t_users = self.db.query(
                "SELECT * FROM t_user_teams a , t_user b where b.id=a.uid ")

            t_user_cq = self.db.query("SELECT * FROM t_user  where role=9 ")

            t_user_teams=self.db.query(
                   """
                    select a.*,b.team_id from t_user a inner join t_user_teams b on a.id=b.uid
                    """
                    )
            t_acc_types = self.db.query(
                """select * from t_projects_type where income_category='会计业务' order by order_int  """
            )
            t_promo_types = self.db.query(
                """select * from t_projects_type where income_category='套餐' order by order_int  """
            )
            t_product_type = self.db_customer.query(
                """select * from t_type where tag='订购服务' order by order_int  """
            )
            year = datetime.datetime.today().year
            year_list =[]
            for item in range(year-2,year+2):
                year_list.append(item)
            return self.render(
                'project/allprojects.html',
                year_list=year_list,
                t_product_type=t_product_type,
                t_promo_types=t_promo_types,
                params=params,
                t_acc_types=t_acc_types,
                t_user_teams=t_user_teams,
                t_user_cq=t_user_cq,
                t_users=t_users,
                t_rec_contarct_type=t_rec_contarct_type,
                t_income_type=t_income_type,
                t_users_kf=t_users_kf,
                pagination=pagination,
                t_projects=t_projects,
                t_project_bussniss=t_project_bussniss,
                form_tag="my",
                tag=tag,
                add_t_company=add_t_company,
                is_exit_t_company=is_exit_t_company,
                search_key="",
                t_building=t_building,
                t_business_channel=t_business_channel,
                t_sign_type=t_sign_type,
                t_company=t_company,
                t_talk_type=t_talk_type,
                # categorys=categorys,
                style=style,
                t_user_group=t_user_group)

        elif tag == "my1":
            uid = self.get_secure_cookie("uid")
            role = self.get_secure_cookie("role")
            style = self.get_argument('style', '')
            page = int(self.get_argument("page", 1))
            cq = self.get_argument("cq", "")
            kfgw=self.get_argument("kfgw","")
            kefu = self.get_argument("kefu", "")
            building_id = self.get_argument("building_id", "")
            income_bussniss = self.get_argument("income_bussniss", "")
            from_id = self.get_argument("from_id", "")
            start = self.get_argument("start", "")
            end = self.get_argument("end", "")
            company_id=self.get_argument('company_id','')
            company_guid=self.get_argument('company_guid','')
            if company_id and company_guid:
                add_t_company = self.db_company.get(
                    "select * from t_company where id=%s and company_guid=%s",
                    company_id, company_guid)
                is_exit_t_company=self.db.get('''
                    select * from t_projects where rel_company_id=%s and rel_company_id_name=%s
                ''',company_id,add_t_company.entName)
                if not is_exit_t_company:
                    is_exit_t_company='-1'
                if not add_t_company:
                    self.write("not company")
            else:
                is_exit_t_company=''
                add_t_company=''
            params = {
                "income_bussniss": income_bussniss,
                "cq": cq,
                "kfgw":kfgw,
                "kefu": kefu,
                "from_id": from_id,
                "building_id": building_id,
                "start": start,
                "end": end
            }
            add_sql = ""
            sql_income_bussniss = ""
            sql_cq = ""
            sql_kfgw=""
            sql_kefu = ""
            sql_from_id = ""
            sql_building_id = ""
            sql_date = ""
            if income_bussniss and income_bussniss != "0":
                sql_income_bussniss = " and a.id in (select project_id from t_projects_service_income aaaa where  service_money > 0 and  service_id=%s and aaaa.project_id=a.id)  " % (
                    income_bussniss)
            if cq and cq != "0":
                sql_cq = " and  a.id in (select project_id from t_projects_member aaaa where  team_id=38 and member_id=%s and aaaa.project_id=a.id)  " % (
                    cq)
            if kfgw and kfgw !='0':
                sql_kfgw = "and  a.id in (select project_id from t_projects_member aaaa where  team_id=36 and member_id=%s and aaaa.project_id=a.id) " % (
                    kfgw)
            if kefu and kefu != "0":
                sql_kefu = "and  a.id in (select project_id from t_projects_member aaaa where  team_id=39 and member_id=%s and aaaa.project_id=a.id) " % (
                    kefu)
            if from_id and from_id != "0":
                sql_from_id = " and a.busniess_from_id=%s" % (from_id)
            if building_id and building_id != "0":
                sql_building_id = " and a.building_id=%s" % (building_id)
            if start and end:
                sql_date = " and a.created_at between '%s' and '%s'" % (start,
                                                                        end)
            add_sql = sql_income_bussniss + sql_cq + sql_kfgw + sql_kefu + sql_from_id + sql_building_id + sql_date

            pre_page = 10
            count = self.db.get('''
                  SELECT count(*) count
                FROM t_projects  a

                   where   uid=%s ''' + add_sql, uid)
            pagination = Pagination(page, pre_page, count.count, self.request)
            startpage = (page - 1) * pre_page
            # if role=='1':
            #     categorys=self.db.query('''
            #         select * from t_projects_category where role=1''')
            # else:
            #     categorys=self.db.query('select * from t_projects_category')
            if style:
                t_projects = self.db.query('''
                      SELECT  a.*,b.member_name sale_name ,c.member_name promo_name,d.bs,f.member_name service_man,
                 g.bsa qc_name,h.category_name
                FROM t_projects a
                 left join (select member_name ,project_id from t_projects_member where team_id=36  ) b
                 on a.id=b.project_id
                 left join (select member_name ,project_id from t_projects_member where team_id=39  ) c
				 on a.id=c.project_id
                left join (select member_name ,project_id from t_projects_member where team_id=34  )  f
				 on a.id=f.project_id
                left join (select project_id,GROUP_CONCAT(concat(member_name,' ')) bsa
                from t_projects_member where team_id=38 group by project_id )  g
				 on a.id=g.project_id

                 left join (select project_id,GROUP_CONCAT(concat(a.service_id,'|',a.service_money)) bs from t_projects_service_income a

                    where service_money > 0
                    group by project_id) d
                 on  a.id=d.project_id
                 left join(select category_name,project_id from t_projects_category_list) h
                 on a.id=h.project_id
                 left join()
                   where   h.category_name=%s and a.uid=%s
                order by created_at desc limit %s,%s
                ''', style, uid, startpage, pre_page)
            else:
                t_projects = self.db.query('''
                     SELECT  a.*, b.team_list
                FROM t_projects a

                left join (select project_id,GROUP_CONCAT(concat(member_name,'|',team_id)) team_list
                from t_projects_member group by project_id )  b
				 on a.id=b.project_id
                   where   a.uid=%s  ''' + add_sql + '''
                order by a.created_at desc limit %s,%s
                ''', uid, startpage, pre_page)
            t_project_bussniss = self.db.query(
                """select * from t_projects_type where income_category='业务类型' order by order_int  """
            )

            t_income_type = self.db.query("""
                select * from t_projects_type where income_category='业务来源' order by order_int desc
                """)

            t_sign_type = self.db.query("""
                select * from t_projects_type where income_category='签约方式' order by order_int desc
                """)
            t_talk_type = self.db.query(
                "select * from t_projects_type where income_category='沟通方式' order by order_int desc "
            )
            t_company = self.db.query("""
                select * from t_projects_type where income_category='收入公司' order by order_int desc
                """)
            t_business_channel = self.db.query("""
                select * from t_projects_type where income_category='推广来源渠道' order by order_int desc
                """)
            t_building = self.db.query(
                "select * from t_projects_type where income_category='楼盘' order by order_int desc "
            )
            t_users_kf = self.db.query("select * from t_user  where role=6")
            t_rec_contarct_type = self.db.query(
                "select * from t_projects_type where income_category='合同确认' order by order_int desc "
            )
            t_user_group = self.db.query("select * from t_user_group")
            t_users = self.db.query(
                "SELECT * FROM t_user_teams a , t_user b where b.id=a.uid ")

            t_user_cq = self.db.query("SELECT * FROM t_user  where role=9 ")

            t_user_teams=self.db.query(
                   """
                    select a.*,b.team_id from t_user a inner join t_user_teams b on a.id=b.uid
                    """
                    )
            t_acc_types = self.db.query(
                """select * from t_projects_type where income_category='会计业务' order by order_int  """
            )
            t_promo_types = self.db.query(
                """select * from t_projects_type where income_category='套餐' order by order_int  """
            )
            return self.render(
                'project/allprojects3.html',
                t_promo_types=t_promo_types,
                params=params,
                t_acc_types=t_acc_types,
                t_user_teams=t_user_teams,
                t_user_cq=t_user_cq,
                t_users=t_users,
                t_rec_contarct_type=t_rec_contarct_type,
                t_income_type=t_income_type,
                t_users_kf=t_users_kf,
                pagination=pagination,
                t_projects=t_projects,
                t_project_bussniss=t_project_bussniss,
                form_tag="my",
                tag=tag,
                add_t_company=add_t_company,
                is_exit_t_company=is_exit_t_company,
                search_key="",
                t_building=t_building,
                t_business_channel=t_business_channel,
                t_sign_type=t_sign_type,
                t_company=t_company,
                t_talk_type=t_talk_type,
                # categorys=categorys,
                style=style,
                t_user_group=t_user_group)

        elif tag =="output":
            start = self.get_argument("start","")
            end = self.get_argument("end","")
            cq = self.get_argument("cq", "")
            kefu = self.get_argument("kefu", "")
            building_id = self.get_argument("building_id", "")
            income_bussniss = self.get_argument("income_bussniss", "")
            from_id = self.get_argument("from_id", "")
            start = self.get_argument("start", "")
            end = self.get_argument("end", "")
            sales = self.get_argument("sales", "")
            kfkj=self.get_argument('kfkj','')
            kfgw=self.get_argument('kfgw','')
            t_projects=''
            params = {
                "sales": sales,
                "income_bussniss": income_bussniss,
                "cq": cq,
                "kefu": kefu,
                "from_id": from_id,
                "building_id": building_id,
                "start": start,
                "end": end,
                "kfkj":kfkj,
                "kfgw":kfgw
            }
            add_sql = ""
            sql_income_bussniss = ""
            sql_cq = ""
            sql_kefu = ""
            sql_from_id = ""
            sql_building_id = ""
            sql_date = ""
            sql_sales = ""
            sql_kfkj=""
            sql_kfgw=""
            if income_bussniss and income_bussniss != "0":
                sql_income_bussniss = " and a.id in (select project_id from t_projects_service_income aaaa where  service_money > 0 and  service_id=%s and aaaa.project_id=a.id)  " % (
                    income_bussniss)
            if cq and cq != "0":
                sql_cq = " and  a.id in (select project_id from t_projects_member aaaa where  team_id=38 and member_id=%s and aaaa.project_id=a.id)  " % (
                    cq)
            if kefu and kefu != "0":
                sql_kefu = "and  a.id in (select project_id from t_projects_member aaaa where  team_id=39 and member_id=%s and aaaa.project_id=a.id) " % (
                    kefu)
            if kfgw and  kfgw!="0":
                sql_kfgw = "and  a.id in (select project_id from t_projects_member aaaa where  team_id=36 and member_id=%s and aaaa.project_id=a.id) "%(kfgw)
            if from_id and from_id != "0":
                sql_from_id = " and a.busniess_from_id=%s" % (from_id)
            if building_id and building_id != "0":
                sql_building_id = " and a.building_id=%s" % (building_id)
            if sales and sales != "0":
                sql_sales = "and  a.id in (select project_id from t_projects_member aaaa where  team_id=34 and member_id=%s and aaaa.project_id=a.id) " % (
                    sales)
            if kfkj and kfkj !='0':
                sql_kfkj=" and a.id in (select project_id from t_projects_member  where  team_id=205 and member_id=%s and project_id=a.id) "%kfkj
            if start and end:
                sql_date = " and a.created_at between '%s' and '%s'" % (start,
                                                                        end)
            add_sql = sql_income_bussniss + sql_cq + sql_sales + sql_kefu + sql_from_id + sql_building_id + sql_date+sql_kfkj+sql_kfgw

            return_str =  False
            if role == "8" or role == "3" or role == "11" or role=='1' :  #无畏亮
                return_str= True
            if return_str==False:
                self.write("没有访问权限" )
            else:
                if not start and not end :
                    pass
                else:
                    t_project_bussniss = self.db.query(
                        """select * from t_projects_type where income_category='业务类型' order by order_int  """
                    )
                    if role=='1':


                        t_projects = self.db.query('''
                            SELECT  a.*,b.member_name sale_name ,c.member_name promo_name,d.bs,f.member_name service_man,
                g.member_name qc_name,h.member_name kfkj_name,


            (
                select ifnull(sum(income_money),0)
                from t_projects_income aa
                                ,t_projects_income_title bb

                                where aa.parent_id=bb.id and  aa.project_id=a.id and income_uid > 0
                                and income_id =40

                ) total_con_income,
            (
                            select ifnull(sum(income_money),0)
                            from t_projects_income aa
                                            ,t_projects_income_title bb

                                            where aa.parent_id=bb.id and  aa.project_id=a.id and income_uid > 0
                                            and income_id <=43

                            ) total_all_income

                FROM t_projects a
                left join (select member_name ,project_id from t_projects_member where team_id=36  ) b
                on a.id=b.project_id
                left join (select member_name ,project_id from t_projects_member where team_id=39  ) c
                on a.id=c.project_id
                left join (select member_name ,project_id from t_projects_member where team_id=34  )  f
                on a.id=f.project_id

                left join (select project_id,GROUP_CONCAT(concat(member_name,' '))   member_name
                from t_projects_member where team_id=38 group by project_id )  g
				 on a.id=g.project_id

                   left join (select member_name ,project_id,member_id from t_projects_member where team_id=205  ) h
                on a.id=h.project_id  and h.member_id > 0

                left join (select project_id,GROUP_CONCAT(concat(a.service_id,'|',a.service_money)) bs
                from t_projects_service_income a

                    where service_money <> 0
                    group by project_id) d
                        on  a.id=d.project_id
                            where  is_lock=0 and uid=%s
                            '''+add_sql+'''
                            order by id 
                            ''',uid)
                    else: #财务
                        t_projects = self.db.query("""
                                SELECT  a.*,mbs,bs,
            (
                select ifnull(sum(income_money),0)
                from t_projects_income aa,t_projects_income_title bb

                                where aa.parent_id=bb.id and  aa.project_id=a.id and income_uid > 0
                                and income_id =40

                ) total_con_income,
            (
                            select ifnull(sum(income_money),0)
                            from t_projects_income aa
                                            ,t_projects_income_title bb

                                            where aa.parent_id=bb.id and  aa.project_id=a.id and income_uid > 0
                                            and income_id <=43

                            ) total_all_income

                FROM t_projects a
               
				left join (select project_id,group_concat(team_name,"|",member_name)  mbs 
                from t_projects_member where member_id > 0 group by project_id ) b  on b.project_id=a.id

                left join (select project_id,GROUP_CONCAT(concat(a.service_id,'|',a.service_money)) bs
                from t_projects_service_income a
                    where service_money <> 0
                    group by project_id) d
                        on  a.id=d.project_id
                            where  is_lock=0 
                                   """+add_sql+"""
            #                 order by id 
                        """)
            #             t_projects = self.db.query('''
            #                 SELECT  a.*,b.member_name sale_name ,c.member_name promo_name,d.bs,f.member_name service_man,
            #     g.member_name qc_name,h.member_name kfkj_name,


            # (
            #     select ifnull(sum(income_money),0)
            #     from t_projects_income aa
            #                     ,t_projects_income_title bb

            #                     where aa.parent_id=bb.id and  aa.project_id=a.id and income_uid > 0
            #                     and income_id =40

            #     ) total_con_income,
            # (
            #                 select ifnull(sum(income_money),0)
            #                 from t_projects_income aa
            #                                 ,t_projects_income_title bb

            #                                 where aa.parent_id=bb.id and  aa.project_id=a.id and income_uid > 0
            #                                 and income_id <=43

            #                 ) total_all_income

            #     FROM t_projects a
            #     left join (select member_name ,project_id from t_projects_member where team_id=36  ) b
            #     on a.id=b.project_id
            #     left join (select member_name ,project_id from t_projects_member where team_id=39  ) c
            #     on a.id=c.project_id
            #     left join (select member_name ,project_id from t_projects_member where team_id=34  )  f
            #     on a.id=f.project_id


            #     left join (select project_id,GROUP_CONCAT(concat(member_name,' '))   member_name
            #     from t_projects_member where team_id=38 group by project_id )  g
			# 	 on a.id=g.project_id
            #       left join (select member_name ,project_id,member_id from t_projects_member where team_id=205  ) h
            #     on a.id=h.project_id and h.member_id > 0
            #     left join (select project_id,GROUP_CONCAT(concat(a.service_id,'|',a.service_money)) bs
            #     from t_projects_service_income a

            #         where service_money <> 0
            #         group by project_id) d
            #             on  a.id=d.project_id
            #                 where  is_lock=0
            #                 '''+add_sql+'''
            #                 order by id 
            #                 ''')
                    print add_sql
                    # 创建 xls 文件对象
                    wb = xlwt.Workbook()
                    # 新增一个表单
                    sh = wb.add_sheet(u'业绩表')
                    # 按位置添加数据a
                    sh.write(0, 0, u"序号")
                    sh.write(0, 1, u"日期")
                    sh.write(0, 2, u"客户姓名")
                    sh.write(0, 3 , u"公司名")
                    sh.write(0, 4, u"联系方式")
                    sh.write(0, 5, u"销售顾问")
                    sh.write(0, 6, u"客服顾问")
                    sh.write(0, 7, u"工商专员")
                    sh.write(0,8,u"客服会计")
                    sh.write(0,9,u"创建人")
                    sh.write(0, 10, u"来源渠道")
                    sh.write(0, 11, u"内部推荐人")
                    sh.write(0, 12, u"应收账款")
                    sh.write(0, 13, u"业务内容")
                    sh.write(0, 14, u"注册地址类型")
                    sh.write(0, 15, u"合同金额")
                    sh.write(0, 16, u"其他收入金额")
                    for bidx, row in enumerate(t_project_bussniss):
                        sh.write(0, 17 + bidx, row.income_name)
                    af_num = len(t_project_bussniss)
                    sh.write(0, 18+ af_num, u"合同定金")
                    sh.write(0, 19 + af_num, u"实收定金")
                    sh.write(0, 20 + af_num, u"尾款")
                    sh.write(0, 21 + af_num, u"客户推荐人")
                    sh.write(0, 22+ af_num, u"客户来源")
                    sh.write(0, 23+ af_num, u"来源平台")
                    sh.write(0, 24+ af_num, u"在线客服")

                    sh.write(0, 25+ af_num, u"订单编号")


                    sh.write(0, 26+ af_num, u"签约方式")
                    sh.write(0, 27+ af_num, u"是否记账")
                    sh.write(0, 28+ af_num, u"成交周期")
                    sh.write(0, 29+ af_num, u"搜索词")
                    sh.write(0, 30+ af_num, u"来源方式")
                    sh.write(0, 31+ af_num, u"是否有合同")
                    sh.write(0, 32+ af_num, u"合同编号")
                    sh.write(0, 33+ af_num, u"业务状态")

                    for idx, item in enumerate(t_projects):
                        idx= idx+1
                        sh.write(idx, 0, item.id)
                        sh.write(idx, 1, item.created_at.strftime("%Y-%m-%d"))
                        sh.write(idx, 2, item.customer_name)
                        sh.write(idx, 3 , item.customer_company)

                        sh.write(idx, 4, "") #不要联系方式
                        sh.write(idx, 5,self.get_member(item.mbs,"销售顾问"))
                        sh.write(idx, 6,self.get_member(item.mbs,"客服顾问"))
                        sh.write(idx, 7, self.get_member(item.mbs,"工商专员"))


                        # if item.customer_company and len(item.customer_company) > 6 and not  item.kfkj_name:
                        #     t_customer = self.db_customer.get("select * from t_customer where  company=%s",item.customer_company)
                        #     if t_customer:
                        #         item.kfkj_name=t_customer.acc_uid_name
                        #         print t_customer.acc_uid_name
                        sh.write(idx,8,self.get_member(item.mbs,"客服会计"))
                        sh.write(idx,9,item.uid_name)
                        sh.write(idx, 10, item.busniess_from_id_name)
                        sh.write(idx, 11, item.recommend_staff)
                        sh.write(idx, 12,'')
                        sh.write(idx, 13, item.project_name)
                        sh.write(idx, 14, item.addr_type)
                        sh.write(idx, 15, item.all_income)
                        sh.write(idx, 16, '')
                        for bidx,row in enumerate(t_project_bussniss):
                            bidx_new = 17+bidx
                            sh.write(idx, bidx_new,
                                        self.write_income(item.bs, row.id))
                        sh.write(idx, 18 + af_num, float(item.pre_income))
                        sh.write(idx, 19 + af_num, float(item.total_con_income))
                        sh.write(idx, 20 + af_num,
                                 float(item.all_income - item.total_con_income))
                        sh.write(idx, 21 + af_num, item.recommend_by)


                        sh.write(idx, 22+ af_num, item.busniess_from_id_name)
                        sh.write(idx, 23+ af_num, item.channel_id_name)
                        sh.write(idx, 24+ af_num, self.get_member(item.mbs,"在线客服"))

                        sh.write(idx, 25+ af_num, item.contract_number)

                        f_str = u"否"
                        if item.is_finance:
                            f_str = u"是"
                        sh.write(idx, 26+ af_num, item.sign_type_id_name)
                        sh.write(idx, 27+ af_num, f_str)

                        sh.write(idx, 28+ af_num, item.deal_day)
                        sh.write(idx, 29+ af_num, item.from_word)
                        sh.write(idx, 30+ af_num, item.talk_type_id_name)
                        sh.write(idx, 31+ af_num, item.contract_confirm_id_name)
                        sh.write(idx, 32+ af_num, item.contract_remark)
                        project_milepost_type = self.db.query(
                            """select *,b.order_int border_int from t_projects_type a
                            inner join t_projects_milepost b on b.type_id=a.id where income_category='办结' and a.is_hide=0
                            and project_id=%s and income_name='仓管确认交接完成' order by b.order_int""",
                            item.id)

                        project_btypes = self.db.query(
                            "select * from  t_projects_member  where project_id=%s  and btype_id <> 0  and not_transition=0 ",
                            item.id)
                        is_end = 2
                        is_cancel = 1
                        is_cancel_arr =[]
                        if len(project_milepost_type) ==0:
                            is_end=1
                        for row in project_milepost_type:
                            if row.income_name == "仓管确认交接完成" and not  row.confirm_at:
                                is_con = 0
                                for row1 in project_btypes:
                                    if row.member_id==row1.mid and   row1.is_cancel_confirm_at :
                                        #   print "dump....", is_end, row1.is_cancel_confirm_at
                                        is_con = 1
                                        is_cancel_arr.append(row1.mid)

                                if is_con:
                                    continue
                                is_end = 1
                                break
                        if len(project_btypes)  and len(project_btypes)==len(is_cancel_arr):
                            is_cancel = 2
                        presult=u"办理中"
                        if is_cancel==2:
                            presult=u"取消单"
                        elif is_end==2:
                            presult=u"已办结"
                        sh.write(idx, 33 + af_num, presult)
                    # sh.write(0, 18+af_num, u"在线客服")
                    # 保存文件
                    wb.save('media/output/%s.xls'%(uid))
                t_project_bussniss = self.db.query(
                    """select * from t_projects_type where income_category='业务类型' order by order_int  """
                )

                t_income_type = self.db.query("""
                    select * from t_projects_type where income_category='业务来源' order by order_int desc
                    """)

                t_sign_type = self.db.query("""
                    select * from t_projects_type where income_category='签约方式' order by order_int desc
                    """)
                t_talk_type = self.db.query(
                    "select * from t_projects_type where income_category='沟通方式' order by order_int desc "
                )
                t_company = self.db.query("""
                    select * from t_projects_type where income_category='收入公司' order by order_int desc
                    """)
                t_business_channel = self.db.query("""
                    select * from t_projects_type where income_category='推广来源渠道' order by order_int desc
                    """)
                t_building = self.db.query(
                    "select * from t_projects_type where income_category='楼盘' order by order_int desc "
                )
                t_users_kf = self.db.query("select * from t_user  where role=6")
                t_rec_contarct_type = self.db.query(
                    "select * from t_projects_type where income_category='合同确认' order by order_int desc "
                )
                t_user_group=self.db.query("select * from t_user_group")
                t_users = self.db.query(
                    "SELECT * FROM t_user_teams a , t_user b where b.id=a.uid "
                )

                t_user_cq = self.db.query(
                    "SELECT * FROM t_user  where role=9 "
                )
                t_user_sales = self.db.query("SELECT * FROM t_user_teams a , t_user b where b.id=a.uid and team_id=1 ")
                t_user_kfkj=self.db.query('''
                    select member_id,member_name from t_projects_member where team_name='客服会计' and member_id <> 0
                    group by member_name
                ''')
                return self.render(
                    "project/output.html",
                    output_path="/static/output/%s.xls" % (uid),
                    search_key="",
                    params=params,
                    t_user_sales=t_user_sales,
                    get_member=self.get_member,
                    t_user_cq=t_user_cq,
                    t_user_kfkj=t_user_kfkj,
                    t_users=t_users,
                    write_income=self.write_income,
                    t_rec_contarct_type=t_rec_contarct_type,
                    t_income_type=t_income_type,
                    t_users_kf=t_users_kf,
                    t_projects=t_projects,
                    t_project_bussniss=t_project_bussniss,
                    t_building=t_building,
                    t_business_channel=t_business_channel,
                    t_sign_type=t_sign_type,
                    t_company=t_company,
                    t_talk_type=t_talk_type,
                    start=start,
                    tag=tag,
                    end=end,
                    num=len(t_projects))

        elif tag == "projects_transition":
            launch=self.get_argument('launch',0)
            id=self.get_argument('id','')
            fq_name=self.get_argument('fq_name','')
            company=self.get_argument('company','')
            status=self.get_argument('status','')
            is_inner=self.get_argument('is_inner','')
            sql=''
            if id:
                sql+=' and b.project_id=%s '%id
            if fq_name:
                sql+=' and b.uid_name="%s" '%fq_name
            if company:
                sql+=' and a.customer_company like "%%'+company+'%%"'
            if status=='1':
                sql+=' and b.rec_by_uid_at is not null'
            elif status=='0':
                sql+=' and b.rec_by_uid_at is null'
            if is_inner=='1':
                sql+=' and b.is_inner=1 '
            elif is_inner=='0':
                sql+=' and b.is_inner=0 '
            params={
                'id':id,
                'fq_name':fq_name,
                'company':company,
                'status':status,
                'is_inner':is_inner
            }
            page = int(self.get_argument("page", 1))
            pre_page = 20
            if launch:
                count = self.db.get('''
                    select count(*) count from
                    t_company a ,
                    t_projects_transition  b
                    where a.id=b.company_id and b.uid=%s and b.project_company_type=2''' ,uid)
                pagination = Pagination(page, pre_page, count.count, self.request)
                startpage = (page - 1) * pre_page
                t_projects = self.db.query('''
                select *,a.company_name customer_company,b.uid_name post_by_name,b.id pt_id from t_company a , t_projects_transition  b
                 where a.id=b.company_id  and b.uid=%s and b.project_company_type=2
                order by a.created_at desc limit %s,%s
                ''', uid,startpage, pre_page)
            else:
                count = self.db.get('''
             select count(*) count
                 from  t_projects_transition b
                 where (b.project_id in (select id from t_projects where id=b.project_id)
                 or b.company_id in (select id from t_company where id=b.company_id ) and b.project_company_type=2)
                   and   (rec_by_uid=%s or rec_by=%s or b.uid=%s) '''+sql
             ,uid,uid_name,uid)
                print("""
                 select count(*) count from
                    t_projects a ,
                    t_projects_transition  b
                    where a.id=b.project_id and rec_by_uid="""+uid+sql
                )
                pagination = Pagination(page, pre_page, count.count, self.request)
                startpage = (page - 1) * pre_page
                # t_projects = self.db.query('''
                # select *,b.uid_name post_by_name,b.id pt_id from t_projects a , t_projects_transition  b
                #  where a.id=b.project_id  and   (rec_by_uid=%s or rec_by=%s)'''+sql+'''
                # order by b.rec_by_uid_at,b.created_at desc limit %s,%s
                # ''', uid,uid_name,startpage, pre_page)
                
                t_projects = self.db.query('''
                select b.*,b.uid_name post_by_name,
                b.id pt_id,a.customer_company,c.company_name,c.company_code
           
                 from  t_projects_transition b
                 left join t_projects a on  a.id=b.project_id
                 left join t_company c on c.id=b.company_id
                 where (b.project_id in (select id from t_projects where id=b.project_id)
                 or b.company_id in (select id from t_company where id=b.company_id ) and b.project_company_type=2)
                   and   (rec_by_uid=%s or rec_by=%s or b.uid=%s) '''+sql+'''
                order by b.rec_by_uid_at,b.created_at desc limit %s,%s
                ''', uid,uid_name,uid,startpage, pre_page)

            t_projects_type=self.db.query(
                    """
                    select * from t_projects_type where income_category='移交资料'
                    """
                )
            return self.render(
                'project/projects_transition.html',
                form_tag="my",
                tag=tag,
                params=params,
                launch=launch,
                t_projects_type=t_projects_type,
                pagination=pagination,
                t_projects=t_projects,
                search_key="")
        elif tag == "projects_transition_details":
            id=self.get_argument('id','')
            project_id=self.get_argument("project_id","")
            if not id and not project_id:
                self.write("not project_id")
            else:
                t_projects = self.db.get('''
                    select a.*,b.use_type,b.tran_at,b.rec_by_uid_at
                    ,b.rec_by,b.remark,b.file_name,b.created_at 
                     pt_created_at,c.company_name,b.type_names,b.uid_name post_by_name ,b.id pt_id 
                    from t_projects_transition  b left join t_projects a on a.id=b.project_id
                    left join t_company c on c.id=b.company_id
                    where  b.id=%s
                    ''', id)
                return self.render(
                    'project/projects_transition_details.html',
                    form_tag="my",
                    tag=tag,
                    t_projects=t_projects,
                    search_key="")

        elif tag == "projects_simple_details":
            id=self.get_argument("id","")
            guid = self.get_argument("guid")
            if not id and not project_id:
                self.write("not project_id")
            else:
                t_project = self.db.get('''
                    select *  from t_projects
                    where id=%s and guid=%s
                    ''', id,guid)
                t_projects_type=self.db.query(
                    """
                    select * from t_projects_type where income_category='移交资料'
                    """
                )
                t_project_transitions=self.db.query(
                    """
                    select * from t_projects_transition where project_id=%s and file_type=0 order by created_at desc
                    """,t_project.id)
                return self.render(
                    'project/projects_simple_details.html',
                    form_tag="my",
                    tag=tag,
                    t_project_transitions=t_project_transitions,
                    t_project=t_project,
                    t_projects_type=t_projects_type,
                    search_key="")

        elif tag == "allview":
            uid = self.get_secure_cookie("uid")
            style=self.get_argument('style','')
            page = int(self.get_argument("page", 1))
            cq = self.get_argument("cq","")
            kefu = self.get_argument("kefu","")
            building_id = self.get_argument("building_id","")
            income_bussniss = self.get_argument("income_bussniss","")
            from_id = self.get_argument("from_id","")
            start = self.get_argument("start","")
            end = self.get_argument("end","")
            sales = self.get_argument("sales","")
            kfgw=self.get_argument('kfgw','')
            project_name=self.get_argument('project_name','')
            params = {
                "sales": sales,
                "income_bussniss": income_bussniss,
                "cq": cq,
                "kefu": kefu,
                "from_id": from_id,
                "building_id": building_id,
                "start": start,
                "end": end,
                "kfgw":kfgw,
                'project_name':project_name
            }
            add_sql = ""
            sql_income_bussniss=""
            sql_cq = ""
            sql_kefu = ""
            sql_kfgw=""
            sql_from_id = ""
            sql_building_id = ""
            sql_date = ""
            sql_sales = ""
            sql_project_name=''
            if income_bussniss and  income_bussniss!="0":
                sql_income_bussniss = " and a.id in (select project_id from t_projects_service_income aaaa where  service_money > 0 and  service_id=%s and aaaa.project_id=a.id)  "%(income_bussniss)
            if cq and  cq!="0":
                sql_cq = " and  a.id in (select project_id from t_projects_member aaaa where  team_id=38 and member_id=%s and aaaa.project_id=a.id)  "%(cq)
            if kefu and  kefu!="0":
                sql_kefu = "and  a.id in (select project_id from t_projects_member aaaa where  team_id=39 and member_id=%s and aaaa.project_id=a.id) "%(kefu)
            if kfgw and  kfgw!="0":
                sql_kfgw = "and  a.id in (select project_id from t_projects_member aaaa where  team_id=36 and member_id=%s and aaaa.project_id=a.id) "%(kfgw)
            if from_id and from_id!="0":
                sql_from_id = " and a.busniess_from_id=%s"%(from_id)
            if building_id  and building_id !="0":
                sql_building_id =  " and a.building_id=%s"%(building_id)
            if sales and sales != "0":
                sql_sales = "and  a.id in (select project_id from t_projects_member aaaa where  team_id=34 and member_id=%s and aaaa.project_id=a.id) " % (
                    sales)
            if start and end:
                sql_date = " and a.created_at between '%s' and '%s'"%(start,end)
            if project_name:
                sql_project_name=' and a.project_name like "%%'+project_name+'%%" '
            add_sql = sql_income_bussniss + sql_cq + sql_sales + sql_kefu+sql_kfgw + sql_from_id + sql_building_id + sql_date+sql_project_name
     
            pre_page = 10
            count = self.db.get(
                '''
                  SELECT count(*) count,(
                      select sum(all_income) from t_projects a where   is_lock=0 '''+ add_sql+'''
                  ) sum_income
                FROM t_projects  a

                   where   is_lock=0 '''+ add_sql)
            pagination = Pagination(page, pre_page, count.count, self.request)
            startpage = (page - 1) * pre_page
            # if role=='1':
            #     categorys=self.db.query('''
            #         select * from t_projects_category where role=1''')
            # else:
            #     categorys=self.db.query('select * from t_projects_category')
            if style:
                t_projects = self.db.query('''
                      SELECT  a.*,b.member_name sale_name ,c.member_name promo_name,d.bs,f.member_name service_man,
                 g.bsa qc_name,h.category_name
                FROM t_projects a
                 left join (select member_name ,project_id from t_projects_member where team_id=36  ) b
                 on a.id=b.project_id
                 left join (select member_name ,project_id from t_projects_member where team_id=39  ) c
				 on a.id=c.project_id
                left join (select member_name ,project_id from t_projects_member where team_id=34  )  f
				 on a.id=f.project_id
                left join (select project_id,GROUP_CONCAT(concat(member_name,' ')) bsa
                from t_projects_member where team_id=38 group by project_id )  g
				 on a.id=g.project_id

                 left join (select project_id,GROUP_CONCAT(concat(a.service_id,'|',a.service_money)) bs from t_projects_service_income a

                    where service_money > 0
                    group by project_id) d
                 on  a.id=d.project_id
                 left join(select category_name,project_id from t_projects_category_list) h
                 on a.id=h.project_id
                 left join()
                   where   h.category_name=%s and a.uid=%s
                order by created_at desc limit %s,%s
                ''',style,uid,startpage, pre_page)
            else:
                t_projects = self.db.query('''
                     SELECT  a.*, b.team_list
                FROM t_projects a

                left join (select project_id,GROUP_CONCAT(concat(member_name,'|',team_id)) team_list
                from t_projects_member group by project_id )  b
				 on a.id=b.project_id
                   where   is_lock=0  '''+add_sql+'''
                order by a.created_at desc limit %s,%s
                ''',startpage, pre_page)
            t_project_bussniss = self.db.query(
                """select * from t_projects_type where income_category='业务类型' order by order_int  """
            )

            t_income_type = self.db.query("""
                select * from t_projects_type where income_category='业务来源' order by order_int desc
                """)

            t_sign_type = self.db.query("""
                select * from t_projects_type where income_category='签约方式' order by order_int desc
                """)
            t_talk_type = self.db.query(
                "select * from t_projects_type where income_category='沟通方式' order by order_int desc "
            )
            t_company = self.db.query("""
                select * from t_projects_type where income_category='收入公司' order by order_int desc
                """)
            t_business_channel = self.db.query("""
                select * from t_projects_type where income_category='推广来源渠道' order by order_int desc
                """)
            t_building = self.db.query(
                "select * from t_projects_type where income_category='楼盘' order by order_int desc "
            )
            t_users_kf = self.db.query("select * from t_user  where role=6")
            t_rec_contarct_type = self.db.query(
                "select * from t_projects_type where income_category='合同确认' order by order_int desc "
            )
            t_user_group=self.db.query("select * from t_user_group")
            t_users = self.db.query(
                "SELECT * FROM t_user_teams a , t_user b where b.id=a.uid "
            )

            t_user_cq = self.db.query(
                "SELECT * FROM t_user  where role=9 "
            )
            t_user_sales = self.db.query("SELECT * FROM t_user_teams a , t_user b where b.id=a.uid and team_id=1 ")
            return self.render(
                'project/allview.html',
                count=count,
                params=params,
                t_user_sales=t_user_sales,
                t_user_cq=t_user_cq,
                t_users=t_users,
                t_rec_contarct_type=t_rec_contarct_type,
                t_income_type=t_income_type,
                t_users_kf=t_users_kf,
                pagination=pagination,
                t_projects=t_projects,
                t_project_bussniss=t_project_bussniss,
                t_building=t_building,
                t_business_channel=t_business_channel,
                t_sign_type=t_sign_type,
                t_company=t_company,
                t_talk_type=t_talk_type,

                form_tag="my",
                tag=tag,
                search_key="",
                # categorys=categorys,
                style=style,
                t_user_group=t_user_group)




        elif tag == "search":
            role=int(self.get_secure_cookie('role'))
            name=self.get_secure_cookie('name')
            page = int(self.get_argument("page", 1))
            key = self.get_argument("key","")
            self.set_secure_cookie("search_key", key, expires_days=30)
            pre_page = 20
            search_sql = "%"+key +"%"
            # ret_sql = ""
            # add_search_sql = ""
            # if role == "1":
            #     pass
            # elif role == "6":
            #     search_sql = ""
            # elif role == "7":
            #     search_sql = ""
            # elif role == "9":
            #     search_sql = " and "
            #     ret_sql = " and a.uid={0}".format(uid)
            if role==9:
                count = self.db.get(

                    '''SELECT count(*) count FROM t_projects a  inner join t_projects_member b on a.id=b.project_id and b.team_id=38
                        left join (select project_id,group_concat(company) old_companys from t_projects_company_history group by project_id ) c on a.id=c.project_id                        
                    where  member_id=%s and id=%s''',uid,key)
                pagination = Pagination(page, pre_page, count.count, self.request)
                startpage = (page - 1) * pre_page

                t_projects=self.db.query(
                        '''
                        SELECT a.*, b.member_name ,c.old_companys   FROM t_projects a  inner join t_projects_member b
                        on a.id=b.project_id and b.team_id=38
                        left join (select project_id,group_concat(company) old_companys from t_projects_company_history group by project_id ) c on a.id=c.project_id
                        where   member_id=%s and id=%s order by a.created_at desc limit %s,%s
                            ''', uid,key, startpage, pre_page)
            elif role==13:
                count = self.db.get(
                         '''SELECT count(*) count FROM t_projects a
                         inner join t_projects_member b on a.id=b.project_id and b.team_id=36
                        left join (select project_id,group_concat(company) old_companys from t_projects_company_history group by project_id ) c on a.id=c.project_id
                        where  member_id=%s and id=%s''',uid,key)
                pagination = Pagination(page, pre_page, count.count, self.request)
                startpage = (page - 1) * pre_page

                t_projects=self.db.query(
                        '''
                        SELECT a.*, b.member_name , c.old_companys  FROM t_projects a  inner join t_projects_member b
                        on a.id=b.project_id and b.team_id=36
                        left join (select project_id,group_concat(company) old_companys from t_projects_company_history group by project_id ) c on a.id=c.project_id
                        where   member_id=%s and id=%s order by a.created_at desc limit %s,%s
                            ''', uid,key, startpage, pre_page)

            else:
                t_projects= self.db.query("SELECT  a.* , b.name  FROM t_projects a , t_user b where a.uid=b.id and a.id=%s",key)

            if t_projects and role!=9:
                count= self.db.get("""
                SELECT  count(*) count FROM t_projects a inner join t_user b on a.uid=b.id
                left join (select project_id,group_concat(company) old_companys from t_projects_company_history group by project_id ) c on a.id=c.project_id
                 where a.id=%s""",key)
                pagination = Pagination(page, pre_page, count.count, self.request)
                startpage = (page - 1) * pre_page
                t_projects= self.db.query("""
                SELECT  a.* , b.name , c.old_companys  FROM t_projects a inner join t_user b
                on a.uid=b.id  
                left join (select project_id,group_concat(company) old_companys from t_projects_company_history group by project_id ) c on a.id=c.project_id
                where a.id=%s limit %s,%s
                """,key,startpage,pre_page)
                #                 left join t_projects_relation c on
                # relation_ids like "%%,"""+key+""",%%" or relation_ids REGEXP  "^"""+key+""","
                # left join t_projects d on find_in_set(d.id,c.relation_ids)
            else:
                if role==9:
                    count = self.db.get(
                        '''SELECT count(*) count FROM t_projects a  inner join t_projects_member b on a.id=b.project_id and b.team_id=38
                        left join (select project_id,group_concat(company) old_companys from t_projects_company_history group by project_id ) c on a.id=c.project_id                        
                        where  member_id=%s and (project_name like "%''' + search_sql
                        + '''%" or customer_tel like "%''' + search_sql +'''%" or customer_company like "%''' + search_sql +
                        '''%" or a.remark like "%''' + search_sql +
                        '''%" or customer_name like "%''' + search_sql + '''%"
                        or a.id in (select project_id from t_projects_company_history where company like "%''' + search_sql + '''%" )
                        )''',
                        uid)
                    pagination = Pagination(page, pre_page, count.count, self.request)
                    startpage = (page - 1) * pre_page

                    t_projects=self.db.query(
                        '''
                        SELECT a.*, b.member_name  , c.old_companys   FROM t_projects a  inner join t_projects_member b
                        on a.id=b.project_id and b.team_id=38
                        left join (select project_id,group_concat(company) old_companys from t_projects_company_history group by project_id ) c on a.id=c.project_id
                        where   member_id=%s and (project_name like "%''' + search_sql +
                        '''%" or customer_tel like "%''' + search_sql +'''%" or customer_company like "%''' + search_sql +
                        '''%" or a.remark like "%''' + search_sql +
                        '''%" or customer_name like "%''' + search_sql + '''%"
                        or a.id in (select project_id from t_projects_company_history where company like "%''' + search_sql + '''%"
                        ))
                            order by a.created_at desc limit %s,%s
                            ''', uid, startpage, pre_page)

                elif role==13:
                    count = self.db.get(
                        '''SELECT count(*) count FROM t_projects a  inner join t_projects_member b on a.id=b.project_id and b.team_id=36
                        where  member_id=%s and (project_name like "%''' + search_sql
                        + '''%" or customer_tel like "%''' + search_sql +'''%" or customer_company like "%''' + search_sql +
                        '''%" or a.remark like "%''' + search_sql +
                        '''%" or customer_name like "%''' + search_sql + '''%"
                        or a.id in (select project_id from t_projects_company_history where company like "%''' + search_sql + '''%"
                        ))''',
                        uid)
                    pagination = Pagination(page, pre_page, count.count, self.request)
                    startpage = (page - 1) * pre_page

                    t_projects=self.db.query(
                        '''
                        SELECT a.*, b.member_name  , c.old_companys   FROM t_projects a  inner join t_projects_member b
                        on a.id=b.project_id and b.team_id=36
                        left join (select project_id,group_concat(company) old_companys from t_projects_company_history group by project_id ) c on a.id=c.project_id
                        where   member_id=%s and (project_name like "%''' + search_sql +
                        '''%" or customer_tel like "%''' + search_sql +'''%" or customer_company like "%''' + search_sql +
                        '''%" or a.remark like "%''' + search_sql +
                        '''%" or customer_name like "%''' + search_sql + '''%"
                        or a.id in (select project_id from t_projects_company_history where company like "%''' + search_sql + '''%"
                        ))
                            order by a.created_at desc limit %s,%s
                            ''', uid, startpage, pre_page)


                elif role==1:
                    count = self.db.get(
                    '''SELECT count(*) count FROM t_projects a inner join  t_user b on a.uid=b.id 
                        left join (select project_id,group_concat(company) old_companys from t_projects_company_history group by project_id ) c on a.id=c.project_id                    
                     where (project_name like "%'''
                    + search_sql + '''%"  or customer_tel like "%''' + search_sql +'''%" or customer_company like "%''' + search_sql +
                        '''%" or a.remark like "%''' + search_sql +
                    '''%" or customer_name like "%''' + search_sql + '''%"
                    or a.id in (select project_id from t_projects_company_history where company like "%''' + search_sql + '''%"
                    )) and b.name=%s ''',name)
                    pagination = Pagination(page, pre_page, count.count, self.request)
                    startpage = (page - 1) * pre_page
                    t_projects = self.db.query(
                    '''
                    SELECT  a.* , b.name , c.old_companys  FROM t_projects a inner join  t_user b on a.uid=b.id
                        left join (select project_id,group_concat(company) old_companys from t_projects_company_history group by project_id ) c on a.id=c.project_id                    
                     where (project_name like "%'''
                    + search_sql + '''%" or customer_tel like "%''' + search_sql +'''%" or customer_company like "%''' + search_sql +
                        '''%" or a.remark like "%''' + search_sql +
                    '''%" or customer_name like "%''' + search_sql + '''%" 
                    or a.id in (select project_id from t_projects_company_history where company like "%''' + search_sql + '''%"
                    )) and b.name=%s
                    order by created_at desc limit %s,%s
                    ''', name,startpage, pre_page)
                else:
                    count = self.db.get(
                        ''' SELECT count(*) count FROM t_projects a inner join  t_user b on a.uid=b.id 
                        left join (select project_id,group_concat(company) old_companys from t_projects_company_history group by project_id ) c on a.id=c.project_id                        
                         where (project_name like "%'''
                        + search_sql + '''%"  or customer_tel like "%''' + search_sql +
                        '''%" or customer_name like "%''' + search_sql +
                        '''%" or customer_company like "%''' + search_sql +
                        '''%" or a.remark like "%''' + search_sql +
                        '''%"
                         or a.id in (select project_id from t_projects_company_history where company like "%''' + search_sql + '''%"
                        )) ''')
                    pagination = Pagination(page, pre_page, count.count, self.request)
                    startpage = (page - 1) * pre_page
                    t_projects = self.db.query(
                        '''
                        SELECT  a.* , b.name , c.old_companys  FROM t_projects a inner join t_user b on a.uid=b.id 
                        left join (select project_id,group_concat(company) old_companys from t_projects_company_history group by project_id ) c on a.id=c.project_id                        
                         where (project_name like "%'''
                        + search_sql + '''%" or customer_tel like "%''' + search_sql +
                        '''%" or customer_name like "%''' + search_sql +
                        '''%" or customer_company like "%''' + search_sql +
                        '''%" or a.remark like "%''' + search_sql +
                        '''%" or a.company_history like "%'''+search_sql+
                        '''%"
                        or a.id in (select project_id from t_projects_company_history where company like "%''' + search_sql + '''%"
                        ))
                        order by created_at desc limit %s,%s
                        ''', startpage, pre_page)

            return self.render(
                'project/projects_search.html',
                pagination=pagination,
                t_projects=t_projects,
                form_tag="list",search_key=key)

        elif tag =="projects_state":
            t_user_teams_cq = None
            t_cq_service = None
            ntag = self.get_argument("ntag","")
            last_milepost_id = self.get_argument("last_milepost_id", 0)
            btype_id = self.get_argument("btype_id","")
            is_ok = self.get_argument("is_ok","")
            page = int(self.get_argument("page", 1))
            cq = self.get_argument("cq", "")
            kefu = self.get_argument("kefu", "")
            building_id = self.get_argument("building_id", "")
            income_bussniss = self.get_argument("income_bussniss", "")
            from_id = self.get_argument("from_id", "")
            start = self.get_argument("start", "")
            end = self.get_argument("end", "")
            sales = self.get_argument("sales", "")
            qc_key = self.get_argument("qc_key","")
            confirm = self.get_argument("confirm","")
            cq_btype_id=self.get_argument("cq_btype_id","")
            department_id= self.get_argument("department_id","")
            team_id = self.get_argument("team_id","38")
            from_tag_where = self.get_argument("from_tag_where","")
            params = {
                "sales": sales,
                "income_bussniss": income_bussniss,
                "cq": cq,
                "kefu": kefu,
                "from_id": from_id,
                "building_id": building_id,
                "start": start,
                "end": end,
                "last_milepost_id":last_milepost_id,
                "ntag":ntag,
                "qc_key":qc_key,
                "confirm":confirm,
                "cq_btype_id":cq_btype_id,
                "btype_id":btype_id,
                "department_id":department_id,
                "team_id":team_id,
                "from_tag_where":from_tag_where
            }
            add_sql = ""
            sql_cq_btype_id=''
            sql_income_bussniss = ""
            sql_cq = ""
            sql_kefu = ""
            sql_from_id = ""
            sql_building_id = ""
            sql_date = ""
            sql_sales = ""
            sql_qc_key = ""
            sql_btype=""
            sql_cq_add = ""
            if cq_btype_id and cq_btype_id != "0":
                sql_cq_btype_id = "  and  a.id in (select project_id from t_projects_member aaaa where     aaaa.project_id=a.id and btype_id=%s) " % cq_btype_id
            if income_bussniss and income_bussniss != "0":
                sql_income_bussniss = " and a.id in (select project_id from t_projects_service_income aaaa where  service_money > 0 and  service_id=%s and aaaa.project_id=a.id)  " % (
                    income_bussniss)
            if btype_id:
                sql_btype = " and  a.id in (select project_id from t_projects_member aaaa  where  btype_id=%s)  " % (
                    btype_id)

            if cq and cq != "0":
                sql_cq = " and  a.id in (select project_id from t_projects_member aaaa  where  team_id=38 and member_id=%s and aaaa.project_id=a.id)  " % (
                    cq)
                sql_cq_add = " and member_id='"+cq+"'"
            if kefu and kefu != "0":
                sql_kefu = "and  a.id in (select project_id from t_projects_member aaaa where  team_id=39 and member_id=%s and aaaa.project_id=a.id) " % (
                    kefu)
            if from_id and from_id != "0":
                sql_from_id = " and a.busniess_from_id=%s" % (from_id)
            if building_id and building_id != "0":
                sql_building_id = " and a.building_id=%s" % (building_id)
            if sales and sales != "0":
                sql_sales = "and  a.id in (select project_id from t_projects_member aaaa where  btype_id >0 and member_id=%s and aaaa.project_id=a.id) " % (
                    sales)
            if start and end:
                sql_date = " and a.created_at between '%s' and '%s'" % (start, end)
            if qc_key:
                sql_qc_key += ''' and (id like "%%'''+qc_key+'''%%" or project_name like   "%%''' + qc_key + '''%%"  or customer_name like   "%%''' + qc_key + '''%%"  or customer_tel like   "%%''' + qc_key + '''%%" or customer_company like   "%%''' + qc_key + '''%%")'''
            department_id_sql,department_id_sql1="",""
            if department_id :
                department_id_sql=" and project_department_id={}  and team_id={} ".format(department_id,team_id)
                department_id_sql1=" and project_department_id={} ".format(department_id)

            add_sql = sql_cq_btype_id + sql_income_bussniss + sql_cq + sql_sales + sql_kefu + sql_from_id + sql_building_id + sql_date + sql_qc_key + sql_btype

 
# or  is_cancel=0 or  not_transition=0
            wait_count = self.db.get(
                '''              SELECT count(*) count from t_projects a  where id not in(
                        select project_id from t_projects_member aa,t_projects bb
                        where aa.project_id=bb.id and   (btype_id>0  or not_transition=1 or is_cancel=1)   group by project_id    ) and is_acc=0 and  project_department_id=0
                    ''' + add_sql)

            not_transition_count = self.db.get('''          SELECT  count(*) count

                FROM t_projects a
                    inner join t_projects_member b on btype_id > 0
                    and  a.id=b.project_id and not_transition=1 
                    '''+add_sql+department_id_sql)

            cancel_wait_count1 = self.db.get('''
            SELECT  count(*) count
                FROM t_projects a
                    inner join t_projects_member b on  btype_id <> 0
                    and  a.id=b.project_id and is_cancel=1 and is_cancel_confirm_at is null and project_department_id =0
                    '''+add_sql+department_id_sql)

            cancel_confirm_count1 = self.db.get('''
            SELECT  count(*) count
                FROM t_projects a
                    inner join t_projects_member b on  btype_id >0
                    and  a.id=b.project_id and is_cancel=1 and is_cancel_confirm_at is not null
                    '''+add_sql+department_id_sql)
                
            department_id_count = self.db.get(''' 
                    select count(*) count from t_projects a where id not in(
                    select project_id from t_projects_member
                    where  team_id=205 and btype_id>0 
                    ) and project_department_id=1
                    '''.format(team_id)+add_sql)

            dis_banjie_count=self.db.get('''
              SELECT   count(*) count
                      FROM t_projects
                    a inner join t_projects_member b on a.id=b.project_id and not_transition=0
                    
and btype_id > 0
                    where  is_cancel=0 and last_milepost_id  in (162,167) and btype_id=155 '''  
                                           +department_id_sql)
            is_banjie_count=self.db.get('''
              SELECT   count(*) count
                      
                     FROM t_projects
                    a inner join t_projects_member b on a.id=b.project_id and not_transition=0
                    
and btype_id > 0
                    where  is_cancel=0 and last_milepost_id not in (162,167) and btype_id=155 '''  
                                           +department_id_sql)       
            if last_milepost_id or ntag in ['dis_banjie','is_banjie']:
                # print "last_milepost_id", last_milepost_id
                if last_milepost_id:
                    add_sql += " and last_milepost_id=" + last_milepost_id
                elif ntag=='dis_banjie':
                    add_sql+=" and last_milepost_id in (162,167) and btype_id=155 "
                elif ntag=='is_banjie':
                    add_sql+=" and last_milepost_id not in (162,167) and btype_id=155 "

                pre_page = 20
                _btype_sql=""
                if btype_id:
                    _btype_sql =" and b.btype_id =%s "%(btype_id)
                else:
                    _btype_sql =" and b.btype_id > 0  "
                print '''  SELECT   count(*) count
                      
                     FROM t_projects
                    a inner join t_projects_member b on a.id=b.project_id and not_transition=0
                    
and btype_id > 0
                    where  is_cancel=0 ''' + _btype_sql + add_sql +department_id_sql+sql_cq_add 

                count = self.db.get('''    SELECT   count(*) count
                      
                     FROM t_projects
                    a inner join t_projects_member b on a.id=b.project_id and not_transition=0
                    
and btype_id > 0
                    where  is_cancel=0 ''' + _btype_sql + add_sql +
                                           sql_cq_add+department_id_sql)

                pagination = Pagination(page, pre_page, count.count, self.request)
                startpage = (page - 1) * pre_page
                print '''
                    SELECT  a.* ,b.mid,b.member_name,b.btype_id_name,
                    b.last_milepost_id_name,last_milepost_id_at,b.created_at cq_created_at
                     FROM t_projects
                    a inner join t_projects_member b on a.id=b.project_id and not_transition=0
                    
and btype_id > 0
                    where  is_cancel=0 ''' + _btype_sql + add_sql +department_id_sql+ sql_cq_add
                t_projects = self.db.query('''
                    SELECT  a.* ,b.mid,b.member_name,b.btype_id_name,
                    b.last_milepost_id_name,last_milepost_id_at,b.created_at cq_created_at
                     FROM t_projects
                    a inner join t_projects_member b on a.id=b.project_id and not_transition=0
                    
and btype_id > 0
                    where  is_cancel=0 ''' + _btype_sql + add_sql +department_id_sql+
                                           sql_cq_add + '''
                                    order by b.created_at desc limit %s,%s
                    ''', startpage, pre_page)
                print('''
                SELECT  a.* ,b.mid,b.member_name,b.btype_id_name,
                    b.last_milepost_id_name,last_milepost_id_at,b.created_at cq_created_at
                     FROM t_projects
                    a inner join t_projects_member b on a.id=b.project_id and not_transition=0
                    
and btype_id > 0
                    where  is_cancel=0 ''' + _btype_sql + add_sql +department_id_sql+
                                           sql_cq_add + '''
                                    order by b.created_at desc
                ''')

            elif ntag == "wait":
                add_inner_sql=" "
                if   department_id:
                    count = department_id_count
                    # add_inner_sql=" and team_id={} ".format(team_id)
                else:
                    # add_sql+=""" and project_department_id = 0""" 
                    count = wait_count
                pre_page = 20
               
                pagination = Pagination(page, pre_page, count.count,
                                        self.request)
                startpage = (page - 1) * pre_page
                print add_sql
                # t_projects = self.db.query('''
                #             SELECT a.*,

                # b.bsa
                # FROM t_projects a
                #     left  join (select project_id,GROUP_CONCAT(btype_id_name) bsa
                #     from t_projects_member  where btype_id <> 0 '''+add_inner_sql+''' group by project_id ) b
                #     on a.id=b.project_id

                #            where   bsa is null   and is_acc=0
                #         ''' + add_sql + '''
                #         order by a.created_at desc limit %s,%s
                #         ''', startpage, pre_page)
  
                t_projects = self.db.query('''
                        select a.* from t_projects a  where id not in(
                        select project_id from t_projects_member a
                        where  (btype_id>0  or not_transition=1 or is_cancel=1)  ) and is_acc=0 and  project_department_id=0
                       
                        order by created_at desc limit %s,%s
                        ''', startpage, pre_page)
            elif ntag == "wait_department":
                add_inner_sql=" "
                add_sql+=""" and project_department_id ={}""".format(department_id,team_id)
                count = department_id_count
                add_inner_sql=" and team_id={} ".format(team_id)
                pre_page = 20
               
                pagination = Pagination(page, pre_page, count.count,
                                        self.request)
                startpage = (page - 1) * pre_page
                print '''  select a.* from t_projects a  where id not in(
                        select project_id from t_projects_member 
                        where  team_id=%s and btype_id>0  ) and project_department_id=%s   and is_acc=0
                       '''%(team_id,department_id)+add_sql

                # t_projects = self.db.query('''
                #         select a.* from t_projects a  where id not in(
                #         select project_id from t_projects_member 
                #         where  team_id=%s and btype_id>0 ) and project_department_id=%s   and is_acc=0
                #        '''+add_sql+''' order by created_at desc limit %s,%s
                #         ''',team_id,department_id, startpage, pre_page)

                t_projects = self.db.query('''
                          select  *  from t_projects a where id not in(
                    select project_id from t_projects_member
                    where  team_id=205 and btype_id>0 
                    ) and project_department_id=1 order by created_at desc limit %s,%s
                        ''', startpage, pre_page)                
            elif ntag =="is_cancel":
                pre_page = 20
                count = cancel_wait_count1
                pagination = Pagination(page, pre_page, count.count,
                                        self.request)
                startpage = (page - 1) * pre_page
                sql = ""
                t_projects = self.db.query('''
                         SELECT a.*,member_name bsa

                FROM t_projects a
                    inner join t_projects_member b on btype_id >0
                    and  a.id=b.project_id and is_cancel=1 and is_cancel_confirm_at is null
                    '''+add_sql+department_id_sql+'''
                        order by a.created_at desc limit %s,%s
                        ''', startpage, pre_page)

                        
            elif ntag == "is_cancel_confirm":
                pre_page = 20
                count = cancel_confirm_count1
                pagination = Pagination(page, pre_page, count.count,
                                        self.request)
                startpage = (page - 1) * pre_page
                sql = ""
                t_projects = self.db.query('''
                         SELECT a.*,member_name bsa
                FROM t_projects a
                    inner join t_projects_member b on btype_id<> 0
                    and  a.id=b.project_id and is_cancel=1 and is_cancel_confirm_at is not  null
                    '''+add_sql+department_id_sql+'''
                        order by a.created_at desc limit %s,%s
                        ''', startpage, pre_page)

            elif ntag == "not_transition":
                pre_page = 20
                count = not_transition_count
                pagination = Pagination(page, pre_page, count.count,
                                        self.request)
                startpage = (page - 1) * pre_page
                sql = ""
                # print "add_sql",add_sql
                t_projects = self.db.query('''
                         SELECT a.*,member_name bsa

                FROM t_projects a
                    inner join t_projects_member b on btype_id > 0
                    and  a.id=b.project_id  and not_transition=1
                    '''+add_sql+department_id_sql+'''
                        order by a.created_at desc limit %s,%s
                        ''', startpage, pre_page)
            else:
                pre_page = 20
                count = self.db.get('''
                 SELECT   count(*) count
                FROM t_projects a
                    left join (select project_id,GROUP_CONCAT(concat(member_name,'(',btype_id_name,')')) bsa
                    from t_projects_member aa,t_projects bb where aa.project_id=bb.id and  btype_id >0 '''+department_id_sql+''' group by project_id ) b
                    on a.id=b.project_id where is_lock=0  ''' + add_sql+department_id_sql1)
                pagination = Pagination(page, pre_page, count.count,
                                        self.request)
                startpage = (page - 1) * pre_page

                t_projects = self.db.query('''
                            SELECT a.*,

                b.bsa
                FROM t_projects a
                    left join (select project_id,GROUP_CONCAT(concat(member_name,'(',btype_id_name,')')) bsa
                    from t_projects_member aa,t_projects bb where aa.project_id=bb.id and   btype_id >0  '''+department_id_sql+''' group by project_id ) b
                    on a.id=b.project_id where is_lock=0   '''+add_sql+department_id_sql1+'''
                        order by a.created_at desc limit %s,%s
                        ''', startpage, pre_page)
                print ''' SELECT a.*,

                b.bsa
                FROM t_projects a
                    left join (select project_id,GROUP_CONCAT(concat(member_name,'(',btype_id_name,')')) bsa
                    from t_projects_member aa,t_projects bb where aa.project_id=bb.id and   btype_id >0  '''+department_id_sql+''' group by project_id ) b
                    on a.id=b.project_id where is_lock=0   '''+add_sql

            if not from_tag_where:
                department_id_sql=""
            if not btype_id:
                project_btypes = self.db.query(
                    """select *,(select count(*)  from t_projects_member aa,t_projects bb where aa.project_id=bb.id and last_milepost_id=a.id and  not_transition=0 and is_lock=0   and is_cancel=0 """+department_id_sql+""") c
                    from t_projects_type a where income_category='办结'  order by order_int"""
                )
            else:
                project_btypes = self.db.query(
                    """select *,(select count(*)  from t_projects_member aa,t_projects bb where aa.project_id=bb.id and last_milepost_id=a.id  and
                   btype_id=%s and  not_transition=0 and is_lock=0   and is_cancel=0  """+department_id_sql+""") c
                from t_projects_type a where income_category='办结' order by order_int""",
                    btype_id)
            t_project_bussniss = self.db.query(
                """select * from t_projects_type where income_category='业务类型' order by order_int  """
            )
            t_project_type = self.db.query(
                """select * from t_projects_type where income_category='业务分类' order by ext_type_id  """
            )
            t_income_type = self.db.query("""
                select * from t_projects_type where income_category='业务来源' order by order_int desc
                """)

            t_sign_type = self.db.query("""
                select * from t_projects_type where income_category='签约方式' order by order_int desc
                """)
            t_talk_type = self.db.query(
                "select * from t_projects_type where income_category='沟通方式' order by order_int desc "
            )
            t_company = self.db.query("""
                select * from t_projects_type where income_category='收入公司' order by order_int desc
                """)
            t_business_channel = self.db.query("""
                select * from t_projects_type where income_category='推广来源渠道' order by order_int desc
                """)
            t_building = self.db.query(
                "select * from t_projects_type where income_category='楼盘' order by order_int desc "
            )
            t_users_kf = self.db.query("select * from t_user  where role=6")
            t_rec_contarct_type = self.db.query(
                "select * from t_projects_type where income_category='合同确认' order by order_int desc "
            )
            t_user_group = self.db.query("select * from t_user_group")
            t_users = self.db.query(
                "SELECT * FROM t_user_teams a , t_user b where b.id=a.uid ")

            t_user_cq = self.db.query("SELECT * FROM t_user  where role=9 ")
            t_user_sales = self.db.query(
                "SELECT * FROM t_user_teams a , t_user b where b.id=a.uid and team_id=1 "
            )
            t_user_teams_cq=self.db.query(
                   """
                    select a.*,b.team_id from t_user a inner join t_user_teams b on a.id=b.uid where b.team_id=5
                    """
                    )
            t_cq_service = self.db.query(
                    "select * from t_projects_type where income_category='业务分类' order by order_int desc "
                )
            t_cq_department = self.db.query(  "select * from t_user_department where  is_used=1 order by order_int desc ")
            return self.render(
                'project/projects_state.html',
                dis_banjie_count=dis_banjie_count,
                is_banjie_count=is_banjie_count,
                t_cq_department=t_cq_department,
                t_project_type=t_project_type,
                cancel_wait_count1=cancel_wait_count1,
                cancel_confirm_count1=cancel_confirm_count1,
                params=params,
                t_user_sales=t_user_sales,
                t_user_cq=t_user_cq,
                t_users=t_users,
                t_rec_contarct_type=t_rec_contarct_type,
                t_income_type=t_income_type,
                t_users_kf=t_users_kf,
                pagination=pagination,
                t_projects=t_projects,
                t_project_bussniss=t_project_bussniss,
                t_building=t_building,
                t_business_channel=t_business_channel,
                t_sign_type=t_sign_type,
                t_company=t_company,
                t_talk_type=t_talk_type,
                ntag=ntag,
                is_ok=is_ok,
                t_user_teams_cq=t_user_teams_cq,
                t_cq_service=t_cq_service,
                not_transition_count=not_transition_count,
                wait_count=wait_count,
                project_btypes=project_btypes,
                last_milepost_id=last_milepost_id,
                tag=tag,
                department_id_count=department_id_count,
                dt=dt,
                diff_date=self.diff_date,
                search_key="")

        elif tag =="projects_state_type":
            t_user_teams_cq = None
            t_cq_service = None
            ntag = self.get_argument("ntag","")
            last_milepost_id = self.get_argument("last_milepost_id", 0)

            is_ok = self.get_argument("is_ok","")
            page = int(self.get_argument("page", 1))
            cq = self.get_argument("cq", "")
            kefu = self.get_argument("kefu", "")
            kfgw=self.get_argument('kfgw',"")
            building_id = self.get_argument("building_id", "")
            income_bussniss = self.get_argument("income_bussniss", "")
            from_id = self.get_argument("from_id", "")
            start = self.get_argument("start", "")
            end = self.get_argument("end", "")
            sales = self.get_argument("sales", "")
            qc_key = self.get_argument("qc_key","")
            confirm = self.get_argument("confirm","")
            cq_btype_id = self.get_argument("cq_btype_id", "158")

            if cq_btype_id!="158":
                return "error"
            params = {
                "sales": sales,
                "income_bussniss": income_bussniss,
                "cq": cq,
                "kefu": kefu,
                "kfgw":kfgw,
                "from_id": from_id,
                "building_id": building_id,
                "start": start,
                "end": end,
                "last_milepost_id":last_milepost_id,
                "ntag":ntag,
                "qc_key":qc_key,
                "confirm":confirm,
                "cq_btype_id":cq_btype_id
            }
            add_sql = ""
            sql_cq_btype_id=''
            sql_income_bussniss = ""
            sql_cq = ""
            sql_kefu = ""
            sql_kfgw=""
            sql_from_id = ""
            sql_building_id = ""
            sql_date = ""
            sql_sales = ""
            sql_qc_key = ""
            default_sql=""
            sql_cq_add = ""
            sql_cq_btype_id_count ="  and  a.id in (select project_id from t_projects_member aaaa where  btype_id=%s  and aaaa.project_id=a.id) "%cq_btype_id

            if ntag=="wait":
                default_sql = "  inner join t_projects_service_income c    on  service_id=9   and a.id=c.project_id and service_money > 0"


            if  cq_btype_id and cq_btype_id != "0" and ntag!="wait":
                sql_cq_btype_id ="  and  a.id in (select project_id from t_projects_member aaaa where  btype_id=%s  and aaaa.project_id=a.id) "%cq_btype_id
                # sql_cq_btype_id +="  or  a.id in (select project_id from t_projects_service_income bbbb where  bbbb.service_id=9  and service_money > 0 and bbbb.project_id=a.id) "
            if income_bussniss and income_bussniss != "0":
                sql_income_bussniss = " and a.id in (select project_id from t_projects_service_income aaaa where  service_money > 0 and  service_id=%s and aaaa.project_id=a.id)  " % (
                    income_bussniss)
            if cq and cq != "0":
                sql_cq = " and  a.id in (select project_id from t_projects_member aaaa  where  team_id=38 and member_id=%s and aaaa.project_id=a.id)  " % (
                    cq)
                sql_cq_add = " and member_id='"+cq+"'"
            if kefu and kefu != "0":
                sql_kefu = "and  a.id in (select project_id from t_projects_member aaaa where  team_id=39 and member_id=%s and aaaa.project_id=a.id) " % (
                    kefu)
            if kfgw and kfgw != "0":
                sql_kfgw = "and  a.id in (select project_id from t_projects_member aaaa where  team_id=36 and member_id=%s and aaaa.project_id=a.id) " % (
                    kfgw)
            if from_id and from_id != "0":
                sql_from_id = " and a.busniess_from_id=%s" % (from_id)
            if building_id and building_id != "0":
                sql_building_id = " and a.building_id=%s" % (building_id)
            if sales and sales != "0":
                sql_sales = "and  a.id in (select project_id from t_projects_member aaaa where  team_id=34 and member_id=%s and aaaa.project_id=a.id) " % (
                    sales)
            if start and end:
                sql_date = " and a.created_at between '%s' and '%s'" % (start, end)
            if qc_key:
                sql_qc_key += ''' and (id = "'''+qc_key+'''" or project_name like   "%%''' + qc_key + '''%%"  or customer_name like   "%%''' + qc_key + '''%%"  or customer_tel like   "%%''' + qc_key + '''%%" or customer_company like   "%%''' + qc_key + '''%%")'''

            add_sql = sql_cq_btype_id+sql_income_bussniss + sql_cq + sql_sales + sql_kefu+sql_kfgw+ sql_from_id + sql_building_id + sql_date+sql_qc_key



            wait_count = self.db.get(
                '''                                      SELECT  count(*) count
                     from t_projects a 
                    
                    where id not in(
                                    select aa.project_id from t_projects_member aa
                                    inner join t_projects bb on   bb.id=aa.project_id 
                                    inner join t_projects_service_income cc    on  service_id=9   and bb.id=cc.project_id 
                                    where  (btype_id>0  or not_transition=1 or is_cancel=1)  ) and is_acc=0 and  project_department_id=0
                    ''')
            wait_count1 = self.db.get('''          SELECT  count(*) count
                FROM t_projects a
                 '''+default_sql+'''
                    inner join t_projects_member b on (team_id=38 or team_id=205)
                    and  a.id=b.project_id and not_transition=1 and is_cancel=0
                    '''+sql_cq_btype_id_count)
            cancel_wait_count1 = self.db.get('''
            SELECT  count(*) count
                FROM t_projects a
                 '''+default_sql+'''
                    inner join t_projects_member b on team_id=38
                    and  a.id=b.project_id and is_cancel=1 and is_cancel_confirm_at is null
                    '''+sql_cq_btype_id_count)

            cancel_confirm_count1 = self.db.get('''
            SELECT  count(*) count
                FROM t_projects a
                 '''+default_sql+'''
                    inner join t_projects_member b on team_id=38
                    and  a.id=b.project_id and is_cancel=1 and is_cancel_confirm_at is not null
                    '''+sql_cq_btype_id_count)



            if last_milepost_id:
                # print "last_milepost_id", last_milepost_id
                add_sql += " and last_milepost_id=" + last_milepost_id
                pre_page = 20
                count = self.db.get('''    SELECT   count(*) count
                     FROM t_projects
                      '''+default_sql+'''
                    a inner join t_projects_member b on a.id=b.project_id


                    where  b.btype_id <> 0  and is_cancel=0
               ''' + add_sql + sql_cq_add + sql_cq_btype_id_count)
                pagination = Pagination(page, pre_page, count.count, self.request)
                startpage = (page - 1) * pre_page

                t_projects = self.db.query(
                    '''
                    SELECT  a.* ,b.mid,b.member_name,b.btype_id_name,concat(ifnull(b.zone_id_name,''),'|',mid,'|',member_name,'|',btype_id_name,'|',b.zone_id) gszm,
                    b.last_milepost_id_name,last_milepost_id_at,b.created_at cq_created_at
                     FROM t_projects
                      '''+default_sql+'''
                    a inner join t_projects_member b on a.id=b.project_id


                    where  b.btype_id <> 0  '''+add_sql+sql_cq_add+''' and is_cancel=0
                                    order by b.created_at desc limit %s,%s
                    ''', startpage, pre_page)

            elif ntag == "wait":

                pre_page = 20
                count = wait_count
                pagination = Pagination(page, pre_page, count.count,
                                        self.request)
                startpage = (page - 1) * pre_page
                # print add_sql,"___"

                t_projects = self.db.query('''
                    select a.*,"" bsa from t_projects a 
                    
                    
                    where id not in(
                                    select aa.project_id from t_projects_member aa
                                    inner join t_projects bb on   bb.id=aa.project_id 
                                    inner join t_projects_service_income cc    on  service_id=9   and bb.id=cc.project_id 
                                    where  (btype_id>0  or not_transition=1 or is_cancel=1)  ) and is_acc=0 and  project_department_id=0
                       
                     
                        order by a.created_at desc limit %s,%s
                        ''', startpage, pre_page)

            elif ntag =="is_cancel":
                pre_page = 20
                count = cancel_wait_count1
                pagination = Pagination(page, pre_page, count.count,
                                        self.request)
                startpage = (page - 1) * pre_page
                sql = ""
                t_projects = self.db.query('''
                         SELECT a.*,member_name bsa,
                concat(ifnull(b.zone_id_name,''),'|',mid,'|',member_name,'|',btype_id_name,'|',b.zone_id) gszm
                FROM t_projects a
                 '''+default_sql+'''
                    inner join t_projects_member b on team_id=38
                    and  a.id=b.project_id and is_cancel=1 and is_cancel_confirm_at is null
                    '''+add_sql+'''
                        order by a.created_at desc limit %s,%s
                        ''', startpage, pre_page)
            elif ntag == "is_cancel_confirm":
                pre_page = 20
                count = cancel_confirm_count1
                pagination = Pagination(page, pre_page, count.count,
                                        self.request)
                startpage = (page - 1) * pre_page
                sql = ""
                t_projects = self.db.query('''
                         SELECT a.*,member_name bsa,concat(ifnull(b.zone_id_name,''),'|',mid,'|',member_name,'|',btype_id_name,'|',b.zone_id) gszm
                FROM t_projects a
                 '''+default_sql+'''
                    inner join t_projects_member b on team_id=38
                    and  a.id=b.project_id and is_cancel=1 and is_cancel_confirm_at is not  null
                    '''+add_sql+'''
                        order by a.created_at desc limit %s,%s
                        ''', startpage, pre_page)

            elif ntag == "not_transition":
                pre_page = 20
                count = wait_count1
                pagination = Pagination(page, pre_page, count.count,
                                        self.request)
                startpage = (page - 1) * pre_page
                sql = ""
                # print "add_sql",add_sql
                t_projects = self.db.query('''
                         SELECT a.*,concat(member_name) bsa,
                         concat(ifnull(b.zone_id_name,''),'|',mid,'|',member_name,'|',btype_id_name,'|',b.zone_id) gszm
                FROM t_projects a
                 '''+default_sql+'''
                    inner join t_projects_member b on (team_id=38)
                    and  a.id=b.project_id  and not_transition=1
                    '''+add_sql+'''
                        order by a.created_at desc limit %s,%s
                        ''', startpage, pre_page)
            else:
                pre_page = 20
                count = self.db.get('''
                 SELECT   count(*) count
                FROM t_projects a
                 '''+default_sql+'''
                    left join (select project_id,GROUP_CONCAT(concat(member_name,'(',btype_id_name,')')) bsa
                    from t_projects_member aa,t_projects bb where aa.project_id=bb.id and  team_id=38 group by project_id ) b
                    on a.id=b.project_id where is_lock=0  ''' + add_sql)
                pagination = Pagination(page, pre_page, count.count,
                                        self.request)
                startpage = (page - 1) * pre_page

                t_projects = self.db.query('''
                            SELECT a.*,

                b.bsa,b.gszm
                FROM t_projects a
                 '''+default_sql+'''
                    left join (select project_id,GROUP_CONCAT(concat(member_name,'(',btype_id_name,')')) bsa,group_concat(ifnull(aa.zone_id_name,''),'|',mid,'|',member_name,'|',btype_id_name,'|',aa.zone_id) gszm
                    from t_projects_member aa,t_projects bb where aa.project_id=bb.id and  team_id=38 group by project_id ) b
                    on a.id=b.project_id where is_lock=0   '''
                                           + add_sql + '''
                        order by a.created_at desc limit %s,%s
                        ''', startpage, pre_page)

                

            project_btypes = self.db.query(
                """select *,(select count(*)  from t_projects_member aa,t_projects bb where aa.project_id=bb.id and last_milepost_id=a.id and btype_id=%s  and is_cancel=0 ) c
                from t_projects_type a where income_category='办结' order by order_int""",
                cq_btype_id)
            t_project_bussniss = self.db.query(
                """select * from t_projects_type where income_category='业务类型' order by order_int  """
            )

            t_income_type = self.db.query("""
                select * from t_projects_type where income_category='业务来源' order by order_int desc
                """)

            t_sign_type = self.db.query("""
                select * from t_projects_type where income_category='签约方式' order by order_int desc
                """)
            t_talk_type = self.db.query(
                "select * from t_projects_type where income_category='沟通方式' order by order_int desc "
            )
            t_company = self.db.query("""
                select * from t_projects_type where income_category='收入公司' order by order_int desc
                """)
            t_business_channel = self.db.query("""
                select * from t_projects_type where income_category='推广来源渠道' order by order_int desc
                """)
            t_building = self.db.query(
                "select * from t_projects_type where income_category='楼盘' order by order_int desc "
            )
            t_users_kf = self.db.query("select * from t_user  where role=6")
            t_rec_contarct_type = self.db.query(
                "select * from t_projects_type where income_category='合同确认' order by order_int desc "
            )
            t_user_group = self.db.query("select * from t_user_group")
            t_users = self.db.query(
                "SELECT * FROM t_user_teams a , t_user b where b.id=a.uid ")

            t_user_cq = self.db.query("SELECT * FROM t_user  where role=9 ")
            t_user_sales = self.db.query(
                "SELECT * FROM t_user_teams a , t_user b where b.id=a.uid and team_id=1 "
            )
            t_user_teams_cq=self.db.query(
                   """
                    select a.*,b.team_id from t_user a inner join t_user_teams b on a.id=b.uid where b.team_id=5
                    """
                    )
            t_cq_service = self.db.query(
                    "select * from t_projects_type where income_category='业务分类' order by order_int desc "
                )
            t_projects_type=self.db.query("""
                select id,income_name from t_projects_type where income_category='区域'
            """)
            return self.render(
                'project/projects_state_type.html',
                cancel_wait_count1=cancel_wait_count1,
                cancel_confirm_count1=cancel_confirm_count1,
                params=params,
                t_projects_type=t_projects_type,
                t_user_sales=t_user_sales,
                t_user_cq=t_user_cq,
                t_users=t_users,
                t_rec_contarct_type=t_rec_contarct_type,
                t_income_type=t_income_type,
                t_users_kf=t_users_kf,
                pagination=pagination,
                t_projects=t_projects,
                t_project_bussniss=t_project_bussniss,
                t_building=t_building,
                t_business_channel=t_business_channel,
                t_sign_type=t_sign_type,
                t_company=t_company,
                t_talk_type=t_talk_type,
                ntag=ntag,
                is_ok=is_ok,
                dt=dt,
                diff_date=self.diff_date,
                t_user_teams_cq=t_user_teams_cq,
                t_cq_service=t_cq_service,
                wait_count1=wait_count1,
                wait_count=wait_count,
                project_btypes=project_btypes,
                last_milepost_id=last_milepost_id,
                tag=tag,
                search_key="")
        elif tag == "list_finance":
            page = int(self.get_argument("page", 1))
            order_int=self.get_argument("order_int",'0')
            show = self.get_argument("show",'1')
            state = self.get_argument("state","")
            sql,role_sql,role_sql1,sql_compl,sql_count,role_c_sql,role_c_sql1="","","","","","",""
            inner_sql=' inner '
            if state=="5":
                inner_sql=' left '
            if state=="3":
                role_sql =" where  fi_confirm_uid =0 and income_uid > 0 "
            elif state=="2":
                role_sql =" where  income_uid = 0 "
            elif state=="5":
                role_c_sql ="  where  contract_uid = 0 "
            if show=="1":
                if state=="3":
                    role_sql=" where  fi_confirm_uid =0 and income_uid > 0  "
                    role_c_sql=" where contract_confirm_at is not null "
                elif state=="2":
                    role_sql =" where  income_uid = 0 "
                elif state=="5":
                    role_c_sql ="  where  contract_uid = 0 "
                sql=""" SELECT a.customer_company,b.fi_count ,a.id,a.customer_name,a.project_name,a.guid,a.all_income,a.uid_name,a.created_at
                 from t_projects a """+inner_sql+"""  join (select  count(*) fi_count,project_id,income_uid_at from t_projects_income_title
                                     """+role_sql+""" group by project_id) b on b.project_id=a.id """+role_c_sql
                sql_count = """
                SELECT count(*) count
            from t_projects a """+inner_sql+"""  join (select  count(*) fi_count,project_id from t_projects_income_title
                              """+role_sql+"""  group by project_id) b on b. project_id=a.id
                """+role_c_sql
            elif show=="2":
                if state=="3":
                    role_sql =" where fi_confirm_uid >0 and income_uid > 0 "
                    role_c_sql="  order by b.fi_confirm_at desc "
                elif state=="2":
                    role_sql =" where  income_uid > 0 "
                    role_c_sql="  order by b.income_uid_at desc "
                elif state=="5":
                    role_c_sql =" where  contract_uid > 0  order by a.contract_confirm_at desc "
                sql=""" SELECT a.customer_company,b.fi_count ,a.id,a.customer_name,a.project_name,a.guid,a.all_income,a.uid_name,a.created_at
                 from t_projects a inner  join (select  count(*) fi_count,project_id,fi_confirm_at,income_uid_at from t_projects_income_title
                                      """+role_sql+""" group by project_id) b on b. project_id=a.id"""+role_c_sql
                sql_count = """
                SELECT count(*) count
            from t_projects a inner  join (select  count(*) fi_count,project_id,fi_confirm_at,income_uid_at from t_projects_income_title
                              """+role_sql+"""  group by project_id) b on b. project_id=a.id"""+role_c_sql

            if show=="3":
                if state=="3":
                    role_sql =" where fi_confirm_uid <>0 and income_uid > 0 "
                elif state=="2":
                    role_sql =" where  income_uid <> 0 "
                elif state=="5":
                    role_c_sql ="  where  contract_uid = 0 " 
                    role_sql =" where  income_uid <> 0 "
                sql=""" SELECT a.customer_company,b.fi_count ,a.id,a.customer_name,a.project_name,a.guid,a.all_income,a.uid_name,a.created_at
                 from t_projects a inner  join (select  count(*) fi_count,project_id from t_projects_income_title
                                    """+role_sql+""" and is_print=0  group by project_id) b on b. project_id=a.id"""+role_c_sql
                sql_count = """
                SELECT count(*) count
            from t_projects a inner  join (select  count(*) fi_count,project_id from t_projects_income_title
                             """+role_sql+""" and is_print=0 group by project_id) b on b. project_id=a.id
                """+role_c_sql
            elif show=="4":
                sql=""" SELECT a.customer_company,b.fi_count ,a.id,a.customer_name,a.project_name,a.guid,a.all_income,a.uid_name,a.created_at
                 from t_projects a inner  join (select  count(*) fi_count,project_id from t_projects_income_title
                                        where is_print=1
                                       group by project_id) b on b.project_id=a.id"""
                sql_count = """
                SELECT count(*) count
            from t_projects a inner  join (select  count(*) fi_count,project_id from t_projects_income_title
                               where is_print=1 
                              group by project_id) b on b.project_id=a.id"""

            pre_page = 20

            if state=="3":
                role_sql1 =" where fi_confirm_uid =0 and income_uid > 0  "
                role_c_sql1=" where contract_confirm_at is not null "
            elif state=="2":
                role_sql1 =" where  income_uid = 0 "
            elif state=="5":
                role_c_sql1 =" where  contract_uid = 0 "
                role_sql1 =" where  income_uid <> 0 "
            print role_sql1,"role_sql1"
            count_wait = self.db.get('''  SELECT count(*) count
            from t_projects a '''+inner_sql+'''  join (select  count(*) fi_count,project_id from t_projects_income_title
                            '''+role_sql1+'''  group by project_id) b on b. project_id=a.id ''' +role_c_sql1)
            count_compl= self.db.get('''  SELECT count(*) count
            from t_projects a inner  join (select  count(*) fi_count,project_id from t_projects_income_title
                            '''+role_sql1.replace('=','<>')+''' group by project_id) b on b. project_id=a.id '''+role_c_sql1.replace('=','<>') )

            print ''' SELECT count(*) count
            from t_projects a inner  join (select  count(*) fi_count,project_id from t_projects_income_title
                             '''+role_sql1.replace('=','<>')+''' and is_print=0 group by project_id) b on b. project_id=a.id '''
            count_print_wait= self.db.get('''  SELECT count(*) count
            from t_projects a inner  join (select  count(*) fi_count,project_id from t_projects_income_title
                             '''+role_sql1.replace('=','<>')+''' and is_print=0 group by project_id) b on b. project_id=a.id ''' )
            count_print_compl= self.db.get(''' SELECT count(*) count
            from t_projects a inner  join (select  count(*) fi_count,project_id from t_projects_income_title
                              where  is_print=1  group by project_id) b on b. project_id=a.id ''' )


            count = self.db.get(sql_count)
            print sql_count
            pagination = Pagination(page, pre_page, count.count, self.request)
            startpage = (page - 1) * pre_page
            print(sql)
            t_projects = self.db.query(
                    sql+''' limit %s,%s''', startpage,  pre_page)


            return self.render(
                'project/list_finance.html',
                count_print_compl=count_print_compl,
                count_print_wait=count_print_wait,
                count_wait=count_wait,
                count_compl=count_compl,
                pagination=pagination,
                order_int=order_int,
                page1=page,
                t_projects=t_projects,
                show=show,
                state=state,
                form_tag="list",
                search_key="")
        elif tag == "list_confirm":
            page = int(self.get_argument("page", 1))
            order_int=self.get_argument("order_int",'0')
            pre_page = 20
            sql_str= ""
            sql_cc=''
            sql_d=''
            order_by_str =" a.created_at "
            if role=="6":
                sql_str = " where busniess_from_id=2"
            elif role=="2":
                order_by_str =" cc "
            elif role == "3":
                order_by_str = " d "
            if order_int=='1':
                if role=="3" or role=='5':
                    order_by_str=' dd '
                elif role=="2":
                    order_by_str =" ccc "
            count = self.db.get('''SELECT count(*) count FROM t_projects ''' + sql_str)
            pagination = Pagination(page, pre_page, count.count, self.request)
            startpage = (page - 1) * pre_page

            if role=='2' or role=='3':
                if role=='2':
                    sql_cc='''(select  count(*) c from t_projects_income_title  where project_id=a.id and income_uid =0)cc,
                    (select  count(*) c from t_projects_income_title  where project_id=a.id and income_uid <>0 and is_print=0)ccc'''
                else:
                    sql_d="""

                    (select  count(*) c from t_projects_income_title
                         where project_id=a.id and fi_confirm_uid =0 and income_uid > 0)d,
                         (select  count(*) c from t_projects_income_title
                         where project_id=a.id and fi_confirm_uid <> 0 and income_uid > 0 and  is_print=0)dd
                         """
                t_projects = self.db.query(
                '''
                SELECT a.id,a.customer_name,a.project_name,a.guid,a.all_income,a.uid_name,a.created_at,
                         '''+sql_cc+sql_d+'''
                        FROM t_projects a
                        ''' + sql_str +''' order by '''+order_by_str+''' desc limit %s,%s''', startpage,
                pre_page)
                print '''SELECT a.id,a.customer_name,a.project_name,a.guid,a.all_income,a.uid_name,a.created_at,
                         '''+sql_cc+sql_d+'''
                        FROM t_projects a
                        ''' + sql_str +''' order by '''+order_by_str+''' desc'''

            elif role=='5':
                
                sql_d="""
                    ,(select  count(*) c from t_projects_income_title
                         where project_id=a.id and fi_confirm_uid =0 and income_uid > 0)d,
                         (select  count(*) c from t_projects_income_title
                         where project_id=a.id and fi_confirm_uid <> 0 and income_uid > 0 and  is_print=0)dd
                         """
                t_projects = self.db.query(
                '''
                SELECT a.id,a.customer_name,a.project_name,a.guid,a.all_income,a.uid_name,a.contract_uid,a.contract_confirm_id_name,
                        a.contract_uid_name,a.contract_confirm_at,a.created_at,
                         (select  count(*) c from t_projects_income_title  where project_id=a.id and income_uid =0
                        )
                        cc,
                        (select  count(*) c from t_projects_income_title
                         where project_id=a.id and fi_confirm_uid =0 and income_uid > 0
                        )
                         d
                            # ,ifnull(b.member_name,'') kfgw,ifnull(c.member_name,'') zxkf
                        '''+sql_d+'''

                        FROM t_projects a
                        # left join t_projects_member b on a.id=b.project_id  and b.team_id=39
                        # left join t_projects_member c on a.id=c.project_id  and c.team_id=36


                        ''' + sql_str +''' order by '''+order_by_str+''' desc limit %s,%s''', startpage,
                pre_page)


            elif role=='6':
                t_projects = self.db.query(
                '''
                SELECT a.id,a.customer_name,a.project_name,a.guid,a.all_income,a.uid_name,a.busniess_from_id_name,a.created_at,
                a.channel_id_name,a.from_word,a.from_word_uid,
                         (select  count(*) c from t_projects_income_title  where project_id=a.id and income_uid =0
                        )
                        cc,
                        (select  count(*) c from t_projects_income_title
                         where project_id=a.id and fi_confirm_uid =0 and income_uid > 0
                        )
                        d,
                           ifnull(b.member_name,'') kfgw,ifnull(c.member_name,'') zxkf


                        FROM t_projects a
                        left join t_projects_member b on a.id=b.project_id  and b.team_id=39
                        left join t_projects_member c on a.id=c.project_id  and c.team_id=36


                        ''' + sql_str +''' order by '''+order_by_str+''' desc limit %s,%s''', startpage,
                pre_page)
            return self.render(
                'project/projects_list_confirm.html',
                pagination=pagination,
                order_int=order_int,
                page1=page,
                t_projects=t_projects,
                form_tag="list",
                search_key="")
        elif tag=="new":
            form_tag = self.get_argument("form_tag")
            t_income_type = self.db.query("""
                select * from t_projects_type where income_category='业务来源' order by order_int desc
                """)

            t_sign_type = self.db.query("""
                select * from t_projects_type where income_category='签约方式' order by order_int desc
                """)
            t_talk_type = self.db.query(
                        "select * from t_projects_type where income_category='沟通方式' order by order_int desc "
                    )
            t_company = self.db.query("""
                select * from t_projects_type where income_category='收入公司' order by order_int desc
                """)
            t_business_channel = self.db.query("""
                select * from t_projects_type where income_category='推广来源渠道' order by order_int desc
                """)
            t_building = self.db.query(
                "select * from t_projects_type where income_category='楼盘' order by order_int desc "
            )
            t_users = self.db.query(
                "select * from t_user  "
            )
            return self.render(
                'project/project_new.html',
                t_building=t_building,
                t_business_channel=t_business_channel,
                t_sign_type=t_sign_type,
                t_income_type=t_income_type,
                form_tag=form_tag,
                search_key="",
                t_talk_type=t_talk_type,
                t_company=t_company,
                t_users=t_users)
        elif tag == "modify":
            form_tag = self.get_argument("form_tag")
            project_id = self.get_argument("project_id")
            guid = self.get_argument("guid")
            if not project_id:
                self.write("0")
            elif not guid:
                self.write("1")
            else:
                t_project = self.db.get('select * from t_projects where id=%s and guid=%s',project_id,guid)
                if not t_project:
                    self.write('not project')
                else:
                    t_income_type = self.db.query("""
                        select * from t_projects_type where income_category='业务来源' order by order_int desc
                        """)
                    t_business_type = self.db.query("""
                        select * from t_projects_type where income_category='业务类型' order by order_int desc
                        """)
                    t_sign_type = self.db.query("""
                        select * from t_projects_type where income_category='签约方式' order by order_int desc
                        """)
                    t_talk_type = self.db.query(
                        "select * from t_projects_type where income_category='沟通方式' order by order_int desc "
                    )
                    return self.render(
                        'project/project_modify.html',
                        t_talk_type=t_talk_type,
                        t_project=t_project,
                        t_sign_type=t_sign_type,
                        t_income_type=t_income_type,
                        form_tag=form_tag,
                        t_business_type=t_business_type,
                        search_key="",
                        setCheckbox=self.setCheckbox)

        elif tag=="view_img":
            img = self.get_argument("img")
            img_type_list = ['jpg','jpeg','png','gif','bmp']
            is_img = False
            for item in img_type_list:
                if item in img:
                    is_img = True
                    break;
            if not is_img:
                return self.redirect(img)
            return self.render("project/view_img.html",img=img)

        elif tag=="show":
            guid= self.get_argument("guid","")
            id = self.get_argument("id")
            addr_provider=self.get_argument('addr_provider',0)
            xiezhu_id=self.get_argument('xiezhu_id',0)
            mid = self.get_argument("mid",0)
            is_ok=self.get_argument('is_ok','')
            from_mod = self.get_argument('from_mod','')
            express_list_type=self.get_argument('express_list_type','0')
            #company_count=''
            #customer_count=''
            t_project_up=''
            t_project_down=''
            t_customer = None
            guid_sql="and a.guid='%s'"%(guid)
            if  from_mod:
                guid_sql=""
            t_project = self.db.get(
                """select a.*,b.income_name contract_sign_type_name,c.name uid_name,
                d.gc_business,d.gc_request
                 from t_projects a
                  inner join  t_projects_type b  on a.contract_sign_type_id=b.id
                 inner join t_user c on a.uid=c.id
                left join (select group_concat(id,'|',guid) gc_business ,group_concat(distinct project_request) gc_request,project_id from business_develop_manage
                where  find_in_set(%s,project_id)
                ) d on find_in_set(a.id,d.project_id)
        
                 where   a.id=%s """+guid_sql,id,
                id)
            if not t_project:
                return self.write(u"该项目不存在！"+id+guid)
            else:
                t_project_members = self.db.query("""
                select a.*,b.name,datediff(DATE_FORMAT(now(),'%%Y-%%m-%%d'),DATE_FORMAT(a.created_at,'%%Y-%%m-%%d')) ddf,
                datediff(DATE_FORMAT(now(),'%%Y-%%m-%%d'),DATE_FORMAT(a.updated_at,'%%Y-%%m-%%d')) ddff
                from t_projects_member a , t_user b
                 where a.member_id=b.id and  project_id=%s order by created_at desc""",id)
                if t_project.company_uid and len(t_project.company_uid)==17:
                    t_customer=self.db_customer.get('''
                    select * from t_customer where company_reguid=%s 
                ''',t_project.company_uid)
                    if not t_customer:
                        t_customer=self.db_customer.get('''
                    select * from t_customer where company=%s
                ''',t_project.customer_company)
                elif  t_project.customer_company and len(t_project.customer_company) >6:
                    t_customer=self.db_customer.get('''
                    select * from t_customer where company=%s limit 1
                ''',t_project.customer_company)
                visible_other_relation=self.db.query('''
                        SELECT a.id  FROM t_projects a
                 inner join t_projects_member c on a.id=c.project_id
                 inner join  t_user_visible_other d on d.be_checker_id=member_id and d.checker_id=%s and a.uid!=d.be_checker_id
                and a.id=%s'''+guid_sql,uid,id)
                visible_other=self.db.get('''
                SELECT a.id  FROM t_projects a
                inner join  t_user_visible_other d on  a.uid=d.be_checker_id and d.checker_id=%s and a.id=%s
                    '''+guid_sql,uid,id)
                # visible_correlation=self.db_customer.query('''
                # select a.id from t_customer a
                # inner join  '''+options.mysql_database+'''.t_projects b on b.customer_company=a.company and b.uid!=%s
                #  where a.company=%s and a.acc_uid=%s
                #     and a.acc_uid not in (select member_id from '''+options.mysql_database+'''.t_projects_member where project_id=%s)

                # ''',uid,t_project.customer_company,uid,t_project.id)
                if visible_other or visible_other_relation:
                    visible_project=False
                else:
                    visible_project=True
                can_role = ['8','2','3','5','7','10','11']
                can_user = ['210'] #陈月娇
                if t_project.uid == int(uid) or self.checkUserArrIn(
                        can_user, uid) or self.checkUserIn(
                            t_project_members, uid) or self.checkRoleIn(
                                can_role, role) or self.checkAccIn(
                                    t_customer, uid):
                    pass
                elif visible_other_relation or visible_other:
                    pass
                else:
                    return self.write(u"您非本项目相关人员,无法查看,如有疑问."+role+"/"+uid)




                t_project_bussniss = self.db.query(
                    """select * from t_projects_type where income_category='业务类型' """
                )

                t_project_role = self.db.query("""select a.*,
                datediff(DATE_FORMAT(now(),'%%Y-%%m-%%d'),DATE_FORMAT(a.updated_at,'%%Y-%%m-%%d')) ddff
                from t_projects_member a , t_projects_type b  where a.team_id=b.id and  project_id=%s order by order_int""",id)
                t_business_type = self.db.query("""
                    select * from t_projects_type where income_category='收入类型' order by order_int desc
                    """)
                t_company = self.db.query("""
                    select * from t_projects_type where income_category='收入公司' order by order_int desc
                    """)
                t_pay_type = self.db.query("""
                    select * from t_projects_type where income_category='支付方式' order by order_int desc
                    """)
                t_finance_confirm = self.db.query(
                    "select * from t_projects_type where income_category='财务确认' order by order_int desc "
                )

                t_file_type = self.db.query(
                    "select * from t_projects_type where income_category='资料交接明细' order by order_int desc "
                )
                t_file_type_cate = self.db.query(
                    "select * from t_projects_type where income_category='资料类型' order by order_int desc "
                )
                t_rec_contarct_type = self.db.query(
                    "select * from t_projects_type where income_category='合同确认' order by order_int  "
                )
                t_talk_type = self.db.query(
                    "select * from t_projects_type where income_category='沟通方式' order by order_int desc "
                )
                t_income_type = self.db.query("""
                select * from t_projects_type where income_category='业务来源' order by order_int desc
                """)
                t_income_other_type = self.db.query("""
                select * from t_projects_type where income_category='代收类型' order by order_int desc
                """)



                rec_income_money = self.db.get("""
                         select ifnull(sum(income_money),0) c from t_projects_income a ,
                          t_projects_income_title  b
                             where a.project_id=b.project_id and  a.project_id=%s and income_uid > 0
                             and income_id <= 43
                """, id)



                wait_rec_income_money = self.db.get("""
                              select ifnull(sum(income_money),0) c from t_projects_income a , t_projects_income_title  b
                                  where a.project_id=b.project_id and  a.project_id=%s and income_uid = 0
                                   and income_id <= 43
                """, id)



                rec_income_money_other = self.db.get("""
                         select ifnull(sum(income_money),0) c from t_projects_income a ,
                          t_projects_income_title  b
                             where a.project_id=b.project_id and  a.project_id=%s and income_uid > 0
                             and income_id >= 43
                """, id)
                wait_rec_income_money_other = self.db.get(
                    """
                              select ifnull(sum(income_money),0) c from t_projects_income a , t_projects_income_title  b
                                  where a.project_id=b.project_id and  a.project_id=%s and income_uid = 0
                                   and income_id >= 43
                """, id)
                if t_project.busniess_from_id!=203:
                    service_income_sql=' and  service_id!=276 and service_id!=72 '
                else:
                    service_income_sql=''
                t_projects_service_income = self.db.query(
                    """ select *,b.order_int1 from t_projects_service_income  a
                     left join t_projects_type b on a.service_id=b.id 
                      where project_id=%s """+service_income_sql+"""  order by b.order_int1 """,id)
                t_projects_service_income_list = self.db.query(
                    "select * from t_projects_service_income where project_id=%s  and (service_money <> 0 or is_free=1)",
                    id)

                # t_projects_file = self.db.query("select * from t_projects_file where project_id=%s order by order_int ",id)

                t_business_channel = self.db.query("""
                select * from t_projects_type where income_category='推广来源渠道' order by order_int desc
                """)
                t_building = self.db.query(
                    "select * from t_projects_type where income_category='楼盘' order by order_int desc "
                )


                t_sign_type = self.db.query("""
                select * from t_projects_type where income_category='签约方式' order by order_int desc
                """)
                t_project_income_title = self.db.query("""
                        select a.*,b.income_money income_money_total,b.income_title,c.pay_list from t_projects_income_title a , (
                        select parent_id,sum(income_money) income_money,GROUP_CONCAT(concat(income_name,'|',income_money))  income_title
                        from t_projects_income group by parent_id) b left join
                          (select title_id, GROUP_CONCAT(concat( service_name,"|",service_money)) pay_list from t_projects_income_detail
                    group by title_id) c on c.title_id=b.parent_id
                        where a.id=b.parent_id and project_id=%s
                        order by created_at desc
                """, id)

                # print "7"


                t_project_income_wait = self.db.get("""
                            select (
                            select ifnull(sum(income_money),0)  income_money from t_projects_income a
                                            ,t_projects_income_title b
                                            where a.parent_id=b.id  and  a.project_id={0} and
                                             income_uid > 0 and income_id =40) aa ,
                            (
                            select ifnull(sum(income_money),0)  income_money from t_projects_income a
                                            ,t_projects_income_title b
                                            where a.parent_id=b.id  and  a.project_id={0} and
                                             income_uid > 0 and income_id =43) bb     ,

                                                (
                            select ifnull(sum(income_money),0)  income_money from t_projects_income a
                                            ,t_projects_income_title b
                                            where a.parent_id=b.id  and  a.project_id={0} and
                                             income_uid > 0 and income_id >43) cc,

                            (select ifnull(sum(income_money),0)  income_money from t_projects_income a
                                            ,t_projects_income_title b
                                            where a.parent_id=b.id  and  a.project_id={0} and
                                             income_uid > 0 and income_id <=43) dd


                """.format(id))
                # print "8"

                t_project_income = self.db.query(
                    """select a.*,b.pay_type_name,b.income_at income_at_a  from t_projects_income a
                    ,t_projects_income_title b
                    where a.parent_id=b.id  and  a.project_id=%s  and income_uid > 0 order by created_at desc
                """, id)




                # print "9"

                t_project_state1 = self.db.query("select * from t_projects_state where  is_hide=1 order by order_int ")
                t_project_state2 = self.db.query("select * from t_projects_state where  is_hide=2 order by order_int ")
                t_project_state3 = self.db.query("select * from t_projects_state where  is_hide=3 order by order_int ")
                t_project_state4 = self.db.query("select * from t_projects_state where  is_hide=4 order by order_int ")
                t_project_state5 = self.db.query("select * from t_projects_state where  is_hide=5 order by order_int ")
                t_project_state6 = self.db.query("select * from t_projects_state where  is_hide=6 order by order_int ")
                t_project_state7 = self.db.query("select * from t_projects_state where  is_hide=7 order by order_int ")
                t_project_state8 = self.db.query("select * from t_projects_state where  is_hide=8 order by order_int ")
                t_project_state9 = self.db.query("select * from t_projects_state where  is_hide=9 order by order_int ")
                t_project_state10 = self.db.query("select * from t_projects_state where  is_hide=10 order by order_int ")
                t_project_state11 = self.db.query("select * from t_projects_state where  is_hide=11 order by order_int ")
                t_project_state_msg1 = self.db.query(
                    "select * from t_projects_state_msg where  project_id=%s and type_id=1 order by created_at desc",id
                )
                t_project_state_msg2 = self.db.query(
                    "select * from t_projects_state_msg where  project_id=%s and type_id=2 order by created_at desc",
                    id)
                t_project_state_msg3 = self.db.query(
                    "select * from t_projects_state_msg where  project_id=%s and type_id=3 order by created_at desc",
                    id)
                t_project_state_msg4 = self.db.query(
                    "select * from t_projects_state_msg where  project_id=%s and type_id=4 order by created_at desc",
                    id)
                t_project_state_msg5 = self.db.query(
                    "select * from t_projects_state_msg where  project_id=%s and type_id=5 order by created_at desc",
                    id)
                t_project_state_msg6 = self.db.query(
                    "select * from t_projects_state_msg where  project_id=%s and type_id=6 order by created_at desc",
                    id)
                t_project_state_msg7 = self.db.query(
                    "select * from t_projects_state_msg where  project_id=%s and type_id=7 order by created_at desc",
                    id)
                t_project_state_msg8 = self.db.query(
                    "select * from t_projects_state_msg where  project_id=%s and type_id=8 order by created_at desc",
                    id)
                t_project_state_msg9 = self.db.query(
                    "select * from t_projects_state_msg where  project_id=%s and type_id=9 order by created_at desc",
                    id)
                t_project_state_msg10 = self.db.query(
                    "select * from t_projects_state_msg where  project_id=%s and type_id=10 order by created_at desc",
                    id)
                t_project_state_msg11 = self.db.query(
                    "select * from t_projects_state_msg where  project_id=%s and type_id=11 order by created_at desc",
                    id)

                # print "9aETDHH FCM"

                t_projects_income_all=self.db.query("""
                select income_money,income_name,remark from t_projects_income_other where project_id=%s
                """,t_project.id)
                t_projects_income_allmoney=self.db.get("""
                select sum(income_money) from t_projects_income_other where project_id=%s
                """,t_project.id)
                t_projects_linkmans=self.db.query("""
                select * from t_projects_linkman where project_id=%s
                """,t_project.id)
                t_projects_transitions=self.db.query(
                    """
                    select * from t_projects_transition where project_id=%s and file_type=0 order by created_at desc
                    """,t_project.id)
                t_projects_transitions_customer=self.db.query(
                    """
                    select * from t_projects_transition where project_id=%s and file_type=0 and is_customer=1 order by created_at desc
                    """,t_project.id)
                t_projects_transitions_file=self.db.query(
                    """
                    select * from t_projects_transition_upload where project_id=%s order by created_at desc
                    """,t_project.id)
                t_projects_parents=self.db.query(
                    '''
                    select * from t_projects_parent where parent_id=%s
                    ''',id)
                t_projects_relate=self.db.query(
                   '''
                   select a.* from t_projects a inner join t_projects_parent b on a.id=b.project_id
                   where b.parent_id=%s
                   ''',id
                )
                t_user_teams=self.db.query(
                   """
                    select a.*,b.team_id from t_user a inner join t_user_teams b on a.id=b.uid
                    """
                    )
                t_user_kfs=self.db.query('''
                    select * from t_user where role=13 and id not in (
                    select a.id from t_user a inner join t_user_teams b on a.id=b.uid and b.team_id=2
                    )
                ''')
                t_user_teams_cq=self.db.query(
                   """
                    select a.*,b.team_id from t_user a inner join t_user_teams b on a.id=b.uid where b.team_id=5 order by not_process
                    """
                    )
                t_project_kf = self.db.get("select * from t_projects_member where project_id=%s and team_id=39",id)

                t_users_kf = self.db.query("select a.*,b.team_id from t_user a inner join t_user_teams b on a.id=b.uid where b.team_id=4")
                t_cq_service = self.db.query(
                    "select * from t_projects_type where income_category='业务分类' order by order_int desc "
                )
                project_milepost_type = self.db.query(
                    """select *,b.order_int border_int,date_format(b.confirm_at,"%%Y-%%m-%%d")=date_format(now(),"%%Y-%%m-%%d") is_today from t_projects_type a
                     inner join t_projects_milepost b on b.type_id=a.id where income_category='办结' and a.is_hide=0
                      and project_id=%s order by b.order_int""",
                    id)

                project_btypes = self.db.query(
                    "select * from  t_projects_member  where project_id=%s  and btype_id <> 0  and not_transition=0 ",
                    id)
                is_end = 2
                is_cancel = 1
                is_cancel_arr =[]
                if len(project_milepost_type) ==0:
                    is_end=1
                for row in project_milepost_type:
                    if row.income_name == "仓管确认交接完成" and not  row.confirm_at:
                        is_con = 0
                        for row1 in project_btypes:
                            if row.member_id==row1.mid and   row1.is_cancel_confirm_at :
                                #   print "dump....", is_end, row1.is_cancel_confirm_at
                                is_con = 1
                                is_cancel_arr.append(row1.mid)

                        if is_con:
                            continue
                        is_end = 1
                        break
                if len(project_btypes)  and len(project_btypes)==len(is_cancel_arr):
                    is_cancel = 2

                zones = self.db.query("select * from t_projects_type where income_category='区域'")
                citys = self.db.query(
                    "select * from t_projects_type where income_category='地市'")
                # print "10"

                project_note = self.db.query("""
                        select a.*,c.check_id,c.check_at,c.check_name,b.note_id,b.read_name,a.id as aid,c.remark,c.state_id,c.created_name from t_projects_note a
                        left join ( select note_id,GROUP_CONCAT(concat(created_name,','))  read_name
                        from t_projects_note_confirm  group by note_id) b

                         on a.id=b.note_id
                         left join (select id check_id,check_name,check_at,note_id,remark,state_id,created_name from t_projects_note_check) c
                         on a.id=c.note_id
                         where a.project_id=%s order by creatd_at desc
                        """, t_project.id)
                project_note_unread = self.db.query("""
                        select * from t_projects_note a

                         where project_id=%s

                         and id not in(
								select note_id from t_projects_note_confirm where note_id=a.id and created_by=%s
                         )

                         order by creatd_at desc
                        """, t_project.id,uid)

                t_projects_note_check=self.db.query(
                    """
                    select * from t_projects_note a where project_id=%s and is_check=1
                       and id not in(
								select note_id from t_projects_note_check where note_id=a.id
                         )
                         order by creatd_at desc
                    """,t_project.id)

                if role=='1' or role=='12':
                    t_projects_types=self.db.query(
                    """
                    select * from t_projects_type where income_category='业务类型' order by order_int
                    """
                    )
                else:
                    t_projects_types=''

                t_projects_type=self.db.query(
                    """
                    select * from t_projects_type where income_category='移交资料' order by order_int
                    """
                )
                item_transfile = None
                item_transfile_sales = None
                curr_member = None
                if mid:

                    item_transfile = self.db.get(
                        '''select * from t_projects_transfile where pm_id=%s  and mtype=1 order by created_at desc limit 1''', mid)
                    item_transfile_sales = self.db.get('''
                                select * from t_projects_transfile where pm_id=%s and mtype=2 limit 1
                            ''', mid)

                else:
                    for r in project_btypes:
                        mid = r.mid
                        item_transfile = self.db.get('''
                                select * from t_projects_transfile where pm_id=%s and mtype=1
                            ''', mid)
                        break
                    for r in project_btypes:
                        mid = r.mid
                        item_transfile_sales = self.db.get(
                            '''
                                select * from t_projects_transfile where pm_id=%s and mtype=2
                            ''', mid)

                        break

                if mid:
                    curr_member = self.db.get(
                        'select * from t_projects_member where mid=%s', mid)

                # t_projects_transfile=self.db.query('''
                #         select * from t_projects_transfile where project_id=%s limit 1
                #     ''',id)
                visible_note=self.db.get(
                    '''
                     select * from  t_projects_member  where project_id=%s and team_name!='在线客服' and member_id=%s limit 1
                    ''',t_project.id,uid)


                t_company_id=self.db.get(
                    '''select id from t_company where company_name=%s''',t_project.customer_company
                )
                area_type=self.db.query(
                """
                select income_name from t_projects_type where income_category='区域'
                """
                )
                projects_addr_provider=self.db.query('''
                    select a.*,b.area,b.addr_type,b.provider,b.danbao_matter,
                    b.fp_limit from t_projects_addr_provider a
                    left join t_addr_provider_manage b
                    on a.addr_id=b.id
                     where project_id=%s order by a.created_at desc
                ''',t_project.id)
                addr_milepost=self.db.query("""
                    select * from t_projects_addr_milepost where project_id=%s""",t_project.id)
                if projects_addr_provider and not addr_provider:
                    addr_provider=projects_addr_provider[0].id


                xiezhu_applys=self.db.query('''
                select a.*,b.project_name,b.customer_name,b.customer_company,
                c.uid_name gs_uid_name,c.uid gs_uid,c.confirm_at gs_confirm_at,c.is_pass gs_is_pass,c.id gs_id,
                d.uid_name xs_uid_name,d.confirm_at xs_confirm_at,d.id xs_id,
                datediff(f.confirm_at,d.confirm_at) zhouqi,
                f.uid_name sh_uid_name,f.confirm_at sh_confirm_at,f.is_pass sh_is_pass,f.created_at sh_created_at,f.id sh_id,
                f.fz_name sh_fz_name,
                g.uid_name queren_uid_name,g.confirm_at queren_confirm_at,g.id queren_id
                 from t_xiezhu_apply a
                inner join t_projects b
                 on a.project_id=b.id
                left join t_xiezhu_apply_milepost c
                 on a.id=c.xiezhu_id and c.type_name='待审核'
                left join  t_xiezhu_apply_milepost d
                 on a.id=d.xiezhu_id and d.type_name='待接单'
                left join  t_xiezhu_apply_milepost f
                 on a.id=f.xiezhu_id and f.type_name='结果审核'
                left join  t_xiezhu_apply_milepost g
                 on a.id=g.xiezhu_id and g.type_name='已确认'
                 where a.project_id=%s order by a.created_at
            ''',t_project.id)


                if xiezhu_applys and not xiezhu_id:
                    xiezhu_id=xiezhu_applys[0].id
                xiezhu_apply_mileposts=self.db.query('''
                select a.*,b.uid_name gs_uid_name,b.uid gs_uid from t_xiezhu_apply_milepost a
                left join t_xiezhu_apply_milepost b
                on a.xiezhu_id=b.xiezhu_id and b.type_name='待审核'
                 where a.xiezhu_id=%s
            ''',xiezhu_id)
                t_projects_relation=self.db.get('''
                select * from t_projects_relation where (relation_ids like "%%,'''+str(t_project.id)+''',%%" or relation_ids REGEXP  "^'''+str(t_project.id)+'''," ) limit 1''')
                # t_relation_projects=[]
                # if t_projects_relation:
                #     for idx,item in enumerate(t_projects_relation.relation_ids.split(',')[:-1]):
                #         t_relation_projects.append([])
                #         sql=self.db.get('select concat(guid,"|",id,"|",project_name) guid_id from t_projects where id=%s',item)
                #         t_relation_projects[idx].append(sql.guid_id)
                #         if t_projects_relation.uid_names:
                #             for row in t_projects_relation.uid_names.split(',')[:-1]:
                #                 if item in row:
                #                     row1=row.split('|')
                #                     if item ==row1[1]:
                #                         row2=row1[0]+'|'+row1[2]
                #                     elif item==row1[2]:
                #                         row2=row1[0]+'|'+row1[1]
                #                     t_relation_projects[idx].append(row2)



                company_history=self.db.query('''
                select * from t_projects_company_history where project_id=%s
                ''',t_project.id)
                t_promo_types = self.db.query(
                """select * from t_projects_type where income_category='套餐' order by order_int  """
                )
                express_type=self.db.query('''
                    select * from t_projects_type where income_category='快递类型'
                ''')
                payment_type=self.db.query('''
                    select * from t_projects_type where income_category='快递付费'
                ''')
                t_express_send=self.db.query('''
                select * from t_express where project_id=%s and guid=%s and send_or_rec=0 order by created_at desc''',t_project.id,t_project.guid)
                t_express_rec=self.db.query('''
                select * from t_express where project_id=%s and guid=%s and send_or_rec=1 order by created_at desc''',t_project.id,t_project.guid)
                if t_project.customer_company:
                    t_cutomer_addr_msg=self.db.query('''
                        select * from t_customer_addr_msg where company=%s
                    ''',t_project.customer_company)
                else:
                    t_cutomer_addr_msg=self.db.query('''
                        select * from t_customer_addr_msg where tel=%s
                    ''',t_project.customer_tel)
                t_projects_type1=self.db.query(
                    """
                    select * from t_projects_type where income_category='移交资料' and  jiaojie_order>0 order by jiaojie_order
                    """
                )

                t_project_chuna_history=self.db.get('''
                select * from t_project_chuna_history where project_id=%s
                ''',t_project.id)
                # if role=='8' or role=='3' or role=='11':
                #     t_project_up = self.db.get('''
                #      SELECT  guid,id FROM t_projects
                #    where  id > %s and is_lock=0 order by created_at  limit 1''',t_project.id)
                #     t_project_down = self.db.get('''
                #      SELECT  guid,id FROM t_projects
                #    where  id < %s and is_lock=0 order by created_at desc limit 1''',t_project.id)
                # elif role=='6':
                #     t_project_up=self.db.get('''
                #     SELECT guid,id FROM t_projects
                #     where id>%s and busniess_from_id=2 order by created_at  limit 1''',t_project.id)
                #     t_project_down=self.db.get('''
                #     SELECT guid,id FROM t_projects
                #     where id<%s and busniess_from_id=2 order by created_at desc limit 1''',t_project.id)
                # elif role=='9':
                #     t_project_up = self.db.get(
                #         '''SELECT a.guid,a.id FROM t_projects a  inner join t_projects_member b on a.id=b.project_id and b.team_id=38
                #         and member_id=%s where id>%s order by a.created_at limit 1
                #         ''',uid,t_project.id)
                #     t_project_down = self.db.get(
                #         '''SELECT a.guid,a.id FROM t_projects a  inner join t_projects_member b on a.id=b.project_id and b.team_id=38
                #         and member_id=%s where id<%s order by a.created_at desc limit 1
                #         ''',uid,t_project.id)
                confirm_banjie = self.db.get(
                    '''
                    SELECT  a.id ,b.mid,b.banjie_remark,
                  b.confirm_banjie,b.confirm_name,b.guid m_guid,d.confirm_at
                        FROM t_projects
                    a inner join t_projects_member b on a.id=b.project_id
                    inner join t_projects_milepost d on b.project_id=d.project_id and d.confirm_at is not null and d.type_id=151
                    and b.member_name=d.uid_name
                    and b.btype_id=d.btype_id and b.mid=d.member_id and d.member_id=%s
                    where  b.btype_id <> 0    and b.is_cancel=0  and d.confirm_at>='2018-10-01 00:00:00'
                    and a.id=%s''',mid,t_project.id)

                t_projects_note_chengjiao=self.db.query('''
                select * from t_projects_note_chengjiao
                ''')

                data_str = "%s_%s_%sV2FYJT" % (t_project.id,
                                       t_project.customer_company, dt)
                hash_md5 = hashlib.md5(data_str)
                md5_str =  hash_md5.hexdigest()
                company_history_permission=self.checkUserIn(t_project_members,uid)

                t_logff_type =self.db.query("select * from t_projects_type  a left join (select last_reject_remark,id logoff_id,ifnull(state_id,0) state_id,state_id_name,leader_uid,leader_uid_name,leader_at ,mid,uid,uid_name,finish_at,type_id from t_projects_logoff where project_id=%s) b on a.order_int=b.type_id  where income_category='注销' order by order_int ",t_project.id)
                t_projects_information_reject=self.db.query(' select * from t_projects_information_reject where project_id=%s ',t_project.id)
                t_projects_reject_titles=self.db.get('''
                select if(group_concat(reject_msg_titles) is null,'',group_concat(reject_msg_titles)) reject_msg_titles from t_projects_information_reject where handler_uid=%s and 
                 project_id=%s and (handler_at is null or handler_at is not null and confirm_status=2 and not confirm_at ) group by project_id
                ''',uid,t_project.id)
                if not t_projects_reject_titles:
                    t_projects_reject_titles=''
                else:
                    t_projects_reject_titles=t_projects_reject_titles.reject_msg_titles
                t_trade=self.db.query('''
                select a.trade_name,a.trade_number,a.trade_regtype,b.message,b.created_at from t_trade a
                left join  t_trade_msg b on a.id=b.trade_id
                and b.id=
                (select max(id) from t_trade_msg where trade_id=a.id 
                 group by trade_id)
                 where a.project_id=%s
                ''',t_project.id)
                return self.render(
                    "project/project_show.html",
                    get_filename_uuid4=self.get_filename_uuid4,
                    t_trade=t_trade,
                    t_logff_type=t_logff_type,
                    visible_project=visible_project,
                    md5_str=md5_str,
                    is_end=is_end,
                    dt=dt,
                    t_user_kfs=t_user_kfs,
                    t_projects_reject_titles=t_projects_reject_titles,
                    t_projects_information_reject=t_projects_information_reject,
                    curr_member=curr_member,
                    company_history_permission=company_history_permission,
                    is_cancel=is_cancel,
                    confirm_banjie=confirm_banjie,
                    t_projects_note_chengjiao=t_projects_note_chengjiao,
                    t_project_chuna_history=t_project_chuna_history,
                    t_projects_type1=t_projects_type1,
                    t_cutomer_addr_msg=t_cutomer_addr_msg,
                    t_express_send=t_express_send,
                    t_express_rec=t_express_rec,
                    payment_type=payment_type,
                    express_type=express_type,
                    express_list_type=express_list_type,
                    t_project_up=t_project_up,
                     t_project_down=t_project_down,
                    company_count=0,
                  customer_count=0,
                    company_history=company_history,
                    t_projects_relation=t_projects_relation,
                    t_relation_projects="",
                    addr_provider=addr_provider,
                    xiezhu_id=xiezhu_id,
                    addr_milepost=addr_milepost,
                    xiezhu_apply_mileposts=xiezhu_apply_mileposts,
                    t_customer=t_customer,
                    projects_addr_provider=projects_addr_provider,
                    t_projects_transitions_customer=t_projects_transitions_customer,
                    zones=zones,
                    area_type=area_type,
                    t_company_id=t_company_id,
                    t_projects_note_check=t_projects_note_check,
                    project_note_unread=project_note_unread,
                    item_transfile_sales=item_transfile_sales,
                    t_projects_types=t_projects_types,
                    t_user_teams_cq=t_user_teams_cq,
                    citys=citys,
                    mid=mid,
                    item_transfile=item_transfile,
                    visible_note=visible_note,
                    t_projects_type=t_projects_type,
                    is_ok=is_ok,
                    project_milepost_item = None,
                    project_milepost_type=project_milepost_type,
                    t_cq_service=t_cq_service,
                    project_note=project_note,
                    project_btypes=project_btypes,
                    t_project_state_msg1=t_project_state_msg1,
                    t_project_state_msg2=t_project_state_msg2,
                    t_project_state_msg3=t_project_state_msg3,
                    t_project_state_msg4=t_project_state_msg4,
                    t_project_state_msg5=t_project_state_msg5,
                    t_project_state_msg6=t_project_state_msg6,
                    t_project_state_msg7=t_project_state_msg7,
                    t_project_state_msg8=t_project_state_msg8,
                    t_project_state_msg9=t_project_state_msg9,
                    t_project_state_msg10=t_project_state_msg10,
                    t_project_state_msg11=t_project_state_msg11,
                    t_project_state1=t_project_state1,
                    t_project_state2=t_project_state2,
                    t_project_state3=t_project_state3,
                    t_project_state4=t_project_state4,
                    t_project_state5=t_project_state5,
                    t_project_state6=t_project_state6,
                    t_project_state7=t_project_state7,
                    t_project_state8=t_project_state8,
                    t_project_state9=t_project_state9,
                    t_project_state10=t_project_state10,
                    t_project_state11=t_project_state11,
                    t_projects_relate=t_projects_relate,
                    t_projects_income_all=t_projects_income_all,
                    t_projects_income_allmoney=t_projects_income_allmoney,
                    t_projects_linkmans=t_projects_linkmans,
                    t_projects_parents=t_projects_parents,
                    t_projects_transitions=t_projects_transitions,
                    t_projects_transitions_file=t_projects_transitions_file,
                    t_project_income=t_project_income,
                    t_project_income_wait=t_project_income_wait,
                    t_project_kf=t_project_kf,
                    t_users_kf=t_users_kf,
                    t_project_income_title=t_project_income_title,
                    t_income_other_type=t_income_other_type,
                    t_business_channel=t_business_channel,
                    t_building=t_building,
                    t_income_type=t_income_type,
                    t_promo_types=t_promo_types,
                    t_sign_type=t_sign_type,
                    getMemberName=self.getMemberName,
                    getMemberNameCQ1=self.getMemberNameCQ1,
                    wait_rec_income_money_other=wait_rec_income_money_other,
                    rec_income_money_other=rec_income_money_other,
                    t_projects_service_income_list=
                    t_projects_service_income_list,
                    t_projects_service_income=t_projects_service_income,
                    t_project_bussniss=t_project_bussniss,
                    t_talk_type=t_talk_type,
                    rec_income_money=rec_income_money.c,
                    wait_rec_income_money=wait_rec_income_money.c,
                    t_rec_contarct_type=t_rec_contarct_type,
                  #  t_projects_file=t_projects_file,
                    t_file_type_cate=t_file_type_cate,
                    t_file_type=t_file_type,
                    t_finance_confirm=t_finance_confirm,
                    t_company=t_company,
                    t_pay_type=t_pay_type,
                    t_business_type=t_business_type,
                    t_project=t_project,
                    form_tag="show",
                    t_project_role=t_project_role,
                    getMemberId=self.getMemberId,
                    getMemberIdInProject = self.getMemberIdInProject,
                    xiezhu_applys=xiezhu_applys,
                    t_user_teams=t_user_teams,
                    t_project_members=t_project_members,
                    created_at=datetime.datetime.now(),
                    search_key="")


        elif tag=='projects_yingshou':
            sql = ""
            qtype = self.get_argument("qtype","my")
            keyword = self.get_argument("keyword","")
            page = int(self.get_argument("page", 1))
            if qtype=="my":
                sql = " and e.acc_uid=%s "%(uid)
            pre_page = 20
            count = self.db.get('''
      select count(*) count
                        from  t_projects b
                                    left join (select aa.project_id,ifnull(sum(income_money),0)  aa from t_projects_income aa
                                                                            ,t_projects_income_title bb
                                                                            where aa.parent_id=bb.id and
                                                                            income_uid > 0 and income_id >43 group by aa.project_id) f
                                                                            on  b.id=f.project_id

                                    left join ( select   aa.project_id,ifnull(sum(income_money),0)  dd from t_projects_income aa
                                                                    ,t_projects_income_title bb
                                                                    where aa.parent_id=bb.id  and
                                                                    income_uid > 0 and income_id <=43  group by aa.project_id)  g  on
                                                                            b.id=g.project_id
                                    inner
                        join db_customer.t_customer e  on b.customer_company=e.company
                                                    where   customer_company!=""  and (all_income -dd) > 0


               ''' + sql)
            pagination = Pagination(page, pre_page, count.count, self.request)
            startpage = (page - 1) * pre_page

            customers = self.db.query("""
                    select acc_uid_name,customer_company,e.id,e.guid,
                        ifnull(sum(all_income),0) all_income,
                        ifnull(sum(aa),0) aa, ifnull(sum(dd),0) dd

                        from  t_projects b
                                    left join (select aa.project_id,ifnull(sum(income_money),0)  aa from t_projects_income aa
                                                                            ,t_projects_income_title bb
                                                                            where aa.parent_id=bb.id and
                                                                            income_uid > 0 and income_id >43 group by aa.project_id) f
                                                                            on  b.id=f.project_id

                                    left join ( select   aa.project_id,ifnull(sum(income_money),0)  dd from t_projects_income aa
                                                                    ,t_projects_income_title bb
                                                                    where aa.parent_id=bb.id  and
                                                                    income_uid > 0 and income_id <=43  group by aa.project_id)  g  on
                                                                            b.id=g.project_id
                                    inner
                        join db_customer.t_customer e  on b.customer_company=e.company
                                                    where    customer_company!="" and (all_income -dd) > 0  """
                                      + sql + """

                                                    group by customer_company,e.id,e.guid,acc_uid_name

                                                    limit %s,%s
            """, startpage, pre_page)
            self.render(
                'project/finance_list.html',
                keyword=keyword,
                customers=customers,
                pagination=pagination,
                tag=tag,
                qtype=qtype,
                search_key='')

        elif tag=="project_relation":
            uid=self.get_secure_cookie('uid')
            page = int(self.get_argument("page", 1))
            pre_page = 20
            count = self.db.get('''
                     SELECT  count(*) count
                FROM t_projects a

                left join (select member_id,project_id,GROUP_CONCAT(concat(member_name,'|',team_id)) team_list
                from t_projects_member group by project_id )  b
				 on a.id=b.project_id
                order by a.created_at desc
                ''')

            pagination = Pagination(page, pre_page, count.count, self.request)
            startpage = (page - 1) * pre_page

            t_projects = self.db.query('''
                SELECT  a.*, b.team_list
                FROM t_projects a

                left join (select *,GROUP_CONCAT(concat(member_name,'|',team_id)) team_list
                from t_projects_member  group by project_id )  b
				 on a.id=b.project_id
                 where find_in_set(%s,b.member_id)
                order by a.created_at desc
                ''',uid)

            self.render('project/project_relation.html',
            t_projects=t_projects,
            pagination=pagination,
            search_key='')

        elif tag=="note_check":
            page = int(self.get_argument("page", 1))
            not_check=self.get_argument('is_check','')
            project_name=self.get_argument('project_name','')
            fq_uid_name=self.get_argument('fq_uid_name','')
            params={
                'project_name':project_name,
                'fq_uid_name':fq_uid_name
            }
            pre_page = 20
            sql_project_name=''
            sql_fq_uid_name=''
            if project_name:
                sql_project_name+=' and b.project_name like "%%'+project_name+'%%" '
            if fq_uid_name:
                sql_fq_uid_name+=' and a.uid_name="%s" '%fq_uid_name
            if not_check:
                count=self.db.get(
                """ select count(*) count
                      from t_projects_note  a
                      inner join t_projects b
                     on a.project_id=b.id """+sql_project_name+"""
                     where  is_check=1 """+sql_fq_uid_name+"""
                       and a.id not in(
								select note_id from t_projects_note_check where note_id=a.id
                         )
                """)
                pagination = Pagination(page, pre_page, count.count, self.request)
                startpage = (page - 1) * pre_page
                t_projects_note_check=self.db.query(
                    """
                    select b.project_name,a.msg,c.state_id,
                     a.uid_name,b.id,b.guid,a.is_check
                     from t_projects_note a inner join t_projects b
                     on a.project_id=b.id"""+sql_project_name+"""
                     left join (select state_id,note_id,check_at from t_projects_note_check) c
                      on a.id=c.note_id
                     where  a.is_check=1"""+sql_fq_uid_name+"""
                       and a.id not in(
								select note_id from t_projects_note_check where note_id=a.id
                         )
                         order by  c.check_at desc,a.creatd_at desc  limit %s,%s
                    """,startpage,pre_page)
            else:
                count=self.db.get(
                    """ select count(*) count
                        from t_projects_note  a
                        inner join t_projects b
                        on a.project_id=b.id"""+sql_project_name+"""
                        where  is_check=1
                    """+sql_fq_uid_name)
                pagination = Pagination(page, pre_page, count.count, self.request)
                startpage = (page - 1) * pre_page
                t_projects_note_check=self.db.query(
                        """
                        select b.project_name,c.state_id,c.check_at,
                        a.uid_name,b.id,b.guid,a.msg,a.is_check
                        from t_projects_note a inner join t_projects b
                        on a.project_id=b.id"""+sql_project_name+"""
                         left join (select state_id,note_id,check_at from t_projects_note_check) c
                      on a.id=c.note_id
                        where  a.is_check=1"""+sql_fq_uid_name+"""
                            order by c.check_at desc,a.creatd_at desc
                        """)
            self.render(
                'project/note_not_check.html',
                pagination=pagination,
                tag=tag,
                params=params,
                not_check=not_check,
                t_projects_note_check=t_projects_note_check,
                search_key=''
            )
        elif tag=="not_check_detail":
            id=self.get_argument('id')
            t_customer=''
            t_project=self.db.get("""
                    select * from t_projects where id=%s
            """,id)
            if t_project:
                if t_project.customer_company:
                    t_customer=self.db_customer.get(' select id from t_customer where company=%s limit 1',t_project.customer_company)
            t_projects_note_check=self.db.query(
                    """
                    select * from t_projects_note a where project_id=%s and is_check=1
                       and id not in(
								select note_id from t_projects_note_check where note_id=a.id
                         )
                         order by creatd_at desc
                    """,id)
            t_project_all_check=self.db.query(
                """
                        select *,b.id check_id from t_projects_note a
                        left join t_projects_note_check b
                         on a.id=b.note_id
                        where a.project_id=%s and a.is_check=1
                         and a.id  in(
								select note_id from t_projects_note_check where note_id=a.id
                         )
                         order by a.creatd_at desc
                """,id
            )
            self.render(
                'project/note_not_check_detail.html',
                t_projects_note_check=t_projects_note_check,
                t_project_all_check=t_project_all_check,
                t_project_id=id,
                t_project=t_project,
                t_customer=t_customer,
                search_key=''
            )

        elif tag=="t_company":
            company=self.get_argument('company','')
            company_code=self.get_argument('company_code','')
            project_id=self.get_argument('project_id','')
            t_company=self.db.get('select * from t_company where company_name=%s',company)

            if t_company and t_company.company_code!=company_code:
                self.db.execute(
                    """
                    update t_company set company_code=%s,updated_uid=%s,updated_uid_name=%s,updated_at=%s
                     where company_name=%s
                    """,company_code,uid,uid_name,dt,company)
            elif not t_company:
                self.db.execute(
                """
                insert into t_company(company_name,company_code,created_at,uid,uid_name)
                 values(%s,%s,%s,%s,%s)
                """,company,company_code,dt,uid,uid_name)
            t_company=self.db.get('select * from t_company where company_name=%s',company)
            t_projects_transitions=self.db.query(
                """
                select * from t_projects_transition where project_id=%s and file_type=0 and project_company_type=1 order by created_at desc
                """,project_id)

            t_company_transitions=self.db.query(
                """
                select a.* from t_projects_transition a inner join t_company b
                 on a.company_id=b.id
                 where a.file_type=0 and a.project_company_type=2 order by a.created_at desc
                """)

            t_projects_type=self.db.query(
                    """
                    select * from t_projects_type where income_category='移交资料' order by order_int
                    """
                )
            t_project=self.db.get('''
                select * from t_projects where id=%s
            ''',project_id)
            self.render('project/project_company.html',
            t_company=t_company,
            project_id=project_id,
            t_projects_transitions=t_projects_transitions,
            t_company_transitions=t_company_transitions,
            t_projects_type=t_projects_type,
            t_project=t_project,
            search_key='')

        elif tag=="search_transition":
            company=self.get_argument('company')
            company_code=self.get_argument('company_code')
            sql_company=''
            sql_company_code=''
            if company and not company_code:
                t_project=self.db.query(''' select id,company_uid,customer_company from t_projects where customer_company like "%%'''+company+'''%%" ''')
            elif not company and company_code:
                t_project=self.db.query(''' select id,company_uid,customer_company from t_projects where company_uid like "%%'''+company_code+'''%%" ''')
            elif company and company_code:
                t_project=self.db.query(''' select id,company_uid,customer_company from t_projects where company_uid like "%%'''+company_code+'''%%" customer_company like "%%'''+company+'''%%" ''')
            if not t_project:
                pass
            self.write({'project':t_project})

        elif tag=="todo_arrange":
            my=self.get_argument('my','')
            uid_name=self.get_secure_cookie('name')
            todo=self.get_argument('todo','')
            fz_name=self.get_argument('fz_per','')
            bs_name=self.get_argument('bs_per','')
            department_name=self.get_argument('department','')
            project_name=self.get_argument('project','')
            company=self.get_argument('comp','')
            start_time=self.get_argument('start','')
            end_time=self.get_argument('end','')
            bs_area=self.get_argument('bs_area','')
            bs_address=self.get_argument('bs_addr','')
            page=int(self.get_argument('page',1))
            waitme = self.get_argument("waitme","")
            banli_time=self.get_argument('banli_time','')
            order_bl=self.get_argument('order_bl','')
            order_bl_time=self.get_argument('order_bl_time','')
            todo_tags_search=self.get_argument('todo_tags_search','')
            pre_page=10
            params={
                'todo_tags_search':todo_tags_search,
                'bs_address':bs_address,
                'bs_area':bs_area,
                'fz_name':fz_name,
                'bs_name':bs_name,
                'departmet_name':department_name,
                'company':company,
                'start_time':start_time,
                'end_time':end_time,
                'project_name':project_name,
                'banli_time':banli_time,
                'order_bl':order_bl,
                'order_bl_time':order_bl_time
            }
            sql=''
            sql1=''
            sql_nums=''
            sql_dep=''
            order_int=' a.created_at desc '
            if order_bl:
                order_int=' a.bl_date '+order_bl
            elif order_bl_time:
                order_int=' a.start_time '+order_bl_time
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
                sql_dep=' and b.department_name="%s" '%department_name
            if project_name:
                sql+=' and a.project_name like "%%'+project_name+'%%"'
            if company:
                sql+=' and a.company like "%%'+company+'%%"'
            if start_time and end_time:
                sql+=' and a.bl_date between "%s" and "%s"'%(start_time,end_time)
            if banli_time=='0':
                sql+= ' and a.start_time >= "08:00:00" and a.end_time <= "12:00:00" '
            if banli_time=='1':
                sql+= ' and a.start_time >= "12:00:00" and a.end_time <= "24:00:00" '
            if todo_tags_search:
                for item in todo_tags_search.split(','):
                    if item:
                        sql+=' and find_in_set("%s",todo_tags) '%item
            t_user = self.db.get('select * from t_user where id=%s',uid)
            department_sql = ""
            mycount_sql_str=""
            sql_my_leader=""

            if my:
                mycount_sql_str="  and responsible_per='"+uid_name+"'"
            if waitme:
                sql_my_leader = "  and a.leader_id=" + uid
            if t_user.department_name==u"会计部" or t_user.department_name==u"工商部":
                department_sql = " and b.department_name='"+t_user.department_name+"' "
                nums = self.db.get("""  select count(*) count,
                    (select count(*) c from t_todo_arrange_status a , t_todo_arrange b,t_user c where a.todo_id=b.id and
                    b.responsible_per=c.name and c.department_name=%s  and  a.created_at is null and a.updated_at is null and (banshi_per  is not null) """
                                   + mycount_sql_str + """) a,
                    (select count(*) c from t_todo_arrange_status a , t_todo_arrange b,t_user c where a.todo_id=b.id and
                    b.responsible_per=c.name and c.department_name=%s  and a.created_at is not null and a.updated_at is null """
                                   + mycount_sql_str + """) b,
                    (select count(*) c from t_todo_arrange_status a, t_todo_arrange b,t_user c where a.todo_id=b.id and
                    b.responsible_per=c.name and c.department_name=%s  and  a.created_at is not null and a.updated_at is not null """
                                   + mycount_sql_str + """)
                     c from t_todo_arrange_status aa

                        """, t_user.department_name, t_user.department_name,
                                   t_user.department_name)

            else:
                if my:
                    sql_nums=' inner join t_todo_arrange bbb on aa.todo_id=bbb.id and (bbb.responsible_per="%s" or bbb.banshi_per="%s") '%(uid_name,uid_name)
                nums=self.db.get(
                        """
                        select count(*) count,
                        (select count(*) c from t_todo_arrange_status aa """+sql_nums+""" inner join t_todo_arrange bb on aa.todo_id=bb.id where aa.created_at is null and aa.updated_at is null and (bb.banshi_per  is not null)) a,
                        (select count(*) c from t_todo_arrange_status aa """+sql_nums+""" where aa.created_at is not null and aa.updated_at is null) b,
                        (select count(*) c from t_todo_arrange_status aa """+sql_nums+""" where aa.created_at is not null and aa.updated_at is not null) c
                         from t_todo_arrange_status d
                        """
                    )
            wait_my_sql=""
            if my:
                wait_my_sql = "  and ( a.leader_id = " + uid+" or   responsible_per='"+uid_name+"' or a.leader_id='"+uid+"') "
            wait_per_count = self.db.get(
                """select count(*) count,
                ( select count(*) count from t_todo_arrange a ,t_todo_arrange_status c  ,t_user b
                 where a.id=c.todo_id and  a.responsible_per=b.name and  banshi_per is not null and  todo_type=0
                 """+ department_sql + wait_my_sql+"""
                 ) count1
                from t_todo_arrange a ,t_todo_arrange_status c  ,t_user b  where a.id=c.todo_id and  a.responsible_per=b.name and  banshi_per is null  """
                + department_sql + wait_my_sql)


            departments=self.db.query(
                """
                select name from t_user_department where parent_id=0
                """
            )

            area_type=self.db.query(
                """
                select income_name from t_projects_type where income_category='区域'
                """
            )



            if todo=="-1000" or todo=='-2000':

                if todo == '1':
                    sql1 = 'and d.created_at is NULL and d.updated_at is NULL and (banshi_per  is not null) '
                elif todo == '2':
                    sql1 = 'and d.created_at is not NULL and d.updated_at is NULL '
                elif todo == '3':
                    sql1 = 'and d.created_at is not NULL and d.updated_at is not NULL '
                elif todo == "-1000":
                    sql1 += " and a.banshi_per is null and banshi_per is null"
                elif todo=="-2000":
                    sql1 += " and todo_type=0 and banshi_per is not null"
                    order_int=' a.leader_distribute_at desc, '+order_int
                count = self.db.get("""
               select count(*) count
                from t_todo_arrange a inner join t_user b
                 on a.responsible_per=b.name
                 left join t_user c on a.banshi_per=c.name
                  inner join t_todo_arrange_status d
                   on a.id=d.todo_id
                   where is_hide=0 """ + wait_my_sql
                                    + sql1 + sql + department_sql + """
                    """)
                pagination = Pagination(page, pre_page, count.count,
                                        self.request)
                startpage = (page - 1) * pre_page
                todo_arranges = self.db.query("""
                select a.*,b.phone phone_fz ,b.department_name,c.phone phone_bs,
                 d.created_at bs_created_at,d.updated_at fz_updated_at
                from t_todo_arrange a inner join t_user b
                 on a.responsible_per=b.name
                 left join t_user c on a.banshi_per=c.name
                  inner join t_todo_arrange_status d
                   on a.id=d.todo_id

                   where is_hide=0  """ + wait_my_sql + sql1 + sql +
                                              department_sql + """
                    order by """+order_int+""" limit %s,%s """, startpage,
                                              pre_page)
# t_todo_arrange a ,t_todo_arrange_status c  ,t_user b  where a.id=c.todo_id and  a.responsible_per=b.name and  banshi_per is null

            elif my:

                if todo=='1':
                    sql1='and d.created_at is NULL and d.updated_at is NULL and (banshi_per  is not null)'
                elif todo=='2':
                    sql1='and d.created_at is not NULL and d.updated_at is NULL '
                elif todo=='3':
                    sql1='and d.created_at is not NULL and d.updated_at is not NULL '
                elif todo == "-1000":
                    sql1 += " and todo_type=0 and banshi_per is null"
                elif todo=="-2000":
                    sql1 += " and todo_type=0 and banshi_per is not null"

                count=self.db.get(
                    """
                select count(*) count
                from t_todo_arrange a inner join t_user b
                 on a.responsible_per=b.name
                 left join t_user c on a.banshi_per=c.name
                  inner join t_todo_arrange_status d
                   on a.id=d.todo_id
                   where (a.responsible_per=%s or a.banshi_per=%s) """+sql1+department_sql+sql+"""
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
                   where (a.responsible_per=%s or a.banshi_per=%s) """+sql1+sql+"""
                    order by """+order_int+""" limit %s,%s """,uid_name,uid_name,startpage,pre_page)
            else:

                if sql:

                    if todo=='1':
                        sql+=' and d.created_at is NULL and d.updated_at is NULL and (banshi_per  is not null)'
                    elif todo=='2':
                        sql+=' and d.created_at is not NULL and d.updated_at is NULL '
                    elif todo=='3':
                        sql+='  and d.created_at is not NULL and d.updated_at is not NULL '
                    elif todo=="-1000":
                        sql += " and todo_type=0 and banshi_per is null"

                    count=self.db.get(
                    """
                    select count(*) count
                    from t_todo_arrange a inner join t_user b
                    on a.responsible_per=b.name
                    left join t_user c on a.banshi_per=c.name
                    inner join t_todo_arrange_status d
                    on a.id=d.todo_id where """+sql[4:]+department_sql+"""
                    order by a.created_at desc""")
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
                    on a.id=d.todo_id where """+sql[4:]+department_sql+"""
                    order by """+order_int+""" limit %s,%s""",startpage,pre_page)

                else:
                    sql=""
                    if todo=='1':
                        sql = 'where d.created_at is null and d.updated_at is null and (banshi_per  is not null) '
                    elif todo=='2':
                        sql='where d.created_at is not NULL and d.updated_at is NULL'
                    elif todo=='3':
                        sql='where d.created_at is not NULL and d.updated_at is not NULL'
                    elif todo == "-1000":
                        sql += " and todo_type=0 and banshi_per is null"


                    count=self.db.get(
                        """
                        select count(*) count
                        from t_todo_arrange a inner join t_user b
                        on a.responsible_per=b.name
                        left join t_user c on a.banshi_per=c.name
                        inner join t_todo_arrange_status d
                        on a.id=d.todo_id """+sql+department_sql+"""
                        order by a.created_at desc
                        """
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
                        on a.id=d.todo_id """+sql+department_sql+"""
                         order by """+order_int+""" limit %s,%s
                        """,startpage,pre_page)
            t_todo_leader = self.db.query("select * from t_todo_leader where is_hide=0")
            responsible_per=self.db.query('''
                select responsible_per responsible_per_name from t_todo_arrange a
                inner join t_user b on a.responsible_per=b.name and b.is_lock=0 '''+sql_dep+''' group by responsible_per_name
            ''')
            banshi_per = self.db.query('''
              select banshi_per banshi_per_name from t_todo_arrange a
                inner join t_user b on a.banshi_per=b.name and  b.is_lock=0 group by banshi_per_name 
            ''')
            todo_tags=self.db_company.query('''
                select group_concat(id,'_',tag_name) gc,tag_category 
                 from t_company_tag where is_hide=2 group by tag_category order by order_int 
            ''')
            self.render(
                'project/todo_arrange.html',
                search_key='',
                todo_tags=todo_tags,
                t_todo_leader=t_todo_leader,
                my=my,
                responsible_per=responsible_per,
                banshi_per=banshi_per,
                params=params,
                area_type=area_type,
                departments=departments,
                todo=todo,
                nums=nums,
                tag=tag,
                pagination=pagination,
                todo_arranges=todo_arranges,
                wait_per_count=wait_per_count,
            )

        elif tag=="bj_manage":
            # order=self.get_argument('order',0)
            page=int(self.get_argument('page',1))
            pre_page=20
            # area_search=self.get_argument('area_search','')
            # project_type_search=self.get_argument('project_type_search','')
            # is_kp_addr_search=self.get_argument('is_kp_addr_search','')
            # is_fhq_search=self.get_argument('is_fhq_search','')
            # params={
            #     'area_search':area_search,
            #     'project_type_search':project_type_search,
            #     'is_fhq_search':is_fhq_search,
            #     'is_kp_addr_search':is_kp_addr_search
            # }
            # sql=''
            # if area_search:
            #     sql+=' and a.area="%s" '%area_search
            # if project_type_search:
            #     sql+=' and a.project_type like "%%'+project_type_search+'%%" '
            # if  is_kp_addr_search:
            #     sql+=' and a.is_kp_addr=%s'% is_kp_addr_search
            # if is_fhq_search:
            #     sql+=' and a.is_fhq=%s'%is_fhq_search
            # if sql:
            #     sql=' where '+sql[4:]
            # count=self.db.get('''
            #   select count(*) count from  t_bj_manage a '''+sql)
            # if order=='1':
            #     sql+=' order by a.area desc, '
            # else:
            #     sql+=' order by a.area, '
            # area_type=self.db.query(
            #     """
            #     select income_name from t_projects_type where income_category='区域'
            #     """
            # )
            # pagination=Pagination(page,pre_page,count.count,self.request)
            # startpage=(page-1) * pre_page
            # bj_manage=self.db.query('''
            # select a.*,
            # (select GROUP_CONCAT(concat('报价:',price,'&nbsp;&nbsp;','报价人:',bj_name,'&nbsp;&nbsp;','时间:',date(created_at)))
            #  from t_bj_price_history  where bj_mange_id=a.id) b,
            #  (select price from t_bj_price_history where bj_mange_id=a.id order by created_at desc limit 1) c
            #  from  t_bj_manage a '''+sql+''' a.created_at desc limit %s,%s''',startpage,pre_page)
            manage_type=self.get_argument('manage_type','0')
            params={
                'manage_type':manage_type
            }
            area_type=self.db.query(
                """
                select income_name from t_projects_type where income_category='区域'
                """
            )
            count=self.db.get('''  select count(*) count
            from t_addr_provider_manage  where manage_type=%s ''',manage_type)
            pagination=Pagination(page,pre_page,count.count,self.request)
            startpage=(page-1) * pre_page
            addr_provider_manage=self.db.query('''
             select *
              from t_addr_provider_manage
              where manage_type=%s
            order by order_at desc,order_int desc limit %s,%s
            ''',manage_type,startpage,pre_page)

            self.render('project/bj_manage.html',
            search_key='',
            addr_provider_manage=addr_provider_manage,
            pagination=pagination,
            manage_type=manage_type,
            area_type=area_type,
            params=params,
             tag=tag,
            )
        elif tag=="bj_manage_yw":
            # order=self.get_argument('order',0)
            page=int(self.get_argument('page',1))
            pre_page=20
            manage_type=self.get_argument('manage_type','0')

            product_bid = self.db_ext.query("select a.*,b.name category_name from t_products a , t_category b where a.category_id=b.id  order by b.order_int")
            t_category=self.db_ext.query(" select * from t_category ")
            self.render('project/bj_manage_yw.html',
            search_key='',
            product_bid=product_bid,
            t_category=t_category,
            manage_type=manage_type,
            tag=tag,
            )

        elif tag=="provider_manage":
            is_gy_manage = self.get_secure_cookie("is_gy_manage")
            if is_gy_manage !="1":
                return self.write("0")
            kz=self.get_argument('kz','')
            page=int(self.get_argument('page',1))
            pre_page=20
            area_type=self.db.query(
                """
                select income_name from t_projects_type where income_category='区域'
                """
            )
            count=self.db.get('''  select count(*) count from t_addr_provider_manage''')
            pagination=Pagination(page,pre_page,count.count,self.request)
            startpage=(page-1) * pre_page
            addr_provider_manage=self.db.query('''
             select a.*,
             (select price from t_addr_provider_history where addr_id=a.id order by created_at desc limit 1) b,
             (select GROUP_CONCAT(concat('价格:',price,'&nbsp;&nbsp;','报价人:',uid_name,'&nbsp;&nbsp;','时间:',date(created_at)))
             from t_addr_provider_history  where addr_id=a.id) c
              from t_addr_provider_manage a
            order by a.created_at desc limit %s,%s
            ''',startpage,pre_page)

            count1=self.db.get('''  select count(*) count  from t_kz_provider_manage''')
            pagination1=Pagination(page,pre_page,count1.count,self.request)
            startpage1=(page-1) * pre_page
            kz_provider_manage=self.db.query('''
            select a.*,
             (select price from t_kz_provider_history where kz_id=a.id order by created_at desc limit 1) b,
             (select GROUP_CONCAT(concat('价格:',price,'&nbsp;&nbsp;','报价人:',uid_name,'&nbsp;&nbsp;','时间:',date(created_at)))
             from t_kz_provider_history  where kz_id=a.id) c
             from t_kz_provider_manage a order by a.created_at desc limit %s,%s
            ''',startpage1,pre_page)
            self.render(
                'project/provider_manage.html',
                search_key='',
                kz=kz,
                area_type=area_type,
                addr_provider_manage=addr_provider_manage,
                pagination=pagination,
                pagination1=pagination1,
                kz_provider_manage=kz_provider_manage)

        elif tag=="relation_projects":
            page=int(self.get_argument('page',1))
            pre_page=20
            cq = self.get_argument("cq", "")
            xiaoshou=self.get_argument('xiaoshou','')
            kefu = self.get_argument("kefu", "")
            building_id = self.get_argument("building_id", "")
            income_bussniss = self.get_argument("income_bussniss", "")
            from_id = self.get_argument("from_id", "")
            start = self.get_argument("start", "")
            end = self.get_argument("end", "")
            key = self.get_argument("key","")
            showtype = self.get_argument("showtype","")
            show_tag=self.get_argument('show_tag','')
            kfgw=self.get_argument('kfgw','')
            params = {
                "income_bussniss": income_bussniss,
                "cq": cq,
                "xiaoshou": xiaoshou,
                "kefu": kefu,
                "from_id": from_id,
                "building_id": building_id,
                "start": start,
                "end": end,
                "key": key,
                "showtype":showtype,
                "show_tag":show_tag,
                "kfgw":kfgw
            }
            add_sql = "  "
            sql_income_bussniss = ""
            sql_cq = ""
            sql_xs=""
            sql_kefu = ""
            sql_kfgw=""
            sql_from_id = ""
            sql_building_id = ""
            sql_date = ""
            sql_key = ""
            sql_join=''' inner join t_projects_member c on a.id=c.project_id
                   '''
            if income_bussniss and income_bussniss != "0":
                sql_income_bussniss = " and a.id in (select project_id from t_projects_service_income aaaa where  service_money > 0 and  service_id=%s and aaaa.project_id=a.id)  " % (
                    income_bussniss)
            if key and key != "0":
                sql_key = ''' and  a.id in (select project_id from t_projects_member aaaa where  aaaa.project_id=a.id  and (a.id like "%%'''+key+'''%%" or a.project_name like   "%%''' + key + '''%%"  or a.customer_name like   "%%''' + key + '''%%"  or a.customer_tel like   "%%''' + key + '''%%" or a.customer_company like   "%%''' + key + '''%%"))  '''

            if cq and cq != "0":
                sql_cq = " and  a.id in (select project_id from t_projects_member aaaa where  team_id=38 and member_id=%s and aaaa.project_id=a.id)  " % (
                    cq)
            if xiaoshou and xiaoshou!="0":
                sql_xs = " and  a.id in (select project_id from t_projects_member aaaa where  team_id=34 and member_id=%s and aaaa.project_id=a.id)  " % (
                    xiaoshou)
            if kefu and kefu != "0":
                sql_kefu = "and  a.id in (select project_id from t_projects_member aaaa where  team_id=39 and member_id=%s and aaaa.project_id=a.id) " % (
                    kefu)
            if kfgw and kfgw!="0":
                sql_kfgw = "and  a.id in (select project_id from t_projects_member aaaa where  team_id=36 and member_id=%s and aaaa.project_id=a.id) " % (
                    kfgw)
            if from_id and from_id != "0":
                sql_from_id = " and a.busniess_from_id=%s" % (from_id)
            if building_id and building_id != "0":
                sql_building_id = " and a.building_id=%s" % (building_id)
            if start and end:
                sql_date = " and a.created_at between '%s' and '%s'" % (start,end)
            add_sql = sql_income_bussniss + sql_cq + sql_xs + sql_kefu+sql_kfgw + sql_from_id + sql_building_id + sql_date + sql_key
            if add_sql:
                add_sql=' where '+add_sql[4:]
            print uid_name,showtype
            if showtype=="recommend":
                add_sql+=" and recommend_staff='%s' "%(uid_name)

            else:
                if show_tag=='other_projects':
                    sql_join='''
                     inner join  t_user_visible_other d on  a.uid=d.be_checker_id and d.checker_id=%s
                    '''%uid

                elif show_tag=='other_relation_projects':
                    sql_join+='''
                    inner join  t_user_visible_other d on d.be_checker_id=member_id and d.checker_id=%s and a.uid!=d.be_checker_id
                '''%uid
                else:
                    add_sql+=" and member_id=%s "%(uid)
            t_project_bussniss = self.db.query(
                """select * from t_projects_type where income_category='业务类型' order by order_int  """
            )

            t_income_type = self.db.query("""
                select * from t_projects_type where income_category='业务来源' order by order_int desc
                """)


            t_building = self.db.query(
                "select * from t_projects_type where income_category='楼盘' order by order_int desc "
            )
            t_user_cq = self.db.query("SELECT * FROM t_user  where role=9 ")
            t_users = self.db.query(
                "SELECT * FROM t_user_teams a , t_user b where b.id=a.uid ")
            count = self.db.get('''
                     SELECT count(*) count  FROM t_projects a
                   '''+sql_join+add_sql)

            pagination=Pagination(page,pre_page,count.count,self.request)
            startpage=(page-1)*pre_page
            t_projects = self.db.query('''
                     SELECT a.*,b.team_list  FROM t_projects a
                    left join (select project_id,GROUP_CONCAT(concat(member_name,'|',team_id)) team_list
                from t_projects_member group by project_id )  b
				 on a.id=b.project_id

                    '''+sql_join+add_sql+'''
                        order by a.created_at desc limit %s,%s
                        ''',startpage, pre_page)
            self.render('project/relation_projects.html',
            tag=tag,
            t_projects=t_projects,
            t_project_bussniss=t_project_bussniss,
            t_income_type=t_income_type,
            t_building=t_building,
            t_user_cq=t_user_cq,
            t_users=t_users,
            pagination=pagination,
            params=params,
            search_key='')

        elif tag=="search_addr":
            area=self.get_argument('area','')
            addr_type=self.get_argument('addr_type','')
            provider=self.get_argument('provider','')
            sql=''
            if area:
                sql+=' and area="%s"'%area
            if addr_type:
                sql+=' and addr_type like"%%'+addr_type+'%%"'
            if provider:
                sql+=' and provider like "%%'+provider+'%%"'
            if sql:
                addr_provider=self.db.query('''
            select id,area,addr_type,provider,danbao_matter,fp_limit from t_addr_provider_manage where
            '''+sql[4:])
            self.write({'addr_provider':addr_provider})

        elif tag=="list_addr_confirm":
            confirm=self.get_argument('confirm','')
            page=int(self.get_argument('page',1))
            order=' order by a.fz_id ,a.caiwu_confirm,created_at desc '
            pre_page=20
            if confirm:
                order='  order by a.caiwu_confirm, a.fz_id desc,created_at desc '
            count=self.db.get('''
                    select count(*) count from t_projects_addr_provider a
                    inner join t_addr_provider_manage b
                    on a.addr_id=b.id
                ''')
            pagination=Pagination(page,pre_page,count.count,self.request)
            startpage=(page-1)*pre_page
            projects_addr_provider=self.db.query('''
                    select a.*,b.area,b.addr_type,b.provider,b.danbao_matter,
                    b.fp_limit,c.id project_id,c.project_name,c.customer_company,
                    c.customer_name,c.guid from t_projects_addr_provider a
                    left join t_addr_provider_manage b
                    on a.addr_id=b.id
                    inner join t_projects c
                    on a.project_id=c.id '''+order+'''limit %s,%s
                    ''',startpage,pre_page)
            self.render(
                'project/list_addr_confirm.html',
                projects_addr_provider=projects_addr_provider,
                pagination=pagination,
                search_key=''
            )

        elif tag=="xiezhu_apply":
            page=int(self.get_argument('page',1))
            pre_page=20
            xiezhu_id=self.get_argument('xiezhu_id','')
            todo=self.get_argument('todo','')
            t_project=''
            search_project=self.get_argument('search_project','')
            xiezhu_content=self.get_argument('xiezhu_content','')
            gs_uid=self.get_argument('gs_uid','')
            xs_guwen_uid=self.get_argument('xs_guwen_uid','')
            t_user_teams=self.db.query(
                   """
                    select a.*,b.team_id from t_user a inner join t_user_teams b on a.id=b.uid
                    """
                    )
            sql=""
            search_sql=""
            search_pro=""
            sql_sum=[]
            for i in range(9):
                sql_sum.append('')
            params={
                'search_project':search_project,
                'xiezhu_content':xiezhu_content,
                'gs_uid':gs_uid,
                'xs_guwen_uid':xs_guwen_uid
            }
            if search_project:
                search_pro+=''' a.project_id=aa.id and (aa.id like "%%'''+search_project+'''%%"
                     or aa.customer_company like "%%'''+search_project+'''%%"
                     or aa.project_name like "%%'''+search_project+'''%%"
                     or aa.customer_name like "%%'''+search_project+'''%%"
                     ) '''

            if search_pro:
                search_sql+=' inner join t_projects aa on '+search_pro

            if gs_uid:
                search_sql+='''
                 inner join t_xiezhu_apply_milepost bb
                 on a.id=bb.xiezhu_id and bb.type_name='待审核' and bb.uid=%s
                 '''%gs_uid
            if xs_guwen_uid:
                search_sql+='''
                 inner join t_xiezhu_apply_milepost cc
                 on a.id=cc.xiezhu_id and cc.type_name='待接单' and cc.uid=%s
                 '''%xs_guwen_uid
            if xiezhu_content:
                search_sql+=' where a.xiezhu_content like "%%'+xiezhu_content+'%%"'


            if todo=='1':
                sql+=''' inner join t_xiezhu_apply_milepost h
                   on a.id=h.xiezhu_id and h.type_name="待审核"
                   and h.confirm_at is null and h.is_pass is null '''
            elif todo=='2':
                sql+=''' inner join t_xiezhu_apply_milepost i
                   on a.id=i.xiezhu_id and i.type_name="待审核"
                    and i.is_pass=0 '''
            elif todo=='3':
                sql+=''' inner join t_xiezhu_apply_milepost j
                   on a.id=j.xiezhu_id and j.type_name="待审核"
                    and j.confirm_at is not null inner join
                    t_xiezhu_apply_milepost k on a.id=k.xiezhu_id
                    and k.type_name="待接单" and k.confirm_at is null
                     '''
            elif todo=='4':
                sql+=''' inner join t_xiezhu_apply_milepost l
                        on a.id=l.xiezhu_id and l.type_name="待接单"
                         and l.confirm_at is not null where
                         (select count(*) count  from t_xiezhu_apply_milepost
                         where a.id=xiezhu_id and
                          type_name="结果审核")=0
                     '''
            elif todo=='5':
                sql+=''' inner join t_xiezhu_apply_milepost o
                        on a.id=o.xiezhu_id and o.type_name="结果审核"
                         and o.confirm_at is null and o.is_pass is null
                     '''
            elif todo=='6':
                sql+=''' inner join t_xiezhu_apply_milepost p
                        on a.id=p.xiezhu_id and p.type_name="结果审核"
                         and p.confirm_at is null and p.is_pass=0
                     '''
            elif todo=='7':
                sql+='''
                         inner join t_xiezhu_apply_milepost r on a.id=r.xiezhu_id and
                         r.type_name="已确认" and r.confirm_at is null
                '''
            elif todo=='8':
                sql+='''
                         inner join t_xiezhu_apply_milepost r on a.id=r.xiezhu_id and
                         r.type_name="已确认" and r.confirm_at is not null
                '''
            if role!='7' and role!='8':
                sql_sum=[]
                sql_sum.append(' and (h.uid=%s or h.fz_id=%s) '%(uid,uid))
                sql_sum.append(' and (i.uid=%s or i.fz_id=%s) '%(uid,uid))

                sql_sum.append('''
                 inner join t_xiezhu_apply_milepost ccc
                 on cc.id=ccc.xiezhu_id and ccc.type_name="待审核" and (ccc.uid=%s or ccc.fz_id=%s)
                '''%(uid,uid))


                sql_sum.append(''' inner join t_xiezhu_apply_milepost ddd
                 on dd.id=ddd.xiezhu_id and (ddd.type_name="待审核" or ddd.type_name="待接单") and (ddd.uid=%s or ddd.fz_id=%s)
                '''%(uid,uid))

                sql_sum.append('''
                 inner join t_xiezhu_apply_milepost eee
                 on ee.id=eee.xiezhu_id and (eee.type_name="待审核" or eee.type_name="待接单") and (eee.uid=%s or eee.fz_id=%s)
                '''%(uid,uid))

                sql_sum.append(''' inner join t_xiezhu_apply_milepost fff
                 on ff.id=fff.xiezhu_id and (fff.type_name="待审核" or fff.type_name="待接单") and (fff.uid=%s or fff.fz_id=%s)
                 '''%(uid,uid))
                sql_sum.append(''' inner join t_xiezhu_apply_milepost ggg
                 on gg.id=ggg.xiezhu_id and (ggg.type_name="待审核" or ggg.type_name="待接单") and (ggg.uid=%s or ggg.fz_id=%s)
                '''%(uid,uid))
                sql_sum.append(''' inner join t_xiezhu_apply_milepost hhh
                 on hh.id=hhh.xiezhu_id and (hhh.type_name="待审核" or hhh.type_name="待接单") and (hhh.uid=%s or hhh.fz_id=%s)
                '''%(uid,uid))
                sql_sum.append(""" inner join t_xiezhu_apply_milepost cd
                 on tt.id=cd.xiezhu_id and (cd.type_name='待审核' or cd.type_name='待接单') and (cd.uid=%s or cd.fz_id=%s) """%(uid,uid))
            sum=self.db.get('''
                select count(*) count ,
                (select count(*) c  from t_xiezhu_apply aa inner
                    join t_xiezhu_apply_milepost h
                   on aa.id=h.xiezhu_id and h.type_name="待审核"
                   and h.confirm_at is null and h.is_pass is null '''+sql_sum[0]+''') a,

                  (select count(*) c  from t_xiezhu_apply bb inner join
                  t_xiezhu_apply_milepost i
                   on bb.id=i.xiezhu_id and i.type_name="待审核"
                    and i.is_pass=0 '''+sql_sum[1]+''') b,

                     (select count(*) c  from t_xiezhu_apply cc inner
                     join t_xiezhu_apply_milepost j
                   on cc.id=j.xiezhu_id and j.type_name="待审核"
                    and j.confirm_at is not null '''+sql_sum[2]+''' inner join
                    t_xiezhu_apply_milepost k on cc.id=k.xiezhu_id
                    and k.type_name="待接单" and k.confirm_at is null ) c,

                     (select count(*) c  from t_xiezhu_apply dd
                       inner join t_xiezhu_apply_milepost l
                        on dd.id=l.xiezhu_id and l.type_name="待接单"
                         and l.confirm_at is not null '''+sql_sum[3]+''' where
                         (select count(*) count  from t_xiezhu_apply_milepost
                         where dd.id=xiezhu_id and
                          type_name="结果审核")=0) d,

                     (select count(*) c  from t_xiezhu_apply ee inner
                     join t_xiezhu_apply_milepost o
                        on ee.id=o.xiezhu_id and o.type_name="结果审核"
                         and o.confirm_at is null and o.is_pass is null'''+sql_sum[4]+''') e,

                     (select count(*) c  from t_xiezhu_apply ff  inner
                     join t_xiezhu_apply_milepost p
                        on ff.id=p.xiezhu_id and p.type_name="结果审核"
                         and p.confirm_at is null and p.is_pass=0 '''+sql_sum[5]+''') f,

                     (select count(*) c  from t_xiezhu_apply gg inner
                     join t_xiezhu_apply_milepost q on gg.id=q.xiezhu_id and
                         q.type_name="已确认" and q.confirm_at is null '''+sql_sum[6]+''') g,
                     (select count(*) c  from t_xiezhu_apply hh inner
                      join t_xiezhu_apply_milepost r on hh.id=r.xiezhu_id and
                         r.type_name="已确认" and r.confirm_at is not null '''+sql_sum[7]+''') h
                    from t_xiezhu_apply tt '''+sql_sum[8])
            if role=='7' or role=='8':
                count=self.db.get('''
                select count(*) count from t_xiezhu_apply a
            '''+sql+search_sql)
                pagination=Pagination(page,pre_page,count.count,self.request)
                start_page=(page-1)*pre_page

                xiezhu_applys=self.db.query('''
                select a.*,b.project_name,b.customer_name,b.customer_company,b.guid,b.id project_id,
                c.uid_name gs_uid_name,c.uid gs_uid,c.confirm_at gs_confirm_at,c.is_pass gs_is_pass,c.id gs_id,
                d.uid_name xs_uid_name,d.confirm_at xs_confirm_at,d.id xs_id,
                datediff(f.confirm_at,d.confirm_at) zhouqi,
                f.uid_name sh_uid_name,f.confirm_at sh_confirm_at,f.is_pass sh_is_pass,f.created_at sh_created_at,f.id sh_id,
                f.fz_name sh_fz_name,
                g.uid_name queren_uid_name,g.confirm_at queren_confirm_at,g.id queren_id
                 from t_xiezhu_apply a
                inner join t_projects b
                 on a.project_id=b.id
                left join t_xiezhu_apply_milepost c
                 on a.id=c.xiezhu_id and c.type_name='待审核'
                left join  t_xiezhu_apply_milepost d
                 on a.id=d.xiezhu_id and d.type_name='待接单'
                left join  t_xiezhu_apply_milepost f
                 on a.id=f.xiezhu_id and f.type_name='结果审核'
                left join  t_xiezhu_apply_milepost g
                 on a.id=g.xiezhu_id and g.type_name='已确认'
                 '''+sql+search_sql+'''
                 order by a.created_at desc limit %s,%s
            ''',start_page,pre_page)
            else:
                count=self.db.get('''
                select count(*) count from t_xiezhu_apply a
                inner join t_xiezhu_apply_milepost cd
                 on a.id=cd.xiezhu_id and (cd.type_name='待审核' or cd.type_name='待接单') and (cd.uid=%s or cd.fz_id=%s)
            '''+sql+search_sql,uid,uid)
                pagination=Pagination(page,pre_page,count.count,self.request)
                start_page=(page-1)*pre_page

                xiezhu_applys=self.db.query('''
                select a.*,b.project_name,b.customer_name,b.customer_company,b.guid,b.id project_id,
                c.uid_name gs_uid_name,c.uid gs_uid,c.confirm_at gs_confirm_at,c.is_pass gs_is_pass,c.id gs_id,
                d.uid_name xs_uid_name,d.confirm_at xs_confirm_at,d.id xs_id,
                datediff(f.confirm_at,d.confirm_at) zhouqi,
                f.uid_name sh_uid_name,f.confirm_at sh_confirm_at,f.is_pass sh_is_pass,f.created_at sh_created_at,f.id sh_id,
                f.fz_name sh_fz_name,
                g.uid_name queren_uid_name,g.confirm_at queren_confirm_at,g.id queren_id
                 from t_xiezhu_apply a
                inner join t_projects b
                 on a.project_id=b.id
                left join t_xiezhu_apply_milepost c
                 on a.id=c.xiezhu_id and c.type_name='待审核'
                left join  t_xiezhu_apply_milepost d
                 on a.id=d.xiezhu_id and d.type_name='待接单'
                left join  t_xiezhu_apply_milepost f
                 on a.id=f.xiezhu_id and f.type_name='结果审核'
                left join  t_xiezhu_apply_milepost g
                 on a.id=g.xiezhu_id and g.type_name='已确认'
                inner join t_xiezhu_apply_milepost cd
                 on a.id=cd.xiezhu_id and (cd.type_name='待审核' or cd.type_name='待接单') and (cd.uid=%s or cd.fz_id=%s)
                 '''+sql+search_sql+'''
                 order by a.created_at desc limit %s,%s
            ''',uid,uid,start_page,pre_page)
            self.render(
                'project/list_xiezhu_apply.html',
                todo=todo,
                tag=tag,
                sum=sum,
                params=params,
                search_key='',
                t_project=t_project,
                pagination=pagination,
                t_user_teams=t_user_teams,
                xiezhu_applys=xiezhu_applys
            )

        elif tag=="xiezhu_apply_detail":
            xiezhu_id=self.get_argument('xiezhu_id')
            xiezhu_apply_mileposts=self.db.query('''
                select id,type_name,uid,uid_name,remark,is_pass,date_format(created_at,'%%Y-%%m-%%d') created_at,
                date_format(confirm_at,'%%Y-%%m-%%d') confirm_at,date_format(reject_at,'%%Y-%%m-%%d') reject_at,fz_name,fz_id
                from t_xiezhu_apply_milepost where xiezhu_id=%s
            ''',xiezhu_id)
            self.write({'mileposts':xiezhu_apply_mileposts})

        elif tag=="search_relation_project":
            project_id=self.get_argument('project_id','')
            project_name=self.get_argument('project_name','')
            current_id=self.get_argument('current_id','')
            sql=''
            if project_id:
                sql+=' and a.id=%s'%project_id
            if project_name:
                sql+=' and a.project_name like "%%'+project_name+'%%"'
            if sql:
                sql=' where'+sql[4:]
            t_projects=self.db.query('''
                select a.id, find_in_set('''+current_id+''',b.relation_ids) is_inside,a.customer_company,a.project_name,b.id relation_id from t_projects a
                left join t_projects_relation b
                on find_in_set(cast(a.id as char(10)),b.relation_ids)
            '''+sql)
            self.write({'projects':t_projects})

        elif tag=="same_company":
            customer_company=self.get_argument('customer_company','')
            company=self.get_argument('company','')
            project_id=self.get_argument('project_id','')
            same_project=''
            same_customer=''
            if company!=customer_company:
                customer=self.db_customer.get('''
                    select id,company from t_customer where company=%s limit 1
                    ''',customer_company)
                same_project=self.db.get('''
            select customer_company from t_projects where customer_company=%s group by customer_company having count(*)>1
        ''',company)
                same_customer=self.db_customer.get('''
                select company from t_customer where company=%s limit 1
        ''',company)

            else:
                customer='-2'


            self.write({'customer':customer,'project':same_project,'same_customer':same_customer})

        elif tag=="kf_count":
            todo=self.get_argument('todo','')
            all_income=self.get_argument('all_income','')
            page=int(self.get_argument('page',1))
            pre_page=20
            sql=''
            if todo=='1':
                sql+=" where busniess_from_id_name='推广' "
            if todo=='2':
                sql+=" where busniess_from_id_name='客户推荐' "
            if todo=='3':
                sql+=" where busniess_from_id_name='内部推荐' "
            if todo=='4':
                sql+=" where busniess_from_id_name='楼盘' "

            kf_count=self.db.query('''
                select uid_name,count(*) count,sum(all_income) all_incomes,DATE_FORMAT(created_at,"%%Y-%%m-%%d" ) created_at
                 from t_kf_count '''+sql+'''GROUP BY DATE_FORMAT(created_at,"%%Y-%%m-%%d" ),uid_name order by uid_name
            ''')
            kf_name=self.db.query('''
                select uid_name from t_kf_count GROUP BY uid_name order by uid_name
            ''')

            date_time=self.db.query('''
                select DATE_FORMAT(created_at,"%%Y-%%m-%%d" ) date from t_kf_count
                GROUP BY DATE_FORMAT(created_at,"%%Y-%%m-%%d" ) order by created_at desc
            ''')
            datas=[]
            all_incomes=[]
            if all_income:
                for idx,row in enumerate(date_time):
                    all_incomes.append([row.date])
                    for item in kf_name:
                        for idx1,data in enumerate(kf_count):
                            if data.created_at==row.date and data.uid_name==item.uid_name:
                                all_incomes[idx].append(data.all_incomes)
                                break
                            if idx1==kf_count.index(kf_count[-1])  and (data.created_at!=row.date or data.uid_name!=item.uid_name) :
                                all_incomes[idx].append(0)

                pagination=Pagination(page,pre_page,len(all_incomes),self.request)
                startpage=(page-1)*pre_page
                all_incomes=all_incomes[startpage:startpage+pre_page]
            else:
                for idx,row in enumerate(date_time):
                    datas.append([row.date])
                    for item in kf_name:
                        for idx1,data in enumerate(kf_count):
                            if data.created_at==row.date and data.uid_name==item.uid_name:
                                datas[idx].append(data.count)
                                break
                            if idx1==kf_count.index(kf_count[-1])  and (data.created_at!=row.date or data.uid_name!=item.uid_name) :
                                datas[idx].append(0)

                pagination=Pagination(page,pre_page,len(datas),self.request)
                startpage=(page-1)*pre_page
                datas=datas[startpage:startpage+pre_page]
            self.render('project/kf_count.html',
            kf_name=kf_name,
            all_incomes=all_incomes,
            all_income=all_income,
            pagination=pagination,
            datas=datas,
            todo=todo,
            date_time=date_time,
            search_key="")

        elif tag=="gs_count":
            page=int(self.get_argument('page',1))
            pre_page=20

            gs_count=self.db.query('''
                select uid_name,count(*) count,DATE_FORMAT(created_at,"%%Y-%%m-%%d" ) created_at
                 from t_gs_count GROUP BY DATE_FORMAT(created_at,"%%Y-%%m-%%d" ),uid_name order by uid_name
            ''')
            gs_name=self.db.query('''
                select uid_name from t_gs_count GROUP BY uid_name order by uid_name
            ''')

            date_time=self.db.query('''
                select DATE_FORMAT(created_at,"%%Y-%%m-%%d" ) date from t_gs_count
                GROUP BY DATE_FORMAT(created_at,"%%Y-%%m-%%d" ) order by created_at desc
            ''')
            datas=[]
            for idx,row in enumerate(date_time):
                datas.append([row.date])
                for item in gs_name:
                    for idx1,data in enumerate(gs_count):
                        if data.created_at==row.date and data.uid_name==item.uid_name:
                            datas[idx].append(data.count)
                            break
                        if idx1==gs_count.index(gs_count[-1])  and (data.created_at!=row.date or data.uid_name!=item.uid_name) :
                            datas[idx].append(0)

            pagination=Pagination(page,pre_page,len(datas),self.request)
            startpage=(page-1)*pre_page
            datas=datas[startpage:startpage+pre_page]
            self.render(
            'project/gs_count.html',
            gs_name=gs_name,
            pagination=pagination,
            datas=datas,
            date_time=date_time,
            search_key="")

        elif tag=="relation_show":
            id=self.get_argument('id')
            guid=self.get_argument('guid')
            t_project=self.db.get('''
                select * from t_projects where id=%s and guid=%s
            ''',id,guid)
            if not t_project:
                self.write('该项目不存在:',id,guid)
            else:
                t_projects_relation=self.db.get('''
                    select * from t_projects_relation where relation_ids like "%%,'''+str(id)+''',%%" or relation_ids REGEXP  "^'''+str(id)+'''," ''')
                t_relation_projects=[]
                if t_projects_relation:
                    for idx,item in enumerate(t_projects_relation.relation_ids.split(',')[:-1]):
                        t_relation_projects.append([])
                        sql=self.db.get('select concat(guid,"|",id,"|",project_name) guid_id from t_projects where id=%s',item)
                        t_relation_projects[idx].append(sql.guid_id)
                        if t_projects_relation.uid_names:
                            for row in t_projects_relation.uid_names.split(',')[:-1]:
                                if item in row:
                                    row1=row.split('|')
                                    if item ==row1[1]:
                                        row2=row1[0]+'|'+row1[2]
                                    elif item==row1[2]:
                                        row2=row1[0]+'|'+row1[1]
                                    t_relation_projects[idx].append(row2)
            self.render(
                'project/project_relation_other.html',
                 search_key="",
                 t_relation_projects=t_relation_projects,
                 t_projects_relation=t_projects_relation,
                 t_project=t_project
                )

        elif tag=="project_check":
            page=int(self.get_argument('page',1))
            step=self.get_argument('step','')
            project_id=self.get_argument('project_id','')
            company=self.get_argument('company','')
            tel=self.get_argument('tel','')
            project_name=self.get_argument('project_name','')
            pre_page=20
            sql='  left join t_projects_check b on a.id=b.project_id '
            search_sql=''
            sql1=''
            order=' sh_created_at desc,kf_created_at desc'
            params={
                'project_id':project_id,
                'company':company,
                'tel':tel,
                'project_name':project_name
            }
            if step=='1':
                sql=' left join t_projects_check b on a.id=b.project_id and b.sh_created_at is null'
                sql1= ' and a.id not in(select project_id from t_projects_check where project_id=a.id and sh_created_at is not null )'
                order=' kf_created_at asc,a.created_at desc'
            elif step=='2':
                sql='  inner join t_projects_check b on a.id=b.project_id and b.kf_check_status is not null and b.sh_created_at is null '
            elif step=='3':
                sql='  inner join t_projects_check b on a.id=b.project_id and b.sh_created_at is not null'
            if project_id:
                search_sql+=' and a.id=%s '%project_id
            if company:
                search_sql+=' and a.customer_company like "%%'+company+'%%" '
            if tel:
                search_sql+=' and  a.customer_tel=%s '%tel
            if project_name:
                search_sql+=' and  a.project_name like "%%'+project_name+'%%" '
            count=self.db.get('''
                select count(*) count from t_projects a '''+sql+''' where (busniess_from_id_name='内部推荐' or
                 (busniess_from_id_name!='内部推荐' and recommend_staff  in (select name from t_user) ))
            '''+search_sql+sql1)
            pagination=Pagination(page,pre_page,count.count,self.request)
            startpage=(page-1)*pre_page
            t_projects=self.db.query('''
                select a.id p_id,a.project_name,a.recommend_staff,a.created_at,a.customer_company,
                a.customer_name,a.customer_tel,a.guid,
                b.* from t_projects a '''+sql+'''
                 where (a.busniess_from_id_name='内部推荐' or
                 (a.busniess_from_id_name!='内部推荐' and a.recommend_staff  in (select name from t_user))) '''+search_sql+sql1+''' order by '''+order+'''  limit %s,%s
            ''',startpage,pre_page)
            self.render('project/project_check.html',
                search_key="",
                step=step,
                params=params,
                pagination=pagination,
                t_projects=t_projects)


        elif tag=="upload_file":
            page=int(self.get_argument('page',1))
            pre_page=20
            count=self.db.get('''
                select count(*) count from t_upload_file
            ''')
            pagination=Pagination(page,pre_page,count.count,self.request)
            startpage=(page-1)*pre_page
            t_upload_file=self.db.query('''
                select * from t_upload_file order by created_at desc limit %s,%s
            ''',startpage,pre_page)
            self.render(
            'project/upload_file.html',
            search_key="",
            t_upload_file=t_upload_file,
            pagination=pagination
            )

        elif tag=="projects_company_history":
            page=int(self.get_argument('page',1))
            s_project_id=self.get_argument('s_project_id','')
            s_company=self.get_argument('s_company','')
            pre_page=20
            sql=''
            if s_project_id:
                sql= ' where a.id=%s '%s_project_id
            if s_company:
                sql=' where a.customer_company like "%%'+s_company+'%%" '
            params={
                's_project_id':s_project_id,
                's_company':s_company
            }
            count=self.db.get('''
                    select count(*) count from (select count(*) count from t_projects a
                inner join t_projects_company_history b
                on a.id=b.project_id '''+sql+''' group by project_id) bb
            ''')
            pagination=Pagination(page,pre_page,count.count,self.request)
            startpage=(page-1)*pre_page
            t_projects=self.db.query('''
                select a.*,GROUP_CONCAT(concat(b.company)) history_company from t_projects a
                inner join t_projects_company_history b
                on a.id=b.project_id '''+sql+''' group by project_id order by b.created_at desc limit %s,%s
            ''',startpage,pre_page)
            self.render(
            'project/projects_company_history.html',
            search_key="",
            t_projects=t_projects,
            pagination=pagination,
            params=params,
            tag=tag
            )

        elif tag=="express_list":
            todo=self.get_argument('todo','')
            express_manage=self.get_secure_cookie('express_manage')
            step=self.get_argument('step','0')
            page=int(self.get_argument('page',1))
            pre_page=20
            department=self.get_argument('department','')
            start_time=self.get_argument('start_time','')
            end_time=self.get_argument('end_time','')
            source=self.get_argument('source','')
            express_type=self.get_argument('express_type','')
            payment_type=self.get_argument('payment_type','')
            search_key=self.get_argument('search_key','')
            express_number_search=self.get_argument('express_number_search','')
            params={
                "department":department,
                "start_time":start_time,
                "end_time":end_time,
                "source":source,
                "express_type":express_type,
                "payment_type":payment_type,
                'search_key':search_key,
                "express_number_search":express_number_search
            }
            sql=''
            if search_key:
                project_id_sql=''
                if search_key.isdigit():
                    project_id_sql+=' or project_id=%s '%search_key
                sql+=' and (rec_company like "%%'+search_key+'%%" '+project_id_sql+' or rec_name="%s") '%search_key
            
            if department:
                sql+=' and sender_department="%s" '%department
            if start_time and end_time:
                sql+=' and created_send_at between "%s" and "%s" '%(start_time,end_time)
            if source:
                sql+=' and source=%s '%source
            if express_type:
                sql+='  and express_type_id=%s '%express_type
            if payment_type:
                sql+=' and payment_type_id=%s '%payment_type
            if express_number_search:
                sql+=' and express_number like "%%'+express_number_search+'%%" '
            express_type=self.db.query('''
                    select * from t_projects_type where income_category='快递类型'
                ''')
            payment_type=self.db.query('''
                    select * from t_projects_type where income_category='快递付费'
                ''')

            t_projects_type=self.db.query(
                    """
                    select * from t_projects_type where income_category='移交资料' and  jiaojie_order>0 order by jiaojie_order
                    """)
            t_cutomer_addr_msg=self.db.query('''
                    select * from t_customer_addr_msg where uid=%s
                ''',uid)
            addsql=''
            sums_sql=' and send_or_rec=%s '%step
            sums_sql1=' where send_or_rec=%s '%step
            if express_manage!='1' and  '245' not in role_list:
                sums_sql=' and (uid=%s or send_at_uid=%s) '%(uid,uid)+sums_sql
                sums_sql1=sums_sql1+' and (aa.uid=%s or aa.send_at_uid=%s)  '%(uid,uid)
            sums=self.db.get('''
                    select count(*) a,
                    (select count(*) from t_express where accept_at is null '''+sums_sql+''' ) b,
                    (select count(*) from t_express where accept_state=1 and send_at is null '''+sums_sql+''' ) c,
                    (select  count(*) from t_express where accept_state=1 and send_at is not null and confirm_at is null '''+sums_sql+''') d,
                    (select count(*)  from t_express where accept_state=2 and send_at is null '''+sums_sql+''') e,
                       (select  count(*) from t_express where accept_state=1 and send_at is not null and confirm_at is not null '''+sums_sql+''') f
                    from  t_express aa'''+sums_sql1)
            if todo=='1':
                addsql=' and accept_at is null '
            elif todo=='2':
                addsql=' and accept_state=1 and send_at is null '
            elif todo=='3':
                addsql=' and  accept_state=1 and send_at is not null and confirm_at is null '
            elif todo=='4':
                addsql=' and accept_state=2 and send_at is null '
            elif todo=='5':
                addsql=' and  accept_state=1 and send_at is not null and confirm_at is not null '
            if express_manage=='1' or '245' in role_list:
                count=self.db.get('''
                select count(*) count from t_express where send_or_rec=%s'''+addsql+sql,step)
                pagination=Pagination(page,pre_page,count.count,self.request)
                startpage=(page-1)*pre_page
                t_express=self.db.query('''
                select * from t_express  where send_or_rec=%s '''+addsql+sql+''' order by created_at desc LIMIT %s,%s''',step,startpage,pre_page)
            else:
                count=self.db.get('''
                    select count(*) count from t_express where (uid=%s or send_at_uid=%s) and send_or_rec=%s'''+addsql+sql,uid,uid,step)
                pagination=Pagination(page,pre_page,count.count,self.request)
                startpage=(page-1)*pre_page
                t_express=self.db.query('''
                select * from t_express where (uid=%s or send_at_uid=%s) and send_or_rec=%s'''+addsql+sql+
                ''' order by created_at desc limit %s,%s''',uid,uid,step,startpage,pre_page)
            t_user_dep = self.db.query(
                ''' select concat(department_zone,department_name) department_name from t_user where department_name <>''
                 group by concat(department_zone,department_name) '''
            )
            self.render('project/express_list.html',
            search_key="",
            todo=todo,
            sums=sums,
            step=step,
            tag=tag,
            params=params,
            t_user_dep=t_user_dep,
            t_projects_type=t_projects_type,
            pagination=pagination,
            express_type=express_type,
            payment_type=payment_type,
            t_cutomer_addr_msg=t_cutomer_addr_msg,
            t_express=t_express)

        elif tag=="express_output":
            todo=self.get_argument('todo','')
            express_manage=self.get_secure_cookie('express_manage')
            step=self.get_argument('step','0')
            params=self.get_argument('params','')
            params=eval(params)

            sql=''
            addsql=''
            sheet_name=u'全部'
            send_and_rec=''
            source=''
            if params['department']:
                sql+=' and sender_department="%s" '%params['department']
            if params['start_time'] and params['end_time']:
                sql+=' and created_send_at between "%s" and "%s" '%(params['start_time'],params['end_time'])
            if params['source']:
                sql+=' and source=%s '%params['source']
            if params['express_type']:
                sql+='  and express_type_id=%s '%params['express_type']
            if params['payment_type']:
                sql+=' and payment_type_id=%s '%params['payment_type']
            if todo=='1':
                addsql=' and accept_at is null '
                sheet_name=u'待审核'
            elif todo=='2':
                addsql=' and accept_state=1 and send_at is null '
                sheet_name=u'待发件'
            elif todo=='3':
                addsql=' and  accept_state=1 and send_at is not null '
                sheet=u'已发件'
            elif todo=='4':
                addsql=' and accept_state=2 and send_at is null '
                sheet_name=u'驳回件'

            if express_manage=='1':
                t_express=self.db.query('''
                select * from t_express  where send_or_rec=%s '''+addsql+sql,step)
            else:
                t_express=self.db.query('''
                select * from t_express where (uid=%s or send_at_uid=%s) and send_or_rec=%s'''+addsql+sql,uid,uid,step)

            wb=xlwt.Workbook()
            sh=wb.add_sheet(sheet_name)
            sh.write(0,0,u'申请时间')
            sh.write(0,1,u'发件时间')
            sh.write(0,2,u'快递单号')
            sh.write(0,3,u'公司名称')
            sh.write(0,4,u'客户名称')
            sh.write(0,5,u'订单编号')
            sh.write(0,6,u'收件人电话')
            sh.write(0,7,u'资料明细')
            sh.write(0,8,u'其他资料')
            sh.write(0,9,u'快递名称')
            sh.write(0,10,u'付款方式')
            sh.write(0,11,u'寄件人/收件人')
            sh.write(0,12,u'创建人')
            sh.write(0,13,u'来源')
            for idx,row in enumerate(t_express):
                if step=='1':
                    send_and_rec=row.rec_name+'/'+row.send_at_name
                else:
                    send_and_rec=row.send_at_name+'/'+row.rec_name
                if row.source==0:
                    source=u'收入管理系统'
                elif row.source==1:
                    source=u'客户管理系统'
                else:
                    source=u'新建'
                idx=idx+1
                sh.write(idx,0,row.created_at.strftime("%Y-%m-%d %H:%M:%S"))
                if row.created_send_at:
                    sh.write(idx,1,row.created_send_at.strftime("%Y-%m-%d %H:%M:%S"))
                else:
                    sh.write(idx,1,u'')
                sh.write(idx,2,row.express_number)
                sh.write(idx,3,row.rec_company)
                sh.write(idx,4,row.rec_name)
                sh.write(idx,5,row.project_id)
                sh.write(idx,6,row.rec_tel)
                sh.write(idx,7,row.rec_file)
                sh.write(idx,8,row.other_rec_file)
                sh.write(idx,9,row.express_type_id_name)
                sh.write(idx,10,row.payment_type_id_name)

                sh.write(idx,11,send_and_rec)

                sh.write(idx,12,row.uid_name)
                sh.write(idx,13,source)

            wb.save('media/output/快递导出.xls')
            self.write({'output_path':'static/output/快递导出.xls'})

        elif tag=="express_output_cd_banjie":
            params=self.get_argument('params','')
            print(params)
            params=eval(params)

            sql=' and b.confirm_at is not null '
            if params['bj_check']=='1':
                sql+=' and a.confirm_banjie=1 '
            elif params['bj_check']=='0':
                sql+=' and a.confirm_banjie=0 '

            if params['name']:
                sql+=' and a.member_name="%s" '%params['name']
            if params['btype']:
                sql+=' and a.btype_id=%s '%params['btype']
            if params['gs_name']:
                sql+=' and  a.member_name="%s" '%params['gs_name']

            if params['start_time'] and params['end_time']:
                sql+=' and b.confirm_at between "%s" and "%s"  '%(params['start_time'],params['end_time'])

            if params['start_time_fp'] and params['end_time_fp']:
                sql+=' and a.created_at between "%s" and "%s"  '%(params['start_time_fp'],params['end_time_fp'])

            if params['customer_name']:
                sql+=' and c.customer_name="%s" '%params['customer_name']
            if params['btype_name']:
                sql+=' and a.btype_id_name="%s" '%params['btype_name']
            if params['jd_day']:
                sql+=' and datediff( d.confirm_at,a.created_at)=%s '%params['jd_day']
            if role=='9' and '270' not in role_list:
                sql+=' and a.member_name="%s" '%uid_name
            if '270' in role_list:
                sql+=' and (a.btype_id=158 or a.member_name="%s") '%uid_name

            t_projects=self.db.query('''
                    select a.last_state_remark,a.state_msg_counts, a.last_state_msg,a.last_state_msg_at,a.member_name,a.project_id,a.created_at fp , d.confirm_at jd,c.customer_company,a.mid,b.confirm_at,
                    c.customer_name,a.btype_id_name,datediff( d.confirm_at,a.created_at) jd_day,c.guid,datediff(b.confirm_at,b.created_at)
                    bj_day from  t_projects_member a
                    inner join t_projects_milepost b on a.project_id=b.project_id and  a.mid=b.member_id and b.order_int=3
                    inner join t_projects c on a.project_id=c.id
                    inner join t_projects_milepost d on a.project_id=d.project_id and  a.mid=d.member_id and d.order_int=2 and d.confirm_at is not null

                    where a.team_id=38 '''+sql+''' order by b.confirm_at desc
                    ''')


            wb=xlwt.Workbook()
            sh=wb.add_sheet(u'办结列表')
            sh.write(0,0,u'分配时间')
            sh.write(0,1,u'订单号')
            sh.write(0,2,u'公司名称')
            sh.write(0,3,u'客户姓名')
            sh.write(0,4,u'办理项目')
            sh.write(0,5,u'工商专员')
            sh.write(0,6,u'接单日期')
            sh.write(0,7,u'接单时长')
            sh.write(0,8,u'办结日期')
            sh.write(0,9,u'办结时长')
            for idx,item in enumerate(t_projects):
                idx+=1
                sh.write(idx,0,item.fp.strftime('%Y-%m-%d'))
                sh.write(idx,1,item.project_id)
                sh.write(idx,2,item.customer_company)
                sh.write(idx,3,item.customer_name)
                sh.write(idx,4,item.btype_id_name)
                sh.write(idx,5,item.member_name)
                sh.write(idx,6,item.jd.strftime('%Y-%m-%d'))
                sh.write(idx,7,str(item.jd_day)+u'天')
                sh.write(idx,8,item.confirm_at.strftime('%Y-%m-%d'))
                sh.write(idx,9,str(item.bj_day)+u'天')
            wb.save('media/output/办结工商统计(%s).xls'%uid_name)
            self.write({'output_path':'static/output/办结工商统计(%s).xls'%uid_name})

        elif tag=="project_confirm_banjie":
            step=self.get_argument('step','')
            page=int(self.get_argument('page',1))
            pre_page = 20
            project_id=self.get_argument('project_id','')
            project_name=self.get_argument('project_name','')
            customer_company=self.get_argument('customer_company','')
            customer_name=self.get_argument('customer_name','')
            customer_tel=self.get_argument('customer_tel','')
            gendan=self.get_argument('gendan','')
            sale_man=self.get_argument('sale_man','')
            start_time=self.get_argument('start_time','')
            end_time=self.get_argument('end_time','')
            department_id = self.get_argument("department_id",'')
            team_id = self.get_argument("team_id",'')
            sql=''
            if '231' in role_list:
                if step=='1':
                    sql=' and b.confirm_banjie=0 '
                if step=='2':
                    sql=' and b.confirm_banjie=1 '
                if step=='3':
                    sql=' and b.confirm_banjie=2 '
                if project_id:
                    sql+=' and a.id=%s'%project_id
                if project_name:
                    sql+=' and a.project_name  like "%%'+project_name+'%%" '
                if customer_company:
                    sql+=' and a.customer_company like "%%'+customer_company+'%%" '
                if customer_name:
                    sql+=' and a.customer_name="%s" '%customer_name
                if customer_tel:
                    sql+=' and a.customer_tel like "%%'+customer_tel+'%%" '
                if gendan:
                    sql+=' and b.member_name="%s" '%gendan
                if sale_man:
                    sql+=' and c.member_name="%s" '%sale_man
                if start_time and end_time:
                    sql+=' and d.confirm_at between "%s" and "%s" '%(start_time,end_time)
                if department_id:
                    sql+=" and a.project_department_id=%s "%(department_id)
                if team_id :
                    sql+=" and b.team_id=%s "%(team_id)
                # print sql,department_id,type(department_id)
                params={
                    'department_id':department_id,
                    'project_id':project_id,
                    'project_name':project_name,
                    'customer_company':customer_company,
                    'customer_name':customer_name,
                    'customer_tel':customer_tel,
                    'gendan':gendan,
                    'sale_man':sale_man,
                    'start_time':start_time,
                    'end_time':end_time,
                    "team_id":team_id
                }
                count = self.db.get('''  SELECT   count(*) count
                        FROM t_projects
                    a inner join t_projects_member b on a.id=b.project_id
                    inner join t_projects_milepost d on b.project_id=d.project_id and d.confirm_at is not null and d.type_id=151  and b.member_name=d.uid_name
                    and b.btype_id=d.btype_id and b.mid=d.member_id
                    where b.is_cancel=0 and b.btype_id <> 0 and b.btype_id is not null  and  d.confirm_at>='2018-10-01 00:00:00'
                '''+sql)
                pagination = Pagination(page, pre_page, count.count, self.request)
                startpage = (page - 1) * pre_page

                t_projects = self.db.query(
                    '''
                    SELECT  a.* ,b.mid,b.member_name,b.btype_id_name,b.banjie_remark,b.team_name,
                    b.last_milepost_id_name,b.last_milepost_id_at,b.created_at cq_created_at,b.confirm_banjie,b.guid m_guid,b.member_name sale_man,d.confirm_at
                        FROM t_projects
                    a inner join t_projects_member b on a.id=b.project_id
                    inner join t_projects_milepost d on b.project_id=d.project_id and d.confirm_at is not null and d.type_id=151 and b.member_name=d.uid_name
                    and b.btype_id=d.btype_id and b.mid=d.member_id
                    where b.is_cancel=0 and b.btype_id <> 0  and b.btype_id is not null   and d.confirm_at>='2018-10-01 00:00:00' '''+sql+'''
                                    order by b.created_at desc limit %s,%s
                    ''', startpage, pre_page)
                t_projects_export = self.db.query(
                    '''
                    SELECT  a.* ,b.mid,b.member_name,b.btype_id_name,b.banjie_remark,
                    b.last_milepost_id_name,b.last_milepost_id_at,b.created_at cq_created_at,b.confirm_banjie,b.guid m_guid,c.member_name sale_man,d.confirm_at
                        FROM t_projects
                    a inner join t_projects_member b on a.id=b.project_id
                    inner join t_projects_member c on a.id=c.project_id and c.team_name='销售顾问'
                    inner join t_projects_milepost d on b.project_id=d.project_id and d.confirm_at is not null and d.type_id=151 and b.member_name=d.uid_name
                    and b.btype_id=d.btype_id and b.mid=d.member_id
                    where   b.is_cancel=0 and b.btype_id <> 0 and d.confirm_at>='2018-10-01 00:00:00' '''+sql+'''
                                    order by b.created_at desc''')
                if project_id or project_name or customer_company or customer_name or customer_tel or gendan or sale_man or(start_time and end_time):
                    wb=xlwt.Workbook()
                    sheet_name=u'办结确认表'
                    if step=='1':
                        sheet_name=u'待确认表'
                    elif step=='2':
                        sheet_name=u'已确认表'
                    elif step=='3':
                        sheet_name=u'异常带确认'
                    sh=wb.add_sheet(sheet_name)
                    sh.write(0,0,u'编号')
                    sh.write(0,1,u'业务内容')
                    sh.write(0,2,u'公司名称')
                    sh.write(0,3,u'客户名称')
                    sh.write(0,4,u'客户电话')
                    sh.write(0,5,u'跟单专员')
                    sh.write(0,6,u'销售顾问')
                    sh.write(0,7,u'合同金额')
                    sh.write(0,8,u'办结时间')
                    sh.write(0,9,u'创建人')
                    sh.write(0,10,u'创建时间')
                    sh.write(0,11,u'状态')
                    for idx,row in enumerate(t_projects_export):
                        idx=idx+1
                        sh.write(idx,0,row.id)
                        sh.write(idx,1,row.project_name)
                        sh.write(idx,2,row.customer_company)
                        sh.write(idx,3,row.customer_name)
                        sh.write(idx,4,row.customer_tel)
                        sh.write(idx,5,row.member_name)
                        sh.write(idx,6,row.sale_man)
                        sh.write(idx,7,row.all_income)
                        sh.write(idx,8,row.confirm_at.strftime("%Y-%m-%d %H:%M:%S"))
                        sh.write(idx,9,row.uid_name)
                        sh.write(idx,10,row.created_at.strftime("%Y-%m-%d"))
                        if row.confirm_banjie==0:
                            sh.write(idx,11,u'未审核')
                        elif row.confirm_banjie==1:
                            sh.write(idx,11,u'已确认')
                        elif row.confirm_banjie=='2':
                            sh.write(idx,11,'异常待确认 备注：'+row.banjie_remark)
                    wb.save('media/output/办结确认数据导出.xls')


            else:
                if step=='1':
                    sql=' and b.confirm_banjie=0 '
                if step=='2':
                    sql=' and b.confirm_banjie=1 '
                if step=='3':
                    sql=' and b.confirm_banjie=2 '
                if project_id:
                    sql+=' and a.id=%s'%project_id
                if project_name:
                    sql+=' and a.project_name  like "%%'+project_name+'%%" '
                if customer_company:
                    sql+=' and a.customer_company like "%%'+customer_company+'%%" '
                if customer_name:
                    sql+=' and a.customer_name="%s" '%customer_name
                if customer_tel:
                    sql+=' and a.customer_tel like "%%'+customer_tel+'%%" '
                if gendan:
                    sql+=' and b.member_name="%s" '%gendan
                if sale_man:
                    sql+=' and c.member_name="%s" '%sale_man
                if start_time and end_time:
                    sql+=' and d.confirm_at between "%s" and "%s" '%(start_time,end_time)
                if department_id:
                    sql+=" and a.project_department_id=%s "%(department_id)
                if team_id :
                    sql+=" and b.team_id=%s "%(team_id)                    
                params={
                    'project_id':project_id,
                    'project_name':project_name,
                    'customer_company':customer_company,
                    'customer_name':customer_name,
                    'customer_tel':customer_tel,
                    'gendan':gendan,
                    'sale_man':sale_man,
                    'start_time':start_time,
                    'end_time':end_time,
                    "department_id":department_id,
                    "team_id":team_id
                }
                count = self.db.get('''  SELECT   count(*) count
                        FROM t_projects
                    a inner join t_projects_member b on a.id=b.project_id
                    inner join t_projects_milepost d on b.project_id=d.project_id and d.confirm_at is not null and d.type_id=151  and b.member_name=d.uid_name
                    and b.btype_id=d.btype_id and b.mid=d.member_id
                    where  b.btype_id <> 0  and b.is_cancel=0 and  d.confirm_at>='2018-10-01 00:00:00' and b.member_name=%s
                '''+sql,uid_name)
                pagination = Pagination(page, pre_page, count.count, self.request)
                startpage = (page - 1) * pre_page

                t_projects = self.db.query(
                    '''
                    SELECT  a.* ,b.mid,b.member_name,b.btype_id_name,b.banjie_remark,b.team_name,
                    b.last_milepost_id_name,b.last_milepost_id_at,b.created_at cq_created_at,b.confirm_banjie,b.guid m_guid,b.member_name sale_man,d.confirm_at
                        FROM t_projects
                    a inner join t_projects_member b on a.id=b.project_id
                    inner join t_projects_milepost d on b.project_id=d.project_id and d.confirm_at is not null and d.type_id=151 and b.member_name=d.uid_name
                    and b.btype_id=d.btype_id and b.mid=d.member_id
                    where  b.btype_id <> 0    and b.is_cancel=0  and d.confirm_at>='2018-10-01 00:00:00' and b.member_name=%s '''+sql+'''
                                    order by b.created_at desc limit %s,%s
                    ''',uid_name, startpage, pre_page)
            self.render('project/project_confirm_banjie.html',
                output_path="static/output/办结确认数据导出.xls",
                search_key="",
                step=step,
                tag=tag,
                pagination=pagination,
                t_projects=t_projects,
                params=params)

        elif tag=="income_history_list":
            page=int(self.get_argument('page',1))
            pre_page = 20
            count=self.db.get('''
             select count(*) count from t_project_chuna_history
            ''')
            pagination = Pagination(page, pre_page, count.count, self.request)
            startpage = (page - 1) * pre_page

            t_project_chuna_history=self.db.query('''
             select * from t_project_chuna_history  order by updated_at desc limit %s,%s
            ''',startpage,pre_page)
            self.render('project/income_history_list.html',
            search_key="",
            tag=tag,
            t_project_chuna_history=t_project_chuna_history,
            pagination=pagination
            )

        elif tag=="manage_chengjiao":
            page=int(self.get_argument('page',1))
            pre_page = 20
            count=self.db.get('''
                select count(*) count from t_projects_note_chengjiao
            ''')
            pagination = Pagination(page, pre_page, count.count, self.request)
            startpage = (page - 1) * pre_page
            projects_note_chengjiao=self.db.query('''
                select * from t_projects_note_chengjiao order by created_at desc
            ''')

            self.render('project/manage_chengjiao.html',
                search_key="",
                tag=tag,
                projects_note_chengjiao=projects_note_chengjiao,
                pagination=pagination
                )
        elif tag=="cq_bj_list":
            name=self.get_argument('name','')
            type_id=self.get_argument('type_id','')
            bj_check=self.get_argument('bj_check','0')
            confirm_at=self.get_argument('confirm_at','')
            page=int(self.get_argument('page','1'))
            way=self.get_argument('way','')
            pre_page=10
            sql=''
            a_add='#dingdanliuzhuan'
            params={
                'name':name,
                'type_id':type_id,
                'bj_check':bj_check,
                'confirm_at':confirm_at,
                'way':way
            }
            way_sql=" '%%Y-%%m-%%d' "
            if way=='month':
                way_sql=" '%%Y-%%m' "
            elif way=='week':
                way_sql=" '%%Y-%%m-%%u' "
            if name:
                sql+=' and a.member_name="%s" '%name
            if type_id:
                sql+=' and a.btype_id=%s '%type_id
            if confirm_at:
                sql+=' and date_format(b.confirm_at,'+way_sql+')="{}"'.format(confirm_at)
            count=self.db.get('''
            select count(*) count  from  t_projects_member a
                inner join t_projects_milepost b on a.project_id=b.project_id and  a.mid=b.member_id and b.order_int=3
                inner join t_projects c on a.project_id=c.id
                inner join t_projects_milepost d on a.project_id=d.project_id and  a.mid=d.member_id and d.order_int=2 and d.confirm_at is not null
                where a.team_id=38   and  a.confirm_banjie=1 '''+sql+'''
            ''')
            pagination = Pagination(page, pre_page, count.count, self.request)
            start_page = (page - 1) * pre_page
            t_projects=self.db.query('''
            select c.customer_company,c.id,c.guid  from  t_projects_member a
                inner join t_projects_milepost b on a.project_id=b.project_id and  a.mid=b.member_id and b.order_int=3
                inner join t_projects c on a.project_id=c.id
                inner join t_projects_milepost d on a.project_id=d.project_id and  a.mid=d.member_id and d.order_int=2 and d.confirm_at is not null
                where a.team_id=38 and b.confirm_at is not null   and  a.confirm_banjie=1 '''+sql+''' order by  b.confirm_at desc limit %s,%s
            ''',start_page,pre_page)
            return self.render('project/cq_bj_list.html',
                t_projects=t_projects,
                pagination=pagination,
                params=params,
                a_add=a_add)

        elif tag=="cq_jd_list":
            page=int(self.get_argument('page',1))
            pre_page = 20
            show_tag=self.get_argument('show_tag','1')
            gs_name=self.get_argument('gs_name','')
            start_time=self.get_argument('start_time','')
            end_time=self.get_argument('end_time','')
            start_time_fp=self.get_argument('start_time_fp','')
            end_time_fp=self.get_argument('end_time_fp','')
            customer_name=self.get_argument('customer_name','')
            btype_name=self.get_argument('btype_name','')
            jd_day=self.get_argument('jd_day','')
            way=self.get_argument('way','')
            name=self.get_argument('name','')
            count_type=self.get_argument('count_type','')
            btype=self.get_argument('btype','')
            bj_check=self.get_argument('bj_check','1')
            work_sql=''
            work_sel_sql=''
            params={
                'gs_name':gs_name,
                'show_tag':show_tag,
                'start_time':start_time,
                'end_time':end_time,
                'customer_name':customer_name,
                'btype_name':btype_name,
                'jd_day':jd_day,
                'way':way,
                'name':name,
                'count_type':count_type,
                'btype':btype,
                'bj_check':bj_check,
                'start_time_fp':start_time_fp,
                'end_time_fp':end_time_fp
            }
            sql=''
            sql1=''
            order_int=' d.confirm_at '
            way_sql=" '%%Y-%%m-%%d' "
            if count_type=='project_name':
                gb_sql=' a.member_name '
                gb_sql1=' b.uid_name '
            elif count_type=='gs':
                gb_sql=' a.btype_id '
                gb_sql1=' b.p_type_id '
            if way=='month':
                way_sql=" '%%Y-%%m' "
            elif way=='week':
                way_sql=" '%%Y-%%m-%%u' "
            if show_tag=="2":
                sql=' and b.confirm_at is not null '
                if bj_check=='1':
                    sql+=' and a.confirm_banjie=1 '
                elif bj_check=='0':
                    sql+=' and a.confirm_banjie=0 '
                order_int=' b.confirm_at '
            elif show_tag=="3":
                if not way:
                    sql=' and a.last_state_msg_at is not null '
                order_int=' a.last_state_msg_at '
                work_sel_sql=' e.count,'
                work_sql='''
                left join (select count(*) count,created_at,project_id,p_type_id,uid from t_projects_state_msg group by date_format(created_at,"%%Y-%%m-%%d"),project_id,p_type_id,uid)
                e on date_format(e.created_at,"%%Y-%%m-%%d")=date_format(a.last_state_msg_at,"%%Y-%%m-%%d")
                    and e.uid=a.member_id and e.project_id=a.project_id and e.p_type_id=a.btype_id
                 '''

            if name:
                sql+=' and a.member_name="%s" '%name
            if btype:
                sql+=' and a.btype_id=%s '%btype
            if gs_name:
                sql+=' and  a.member_name="%s" '%gs_name
                sql1+=' and member_name="%s" '%gs_name

            if start_time and end_time:
                if show_tag=='2':
                    sql+=' and b.confirm_at between "%s" and "%s"  '%(start_time,end_time)
                else:
                    sql+=' and d.confirm_at between "%s" and "%s"  '%(start_time,end_time)
                    sql1+=' and jd between "%s" and "%s" '%(start_time,end_time)
            if start_time_fp and end_time_fp:
                sql+=' and a.created_at between "%s" and "%s"  '%(start_time_fp,end_time_fp)

            if customer_name:
                sql+=' and c.customer_name="%s" '%customer_name
                sql1+=' and customer_name="%s" '%customer_name
            if btype_name:
                sql+=' and a.btype_id_name="%s" '%btype_name
                sql1+=' and btype_id_name="%s" '%btype_name
            if jd_day:
                sql+=' and datediff( d.confirm_at,a.created_at)=%s '%jd_day
                sql1+=' and jd_day=%s '%jd_day
            if role=='9' and '270' not in role_list:
                sql+=' and a.member_name="%s" '%uid_name
                sql1+=' and member_name="%s" '%uid_name
            if '270' in role_list:
                sql+=' and (a.btype_id=158 or a.member_name="%s") '%uid_name
                sql1+=' and (btype_id=158 or  member_name="%s") '%uid_name
            if way:
                if show_tag=='4':
                    count=self.db.get('''
                    SELECT count(*) count,sum(sc) ssc,
                    (select group_concat(gb,'|',count)
                    from (SELECT  '''+gb_sql+'''gb,count(*) count from t_projects_genjin_record a
                    where a.mid is not null '''+sql+'''
                    group by gb)aaa  )every_count
                    from (select group_concat(gb,'|',count) gc,df_confirm_at,sum(count) sc from(
                    SELECT  '''+gb_sql+'''gb,date_format(created_at,'''+way_sql+''') df_confirm_at,count(*) count from t_projects_genjin_record a
                    where a.mid is not null '''+sql+'''
                    group by gb,df_confirm_at)aa group by df_confirm_at)aa
                    ''')
                    pagination = Pagination(page, pre_page, count.count, self.request)
                    startpage = (page - 1) * pre_page
                    t_projects=self.db.query('''
                    select group_concat(gb,'|',count) gc,df_confirm_at,sum(count) sc from(
                    SELECT  '''+gb_sql+'''gb,date_format(created_at,'''+way_sql+''') df_confirm_at,count(*) count from t_projects_genjin_record a
                    where a.mid is not null '''+sql+'''
                    group by gb,df_confirm_at)aa group by df_confirm_at
                    order by df_confirm_at desc LIMIT %s,%s
                    ''',startpage,pre_page)
                elif show_tag=='3':
                    count=self.db.get('''
                        select count(*) count,sum(sc) ssc,
                        (
                            select  group_concat(gb,'|',count) from(
                              SELECT
                            '''+gb_sql1+''' gb,count(*) count
                            FROM t_projects_state_msg b
                            inner join t_projects_member a on a.project_id=b.project_id and b.uid=a.member_id and b.p_type_id=a.btype_id
                            inner join t_projects c on a.project_id=c.id
                            inner join t_projects_milepost d on a.project_id=d.project_id and  a.mid=d.member_id and d.order_int=2 and d.confirm_at is not null
                            where  a.team_id=38 '''+sql+''' group by gb order by count desc)aa
                         )every_count
                        from(
                        select  group_concat(gb,'|',count),df_confirm_at,sum(count) sc from (
                        SELECT
                        date_format(b.created_at,'''+way_sql+''') df_confirm_at,'''+gb_sql1+''' gb,count(*) count
                            FROM t_projects_state_msg b
                            inner join t_projects_member a on a.project_id=b.project_id and b.uid=a.member_id and b.p_type_id=a.btype_id
                            inner join t_projects c on a.project_id=c.id
                            inner join t_projects_milepost d on a.project_id=d.project_id and  a.mid=d.member_id and d.order_int=2 and d.confirm_at is not null
                            where  a.team_id=38 '''+sql+''' group by gb,df_confirm_at)aa group by df_confirm_at
                        )aaa
                    ''')
                    pagination = Pagination(page, pre_page, count.count, self.request)
                    startpage = (page - 1) * pre_page
                    t_projects=self.db.query('''
                     select  group_concat(gb,'|',count) gc,df_confirm_at,sum(count) sc from (
                    SELECT
                    date_format(b.created_at,'''+way_sql+''') df_confirm_at,'''+gb_sql1+''' gb,count(*) count
                            FROM t_projects_state_msg b
                            inner join t_projects_member a on a.project_id=b.project_id and b.uid=a.member_id and b.p_type_id=a.btype_id
                            inner join t_projects c on a.project_id=c.id
                            inner join t_projects_milepost d on a.project_id=d.project_id and  a.mid=d.member_id and d.order_int=2 and d.confirm_at is not null
                            where  a.team_id=38 '''+sql+''' group by gb,df_confirm_at)aa group by df_confirm_at order by df_confirm_at desc limit %s,%s
                    ''',startpage,pre_page)
                else:
                    print('''
                    select group_concat(gb,'|',count)
                            from (select '''+gb_sql+''' gb,count(*) count from  t_projects_member a
                inner join t_projects_milepost b on a.project_id=b.project_id and  a.mid=b.member_id and b.order_int=3
                inner join t_projects c on a.project_id=c.id
                inner join t_projects_milepost d on a.project_id=d.project_id and  a.mid=d.member_id and d.order_int=2 and d.confirm_at is not null
                where a.team_id=38 '''+sql+''' group by gb order by count desc)bbb
                    ''')
                    count=self.db.get('''
                        select count(*) count,sum(sc) ssc,
                        (select group_concat(gb,'|',count)
                            from (select '''+gb_sql+''' gb,count(*) count from  t_projects_member a
                inner join t_projects_milepost b on a.project_id=b.project_id and  a.mid=b.member_id and b.order_int=3
                inner join t_projects c on a.project_id=c.id
                inner join t_projects_milepost d on a.project_id=d.project_id and  a.mid=d.member_id and d.order_int=2 and d.confirm_at is not null
                where a.team_id=38 '''+sql+''' group by gb order by count desc)bbb
                        )every_count
                        from (
                        select group_concat(gb,'|',count),df_confirm_at,sum(count) sc from (
                    select '''+gb_sql+''' gb,date_format('''+order_int+''','''+way_sql+''') df_confirm_at,count(*) count from  t_projects_member a
                inner join t_projects_milepost b on a.project_id=b.project_id and  a.mid=b.member_id and b.order_int=3
                inner join t_projects c on a.project_id=c.id
                inner join t_projects_milepost d on a.project_id=d.project_id and  a.mid=d.member_id and d.order_int=2 and d.confirm_at is not null
                where a.team_id=38 '''+sql+''' group by df_confirm_at,gb)aa group by df_confirm_at
                        )bb
                    ''')
                    pagination = Pagination(page, pre_page, count.count, self.request)
                    startpage = (page - 1) * pre_page
      
                    t_projects=self.db.query('''
                    select group_concat(gb,'|',count) gc,df_confirm_at,sum(count) sc from (
                    select '''+gb_sql+''' gb,date_format('''+order_int+''','''+way_sql+''') df_confirm_at,count(*) count from  t_projects_member a
                inner join t_projects_milepost b on a.project_id=b.project_id and  a.mid=b.member_id and b.order_int=3
                inner join t_projects c on a.project_id=c.id
                inner join t_projects_milepost d on a.project_id=d.project_id and  a.mid=d.member_id and d.order_int=2 and d.confirm_at is not null
                where a.team_id=38 '''+sql+''' group by df_confirm_at,gb)aa group by df_confirm_at order by  df_confirm_at desc limit %s,%s
                    ''',startpage,pre_page)
            else:
                if show_tag=='4':
                    count=self.db.get('''
                   SELECT count(*) count from t_projects_genjin_record
                     where mid is not null '''+sql1+'''
                    ''')
                    pagination = Pagination(page, pre_page, count.count, self.request)
                    startpage = (page - 1) * pre_page
                    t_projects=self.db.query('''
                    SELECT * from t_projects_genjin_record
                    where mid is not null '''+sql1+'''
                    order by created_at desc LIMIT %s,%s
                    ''',startpage,pre_page)
                else:
                    count=self.db.get('''
                        select count(*) count  from  t_projects_member a
                        inner join t_projects_milepost b on a.project_id=b.project_id and  a.mid=b.member_id and order_int=3
                        inner join t_projects c on a.project_id=c.id
                        inner join t_projects_milepost d on a.project_id=d.project_id and  a.mid=d.member_id and d.order_int=2 and d.confirm_at is not null
                        where a.team_id=38
                        '''+sql)
                    pagination = Pagination(page, pre_page, count.count, self.request)
                    startpage = (page - 1) * pre_page
                    t_projects=self.db.query('''
                    select  '''+work_sel_sql+''' a.last_state_remark,a.state_msg_counts, a.last_state_msg,a.last_state_msg_at,a.member_name,a.project_id,a.created_at fp , d.confirm_at jd,c.customer_company,a.mid,b.confirm_at,
                    c.customer_name,a.btype_id_name,datediff( d.confirm_at,a.created_at) jd_day,c.guid,datediff(b.confirm_at,b.created_at)
                    bj_day from  t_projects_member a
                    inner join t_projects_milepost b on a.project_id=b.project_id and  a.mid=b.member_id and b.order_int=3
                    inner join t_projects c on a.project_id=c.id
                    inner join t_projects_milepost d on a.project_id=d.project_id and  a.mid=d.member_id and d.order_int=2 and d.confirm_at is not null
                    '''+work_sql+'''
                    where a.team_id=38 '''+sql+''' order by '''+order_int+''' desc limit %s,%s
                    ''',startpage,pre_page)
            member_gs=self.db.query('''
                select member_name uid_name,member_id from t_projects_member
                 where team_id=38 and last_milepost_id is not null and last_milepost_id <> 0  group by member_name
            ''')
            t_projects_type=self.db.query('''
                select id,income_name from t_projects_type where income_category='业务分类'
            ''')
            self.render('project/cq_jd_list.html',
                search_key="",
                tag=tag,
                count=count,
                show_tag=show_tag,
                params=params,
                t_projects_type=t_projects_type,
                t_projects=t_projects,
                member_gs=member_gs,
                pagination=pagination)

        elif tag=="project_liuzhuan_reject":
            page=int(self.get_argument('page',1))
            pre_page = 20
            count=self.db.get('''
                select count(*) count from t_projects a inner join
                t_projects_transfile b on a.id=b.project_id and b.is_ok=1 and mtype=1 and fback_remark is not null
                inner join t_projects_milepost c on a.id=c.project_id and order_int=4 and confirm_at is null and b.pm_id=c.member_id
                where c.uid_name=%s and b.cq_uid_at is null
            ''',uid_name)
            pagination = Pagination(page, pre_page, count.count, self.request)
            startpage = (page - 1) * pre_page
            t_projects=self.db.query('''
            select a.*,c.btype_name,c.uid_name gs_name,b.fback_remark from t_projects a inner join
                t_projects_transfile b on a.id=b.project_id and b.is_ok=1 and mtype=1 and fback_remark is not null
                inner join t_projects_milepost c on a.id=c.project_id and order_int=4 and confirm_at is null and b.pm_id=c.member_id
                where c.uid_name=%s and b.cq_uid_at is null limit %s,%s
            ''',uid_name,startpage,pre_page)
            self.render('project/project_liuzhuan_reject.html',
                search_key="",
                tag=tag,
                t_projects=t_projects,
                pagination=pagination
                )

        elif tag=='cb_addr_manage':
            step=self.get_argument('step','2')
            show_tag=self.get_argument('show_tag','cg')
            page=int(self.get_argument('page',1))
            pre_page = 20
            sql=''
            # if role=='15':
            #     sql=' and uid=%s '%uid
            if show_tag=='cg':
                if step=='2':
                    sql=' and chuna_check_date is null and supply_js_date is null and caiwu_js_date is null '
                elif step=='3':
                    sql=' and chuna_check_date is not null and supply_js_date is null and caiwu_js_date is null and purchaser_caiwu_confirm is null '
                elif step=='4':
                    sql=' and chuna_check_date is not null and supply_js_date is null and caiwu_js_date is null and purchaser_caiwu_confirm is not null and fq_date is null '
                elif step=='5':
                    sql=' and purchaser_qk<>0 '
            elif show_tag=='gy':
                if step=='1':
                    sql=' and chuna_check_date is not null and supply_js_date is null and caiwu_js_date is null and purchaser_caiwu_confirm is not null and fq_date is not null '
                elif step=='2':
                    sql=' and supply_js_date is not null and caiwu_js_date is null and purchaser_caiwu_confirm is not null and fq_date is not null  '
                elif step=='3':
                    sql=' and supply_js_date is not null and caiwu_js_date is not null and purchaser_caiwu_confirm is not null and fq_date is not null and supply_caiwu_confirm is null '
                elif step=='4':
                    sql=' and supply_js_date is not null and caiwu_js_date is not null and purchaser_caiwu_confirm is not null and fq_date is not null and supply_caiwu_confirm is not null '
                elif step=='5':
                    sql=' and supply_qk<>0 '
            count=self.db.get(''' select count(*) count from  t_cb_addr_manage where 0=0 '''+sql)
            pagination=Pagination(page,pre_page,count.count,self.request)
            startpage = (page - 1) * pre_page
            t_cb_addr_manage=self.db.query('''
            select * from t_cb_addr_manage where 0=0
            '''+sql+''' order by created_at desc limit %s,%s ''',startpage,pre_page)
            self.render('project/cb_addr_manage.html',
              search_key="",
              t_cb_addr_manage=t_cb_addr_manage,
              pagination=pagination,
              step=step,
              show_tag=show_tag,
              tag=tag)
        
        elif tag=="logoff_list":
            df=self.get_argument('df','')
            name=self.get_argument('name','')
            type_id=self.get_argument('type_id','')
            member_id=self.get_argument('member_id','')
            start=self.get_argument('start','')
            end=self.get_argument('end','')
            count_type=self.get_argument('count_type','')
            page=int(self.get_argument('page','1'))
            count_way=self.get_argument('count_way','')
            pre_page=10
            a_add='#dingdanliuzhuan'
            params={
                'df':df,
                'name':name,
                'type_id':type_id,
                'member_id':member_id,
                'start':start,
                'end':end,
                'count_type':count_type,
                'count_way':count_way
            }
            state_id_sql=''
            if count_type=='day':
                way_sql=" '%%Y-%%m-%%d' "
            elif count_type=='month':
                way_sql=" '%%Y-%%m' "
            elif count_type=='week':
                way_sql=" '%%Y-%%m-%%u' "
            if df:
                state_id_sql+=' and date_format(finish_at,'+way_sql+')="%s" '%df
            if start and end :
                state_id_sql += " and finish_at between '%s' and '%s' "%(start,end)
            if member_id:
                state_id_sql += " and a.uid=%s "%(member_id)
            if name:
                if count_way=='gs':
                    state_id_sql+=' and a.type_id_name="%s" '%name
                else:
                    state_id_sql+=" and a.uid_name='%s' "%name
        
            if type_id:
                state_id_sql+=' and type_id=%s '%type_id
            count=self.db.get('''
            select  count(*) count
            from t_projects_logoff a
            inner  join  t_projects_member  b on a.mid=b.mid
            inner join t_projects c on c.id = a.project_id  where state_id=2
            '''+state_id_sql)
            pagination=Pagination(page,pre_page,count.count,self.request)
            startpage=(page-1)*pre_page
            t_projects=self.db.query('''
            select  c.id,c.guid,c.customer_company
            from t_projects_logoff a
            inner  join  t_projects_member  b on a.mid=b.mid
            inner join t_projects c on c.id = a.project_id  where state_id=2 
            '''+state_id_sql+''' limit %s,%s ''',startpage,pre_page)
            return self.render('project/cq_bj_list.html',
                t_projects=t_projects,
                pagination=pagination,
                a_add=a_add,
                params=params)

        elif tag=="project_reject":
            sql=''
            my=self.get_argument('my','')
            page=int(self.get_argument('page','1'))
            step=self.get_argument('step','1')
            project_id=self.get_argument('project_id','')
            pre_page=10
            params={
                'step':step,
                'my':my,
                'project_id':project_id
            }
            if role not in ['2','3','5','8']:
                sql+=' and (handler_uid=%s or uid=%s ) '%(uid,uid)
            elif my:
                sql+=' and (handler_uid=%s or uid=%s ) '%(uid,uid)
            if step=='1':
                sql+=' and handler_at is null and confirm_at is null '
            elif step=='2':
                sql+=' and handler_at is not null and confirm_at is null '
            elif step=='3':
                sql+=' and handler_at is not null and confirm_at is not null and confirm_status=1 '
            elif step=='4':
                sql+='  and handler_at is not null and confirm_at is not null and confirm_status=2 '
            if project_id:
                sql+=' and project_id=%s '%project_id
            count=self.db.get(' select count(*) count from t_projects_information_reject  where 0=0 '+sql)
            pagination=Pagination(page,pre_page,count.count,self.request)
            startpage=(page-1)*pre_page
            datas=self.db.query(''' select * from t_projects_information_reject where 0=0 '''+sql+''' limit %s,%s''',startpage,pre_page)
            self.render('project/project_reject.html',
                datas=datas,
                pagination=pagination,
                search_key='',
                params=params,
                tag=tag)
    @tornado.web.authenticated
    def post(self):
        tag = self.get_argument("tag")
        uid_name = self.get_secure_cookie("name")
        role = self.get_secure_cookie("role")
        uid = self.get_secure_cookie("uid")
        dt=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        if tag=="add_income_detail":

            body = self.get_argument("body")
            data = json.loads(body)
            project_id = self.get_argument("project_id")
            income_id = self.get_argument("income_id")
            income_name = self.get_argument("income_name")
            parent_id = self.get_argument("parent_id",0)
            company_id = self.get_argument("company_id")
            company_id_name = self.get_argument("company_id_name")
            pay_type_name = self.get_argument("pay_type_name")
            pay_type_id = self.get_argument("pay_type_id")
            income_at = self.get_argument('income_at')
            income_num = self.get_argument("income_num")
            income_amount = self.get_argument("income_amount")

            income_remark = self.get_argument("income_remark","")
            result = 0
            if not income_id:
                return self.write("not income_id")
            elif not project_id:
                return self.write("not project_id")
            else:
                if int(parent_id) > 0:
                    title_id_result = self.db.execute("""
                        update t_projects_income_title set income_at=%s,
                            updated_at=%s,uid=%s,uid_name=%s,
                            pay_type_name=%s,pay_type_id=%s,company_id=%s,company_id_name=%s
                            where id=%s
                        """,income_at,dt, uid, uid_name, pay_type_name, pay_type_id,
                                            company_id, company_id_name,
                                            parent_id)

                    income_row = self.db.get(
                                    "select * from t_projects_income where income_id=%s and income_num=%s and parent_id=%s and project_id=%s",
                                    income_id, income_num,
                                    parent_id, project_id)


                    for item in data:
                        if item:
                            income_row = self.db.get(
                                "select * from t_projects_income where income_id=%s and income_num=%s and parent_id=%s and project_id=%s",
                               income_id,income_num,
                                parent_id, project_id)
                            if income_row:
                                return_income_id = self.db.execute(
                                    """update  t_projects_income_detail set income_money=%s where
                                        income_id=%s and income_num=%s and parent_id=%s and project_id=%s
                                        """, item["income_money"],
                                   income_id,income_num,
                                    parent_id, project_id)
                            else:
                                result = self.db.execute("""
                                    insert into t_projects_income_detail(income_id,income_name,project_id,service_id,
                                    service_name,service_money,created_at,uid_name,uid
                                    )
                                    values(%s,%s,%s,%s,%s,%s,%s,%s)
                                """, income_id, income_name, project_id,
                                                        service_id, service_name,
                                                        service_money, dt,
                                                        uid_name, uid)
                else:
                    # new !!!!!

                    title_id = self.db.execute("""
                            insert into t_projects_income_title (income_at,project_id,income_title,total,
                            created_at,updated_at,uid,uid_name,guid,pay_type_name,pay_type_id,company_id,company_id_name)
                            values(%s,%s,%s,0,%s,%s,%s,%s,uuid(),%s,%s,%s,%s)
                        """, income_at, project_id, "", dt, dt, uid, uid_name,
                                               pay_type_name, pay_type_id,
                                               company_id, company_id_name)

                    if title_id > 0:
                        income_row = self.db.get(
                            "select * from t_projects_income where income_id=%s and income_num=%s and parent_id=%s and project_id=%s",
                           income_id, income_num, title_id,project_id)
                        if income_row:
                            return_income_id = self.db.execute(
                                """update  t_projects_income set income_money=%s , income_remark=%s where
                                        income_id=%s and income_num=%s and parent_id=%s and project_id=%s
                                    """, income_amount,income_remark,
                                income_id,income_num,
                                title_id, project_id)
                        else:
                            guid = uuid.uuid4()
                            return_income_id = self.db.execute(
                                """insert into t_projects_income(project_id,
                                    income_name,income_money,uid,uid_name,guid,
                                    created_at,updated_at,remark,income_id,parent_id,income_num)
                                    values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
                                    """, project_id, income_name,
                                income_amount, uid, uid_name, guid, dt, dt,
                                income_remark, income_id, title_id, income_num)



                        for item in data:
                            if item:

                                guid = uuid.uuid4()
                                result = self.db.execute(
                                    """
                                        insert into t_projects_income_detail(income_id,income_name,project_id,service_id,
                                        service_name,service_money,created_at,updated_at,uid_name,uid,title_id
                                        )
                                        values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
                                    """, income_id, income_name, project_id,
                                    item["service_id"], item["service_name"],
                                    item["service_money"], dt, dt, uid_name,
                                    uid, title_id)


                self.write(body)

        elif tag=="cancel_memeber_task":
            project_id = self.get_argument("project_id")
            mid = self.get_argument("mid")
            atype= self.get_argument("atype")
            customer_id=self.get_argument('customer_id','0')
            if not mid:
                self.write("not mid")
            elif not project_id:
                self.write("mid")
            else:
                event_msg = ""
                if atype=="zhuangyuan":
                    result = self.db.execute("""
                        update t_projects_member set is_cancel=1 ,is_cancel_at=%s,is_cancel_uid=%s,is_cancel_uid_name=%s where project_id=%s and mid=%s
                    """, dt,uid, uid_name, project_id, mid)
                    event_msg = "%s请求取消订单"%(uid_name)

                elif atype == "manager":
                    event_msg = "%s同意取消订单" % (uid_name)
                    result = self.db.execute("""
                        update t_projects_member set is_cancel_confirm_at=%s,is_cancel_confirm_uid=%s,is_cancel_confirm_uid_name=%s where project_id=%s and mid=%s
                    """,dt, uid, uid_name, project_id, mid)
                elif atype=="manager_roll":
                    event_msg = "%s恢复订单" % (uid_name)
                    result = self.db.execute("""
                        update t_projects_member set   is_cancel_confirm_at=NULL,
                        is_cancel_confirm_uid=0,is_cancel_confirm_uid_name=NULL,is_cancel=0 ,is_cancel_at=NULL,
                        is_cancel_uid=0,is_cancel_uid_name=NULL where project_id=%s and mid=%s
                    """,  project_id, mid)
                #         update t_projects_member set confirm_banjie=%s,banjie_remark=%s where project_id=%s and guid=%s
                elif atype=="banjie_reject":
                    event_msg="%s驳回办结"%uid_name
                    result = self.db.execute("""
                        update t_projects_member set  confirm_banjie=0,banjie_remark=NULL   where project_id=%s and mid=%s
                    """,  project_id, mid)
                events.add_project_event(self, project_id, "流转取消", event_msg,
                                         uid, uid_name,customer_id)
                self.write(str(result))

        elif  tag=="add_income":
            body = self.get_argument("body")
            data = json.loads(body)
            project_id = self.get_argument("project_id")
            pay_type_name = self.get_argument("pay_type_name")
            pay_type_id = self.get_argument("pay_type_id")
            company_id = self.get_argument("company_id")
            company_id_name = self.get_argument("company_id_name")
            parent_id = self.get_argument("parent_id",0)
            income_at = self.get_argument('income_at')

            if int(parent_id) > 0:

                title_id_result = self.db.execute("""
                       update t_projects_income_title set income_at=%s,
                        updated_at=%s,uid=%s,uid_name=%s,
                        pay_type_name=%s,pay_type_id=%s,company_id=%s,company_id_name=%s
                         where id=%s
                    """,income_at,dt, uid, uid_name, pay_type_name, pay_type_id,
                                           company_id, company_id_name,
                                           parent_id)
                if title_id_result==0:

                    for item in data:
                        if item:

                            project_income_id =0
                            income_row = self.db.get(
                                "select * from t_projects_income where income_id=%s and income_num=%s and parent_id=%s and project_id=%s",
                                item["income_id"], item["income_num"],
                                parent_id, project_id)
                            if income_row:
                                return_income_id = self.db.execute(
                                    """update  t_projects_income set income_money=%s where
                                           income_id=%s and income_num=%s and parent_id=%s and project_id=%s
                                        """, item["income_money"],
                                    item["income_id"], item["income_num"],
                                    parent_id, project_id)
                                project_income_id = income_row.id
                            else:

                                guid = uuid.uuid4()
                                project_income_id = self.db.execute(
                                    """insert into t_projects_income(project_id,
                                        income_name,income_money,uid,uid_name,guid,
                                        created_at,updated_at,remark,income_id,parent_id,income_num)
                                        values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
                                        """, project_id, item["income_name"],
                                    item["income_money"], uid, uid_name, guid,dt,dt,
                                    item["remark"], item["income_id"], parent_id,
                                    item["income_num"])


                            income_detail = item.get("income_detail")
                            # print "title----------", parent_id, income_detail
                            if income_detail:
                                js = json.loads(income_detail)
                                self.db.execute(
                                    "delete from t_projects_income_detail where title_id=%s",
                                    parent_id)
                                for aaaa in js:
                                    result = self.db.execute(
                                        """
                                                    insert into t_projects_income_detail(income_id,income_name,project_id,service_id,
                                                    service_name,service_money,created_at,updated_at,uid_name,uid,title_id,project_income_id
                                                    )
                                                    values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
                                                """, item["income_id"],
                                        item["income_name"], project_id,
                                        aaaa["service_id"],
                                        aaaa["service_name"],
                                        aaaa["service_money"], dt, dt,
                                        uid_name, uid, parent_id,
                                        return_income_id)


                                # else:
                                #     if str(aaaa["service_money"])== "0.00" or str(aaaa["service_money"])== "0":

                                #         self.db.execute(
                                #             "delete from t_projects_income_detail  where id=%s and  project_id=%s",detail_id
                                #             , project_id
                                #         )
                                #     else:
                                #         result = self.db.execute(
                                #             """update  t_projects_income_detail set  service_money=%s,updated_at=%s ,uid_name=%s,uid=%s
                                #                     where id=%s and  project_id=%s
                                #                 """, aaaa["service_money"], dt,
                                #             uid_name, uid,detail_id
                                #             , project_id)

            else:
                # print "title----------"
                title_id = self.db.execute("""
                        insert into t_projects_income_title (income_at,project_id,income_title,total,
                        created_at,updated_at,uid,uid_name,guid,pay_type_name,pay_type_id,company_id,company_id_name)
                        values(%s,%s,%s,0,%s,%s,%s,%s,uuid(),%s,%s,%s,%s)
                    """,income_at, project_id, "",dt,dt, uid, uid_name, pay_type_name,
                                           pay_type_id, company_id,
                                           company_id_name)
                for item in data:
                    if item:
                        guid = uuid.uuid4()
                        return_income_id = self.db.execute(
                            """insert into t_projects_income(project_id,
                                income_name,income_money,uid,uid_name,guid,
                                created_at,updated_at,remark,income_id,parent_id,income_num)
                                values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
                                """, project_id, item["income_name"],
                            item["income_money"], uid, uid_name, guid,dt,dt,
                            item["remark"], item["income_id"], title_id,
                            item["income_num"])
                        income_detail = item.get("income_detail")


                        if income_detail:
                            js = json.loads(income_detail)

                            for aaaa in js:
                                result = self.db.execute(
                                    """
                                            insert into t_projects_income_detail(income_id,income_name,project_id,service_id,
                                            service_name,service_money,created_at,updated_at,uid_name,uid,title_id,project_income_id
                                            )
                                            values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
                                        """, item["income_id"],
                                    item["income_name"], project_id,
                                    aaaa["service_id"], aaaa["service_name"],
                                    aaaa["service_money"], dt, dt, uid_name, uid,
                                    title_id,return_income_id)

            self.write("0")
        elif tag=="add_service_income":
            body = self.get_argument("body")
            data = json.loads(body)
            project_id = self.get_argument("project_id")
            free=self.get_argument('free')
            customer_id=self.get_argument('customer_id','0')
            return_val = 100
            txt=''
            if not project_id:
                self.write("project_id not exits")
            elif not  body:
                self.write("not body")
            else:

                for item in data:
                    if item:
                        t_projects_service_income = self.db.get(
                            "select * from t_projects_service_income where  guid=%s and sid=%s",
                            item["guid"],item["sid"])
                        if t_projects_service_income:
                            is_free=0
                            for row in free.split(','):
                                if item['sid']==row:
                                    is_free=1
                                    break
                            return_val = self.db.execute(
                                """
                                update t_projects_service_income set
                                uid=%s,uid_name=%s, updated_at=%s,service_money=%s,is_free=%s
                                where guid=%s and project_id=%s and sid=%s
                            """, uid, uid_name,dt, item["service_money"],is_free, item["guid"],
                                project_id,item["sid"])
                            if float(t_projects_service_income.service_money)!=float(item["service_money"]):
                                txt+=',设置 '+t_projects_service_income.service_name+' 收入 '+str(t_projects_service_income.service_money)+' 修改为 '+item["service_money"]
                            elif  is_free==1 and int(t_projects_service_income.is_free)!=int(is_free) and item["service_money"]=='0.00':
                                txt+=',设置 '+t_projects_service_income.service_name+' 免收费'

                            self.db.execute("""
                                    update t_projects set
                                    all_income=(select ifnull(sum(service_money),0) from t_projects_service_income where project_id=%s),

                                    con_wait_income=ifnull(all_income-(select ifnull(sum(income_money),0) from t_projects_income
                                    a ,t_projects_income_title b where b.id=a.parent_id and a.project_id=%s
                                    and income_uid >0 and a.income_id <= 43),0)

                                        where id=%s
                                    """, t_projects_service_income.project_id,
                                            t_projects_service_income.project_id,
                                            t_projects_service_income.project_id)  #待付款

                if txt:
                    events.add_project_event(self,project_id,'业务收入明细(确认单'+project_id+')',txt[1:],uid,uid_name,customer_id)

            self.write(str(return_val))

            # result = self.db.execute("""
            # insert into t_projects_service_income(project_id,service_id,service_name, service_money,uid,guid,created_at,updated_at,uid_name)
            # values(%s,%s,%s,%s,%s,%s,now(),now(),%s)
            # """, project_id, service_id, service_name, service_money,
            #                          uid, guid,uid_name)


        elif tag=="reset_print_to_customer":
            project_id = self.get_argument("project_id")
            title_id = self.get_argument("title_id")
            if not project_id:
                self.write('project_id is null')
            elif not title_id:
                self.write('project_id is null')
            else:
                result = self.db.execute("delete from t_projects_income_title_print where project_id=%s and title_id=%s",project_id,title_id)

                self.write(result)

        elif tag == "print_to_customer_preview":
            customer_name = self.get_argument("customer_name")
            all_income = self.get_argument("all_income")
            all_income_cn = self.get_argument("all_income_cn")
            project_name = self.get_argument('project_name')
            end_date = self.get_argument("end_date").replace(u"年","-").replace(u"月","-").replace(u"日","")
            end_date1 = self.get_argument('end_date1').replace(
                u"年", "-").replace(u"月", "-").replace(u"日", "")
            end_date2 = self.get_argument("end_date2").replace(
                u"年", "-").replace(u"月", "-").replace(u"日", "")
            wait_pay_income = self.get_argument('wait_pay_income')
            ys_remark  = self.get_argument("ys_remark","")
            remark=self.get_argument("remark","")
            project_id = self.get_argument("project_id")
            title_id = self.get_argument("title_id")

            if not customer_name:
                self.write("not customer_name")
            elif not all_income:
                self.write("not all_income")
            elif not all_income_cn:
                self.write("not all_income_cn")
            else:
                income_print = self.db.get("select * from t_projects_income_title_print where project_id=%s and title_id=%s",project_id,title_id)
                if income_print:
                    result = self.db.execute("""
                            update t_projects_income_title_print set
                            all_income =%s ,
                            wait_income=%s,
                            all_income_cn=%s,
                            project_name=%s,
                            end_date=%s,
                            end_date1=%s,
                            end_date2=%s,
                            customer_name=%s,
                            ys_remark=%s,
                            remark=%s
                            where project_id=%s and title_id=%s
                        """, all_income, wait_pay_income, all_income_cn,
                                             project_name, end_date, end_date1,
                                             end_date2, customer_name,ys_remark,remark,
                                             project_id, title_id)
                else:
                    result = self.db.execute(
                        """
                        INSERT INTO `t_projects_income_title_print`
                            (
                            `project_id`, `title_id`,`all_income`,`wait_income`,
                            `all_income_cn`, `project_name`,`end_date`,
                            `end_date1`,`end_date2`,`created_at`,`updated_at`,`uid_name`,`uid`,customer_name,ys_remark)
                        VALUES
                        (%s,%s,%s,  %s,
                         %s,%s,%s,
                        %s, %s,%s, %s,%s,%s,%s,%s); """, project_id,
                        title_id, all_income, wait_pay_income, all_income_cn,
                        project_name, end_date, end_date1, end_date2,dt,dt, uid_name,
                        uid, customer_name, ys_remark)
                self.write(str(result))
        elif  tag=="delete_service_money":
            project_id = self.get_argument("project_id")
            guid = self.get_argument("guid")
            if not guid:
                self.write('not guid')
            else:
                service_income = self.db.get("select * from t_projects_service_income where guid=%s and project_id=%s ",guid,project_id)

                t_projects_income_detail = self.db.get("select count(*) count from t_projects_income_detail where project_id=%s and service_id=%s",project_id,service_income.service_id)
                if service_income and t_projects_income_detail.count >0:
                    self.write("请删除到款中的(%s)明细"%service_income.service_name)
                else:
                    result = self.db.execute("""update t_projects_service_income set
                            uid=%s,uid_name=%s, updated_at=%s,service_money=0
                            where guid=%s and project_id=%s""",uid, uid_name,dt,guid, project_id)
                    self.db.execute("""
                        update t_projects set
                        all_income=(select ifnull(sum(service_money),0) from t_projects_service_income where project_id=%s),

                        con_wait_income=ifnull(all_income-(select ifnull(sum(income_money),0) from t_projects_income
                        a ,t_projects_income_title b where b.id=a.parent_id and a.project_id=%s
                        and income_uid >0 and a.income_id <= 43),0)

                            where id=%s
                        """, project_id,
                                project_id,
                                project_id)
                    self.write(str(result))



        elif tag=="contract_confirm":
            project_id = self.get_argument("project_id")
            contract_remark = self.get_argument("contract_remark","")
            contract_type_id = self.get_argument("contract_type_id")
            contract_number = self.get_argument("contract_number","")
            contract_confirm_id_name = self.get_argument("contract_confirm_id_name")
            guid = self.get_argument("guid")

            t_project = self.db.get("select * from t_projects where guid=%s and id=%s",guid,project_id)
            if t_project:
                result = self.db.execute(
                    """update t_projects set contract_confirm_id=%s ,
                    contract_confirm_at=%s,
                    contract_uid=%s,
                    contract_uid_name=%s ,
                    contract_remark=%s,
                    contract_confirm_id_name=%s ,
                    contract_number=%s
                    where id=%s """, contract_type_id,dt,uid, uid_name, contract_remark, contract_confirm_id_name, contract_number, project_id)
                if result ==0:
                    msg.insert_new(
                        self, t_project.uid,
                        u"[系统信息] 您好 %s已经设置[%s]合同状态为 %s <a href='/project?tag=show&guid=%s&id=%s'>查看</a>"
                        % (
                            uid_name.decode('utf8'),
                            t_project.project_name,
                            contract_confirm_id_name,
                            t_project.guid,
                            project_id
                        ),1)
                self.write(str(result))

        elif tag =="confirm_word":
            project_id = self.get_argument("project_id")
            project_guid = self.get_argument("project_guid")

            if not project_guid:
                self.set_status(404)
            else:
                t_project = self.db.get("select * from t_projects where id=%s and guid=%s",project_id,project_guid)
                if t_project:
                    result = self.db.execute("update t_projects set from_word_uid=%s, from_word_uid_name=%s,from_word_confirm_at=%s where id=%s",
                    uid,uid_name,dt,project_id)
                    self.write(str(result))
                else:
                    self.write( "not project")

        elif tag =="to_kj":
            project_id = self.get_argument("project_id")
            project_guid = self.get_argument("project_guid")
            department_id = self.get_argument("department_id")
            department_id_name = self.get_argument('department_id_name')
            if not project_guid:
                self.set_status(404)
            else:
                t_project = self.db.get("select * from t_projects where id=%s and guid=%s",project_id,project_guid)
                if t_project:
                    event_msg="流转至%s"%(department_id_name)
                    events.add_project_event(self, project_id, "订单部门流转(确认单"+project_id+")", event_msg,
                                         uid, uid_name,0)
                    result = self.db.execute("update t_projects set project_department_id=%s,project_department_id_name=%s where id=%s",department_id,department_id_name,
                    project_id)
                    self.write(str(result))
                else:
                    self.write( "not project")

        elif tag =="new":
            business_channel = self.get_argument("business_channel", "")
            # busniess_type_str = ",".join(busniess_type)
            busniess_from = self.get_argument("busniess_from","")
            project_name = self.get_argument("project_name")
            customer_name = self.get_argument("customer_name")
            customer_company = self.get_argument("customer_company")
            customer_tel = self.get_argument("customer_tel")
            all_income = self.get_argument("all_income")
            pre_income  = self.get_argument("pre_income","")

            true_income = self.get_argument("true_income",0)
            remark = self.get_argument("remark","")
            sign_type_id_str = self.get_argument("sign_type_id")
            talk_type = self.get_argument("talk_type","")
            from_word = self.get_argument("from_word","无")
            # company = self.get_argument("company")
            recommend_by = self.get_argument("recommend_by","")
            is_finance = self.get_argument("is_finance",'0')
            recommend_staff = self.get_argument("recommend_staff","")
            building_id_str = self.get_argument("building_id", "")
            deal_day = self.get_argument("deal_day","")
            new_contract_type_id = self.get_argument("new_contract_type_id")
            addr_type = self.get_argument("addr_type","")
            kf_id_str = self.get_argument("kf_id", "")
            is_expedited=self.get_argument("is_expedited",0)
            rel_company_id_name=self.get_argument("rel_company_id_name","")
            rel_company_id=self.get_argument("rel_company_id",0)
            promo_id_str = self.get_argument("promo_id", "")
            company_uid = self.get_argument("company_uid","")
            guid = uuid.uuid4()
            if not  pre_income:
                pre_income=0
            if not deal_day:
                deal_day =0
            t_customer = None
            if company_uid:
                company_uid = company_uid.upper()
            customer_company = customer_company.replace("（","(").replace("）",")")
            if not project_name:
                return self.write("not projectname")
            elif customer_company!="" and company_uid and len(company_uid)!=18:
                return self.write("当公司名称不为空,信用代码必须为18位哦.")
            else:
                if customer_company:
                    t_customer_company= self.db_customer.get("select * from t_customer where company=%s ",customer_company)
                    if not t_customer_company:
                        customer_company = customer_company.replace("(","（").replace(")","）")
                        t_customer_company= self.db_customer.get("select * from t_customer where company=%s ",customer_company)
                    
                    if t_customer_company and t_customer_company.company_reguid!=company_uid:
                        return self.write("您输入的公司名称({}),与客户管理系统中的信用代码不一致{},请核实".format(customer_company,t_customer_company.company_reguid))
                if company_uid:
                    t_customer_company= self.db_customer.get("select * from t_customer where company_reguid=%s ",company_uid)
                    if t_customer_company and t_customer_company.company!=customer_company:
                        return self.write("您输入的公司名称({}),与客户管理系统中的信用代码不一致{},请核实".format(customer_company,t_customer_company.company_reguid))

                 
                
                channel_id =0
                channel_id_name = ""
                recommend_id =0
                recommend_id_name =""
                building_id = 0
                building_id_name = ""
                talk_type_id=0
                talk_type_id_name=''
                busniess_from_id = busniess_from.split("|")[0]
                busniess_from_id_name = busniess_from.split("|")[1]
                is_acc = 0 #会计业务
                if busniess_from_id_name=="续帐" or busniess_from_id_name=="会计":
                    # is_acc = 1
                    t_customer = self.db_customer.get(
                        "select * from t_customer where company=%s",
                        customer_company)
                    if not  t_customer:
                        return self.write("%s ---不存在客户管理系统哦"%(customer_company))
                    elif not t_customer.acc_uid:
                        return self.write("该公司(%s)没有分配会计哦" % (customer_company))


                promo_id =0,
                promo_id_name =""
                if promo_id_str and promo_id_str!="0":
                    promo_id = promo_id_str.split("|")[0]
                    promo_id_name = promo_id_str.split("|")[1]
                if business_channel:
                    channel_id = business_channel.split("|")[0]
                    channel_id_name = business_channel.split("|")[1]
                if talk_type:
                    talk_type_id = talk_type.split("|")[0]
                    talk_type_id_name = talk_type.split("|")[1]
                # if company:
                #     company_id = company.split("|")[0]
                #     company_id_name = company.split("|")[1]
                if sign_type_id_str:
                    sign_type_id = sign_type_id_str.split("|")[0]
                    sign_type_id_name = sign_type_id_str.split("|")[1]
                if new_contract_type_id:
                    contract_confirm_id=new_contract_type_id.split("|")[0]
                    contract_confirm_id_name = new_contract_type_id.split("|")[1]

                if int(busniess_from_id) != 2:
                    from_word = ""
                    channel_id="0"
                    channel_id_name=""
                if building_id_str != "0":
                    building_id = building_id_str.split("|")[0]
                    building_id_name = building_id_str.split("|")[1]
                print "building_id_str",building_id_str
                if busniess_from_id_name=="客户推荐" or busniess_from_id_name=="传统开发" or busniess_from_id_name=="会计" or busniess_from_id_name=="续帐":
                    talk_type_id=0
                    talk_type_id_name=''
                if busniess_from_id_name!="传统开发":
                    rel_company_id_name=''
                    rel_company_id=0
                id = self.db.execute(
                    """
                       INSERT INTO `t_projects`
                                (`company_uid`,
                                `is_expedited`,
                                `addr_type`,

                                `recommend_staff`,
                                `project_name`,
                                `customer_name`,
                                `customer_tel`,
                                `customer_company`,
                                `all_income`,
                                `pre_income`,
                                `true_income`,
                                `is_lock`,
                                `uid`,
                                `guid`,
                                `created_at`,
                                `updated_at`,
                                `remark`,
                                `busniess_from_id`,
                                `busniess_from_id_name`,
                                `channel_id`,channel_id_name,contract_sign_type_id,
                                from_word,talk_type_id,talk_type_id_name,uid_name,recommend_by,is_finance,
                                building_id,building_id_name,sign_type_id_name,deal_day,contract_confirm_id,contract_confirm_id_name,rel_company_id_name,rel_company_id,is_acc,promo_id,promo_id_name)
                                VALUES
                                (%s,%s,%s,%s,%s,%s,%s, %s,%s, %s, %s, %s, %s, %s,%s,%s,%s, %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);
                    """,company_uid, is_expedited, addr_type, recommend_staff,
                    project_name, customer_name, customer_tel,
                    customer_company, all_income, pre_income, true_income, 0,
                    uid, guid,dt,dt, remark, busniess_from_id, busniess_from_id_name,
                    channel_id, channel_id_name, sign_type_id, from_word,
                    talk_type_id, talk_type_id_name, uid_name,
                    recommend_by, is_finance, building_id,
                    building_id_name, sign_type_id_name, deal_day,
                    contract_confirm_id, contract_confirm_id_name,
                    rel_company_id_name, rel_company_id, is_acc,promo_id,promo_id_name)
                if id > 0:
                    is_add_kf =""
                    if kf_id_str != "0" and kf_id_str:
                        kf_id = kf_id_str.split("|")[0]
                        kf_id_name = kf_id_str.split("|")[1]
                        # self.db.execute("""
                        #     update t_projects_member set member_id=%s,updated_uid=%s,updated_uid_name=%s,updated_at=now(),member_name=%s
                        #                     where team_id=39 and project_id=%s
                        #                 """, kf_id, uid, uid_name, kf_id_name,
                        #                 id)

                        self.db.execute("""
                        insert into t_projects_member (team_name,team_id,project_id,created_at,member_id,guid,updated_at,updated_uid,updated_uid_name,member_name)
                            values("在线客服",39,%s,%s,%s,uuid(),%s,%s,%s,%s)

                        """, id, dt, kf_id, dt, uid, uid_name, kf_id_name)
                        is_add_kf = " and id!=39 " #在线客服
                        msg.insert_new(
                            self, recommend_id,
                            u"[系统信息] 您好,%s将您设置为[%s]项目角色:在线客服 确认关键词信息哦。<a href='/project?tag=show&guid=%s&id=%s'>查看</a>"
                            % (uid_name.decode('utf8'), project_name, guid,
                            id), 1)



                    add_sql_for_customer = ""

                    # if t_customer:
                        # if busniess_from_id_name=="续帐":
                        #     add_sql_for_customer = " and (income_parentid=203 or is_hide=100) "

                        # is_add_kf += " and id !=205 "
                        # not_transition = 1
                        # if busniess_from_id_name=="会计":
                        #     not_transition=0 #会计流转

                        # self.db.execute("""
                        # insert into t_projects_member (team_name,team_id,project_id,created_at,member_id,
                        # guid,updated_at,updated_uid,updated_uid_name,member_name,not_transition)
                        #     values("客服会计",205,%s,%s,%s,uuid(),%s,%s,%s,%s,%s)
                        # """, id, dt, t_customer.acc_uid, dt, uid, uid_name, t_customer.acc_uid_name,not_transition)
                        #客服会计

                        # msg.insert_new(
                        #     self, recommend_id,
                        #     u"[系统信息] 您好,%s将您设置为[%s]项目角色:客服会计。 有提成的哦.<a href='/project?tag=show&guid=%s&id=%s'>查看</a>"
                        #     % (t_customer.acc_uid_name.decode('utf8'), project_name, guid,
                        #     id), 1)

                    self.db.execute("""
                        insert into t_projects_member (team_name,team_id,project_id,created_at,member_id,guid,updated_at,updated_uid,updated_uid_name)
                            select income_name,id,%s,now(),0,uuid(),now(),%s,%s from t_projects_type where income_category='项目角色' 
                        """ + is_add_kf , id, uid,
                                    uid_name)

                    self.db.execute("""
                            insert into t_projects_service_income(project_id,service_id,service_name, service_money,uid,guid,
                            created_at,updated_at,uid_name)
                            select %s,id,income_name,0,%s,uuid(),now(),now(),%s from t_projects_type
                             where income_category='业务类型'
                    """ + add_sql_for_customer, id, uid, uid_name)


                    # self.db.execute("""
                    #     INSERT INTO `t_projects_file`
                    #         (
                    #         `file_type_id`,
                    #         `file_type_name`,
                    #         `is_upload`,
                    #         `rec_num`,
                    #         `project_id`,
                    #         `guid`,uid,file_type_cate_id,order_int)
                    #         select id,income_name,0,0,%s,uuid(),0,0,order_int from t_projects_type where income_category='资料交接明细' order by order_int desc
                    # """,id)
                    if from_word and from_word != u"无":
                        msg.insert_new_group(
                            self,
                            u"[关键词待确认] 您好 %s创建[%s]新项目关键词[%s]需要确认。 <a href='/project?tag=show&guid=%s&id=%s'>查看</a>"
                            % (uid_name.decode('utf8'), project_name,
                               from_word, guid, id), 2, 6)

                #return self.redirect("project?tag=show&guid=%s&id=%s"%(guid,id))
                return self.write("project?tag=show&guid=%s&id=%s" % (guid, id))


        elif tag=="modify1":
            customer_company = self.get_argument("customer_company",'')
            project_id = self.get_argument("project_id")
            project_guid = self.get_argument("project_guid")
            customer_name=self.get_argument('customer_name','')
            company_uid = self.get_argument("company_uid","")
            is_update_company_customer=self.get_argument('is_update_company_customer','')
            is_update_company_project=self.get_argument('is_update_company_project','')
            t_project = self.db.get('select * from t_projects where id=%s',project_id)
            banjie_company_uid=self.get_argument('banjie_company_uid','')
            t_same_projects = self.db.query('select * from t_projects where customer_company=%s ',t_project.customer_company)
            t_customer = self.db_customer.get('select * from t_customer where company=%s',t_project.customer_company)
            history_company=t_project.customer_company+','
            customer_id=self.get_argument('customer_id','0')
            if banjie_company_uid:
                sql=' company_uid="%s", '%banjie_company_uid
            else:
                sql=''
            if t_project.customer_company!=customer_company and t_project.customer_company!='' and customer_company!='':
                if is_update_company_project:
                    self.db.execute(
                        """
                        update `t_projects` set   customer_company=%s,company_history=CONCAT(company_history,%s) where customer_company=%s""",
                        customer_company,history_company,t_project.customer_company)
                    for t_same_project in t_same_projects:
                        self.db.execute('''
                            insert into t_projects_company_history(project_id,company,uid_name,uid,created_at)
                            values(%s,%s,%s,%s,%s)
                        ''',t_same_project.id,t_project.customer_company,uid_name,uid,dt)
                if t_customer and is_update_company_customer:

                    self.db_customer.execute('''
                        update t_customer set company=%s where company=%s
                    ''',customer_company,t_project.customer_company)
                    self.db_customer.execute("""
                        INSERT INTO `t_company_name`
                            (customer_id,
                            `name`,
                            `uid`,
                            `uid_name`,
                            `created_at`,
                            `remark`)
                            VALUES
                    (%s,%s,%s,%s,%s,%s)""",t_customer.id, t_customer.company, uid, uid_name,dt,'')
                else:
                    self.db.execute(
                            """
                            update `t_projects` set company_history=CONCAT(company_history,%s) where id=%s and guid=%s""",customer_company+',',project_id,project_guid)
                    self.db.execute('''
                            insert into t_projects_company_history(project_id,company,uid_name,uid,created_at)
                            values(%s,%s,%s,%s,%s)
                        ''',project_id,t_project.customer_company,uid_name,uid,dt)
            if customer_name:
                self.db.execute(
                        """
                        update `t_projects` set `customer_name`=%s,company_uid=%s where id=%s and guid=%s""",customer_name,company_uid,project_id,project_guid)
            else:

                self.db.execute(
                        """
                        update `t_projects` set """+sql+""" `customer_company`=%s where id=%s and guid=%s"""
                        ,customer_company,project_id,project_guid)
                if t_project.customer_company!=customer_company:
                    events.add_project_event(self, project_id, "公司名称(确认单"+project_id+")",t_project.customer_company+' 修改为 '+customer_company,
                                         uid, uid_name,customer_id)
        elif tag == "modify":
            business_channel = self.get_argument("business_channel","")
            # busniess_type_str = ",".join(busniess_type)
            busniess_from = self.get_argument("busniess_from", "")
            project_name = self.get_argument("project_name")
            customer_name = self.get_argument("customer_name")
            customer_company = self.get_argument("customer_company")
            customer_tel = self.get_argument("customer_tel")
            pre_income = self.get_argument("pre_income")
            remark = self.get_argument("remark", "")
            sign_type_id_str = self.get_argument("sign_type_id")
            talk_type = self.get_argument("talk_type",'')
            from_word = self.get_argument("from_word", "无")
            # company = self.get_argument("company")
            recommend_by = self.get_argument("recommend_by", "")
            is_finance = self.get_argument("is_finance")
            recommend_staff = self.get_argument("recommend_staff", "")
            building_id_str = self.get_argument("building_id", "")
            deal_day = self.get_argument("deal_day")
            new_contract_type_id = self.get_argument("new_contract_type_id")
            addr_type = self.get_argument("addr_type", "")
            is_company_history=self.get_argument("is_company_history",'')
            project_id = self.get_argument("project_id")
            project_guid = self.get_argument("project_guid")
            is_expedited=self.get_argument("is_expedited")
            customer_id=self.get_argument("customer_id",'0')
            customer_company=self.get_argument("customer_company",'')
            company_uid=self.get_argument("company_uid",'')

            same_company=self.get_argument("same_company",'')
            promo_id_str = self.get_argument("promo_id", "")
            is_update_company_customer=self.get_argument('is_update_company_customer','')
            is_update_company_project=self.get_argument('is_update_company_project','')
            promo_id =0
            promo_id_name =""
            history_company=''

            print(project_name)
            if not project_name:
                return self.write("业务名称不能为空")
            elif customer_company!="" and company_uid and len(company_uid)!=18:
                return self.write("当公司名称不为空,信用代码必须为18位哦.")
            else:
                if customer_company:
                    t_customer_company= self.db_customer.get("select * from t_customer where company=%s ",customer_company)
                    if t_customer_company and t_customer_company.company_reguid!=company_uid:
                        return self.write("您输入的公司名称({}),与客户管理系统中的信用代码不一致{},请核实输入错误还是系统错误".format(customer_company,t_customer_company.company_reguid))
                if company_uid:
                    t_customer_company= self.db_customer.get("select * from t_customer where company_reguid=%s ",company_uid)
                    if t_customer_company and t_customer_company.company!=customer_company:
                        return self.write("您输入的公司名称({}),与客户管理系统中的信用代码不一致{},请核实输入错误还是系统错误".format(customer_company,t_customer_company.company_reguid))


            if not  pre_income:
                pre_income=0
            if not deal_day:
                deal_day =0
            if promo_id_str!='0':
                promo_id = promo_id_str.split("|")[0]
                promo_id_name = promo_id_str.split("|")[1]
            if not project_id:
                print('1')
                self.write("not projectname")
            else:
                t_project = self.db.get('select * from t_projects where id=%s and guid=%s',project_id,project_guid)
                if not t_project:
                    print('2')

                    self.write("not project")
                    
                else:



                    t_same_projects = self.db.query('select * from t_projects where customer_company=%s ',t_project.customer_company)
                    t_customer = self.db_customer.get('select * from t_customer where company=%s',t_project.customer_company)
                    channel_id = 0
                    channel_id_name =""
                    if business_channel:
                        channel_id = business_channel.split("|")[0]
                        channel_id_name = business_channel.split("|")[1]

                    busniess_from_id = busniess_from.split("|")[0]
                    busniess_from_id_name = busniess_from.split("|")[1]
                    if talk_type:
                        talk_type_id = talk_type.split("|")[0]
                        talk_type_id_name = talk_type.split("|")[1]
                    else:
                        talk_type_id=0
                        talk_type_id_name=''
                    # company_id = company.split("|")[0]
                    # company_id_name = company.split("|")[1]
                    sign_type_id = sign_type_id_str.split("|")[0]
                    sign_type_id_name = sign_type_id_str.split("|")[1]
                    recommend_id =0
                    recommend_id_name =""

                    contract_confirm_id=new_contract_type_id.split("|")[0]
                    contract_confirm_id_name = new_contract_type_id.split("|")[1]

                    if busniess_from_id !='2':
                        from_word = ""
                        channel_id="0"
                        channel_id_name=""

                    building_id = 0
                    building_id_name = ""
                    if building_id_str != "0":
                        building_id = building_id_str.split("|")[0]
                        building_id_name = building_id_str.split("|")[1]
                    if busniess_from_id_name=="客户推荐" or busniess_from_id_name=="传统开发" or busniess_from_id_name=="会计" or busniess_from_id_name=="续帐":
                        talk_type_id=0
                        talk_type_id_name=''
                    if busniess_from_id_name!="传统开发":
                        rel_company_id_name=''
                        rel_company_id=0

                    if t_project.customer_company!=customer_company and t_project.customer_company!='' and customer_company!='':
                        if is_company_history and is_update_company_project:
                            history_company=t_project.customer_company+','
                            for t_same_project in t_same_projects:
                                self.db.execute('''
                            insert into t_projects_company_history(project_id,company,uid_name,uid,created_at)
                            values(%s,%s,%s,%s,%s)
                        ''',t_same_project.id,t_project.customer_company,uid_name,uid,dt)
                        elif is_company_history and not is_update_company_project:
                            self.db.execute('''
                            insert into t_projects_company_history(project_id,company,uid_name,uid,created_at)
                            values(%s,%s,%s,%s,%s)
                        ''',t_project.id,t_project.customer_company,uid_name,uid,dt)
                        if is_update_company_project:
                            self.db.execute(
                                """
                                update `t_projects` set customer_company=%s,company_history=CONCAT(company_history,%s) where customer_company=%s""",
                                customer_company,history_company,t_project.customer_company)

                        if t_customer and is_update_company_customer:
                            self.db_customer.execute('''
                                update t_customer set company=%s where company=%s
                            ''',customer_company,t_project.customer_company)
                            self.db_customer.execute("""
                                INSERT INTO `t_company_name`
                                    (customer_id,
                                    `name`,
                                    `uid`,
                                    `uid_name`,
                                    `created_at`,
                                    `remark`)
                                    VALUES
                            (%s,%s,%s,%s,%s,%s)""",t_customer.id, t_customer.company, uid, uid_name,dt,'')
                    print(project_id,project_guid)
                    result = self.db.execute(
                        """
                        update `t_projects` set
                                `is_expedited`=%s,
                                `addr_type`=%s,
                                `recommend_staff`=%s,
                                `project_name`=%s,
                                `customer_name`=%s,
                                `customer_tel`=%s,
                                `customer_company`=%s,
                                `pre_income`=%s,
                                `updated_at`=%s,
                                `remark`=%s,
                                `busniess_from_id`=%s,
                                `busniess_from_id_name`=%s,
                                `channel_id`=%s,
                                channel_id_name=%s,
                                contract_sign_type_id=%s,
                                from_word=%s,
                                talk_type_id=%s,
                                talk_type_id_name=%s,
                                recommend_by=%s,
                                is_finance=%s,
                                building_id=%s,
                                building_id_name=%s,
                                sign_type_id_name=%s,
                                deal_day=%s,
                                contract_confirm_id=%s,
                                contract_confirm_id_name=%s,
                                promo_id=%s,promo_id_name=%s,
                                company_uid=%s
                                  where id=%s and guid=%s
                        """,is_expedited, addr_type, recommend_staff, project_name,
                        customer_name, customer_tel, customer_company
                        , pre_income,dt,
                        remark, busniess_from_id, busniess_from_id_name,
                        channel_id, channel_id_name, sign_type_id, from_word,
                        talk_type_id, talk_type_id_name, recommend_by, is_finance, building_id,
                        building_id_name, sign_type_id_name, deal_day,
                        contract_confirm_id, contract_confirm_id_name,promo_id,promo_id_name,company_uid,project_id,project_guid)

                    if result==0:
                        event_msg=''
                        if int(is_expedited)!=t_project.is_expedited:
                            if is_expedited=='0':
                                event_msg+='加急业务:改为否'
                            else:
                                event_msg+='加急业务:改为是'
                        if int(building_id)!=t_project.building_id:
                            event_msg+=',楼盘:'+t_project.building_id_name+' 修改为 '+building_id_name
                        if int(promo_id)!=t_project.promo_id:
                            if promo_id==0:
                                event_msg+=',优惠活动:取消'+t_project.promo_id_name
                            else:
                                event_msg+=',优惠活动:'+t_project.promo_id_name+' 修改为 '+promo_id_name
                        if not t_project.recommend_by:
                            t_project.recommend_by=''
                        if recommend_by!=t_project.recommend_by:
                            event_msg+=',推荐客户人:'+t_project.recommend_by+' 修改为 '+recommend_by
                        if not t_project.recommend_staff:
                            t_project.recommend_staff=''
                        if recommend_staff!=t_project.recommend_staff:
                            event_msg+=',内部推荐人:'+t_project.recommend_staff+' 修改为 '+recommend_staff
                        if not t_project.from_word:
                            t_project.from_word=''
                        if from_word!=t_project.from_word:
                            event_msg+=',来源关键词:'+t_project.from_word+' 修改为 '+from_word
                        if int(channel_id)!=t_project.channel_id:
                            event_msg+=',来源渠道:'+t_project.channel_id_name+' 修改为 '+channel_id_name
                        if int(sign_type_id)!=t_project.contract_sign_type_id:
                            event_msg+=',签约方式:'+t_project.sign_type_id_name+' 修改为 '+sign_type_id_name
                        if int(talk_type_id)!=t_project.talk_type_id:
                            event_msg+=',来源方式:'+t_project.talk_type_id_name+' 修改为 '+talk_type_id_name
                        if int(is_finance)!=t_project.is_finance:
                            if is_finance=='0':
                                event_msg+=',记账:改为否'
                            elif is_finance=='1':
                                event_msg+=',记账:改为是'
                        if int(contract_confirm_id)!=t_project.contract_confirm_id:
                            event_msg+=',合同情况:'+t_project.contract_confirm_id_name+' 修改为 '+contract_confirm_id_name
                        if not t_project.deal_day:
                            t_project.deal_day=0
                        if int(deal_day)!=t_project.deal_day:
                            event_msg+=',成交周期(天）'+str(t_project.deal_day)+' 修改为 '+str(deal_day)
                        if not t_project.pre_income:
                            t_project.pre_income=0
                        if float(pre_income)!=int(t_project.pre_income):
                            event_msg+=',预计合同定金:'+str(t_project.pre_income)+' 修改为 '+str(pre_income)
                        if not t_project.addr_type:
                            t_project.addr_type=''
                        if addr_type!=t_project.addr_type:
                            event_msg+=',地址类型:'+t_project.addr_type+' 修改为 '+addr_type
                        if not t_project.project_name:
                            t_project.project_name=''
                        if project_name!=t_project.project_name:
                            event_msg+=',业务内容:'+t_project.project_name+' 修改为 '+project_name
                        if not t_project.customer_name:
                            t_project.customer_name=''
                        if customer_name!=t_project.customer_name:
                            event_msg+=',客户姓名:'+t_project.customer_name+' 修改为 '+customer_name
                        if not t_project.customer_company:
                            t_project.customer_company=''
                        if customer_company!=t_project.customer_company:
                            event_msg+=',企业名称:'+t_project.customer_company+' 修改为 '+customer_company
                        if not t_project.customer_tel:
                            t_project.customer_tel=''
                        if customer_tel!=t_project.customer_tel:
                            event_msg+=',联系电话:'+t_project.customer_tel+' 修改为 '+customer_tel
                        
                        if event_msg:
                            if event_msg[0]==',':
                                event_msg=event_msg[1:]
                            events.add_project_event(self, project_id, "业务信息(确认单"+project_id+")", event_msg,
                                         uid, uid_name,customer_id)
                    t_projects_income_title=self.db.query('''
                        select * from t_projects_income_title where project_id=%s and income_uid_at is not null
                    ''',t_project.id)
                    t_project_chuna_history=self.db.get('''
                    select * from t_project_chuna_history where project_id=%s
                    ''',t_project.id)
                    chuna_sql=''
                    result_chuna=0
                    if t_projects_income_title:
                        if t_project.customer_company!=customer_company:
                            if customer_company=='':
                                customer_company='空'
                            chuna_sql+=' company=concat(company,"%s"), company=concat(company,"|"), '%customer_company
                        if t_project.project_name!=project_name:
                            chuna_sql+=' project_name=concat(project_name,"%s"),project_name=concat(project_name,"|"), '%project_name
                        if t_project.customer_name!=customer_name:
                            chuna_sql+=' customer_name=concat(customer_name,"%s"),customer_name=concat(customer_name,"|"),'%customer_name
                        if t_project.customer_tel!=customer_tel:
                            if customer_tel=='':
                                customer_tel='空'
                            chuna_sql+=' customer_tel=concat(customer_tel,"%s"),customer_tel=concat(customer_tel,"|"), '%customer_tel
                        if chuna_sql:

                            if not t_project_chuna_history:
                                result_chuna=self.db.execute('''
                                INSERT INTO t_project_chuna_history
                                (project_id,company,customer_name,customer_tel,project_name,uid,uid_name,updated_at)
                                    values(%s,%s,%s,%s,%s,%s,%s,%s)
                                ''',t_project.id,t_project.customer_company+"|",t_project.customer_name+"|",
                                t_project.customer_tel+"|",t_project.project_name+"|",uid,uid_name,dt)
                            if result_chuna==0:
                                result_chuna=t_project_chuna_history.id
                            self.db.execute('''
                                update t_project_chuna_history set '''+chuna_sql+''' uid=%s,uid_name=%s,updated_at=%s where id=%s
                                ''',uid,uid_name,dt,result_chuna)


                    if same_company:
                        self.db.execute("""
                            insert into t_same_company(project_id,customer_id,customer_company)
                            values(%s,%s,%s)
                        """,project_id,customer_id,customer_company)
                    self.write(str(result))



        elif tag=="delete_member":
            mid = self.get_argument("mid",0)
            guid = self.get_argument("guid")
            project_id = self.get_argument("project_id")
            customer_id=self.get_argument('customer_id','0')
            t_project = self.db.get("select * from t_projects where id=%s",project_id)
            t_project_member = self.db.get(
                "select * from t_projects_member where guid=%s and project_id=%s",
                guid, project_id)
            if not t_project:
                self.write("not t_project")
            elif not t_project_member:
                self.write("not t_project_member")
            else:


                if t_project_member.btype_id >0:

                    #工商专员直接删除
                    result = self.db.execute("""
                    delete from    t_projects_member  where guid=%s and project_id=%s
                """,guid, project_id)
                    if result==0:
                        self.db.execute("""delete from t_projects_milepost where member_id=%s and project_id=%s""",mid,project_id)
                else:
                    result = self.db.execute("""
                        update   t_projects_member set member_id=0 ,member_name='',updated_at=%s,updated_uid=%s,updated_uid_name=%s  where guid=%s and project_id=%s
                    """,dt,uid,uid_name, guid, project_id)
                if result ==0:
                    events.add_project_event(self,'0','删除人员(确认单'+project_id+')','删除'+t_project_member.team_name+t_project_member.member_name,uid,uid_name,customer_id)
                    msg.insert_new(
                        self, t_project_member.member_id,
                        u"[系统信息] 您好 %s将您从项目[%s]角色移除 %s <a href='/project?tag=show&guid=%s&id=%s'>查看</a>"
                        % (uid_name.decode('utf8'), t_project.project_name,
                           t_project_member.team_name, t_project.guid,
                           project_id), 1)
                if t_project_member.btype_id_name == u"公司注册" and t_project_member.team_id == 38:
                    self.db.execute("update t_projects set reg_state=0 where id=%s",project_id)

                self.write(str(result))

        elif tag == "add_member_cq":
            member_id_name = self.get_argument("member_id_name")
            project_id = self.get_argument("project_id")
            team_id = self.get_argument("team_id")
            btype_id = self.get_argument("cq_btype_id")
            btype_id_name = self.get_argument("cq_btype_id_name")
            t_user = self.db.get('select * from t_user where name=%s', member_id_name)
            customer_id=self.get_argument('customer_id','0')

            t_income_type = self.db.get(
                'select * from t_projects_type where id=%s', team_id)
            if not t_income_type:
                self.write("not team role")
            elif not  t_user:
                self.write("not user")
            else:
                member_id = t_user.id
                user_uid_name = t_user.name
                dt=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                milepost = self.db.get("select * from t_projects_type where income_category='办结' and order_int=1 ",)
                if not milepost:
                    self.write("not milepost")
                else:
                    not_transition = 0
                    if t_user.not_process==1:
                        # if user_uid_name == u"周萍" or user_uid_name == u"外资" or user_uid_name == u"取消单(无需流转)" or user_uid_name == u"其他(无需流转)" or user_uid_name == u"调整单(无需流转)":
                        not_transition = 1
                        milepost.income_name = "无需流转"
                        milepost.id = "0"
                    if btype_id_name == u"公司注册":
                        self.db.execute("update t_projects set reg_state=1 where id=%s",project_id)
                    id = self.db.execute("""
                                    INSERT INTO `t_projects_member`
                                    (`team_id`,
                                    `team_name`,
                                    `member_id`,
                                    `created_at`,
                                    `project_id`,
                                    `guid`,
                                    `member_name`,
                                    `updated_at`,
                                    `updated_uid`,
                                    `updated_uid_name`,`btype_id`,`btype_id_name`,last_milepost_id_name,last_milepost_id,last_milepost_id_at,not_transition)

                                    values(%s,%s,%s,%s,%s,uuid(),%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)

                                """, team_id, t_income_type.income_name, t_user.id,
                                        dt, project_id, t_user.name,dt, uid,
                                        uid_name, btype_id, btype_id_name,
                                        milepost.income_name, milepost.id, dt,not_transition)
                    if id > 0 and not_transition == 0:
                        team_mile_sql=""
                        if team_id=="205":
                            team_mile_sql = " and order_int in (1,2,3,8)"

                        events.add_project_event(self,project_id,'新增跟单人(确认单'+project_id+')',
                        '新增跟单:'+t_user.name+',跟单业务:'+btype_id_name,uid,uid_name,customer_id)
                        self.db.execute(""" INSERT INTO `t_projects_milepost`
                                            (
                                            `project_id`,
                                            `is_lock`,
                                            `confirm_at`,
                                            `uid`,
                                            `uid_name`,
                                            `guid`,
                                            `created_at`,
                                            `updated_at`,
                                            `remark`,
                                            `type_name`,
                                            `type_id`,
                                            `btype_name`,
                                            `btype_id`,
                                            `order_int`,member_id)

                                            SELECT %s,0,NULL,%s,%s,UUID(),now(),NOW(),NULL,income_name,id,%s,%s,order_int,%s

                                            FROM `t_projects_type` where income_category='办结'""" +team_mile_sql, project_id, member_id, user_uid_name, btype_id_name, btype_id, id)
                        self.db.execute( "update t_projects_milepost set confirm_at=%s where project_id=%s  and member_id=%s order by order_int  limit 1",
                            dt, project_id, id)

                    self.write(str(id))
        # elif tag=="add_to_project_group":
        #     department_id = int(self.get_argument("department_id",0))
        #     department_id_name = self.get_argument("department_id_name","")
        #     if not department_id:
        #         return self.write(" 部门不能为空哦.")
        #     else:
        #         result = self.db.execute("update t_projects set project_department_id=%s, project_department_id_name=%s where id=%s",project_id)
        #         return self.write(str(result))
        elif tag == "add_member_cq_group":
            body = self.get_argument("body")

            milepost = self.db.get(
                "select * from t_projects_type where income_category='办结' and order_int=1 ",
            )
            if not milepost:
                self.write("not milepost")
            else:

                data = json.loads(body)
                if  not data:
                    return self.write("没有可操作数据")
            
                for row in data:
                    if row:
                        cq_department_id_name = row["cq_department_id_name"]
                        cq_department_id = row["cq_department_id"]
                        project_id =row["project_id"]
                        result=1
                        t_acc_member = self.db.get("select count(*) count from t_projects_member where project_id=%s",project_id)
                        if  t_acc_member.count==0:
                                self.db.execute("""insert into t_projects_member (team_name,team_id,project_id,created_at,member_id,
                                guid,updated_at,updated_uid,updated_uid_name,member_name,not_transition)
                                    values("客服会计",205,%s,%s,0,
                                    uuid(),%s,%s,%s,NULL,0) """, project_id, dt, dt, uid, uid_name)
                        if cq_department_id!="0":     
                            result = self.db.execute("update t_projects set project_department_id=%s, project_department_id_name=%s where id=%s",cq_department_id,cq_department_id_name,project_id)
                        for arr in  row["cq_arr"]: 
                            member_name = arr["member_name"]
                            btype_id =  arr["cq_btype_id"]
                            team_id = arr["team_id"]
                            if member_name  and btype_id !="0":
                                t_user = self.db.get('select * from t_user where name=%s', member_name)
                                if not t_user:
                                    return self.write("订单处理人不存在,请检查名字是否有误.")
                                user_uid_name = t_user.name
                                member_id = t_user.id
                                btype_id_name =  arr["cq_btype_id_name"]
                                t_income_type = self.db.get('select * from t_projects_type where id=%s', team_id)                           
                                not_transition = 0
                                # if user_uid_name == u"不流转（外资）" or user_uid_name == u"不流转（其他）" or user_uid_name == u"不流转（跑腿）" or user_uid_name == u"不流转（记账）" or user_uid_name == u"不流转（调整）" or user_uid_name == u"不流转（商标）" or user_uid_name == u"调整单(无需流转)" or user_uid_name == u"不流转（刻章）":
                                if t_user.not_process==1:
                                    not_transition = 1
                                    milepost.income_name = "无需流转"
                                    milepost.id = "0"

                                if btype_id_name == u"公司注册":
                                    self.db.execute("update t_projects set reg_state=1 where id=%s",project_id)
                                id = self.db.execute("""
                                                INSERT INTO `t_projects_member`
                                                (`team_id`,
                                                `team_name`,
                                                `member_id`,
                                                `created_at`,
                                                `project_id`,
                                                `guid`,
                                                `member_name`,
                                                `updated_at`,
                                                `updated_uid`,
                                                `updated_uid_name`,`btype_id`,`btype_id_name`,last_milepost_id_name,last_milepost_id,last_milepost_id_at,not_transition)

                                                values(%s,%s,%s,%s,%s,uuid(),%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)""", team_id, t_income_type.income_name,
                                                    t_user.id, dt, project_id,
                                                    t_user.name,dt, uid, uid_name, btype_id,
                                                    btype_id_name, milepost.income_name,
                                                    milepost.id, dt, not_transition)
                                    
                                if id > 0 and not_transition == 0 :
                                    team_mile_sql=""
                                    print "team_id",team_id,type(team_id)
                                    if team_id==205:
                                        team_mile_sql = " and order_int in (1,2,3,8)"
                                    self.db.execute("""INSERT INTO `t_projects_milepost`
                                                        (
                                                        `project_id`,
                                                        `is_lock`,
                                                        `confirm_at`,
                                                        `uid`,
                                                        `uid_name`,
                                                        `guid`,
                                                        `created_at`,
                                                        `updated_at`,
                                                        `remark`,
                                                        `type_name`,
                                                        `type_id`,
                                                        `btype_name`,
                                                        `btype_id`,
                                                        `order_int`,member_id)

                                                        SELECT %s,0,NULL,%s,%s,UUID(),now(),NOW(),NULL,income_name,id,%s,%s,order_int,%s

                                                        FROM `t_projects_type` where income_category='办结' """+team_mile_sql, project_id, member_id, user_uid_name,
                                                            btype_id_name, btype_id, id)
                                    self.db.execute(
                                        "update t_projects_milepost set confirm_at=%s where project_id=%s  and member_id=%s order by order_int  limit 1",
                                        dt, project_id, id)

                return self.write("0")

        elif tag=="add_member":
            member_id = self.get_argument("member_id")
            guid = self.get_argument("guid")
            project_id = self.get_argument("project_id")
            cannot_update=self.get_argument('cannot_update','')
            customer_id=self.get_argument('customer_id','0')
            if not project_id:
                self.write("not projectid")
            elif not member_id:
                self.write("not memberid")
            else:
                t_user = self.db.get('select * from t_user where id=%s', member_id)
                t_project = self.db.get("select * from t_projects where id=%s ",project_id)
                if not t_project:
                    self.write("not project ")
                else:
                    tpm = self.db.get("select * from t_projects_member where guid=%s and project_id=%s ",guid,project_id)
                    if not tpm:
                        self.write("not member team")
                    else:

                        if int(member_id
                                ) == 0 and tpm.member_id > 0 or tpm.member_id != int(member_id
                                ) :
                            msg.insert_new(
                                self, tpm.member_id,
                                u"[系统信息] 您好 %s将您从项目[%s]角色移除 %s  <a href='/project?tag=show&guid=%s&id=%s'>查看</a>"
                                % (uid_name.decode('utf8'), t_project.project_name,
                                tpm.team_name, t_project.guid, t_project.id), 1)
                        if int(
                                member_id
                        ) > 0 and tpm.member_id == 0 or tpm.member_id != int(
                                member_id):
                            msg.insert_new(
                                self, member_id,
                                u"[系统信息] 您好,%s将您设置为[%s]项目角色:%s <a href='/project?tag=show&guid=%s&id=%s'>查看</a>"
                                % (uid_name.decode('utf8'),
                                    t_project.project_name, tpm.team_name,
                                    t_project.guid, t_project.id), 1)
                        if t_user:
                            sql=""" ,updated_at=now() """
                            if cannot_update=='1':
                                sql=''
                            id = self.db.execute("""
                                            update t_projects_member set member_id=%s,updated_uid=%s,updated_uid_name=%s,member_name=%s """+sql+"""
                                            where guid=%s and project_id=%s
                                        """, member_id, uid, uid_name, t_user.name,
                                                 guid, project_id)
                        else:
                            self.db.execute("""
                                            update t_projects_member set member_id=%s,updated_uid=%s,updated_uid_name=%s,member_name='',updated_at=%s
                                            where guid=%s and project_id=%s
                                        """, member_id, uid, uid_name,dt,
                                                 guid, project_id)
                        if tpm.member_id!=int(member_id):
                            events.add_project_event(self,project_id,'业务相关人员(确认单'+project_id+')',
                            tpm.team_name+':'+tpm.member_name+' 修改为 '+t_user.name,uid,uid_name,customer_id)        
                        self.write("0")


        # elif  tag=="add_income":
        #     body = self.get_argument("body")
        #     data = json.loads(body)
        #     project_id = self.get_argument("project_id")
        #     pay_type_name = self.get_argument("pay_type_name")
        #     pay_type_id = self.get_argument("pay_type_id")
        #     company_id = self.get_argument("company_id")
        #     company_id_name = self.get_argument("company_id_name")

        #     guid = uuid.uuid4()
        #     title_id = self.db.execute("""
        #             insert into t_projects_income_title (project_id,income_title,total,
        #             created_at,updated_at,uid,uid_name,guid,pay_type_name,pay_type_id,company_id,company_id_name)
        #             values(%s,%s,0,now(),now(),%s,%s,uuid(),%s,%s,%s,%s)
        #         """, project_id, "", uid, uid_name, pay_type_name, pay_type_id,
        #                                company_id, company_id_name)


        #     for item in data:
        #         if item:
        #             try:
        #                 return_income_id = self.db.execute(
        #                     """insert into t_projects_income(project_id,
        #                     income_name,income_money,uid,uid_name,guid,
        #                     created_at,updated_at,remark,income_id,parent_id,income_num)
        #                     values(%s,%s,%s,%s,%s,%s,now(),now(),%s,%s,%s,%s)
        #                     """, project_id, item["income_name"],
        #                     item["income_money"], uid, uid_name, guid,
        #                     item["remark"], item["income_id"], title_id,
        #                     item["income_num"])


        #             except :
        #                 pass

        #         # return_income_id = self.db.execute(
        #         #     """insert into t_projects_income(project_id,
        #         # income_name,income_money,is_lock,uid,guid,
        #         # created_at,updated_at,remark,income_id,company_id,company_name,
        #         # pay_type_id,pay_type_name,income_at,is_other,income_num,parent_id)
        #         # values(%s,%s,%s,0,%s,%s,now(),now(),%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
        #         # """, project_id, item.income_name, income_money, uid, guid,
        #         #     remark, income_id, company_id, company_name, pay_type_id,
        #         #     pay_type_name, income_at, is_other, income_num, title_id)

        #     self.write(body)

        # project_id  = self.get_argument("project_id")
        # income_name = self.get_argument("income_name")
        # income_num = self.get_argument("income_num")
        # income_id = self.get_argument("income_id")
        # income_money = self.get_argument("income_money")
        # guid = uuid.uuid4()
        # remark = self.get_argument("remark","")
        # is_other = self.get_argument("is_other")
        # pay_type_id = self.get_argument("pay_type_id")
        # pay_type_name = self.get_argument("pay_type_name")
        # company_id = self.get_argument('company_id')
        # company_name = self.get_argument("company_name")
        # income_at = self.get_argument("income_at")
        # parent_id = self.get_argument("parent_id")
        # if not  project_id:
        #     self.write("not projectid")
        # else:
        #     t_project = self.db.get("select * from t_projects where id=%s",project_id)
        #     if not t_project:
        #         self.write("not project")
        #     else:

        #         title_id = self.db.execute("""
        #             insert into t_projects_income_title (project_id,income_title,total,is_ok,
        #             created_at,updated_at,uid,uid_name)
        #             values(%s,%s,0,0,now(),now(),%s,%s)
        #         """,project_id,)
        #         return_income_id = self.db.execute(
        #             """
        #         insert into t_projects_income(project_id,
        #         income_name,income_money,is_lock,uid,guid,
        #         created_at,updated_at,remark,income_id,company_id,company_name,
        #         pay_type_id,pay_type_name,income_at,is_other,income_num,parent_id)
        #         values(%s,%s,%s,0,%s,%s,now(),now(),%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
        #         """, project_id, income_name, income_money, uid, guid,
        #             remark, income_id, company_id, company_name,
        #             pay_type_id, pay_type_name, income_at, is_other,
        #             income_num, parent_id)
        #         if return_income_id > 0:
        #             result = self.db.execute("""
        #             insert into t_projects_income_state (
        #                         project_id,
        #                         project_income_id,
        #                         income_state,
        #                         income_state_id,
        #                         uid,
        #                         created_at,
        #                         uid_name)
        #             select %s,%s,income_name,id,0,now(),'' from t_projects_type
        #             where income_category='财务确认'   order by order_int desc
        #             """, project_id, return_income_id)
        #             if int(is_other)==0 and int(income_id)==40:#更新定金
        #                 result = self.db.execute("""
        #                     update t_projects set true_income=(
        #                              select ifnull(sum(income_money),0)
        #                               from  t_projects_income  where
        #                               project_id=%s
        #
        #                               and  income_id=40

        #                         ) where id=%s
        #                         """, project_id, project_id)

        #             if result > 0 :
        #                 role= 2
        #                 msg.insert_new_group(
        #                     self,
        #                     u"[审核信息] 您好 %s已经为[%s]新增一笔 %s元到款，请审核。 <a href='/project?tag=show&guid=%s&id=%s'>查看</a>"
        #                     % (uid_name.decode('utf8'), t_project.project_name,income_money,
        #                     t_project.guid,
        #                     project_id), 2, role)


        #         self.write(str(return_income_id))

        # elif  tag=="add_income":
        #     project_id  = self.get_argument("project_id")
        #     income_name = self.get_argument("income_name")
        #     income_id = self.get_argument("income_id")
        #     income_money = self.get_argument("income_money")
        #     guid = uuid.uuid4()
        #     remark = self.get_argument("remark","")
        #     is_other = self.get_argument("is_other")
        #     pay_type_id = self.get_argument("pay_type_id")
        #     pay_type_name = self.get_argument("pay_type_name")
        #     company_id = self.get_argument('company_id')
        #     company_name = self.get_argument("company_name")
        #     income_at = self.get_argument("income_at")
        #     if not  project_id:
        #         self.write("not projectid")
        #     elif not income_money:
        #         self.write("not income money")
        #     elif not income_id:
        #         self.write("not income_id")
        #     else:
        #         t_project = self.db.get("select * from t_projects where id=%s",project_id)
        #         if not t_project:
        #             self.write("not project")
        #         else:
        #             return_income_id = self.db.execute("""
        #             insert into t_projects_income(project_id,
        #             income_name,income_money,is_lock,uid,guid,
        #             created_at,updated_at,remark,income_id,company_id,company_name,
        #             pay_type_id,pay_type_name,income_at,is_other)
        #             values(%s,%s,%s,0,%s,%s,now(),now(),%s,%s,%s,%s,%s,%s,%s,%s)
        #             """, project_id, income_name, income_money, uid, guid, remark,
        #                                 income_id, company_id, company_name,
        #                                 pay_type_id, pay_type_name, income_at,
        #                                 is_other)
        #             if return_income_id > 0:
        #                 result = self.db.execute("""
        #                 insert into t_projects_income_state (
        #                             project_id,
        #                             project_income_id,
        #                             income_state,
        #                             income_state_id,
        #                             uid,
        #                             created_at,
        #                             uid_name)
        #                 select %s,%s,income_name,id,0,now(),'' from t_projects_type
        #                 where income_category='财务确认'   order by order_int desc
        #                 """, project_id, return_income_id)
        #                 if int(is_other)==0 and int(income_id)==40:#更新定金
        #                     result = self.db.execute("""
        #                         update t_projects set true_income=(
        #                                  select ifnull(sum(income_money),0)
        #                                   from  t_projects_income  where
        #                                   project_id=%s
        #
        #                                   and  income_id=40

        #                             ) where id=%s
        #                             """, project_id, project_id)

        #                 if result > 0 :
        #                     role= 2
        #                     msg.insert_new_group(
        #                         self,
        #                         u"[审核信息] 您好 %s已经为[%s]新增一笔 %s元到款，请审核。 <a href='/project?tag=show&guid=%s&id=%s'>查看</a>"
        #                         % (uid_name.decode('utf8'), t_project.project_name,income_money,
        #                         t_project.guid,
        #                         project_id), 2, role)


        #             self.write(str(return_income_id))
        elif tag == "delete_income":
            project_guid = self.get_argument("project_guid")
            id = self.get_argument("id")
            guid = self.get_argument("guid")
            project_id = self.get_argument("project_id")

            t_project = self.db.get("select * from t_projects where id=%s and guid=%s",project_id,project_guid)
            if not t_project:
                self.write("not project")
            else:
                result = 100
                return_result =  self.db.execute("delete from t_projects_income_title where id=%s and guid=%s",id,guid)
                if return_result==0:
                    result = self.db.execute("delete from t_projects_income where parent_id=%s",id)
                    if result == 0:
                        result = self.db.execute("delete from t_projects_income_detail where title_id=%s",id)

                self.write(str(result))
        elif tag == "modify_income":
            project_id = self.get_argument("project_id")
            income_name = self.get_argument("income_name")
            income_id = self.get_argument("income_id")
            income_money = self.get_argument("income_money")
            guid = self.get_argument("project_guid")
            remark = self.get_argument("remark", "")
            is_other = self.get_argument("is_other")
            pay_type_id = self.get_argument("pay_type_id")
            pay_type_name = self.get_argument("pay_type_name")
            company_id = self.get_argument('company_id')
            company_name = self.get_argument("company_name")
            income_at = self.get_argument("income_at")
            id = self.get_argument("id")
            guid = self.get_argument("guid")

            if not project_id:
                self.write("not projectid")
            elif not income_money:
                self.write("not income money")
            elif not income_id:
                self.write("not income_id")
            else:
                t_project = self.db.get("select * from t_projects where id=%s",
                                        project_id)

                if not t_project:
                    self.write("not project")
                else:
                    return_income_id = self.db.execute(
                        """
                    update t_projects_income set
                    income_name=%s,income_money=%s,
                    updated_at=%s,remark=%s,
                    income_id=%s,
                    company_id=%s,
                    company_name=%s,
                    pay_type_id=%s,
                    pay_type_name=%s,
                    income_at=%s,is_other=%s
                    where id=%s and guid=%s
                    """, income_name, income_money,dt, remark, income_id,
                        company_id, company_name, pay_type_id, pay_type_name,
                        income_at, is_other, id, guid)
                    if return_income_id > 0:
                        result = self.db.execute("""
                        insert into t_projects_income_state (
                                    project_id,
                                    project_income_id,
                                    income_state,
                                    income_state_id,
                                    uid,
                                    created_at,
                                    uid_name)
                        select %s,%s,income_name,id,0,now(),'' from t_projects_type
                        where income_category='财务确认'   order by order_int desc
                        """, project_id, return_income_id)
                        if int(is_other) == 0 and int(income_id) == 40:  #更新定金
                            result = self.db.execute("""
                                update t_projects set true_income=(
                                         select ifnull(sum(income_money),0)
                                          from  t_projects_income  where
                                          project_id=%s

                                          and  income_id=40

                                    ) where id=%s
                                    """, project_id, project_id)

                        if result > 0:
                            role = 2
                            msg.insert_new_group(
                                self,
                                u"[审核信息] 您好 %s已经为[%s]新增一笔 %s元到款，请审核。 <a href='/project?tag=show&guid=%s&id=%s'>查看</a>"
                                % (uid_name.decode('utf8'),
                                   t_project.project_name, income_money,
                                   t_project.guid, project_id), 2, role)

                    self.write(str(return_income_id))
        elif tag=="confirm":
            guid = self.get_argument("title_guid")
            project_id = self.get_argument("project_id")
            title_id = self.get_argument("title_id")
            ctype = self.get_argument("ctype")
            if not guid and project_id:
                self.write("not guid/project_id")
            else:
                t_project = self.db.get("select * from t_projects where id=%s",
                                        project_id)
                if not t_project:
                    self.write("not project")
                else:

                    if ctype =="1":
                        returnid = self.db.execute(
                                """update  t_projects_income_title set income_uid=%s ,income_uid_name=%s,
                                income_uid_at=%s where project_id=%s and  guid=%s and  id=%s """
                            ,uid,uid_name,dt,project_id,guid,title_id
                            )
                        msg.insert_new(
                            self, t_project.uid,
                            u"[系统信息] 您好%s已为[%s]的一笔到款，进行最终确认。 <a href='/project?tag=show&guid=%s&id=%s'>查看</a>"
                            % (uid_name.decode('utf8'),
                               t_project.project_name, t_project.guid,
                               project_id), 1)

                    else:
                        returnid = self.db.execute(
                            """update  t_projects_income_title set fi_confirm_uid=%s ,fi_confirm_uid_name=%s,
                                fi_confirm_at=%s where project_id=%s and  guid=%s and  id=%s """,
                            uid, uid_name,dt, project_id, guid, title_id)
                        msg.insert_new(
                            self, t_project.uid,
                            u"[系统信息] 您好 %s已经为[%s]确认一笔到款，请等待财务最终于确认哦。 <a href='/project?tag=show&guid=%s&id=%s'>查看</a>"
                            % (

                                uid_name.decode('utf8'),
                                t_project.project_name,
                                t_project.guid,
                                project_id
                            ),1)


                        # self.db.execute("""
                        #  update t_projects set con_wait_income=(   select ifnull(sum(b.income_money),0) from t_projects_income_state a ,
                        #   t_projects_income b
                        #     where a.project_income_id=b.id and  a.project_id=%s and  income_state_id=49 and a.uid = 0 and b.is_other=0),
                        #     waitpay_other=( select ifnull(sum(b.income_money),0) from t_projects_income_state a , t_projects_income b
                        #     where a.project_income_id=b.id and  a.project_id=%s and  income_state_id=49 and a.uid = 0 and b.is_other=1)
                        #      where id=%s
                        # """, project_id, project_id, project_id) #待付款

                    if t_project.wait_set_state == 0 :
                        for item in self.db.query("select * from t_user where qc=1"):
                            msg.insert_new(
                                self, item.id,
                                u"[系统信息] 您好 - %s已经为[%s]确认第一笔到款，请设置跟单员哦。 <a href='/project?tag=show&guid=%s&id=%s'>查看</a>"
                                % ( uid_name.decode('utf8'),
                                t_project.project_name, t_project.guid,
                                project_id), 1)
                        self.db.execute(
                                "update t_projects set wait_set_state=1 where id=%s",
                                project_id)
                    self.db.execute("""
                             update t_projects set
                             all_income=(select ifnull(sum(service_money),0) from t_projects_service_income where project_id=%s),

                             con_wait_income=ifnull(all_income-(select ifnull(sum(income_money),0) from t_projects_income
                             a ,t_projects_income_title b where b.id=a.parent_id and a.project_id=%s
                             and income_uid >0 and a.income_id <= 43),0)

                                 where id=%s
                            """, project_id,
                                    project_id,
                                    project_id)
                    self.write(str(returnid))

        elif tag=="upload_file_info":
            guid = self.get_argument("guid")
            project_id = self.get_argument("project_id")
            origin_num = self.get_argument("origin_num",0)
            print_num = self.get_argument("print_num",0)
            remark = self.get_argument("id_remark", "")
            rec_num = self.get_argument("rec_num",0)
            chop_num = self.get_argument("chop_num",0)
            info_num = self.get_argument("info_num",0)
            id_number = self.get_argument("id_number","")
            file_path = None
            if not project_id:
                self.write("not project_id")
            else:
                is_upload = False
                try:
                    file1 = self.request.files['file'][0]
                    is_upload = True
                except:
                    pass
                if is_upload:
                    ori_filename = file1["filename"]
                    filename_full = options.upload_path + "/projectfile/%s/" % (
                        project_id)
                    url_path = "/static/projectfile/%s/" % (project_id)
                    try:
                        os.makedirs(filename_full)
                    except OSError:
                        if not os.path.isdir(filename_full):
                            raise
                    extension = os.path.splitext(ori_filename)[1]

                    uuid_str = str(uuid.uuid4())
                    fname = "{0}_{1}{2}".format(uuid_str, project_id,
                                                extension)

                    save_full_path = filename_full + fname
                    url_fname = "{0}{1}".format(url_path, fname)

                    output_file = open(save_full_path, 'w')
                    output_file.write(file1["body"])
                    file_path = url_fname
                result = self.db.execute("""
                        update t_projects_file set
                        origin_num=%s,print_num=%s,remark=%s, uid=%s,uid_name=%s,upload_at=%s,rec_num=%s,chop_num=%s,
                        file_path=%s,info_num=%s,id_number=%s

                        where guid=%s and project_id=%s

                """, origin_num, print_num, remark, uid, uid_name,dt, rec_num,
                                         chop_num, file_path, info_num,id_number, guid,
                                         project_id)
                self.write(str(0))
        elif tag=="upload":
            project_id = self.get_argument("project_id")

            file_type_id = self.get_argument("file_type_id")
            file_type_name = self.get_argument("file_type_name")
            file_type_cate_id = self.get_argument("file_type_cate_id")
            file_type_cate_name = self.get_argument("file_type_cate_name")
            file_path = None
            rec_num = self.get_argument("rec_num")
            if not project_id:
                self.write("not project_id")
            else:
                is_upload = False
                try:
                    file1 = self.request.files['file'][0]
                    is_upload =True
                except:
                    pass


                if is_upload:
                    ori_filename=file1["filename"]
                    filename_full = options.upload_path+"/projectfile/%s/"%(project_id)
                    url_path = "/static/projectfile/%s/" % (project_id)
                    try:
                        os.makedirs(filename_full)
                    except OSError:
                        if not os.path.isdir(filename_full):
                            raise
                    extension = os.path.splitext(ori_filename)[1]

                    uuid_str = str(uuid.uuid4())
                    fname = "{0}_{1}{2}".format(uuid_str,project_id,extension)

                    save_full_path = filename_full+fname
                    url_fname = "{0}{1}".format(url_path,fname)

                    output_file = open(save_full_path, 'w')
                    output_file.write(file1["body"])
                    file_path = url_fname
                guid= uuid.uuid4()
                result = self.db.execute("""
                            INSERT INTO `t_projects_file`
                                (`file_type_id`,
                                `file_type_name`,
                                `is_upload`,
                                `rec_num`,
                                `file_path`,
                                `uid`,
                                `uid_name`,
                                `file_type_cate_name`,
                                `file_type_cate_id`,upload_at,project_id,guid)
                            values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
                """, file_type_id, file_type_name, is_upload, rec_num,
                                         file_path, uid, uid_name,
                                         file_type_cate_name,
                                         file_type_cate_id,dt, project_id, guid)

                self.write(str(result))

        elif tag=="delete_file":
            file_id = self.get_argument("file_id")
            file_guid = self.get_argument("file_guid")
            if not file or not file_guid:
                self.write("-1000")
            else:
                t_projects_file = self.db.get('select * from t_projects_file where id=%s and guid=%s',file_id,file_guid)
                if t_projects_file:
                    if t_projects_file.file_path:
                        full_path = options.upload_path+t_projects_file.file_path
                        if os.path.isfile(full_path):
                            os.remove(full_path)
                    self.db.execute("delete from t_projects_file where id=%s and guid=%s",file_id,file_guid)
                    self.write("1")
                else:
                    self.write("0")
        elif tag == "add_state":
            state_id = self.get_argument("state_id")
            state_id_name = self.get_argument("state_id_name")
            state_remark = self.get_argument("state_remark")
            project_id = self.get_argument("project_id")
            curr_state_id = self.get_argument("curr_state_id")
            type_id = self.get_argument("type_id",0)
            customer_id=self.get_argument('customer_id','0')
            project_type=self.db.get('''
                select * from t_projects_type where income_category='业务分类' and ext_type_id <> 0
                 and ext_type_id1=%s''',type_id)
            if not state_id and not  state_id_name:
                self.write("not state_id or state_name ")
            else:
                if int(curr_state_id) > 0:
                    dt=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    result = self.db.execute("""
                        update  t_projects_state_msg set  state_id=%s,state_id_name=%s,state_remark=%s
                        ,uid=%s,uid_name=%s,updated_at=%s where id=%s and project_id=%s
                    """, state_id, state_id_name, state_remark, uid, uid_name,dt,
                                             curr_state_id, project_id)
                    events.add_project_event(self,project_id,'修改办理进度',project_type.income_name+' 修改为 '+state_id_name,uid,uid_name,customer_id)

                else:
                    dt=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    result = self.db.execute("""
                        insert into t_projects_state_msg(state_id,state_id_name,state_remark,project_id,
                        guid,uid,uid_name,created_at,type_id,p_type_id,p_type_name)
                        values(%s,%s,%s,%s,uuid(),%s,%s,%s,%s,%s,%s)
                    """, state_id, state_id_name, state_remark, project_id,
                                             uid, uid_name, dt,type_id,project_type.id,project_type.income_name)
                    if result>0:
                        if state_remark:
                            remark_add=',备注:'+state_remark
                        else:
                            remark_add=''
                        events.add_project_event(self,project_id,'新增办理进度','将'+project_type.income_name+'设置状态：'+state_id_name+remark_add,uid,uid_name,customer_id)

                t_project_member=self.db.get('''
                select mid from t_projects_member where team_name='工商专员'
                    and project_id=%s and btype_id=%s and member_name=%s
                ''',project_id,project_type.id,uid_name)
                print(project_id,project_type.id)
                if t_project_member:
                    if result>0:
                        self.db.execute('''
                        update t_projects_member set last_state_msg=%s,last_state_msg_at=%s,state_msg_ids=concat(state_msg_ids,%s),last_state_remark=%s where mid=%s
                    ''',state_id_name,dt,str(result)+',',state_remark,t_project_member.mid)
                    else:
                        self.db.execute('''
                        update t_projects_member set last_state_msg=%s,last_state_msg_at=%s,last_state_remark=%s where mid=%s
                    ''',state_id_name,dt,state_remark,t_project_member.mid)
                    self.set_statis(project_id,state_id_name,'')
                self.write(str(result))

        elif tag =="delete":
            curr_state_id = self.get_argument("curr_state_id")
            guid = self.get_argument("guid")
            project_id = self.get_argument("project_id")
            type_id = self.get_argument("type_id",0)
            customer_id=self.get_argument('customer_id','0')
            if not curr_state_id:
                self.write("not curr_state_id")
            else:
                project_type=self.db.get('''
                select * from t_projects_type where income_category='业务分类' and ext_type_id <> 0
                 and ext_type_id=%s''',type_id)
                t_project_member1=self.db.get('''
                select mid from t_projects_member a
                inner join t_projects_state_msg b on a.btype_id=b.p_type_id
                and b.uid_name=%s and b.id=%s and hour(timediff(now(),b.created_at))>=24
                 where team_name='工商专员'
                    and a.project_id=%s and btype_id=%s and member_name=%s
                ''',uid_name,curr_state_id,project_id,project_type.id,uid_name)
                if t_project_member1 and uid_name!='罗文波':
                    self.write('-100')
                else:
                    t_projects_state_msg=self.db.get(
                        ' select * from t_projects_state_msg where id=%s and guid=%s ',curr_state_id,guid)
                    result = self.db.execute("""
                            delete from t_projects_state_msg
                            where id=%s
                            and guid=%s
                            and project_id=%s
                    """,curr_state_id,guid,project_id)
                    if result==0:
                        events.add_project_event(self,project_id,'删除办理进度','删除 '+t_projects_state_msg.state_id_name+'('+t_projects_state_msg.p_type_name+')',uid,uid_name,customer_id)
                    t_project_member=self.db.get('''
                    select state_msg_ids,mid from t_projects_member where team_name='工商专员'
                        and project_id=%s and  member_name=%s and
                        state_msg_ids like "%%,'''+str(curr_state_id)+''',%%" or state_msg_ids REGEXP  "^'''+str(curr_state_id)+''',"
                    ''',project_id,uid_name)
                    if t_project_member:
                        if len(t_project_member.state_msg_ids.split(',')[:-1])>1:
                            if t_project_member.state_msg_ids.split(',')[:-1][-1]==str(curr_state_id):
                                t_projects_state_msg=self.db.get('''
                                select created_at,state_id_name,state_remark from t_projects_state_msg where id=%s
                                ''',t_project_member.state_msg_ids.split(',')[:-1][-2])
                                if t_projects_state_msg:
                                    self.db.execute('''
                                update t_projects_member set last_state_remark=%s,last_state_msg=%s,last_state_msg_at=%s,state_msg_ids=REPLACE(state_msg_ids,%s,'') where mid=%s
                            ''',t_projects_state_msg.state_remark,t_projects_state_msg.state_id_name,t_projects_state_msg.created_at,curr_state_id+',',t_project_member.mid)
                            else:
                                self.db.execute('''
                                update t_projects_member set state_msg_ids=REPLACE(state_msg_ids,%s,'') where mid=%s
                            ''',curr_state_id+',',t_project_member.mid)
                        else:
                            self.db.execute('''
                            update t_projects_member set state_remark=null,last_state_msg=null,last_state_msg_at=null,state_msg_ids='' where mid=%s
                        ''',t_project_member.mid)



                    self.write(str(result))

        elif tag=="not_print":
            uid=self.get_argument('uid')
            self.db.execute("""
                update t_projects_income_title set is_print=1 where id=%s
            """,uid)
        elif tag=="already_print":
            uid=self.get_argument('uid')
            self.db.execute("""
                update t_projects_income_title set is_print=0 where id=%s
            """,uid)
        elif tag=='add_project_money':
            caval=self.get_argument('caval') or int(0)
            ca=self.get_argument('ca')
            caid=self.get_argument('caid')
            caremark=self.get_argument('caremark','')
            shuikongpanval=self.get_argument('shuikongpanval') or int(0)
            shuikongpan=self.get_argument('shuikongpan')
            shuikongpanid=self.get_argument('shuikongpanid')
            shuikongpanremark=self.get_argument('shuikongpanremark','')
            yinhuashuival=self.get_argument('yinhuashuival') or int(0)
            yinhuashui=self.get_argument('yinhuashui')
            yinhuashuiid=self.get_argument('yinhuashuiid')
            yinhuashuiremark=self.get_argument('yinhuashuiremark','')
            fakuanval=self.get_argument('fakuanval') or int(0)
            fakuan=self.get_argument('fakuan')
            fakuanid=self.get_argument('fakuanid')
            fakuanremark=self.get_argument('fakuanremark','')
            otherval=self.get_argument('otherval') or int(0)
            other=self.get_argument('other')
            otherid=self.get_argument('otherid')
            otherremak=self.get_argument('otherremak','')
            tuikuan=self.get_argument('tuikuan')
            tuikuanval=self.get_argument('tuikuanval') or int(0)
            tuikuanid=self.get_argument('tuikuanid')
            tuikuanremark=self.get_argument('tuikuanremark','')

            project_id=int(self.get_argument('project_id'))

            is_exits=self.db.query('select * from t_projects_income_other where project_id=%s',project_id)

            is_exits_tuikuan=self.db.get('select * from t_projects_income_other where project_id=%s and income_name="退款" ',project_id)
            if is_exits:
                self.db.execute('''
                        update t_projects_income_other set income_money=%s,updated_at=%s,updated_uid=%s,updated_uid_name=%s,remark=%s
                        where project_id=%s and income_name='CA费用'
                    ''',caval,dt,uid,uid_name,caremark,project_id)
                self.db.execute('''
                        update t_projects_income_other set income_money=%s,updated_at=%s,updated_uid=%s,updated_uid_name=%s,remark=%s
                        where project_id=%s and income_name='税控盘'
                    ''',shuikongpanval,dt,uid,uid_name,shuikongpanremark,project_id)
                self.db.execute('''
                        update t_projects_income_other set income_money=%s,updated_at=%s,updated_uid=%s,updated_uid_name=%s,remark=%s
                        where project_id=%s and income_name='印花税'
                    ''',yinhuashuival,dt,uid,uid_name,yinhuashuiremark,project_id)
                self.db.execute('''
                        update t_projects_income_other set income_money=%s,updated_at=%s,updated_uid=%s,updated_uid_name=%s,remark=%s
                        where project_id=%s and income_name='罚款'
                    ''',fakuanval,dt,uid,uid_name,fakuanremark,project_id)
                self.db.execute('''
                        update t_projects_income_other set income_money=%s,updated_at=%s,updated_uid=%s,updated_uid_name=%s,remark=%s
                        where project_id=%s and income_name='其他'
                    ''',otherval,dt,uid,uid_name,otherremak,project_id)
                if is_exits_tuikuan:
                    self.db.execute('''
                        update t_projects_income_other set income_money=%s,updated_at=%s,updated_uid=%s,updated_uid_name=%s,remark=%s
                        where project_id=%s and income_name='退款'
                    ''',tuikuanval,dt,uid,uid_name,tuikuanremark,project_id)
                else:
                    self.db.execute(
                        '''
                        insert into t_projects_income_other
                        (project_id,income_id,income_name,income_money,created_at,
                        uid,uid_name,remark
                        ) values(%s,%s,%s,%s,%s,%s,%s,%s)
                    ''',project_id,tuikuanid,tuikuan,tuikuanval,dt,uid,uid_name,tuikuanremark)

            else:
                self.db.execute(
                        '''
                        insert into t_projects_income_other(project_id,income_id,income_name,income_money,created_at,
                        uid,uid_name,remark) values(%s,%s,%s,%s,%s,%s,%s,%s)
                    ''',project_id,caid,ca,caval,dt,uid,uid_name,caremark)

                self.db.execute(
                        '''
                        insert into t_projects_income_other
                        (project_id,income_id,income_name,income_money,created_at,
                        uid,uid_name,remark
                        ) values(%s,%s,%s,%s,%s,%s,%s,%s)
                    ''',project_id,shuikongpanid,shuikongpan,shuikongpanval,dt,uid,uid_name,shuikongpanremark)

                self.db.execute(
                        '''
                        insert into t_projects_income_other
                        (project_id,income_id,income_name,income_money,created_at,
                        uid,uid_name,remark
                        ) values(%s,%s,%s,%s,%s,%s,%s,%s)
                    ''',project_id,yinhuashuiid,yinhuashui,yinhuashuival,dt,uid,uid_name,yinhuashuiremark)

                self.db.execute(
                        '''
                        insert into t_projects_income_other
                        (project_id,income_id,income_name,income_money,created_at,
                        uid,uid_name,remark
                        ) values(%s,%s,%s,%s,%s,%s,%s,%s)
                    ''',project_id,fakuanid,fakuan,fakuanval,dt,uid,uid_name,fakuanremark)


                self.db.execute(
                        '''
                        insert into t_projects_income_other
                        (project_id,income_id,income_name,income_money,created_at,
                        uid,uid_name,remark
                        ) values(%s,%s,%s,%s,%s,%s,%s,%s)
                    ''',project_id,otherid,other,otherval,dt,uid,uid_name,otherremak)

                self.db.execute(
                        '''
                        insert into t_projects_income_other
                        (project_id,income_id,income_name,income_money,created_at,
                        uid,uid_name,remark
                        ) values(%s,%s,%s,%s,%s,%s,%s,%s)
                    ''',project_id,tuikuanid,tuikuan,tuikuanval,dt,uid,uid_name,tuikuanremark)

        elif tag=='add':
            project_id=self.get_argument('project_id')
            tel=self.get_argument( "tel")
            name=self.get_argument("name")
            remark=self.get_argument("remark")
            gender=int(self.get_argument("gender"))
            linkman_id=self.get_argument("linkman_id")
            customer_id=self.get_argument('customer_id','0')
            txt=''
            if linkman_id!='None':
                t_projects_linkman=self.db.get(
                    ' select * from t_projects_linkman where id=%s ',linkman_id)
                self.db.execute(
                    """
                    update t_projects_linkman set name=%s,
                    tel=%s,remark=%s,gender=%s,uid_name=%s,uid=%s,updated_at=%s,project_id=%s where id=%s
                    """,name,tel,remark,gender,uid_name,uid,dt,project_id,int(linkman_id)
                )
                if t_projects_linkman.name!=name:
                    txt+=',联系人:'+t_projects_linkman.name+' 修改为 '+name
                if t_projects_linkman.tel!=tel:
                    txt+=',联系电话:'+t_projects_linkman.tel+' 修改为 '+tel
                if txt:

                    events.add_project_event(self,project_id,'修改联系人(确认单'+project_id+')',
                    txt[1:]
                ,uid,uid_name,customer_id)
            else:
                self.db.execute(
                    '''
                    insert into t_projects_linkman
                    (name,tel,remark,gender,uid_name,uid,created_at,project_id)
                    values(%s,%s,%s,%s,%s,%s,%s,%s)
                    ''',name,tel,remark,gender,uid_name,uid,dt,project_id)
                events.add_project_event(self,project_id,'添加联系人(确认单'+project_id+')',
                '增加 联系人:'+name+' 联系电话:'+tel
                ,uid,uid_name,customer_id)
        elif tag=='delete_linkman':
            id=self.get_argument('id')
            project_id=self.get_argument('project_id','0')
            customer_id=self.get_argument('customer_id','0')
            t_projects_linkman=self.db.get(
                    ' select * from t_projects_linkman where id=%s ',id)
            result=self.db.execute(
                '''
                delete from t_projects_linkman where id=%s
                ''',id
            )
            if result==0:
                events.add_project_event(self,project_id,'删除联系人(确认单'+project_id+')',
                '删除 联系人:'+t_projects_linkman.name+' 联系电话:'+t_projects_linkman.tel
                ,uid,uid_name,customer_id)

        elif tag=='add_tran1':
            trans_remark=self.get_argument('trans_remark','')
            project_id=self.get_argument('project_id')
            customer_id=self.get_argument('customer_id','0')
            len1=int(self.get_argument('len'))
            is_upload = False
            file_path = None
            for i in range(len1):
                try:
                    file1 = self.request.files['file'+str(i)][0]
                    is_upload = True
                except:
                    pass
                if is_upload:
                    ori_filename = file1["filename"]
                    filename_full = options.upload_path + "/attachment/%s/" % (
                         str(datetime.datetime.now().strftime("%m")))
                    url_path = "/static/attachment/%s/" % (str(datetime.datetime.now().strftime("%m")))
                    try:
                        os.makedirs(filename_full)
                    except OSError:
                        if not os.path.isdir(filename_full):
                            raise

                    uuid_str = str(uuid.uuid4())
                    fname = "{0}".format(ori_filename)

                    save_full_path = filename_full + uuid_str+'_'+fname
                    url_fname = "{0}{1}".format(url_path, uuid_str+'_'+fname)

                    output_file = open(save_full_path, 'w')
                    output_file.write(file1["body"])
                    file_path = url_fname
                result=self.db.execute('''
                        insert into t_projects_transition_upload(file_name,created_at,uid,uid_name,remark,project_id)
                         values(%s,%s,%s,%s,%s,%s)
                    ''',file_path,dt,uid,uid_name,trans_remark,project_id)
                if result>0:
                    events.add_project_event(self,project_id, "上传附件(确认单"+project_id+")",'上传'+ori_filename,
                                         uid, uid_name,customer_id)

                # else:
                #     if file_path:
                #         self.db.execute('''
                #         update t_projects_transition_upload set remark=%s,file_name=%s where id=%s
                #     ''',trans_remark,file_path,transition_id)
                #     else:
                #         self.db.execute('''
                #         update t_projects_transition_upload set remark=%s where id=%s
                #     ''',trans_remark,transition_id)


        elif tag=='add_tran':
            mid = self.get_argument('mid', 0)
            tran_by=self.get_argument('tran_by',"")
            is_inner = int(self.get_argument('is_inner'))
            rec_by=self.get_argument('rec_by')
            tran_at=self.get_argument('tran_at')
            trans_remark=self.get_argument('trans_remark',"")
            transition_id=self.get_argument('transition_id')
            project_id=self.get_argument('project_id',0)
            use_type = self.get_argument('use_type')
            project_company_type=self.get_argument('project_company_type',1)
            company_id=self.get_argument('company_id',0)
            company_name=self.get_argument('company_name','')
            rec_by_uid = 0
            type_ids=self.get_argument('type_ids')
            type_names = self.get_argument('type_names')
            is_customer = self.get_argument("is_customer", 0)
            dir_id =project_id
            if not dir_id:
                dir_id = company_id

            if is_inner:
                t_user = self.db.get("select * from t_user where name=%s",rec_by)
                if t_user:
                    rec_by_uid = t_user.id
            file_path =''
            if is_inner and  not t_user:
                self.write("内部交接:签收用户不存在哦.")
            elif not rec_by:
                self.write("接收方的名字不能为空")
            else:
                for k,file1 in self.request.files.items():
                    is_upload = False
                    try:
                        file1 =file1[0]
                        is_upload = True
                    except:
                        pass
                    if is_upload:
                        ori_filename = file1["filename"]
                        filename_full = options.upload_path + "/customer/%s/" % (
                            dir_id)
                        url_path = "/static/customer/%s/" % (dir_id)
                        try:
                            os.makedirs(filename_full)
                        except OSError:
                            if not os.path.isdir(filename_full):
                                raise
                        extension = os.path.splitext(ori_filename)[1]

                        uuid_str = str(uuid.uuid4())
                        fname = "{0}_{1}{2}".format(uuid_str, dir_id, extension)

                        save_full_path = filename_full + fname
                        url_fname = "{0}{1}".format(url_path, fname)

                        output_file = open(save_full_path, 'w')
                        output_file.write(file1["body"])
                        file_path = url_fname
                if transition_id=='0':
                    result = self.db.execute(
                        '''
                        insert into t_projects_transition
                        (remark,file_name,created_at,tran_by,rec_by,tran_at,uid,uid_name,
                        is_inner,rec_by_uid,type_ids,type_names,use_type,project_company_type,company_id,is_customer,project_id,mid)
                        values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
                        ''', trans_remark, file_path,dt, tran_by, rec_by, tran_at,
                        uid, uid_name, is_inner, rec_by_uid, type_ids,
                        type_names, use_type, project_company_type, company_id,
                        is_customer, project_id, mid)
                    # else:
                    #     result = self.db.execute('''
                    #     insert into t_projects_transition
                    #     (remark,file_name,created_at,tran_by,rec_by,tran_at,uid,uid_name,
                    #     project_id,is_inner,rec_by_uid,type_ids,type_names,use_type,project_company_type)
                    #     values(%s,%s,now(),%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
                    #     ''', trans_remark, file_path, tran_by, rec_by, tran_at,
                    #                          uid, uid_name, project_id,
                    #                          is_inner, rec_by_uid,type_ids,type_names,use_type,project_company_type)
                    if result > 0 and is_inner:
                        if not self.db.get(
                                'select * from t_projects_member_other where project_id=%s and member_id=%s',
                                project_id, rec_by_uid):
                            self.db.execute("""
                                insert   into  t_projects_member_other(team_name,member_id,member_name,project_id,created_at)
                                    values(%s,%s,%s,%s,%s)

                                        """, u"外勤", rec_by_uid, rec_by,
                                            project_id,dt)
                    self.write(str(result))
                else:

                    result = 0
                    if file_path:
                        result = self.db.execute("""
                            update t_projects_transition set remark=%s,file_name=%s,tran_by=%s,rec_by=%s,tran_at=%s,uid=%s,uid_name=%s,
                            is_inner=%s,rec_by_uid=%s,type_ids=%s,type_names=%s,use_type=%s,project_company_type=%s,company_id=%s
                            where  id=%s
                            """, trans_remark, file_path, tran_by, rec_by,
                                                 tran_at, uid, uid_name,
                                                 is_inner, rec_by_uid,type_ids,type_names,use_type,
                                                 project_company_type,company_id,
                                                 transition_id)

                    else:
                        result = self.db.execute("""
                            update t_projects_transition set remark=%s,tran_by=%s,rec_by=%s,tran_at=%s,uid=%s,uid_name=%s,
                             is_inner=%s,rec_by_uid=%s,type_ids=%s,type_names=%s,use_type=%s
                            where  id=%s
                            """, trans_remark, tran_by, rec_by, tran_at, uid,
                                                 uid_name, is_inner,
                                                 rec_by_uid,type_ids,type_names,use_type,
                                                 transition_id)

                    if result == 0 and is_inner:
                        if not self.db.get(
                                'select * from t_projects_member_other where project_id=%s and member_id=%s',
                                project_id, rec_by_uid):
                            self.db.execute("""
                                insert   into  t_projects_member_other(team_name,member_id,member_name,project_id,created_at)
                                    values(%s,%s,%s,%s,%s)

                                        """, u"外勤", rec_by_uid, rec_by,
                                            project_id,dt)



                    self.write(str(result))

        elif tag=='delete_tran_upload':
            transition_id=self.get_argument('transition_id')
            project_id = self.get_argument('project_id')
            file_name=self.get_argument('file_name','')
            customer_id=self.get_argument('customer_id','0')
            if not transition_id:
                self.write("transition_id is null")
            elif not project_id:
                self.write("project is null")
            else:
                result = self.db.execute(
                    '''
                    delete from t_projects_transition_upload where id=%s and project_id=%s
                    ''',transition_id,project_id
                )
                if result==0:
                    events.add_project_event(self,project_id, "删除附件(确认单"+project_id+")", "删除附件"+file_name,
                                         uid, uid_name,customer_id)
                self.write(str(result))

        elif tag=='set_companyinfo':
            customer_company=self.get_argument("customer_company",'')
            company_uid=self.get_argument("company_uid","")
            company_person=self.get_argument("comany_person","")
            true_reg_addr=self.get_argument("true_reg_addr","")
            company_created_day=self.get_argument("company_created_day","")
            company_expired_day=self.get_argument("company_expired_day","")
            company_fever = self.get_argument("company_fever",'')
            project_id=self.get_argument('project_id')
            zone = self.get_argument("zone",'')
            city = self.get_argument("city",'')
            if not company_created_day:
                company_created_day = None

            if not company_expired_day :
                company_expired_day = None


            result = self.db.execute('''
                update t_projects set customer_company=%s,company_uid=%s,comany_person=%s,true_reg_addr=%s,
                company_created_day=%s,company_expired_day=%s,
                company_confirm_uid_name=%s,company_confirm_at=%s,company_confirm_uid=%s,city=%s , zone=%s,company_fever=%s where id=%s
            ''', customer_company, company_uid, company_person, true_reg_addr,company_created_day,company_expired_day,
                                     uid_name,dt, uid, city, zone, company_fever,
                                     project_id)
            self.write(str(result))
        elif tag == 'addto_customer':
            customer_company = self.get_argument("customer_company")
            company_uid = self.get_argument("company_uid", "")
            company_person = self.get_argument("comany_person", "")
            true_reg_addr = self.get_argument("true_reg_addr", "")
            company_created_day = self.get_argument("company_created_day")
            company_expired_day = self.get_argument("company_expired_day")
            company_fever = self.get_argument("company_fever")
            project_id = self.get_argument('project_id')
            zone = self.get_argument("zone")
            city = self.get_argument("city")
            result = ""
            if not company_created_day:
                company_created_day = None
            if not company_expired_day:
                company_expired_day = None

            if not customer_company:
                result = "公司名不能为空哦."
            elif not company_uid:
                result = "统一社会信用代码不能为空哦."
            elif not company_person:
                result = "法人不能为空哦."
            else:
                t_customer = self.db.get(
                    "select * from db_customer.`t_customer` where company=%s",
                    customer_company)
                t_customer_uid = self.db.get(
                    "select * from db_customer.`t_customer` where company_reguid=%s",
                    company_uid)

                if t_customer:
                    result = u"公司名( %s )已经存在,<a href='http://192.168.2.168:8888/customer?tag=show&id=%s&guid=%s' target='_blank'>查看</a>" % (
                        customer_company, t_customer.id, t_customer.guid)
                elif t_customer_uid:
                    result = u"统一社会信用代码( %s )已经存在,<a href='http://192.168.2.168:8888/customer?tag=show&id=%s&guid=%s'  target='_blank'>查看</a>" % (
                        company_uid, t_customer.id, t_customer.guid)

                else:
                    result = self.db.execute("""
                            INSERT INTO db_customer.`t_customer`
                                    (zone,city, company_reguid,
                                    `company`,
                                    `reg_addr`,

                                    `reg_person`,

                                    `created_at`,
                                    `updated_at`,
                                    `guid`,`reg_date`,`end_date`,uid,uid_name,is_fever)
                                    VALUES
                                    (%s,%s,%s,%s,%s,%s,%s,%s,uuid(),%s,%s,%s,%s,%s);

                            """, city, zone,company_uid,
                            customer_company, true_reg_addr,
                                            company_person,dt,dt,
                                            company_created_day, company_expired_day,
                                            uid, uid_name, company_fever)
                    if result > 0 :
                        result="ok"
                    else:
                        result="创建失败"
            self.write(result)
        elif tag=='relation_project':
            project_id=self.get_argument('project_id')
            other_project_id=self.get_argument('other_project_id')

            exit_relation=self.db.query(' select * from t_projects_parent where project_id=%s',other_project_id)
            if exit_relation:
                self.write('1')

            else:
                self.db.execute(
                '''
                insert into t_projects_parent(project_id,parent_id,created_at,uid,uid_name)
                values(%s,%s,%s,%s,%s)
                ''',other_project_id,project_id,dt,uid,uid_name
                )
        elif tag=='delete_relation_project':
            uid=int(self.get_argument('id'))
            project_id=self.get_argument('project_id')
            self.db.execute(
                '''
                delete from t_projects_parent where project_id=%s and parent_id=%s
                ''',uid,project_id)

        elif tag=='add_recode':
            recode=self.get_argument('recode')
            project_id=self.get_argument('project_id')
            dingjin=self.get_argument('dingjin') or 0
            money=self.get_argument('money') or 0
            rel_id=self.get_argument('rel_id')
            if rel_id=='0':

                self.db.execute(
                '''
                insert into t_projects_recode(recode,money,dingjin,created_at,uid,uid_name,project_id)
                 values(%s,%s,%s,%s,%s,%s,%s)
                ''',recode,money,dingjin,dt,uid,uid_name,project_id
                )
            else:
                self.db.execute(
                '''
                 update t_projects_recode set recode=%s,money=%s,dingjin=%s,uid=%s,uid_name=%s where id=%s
                ''',recode,money,dingjin,uid,uid_name,rel_id)

        elif tag=='delete_recode':
            id=self.get_argument('id')
            self.db.execute(
                '''
                    delete from t_projects_recode where id=%s
                ''',id
            )

        elif tag=='add_manage_addr':
            addr_type=self.get_argument('addr_type')
            addr_cp=self.get_argument('addr_cp')
            addr_price=self.get_argument('addr_price')
            addr_price_time=self.get_argument('addr_price_time')
            start_time=self.get_argument('start_time')
            expired_time=self.get_argument('expired_time')
            rel_id=self.get_argument('rel_id')
            project_id=self.get_argument('project_id')

            if rel_id=='0':
                self.db.execute(
                    '''
                    insert into t_projects_addr(addr_type,addr_cp,project_id,
                    addr_price,addr_price_time,start_time,expired_time,updated_at,created_at,uid,uid_name)
                    values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
                    ''',addr_type,addr_cp,project_id,addr_price,addr_price_time,start_time,expired_time,dt,dt,uid,uid_name
                    )
            else:
                self.db.execute(
                    """
                    update t_projects_addr set addr_type=%s,addr_cp=%s,addr_price=%s,addr_price_time=%s,start_time=%s,
                    expired_time=%s,updated_at=%s,uid=%s,uid_name=%s where id=%s
                    """,addr_type,addr_cp,addr_price,addr_price_time,start_time,expired_time,dt,uid,uid_name,int(rel_id)
                )

        elif tag=='delete_manage_addr':
            id=self.get_argument('id')
            self.db.execute(
                '''
                    delete from t_projects_addr where id=%s
                ''',id
            )

        elif tag=="add_role_allot":
            role_type_id=self.get_argument('role_type_id')
            user_ids=self.get_argument('user_ids')
            user_ids=user_ids.split(',')
            for u_uid in user_ids:
                self.db.execute(
                """
                insert into t_user_visible(uid,type_id,created_by,created_at)
                values(%s,%s,%s,%s)
                """,u_uid,role_type_id,uid,dt)

        elif tag=="delete_role_allot":
            role_type_id=self.get_argument('role_type_id')
            user_ids=self.get_argument('user_ids')
            user_ids=user_ids.split(',')
            for u_uid in user_ids:
                self.db.execute(
                """
                delete from t_user_visible where uid=%s and type_id=%s
                """,u_uid,role_type_id
                )
        elif tag == "project_note":
            note_content = self.get_argument('note_content','')
            project_id = self.get_argument('project_id','')
            note_id=self.get_argument('note_id','')
            is_cancel=self.get_argument('is_cancel','')
            is_check=self.get_argument('is_check',0)
            is_chengjiao=self.get_argument('is_chengjiao',0)
            customer_id=self.get_argument('customer_id','0')
            if is_cancel:
                result=self.db.execute('''
                    update t_projects_note set is_cancel=%s where id=%s
                ''',is_cancel,note_id)
            else:
                if note_id:
                    result=self.db.execute(
                        '''
                        update t_projects_note set msg=%s,uid=%s,uid_name=%s where id=%s
                        ''',note_content,uid,uid_name,note_id
                    )
                else:

                    result=self.db.execute("""
                    insert into t_projects_note(msg,creatd_at,uid,uid_name,project_id,is_check,is_chengjiao)
                    values(%s,%s,%s,%s,%s,%s,%s)
                    """, note_content,dt, uid, uid_name, project_id,is_check,is_chengjiao)
                    if result>0:
                        if is_check=='1':
                            txt=' (需要上级审核)'
                        else:
                            txt=''
                        if is_chengjiao=='1':
                            txt+='(成交事项)'
                        events.add_project_event(self,project_id,'新增交代事项',note_content+txt,
                        uid,uid_name,customer_id)

        elif tag == "delete_note":
            id = self.get_argument('id')
            self.db.execute("""
                delete from t_projects_note where id=%s
                """, id)
            self.db.execute(
                """
                delete from t_projects_note_confirm where note_id=%s
                """,id)

        elif tag=="reject":
            reject_remark=self.get_argument('reject_remark')
            project_id=self.get_argument('project_id')
            pm_id = self.get_argument("pm_id")
            mid = self.get_argument("mid")
            if not pm_id:
                self.write("not pmid")
            else:
                t_projects_type = self.db.get(
                        "select * from t_projects_type  where income_name='填写办结信息'"
                    )
                if not t_projects_type:
                    return self.write("not project_type")
                else:

                    result1 =self.db.execute(
                    '''
                    update t_projects_milepost set reject_remark=%s,confirm_at=NULL where member_id=%s and type_id=%s
                    ''',reject_remark,mid,t_projects_type.id)
                    if result1 == 0:
                        result = self.db.execute(
                        """update t_projects_member set last_milepost_id=%s ,
                         last_milepost_id_name=%s,
                         last_milepost_id_at=%s where mid=%s
                    and project_id=%s""", t_projects_type.id,
                        t_projects_type.income_name,dt, mid, project_id)
                self.write(str(result1))
        elif tag == 'reject_transfile':
            reject_remark = self.get_argument('reject_remark',"")
            pm_id = self.get_argument("pm_id")
            project_id = self.get_argument('project_id')
            mtype = self.get_argument("mtype")
            if not project_id:
                self.write("not project_id")
            elif not reject_remark:
                self.write("not reject_remark")
            elif not mtype:
                self.write("not mtype")
            else:
                t_projects_type = None
                if mtype=="1":
                    t_projects_type = self.db.get(
                        "select * from t_projects_type  where income_name='办结'"
                    )
                elif mtype=="2":
                    t_projects_type = self.db.get(
                        "select * from t_projects_type  where income_name='填写办结信息'"
                    )


                if t_projects_type:
                    self.db.execute(
                        """update t_projects_transfile set is_ok=1,fback_remark=%s where project_id=%s and pm_id=%s and mtype=%s""",
                        reject_remark, project_id, pm_id,mtype)
                    self.db.execute(
                        """update t_projects_member set last_milepost_id=%s , last_milepost_id_name=%s, last_milepost_id_at=%s where mid=%s
                    and project_id=%s""", t_projects_type.id,
                        t_projects_type.income_name,dt, pm_id, project_id)
                    if mtype=="1":
                        self.db.execute(
                        "update t_projects_milepost set confirm_at=%s where member_id=%s and project_id=%s  and order_int=4 ",
                        None, pm_id, project_id)
                    else:
                        self.db.execute(
                        "update t_projects_milepost set confirm_at=%s where member_id=%s and project_id=%s  and type_id=%s ",
                        None, pm_id, project_id, t_projects_type.id)

        elif tag=='update_project_type':
            numarr=self.get_argument('numarr')
            numarr=numarr.split(',')
            for item in numarr[::2]:
                self.db.execute('''
                    update t_projects_type set income_name=%s where id=%s
                ''',numarr[numarr.index(item)+1],item)

        elif tag=='insert_project_type':
            name=self.get_argument('name')
            self.db.execute("""
                insert into t_projects_type(income_name,income_category,order_int)
                 values(%s,'业务类型',%s)
            """,name,uid)

        elif tag=="projects_note_confirm":
            check_val=self.get_argument('check_val')
            check_val=check_val.split(',')
            for item in check_val:
                self.db.execute(
                    """
                    insert into t_projects_note_confirm(note_id,created_by,created_at,created_name)
                     values(%s,%s,%s,%s)
                    """,item,uid,dt,uid_name)

        elif tag=="add_project_transfile":
            type_ids=self.get_argument('type_ids')
            type_names=self.get_argument('type_names')
            project_id=self.get_argument('project_id')
            pm_id=self.get_argument('pm_id')
            mtype=self.get_argument("mtype")
            remark=self.get_argument('remark',"")
            is_exist_project_id=self.db.get('''
            select * from t_projects_transfile where project_id=%s and pm_id=%s and mtype=%s
            ''',project_id,pm_id,mtype)
            if is_exist_project_id:
                result = self.db.execute('''
                update t_projects_transfile set trans_type=%s,trans_type_txt=%s,pm_id=%s,uid=%s,remark=%s,created_at=%s where project_id=%s and
                pm_id=%s and mtype=%s
                ''',type_ids,type_names,pm_id,uid,remark,dt,project_id,pm_id,mtype)
            else:
                result = self.db.execute(
                ''' insert into t_projects_transfile(trans_type,trans_type_txt,project_id,pm_id,uid,remark,created_at,mtype)
                 values(%s,%s,%s,%s,%s,%s,%s,%s)''',type_ids,type_names,project_id,pm_id,uid,remark,dt,mtype)
            self.write(str(result))
        elif tag=="accept_project_transfile":
            project_id=self.get_argument('project_id')
            pm_id=self.get_argument('pm_id')
            mtype=self.get_argument("mtype")
            if not project_id:
                return self.write("projectid is null")
            elif not pm_id:
                return self.write(" pm_id is null")
            elif not mtype:
                return self.write("mtype is null")
            else:

                is_exist_project_id=self.db.get('''
                select * from t_projects_transfile where project_id=%s and pm_id=%s and mtype=%s
                ''',project_id,pm_id,mtype)
                if is_exist_project_id:
                    result = self.db.execute('''
                    update t_projects_transfile set cq_uid=%s,cq_uid_name=%s ,cq_uid_at=%s where project_id=%s and
                    pm_id=%s and mtype=%s
                    ''',uid,uid_name,dt,project_id,pm_id,mtype)
                    self.write(str(result))


        elif tag=="check_transfile":
            pm_id=self.get_argument('pm_id')
            project_id = self.get_argument('project_id')
            mtype = self.get_argument("mtype",1)
            check_type = self.get_argument("check_type","")
            if not project_id:
                return self.write("not project_id")
            elif not pm_id:
                return self.write("not pm_id")
            else:
                addsql=""
                if check_type=="1":
                    addsql=" and cq_uid <> 0 "

                is_exist_project_id=self.db.get('''
                select * from t_projects_transfile where project_id=%s and pm_id=%s and mtype=%s
                ''' + addsql ,project_id,pm_id,mtype)
                result = 0
                if is_exist_project_id:
                    result = 1

                self.write(str(result))



        elif tag=='confirm_transition':
            id=self.get_argument('id')
            rec_by_uid_at=self.get_argument('rec_by_uid_at')


            if rec_by_uid_at:
                self.db.execute('''
            update t_projects_transition set rec_by_uid_at=NULL where id=%s
            ''',id)
            else:
                self.db.execute('''
            update t_projects_transition set rec_by_uid_at=%s where id=%s
            ''',dt,id)

        elif tag=="check_note":
            all_is_check=self.get_argument('all_is_check','')
            project_id=self.get_argument('project_id','')
            customer_id=self.get_argument('customer_id','0')
            check_id_pass=self.get_argument('check_id_pass','')
            check_id_bouhui=self.get_argument('check_id_bouhui','')

            if check_id_pass:
                self.db.execute('''
                update t_projects_note_check set check_id=%s,check_name=%s,check_at=%s where id=%s
                ''',uid,uid_name,dt,check_id_pass)
                events.add_project_event(self,project_id,'审核交代事项(确认单'+project_id+')',
                        uid_name+'审核通过'
                        ,uid,uid_name,customer_id)
            elif check_id_bouhui:
                self.db.execute('''
                update t_projects_note_check set check_id=%s,check_name=%s,check_at=%s,state_id=1 where id=%s
                ''',uid,uid_name,dt,check_id_bouhui)
                events.add_project_event(self,project_id,'审核交代事项(确认单'+project_id+')',
                        uid_name+'驳回'
                        ,uid,uid_name,customer_id)
            else:
                all_is_check=all_is_check.split('-')
                for item in all_is_check:
                    item=item.split(',')
                    is_exist=self.db.query('''
                    select * from t_projects_note_check where note_id=%s
                    ''',item[0])
                    if is_exist:
                        result=self.db.execute('''
                            update t_projects_note_check set created_by=%s,created_name=%s,remark=%s,state_id=%s where note_id=%s
                        ''',uid,uid_name,item[2],item[1],item[0])
                    else:
                        result=self.db.execute('''
                            insert into t_projects_note_check(note_id,project_id,created_by,created_at,created_name,remark,state_id)
                            values(%s,%s,%s,%s,%s,%s,%s)
                        ''',item[0],project_id,uid,dt,uid_name,item[2],item[1])
                    if result>=0:
                        events.add_project_event(self,project_id,'审核交代事项(确认单'+project_id+')',
                        uid_name+'审核通过，待最终审核' if item[1]=='0' else uid_name+'驳回'
                        ,uid,uid_name,customer_id)
                    if item[1]=='1':
                        self.db.execute('''
                            delete from t_projects_note_confirm where note_id=%s
                        ''',item[0])

        elif tag=="add_update_todo":
            company=self.get_argument('company','')
            bs_area=self.get_argument('bs_area','')
            bs_address=self.get_argument('bs_address','')
            created_at=self.get_argument('created_at','')
            start_time=self.get_argument('start_time','')
            end_time=self.get_argument('end_time','')
            project_name=self.get_argument('project_name','')
            banshi_per=self.get_argument('banshi_per',None)
            remark=self.get_argument('remark','')
            id=self.get_argument('id','')
            id1=self.get_argument('id1','')
            leader_id = self.get_argument("leader_id","")
            leader_name = self.get_argument("leader_name","")
            project_zj=self.get_argument('project_zj','')
            todo_type = self.get_argument("todo_type",0)
            todo_tags=self.get_argument('todo_tags','')
            print(todo_tags)
            leader_sql=''
            if not banshi_per:
                banshi_per= None
            if id:
                self.db.execute('''update t_todo_arrange set project_zj=%s,updated_at=%s where id=%s''',project_zj,dt,id)
            elif id1:
                t_todo_arrange=self.db.get(''' select banshi_per from t_todo_arrange where id=%s''',id1)
                if t_todo_arrange.banshi_per!=banshi_per:
                    self.db.execute('''
                        update t_todo_arrange_status set created_at=null,updated_at=null where todo_id=%s
                    ''',id1)
                    self.db.execute(
                    '''
                    update t_todo_arrange set project_zj='' where id=%s
                ''',id1)
                if banshi_per:
                    leader_sql=' leader_distribute_at=now(), '
                self.db.execute(
                '''
                    update t_todo_arrange set '''+leader_sql+''' company=%s,bs_area=%s,bs_address=%s,project_name=%s,
                    banshi_per=%s,remark=%s,start_time=%s,end_time=%s,bl_date=%s,todo_tags=%s where id=%s
                ''',company,bs_area,bs_address,project_name,banshi_per,remark,start_time,end_time,created_at,todo_tags,id1)


            else:
                result = self.db.execute('''
                insert into t_todo_arrange(company,bs_area,bs_address,bl_date,created_at,project_name,responsible_per,
                banshi_per,remark,start_time,end_time,leader_id,leader_name,todo_type,todo_tags
                ) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
                ''', company, bs_area, bs_address, created_at,dt, project_name,
                                         uid_name, banshi_per, remark,
                                         start_time, end_time, leader_id,
                                         leader_name, todo_type,todo_tags)
                self.db.execute('''
                    insert into t_todo_arrange_status(todo_id) values(%s)
                ''',result)
                # print(result)

        elif tag=="delete_todo":
            todoid=self.get_argument('todoid')
            self.db.execute(' delete from t_todo_arrange where id=%s',todoid)

        elif tag=="confirm_todo":
            id=self.get_argument('id')
            bs=self.get_argument('bs','')
            fz=self.get_argument('fz','')
            dt=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            if bs:
                self.db.execute('''
                update t_todo_arrange_status set created_at=%s where todo_id=%s''',dt,id)
            elif fz:
                self.db.execute('''
                 update t_todo_arrange_status set  updated_at=%s where todo_id=%s
                ''',dt,id)
            t_todo_arrange_status=self.db.get('''
                select created_at,updated_at from t_todo_arrange_status where todo_id=%s
                ''',id)
            self.write({'created':str(t_todo_arrange_status.created_at),'updated':str(t_todo_arrange_status.updated_at)})

        elif tag=="add_bj_manage":
            area=self.get_argument('area','')
            project_type=self.get_argument('project_type','')
            price=self.get_argument('price','')
            is_kp_addr=self.get_argument('is_kp_addr','')
            is_fhq=self.get_argument('is_fhq','')
            invoice_limited=self.get_argument('invoice_limited','')
            note=self.get_argument('note','')
            bj_id=self.get_argument('bj_id','')
            delete_id=self.get_argument('delete_id','')
            if delete_id:
                self.db.execute('''
                delete from t_addr_provider_manage where id=%s
                ''',delete_id)
            # if bj_id:
            #     self.db.execute('''
            #         update t_bj_manage set is_kp_addr=%s,is_fhq=%s,area=%s,project_type=%s,
            #         invoice_limited=%s,note=%s,updated_at=%s where id=%s
            #     ''',is_kp_addr,is_fhq,area,project_type,invoice_limited,note,dt,bj_id)
            #     self.db.execute('''
            #     insert into t_bj_price_history(price,created_at,bj_mange_id,bj_uid,bj_name)
            #     values(%s,%s,%s,%s,%s)
            # ''',price,dt,bj_id,uid,uid_name)
            # else:
            #     result=self.db.execute('''
            # insert into t_bj_manage(is_kp_addr,is_fhq,area,project_type,invoice_limited,note,uid,uid_name,created_at)
            # values(%s,%s,%s,%s,%s,%s,%s,%s,%s)
            # ''',is_kp_addr,is_fhq,area,project_type,invoice_limited,note,uid,uid_name,dt)

            #     self.db.execute('''
            #     insert into t_bj_price_history(price,created_at,bj_mange_id,bj_uid,bj_name)
            #     values(%s,%s,%s,%s,%s)
            # ''',price,dt,result,uid,uid_name)

        elif tag=="provider_manage_order":
            id=self.get_argument('id')
            up_id=self.get_argument('up_id','')
            top_id=self.get_argument('top_id','')
            down_id=self.get_argument('down_id','')
            bottom_id=self.get_argument('bottom_id','')
            id1=0

            if up_id:
                id1=up_id
            elif top_id:
                id1=top_id
            elif down_id:
                id1=down_id
            elif bottom_id:
                id1=bottom_id
            if up_id or down_id:
                ud_provider_manage=self.db.get('''
                select order_at,order_int from t_addr_provider_manage where id=%s
                ''',id1)
                provider_manage=self.db.get('''
                select order_at,order_int from t_addr_provider_manage where id=%s
                ''',id)
                self.db.execute('''
                    update t_addr_provider_manage set
                    order_at=%s,order_int=%s where id=%s;
                    update t_addr_provider_manage set
                    order_at=%s,order_int=%s where id=%s;
                ''',ud_provider_manage.order_at,ud_provider_manage.order_int,id,
                provider_manage.order_at,provider_manage.order_int,id1)

            elif top_id or bottom_id:
                ud_provider_manage=self.db.get('''
                select order_at,order_int from t_addr_provider_manage where id=%s
                ''',id1)
                provider_manage=self.db.get('''
                select order_at,order_int from t_addr_provider_manage where id=%s
                ''',id)
                if bottom_id:
                    self.db.execute('''

                        update t_addr_provider_manage set
                        order_at=%s,order_int=%s where id=%s;
                    ''',ud_provider_manage.order_at,ud_provider_manage.order_int-1,id,
                    )
                elif top_id:
                    self.db.execute('''

                        update t_addr_provider_manage set
                        order_at=%s,order_int=%s where id=%s;
                    ''',ud_provider_manage.order_at,ud_provider_manage.order_int+1,id,
                    )



        elif tag=="provider_manage":
            is_gy_manage = self.get_secure_cookie("is_gy_manage")
            if is_gy_manage !="1":
                return self.write("0")
            kz_project=self.get_argument('kz_project','')
            kz_price=self.get_argument('kz_price','')
            kz=self.get_argument('kz','')
            kz_area=self.get_argument('kz_area','')
            addr_type=self.get_argument('addr_type','')
            price=self.get_argument('price','')
            provider=self.get_argument('provider','')
            remark=self.get_argument('remark','')
            proivde_end=self.get_argument('proivde_end','')
            danbao_matter=self.get_argument('danbao_matter','')
            addr_id=self.get_argument('addr_id','')
            kz_id=self.get_argument('kz_id','')
            area=self.get_argument('area','')
            fp_limit=self.get_argument('fp_limit','')
            a_type=self.get_argument('type','')
            addr_nature=self.get_argument('addr_nature','')
            cost_price=self.get_argument('cost_price','')
            register_price=self.get_argument('register_price','')
            same_area_change_price=self.get_argument('same_area_change_price','')
            dif_area_change_price=self.get_argument('dif_area_change_price','')
            address=self.get_argument('address','')
            business_scope_limit=self.get_argument('business_scope_limit','')
            accept_material=self.get_argument('accept_material','')
            lock=self.get_argument('lock','0')
            renew=self.get_argument('renew','0')
            manage_type=self.get_argument('manage_type','0')
            delete_id=self.get_argument('delete_id','')
            if kz:
                if kz_id:
                    self.db.execute(''' update t_kz_provider_manage set kz_project=%s,area=%s where id=%s''',kz_project,kz_area,kz_id)
                    self.db.execute('''
                     insert into t_kz_provider_history(price,created_at,kz_id,uid,uid_name)
                      values(%s,%s,%s,%s,%s)''',kz_price,dt,kz_id,uid,uid_name)
                else:
                    result=self.db.execute('''
                    insert into t_kz_provider_manage(area,kz_project,created_at,uid,uid_name)
                     values(%s,%s,%s,%s,%s)''',kz_area,kz_project,dt,uid,uid_name)
                    self.db.execute('''
                     insert into t_kz_provider_history(price,created_at,kz_id,uid,uid_name)
                      values(%s,%s,%s,%s,%s)''',kz_price,dt,result,uid,uid_name)
            else:
                if addr_id:
                    self.db.execute('''
                    update  t_addr_provider_manage set
                    fp_limit=%s,area=%s,provider=%s,danbao_matter=%s,type=%s,
                    addr_nature=%s,cost_price=%s,register_price=%s,same_area_change_price=%s,dif_area_change_price=%s,
                    address=%s,business_scope_limit=%s,accept_material=%s,is_lock=%s,is_renew=%s
                     where id=%s
                    ''',fp_limit,area,provider,danbao_matter,a_type,addr_nature,cost_price,register_price,
                        same_area_change_price,dif_area_change_price,address,business_scope_limit,accept_material,lock,renew,addr_id)

                    # self.db.execute('''
                    #  insert into t_addr_provider_history(price,created_at,addr_id,uid,uid_name)
                    #   values(%s,now(),%s,%s,%s)''',price,addr_id,uid,uid_name)
                elif delete_id:
                    self.db.execute('''
                    delete from t_addr_provider_manage where id=%s
                    ''',delete_id)
                else:
                    result=self.db.execute('''
                        insert into t_addr_provider_manage
                        (fp_limit,area,provider,created_at,order_at,uid,uid_name,danbao_matter,type,
                        addr_nature,cost_price,register_price,same_area_change_price,dif_area_change_price,
                        address,business_scope_limit,accept_material,is_lock,is_renew,manage_type)
                        values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
                    ''',fp_limit,area,provider,dt,dt,uid,uid_name,danbao_matter,a_type,addr_nature,cost_price,register_price,
                        same_area_change_price,dif_area_change_price,address,business_scope_limit,accept_material,lock,renew,manage_type)
                    # self.db.execute('''
                    #  insert into t_addr_provider_history(price,created_at,addr_id,uid,uid_name)
                    #   values(%s,now(),%s,%s,%s)''',price,result,uid,uid_name)


        elif tag=="add_addr":
            addr_start_time=self.get_argument('addr_start_time','')
            addr_end_time=self.get_argument('addr_end_time','')
            addr_shoufei=self.get_argument('addr_shoufei','')
            project_id=self.get_argument('project_id','')
            addr_id=self.get_argument('addr_id','')
            project_addr_id=self.get_argument('project_addr_id','')
            confirm_id=self.get_argument('confirm_id','')
            addr_milepost_id=self.get_argument('addr_milepost_id','')
            addr_provider_id=self.get_argument('addr_provider_id','')
            customer_id=self.get_argument('customer_id','0')
            if project_addr_id:
                self.db.execute('''
                update t_projects_addr_provider set addr_start_time=%s,addr_end_time=%s,
                addr_shoufei=%s where id=%s''',addr_start_time,addr_end_time,addr_shoufei,project_addr_id)
            elif confirm_id:
                self.db.execute('''
                update t_projects_addr_provider set caiwu_confirm=1,confirm_time=%s,
                confirm_name=%s where id=%s''',dt,uid_name,confirm_id)
            else:
                self.db.execute(
                    """
                    update t_projects_addr_milepost set confirm_at=%s where id=%s
                    """,dt,addr_milepost_id)
                self.db.execute('''
                    insert into t_projects_addr_milepost(uid,uid_name,project_id,created_at,type_name,addr_provider_id)
                     values(%s,%s,%s,%s,%s,%s)
                    ''',uid,uid_name,project_id,dt,'安排完成',addr_provider_id)
                
                self.db.execute('''
                update t_projects_addr_provider set addr_start_time=%s,addr_end_time=%s,created_at=%s,
                addr_shoufei=%s,addr_id=%s where id=%s''',
                addr_start_time,addr_end_time,dt,addr_shoufei,addr_id,addr_provider_id)
                events.add_project_event(self,project_id,'安排地址(确认单'+project_id+')','安排地址完成',uid,uid_name,customer_id)

        elif tag=="add_addr_milepost":
            project_id=self.get_argument('project_id','')
            addr_provider_id=self.get_argument('addr_provider_id','')
            customer_id=self.get_argument('customer_id','0')
            remark=self.get_argument('remark','')
            id=self.get_argument('id','')
            step=self.get_argument('step')
            txt=''    
            if step=='1':
                result=self.db.execute('''
                insert t_projects_addr_provider(uid,uid_name,project_id)
                 values(%s,%s,%s)
                ''',uid,uid_name,project_id)
                self.db.execute(
                '''
                insert into t_projects_addr_milepost(project_id,created_at,type_name,addr_provider_id)
                values(%s,%s,%s,%s)
                ''',project_id,dt,'待接单',result)
                txt='请求安排地址'
            elif step=='2':
                self.db.execute("""
                    update t_projects_addr_provider set fz_id=%s,fz_name=%s where id=%s
                """,uid,uid_name,addr_provider_id)
                self.db.execute(
                    """
                    update t_projects_addr_milepost set uid=%s,uid_name=%s,confirm_at=%s  where id=%s
                    """,uid,uid_name,dt,id)
                self.db.execute(
                '''
                insert into t_projects_addr_milepost(uid,uid_name,project_id,created_at,type_name,addr_provider_id)
                values(%s,%s,%s,%s,%s,%s)
                ''',uid,uid_name,project_id,dt,'安排中',addr_provider_id)
                txt='确认接单'
            elif step=='3':
                self.db.execute(
                    """
                    update t_projects_addr_milepost set remark=%s where id=%s
                    """,remark,id)
            elif step=='4':
                self.db.execute("""
                delete from t_projects_addr_provider where id=%s
                """,id)
                projects_addr_provider=self.db.get('''
                    select a.*,b.area,b.addr_type,b.provider,b.danbao_matter,
                    b.fp_limit from t_projects_addr_provider a
                    left join t_addr_provider_manage b
                    on a.addr_id=b.id
                     where project_id=%s order by a.created_at desc limit 1
                ''',project_id)
                txt='删除地址安排'
                self.write({'addr_provider':projects_addr_provider})
            events.add_project_event(self,project_id,'安排地址',txt,uid,uid_name,customer_id)

        elif tag=="xiezhu_apply":
            project_id=self.get_argument('project_id','')
            content=self.get_argument('content','')
            gs_uid_name=self.get_argument('gs_uid_name','')
            gs_uid=self.get_argument('gs_uid','')
            xiezhu_id=self.get_argument('xiezhu_id','')
            gs_id=self.get_argument('gs_id','')
            xs_id=self.get_argument('xs_id','')
            sh_id=self.get_argument('sh_id','')
            queren_id=self.get_argument('queren_id','')
            is_pass=self.get_argument('is_pass','')
            fenpei_xs_id=self.get_argument('fenpei_xs_id','')
            fenpei_xs_name=self.get_argument('fenpei_xs_name','')
            xiezhu_zj=self.get_argument('xiezhu_zj','')
            remark=self.get_argument('remark','')
            step=self.get_argument('step','')
            customer_id=self.get_argument('customer_id','0')
            txt=''
            if step=='1':
                if xiezhu_id:
                    is_confirm_at=self.db.get('''
                        select confirm_at,is_pass from t_xiezhu_apply_milepost where id=%s
                    ''',gs_id)
                    if is_confirm_at.confirm_at:
                        self.write('1')
                    elif is_confirm_at.is_pass==0:
                        self.db.execute(''' update t_xiezhu_apply_milepost set is_pass=null where id=%s''',gs_id)
                        self.db.execute('''
                    update t_xiezhu_apply set xiezhu_content=%s where id=%s
                    ''',content,xiezhu_id)
                    else:
                        self.db.execute('''
                    update t_xiezhu_apply set xiezhu_content=%s where id=%s
                    ''',content,xiezhu_id)
                else:
                    result=self.db.execute('''
             insert into t_xiezhu_apply(xiezhu_content,project_id,created_at)
              values(%s,%s,%s)
            ''',content,project_id,dt)

                    self.db.execute('''
             insert into t_xiezhu_apply_milepost(xiezhu_id,type_name,uid,uid_name,created_at)
             values(%s,'待审核',%s,%s,%s)
            ''',result,uid,uid_name,dt)
                    txt='发起协助'
            elif step=='2':
                if is_pass=='1':
                    is_exit=self.db.get('''
                    select * from  t_xiezhu_apply_milepost where xiezhu_id=%s and type_name='待接单'
                    ''',xiezhu_id)
                    if not is_exit:
                        self.db.execute('''
                insert into t_xiezhu_apply_milepost(xiezhu_id,type_name,uid,uid_name,created_at,fz_name,fz_id,remark)
                values(%s,'待接单',%s,%s,%s,%s,%s,%s)
                ''',xiezhu_id,fenpei_xs_id,fenpei_xs_name,dt,uid_name,uid,remark)
                    self.db.execute('''
                update t_xiezhu_apply_milepost set confirm_at=%s,is_pass=%s,fz_id=%s,fz_name=%s where id=%s
            ''',dt,is_pass,uid,uid_name,gs_id)
                    txt='审核通过'
                elif is_pass=='0':
                    self.db.execute('''
                update t_xiezhu_apply_milepost set is_pass=%s,remark=%s,reject_at=%s where id=%s
            ''',is_pass,remark,dt,gs_id)
                    txt='驳回'
            elif step=='3':
                self.db.execute('''
                update t_xiezhu_apply_milepost set confirm_at=%s where id=%s
            ''',dt,xs_id)
                txt='接单'
            elif step=='4':
                if is_pass:
                    self.db.execute(''' update t_xiezhu_apply_milepost set is_pass=null where id=%s''',sh_id)
                else:
                    is_exit=self.db.get('''
                    select * from  t_xiezhu_apply_milepost where xiezhu_id=%s and type_name='结果审核'
                    ''',xiezhu_id)
                    if not is_exit:
                        self.db.execute('''
                        insert into t_xiezhu_apply_milepost(xiezhu_id,type_name,uid,uid_name,created_at)
                        values(%s,'结果审核',%s,%s,%s)
                        ''',xiezhu_id,uid,uid_name,dt)
                    txt='申请办结'
                self.db.execute('''
                update t_xiezhu_apply set xiezhu_zj=%s where id=%s
                ''',xiezhu_zj,xiezhu_id)
                
            elif step=='5':
                if is_pass=='1':
                    is_exit=self.db.get('''
                    select * from  t_xiezhu_apply_milepost where xiezhu_id=%s and type_name='已确认'
                    ''',xiezhu_id)
                    if not is_exit:
                        self.db.execute('''
                        insert into t_xiezhu_apply_milepost(created_at,uid,uid_name,fz_name,fz_id,type_name,xiezhu_id)
                        values(%s,%s,%s,%s,%s,'已确认',%s)''',dt,gs_uid,gs_uid_name,uid_name,uid,xiezhu_id)
                    self.db.execute('''
                    update t_xiezhu_apply_milepost set confirm_at=%s,remark=%s,fz_name=%s,fz_id=%s,is_pass=%s where id=%s
                ''',dt,remark,uid_name,uid,is_pass,sh_id)
                    self.db.execute('''
                    update t_xiezhu_apply set updated_at=%s where id=%s
                    ''',dt,xiezhu_id)
                    txt=uid_name+'审核通过'
                elif is_pass=='0':
                    self.db.execute('''
                    update t_xiezhu_apply_milepost set remark=%s,fz_name=%s,fz_id=%s,is_pass=%s,reject_at=%s where id=%s
                ''',remark,uid_name,uid,is_pass,dt,sh_id)
                    txt=uid_name+'驳回'
            elif step=='6':
                self.db.execute('''
                    update t_xiezhu_apply_milepost set confirm_at=%s where id=%s
                ''',dt,queren_id)
                txt=uid_name+'确认业务已经办结'
            if txt:
                events.add_project_event(self,project_id,'业务协助',txt,uid,uid_name,customer_id)
        elif tag=="project_relation":
            relation_id=self.get_argument('relation_id')
            be_relation_id=self.get_argument('be_relation_id')
            id=self.get_argument('id','')
            customer_id=self.get_argument('customer_id','0')
            be_relation_project_id=self.get_argument('be_relation_project_id','')
            relation_project=self.db.get(''' select customer_company from t_projects where id=%s''',relation_id)
            be_relation_project=self.db.get(''' select customer_company from t_projects where id=%s''',be_relation_id)
            result=None
            # is_exit=self.db.get('''
            #         select * from t_projects_relation where relation_ids like "%%,'''+str(be_relation_id)+''',%%" or relation_ids REGEXP  "^'''+str(be_relation_id)+'''," ''')
            # if is_exit:
            #     self.write('-1')
            if relation_project.customer_company and be_relation_project.customer_company and relation_project.customer_company!=be_relation_project.customer_company:
                self.write('-2')
            elif id and be_relation_project_id:
                t_projects_relation=self.db.get('''
                    select * from t_projects_relation where id=%s
                ''',be_relation_project_id)
                result=self.db.execute('''
                        update t_projects_relation set relation_ids=concat(relation_ids,%s),uid_names= CONCAT(uid_names,%s)  where id=%s
                    ''',t_projects_relation.relation_ids,t_projects_relation.uid_names,id)
                self.db.execute('''
                delete  from t_projects_relation where id=%s
                ''',be_relation_project_id)
            elif id and not be_relation_project_id:
                result=self.db.execute('''
                        update t_projects_relation set relation_ids=concat(relation_ids,%s),uid_names= CONCAT(uid_names,%s)  where id=%s
                    ''',be_relation_id+',',uid_name+'|'+relation_id+'|'+be_relation_id+',',id)
            elif not id and be_relation_project_id:
                result=self.db.execute('''
                        update t_projects_relation set relation_ids=concat(relation_ids,%s),uid_names= CONCAT(uid_names,%s)  where id=%s
                    ''',relation_id+',',uid_name+'|'+relation_id+'|'+be_relation_id+',',be_relation_project_id)
            else:
                result=self.db.execute('''
                insert into t_projects_relation(relation_ids,created_at,uid_names)
                values(%s,%s,%s)''',relation_id+','+be_relation_id+',',dt,uid_name+'|'+relation_id+'|'+be_relation_id+',')
            if result>=0:
                events.add_project_event(self,relation_id,'关联订单(确认单)','订单'+relation_id+'关联订单'+be_relation_id,uid,uid_name,customer_id)
        elif tag=="delete_relation":
            relation_id=self.get_argument('relation_id')
            id=self.get_argument('id')
            self.db.execute('''
            update t_projects_relation set relation_ids=REPLACE(relation_ids,%s,'') where id=%s
            ''',relation_id+',',id)
            relation=self.db.get('''
                select (LENGTH(relation_ids)-LENGTH(REPLACE(relation_ids,',','')))/LENGTH(',') count from t_projects_relation where id=%s
            ''',id)
            if relation.count==1:
                self.db.execute('''
                 delete from t_projects_relation where id=%s
                ''',id)
        elif tag=="delete_project":
            project_id=self.get_argument('project_id')
            guid=self.get_argument('guid')
            self.db.execute('''
            update t_statis_kf a,
            (select member_id,member_name,team_name,date(b.created_at) project_created_at,busniess_from_id_name,
            busniess_from_id,all_income,role,b.id from t_projects_member a ,t_projects b,t_user c
            where member_id=c.id  and a.project_id=b.id and (role=13 or role=6 or role=1) and all_income > 0  and b.id=%s )b
            set a.all_income=a.all_income-b.all_income ,a.all_count=a.all_count-1
            where a.project_created_at=b.project_created_at and a.uid=b.member_id and a.busniess_from_id=b.busniess_from_id
            ''',project_id)
            self.db.execute('''
                delete from t_projects where id=%s and guid=%s
            ''',project_id,guid)
            relation=self.db.get('''
                select (LENGTH(relation_ids)-LENGTH(REPLACE(relation_ids,',','')))/LENGTH(',') count,id
                 from t_projects_relation where
                 relation_ids like "%%,'''+str(project_id)+''',%%" or relation_ids REGEXP  "^'''+str(project_id)+''',"
            ''')
            if relation:
                if relation.count==2:
                    self.db.execute('''
                    delete from t_projects_relation where  id=%s
                    ''',relation.id)
                else:
                    self.db.execute('''
                update t_projects_relation set relation_ids=REPLACE(relation_ids,%s,'') where id=%s
                ''',project_id+',',relation.id)

            self.db.execute('''
                delete from t_projects_member where project_id=%s
            ''',project_id)
            try:
                self.db.execute('''
                    delete from t_projects_member_other where project_id=%s
                ''',project_id)
            except:
                pass
            try:

                self.db.execute('''
                    delete from t_projects_income where project_id=%s
                ''',project_id)
            except:
                pass
            try:
                self.db.execute('''
                    delete from t_projects_income_title where project_id=%s
                ''',project_id)
            except:
                pass
            try:
                self.db.execute('''
                    delete from t_projects_service_income where project_id=%s
                ''',project_id)
            except:
                pass
            try:
                self.db.execute('''
                    delete from t_projects_state_msg where project_id=%s
                ''',project_id)
            except:
                pass
            try:

                self.db.execute('''
                    delete from t_projects_income_other where project_id=%s
                ''',project_id)
            except:
                pass
            try:
                self.db.execute('''
                    delete from t_projects_linkman where project_id=%s
                ''',project_id)
            except:
                pass
            try:
                self.db.execute('''
                    delete from t_projects_transition where project_id=%s
                ''',project_id)
            except:
                pass
            try:
                self.db.execute('''
                    delete from t_projects_transition_upload where project_id=%s
                ''',project_id)
            except:
                pass
            try:
                self.db.execute('''
                    delete from t_projects_company_history where project_id=%s
                ''',project_id)
            except:
                pass
            try:
                self.db.execute('''
                    SET SQL_SAFE_UPDATES = 0;
                    delete a.*,b.* from
                    t_xiezhu_apply a left join t_xiezhu_apply_milepost b on  a.id=b.xiezhu_id where a.project_id=%s;
                    SET SQL_SAFE_UPDATES = 1;
                ''',project_id)
            except:
                pass
            try:
                self.db.execute('''
                    delete from t_projects_milepost where project_id=%s
                ''',project_id)
            except:
                pass
            try:
                self.db.execute('''
                    delete from t_projects_note where project_id=%s
                ''',project_id)
            except:
                pass
            try:
                self.db.execute('''
                    delete from t_projects_note_check where project_id=%s
                ''',project_id)
            except:
                pass


        elif tag=="project_print":
            id=self.get_argument('id','')
            delete_id=self.get_argument('delete_id','')
            if id:
                self.db.execute('''
                    update t_projects_note set is_add_to_print=1 where id=%s
                ''',id)
            elif delete_id:
                self.db.execute('''
                    update t_projects_note set is_add_to_print=0 where id=%s
                ''',delete_id)

        elif tag=="delete_company_history":
            project_id=self.get_argument('project_id')
            self.db.execute('''
                delete from t_projects_company_history where project_id=%s
            ''',project_id)

        elif tag=="project_check":
            kf_check_status=self.get_argument('kf_check_status','')
            remark=self.get_argument('remark','')
            project_id=self.get_argument('project_id','')
            sh_remark=self.get_argument('sh_remark','')
            is_sh=self.get_argument('is_sh','')
            if is_sh:
                self.db.execute('''
                update t_projects_check set sh_uid_name=%s,sh_uid=%s,sh_created_at=%s,sh_remark=%s where project_id=%s
                ''',uid_name,uid,dt,sh_remark,project_id)
            else:
                self.db.execute('''
                    insert into t_projects_check
                    (kf_created_at,project_id,kf_uid,kf_uid_name,remark,kf_check_status)
                    values(%s,%s,%s,%s,%s,%s)
                ''',dt,project_id,uid,uid_name,remark,kf_check_status)

        elif tag=="express":
            source=self.get_argument('source','')
            rec_name=self.get_argument('rec_name','')
            rec_tel=self.get_argument('rec_tel','')
            rec_addr=self.get_argument('rec_addr','')
            rec_file=self.get_argument('rec_file','')
            rec_file_ids=self.get_argument('rec_file_ids','')
            rec_company=self.get_argument('rec_company','')
            express_type_id=self.get_argument('express_type_id','')
            express_type_name=self.get_argument('express_type_name','')
            other_rec_file=self.get_argument('other_rec_file','')
            express_number=self.get_argument('express_number','')
            send_name=self.get_argument('send_name','')
            project_id=self.get_argument('project_id',0)
            payment_type_id=self.get_argument('payment_type_id','')
            payment_type_name=self.get_argument('payment_type_name','')
            express_remark=self.get_argument('express_remark','')
            send_name=self.get_argument('send_name','')
            express_id=self.get_argument('express_id','')
            guid=self.get_argument('guid','')
            send_or_rec=self.get_argument('send_or_rec',0)
            save_customer_add_msg=self.get_argument('save_customer_add_msg','')
            company=self.get_argument('company','')
            len1=int(self.get_argument('len',0))
            created_send_at=self.get_argument('created_send_at','')
            delete_id=self.get_argument('delete_id','')
            cw_confirm_express_ids=self.get_argument('cw_confirm_express_ids','')
            cw_confirm_express_id=self.get_argument('cw_confirm_express_id','')
            txt=''
            event_type=''
            is_upload = False
            file_path =''
            t_customer=self.db_customer.get(' select id from t_customer where id=%s and guid=%s ',project_id,guid)
            t_project=self.db.get(' select id from t_projects where id=%s and guid=%s ',project_id,guid)
            if not created_send_at:
                created_send_at=None
            for i in range(len1):
                try:
                    file1 = self.request.files['file'+str(i)][0]
                    is_upload = True
                except:
                    pass
                if is_upload:
                    ori_filename = file1["filename"]
                    filename_full = options.upload_path + "/express/%s/" % (express_id)
                    url_path = "/static/express/%s/" % (express_id)
                    try:
                        os.makedirs(filename_full)
                    except OSError:
                        if not os.path.isdir(filename_full):
                            raise

                    uuid_str = str(uuid.uuid4())
                    fname = "{0}".format(ori_filename)

                    save_full_path = filename_full + fname
                    url_fname = "{0}{1}".format(url_path, fname)

                    output_file = open(save_full_path, 'w')
                    output_file.write(file1["body"])
                    file_path += url_fname+'|'

            if file_path:
                self.db.execute('''
                        update t_express set file_path=concat(%s,file_path) where id=%s ''',file_path,express_id)
            else:
                t_user=self.db.get(''' select id,concat(department_zone,department_name) department_name from t_user where name=%s''',send_name)
                if save_customer_add_msg:
                    t_customer_addr_msg=self.db.get('''
                    select * from t_customer_addr_msg where name=%s and tel=%s and addr=%s
                    ''',rec_name,rec_tel,rec_addr)
                    if not t_customer_addr_msg:
                        self.db.execute('''
                            insert into t_customer_addr_msg(name,tel,addr,company,uid,uid_name)
                            values(%s,%s,%s,%s,%s,%s)''',rec_name,rec_tel,rec_addr,rec_company,uid,uid_name)
                    else:
                        self.write('-1')
                if express_id and t_user:
                    t_express=self.db.get('''select * from t_express where id=%s''',express_id)
                    if  t_express.accept_state==0:
                        self.db.execute('''
                            update t_express set send_at_name=%s,send_at_uid=%s,sender_department=%s,rec_name=%s,rec_addr=%s,
                            rec_tel=%s,rec_file=%s,rec_company=%s,remark=%s,express_type_id_name=%s,
                            express_type_id=%s,payment_type_id_name=%s,payment_type_id=%s,
                            rec_file_ids=%s,other_rec_file=%s,express_number=%s,created_send_at=%s
                            where id=%s
                        ''',send_name,t_user.id,t_user.department_name,rec_name,rec_addr,rec_tel,
                        rec_file,rec_company,express_remark,express_type_name,express_type_id,
                        payment_type_name,payment_type_id,rec_file_ids,other_rec_file,express_number,created_send_at,express_id)
                        if t_express.send_or_rec==0:
                            event_type='修改寄件'
                            if t_express.rec_name!=rec_name:
                                txt+=',收件人:'+t_express.rec_name+' 修改为 '+rec_name
                            if t_express.rec_tel!=rec_tel:
                                txt+=',收件人电话:'+t_express.rec_tel+' 修改为 '+rec_tel
                            if t_express.rec_addr!=rec_addr:
                                txt+=',收件人地址:'+t_express.rec_addr+' 修改为 '+rec_addr
                            if t_express.send_at_name!=send_name:
                                txt+=',发件人:'+t_express.send_at_name+' 修改为 '+send_name
                        elif t_express.send_or_rec==1:
                            event_type='修改收件'
                            if t_express.rec_name!=rec_name:
                                txt+=',寄件人:'+t_express.rec_name+' 修改为 '+rec_name
                            if t_express.rec_tel!=rec_tel:
                                txt+=',寄件人电话:'+t_express.rec_tel+' 修改为 '+rec_tel
                            if t_expres.rec_addr!=rec_addr:
                                txt+=',寄件人地址:'+t_express.rec_addr+' 修改为 '+rec_addr
                            if t_express.send_at_name!=send_name:
                                txt+=',收件人:'+t_express.send_at_name+' 修改为 '+send_name
                        if t_express.rec_file!=rec_file:
                            txt+=',交接明细:'+t_express.rec_file+' 修改为 '+rec_file
                        if t_express.other_rec_file!=other_rec_file:
                            txt+=',其他资料:'+t_express.other_rec_file+' 修改为 '+other_rec_file

                        if t_express.rec_company!=rec_company:
                            txt+=',公司名称:'+t_express.rec_company+' 修改为 '+rec_company
                        if t_express.express_number!=express_number:
                            txt+=',快递单号:'+t_express.express_number+' 修改为 '+express_number
                        if t_express.express_type_id_name!=express_type_name:
                            txt+=',快递类型:'+t_express.express_type_id_name+' 修改为 '+express_type_name
                        if t_express.payment_type_id_name!=payment_type_name:
                            txt+=',快递付费:'+t_express.payment_type_id_name+' 修改为 '+payment_type_name
                        if str(t_express.created_send_at.strftime('%Y-%m-%d'))!=created_send_at:
                            txt+=',发件时间:'+str(t_express.created_send_at.strftime('%Y-%m-%d'))+' 修改为 '+created_send_at
                        if txt:
                            if t_project:
                                events.add_project_event(self,t_express.project_id,event_type,txt,uid,uid_name)
                            elif t_customer:
                                events.add_project_event(self,'0',event_type,txt,uid,uid_name,t_express.project_id)
                    else:
                        self.write('-2')

                elif t_user:
                    result=self.db.execute('''
                        INSERT INTO t_express
                    (uid_name,uid,send_at_name,send_at_uid,project_id,rec_name,rec_addr,
                    rec_tel,rec_file,rec_company,remark,express_type_id_name,express_type_id
                    ,payment_type_id_name,payment_type_id,rec_file_ids,other_rec_file,express_number,
                    source,created_at,guid,sender_department,send_or_rec,created_send_at)
                    values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
                    ''',uid_name,uid,send_name,t_user.id,project_id,rec_name,rec_addr,rec_tel,
                    rec_file,rec_company,express_remark,express_type_name,express_type_id,
                    payment_type_name,payment_type_id,rec_file_ids,other_rec_file,express_number,
                    source,dt,guid,t_user.department_name,send_or_rec,created_send_at)
                    if result>0:
                        if send_or_rec=='0':
                            event_type='新建寄件'
                            txt='收件人:'+rec_name+',收件人电话:'+rec_tel+',收件人地址:'+rec_addr+',快递单号:'+express_number+' 等'
                        elif send_or_rec=='1':
                            event_type='新建收件'
                            txt='寄件人:'+rec_name+',寄件人电话:'+rec_tel+',寄人地址:'+rec_addr+',快递单号:'+express_number+' 等'
                        if t_project:
                            events.add_project_event(self,project_id,event_type,txt,uid,uid_name)
                        elif t_customer:
                            events.add_project_event(self,'0',event_type,txt,uid,uid_name,project_id)
                elif delete_id:
                    is_exit=self.db.get(''' select * from t_express where id=%s and accept_at is not null  ''',delete_id)
                    if not is_exit:
                        self.db.execute(''' delete  from t_express where id=%s ''',delete_id)
                        
                    else:
                        self.write('-1')
                elif cw_confirm_express_id:
                    self.db.execute('''
                        update t_express set confirm_at=%s,confirm_name=%s where id=%s
                    ''',dt,uid_name,cw_confirm_express_id)
                elif cw_confirm_express_ids:
                    for id in cw_confirm_express_ids.split(','):
                        self.db.execute('''
                        update t_express set confirm_at=%s,confirm_name=%s where id=%s
                    ''',dt,uid_name,id)
                elif not t_user:
                    self.write('-3')

        elif tag=="delete_express_file":
            file_name=self.get_argument('file_name',)
            express_file_id=self.get_argument('express_file_id')
            file_name='/static/express/'+express_file_id+'/'+file_name+'|'
            self.db.execute('''
                update t_express set file_path=replace(file_path,"'''+file_name+'''",'')  where id=%s
            ''',express_file_id)

        elif tag=="check_express":
            accept_state=self.get_argument('accept_state')
            accept_uid_remark=self.get_argument('accept_uid_remark','')
            express_id=self.get_argument('express_id')
            self.db.execute('''
                update t_express set accept_state=%s,accept_at=%s,accept_uid_name=%s,
                accept_uid=%s,accept_uid_remark=%s where id=%s
            ''',accept_state,dt,uid_name,uid,accept_uid_remark,express_id)

        elif tag=="confrim_express":
            express_number=self.get_argument('express_number')
            send_at=self.get_argument('send_at')
            express_id=self.get_argument('express_id')
            self.db.execute('''
                update t_express set express_number=%s,send_at=%s,send_at_uid=%s,send_at_name=%s where id=%s
            ''',express_number,send_at,uid,uid_name,express_id)

        elif tag=="confirm_send_express":
            express_id=self.get_argument('express_id','')
            express_ids=self.get_argument('express_ids','')
            if express_id:
                self.db.execute('''
                update t_express set send_at=%s where id=%s
            ''',dt,express_id)
            elif express_ids:
                for item in express_ids.split(','):
                    self.db.execute('''
                update t_express set send_at=%s where id=%s
            ''',dt,item)

        elif tag=="project_confirm_banjie":
            confirm_banjie=self.get_argument('confirm_banjie')
            banjie_remark=self.get_argument('banjie_remark','')
            guid=self.get_argument('guid')
            id=self.get_argument('id')
            team_name=self.get_argument('team_name','')
            mid=self.get_argument('mid','')
            project_id=self.get_argument('project_id','')
            self.db.execute('''
            update t_projects_member set confirm_banjie=%s,banjie_remark=%s,confirm_name=%s,confirm_uid=%s
            where project_id=%s and guid=%s''',
            confirm_banjie,banjie_remark,uid_name,uid,id,guid)
            milepost = self.db.get("select * from t_projects_milepost where member_id=%s and type_id=154 and project_id=%s",mid,project_id)
            
            if team_name=='客服会计' and not  milepost.confirm_at:
                if mid:
                    self.db.execute("""
                            update t_projects_transition set rec_by_uid_at=%s 
                             where project_id=%s and mid=%s and is_customer=1
                        """,dt,project_id,mid)
                bresult = self.db.execute("""
                    update t_projects_milepost set confirm_at=%s,uid=%s,uid_name=%s where id=%s 
                """, dt, uid, uid_name, milepost.id)
                if bresult == 0:
                    bresult = self.db.execute(
                        """update t_projects_member set last_milepost_id=%s ,
                        last_milepost_id_name=%s,last_milepost_id_at=%s 
                         where mid=%s and project_id=%s""",
                        milepost.type_id, milepost.type_name, dt,
                        milepost.member_id, project_id)
                t_projects_member = self.db.get(
                    " select * from t_projects_member where mid=%s and project_id=%s",
                    milepost.member_id, project_id)
                if t_projects_member:
                    if milepost.type_name != u'待接单' or  milepost.type_name != u'办理中' and  t_projects_member.btype_id_name==u"公司注册" :
                        self.db.execute(
                            "update t_projects set reg_state=2 where id=%s",
                            project_id)
        elif tag=="manage_chengjiao":
            msg_chengjiao=self.get_argument('msg','')
            id=self.get_argument('id','')
            delete_id=self.get_argument('delete_id','')
            if id:
                self.db.execute('''
                update t_projects_note_chengjiao set msg=%s,updated_at=%s,updated_name=%s,updated_uid=%s where id=%s
                ''',msg_chengjiao,dt,uid_name,uid,id)
            elif delete_id:
                self.db.execute('''
                    delete from t_projects_note_chengjiao where id=%s
                ''',delete_id)
            else:
                self.db.execute('''
                insert into t_projects_note_chengjiao(msg,uid,uid_name,created_at)
                values(%s,%s,%s,%s)
                ''', msg_chengjiao, uid, uid_name, dt)

        elif tag=="edit_zone":
            mid=self.get_argument('mid','')
            mids=self.get_argument('mids','')
            mid1=self.get_argument('mid1','')
            zone_id=self.get_argument('zone_id','')
            zone_id1=self.get_argument('zone_id1','')
            income_name=self.get_argument('income_name','')
            income_name1=self.get_argument('income_name1','')
            if mids:
                for item in mids.split(','):
                    self.db.execute('''
                    update t_projects_member set zone_id=%s,zone_id_name=%s where mid=%s
                ''',zone_id,income_name,item)
            else:
                if mid and zone_id:
                    self.db.execute('''
                        update t_projects_member set zone_id=%s,zone_id_name=%s where mid=%s
                    ''',zone_id,income_name,mid)
                if mid1 and zone_id1:
                    self.db.execute('''
                        update t_projects_member set zone_id=%s,zone_id_name=%s where mid=%s
                    ''',zone_id1,income_name1,mid1)

        elif tag=="expire_msg":
            type_id = self.get_argument("type_id",0)
            curr_state_id = self.get_argument("curr_state_id")
            project_id = self.get_argument("project_id")
            project_type=self.db.get('''
                select * from t_projects_type where income_category='业务分类' and ext_type_id <> 0
                 and ext_type_id=%s''',type_id)
            t_project_member=self.db.get('''
                select mid from t_projects_member a
                inner join t_projects_state_msg b on a.btype_id=b.p_type_id
                and b.uid_name=%s and b.id=%s and hour(timediff(now(),b.created_at))>=24
                 where team_name='工商专员'
                    and a.project_id=%s and btype_id=%s and member_name=%s
                ''',uid_name,curr_state_id,project_id,project_type.id,uid_name)
            if t_project_member and uid_name!='罗文波':
                self.write('-100')

        elif tag=="bj_manage_yw_show":
            category=self.get_argument('category','')
            product=self.get_argument('product','')
            remark=self.get_argument('remark','')
            sql=''

            if category:
                sql+=' and a.category_id=%s '%category
            if product:
                sql+=' and  a.name like "%%'+product+'%%" '
            if remark:
                sql+=' and a.remark like "%%'+remark+'%%" '
            product_bid = self.db_ext.query("select a.*,b.name category_name from t_products a , t_category b where a.category_id=b.id "+sql+" order by b.order_int")
            self.write({'product_bid':product_bid})
        elif tag=="reset_logoff":
            project_id = self.get_argument("project_id")
            mid = self.get_argument("mid")
            logoff_id = self.get_argument("logoff_id")
            type_id = self.get_argument("type_id")
            t_projects_logoff = self.db.get('select * from t_projects_logoff where project_id=%s and type_id=%s',project_id,type_id)
            t_projects_member = self.db.get("select * from t_projects_member where mid=%s",mid)
            reject_remark = self.get_argument("reject_remark","")
            if not t_projects_member:
                return self.write("业务不存在")
            if t_projects_member.member_id ==int(uid) or role=="7" or role=="8":

                if  t_projects_logoff:
                    t_project_type_state = self.db.get('select * from t_projects_type where income_category="注销审核" and order_int=3')
                    log_txt ="驳回"
                    self.db.execute(
                        """insert into t_projects_logoff_log(mid,project_id,uid,type_id,reject_remark,logoff_id,reject_at,leader_uid,btype_id,leader_uid_name,uid_name)
                         values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)""",
                        mid, project_id, t_projects_logoff.uid, type_id,
                        reject_remark, logoff_id, dt, uid, type_id,uid_name,t_projects_logoff.uid_name)
                    self.db.execute("""
                        update  t_projects_logoff set leader_uid=%s,leader_uid_name=%s,leader_at=%s,state_id=%s,state_id_name=%s,last_reject_remark=%s where id=%s
                    """, uid, uid_name, dt, t_project_type_state.order_int,
                                    t_project_type_state.income_name,
                                    reject_remark, logoff_id)
                    event_msg = "%s 取消(%s)确认 %s" % (uid_name,
                                                  t_projects_logoff.uid_name,
                                                  t_projects_logoff.type_id_name)
                    events.add_project_event_ext(self, project_id, "注销业务", event_msg,
                                         uid, uid_name,mid)
                    self.write("0")

                else:
                    self.write("没有撒消记录,请刷新.")
            else:
                return self.write("请切换到您的业务标签下,进行确认哦.")
        elif tag=="confirm_logoff":
            logoff_id = self.get_argument("logoff_id")
            project_id = self.get_argument("project_id")
            mid = self.get_argument("mid")
            if not logoff_id or not  project_id:
                return self.write("project_id and logoff_id is null")
            else:
                t_projects_logoff = self.db.get('select * from t_projects_logoff where id=%s',logoff_id)
                if not t_projects_logoff:
                    return self.write("not t_projects_logoff")

                t_project_type_state = self.db.get('select * from t_projects_type where income_category="注销审核" and order_int=2')


                result = self.db.execute("update t_projects_logoff set leader_uid=%s,leader_uid_name=%s,leader_at=%s,state_id=%s,state_id_name=%s where id=%s",
                uid,uid_name,dt,t_project_type_state.order_int,t_project_type_state.income_name,logoff_id)

                event_msg = "%s 确认(%s)办结 %s" % (uid_name,
                                                  t_projects_logoff.uid_name,
                                                  t_projects_logoff.type_id_name)
                events.add_project_event_ext(self, project_id, "注销业务", event_msg,
                                         uid, uid_name,mid)
                self.write(str(result))

        elif tag=="set_logoff":
            project_id = self.get_argument("project_id")
            type_id = self.get_argument("type_id")
            mid = self.get_argument("mid")
            if not project_id and not type_id:
                return self.write("not id")
            else:
                t_project_type  = self.db.get("select * from t_projects_type where income_category='注销' and order_int=%s",type_id)
                if not t_project_type:
                    return self.write("not project type")
                t_projects_logoff = self.db.get('select * from t_projects_logoff where project_id=%s and type_id=%s',project_id,type_id)
                t_projects_member = self.db.get("select * from t_projects_member where mid=%s",mid)

                if not t_projects_member:
                    return self.write("业务不存在")
                if t_projects_member.member_id ==int(uid):
                    t_project_type_state = self.db.get('select * from t_projects_type where income_category="注销审核" and order_int=1')
                    if not t_projects_logoff:
                        self.db.execute("""
                            insert into t_projects_logoff(mid,project_id,uid,uid_name,finish_at,type_id,type_id_name,state_id,state_id_name)
                            values(%s,%s,%s,%s,%s,%s,%s,%s,%s)
                        """,mid,project_id,uid,uid_name,dt,type_id,t_project_type.income_name,t_project_type_state.order_int,t_project_type_state.income_name)
                        event_msg = "%s 确认完成 %s(%s)" % (
                            uid_name, t_project_type.income_name,
                            t_project_type_state.income_name)
                        events.add_project_event_ext(self, project_id, "注销业务", event_msg,
                                         uid, uid_name,mid)
                        self.write("0")
                    else:
                        self.db.execute("""
                            update t_projects_logoff set uid=%s ,uid_name=%s,finish_at=%s,state_id=%s,state_id_name=%s,leader_uid=0,leader_uid_name=NULL ,leader_at=NULL
                            where id=%s

                        """, uid,uid_name,dt,t_project_type_state.order_int,t_project_type_state.income_name,t_projects_logoff.id)
                        event_msg = "%s 确认完成 %s(%s)" % (
                            uid_name, t_project_type.income_name,
                            t_project_type_state.income_name)
                        events.add_project_event_ext(self, project_id, "注销业务", event_msg,
                                         uid, uid_name,mid)
                        self.write("0")





                else:
                    return self.write("请切换到您的业务标签下,进行确认哦.")

        elif tag=='cb_addr_manage':
            sale_addr=self.get_argument('sale_addr','')
            arrange_date=self.get_argument('arrange_date','')
            company=self.get_argument('company','')
            legal_peson=self.get_argument('legal_peson','')
            purchaser=self.get_argument('purchaser','')
            cost_price=self.get_argument('cost_price','') or '0'
            sell_price=self.get_argument('sell_price','') or '0'
            rent_date=self.get_argument('rent_date','')
            purchaser_pay_money=self.get_argument('purchaser_pay_money','') or '0'
            purchaser_pay_date=self.get_argument('purchaser_pay_date','')
            expire_date=self.get_argument('expire_date','')
            supplier=self.get_argument('supplier','')
            addr_xingzhi=self.get_argument('addr_xingzhi','')
            addr_type=self.get_argument('addr_type','')
            supply_js_date=self.get_argument('supply_js_date','')
            supply_js_money=self.get_argument('supply_js_money','') or '0'
            cb_addr_id=self.get_argument('cb_addr_id','')
            step=self.get_argument('step','')
            purchaser_qk=self.get_argument('purchaser_qk','') or '0'
            supply_qk=self.get_argument('supply_qk','') or '0'
            update_add=''
            if not supply_js_date:
                supply_js_date=None
            if not rent_date:
                rent_date=None
            if not expire_date:
                expire_date=None
            if step=='1':
                update_add=' chuna_check_name="%s",chuna_check_id=%s,chuna_check_date="%s"  '%(uid_name,uid,dt)
            elif step=='2':
                update_add=' fq_date="%s" '%dt
            elif step=='3':
                update_add=' ,supply_js_money=%s,supply_js_date="%s",supply_qk=%s  '%(supply_js_money,supply_js_date,supply_qk)
            elif step=='4':
                update_add=' cawu_js_id=%s,caiwu_js_name="%s",caiwu_js_date="%s" '%(uid,uid_name,dt)
            if cb_addr_id:
                if not step or step=='3':
                    self.db.execute('''
                update t_cb_addr_manage set sale_addr=%s,arrange_date=%s,company=%s,legal_peson=%s,purchaser=%s,
                cost_price=%s,sell_price=%s,rent_date=%s,purchaser_pay_money=%s,purchaser_pay_date=%s,
                expire_date=%s,supplier=%s,addr_xingzhi=%s,addr_type=%s '''+update_add+''' where id=%s
                ''',sale_addr,arrange_date,company,legal_peson,purchaser,cost_price,sell_price,rent_date,purchaser_pay_money,
                purchaser_pay_date,expire_date,supplier,addr_xingzhi,addr_type,cb_addr_id)
                elif step:
                    self.db.execute('''
                    update t_cb_addr_manage set '''+update_add+''' where id=%s
                    '''%cb_addr_id)
            else:
                self.db.execute('''
                insert into t_cb_addr_manage(sale_addr,arrange_date,company,legal_peson,purchaser,
                cost_price,sell_price,rent_date,purchaser_pay_money,purchaser_pay_date,expire_date,supplier,
                addr_xingzhi,addr_type,uid,uid_name,created_at,purchaser_qk)
                values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
                ''',sale_addr,arrange_date,company,legal_peson,purchaser,
                cost_price,sell_price,rent_date,purchaser_pay_money,purchaser_pay_date,expire_date,supplier,
                addr_xingzhi,addr_type,uid,uid_name,dt,purchaser_qk)

        elif tag=='cb_addr_confirm':
            cb_addr_id=self.get_argument('cb_addr_id')
            purchaser_caiwu_confirm=self.get_argument('purchaser_caiwu_confirm','')
            supply_caiwu_confirm=self.get_argument('supply_caiwu_confirm','')
            if not purchaser_caiwu_confirm:
                self.db.execute('''
                update t_cb_addr_manage set purchaser_caiwu_confirm=%s where id=%s
                ''',dt,cb_addr_id)
            elif purchaser_caiwu_confirm and not supply_caiwu_confirm:
                self.db.execute('''
                update t_cb_addr_manage set supply_caiwu_confirm=%s where id=%s
                ''',dt,cb_addr_id)
        elif tag=="project_reject":
            reject_msg=self.get_argument('reject_msg','')
            reject_msg_titles=self.get_argument('reject_msg_titles','')
            project_id=self.get_argument('project_id','')
            handler_name=self.get_argument('handler_name','')
            handler_uid=self.get_argument('handler_uid','')
            reject_id=self.get_argument('reject_id','')
            step=self.get_argument('step','')
            project_guid=self.get_argument('project_guid','')
            confirm_reject_msg=self.get_argument('confirm_reject_msg','')
            confirm_status=self.get_argument('confirm_status','')
            
            if step=='1':
                self.db.execute(' update t_projects_information_reject set handler_at=%s where id=%s',dt,reject_id)
            elif step=='2':
                self.db.execute(' update t_projects_information_reject set confirm_at=%s,confirm_status=%s,confirm_reject_msg=%s where id=%s'
                ,dt,confirm_status,confirm_reject_msg,reject_id)
            elif step=='3':
                self.db.execute(' update t_projects_information_reject set handler_at=%s,confirm_at=null where id=%s',dt,reject_id)
            else:
                self.db.execute(''' 
                insert into t_projects_information_reject
                (project_id,project_guid,uid,uid_name,created_at,reject_msg,handler_name,
                handler_uid,reject_msg_titles) 
                values(%s,%s,%s,%s,%s,%s,%s,%s,%s)
                ''',project_id,project_guid,uid,uid_name,dt,reject_msg,handler_name,handler_uid,reject_msg_titles)

        elif tag=="project_trade":
            trade_nums=self.get_argument('trade_nums','')
            # trade_ys_nums=self.get_argument('trade_ys_nums','')
            # trade_ds_nums=self.get_argument('trade_ds_nums','')
            project_id=self.get_argument('project_id','')
            self.db.execute('''
                update t_projects set trade_nums=%s where id=%s
            ''',trade_nums,project_id)