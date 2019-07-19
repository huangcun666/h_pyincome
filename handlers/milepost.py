# -*- coding: utf-8 -*-
from Pagination import Pagination
import tornado
from handlers.base import BaseHandler
import uuid, os, datetime
from tornado.options import define, options
import msg
import json
import events

class MilePostHandler(BaseHandler):
    def get(self):
        id = self.get_argument("id")
        guid = self.get_argument("guid")

        tag = self.get_argument("tag","milepost_project")
        if tag =="milepost_project":
            btypeid= self.get_argument("btypeid")

            project_cq = self.db.query("select * from t_projects_member where project_id=%s and team_id=38",id)
            project_btypes = self.db.query(
                "select * from t_projects_type where income_category='业务分类'",
                )
            project_milepost = self.db.query("select * from t_projects_milepost where project_id=%s",id)
            t_project = self.db.get('select * from t_projects where id=%s',id)
            project_milepost_item = self.db.get(
                'select * from t_projects_type where id=%s', btypeid)
            project_milepost_type = self.db.query(
                "select *,b.order_int border_int from t_projects_type a  inner join t_projects_milepost b on b.type_id=a.id where income_category='办结' and project_id=%s order by b.order_int",id
            )



            return self.render(
                "milepost/milepost_project.html",
                project_milepost_type=project_milepost_type,
                project_milepost_item=project_milepost_item,
                search_key="",
                t_project=t_project,
                project_milepost=project_milepost,
                project_btypes=project_btypes,
                project_cq=project_cq)



    def post(self):
        tag = self.get_argument("tag")
        uid = self.get_secure_cookie("uid")
        uid_name = self.get_secure_cookie("name")
        dt=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        # print "mile", tag
        if tag == "confirm":
            mid = self.get_argument("mid",0)
            mp_id = self.get_argument("mp_id")
            guid = self.get_argument("guid")
            project_id = self.get_argument("project_id")
            update_id = self.get_argument("update_id",0)
            is_close = self.get_argument("is_close")
            btype_id_name=self.get_argument('btype_id_name','')
            milepost = self.db.get("select * from t_projects_milepost where id=%s",mp_id)
            customer_id=self.get_argument('customer_id','0')
            bresult = 1
            # print "milepost===============",
            if not milepost:
                self.write("not milepost")
            else:
                t_project=self.db.get('''
                    select * from t_projects where customer_company!='' and company_uid!='' and comany_person!='' and true_reg_addr!=''
                     and company_created_day is not null and (company_expired_day  is not null or company_fever!=0) and city!='' and zone!='' and id=%s
                ''',project_id)


                if milepost.type_name==u'填写办结信息':
                    t_projects_transfile = self.db.get('''
                        select * from t_projects_transfile where project_id=%s and pm_id=%s and mtype=1
                        ''', project_id, milepost.member_id)
                    if not t_projects_transfile:
                        return self.write("wrong_tran")
                    elif not  t_project and btype_id_name!="公司注销":
                        # print "l.......1"
                        return self.write("-100") #需要补资料
                elif milepost.type_name==u'仓管通知销售交接':
                    t_projects_transfile = self.db.get('''
                        select * from t_projects_transfile where project_id=%s and pm_id=%s and mtype=1 and cq_uid =0
                        ''', project_id, milepost.member_id)
                    # t_projects_transfile_sales = self.db.get('''
                    #     select * from t_projects_transfile where project_id=%s and pm_id=%s and mtype=2
                    #     ''', project_id, milepost.member_id)
                    if  t_projects_transfile:
                        return self.write("not_confirm_cg") #仓管没有确认

                    # elif not  t_projects_transfile_sales:
                    #     return self.write("wrong_tran_sales")
                    elif not t_project and btype_id_name!="公司注销":
                        # print "l.......2", btype_id_name
                        return self.write("-100")  #需要补资料


                    else:
                        if is_close == "1":
                            t_projects_type = self.db.get(
                                    "select * from t_projects_type  where income_name='仓管确认交接完成'"
                                )
                            if not t_projects_type:
                                return self.write("not t_projects_type")

                            bresult = self.db.execute("""
                                update t_projects_milepost set confirm_at=%s,uid=%s,uid_name=%s where id=%s 
                            """, dt, uid, uid_name, mp_id)

                            if bresult == 0:
                                bresult = self.db.execute(
                                    """
                                    update t_projects_milepost set is_close=1
                                    where member_id=%s and project_id=%s 
                                """, milepost.member_id,
                                    project_id)

                                bresult = self.db.execute(
                                    """
                                    update t_projects_milepost set confirm_at=%s,uid=%s,uid_name=%s
                                    where member_id=%s and project_id=%s  and order_int=8
                                """, dt, uid, uid_name, milepost.member_id,project_id)

                                bresult = self.db.execute(
                                    """ update t_projects_member set
                                        last_milepost_id=%s ,
                                        last_milepost_id_name=%s , 
                                        last_milepost_id_at=%s ,
                                        is_close=1
                                        where mid=%s and project_id=%s 
                                    """, t_projects_type.id,
                                         t_projects_type.income_name,
                                         dt,
                                         milepost.member_id,
                                         project_id)
                                
                              
                            return self.write(str(bresult))
                elif milepost.type_name == u'仓管确认交接完成':
                    if mid :
                        self.db.execute("""
                                update t_projects_transition set rec_by_uid_at=%s where project_id=%s and mid=%s and is_customer=1
                            """,dt,project_id,mid)
                    
                # elif milepost.type_name==u"销售顾问接受交接":
                #     t_projects_transfile = self.db.get('''
                #     select * from t_projects_transfile where project_id=%s and pm_id=%s and mtype=2 and cq_uid != 0
                #     ''', project_id, mid)  # 检查
                #     if not t_projects_transfile:
                #         return self.write("not_confirm_sales")

                t_project1=self.db.get('''
                  select aa.* from (
                                    select 
                                    ifnull(((all_income+ifnull(other_money,0)) -( ifnull(b.income_money,0)+ifnull(daishou_money,0))),0) qk
                                    from t_projects a 
                                    left join (select b1.project_id,ifnull(sum(income_money),0) income_money from t_projects_income b1 ,t_projects_income_title b2 where
                                    b1.parent_id=b2.id and income_id <=43 and  income_uid > 0   group by b1.project_id) b 
                                    on a.id=b.project_id 
                                    left join (select project_id,ifnull(sum(income_money),0) other_money from t_projects_income_other  group by project_id) c 
                                    on a.id=c.project_id 
                                    left join (select e1.project_id,ifnull(sum(income_money),0) daishou_money from t_projects_income e1,t_projects_income_title e2 where 
                                    e1.parent_id=e2.id and 
                                    income_id >43  and  income_uid > 0  group by e1.project_id) e 
                                    on a.id=e.project_id  where a.id=%s
                                    group by a.id) aa where  qk <> 0
                
                ''',project_id)

                bresult = self.db.execute("""
                    update t_projects_milepost set confirm_at=%s,uid=%s,uid_name=%s where id=%s 
                """, dt, uid, uid_name, mp_id)
              
                if t_project1 and milepost.type_name=='办结':
                    if t_project1.qk!=0:
                        self.db.execute('''
                        update t_projects  set is_finance_project=1 where id=%s
                        ''',project_id)


                self.db.execute(
                        """update t_projects_member set last_milepost_id=%s ,
                        last_milepost_id_name=%s , last_milepost_id_at=%s where mid=%s """,
                        milepost.type_id, milepost.type_name, dt,
                        milepost.member_id)
               
                t_projects_member = self.db.get(
                    " select * from t_projects_member where mid=%s and project_id=%s",
                    milepost.member_id, project_id)
                if t_projects_member:
                    if milepost.type_name != u'待接单' or  milepost.type_name != u'办理中' and  t_projects_member.btype_id_name==u"公司注册" :
                        self.db.execute(
                            "update t_projects set reg_state=2 where id=%s",
                            project_id)
                events.add_project_event(self, project_id,'订单流转('+milepost.btype_name+')',milepost.type_name,
                                         uid, uid_name,customer_id)

                return self.write(str(bresult))
        elif tag == "group_confirm": #批量接单
            mid = self.get_argument("mid")

            result =1
            for item in mid.split(","):
                # print "item",item
                milepost = self.db.query(
                    "select * from t_projects_milepost where member_id=%s and confirm_at is null and (order_int=1 or order_int=2) order by order_int ",
                    item)
                for row in milepost:
                    bresult = self.db.execute("""
                        update t_projects_milepost set 
                        confirm_at=%s,uid=%s,uid_name=%s 
                        where id=%s  
                    """, dt, uid, uid_name, row.id)
                    # print "bresult", bresult, "row.id0", row.id
                    if row.order_int == 2:

                        self.db.execute(
                            """update t_projects_member set last_milepost_id=%s ,
                            last_milepost_id_name=%s , last_milepost_id_at=%s where mid=%s and project_id=%s""",
                            row.type_id, row.type_name, dt, item,
                            row.project_id)
            self.write(str(result))
        elif tag == "group_confirm_other":
            mid = self.get_argument("mid")
            type_name = self.get_argument("type_name")
            result = 1
            for item in mid.split(","):
                # print item,type_name,"....."
                milepost = self.db.query(
                    "select * from t_projects_milepost where member_id=%s and confirm_at is null and (type_name=%s) order by order_int ",
                    item, type_name)
                for row in milepost:
                    # print item,type_name,".....",row
                    bresult = self.db.execute("""
                        update t_projects_milepost set 
                        confirm_at=%s,uid=%s,uid_name=%s 
                        where id=%s  
                    """, dt, uid, uid_name, row.id)
                    if bresult ==0:
                        result = self.db.execute(
                                """update t_projects_member set last_milepost_id=%s ,
                                last_milepost_id_name=%s , last_milepost_id_at=%s where mid=%s and project_id=%s""",
                                row.type_id, row.type_name, dt, item,row.project_id)
                        if result==0:
                            self.db.execute("update t_projects set category_id=0 ,category_id_name=NULL where id=%s",row.project_id)

            self.write(str(result))
        elif tag == "reset_category":
            category_id = self.get_argument("category_id")
            if not category_id:
                self.write("not category_id")
            else:
                result =     self.db.execute(
                    "update t_projects set category_id=0 ,category_id_name=NULL where category_id=%s ",
                    category_id)
                self.write(str(result))

        elif tag =="update_remark":
            mp_id = self.get_argument("mp_id")
            guid = self.get_argument("guid")
            remark = self.get_argument("milepost_remark","")
            dt=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            project_id = self.get_argument("project_id")
            result = self.db.execute("""
                update t_projects_milepost set confirm_at=%s,remark=%s where id=%s and project_id=%s
            """,dt,remark, mp_id,project_id)
            self.write(str(result))
