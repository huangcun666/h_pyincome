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
import tools
logger = logging.getLogger('boilerplate.' + __name__)


class TradeHandler(BaseHandler):


    @tornado.web.authenticated
    def get(self):
        tag = self.get_argument("tag","list")
        uid = self.get_secure_cookie("uid")
        uid_name=self.get_secure_cookie('name')
        page=int(self.get_argument('page',1))
        my = self.get_argument("my","1")
        role = self.get_secure_cookie("role")
        search_key = self.get_argument("search_key",'')

        my_sql =""
        sql_where =""
        sql_inner=""
        if role!="8":
            my_sql=" and created_uid=%s "%(uid)
        pre_page=20
        if tag =="list":
            page= int(self.get_argument("page",1))
            todo  = self.get_argument("todo","")
            status = int(self.get_argument("status",0))
            is_end = int(self.get_argument("is_end",0))
            show_tag=self.get_argument('show_tag','')
            trade_id = self.get_argument("trade_id","")
            key = self.get_argument("key","")
            trade_regtype = self.get_argument("trade_regtype","")
            trade_color = self.get_argument("trade_color","")
            project_id = self.get_argument("project_id","")
            created_uid_name = self.get_argument("created_uid_name","")            
            paramas = {
                "status":status,
                "is_end":is_end,
                "tag":tag,
                "todo":todo,
                "trade_id":trade_id,
                "created_uid_name":created_uid_name,
                "key":key,
                "trade_regtype":trade_regtype,
                "trade_color":trade_color,
                "project_id":project_id,
                "show_tag":show_tag
            }
            t_user_relation=self.db.get('''
                    select group_concat(a.uid) gc from t_user_relation a
                    inner join t_user_relation b on
                        find_in_set(a.department_name,b.department_name)
                    and b.uid=%s and b.is_leader<>0
                    where a.uid!=b.uid and a.is_leader=0
                ''',uid)

            if show_tag=='relation':
                my_sql=' and c.id=(select max(project_id) from t_projects_member where member_id=%s and project_id=a.project_id) '%uid

            elif show_tag=='subordinate' and uid=='161':
                my_sql=' and created_uid=(select id from  t_user where role=10 and id=a.created_uid) '
            elif show_tag=='subordinate' and t_user_relation.gc!=None:
                my_sql=" and find_in_set(created_uid,'%s') "%str(t_user_relation.gc)
            if is_end:
                sql_where +=" and is_end =%s "%(is_end)
            elif status==0 or status  :
                if status==1 and todo=="7":
                    sql_where +=" and d.mile_by_at is not  null"
                elif status==0 and todo=="7":
                    sql_where +=" and d.mile_by_at is   null"
                if status and todo=="3":
                    sql_where +=" and d.state_id=%s"%(status)

                # else:
                #     sql_where +=" and d.state_id=%s"%(status)
            # else:
            #     sql_where +=" and d.state_id=%s"%(status)
            
            if trade_id.isdigit():
                sql_where+=" and a.id=%s "%trade_id
            if key:
                sql_where+="""
                    and ( trade_by like "%%"""+key+"""%%"
                    or trade_name='"""+key+"""' or  trade_number like "%%"""+key+"""%%" )
                """
                
                # " and (trade_by='{0}' or trade_name='{0}' or trade_number='{0}') ".format(key)
            if trade_regtype:
                sql_where+=" and a.trade_regtype='%s' "%trade_regtype
            if trade_color:
                sql_where+=" and a.trade_color='%s' "%trade_color
            if project_id:
                sql_where+=" and a.project_id=%s "%project_id
            if created_uid_name:
                sql_where+=" and a.created_uid_name='%s' "%created_uid_name
            if todo=='pending':
                sql_where+=" and  pending=1 and curr_mile_id=1 and is_end=0  "
            elif todo:
                sql_where+=" and is_end=0 "
                if todo=='1' :
                    sql_where+=' and pending=0 '
                sql_where +=" and curr_mile_id=%s"%(todo)
            pre_page=20
            every_counts=self.db.get('''
            SELECT count(*) a,
            (
                   SELECT count(*) 

             FROM  t_trade a 
              left join t_projects c on a.project_id=c.id 
                 inner join t_trade_milepost d on d.trade_id=a.id  and a.curr_mile_id=d.mile_id_order
                  where  is_close=0   and pending=1 and curr_mile_id=1 and is_end=0  '''+my_sql+'''
            )b,
            (
                 SELECT count(*) count FROM  t_trade a 
                  left join t_projects c on a.project_id=c.id 
                 inner join t_trade_milepost d on d.trade_id=a.id  and a.curr_mile_id=d.mile_id_order
                   where  is_close=0  and d.state_id=0  and curr_mile_id=1 and is_end=0  '''+my_sql+'''
            )c,
            (
                SELECT count(*) count FROM  t_trade a 
                 left join t_projects c on a.project_id=c.id 
                 inner join t_trade_milepost d on d.trade_id=a.id  and a.curr_mile_id=d.mile_id_order
                   where  is_close=0  and d.state_id=2  and curr_mile_id=1  and is_end=0'''+my_sql+'''
            )d,
            (
            SELECT count(*) count FROM  t_trade a 
             left join t_projects c on a.project_id=c.id 
            inner join t_trade_milepost d on d.trade_id=a.id  and a.curr_mile_id=d.mile_id_order
            where  is_close=0  and d.state_id=0  and curr_mile_id=2 and is_end=0'''+my_sql+'''
            )e,
            (
                 SELECT count(*) count FROM  t_trade a 
                  left join t_projects c on a.project_id=c.id 
                 inner join t_trade_milepost d on d.trade_id=a.id  and a.curr_mile_id=d.mile_id_order
                   where  is_close=0  and d.state_id=2  and curr_mile_id=2 and is_end=0'''+my_sql+''' 
            )f,
            (
                 SELECT count(*) count FROM  t_trade a 
                  left join t_projects c on a.project_id=c.id 
                 inner join t_trade_milepost d on d.trade_id=a.id  and a.curr_mile_id=d.mile_id_order
                   where  is_close=0  and d.state_id=0  and curr_mile_id=3  and is_end=0'''+my_sql+'''
            )g,
            (
                 SELECT count(*) count FROM  t_trade a 
                  left join t_projects c on a.project_id=c.id 
                 inner join t_trade_milepost d on d.trade_id=a.id  and a.curr_mile_id=d.mile_id_order
                   where  is_close=0  and d.state_id=2  and curr_mile_id=3 and is_end=0'''+my_sql+'''
            )h,
            (
                 SELECT count(*) count FROM  t_trade a 
                  left join t_projects c on a.project_id=c.id 
                 inner join t_trade_milepost d on d.trade_id=a.id  and a.curr_mile_id=d.mile_id_order
                   where  is_close=0  and d.state_id=3  and curr_mile_id=3 and is_end=0 '''+my_sql+'''
            )i,
            (
                 SELECT count(*) count FROM  t_trade a
                  left join t_projects c on a.project_id=c.id  
                 inner join t_trade_milepost d on d.trade_id=a.id  and a.curr_mile_id=d.mile_id_order
                   where  is_close=0  and d.state_id=4  and curr_mile_id=3 and is_end=0 '''+my_sql+'''
            )i1
            ,
            (
                 SELECT count(*) count FROM  t_trade a 
                  left join t_projects c on a.project_id=c.id 
                 inner join t_trade_milepost d on d.trade_id=a.id  and a.curr_mile_id=d.mile_id_order
                   where  is_close=0  and d.state_id=6  and curr_mile_id=3 and is_end=0 '''+my_sql+'''
            )i2,
            (
                 SELECT count(*) count FROM  t_trade a
                  left join t_projects c on a.project_id=c.id  
                 inner join t_trade_milepost d on d.trade_id=a.id  and a.curr_mile_id=d.mile_id_order
                   where  is_close=0  and d.state_id=0  and curr_mile_id=4 and is_end=0 '''+my_sql+'''
            )j,
            (
                 SELECT count(*) count FROM  t_trade a 
                  left join t_projects c on a.project_id=c.id 
                 inner join t_trade_milepost d on d.trade_id=a.id  and a.curr_mile_id=d.mile_id_order
                   where  is_close=0  and d.state_id=2  and curr_mile_id=4  and is_end=0 '''+my_sql+'''
            )k,
            (
                 SELECT count(*) count FROM  t_trade a 
                  left join t_projects c on a.project_id=c.id 
                 inner join t_trade_milepost d on d.trade_id=a.id  and a.curr_mile_id=d.mile_id_order
                   where  is_close=0  and d.state_id=0  and curr_mile_id=5 and is_end=0 '''+my_sql+'''
            )l,
            (
                SELECT count(*) count FROM  t_trade a 
                 left join t_projects c on a.project_id=c.id 
                 inner join t_trade_milepost d on d.trade_id=a.id  and a.curr_mile_id=d.mile_id_order
                   where  is_close=0  and d.state_id=0  and curr_mile_id=6  and is_end=0 '''+my_sql+'''
            )o,
            (
                 SELECT count(*) count FROM  t_trade a 
                  left join t_projects c on a.project_id=c.id 
                 inner join t_trade_milepost d on d.trade_id=a.id  and a.curr_mile_id=d.mile_id_order
                   where  is_close=0   and  mile_by_at is   null  and curr_mile_id=7 and is_end=0 '''+my_sql+'''
            )p,
            (
                 SELECT count(*) count FROM  t_trade a
                  left join t_projects c on a.project_id=c.id  
                 inner join t_trade_milepost d on d.trade_id=a.id  and a.curr_mile_id=d.mile_id_order
                   where  is_close=0  and  mile_by_at is not  null  and curr_mile_id=7 and is_end=0 '''+my_sql+'''
            )q,
            (
                SELECT count(*) count FROM  t_trade a 
                 left join t_projects c on a.project_id=c.id 
                 inner join t_trade_milepost d on d.trade_id=a.id  and a.curr_mile_id=d.mile_id_order
                   where  is_close=0  and is_end =1   '''+my_sql+'''
            )r
             FROM  t_trade a 
              left join t_projects c on a.project_id=c.id 
                 inner join t_trade_milepost d on d.trade_id=a.id  and a.curr_mile_id=d.mile_id_order
                  where    0=0   '''+my_sql)



            count = self.db.get(''' SELECT count(*) count FROM  t_trade a left join 
                (select project_id,group_concat(team_name,"|",member_name)  mbs   from t_projects_member where member_id > 0 group by project_id) b
                on a.project_id=b.project_id
                left join t_projects c on a.project_id=c.id
                 inner join t_trade_milepost d on d.trade_id=a.id  and a.curr_mile_id=d.mile_id_order
                  '''+my_sql+sql_where)
            pagination = Pagination(page, pre_page, count.count, self.request)
            startpage = (page-1) * pre_page
            t_trade = self.db.query('''
                SELECT  a.*,d.*,b.mbs,c.customer_name,c.guid project_guid,e.uid_name gj_name,e.message gj_message,
                e.created_at gj_created_at,f.uid_name cz_name,f.message cz_message,
                f.created_at cz_created_at
                from   t_trade a left join 
                (select project_id,group_concat(team_name,"|",member_name)  mbs   from t_projects_member where member_id > 0 group by project_id) b
                on a.project_id=b.project_id
                left join t_projects c on a.project_id=c.id 
               inner join t_trade_milepost d on d.trade_id=a.id and a.curr_mile_id=d.mile_id_order
                left join t_trade_msg e on e.trade_id=a.id and e.tag_type='跟进记录' and 
                e.id=(select max(id) from t_trade_msg where trade_id=a.id and tag_type='跟进记录')          
                left join t_trade_msg f on f.trade_id=a.id and f.tag_type='操作记录' and 
                f.id=(select max(id) from t_trade_msg where trade_id=a.id and tag_type='操作记录')   
                   where  0=0 '''+my_sql+sql_where+'''
                order by created_at desc limit %s,%s
                ''',startpage,pre_page)

            
            t_mile_type = self.db.query("select * from t_projects_type where income_category='商标' order by order_int ")
            t_trade_color=self.db.query(' select * from t_trade_color ')

            return self.render('trade/trade_list.html'
            ,paramas=paramas,pagination=pagination,
            t_trade_color=t_trade_color,
            t_mile_type=t_mile_type,t_trade=t_trade,
            search_key=search_key,todo=todo,
            my=my,get_member=tools.get_member,
            t_user_relation=t_user_relation,
            form_tag="list",every_counts=every_counts)
        elif tag=="show":
            id = self.get_argument("id")
            if not id:
                return self.write("id is null")
            t_trade = self.db.get("select * from t_trade where id=%s",id)
            t_project = None
            t_proejct_member_arr = None
            if t_trade.project_id:
                t_project = self.db.get('select * from t_projects where id=%s',t_trade.project_id)
                if t_project:
                    t_proejct_member = self.db.get('select project_id,group_concat(team_name,"|",member_name)  mbs   from t_projects_member where member_id > 0 and project_id=%s group by project_id ',t_project.id)
                    if t_proejct_member:
                        t_proejct_member_arr = t_proejct_member.mbs
            t_trade_msg =self.db.query(' select *,date_format(created_at,"%%Y-%%m-%%d")=date_format(now(),"%%Y-%%m-%%d") is_current_day from t_trade_msg where trade_id=%s order by created_at desc,id desc ',id)
            t_trade_milepost_his = self.db.query("select * from t_trade_milepost_his where trade_id=%s",id)
            t_trade_file = self.db.query("select * from t_trade_file where trade_id=%s order by file_by_at desc",id)
            t_trade_milepost = self.db.query("select * from t_trade_milepost where trade_id=%s order by mile_id_order  ",id)
            t_trade_primary=self.db.query(' select * from t_trade_primary where trade_id=%s',id)
            t_trade_color=self.db.query(' select * from t_trade_color ')
            return self.render('trade/trade_show.html',get_member=tools.get_member,t_trade=t_trade,search_key=search_key,t_project=t_project,t_trade_msg=t_trade_msg,t_proejct_member_arr=t_proejct_member_arr,
                                t_trade_milepost_his=t_trade_milepost_his,form_tag="list",t_trade_file=t_trade_file,t_trade_milepost=t_trade_milepost,t_trade_primary=t_trade_primary,t_trade_color=t_trade_color)
    def post(self):
        tag = self.get_argument("tag","")
        uid = self.get_secure_cookie("uid")
        uid_name=self.get_secure_cookie('name')
        page=int(self.get_argument('page',1))
        my = self.get_argument("my","1")
        role = self.get_secure_cookie("role")
        dt = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        if tag=="add":
            trade_name = self.get_argument("trade_name","")
            trade_number = self.get_argument("trade_number","")            
            trade_by = self.get_argument("trade_by","")            
            trade_regtype = self.get_argument("trade_regtype","")            
            trade_color = self.get_argument("trade_color","")            
            project_id = self.get_argument("project_id","")            
            trade_remark = self.get_argument("trade_remark","")     
            trade_id=self.get_argument('trade_id','')
            delete_trade_id=self.get_argument('delete_trade_id','')
            trade_reg_at=self.get_argument('trade_reg_at','')
            if not trade_reg_at:
                trade_reg_at=None
            if delete_trade_id:
                result=self.db.execute(' delete from t_trade where id=%s ',delete_trade_id)
                return self.write(str(result))
            if not trade_name :
                return self.write("商标名称不能为空哦")
            if trade_id:
                t_trade=self.db.get(' select * from t_trade where id=%s ',trade_id)
                self.db.execute("""
                update t_trade set  trade_reg_at=%s,trade_name=%s,trade_number=%s,trade_by=%s,
                trade_regtype=%s,trade_color=%s,project_id=%s,trade_remark=%s where id=%s
                """,trade_reg_at,trade_name,trade_number,trade_by,trade_regtype,trade_color,project_id,trade_remark,trade_id)
                txt=''
                if t_trade.trade_name!=trade_name:
                    txt+='商标名称:'+t_trade.trade_name+' 修改为 '+trade_name
                if t_trade.trade_number!=trade_number:
                    txt+='商标申请号:'+t_trade.trade_number+' 修改为 '+trade_number
                if t_trade.trade_by!=trade_by:
                    txt+='商标申请人:'+t_trade.trade_by+' 修改为 '+trade_by

                if t_trade.trade_regtype!=trade_regtype:
                    txt+='申请类别:'+t_trade.trade_regtype+' 修改为 '+trade_regtype

                if t_trade.trade_color!=trade_color:
                    txt+='申请颜色:'+t_trade.trade_color+' 修改为 '+trade_color
                if t_trade.project_id!=int(project_id):
                    txt+='业务订单号:'+str(t_trade.trade_name)+' 修改为 '+trade_name
                if t_trade.trade_remark!=trade_remark:
                    txt+='备注:'+t_trade.trade_remark+' 修改为 '+trade_remark
                self.db.execute('''
                insert into t_trade_msg(uid,uid_name,message,created_at,trade_id,tag_type,btype_id)
                values(%s,%s,%s,%s,%s,%s,%s)
            ''',uid,uid_name,txt,dt,trade_id,'操作记录','2')
            else:
                result_id = self.db.execute("""insert into t_trade(trade_reg_at,trade_name,trade_number,trade_by,trade_regtype,trade_color,project_id,trade_remark,created_at,created_uid,created_uid_name,curr_mile_id)
                values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,1)
                """,trade_reg_at,trade_name,trade_number,trade_by,trade_regtype,trade_color,project_id,trade_remark,dt,uid,uid_name)
                if result_id:
                    self.db.execute("""
                        insert into t_trade_milepost(trade_id,mile_id_order,mile_id_name,mile_id_other_name)
                        select %s,order_int,income_name,other_name from t_projects_type where income_category='商标'
                    """,result_id)
                return self.write(str(result_id))
        elif tag=="trade_number":
            trade_id = self.get_argument("trade_id")
            trade_number = self.get_argument("trade_number","")
            if not trade_id:
                return self.write("not trade id")
            result = self.db.execute("update t_trade set trade_number=%s where id=%s",trade_number,trade_id)
            self.write(str(result))
        elif tag=="is_end":
            trade_id = self.get_argument("trade_id")
            is_end = self.get_argument("is_end")
            is_end_remark = self.get_argument("is_end_remark","")
            if not trade_id:
                return self.write("not trade id")
            result = self.db.execute("update t_trade set is_end=%s,is_end_at=%s,is_end_uid=%s,is_end_uid_name=%s,is_end_remark=%s where id=%s",
            is_end,dt,uid,uid_name,is_end_remark,trade_id)
            self.write(str(result))


        elif tag=="set_milepost":
            trade_id = self.get_argument("trade_id")
            mile_id = int(self.get_argument("mile_id"))
            state_id_remark = self.get_argument("state_id_remark","")
            state_id = int(self.get_argument("state_id",0))
            state_id_name = self.get_argument("state_id_name","")
            his_id = self.get_argument("his_id",0)
            t_milepost = self.db.get("select * from t_trade_milepost where mile_id=%s",mile_id)
            if  not t_milepost:
                return self.write("not mile_Id")

            end_sql=""
            t_milepost_his = None
            if his_id:
                t_milepost_his = self.db.get("select * from t_trade_milepost_his where his_id=%s",his_id)
            is_end_project = False #or t_milepost.mile_id_order==2
            # if (t_milepost.mile_id_order==1 ) and state_id and   state_id==2 :
            #     is_end_project = True
            if t_milepost.mile_id_order==3 and t_milepost_his and   t_milepost.state_id==3 and state_id==3:
                is_end_project = True
            elif t_milepost.mile_id_order==4 and t_milepost_his  and state_id==3:
                is_end_project = True

            if is_end_project:
                end_sql ="   ,is_end=1,is_end_at='%s',is_end_uid='%s',is_end_uid_name='%s',is_end_remark='%s' "%(
                    dt,uid,uid_name,state_id_remark
                )
            is_his = False
            if (t_milepost.mile_id_order==3 or  t_milepost.mile_id_order==4) and (int(state_id)==2 or int(state_id)==4  or int(state_id)==6  )   :
                is_his = True
            elif   t_milepost.mile_id_order==3 and  state_id_name=="全部驳回" and int(state_id)==3   :
                is_his = True
            elif t_milepost.mile_id_order==3 and t_milepost_his and t_milepost_his.his_name=="部分驳回" and state_id_name!="初审" :
                is_his = True
            if is_his :
                his_order=self.db.get("select count(*) c from t_trade_milepost_his where mile_id=%s",mile_id)
                self.db.execute("""
                    insert into t_trade_milepost_his(his_order,his_name,his_at,his_uid,his_uid_name,mile_id,trade_id,his_remark)
                    values(%s,%s,%s,%s,%s,%s,%s,%s)
                """,his_order.c+1,state_id_name,dt,uid,uid_name,mile_id,trade_id,state_id_remark)  

                      
            result = self.db.execute("""
                update t_trade_milepost set mile_by_at=%s,
                mile_by_uid=%s,mile_by_uid_name=%s,state_id_remark=%s,
                state_id=%s,state_id_name=%s  where mile_id=%s
            """,dt,uid,uid_name,state_id_remark,state_id,state_id_name,mile_id)
            if result==0:
                curr_mile_order= t_milepost.mile_id_order
                if t_milepost_his:
                    print int(state_id) ==1 or (int(state_id) ==3 and  t_milepost_his.his_name=="部分驳回" and  t_milepost.mile_id_order==3)
                    print state_id,t_milepost_his.his_name,t_milepost.mile_id_order
                if int(state_id) ==1 or (int(state_id) ==3 and t_milepost_his and   t_milepost_his.his_name=="部分驳回" and  t_milepost.mile_id_order==3):
                    curr_mile_order = curr_mile_order+1
                
                # if t_milepost.mile_id_order==1:
                #     end_sql=", trade_reg_at='%s' "%(dt) //不用自动填写
                self.db.execute("""
                            update t_trade set curr_mile_id=%s """+end_sql+""" where id=%s
                        """,curr_mile_order,trade_id)
                if state_id_remark:
                    state_id_remark=',备注:'+state_id_remark
                self.db.execute('''
                insert into t_trade_msg(uid,uid_name,message,created_at,trade_id,tag_type,btype_id)
                values(%s,%s,%s,%s,%s,%s,%s)
            ''',uid,uid_name,'阶段 '+str(t_milepost.mile_id_order)+t_milepost.mile_id_name+':'+state_id_name+state_id_remark,dt,trade_id,'操作记录','2')

                

            if his_id:
                    self.db.execute("""update t_trade_milepost_his set 
                    state_id=%s,state_id_name=%s,state_id_at=%s,state_uid=%s,state_uid_name=%s  where his_id=%s
                    """,state_id,state_id_name,dt,uid,uid_name,his_id)

            self.write(str(result))
        elif tag=="rollback":
            trade_id = self.get_argument("trade_id")
            mile_id = self.get_argument("mile_id")
            his_id = self.get_argument("his_id")
            self.db.execute("""
                update t_trade_milepost_his set 
                  state_id=0,state_id_name=NULL,state_id_at=NULL,state_uid=0,state_uid_name=NULL ,
                 his_continue=0,
                his_continue_at=NULL,
                his_continue_uid=0,his_continue_uid_name=NULL,his_continue_remark=NULL,his_continue_name=NULL
                where his_id=%s
            """,his_id)         
            result = self.db.execute("update t_trade set is_end=0,is_end_at=NULL,is_end_uid=0,is_end_uid_name=NULL,is_end_remark=NULL where id=%s",trade_id)
   

        elif tag=="save_trans":
            trade_id = self.get_argument("trade_id")
            mile_id = self.get_argument("mile_id")
            state_id_remark = self.get_argument("state_id_remark")
            t_milepost = self.db.get("select * from t_trade_milepost where mile_id=%s",mile_id)

            result = self.db.execute("""
                update t_trade_milepost set mile_by_at=%s,
                mile_by_uid=%s,mile_by_uid_name=%s,state_id_remark=%s,
                trade_id=%s where mile_id=%s
            """,dt,uid,uid_name,state_id_remark,trade_id,mile_id)
            if state_id_remark:
                state_id_remark=' 备注:'+state_id_remark
            self.db.execute('''
                insert into t_trade_msg(uid,uid_name,message,created_at,trade_id,tag_type,btype_id)
                values(%s,%s,%s,%s,%s,%s,%s)
            ''',uid,uid_name,'阶段 '+str(t_milepost.mile_id_order)+t_milepost.mile_id_name+
            state_id_remark
            ,dt,trade_id,'操作记录','2')
            self.write(str(result))
        elif tag=="his_continue":
            his_continue = self.get_argument("his_continue")
            his_continue_name = self.get_argument("his_continue_name")            
            his_id = self.get_argument("his_id")
            mile_id = self.get_argument("mile_id")
            trade_id = self.get_argument("trade_id")
            his_continue_remark = self.get_argument("his_continue_remark","")
            t_milepost = self.db.get("select * from t_trade_milepost where mile_id=%s",mile_id)

            result = self.db.execute("""
                update t_trade_milepost_his set 
                his_continue=%s,
                his_continue_at=%s,
                his_continue_uid=%s,his_continue_uid_name=%s,his_continue_remark=%s,his_continue_name=%s
                 where his_id=%s
            """,his_continue,dt,uid,uid_name,his_continue_remark,his_continue_name,his_id)

            self.db.execute('''
                insert into t_trade_msg(uid,uid_name,message,created_at,trade_id,tag_type,btype_id)
                values(%s,%s,%s,%s,%s,%s,%s)
            ''',uid,uid_name,'阶段 '+str(t_milepost.mile_id_order)+t_milepost.mile_id_name+"客户意见("+ his_continue_name +")"+ his_continue_remark
            ,dt,trade_id,'操作记录','2')
            self.write(str(result))

        elif tag=="cert":
            trade_id = self.get_argument("trade_id")
            mile_id = self.get_argument("mile_id")
            cert_remark = self.get_argument("cert_remark","")
            cert_at = self.get_argument("cert_at","")
            t_milepost = self.db.get("select * from t_trade_milepost where mile_id=%s",mile_id)
            if  not t_milepost:
                return self.write("not mile_Id")
            result = self.db.execute("""
                update t_trade_milepost set mile_by_at=%s,
                mile_by_uid=%s,mile_by_uid_name=%s,cert_remark=%s,
                cert_at=%s where mile_id=%s
            """,dt,uid,uid_name,cert_remark,cert_at,mile_id)
            if result==0:
                curr_mile_order= t_milepost.mile_id_order+1
                self.db.execute("""
                            update t_trade set curr_mile_id=%s where id=%s
                        """,curr_mile_order,trade_id)
                if cert_remark:
                    cert_remark=',备注:'+cert_remark
                self.db.execute('''
                insert into t_trade_msg(uid,uid_name,message,created_at,trade_id,tag_type,btype_id)
                values(%s,%s,%s,%s,%s,%s,%s)
            ''',uid,uid_name,'阶段 '+str(t_milepost.mile_id_order)+t_milepost.mile_id_name+
            ':电子证书信息时间:'+cert_at+cert_remark
            ,dt,trade_id,'操作记录','2')

            self.write(str(result))

        elif tag=="upload":
            is_upload = 0
            type_name = self.get_argument("type_name")
            trade_remark= self.get_argument("trade_remark","")
            trade_id = self.get_argument("trade_id","")
            mile_id = self.get_argument("mile_id",0)
            his_id = self.get_argument("his_id",0)
            tag_from =self.get_argument("tag_from","")
            print len(self.request.files.items()),"====="
            for k,file1 in self.request.files.items():
                
                ori_filename = file1[0].filename
                filename_full = options.upload_path + "/customer/trade/%s/" % (
                        trade_id)
                url_path = "/static/customer/trade/%s/" % (trade_id)
                try:
                    os.makedirs(filename_full)
                except OSError:
                    if not os.path.isdir(filename_full):
                        raise
                extension = os.path.splitext(ori_filename)[1]

                uuid_str = str(uuid.uuid4())
                fname = "{0}_{1}{2}".format(uuid_str, trade_id,
                                                extension)

                save_full_path = filename_full + fname
                url_fname = "{0}{1}".format(url_path, fname)
                print save_full_path,save_full_path
                output_file = open(save_full_path, 'w')
                output_file.write(file1[0]["body"])
                is_upload= is_upload+1
                self.db.execute("""insert into t_trade_file(type_name,
                file_path,file_by,file_by_uid,file_by_at,trade_id,remark,source_name,mile_id,his_id)
                values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)""",
                type_name,url_fname,uid_name,uid,dt,trade_id,trade_remark,ori_filename,mile_id,his_id
                )

            data = {'result':is_upload}   
            return self.write(json.dumps(data))
        
        elif tag=="trade_msg":
            trade_id=self.get_argument('trade_id','')
            txt_msg=self.get_argument('txt_msg','')
            file_path=None
            is_upload = False
            try:
                file1 = self.request.files['file'][0]
                is_upload = True
            except:
                pass
            if is_upload:
                ori_filename = file1["filename"]
                filename_full = options.upload_path + "/trade/%s/" % (
                    trade_id)
                url_path = "/static/trade/%s/" % (trade_id)
                try:
                    os.makedirs(filename_full)
                except OSError:
                    if not os.path.isdir(filename_full):
                        raise
                extension = os.path.splitext(ori_filename)[1]

                uuid_str = str(uuid.uuid4())
                fname = "{0}_{1}{2}".format(uuid_str, trade_id,
                                            extension)

                save_full_path = filename_full + fname
                url_fname = "{0}{1}".format(url_path, fname)

                output_file = open(save_full_path, 'w')
                output_file.write(file1["body"])
                file_path = url_fname
            self.db.execute('''
                insert into t_trade_msg(uid,uid_name,message,created_at,trade_id,tag_type,btype_id,file_path)
                values(%s,%s,%s,%s,%s,%s,%s,%s)
            ''',uid,uid_name,txt_msg,dt,trade_id,'跟进记录','3',file_path)

        elif tag=="delete_trade_msg":
            msg_id=self.get_argument('msg_id')
            edit_msg=self.get_argument('edit_msg','')
            msg=self.get_argument('msg','')
            if edit_msg:
                self.db.execute(''' update t_trade_msg set message=%s where id=%s ''',msg,msg_id)
            else:
                self.db.execute(' delete from t_trade_msg where id=%s ',msg_id)

        elif tag=='delete_trade_file':
            trade_file_id=self.get_argument('trade_file_id')

            self.db.execute(' delete from t_trade_file where id=%s ',trade_file_id)