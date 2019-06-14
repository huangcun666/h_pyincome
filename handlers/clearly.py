# encoding=utf8
from handlers.base import BaseHandler
import logging,datetime
from Pagination import Pagination
logger = logging.getLogger('boilerplate.' + __name__)
from tornado.options import define, options
import tornado,json,os,uuid,events
import uuid

class  ClearlyHandler(BaseHandler):
    def get_project_info(self,project_id):
        project_info = ""
        if project_id:
            t_project = self.db.get("select * from t_projects where id=%s",project_id)
            if t_project:
                project_info ="<a target='_blank' style='font-size:12px;' href='/project?tag=show&guid={}&id={}'><i class='   icon-external-link'></i>{}</a><br/>" .format(t_project.guid,t_project.id,t_project.project_name)
            else:
                project_info="<i class=' icon-remove'></i> <font color='red'>{}订单不存在.</font><br/>".format(project_id)
        

        return project_info
    def get_clearly_stat(self,clearly_id,dt2):
        t_clearly = self.db_customer.get("select * from t_customer_clearly where id=%s",clearly_id)
        if t_clearly:
            t_count_clearly= self.db_customer.get("select count(distinct(date(uid_at))) c from t_customer_clearly_msg where clearly_id=%s ",clearly_id)
            msg=""
            t_customer_clearly_msg = self.db_customer.get("select * from t_customer_clearly_msg where clearly_id=%s order by uid_at desc limit 1",clearly_id)
            if t_customer_clearly_msg:
                msg = "<br/><i class=' icon-comments-alt'></i>最新跟进:<br/>{} ({} {})".format(t_customer_clearly_msg.ass_msg,t_customer_clearly_msg.uid_name,t_customer_clearly_msg.uid_at)
            return "<font color='red'>跟进{}天{}次</font> {}".format(self.diff_date(t_clearly.ass_uid_by_at,dt2),t_count_clearly.c,msg)
    
    def get_comcompany_logout(self,customer_id):
        pass

    
    def get_except_tag(self,customer_id):
        t_customer_clearly_except = self.db_customer.get("select * from t_customer_clearly_except where customer_id=%s",customer_id)
        if t_customer_clearly_except:

            return_s =t_customer_clearly_except.except_tag_vals+  """ <a href="javascript:void(0)" class="btn btn-info btn-mini a_excpet_tag"
            customer_id="{}"  except_tag_ids="{}" except_remark="{}">设置</a> <font color='red'>{}</font>""".format(customer_id,t_customer_clearly_except.except_tag_ids,t_customer_clearly_except.except_remark,t_customer_clearly_except.except_remark)
            return return_s

        else:
            return """<a href="javascript:void(0)" class="btn btn-info btn-mini a_excpet_tag"
             customer_id="{}" except_remark="" except_tag_ids="">设置</a>""".format(customer_id)
          

    def diff_date(self, dt1, dt2):
        if dt1:
            return (datetime.datetime.strptime(dt2,"%Y-%m-%d %H:%M:%S")-dt1).days

    def get_clearly_info(self,clearly_id):
        strs=""
        if clearly_id:
            t_customer_clearly_milepost = self.db_cust.get("select * from  t_customer_clearly_milepost where clearly_id=%s ",clearly_id)
            if customer.ass_end_confirm:
                result_id_str = ""
                if customer.result_id==3:
                    result_id_str ="(无需处理)"
                else:
                    result_id_str ="办结"

                strs+= " 1.申请{}({}){}".format(result_id_str,customer.ass_uid_name,customer.ass_end_confirm)

        return strs

    def get_clearly_info(self,customer):
        strs=""
        clearly_id = customer.clearly_id
        if clearly_id:
            t_customer_clearly_milepost = self.db_customer.query("select * from  t_customer_clearly_milepost where clearly_id=%s order by mbtype_id ",clearly_id)
           
            if not t_customer_clearly_milepost:
                if customer.state_id==2:
                    return '<td><div class="alert alert-info">待冯恒冠分配跟进人</div></td><td ><div class="alert alert-primary">待冯恒冠分配跟进人</div></td>'.format(customer.state_id_name)
                elif customer.state_id==1:
                    return '<td><div class="alert alert-warning">待李江友设置指导价</div></td><td ><div class="alert alert-primary">待李江友设置指导价</div></td>'.format(customer.state_id_name)   
                        
 
            else:
                for item  in  t_customer_clearly_milepost:
                    strs+="<td style='vertical-align:top'>"
                    result_id_str = ""
                    if item.ass_end_confirm:
                        if item.result_id==3:
                            result_id_str ="(无需处理)"
                        else:
                            result_id_str ="办结"
                        strs+= " 1.申请{}{}({}){} <span class='text-primary' style='color:blue;'><i class=' icon-legal'></i> 业务金额: {}元</span> ".format(item.mbtype_id_name,result_id_str,item.ass_uid_name,item.ass_end_confirm,item.amount)
                    else:
                        strs+= " <div class='alert alert-primary'>{}跟进处理中 {}</div>".format(item.uid_name,item.uid_at)
                    if item.ass_leader_uid_at:
                        strs+="<br/> 2.确认办结({}){}".format(item.ass_leader_uid_name,item.ass_leader_uid_at)
                    if item.year_end_remark:
                        strs+="(备注:{})".format(item.year_end_remark)
                    if item.clearly_end_remark:
                        strs+="(备注:{})".format(item.clearly_end_remark)
                    if item.finance_uid_at:
                        strs+=" <br/>3.财务审核({}){}".format(item.finance_uid_name,item.finance_uid_at)
                    if item.milepost_rollback_remark:
                        strs+=' <br/><span style="color:red;">{} 曾于 {}驳回,<br/>原因:  {}</span>'.format(item.milepost_rollback_uid_name,item.milepost_rollback_at,item.milepost_rollback_remark)
                    if item.clearly_end_at:
                        strs+='<br/>4.({})发起{}办结{}'.format(item.clearly_end_uid_name,item.mbtype_id_name,item.clearly_end_at)
                        for idx,file in enumerate(item.clearly_end_file.split('|')):
                            if file:
                                strs+='''<font color='red'><a href="{}" title="{}" target="_blank"><i class="icon-large icon-picture "></i>附件{}</a> '''.format(
                                        file,file.split('/')[-1],idx+1

                                )
                                # strs+='''<a class="delete_file" href="javascript:;" milepost_id="{}" title="删除 {}" file_type="clearly_end_file" file_path="{}" ><font color='red'>[删除]</a ></a></font>&nbsp;'''.format(
                                #             item.id,file.split('/')[-1],file
                                # )
                        strs+='''<a class="upload_file btn btn-small btn-info" 
                        ass_end_remark="{}"
                         href="javascript:;" hide_clear_id='1' file_path={}"
                          file_type="clearly_end_file" milepost_id="{}" 
                          clearly_id="{}" >[修改办结附件/备注]</a >
                        '''.format(item.clearly_end_remark,item.clearly_end_file,item.id,item.clearly_id,)
                    if item.year_end_at:
                        strs+='<br/>4.({})发起{}办结{}'.format(item.year_end_uid_name,item.mbtype_id_name,item.year_end_at)
                        for idx,file in enumerate(item.year_end_file.split('|')):
                            if file:
                                strs+='''<font color='red'><a href="{}" title="{}" target="_blank"><i class="icon-large icon-picture "></i>附件{}</a> '''.format(
                                        file,file.split('/')[-1],idx+1

                                )
                                strs+='''<a class="delete_file" href="javascript:;" milepost_id="{}" title="删除 {}" file_type="year_end_file" file_path="{}" ><font color='red'>[删除]</a ></a></font>&nbsp;'''.format(
                                            item.id,file.split('/')[-1],file
                                )
                        # strs+='''<a class="upload_file btn btn-small btn-info" 
                        # ass_end_remark="{}"
                        #  href="javascript:;" hide_clear_id='1' file_path={}"
                        #   file_type="year_end_file" milepost_id="{}" 
                        #   clearly_id="{}" >[修改办结附件/备注]</a >
                        # '''.format(item.year_end_remark,item.year_end_file,item.id,item.clearly_id,)


                    # if item.ass_finish_uid_remark:
                    #         strs+="(备注:{})".format(item.clearly_end_remark)
                    if item.finance_uid_at and item.clearly_end==2 :
                            strs+=" <br/>5.({})确认汇算办结{}".format(
                                item.clearly_end_confirm_uid_name,item.clearly_end_confirm_at
                            )
                    if item.finance_uid_at and item.year_end==2 :
                            strs+=" <br/>5.({})确认汇算办结{}".format(
                                item.year_end_confirm_uid_name,item.year_end_confirm_at
                            )                            
                    strs+="</td>"
        return strs
    @tornado.web.authenticated
    def get(self):
        tag = self.get_argument("tag", "all")
        uid = self.get_secure_cookie("uid")
        uid_name = self.get_secure_cookie("name")
        role = self.get_secure_cookie('role')
        is_manager = self.get_secure_cookie("is_manager")
        from_tag = self.get_argument("from_tag", "")
        check_under = self.get_argument('check_under', '')
        dt = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        if tag=="ass_remark":
            clearly_id = self.get_argument("clearly_id")
            if not clearly_id:
                return self.write("not clearly_id")
            t_customer_clearly_msg = self.db_customer.query(
                "select * from  t_customer_clearly_msg  where clearly_id=%s order by id desc  limit 10",
                clearly_id)
            t_customer_clearly_msg_count = self.db_customer.get(
                "select count(*) c from  t_customer_clearly_msg  where clearly_id=%s ",
                clearly_id)

            self.render(
                "c/clearly/ass_remark.html",clearly_id=clearly_id,
                t_customer_clearly_msg=t_customer_clearly_msg,
                t_customer_clearly_msg_count=t_customer_clearly_msg_count)
        elif tag == "clearly_customer_list_details":
            clearly_id = self.get_argument("clearly_id")
            state = self.get_argument("state","")
            if not clearly_id:
                return self.write("not clearly_id")
            t_customer_clearly_milepost = self.db_customer.query(
                "select * from  t_customer_clearly_milepost  where clearly_id=%s  ",
                clearly_id)

            self.render(
                "c/clearly/clearly_customer_list_details.html",
                t_customer_clearly_milepost=t_customer_clearly_milepost,
                state=state)
        elif tag == "all":
            sql = ""
            column_sql=''
            curr_year = self.get_argument("curr_year", "2018")
            orderby_column=" b.uid_at"
            wait = int(self.get_argument("wait",0))
            keyword = self.get_argument("keyword", "")
            qtype = self.get_argument("qtype", "")
            acc = self.get_argument("acc","")
            jz = self.get_argument("jz", "")
            lp = self.get_argument("lp", "")
            kj = self.get_argument('kj', '')
            my = self.get_argument("my", "")
            ass_tj = self.get_argument("ass_tj","")
            ass_day = self.get_argument("ass_day","")
            if role=="1" or role=="13":
                my="2"
            by_tag = self.get_argument("by_tag", '')
            check_kj = self.get_argument('check_kj', '')
            check_under = self.get_argument('check_under', '')
            state = int(self.get_argument("state",0))
            confirm = int(self.get_argument("confirm",0))
            finish = int(self.get_argument("finish",0))
            sale =  self.get_argument('sale', '')
            kf =  self.get_argument('kf', '')
            gj =  self.get_argument('gj', '')
            ass_price = self.get_argument("ass_price","")
            ass_name = self.get_argument("ass_name","")
            ass_num = self.get_argument("ass_num","")
            ass_day_end =self.get_argument("ass_day_end","")
            ass_num_end = self.get_argument("ass_num_end","")
            need = self.get_argument("need","")
            year_type = int(self.get_argument("year_type",0))
            clearly_type = int(self.get_argument("clearly_type",0))
            cpl = self.get_argument("cpl","")
            ass_name = self.get_argument("ass_name",'')
            regdate = self.get_argument("regdate","")
            sf = self.get_argument("sf","")
            tag_id = self.get_argument("tag_id","")
            data_check = self.get_argument("data_check","")
            tel = self.get_argument("tel","")
            tag_id = self.get_argument("tag_id","")
            new_tag = self.get_argument("new_tag","")
            tag_parent_id = self.get_argument("tag_parent_id","")
            total_sql=""
            s_is_general = self.get_argument("s_is_general","")
            s_is_check = self.get_argument("s_is_check","")
            is_except = self.get_argument("is_except","") 
            mbtype_id = int(self.get_argument("mbtype_id",0))
            params = {
                "mbtype_id":mbtype_id,
                "check_under":check_under,
                "s_is_check":s_is_check,
                "s_is_general":s_is_general,
                "tag_id":tag_id,
                "tag_parent_id":tag_parent_id,
                "new_tag":new_tag,
                "ass_day":ass_day,
                'kf':kf,
                'gj':gj,
                'sale':sale,
                "wait": wait,
                "keyword": keyword,
                "curr_year": curr_year,
                "state": state,
                "my": my,
                "kj": kj,
                "acc": acc,
                "by_tag": by_tag,
                "confirm": confirm,
                "finish": finish,
                "ass_name":ass_name,
                "year_type":year_type,
                'clearly_type':clearly_type,
                "cpl":cpl,
                "ass_tj":ass_tj,
                "ass_num":ass_num,
                "ass_name":ass_name,
                "ass_num_end":ass_num_end,
                "ass_day_end":ass_day_end,
                "regdate":regdate,
                "sf":sf,
                 "tag_id":tag_id,
                 "data_check":data_check,
                 "tel":tel,
                 "is_except":is_except,
                 "need":need
            }
            mbtype_id_sql=""
            if mbtype_id:
                mbtype_id_sql+= " and mbtype_id=%s and d.result_id=0 "%(mbtype_id)
            t_user_relation=self.db.query('''
                select a.* from t_user_relation a
                inner join t_user_relation b on
                find_in_set(a.department_name,b.department_name)
                and b.uid=%s and b.is_leader<>0
                where a.uid!=b.uid and a.is_leader=0
                ''',uid)
            under_sql  = ""
            acc_uids=[]
            if t_user_relation and check_under:
                for item in t_user_relation:
                    acc_uids.append(int(item.uid))
                acc_uids=tuple(acc_uids)
            
                if str(acc_uids)[-2]==',':
                    acc_uids=str(acc_uids)[:-2]+')'
                else:
                    acc_uids=str(acc_uids)

                under_sql +=" and  a.acc_uid in  "+acc_uids

            sql=""    
            if regdate and  regdate=="null":
                    sql  = " and reg_date is null"

            elif regdate and sf:
                sf_sql="="
                if sf:
                    if sf=="1":
                        sf_sql="<="
                    elif sf=="2":
                        sf_sql=">="
                    
                sql  += " and year(reg_date){}'{}' ".format(sf_sql,regdate)       
            if data_check:
                sql += " and data_check=1"
            inner_sql = " left join t_customer_clearly b   on  a.id=b.customer_id "

            #     t_linkman where curr_year=%s  and clearly_id=%s

            if state:
                inner_sql = " inner join t_customer_clearly b   on  a.id=b.customer_id  left join (select clearly_id,curr_year,group_concat(cc.name,'|',cc.tel,'|',cc.remark,'|',cc.gender) lk from t_linkman cc where clearly_id > 0 group by clearly_id,curr_year) c on b.id = c.clearly_id and c.curr_year="+curr_year+" "
                column_sql = " ,cremark,b.id  clearly_id, lk,b.data_company,b.data_check ,b.btype_id,b.is_check,no_price,price_remark,b.ass_uid_name,b.ass_uid_confirm,b.ass_finish_name,b.ass_finish_at ,b.ass_finish_uid_remark"

                if state==4 :
                    inner_sql += " inner join t_customer_clearly_milepost d on b.id=d.clearly_id "
                    column_sql+=" "
                    orderby_column= " b.ass_uid_confirm "
                    sql += " and mstate_id=" + str(state) + " "
                elif state==2:
                    total_sql="where state_id=3"

                    inner_sql +=""" left join t_customer_relman
                                    d  on d.customer_id=b.customer_id
                                    """
                    if sale:
                        sql+=" and (sale like '%%" + sale + "%%')"
                    if kf:
                        sql+=" and (kf like '%%" + kf + "%%')"
                    if gj:
                        sql+=" and (gj like '%%" + gj + "%%')"
                    sql += " and state_id=" + str(state) + " "

                elif state==5 :
                    inner_sql += " inner join t_customer_clearly_milepost d on b.id=d.clearly_id "
                    column_sql+=" ,d.milepost_rollback_remark,d.milepost_rollback_at,d.milepost_rollback_uid_name,d.clearly_end_remark,d.year_end_remark "
                    sql += " and mstate_id=" + str(state) + " "
                elif state==6 :
                    inner_sql += " inner join t_customer_clearly_milepost d on b.id=d.clearly_id "
                    column_sql+=" ,d.id milepost_id "
                    sql += " and mstate_id=" + str(state) + "  and mbtype_id=1 and clearly_end=%s "%(clearly_type)
                    if clearly_type==1:
                        orderby_column= " clearly_end_at  "
                    elif  clearly_type==2:
                        orderby_column= " clearly_end_confirm_at  "
                    else:
                        orderby_column= " finance_uid_at  "
                    if need:
                        sql+=" and result_id={} ".format(need)
                
                elif state==8 :
                    inner_sql += " inner join t_customer_clearly_milepost d on b.id=d.clearly_id "
                    column_sql+=" ,d.id milepost_id "
                    if year_type==1:
                        orderby_column =" year_end_at "
                    elif year_type==2:
                        orderby_column =" year_end_confirm_at "
                    else:
                        orderby_column =" finance_uid_at "
                    sql += " and mstate_id=" + str(state) + "  and mbtype_id=2  and year_end=" + str(year_type) + "  "
                    if need:
                        sql+=" and result_id={} ".format(need)

                elif state==3 :      
                    
                    inner_sql += " inner join t_customer_clearly_milepost d on b.id=d.clearly_id " + mbtype_id_sql
                    column_sql+=" ,d.id milepost_id,mbtype_id_name ,d.result_id"                    
                    if cpl:
                        sql += " and state_id > " + str(state) + " "
                        total_sql = " where state_id > " + str(state) + " "
                    else:              

                        sql += " and state_id=" + str(state) + " and d.result_id=0  "
                        total_sql="where state_id="+str(state)   
                    if ass_day and ass_day_end:
                        sql+=" and  b.id in (select id from t_customer_clearly where datediff(now(),date(ass_uid_by_at)) >={} and  datediff(now(),date(ass_uid_by_at)) <={}) ".format(ass_day,ass_day_end)  
                    if ass_num and  ass_num_end:
                        sql+=" and b.id in (select clearly_id from (select clearly_id,count(distinct(date(uid_at))) gj_num  from t_customer_clearly_msg  group by clearly_id ) ddd where gj_num >= {} and gj_num <= {} )".format(ass_num,ass_num_end)  
           
                    # print sql
                else:
                    sql += " and state_id=" + str(state) + " "
                    total_sql="where state_id="+str(state)

            elif wait:
                orderby_column = " b.uid_at "
                sql += " and a.id  in ( select customer_id from t_customer_clearly where curr_year=%s) "%(curr_year)
                inner_sql = " inner join t_customer_clearly b   on  a.id=b.customer_id  left join (select clearly_id,curr_year,group_concat(cc.name,'|',cc.tel,'|',cc.remark,'|',cc.gender) lk from t_linkman cc where clearly_id > 0 group by clearly_id,curr_year) c on b.id = c.clearly_id and c.curr_year="+curr_year+" "
                column_sql = " ,cremark,b.id  clearly_id, lk,b.data_company,b.data_check ,b.btype_id,b.is_check,no_price,price_remark,b.ass_uid_name,b.ass_uid_confirm,b.ass_finish_name,b.ass_finish_at ,b.ass_finish_uid_remark"


            else:
                orderby_column = " b.uid_at "
                sql += " and a.id not in ( select customer_id from t_customer_clearly where curr_year=%s)"%(curr_year)
        
            t_staff_total = self.db_customer.query("select ass_uid_name,count(*) c from t_customer_clearly "+total_sql+" group by ass_uid_name")
            if confirm:
                if confirm==1:
                    sql += " and b.ass_uid_confirm is   null "
                else:
                    sql += " and b.ass_uid_confirm is not  null "

            if finish:
                sql += " and ass_finish =%s "%(finish)

            if ass_name:
                if ass_name=="None":
                    sql += "and b.ass_uid_name is NULL"
                else:
                    sql += "and b.ass_uid_name='%s'"%(ass_name)
            acc_uids = []
            if tel:
                sql+="""  and (a.reg_tel like '%%"""+tel+"""%%' or  a.id in (select customer_id from t_linkman where tel like '%%"""+tel+"""%%'))"""

            if keyword:
                id_sql=" "
                if isinstance(keyword, int):
                   id_sql    =" a.id = " + keyword +" or "
                sql += """ 
                        and ("""+id_sql+""" a.company like '%%""" + keyword + """%%' or a.company_reguid like '%%""" + keyword + """%%' )
                
                
                """
            if s_is_check:
                if s_is_check=="1":
                    sql+=" and b.is_check=1 and b.btype_id=1"
                elif s_is_check=="2":
                    sql+=" and b.is_check=1 and b.btype_id=0"
                else:
                    sql += " and b.is_check=0 " 
            if s_is_general:
                sql+=" and a.is_general={} ".format(s_is_general)
            if under_sql:
                sql+=under_sql
            elif my=="1":
                sql +=" and  a.acc_uid=%s " %(uid)
            elif my=="2":
                sql +=" and b.ass_uid=%s"%(uid)

            if kj:
                sql +=" and  a.acc_uid_name='%s' " %(kj)

            if by_tag =="正常":
                sql += " and a.id not in  (select id from t_customer where  customer_type_name  like '%%解约%%' or customer_type_name  like '%%停账%%' or customer_type_name  like '%%注销%%' or customer_type_name  like '%%逾期%%') "
            # elif by_tag =="非记账":
            #     sql += " and a.id not in  (select id from t_customer where  customer_type_name  like '%%记账%%') "

            # elif by_tag:
            #     sql += " and  customer_type_name like '%%" + by_tag + "%%'"
            elif by_tag=='楼盘':
                sql+=' and a.is_building=1 '
            elif by_tag=='汇算清缴':
                sql+=' and a.is_clearly=1 '
            elif by_tag=='工商年检':
                sql+=' and a.is_year=1 '
            elif by_tag:
                sql+=' and  tag_id_name="%s" '%by_tag
            if is_except:
                orderby_column=" a.id "
                sql+= """ and company  in (
select customer_company from db_income2.t_projects where  customer_company not  in (
select company from t_customer a   inner join t_customer_clearly b 
  on  a.id=b.customer_id  where 
 is_close=0  and a.id  in ( select customer_id from t_customer_clearly where curr_year=2018) order by  b.uid_at )
 and (project_name like '%%年检%%' or project_name like '%%年报%%'  or project_name like '%%汇算%%' ))"""
            query_str = ""
            query_str_count = ""
            customers = None
            page = int(self.get_argument("page", 1))
            pre_page = 20
            count = 0

            count = self.db_customer.get(
                '''SELECT count(*) count from t_customer a '''+inner_sql+''' where   is_close=0''' + sql)
            pagination = Pagination(page, pre_page, count.count,
                                    self.request)
            startpage = (page - 1) * pre_page

            customers = self.db_customer.query(
                '''select *,a.id a_customer_id '''+column_sql+''' from t_customer a  '''
                + inner_sql + ''' where  is_close=0 ''' + sql + '''
            order by '''+orderby_column+''' desc limit %s,%s''', startpage, pre_page)
            print('''
            select *,a.id a_customer_id '''+column_sql+''' from t_customer a  '''
                + inner_sql + ''' where  is_close=0 ''' + sql + '''
            order by '''+orderby_column+''' desc 
            ''')
            
            t_type = self.db_customer.query(
                u"select * from t_type where tag='汇算流程' order by order_int ")
            t_linkman_type = self.db.query(
                "select * from t_projects_type where income_category='联系人' order by order_int"
            )
            t_finish_type = self.db_customer.query(
                "select * from t_type where tag=%s", curr_year)
            t_customer_type = self.db_customer.query(
                "select * from t_type where tag='客户标签' and is_show=1  order by `order` ")
            t_user = self.db.query("select name from t_user ")

            t_sale = self.db_customer.query("select sale name from t_customer_relman where sale is not  null and sale <> '' group by sale ")
            t_kf = self.db_customer.query("select kf name from t_customer_relman where kf is not  null and kf <> '' group by kf ")
            t_gj = self.db_customer.query("select gj  name from t_customer_relman where gj is not  null and gj <> '' group by gj ")
            t_clearly_except = self.db_customer.query("select * from t_type where tag='汇算标签' order by order_int desc")
            self.render(
                'c/clearly/clearly_customer_list_new.html',
                get_project_info=self.get_project_info,
                t_staff_total=t_staff_total,
                get_clearly_stat=self.get_clearly_stat,
                t_clearly_except=t_clearly_except,
                dt=dt,
                get_clearly_info = self.get_clearly_info,
                t_user=t_user,
                t_sale=t_sale,
                t_kf = t_kf,
                t_gj = t_gj,
                t_finish_type=t_finish_type,
                t_linkman_type=t_linkman_type,
                t_customer_type=t_customer_type,
                t_type=t_type,
                params=params,
                curr_year=curr_year,
                customers=customers,
                pagination=pagination,
                check_under=check_under,
                t_user_relation=t_user_relation,
                tag=tag,
                keyword=keyword,
                lp=lp,
                jz=jz,
                my=my,
                kj=kj,
                check_kj=check_kj,
                get_except_tag=self.get_except_tag,
                qtype=qtype)

    @tornado.web.authenticated
    def post(self):
        tag = self.get_argument("tag")
        uid_name = self.get_secure_cookie("name")
        role = self.get_secure_cookie("role")
        uid = self.get_secure_cookie("uid")
        dt = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        if tag =="except_tag":
            except_tag_val = self.get_argument("except_tag_val","")
            except_tag_ids = self.get_argument("except_tag_ids","")
            except_remark = self.get_argument("except_remark","")
            customer_id = self.get_argument("customer_id","")
            if not customer_id:
                return self.write("not customer_id")

            t_except= self.db_customer.get("select * from t_customer_clearly_except where customer_id=%s",customer_id)
            if t_except:
                self.db_customer.execute("""update t_customer_clearly_except set uid=%s,
                uid_name=%s,uid_at=%s,except_remark=%s,except_tag_vals=%s,except_tag_ids=%s  where customer_id=%s""",
                uid,uid_name,dt,except_remark,except_tag_val,except_tag_ids,customer_id)
                txt=" 原标签:%s 设置为:%s 原备注:%s 改为:%s"%(except_tag_val,t_except.except_tag_vals,except_remark,t_except.except_remark)
            else:
                self.db_customer.execute("""insert into t_customer_clearly_except(uid,uid_name,uid_at,except_remark,except_tag_vals,except_tag_ids,customer_id)
                        values(%s,%s,%s,%s,%s,%s,%s)
                
                    """,uid,uid_name,dt,except_remark,except_tag_val,except_tag_ids,customer_id)
                txt="新设置标签%s 备注:%s"%(except_tag_val,except_remark)
            events.add_project_event(self,'0','汇算异常标签',
                    txt
                    ,uid,uid_name,customer_id)
        elif tag == "group_price":
            body = self.get_argument("body")
            group_g_price= self.get_argument('group_g_price')
            group_no_price= self.get_argument('group_no_price')
            group_price_remark= self.get_argument('group_price_remark')


            data = json.loads(body)

            if  not data:
                return self.write("没有可操作数据")

            result = 1
            for item in data:
                if item:
                    t_type = self.db_customer.get(u"select * from t_type where tag='汇算流程' and `order_int`=2")



                    result = self.db_customer.execute(
                        """
                    update  t_customer_clearly set

                    state_id=%s,state_id_name=%s,state_id_at=%s,state_id_uid=%s,state_id_uid_name=%s,
                        g_price=%s,g_price_uid=%s ,g_price_uid_name=%s,g_price_uid_at=%s ,no_price=%s,price_remark=%s
                                where  id=%s
                    """,t_type.order_int,t_type.name,dt,uid,uid_name,
                        group_g_price,uid,uid_name,dt,group_no_price,group_price_remark,

                        item["clearly_id"],
                    )
            self.write(str(result))
        elif tag =="ass_price":
            one_g_price= self.get_argument('one_g_price')
            one_no_price= self.get_argument('one_no_price')
            one_price_remark= self.get_argument('one_price_remark')
            clearly_id = self.get_argument("clearly_id")

            clearly = self.db_customer.get("select * from t_customer_clearly where id=%s",clearly_id)

            if clearly:
                change_price=0
                change_price1=0
                str1=""
                if float(one_g_price)!=clearly.g_price:
                    change_price= 1
                    str1="\n%s:原报备价格%s 更新为%s"%(dt,clearly.g_price,one_g_price)
                if float(one_no_price)!=clearly.no_price:
                    change_price1= 1
                    str1+="\n%s:原非报备价格%s 更新为%s"%(dt,clearly.no_price,one_no_price)
                one_price_remark= one_price_remark+str1
                result = self.db_customer.execute(
                    """
                        update  t_customer_clearly set

                            change_price=%s,change_price1=%s,
                            g_price=%s,g_price_uid=%s ,g_price_uid_name=%s,
                            g_price_uid_at=%s ,no_price=%s,price_remark=%s
                                    where  id=%s
                        """,change_price,change_price1,
                            one_g_price,uid,uid_name,dt,one_no_price,one_price_remark,

                        clearly_id,
                        )
                self.write(str(result))

        elif tag =="group_ass":
            body = self.get_argument("body")
            group_ass_name= self.get_argument('group_ass_name')
            curr_year= self.get_argument('curr_year')

            data = json.loads(body)
            if  not data:
                return self.write("没有可操作数据")
            elif not group_ass_name:
                return self.write("跟进人为空.")
            elif not curr_year:
                return self.write("not curr_year")
            t_user = self.db.get("select * from t_user where name=%s",group_ass_name)
            if not t_user :
                return self.write('跟进人不存在')
            result = 1
            for item in data:
                if item:

                    t_type = self.db_customer.get(u"select * from t_type where tag='汇算流程' and `order_int`=3")
                    self.db_customer.execute("""
                                delete from t_customer_clearly_milepost where clearly_id=%s
                            """, item["clearly_id"])
                    self.db_customer.execute("""
                                insert into t_customer_clearly_milepost(
                                    clearly_id, uid, uid_name, uid_at, mbtype_id,
                                    mbtype_id_name, mstate_id, mstate_id_name,
                                    mstate_uid_at, mstate_uid, mstate_uid_name)
                                    select %s,%s,%s,%s,order_int,name,%s,%s,%s,%s,%s from t_type where tag=%s
                            """, item["clearly_id"], t_user.id, t_user.name,
                                                     dt, t_type.order_int,
                                                     t_type.name, dt, uid,
                                                     uid_name, curr_year)

                    result = self.db_customer.execute(
                        """
                    update  t_customer_clearly set
                    ass_uid=%s,ass_uid_name=%s,ass_uid_at=%s,
                    state_id=%s,state_id_name=%s,state_id_at=%s,state_id_uid=%s,state_id_uid_name=%s


                                where  id=%s
                    """,t_user.id, t_user.name,dt,t_type.order_int,t_type.name,dt,uid,uid_name,


                        item["clearly_id"],
                    )
            self.write(str(result))
        elif tag =="ass_one":
            ass_name= self.get_argument('ass_name')
            clearly_id= self.get_argument('clearly_id')
            curr_year  = self.get_argument("curr_year")
            if not ass_name:
                return self.write("跟进人为空.")
            elif not curr_year:
                return self.write("not curr_year")
            elif not clearly_id:
                return self.write("not clearly_id")

            t_user = self.db.get("select * from t_user where name=%s",ass_name)
            if not t_user :
                return self.write('跟进人不存在')
            result = 1
            t_type = self.db_customer.get(u"select * from t_type where tag='汇算流程' and `order_int`=3")
            self.db_customer.execute("""
                        delete from t_customer_clearly_milepost where clearly_id=%s
                    """, clearly_id)
            self.db_customer.execute("""
                        insert into t_customer_clearly_milepost(
                            clearly_id, uid, uid_name, uid_at, mbtype_id,
                            mbtype_id_name, mstate_id, mstate_id_name,
                            mstate_uid_at, mstate_uid, mstate_uid_name)
                            select %s,%s,%s,%s,order_int,name,%s,%s,%s,%s,%s from t_type where tag=%s
                    """, clearly_id, t_user.id, t_user.name,
                                                dt, t_type.order_int,
                                                t_type.name, dt, uid,
                                                uid_name, curr_year)

            result = self.db_customer.execute(
                """
                    update  t_customer_clearly set ass_uid_confirm=NULL,
                    ass_uid=%s,ass_uid_name=%s,ass_uid_at=%s,
                    state_id=%s,state_id_name=%s,state_id_at=%s,state_id_uid=%s,state_id_uid_name=%s
                    where  id=%s
            """,t_user.id, t_user.name,dt,t_type.order_int,t_type.name,dt,uid,uid_name,


               clearly_id
            )
            self.write(str(result))

        elif tag =="linkman":
            clearly_id = self.get_argument("clearly_id")
            curr_year  = self.get_argument("curr_year")
            if not clearly_id:
                return self.write("not clearly")

            linkman_arr = []
            t_linkman = self.db_customer.query("select * from t_linkman where curr_year=%s  and clearly_id=%s order by created_at desc",curr_year,clearly_id)
            for item in t_linkman:
                linkman_arr.append({"name":item.name,"tel":item.tel,"remark":item.remark})

            self.write(tornado.escape.json_encode({"data":linkman_arr}))
        elif tag=="ass_confirm":
            clearly_id = self.get_argument("clearly_id")
            if not clearly_id:
                return self.write("not clearly_id")
            result = self.db_customer.execute("update t_customer_clearly set ass_uid_confirm=%s where id=%s",dt,clearly_id)
            result = self.db_customer.execute("update t_customer_clearly_milepost set ass_uid_confirm=%s where clearly_id=%s",dt,clearly_id)

            self.write(str(result))

        elif tag == "mile_modify":
            detail_id = self.get_argument("detail_id")
            clearly_id = self.get_argument("clearly_id")
            amount = self.get_argument("amount",0)
            project_id = self.get_argument("project_id","")
            result_remark = self.get_argument("result_remark", "")
            result_id = self.get_argument("result_id")
            result_id_name = self.get_argument("result_id_name")

            if detail_id and clearly_id:
                result = self.db_customer.execute("""
                    update t_customer_clearly_milepost set 
                    amount=%s,
                    project_id=%s,
                    result_remark=%s,
                    result_id=%s,
                    result_id_name=%s
                    where 
                    id=%s
                """,amount,project_id,result_remark,result_id,result_id_name,
                detail_id)
                self.write(str(result))


        elif tag == "ass_finish":
            detail_id = self.get_argument("detail_id")
            clearly_id = self.get_argument("clearly_id")
            amount = self.get_argument("amount")
            project_id = self.get_argument("project_id")
            result_remark = self.get_argument("result_remark", "")

            btype_id = self.get_argument("btype_id")
            btype_id_name = self.get_argument("btype_id_name")
            result_id = self.get_argument("result_id")
            result_id_name = self.get_argument("result_id_name")
            action= self.get_argument("action","")
            state = self.get_argument("state","")
            t_clearly = self.db_customer.get("select * from t_customer_clearly where id=%s ",clearly_id)
            if not clearly_id:
                return self.write("not clearly_id")
            elif not t_clearly:
                return self.write("not t_clearly")

            update_sql=""
            if action == "confirm_end" or state=="4":
                t_type = self.db_customer.get(
                    u"select * from t_type where tag='汇算流程' and `order_int`=5")
                update_sql = " ass_leader_uid='%s',ass_leader_uid_name='%s',ass_leader_uid_at='%s', " % (
                    uid, uid_name, dt)

            elif action == "finance_end" or state == "5":
                if btype_id=="1":#汇算
                    t_type = self.db_customer.get(
                        u"select * from t_type where tag='汇算流程' and `order_int`=6")
                elif btype_id=="2":
                    t_type = self.db_customer.get(
                        u"select * from t_type where tag='汇算流程' and `order_int`=8") #年检
                update_sql = " finance_uid='%s',finance_uid_name='%s',finance_uid_at='%s', " % (
                    uid, uid_name, dt)

            else:
                t_customer = self.db_customer.get("select * from t_customer where id=%s",t_clearly.customer_id)
                if project_id!="0":
                    t_project = self.db.get("select * from t_projects where id=%s",project_id)
                    if not t_project:
                        return self.write("{0}确认单不存在哦.".format(project_id))
                    if  t_project.customer_company !=t_customer.company and  t_project.customer_company!=t_clearly.data_company:
                        return self.write("确认单公司名称[{}]不匹配,[{}][{}],请核实. ".format(t_project.customer_company,t_customer.company,t_clearly.data_company))
                t_type = self.db_customer.get(
                                u"select * from t_type where tag='汇算流程' and `order_int`=4"
                        )
                update_sql ="`ass_uid`='%s', `ass_uid_name`='%s', `ass_end_confirm`='%s', "%(uid,uid_name,dt)
          
            result = self.db_customer.execute("""
                update t_customer_clearly_milepost set
                """ + update_sql + """


                 `project_id`=%s,
                 `amount`=%s,
                 `mstate_id`=%s,
                 `mstate_id_name`=%s,
                 mstate_uid=%s,
                 mstate_uid_name=%s,
                 mstate_uid_at=%s,
                 result_remark=%s,
                 result_id=%s,
                 result_id_name=%s
                 where id=%s
            """, project_id, amount, t_type.order_int,
                                              t_type.name, uid, uid_name, dt,
                                              result_remark, result_id,
                                              result_id_name, detail_id)

            if state==4:
                all_end = self.db_customer.get("""
                        select count(*) c from t_customer_clearly_milepost
                        where clearly_id=%s and     ass_leader_uid_at is null
                    """,clearly_id)

            if state==5:        
                all_end = self.db_customer.get("""
                        select count(*) c from t_customer_clearly_milepost
                        where clearly_id=%s and    finance_uid_at is null
                    """,clearly_id)
            else:

                all_end = self.db_customer.get("""
                        select count(*) c from t_customer_clearly_milepost
                        where clearly_id=%s and    ass_end_confirm is null
                    """,clearly_id)

            if all_end.c == 0:
                result = self.db_customer.execute(
                    """update t_customer_clearly set
                    state_id=%s,state_id_name=%s,state_id_at=%s,state_id_uid=%s,state_id_uid_name=%s where id=%s""",
                    t_type.order_int, t_type.name, dt, uid, uid_name, clearly_id)

            self.write(str(all_end.c))
        elif tag=="ass_leader":
            clearly_id = self.get_argument("clearly_id")
            ass_finish = int(self.get_argument("ass_finish"))
            ass_finish_name = self.get_argument("ass_finish_name")
            ass_finish_uid_remark = self.get_argument("ass_finish_uid_remark","")
            if not clearly_id:
                return self.write("not clearly_id")
            if ass_finish==1:
                pass
            t_type = self.db_customer.get(
                u"select * from t_type where tag='汇算流程' and `order_int`=5")
            result = self.db_customer.execute(
                """update t_customer_clearly set ass_finish_uid=%s,ass_finish_uid_name=%s,ass_finish_at=%s,ass_finish=%s,ass_finish_name=%s,
                state_id=%s,state_id_name=%s,state_id_at=%s,state_id_uid=%s,state_id_uid_name=%s,ass_finish_uid_remark=%s where id=%s""",
                uid, uid_name, dt, ass_finish, ass_finish_name,
                t_type.order_int, t_type.name, dt, uid, uid_name,
                ass_finish_uid_remark, clearly_id)
            self.write(str(result))
        elif tag=="to_end":
            clearly_id = self.get_argument("clearly_id")
            type_end = self.get_argument("type_end")
            end_state  = self.get_argument("end_state")
            milepost_id = self.get_argument("milepost_id")
            finish_remark = self.get_argument("finish_remark","")
            result_id = self.get_argument("result_id",'')
            file_type=self.get_argument('file_type','')
            len1=int(self.get_argument('len',0))
            file_path=''
            if not clearly_id:
                return self.write("not clearly_id")
            is_upload = False
            url_fname=""
            
            if result_id=="3" or (type_end=="clearly_2" or type_end=="year_2" ):
                pass
            else:
                for i in range(len1):    
                    try:
                        file1 = self.request.files['file'+str(i)][0]
                        is_upload = True
                    except:
                        return self.write("请上传办结截图哦")
                    if is_upload:
                        ori_filename = file1["filename"]
                        filename_full = options.upload_path + "/customer/clearly/%s/" % (
                            clearly_id)
                        url_path = "/static/customer/clearly/%s/" % (clearly_id)
                        try:
                            os.makedirs(filename_full)
                        except OSError:
                            if not os.path.isdir(filename_full):
                                raise
                        extension = os.path.splitext(ori_filename)[1]

                        uuid_str = str(uuid.uuid4())
                        fname = "{3}_{0}_{1}{2}".format(ori_filename, clearly_id, extension,uuid_str)

                        save_full_path = filename_full + fname
                        url_fname = "{0}{1}".format(url_path, fname)
                        output_file = open(save_full_path, 'w')
                        output_file.write(file1["body"])
                        file_path += url_fname+'|'           

            if type_end=="clearly_2":
                result = self.db_customer.execute(
                    """update t_customer_clearly_milepost set 
                    clearly_end=%s,clearly_end_confirm_at=%s,clearly_end_confirm_uid=%s,
                    clearly_end_confirm_uid_name=%s ,clearly_end_remark=%s, clearly_end_file=%s where id=%s and clearly_id=%s""",
                    end_state,dt,uid, uid_name,finish_remark,file_path,milepost_id, clearly_id)
            elif type_end=="clearly_1":
                result = self.db_customer.execute(
                    """update t_customer_clearly_milepost set 
                    clearly_end=%s,clearly_end_at=%s,clearly_end_uid=%s,
                    clearly_end_uid_name=%s,clearly_end_remark=%s, clearly_end_file=%s where id=%s and clearly_id=%s""",
                    end_state,dt,uid, uid_name,finish_remark,file_path,milepost_id, clearly_id)                
            elif type_end=="year_1":
                result = self.db_customer.execute(
                    """update t_customer_clearly_milepost set 
                    year_end=%s,year_end_at=%s,year_end_uid=%s,year_end_uid_name=%s ,
                    year_end_remark=%s,
                    year_end_file=%s where id=%s and clearly_id=%s""",
                    end_state,dt,uid, uid_name,finish_remark,file_path,milepost_id, clearly_id)
            elif type_end=="year_2":
                result = self.db_customer.execute(
                    """update t_customer_clearly_milepost set year_end=%s,
                    year_end_confirm_at=%s,year_end_confirm_uid=%s,year_end_confirm_uid_name=%s ,
                    year_end_remark=%s,
                    year_end_file=%s where id=%s and clearly_id=%s""",
                    end_state,dt,uid, uid_name,finish_remark,file_path,milepost_id, clearly_id)
            elif type_end=='upload_file':
                if file_type=='year_end_file':
                    sql='year_end_remark="%s",year_end_file=concat(if(year_end_file is not null,year_end_file,""),if(year_end_file is not null and right(year_end_file,1)="|","%s","%s"))'%(finish_remark,file_path,('|'+file_path))
                elif file_type=='clearly_end_file':
                    sql='clearly_end_remark="%s",clearly_end_file=concat(if(clearly_end_file is not null,clearly_end_file,""),if(clearly_end_file is not null and right(clearly_end_file,1)="|","%s","%s"))'%(finish_remark,file_path,('|'+file_path))
      
                result=self.db_customer.execute('''
                update t_customer_clearly_milepost set '''+sql+''' where id=%s
                ''',milepost_id)
            self.write("0")
        elif tag=="ass_msg":
            clearly_id = self.get_argument("clearly_id")
            ctype = self.get_argument("ctype","")
            ass_msg = self.get_argument('ass_msg',"")
            if not clearly_id:
                return self.write("not clearly_id")
            elif not ass_msg:
                return self.write("跟进内容不能为空哦")

            result = self.db_customer.execute("insert into t_customer_clearly_msg(uid,uid_name,uid_at,ass_msg,ctype,file_path,clearly_id) values(%s,%s,%s,%s,%s,%s,%s)",
            uid,uid_name,dt,ass_msg,ctype,"",clearly_id)
            self.write(str(result))
        elif tag=="delete_msg":
            clearly_id = self.get_argument("clearly_id")
            id = self.get_argument("id")
            if not clearly_id or not  id:
                return self.write("删除失败")
            else:
                result = self.db_customer.execute("delete from t_customer_clearly_msg where id=%s and clearly_id=%s",id,clearly_id)
                self.write(str(result))
        elif tag=="ass_price_roll":
            clearly_id = self.get_argument("clearly_id")

            if not clearly_id:
                return self.write("not clearly_id")
            t_type = self.db_customer.get(
                u"select * from t_type where tag='汇算流程' and `order_int`=1")

            result = self.db_customer.execute("""update t_customer_clearly set state_id=%s ,state_id_name=%s,state_id_at=%s where id=%s""",
             t_type.order_int, t_type.name, dt,clearly_id)

            self.write(str(result))
        elif tag=="rollback": #撒回
            clearly_id = self.get_argument("clearly_id")
            rollback_remark = self.get_argument("rollback_remark","")
            rollback_state =self.get_argument('rollback_state')
            milepost_id = self.get_argument("milepost_id")
            if not clearly_id:
                return self.write("not clearly_id")
            t_type = self.db_customer.get(
                u"select * from t_type where tag='汇算流程' and `order_int`=%s",rollback_state)

            result = self.db_customer.execute("""update t_customer_clearly set
             state_id=%s ,state_id_name=%s,state_id_at=%s ,
             rollback_uid=%s,
             rollback_uid_name=%s,
             rollback_state=%s,
             rollback_at=%s
             where id=%s""",
             t_type.order_int,
              t_type.name, dt,uid,uid_name,rollback_state,dt,clearly_id)
            if result==0:
                update_sql =""
                if rollback_state=="5":
                    update_sql +=""" finance_uid=0 , finance_uid_name=NULL 
                    , finance_uid_at= null , finance_uid_remark=null, clearly_end=0,clearly_end_at=null,clearly_end_uid=0,clearly_end_uid_name=null,clearly_end_confirm_uid=0,clearly_end_confirm_at=null,clearly_end_confirm_uid_name=null,
                    year_end_confirm_at=null,year_end_confirm_uid=0,year_end_confirm_uid_name=null,clearly_end_remark=null,
                    year_end_remark=null,"""
                result = self.db_customer.execute("""update t_customer_clearly_milepost set
                    """+update_sql+"""
                    mstate_id=%s ,
                    mstate_id_name=%s,
                    mstate_uid_at=%s ,
                    mstate_uid=%s,
                    mstate_uid_name=%s,
                    milepost_rollback_uid=%s,
                    milepost_rollback_uid_name=%s,
                    milepost_rollback_remark=%s,
                    milepost_rollback_state=%s,
                    milepost_rollback_at=%s
                    where id=%s""",
                    t_type.order_int,
                    t_type.name, dt,uid,uid_name,uid,uid_name,rollback_remark,rollback_state,dt,milepost_id)

            self.write(str(result))

        elif tag == "add":
            body = self.get_argument("body")
            curr_year= self.get_argument('curr_year')
            do_action = self.get_argument("do_action","")
            kj_rollback_remark = self.get_argument("kj_rollback_remark","")

            data = json.loads(body)
            if not curr_year or not data:
                return self.write("没有可操作数据")

            for item in data:
                btype_id = 0
                btype_id_name = ""
                try:
                    btype_id = item["btype_id"]
                    btype_id_name = item["btype_id_name"]
                except :
                    pass
                g_price= 0
                try:
                    g_price = item["g_price"]
                except :
                    pass
                t_user = None
                t_type2 = None
                if item:
                    update_sql =""
                    if item["state"]==1:
                        t_type = self.db_customer.get(u"select * from t_type where tag='汇算流程' and `order_int`=2")
                        update_sql +="state_id=%s,state_id_name='%s',state_id_at='%s',state_id_uid=%s,state_id_uid_name='%s',"%(t_type.order_int,t_type.name,dt,uid,uid_name)
                    elif item["state"]==2:
                        t_type = self.db_customer.get(
                            u"select * from t_type where tag='汇算流程' and `order_int`=3"
                        )
                        t_type2 = t_type
                        t_user = self.db.get('select * from t_user where name=%s',item["ass_uid_name"])
                        if not t_user:
                            return self.write("跟进人不存在哦,请确认名字是否正确.")
                        update_sql += " state_id=%s,state_id_name='%s',state_id_at='%s',state_id_uid=%s,state_id_uid_name='%s',ass_uid=%s,ass_uid_name='%s',ass_uid_by=%s,ass_uid_by_name='%s',ass_uid_by_at='%s'," % (
                            t_type.order_int, t_type.name, dt, uid, uid_name,
                            t_user.id,t_user.name,uid,uid_name,dt)

                    t_customer_clearly = self.db_customer.get(
                        "select * from t_customer_clearly where curr_year=%s and customer_id=%s",
                        curr_year, item["customer_id"])

                    if g_price and role=="8" :
                        update_sql +=" g_price='%s',g_price_uid=%s ,g_price_uid_name='%s',g_price_uid_at='%s' ,no_price='%s',price_remark='%s',"%(item["g_price"],uid,uid_name,dt,item["no_price"],item["price_remark"])

                    self.db_customer.execute("update t_customer set is_general=%s,reg_date=%s where id=%s",item["is_general"],item["reg_date"],item["customer_id"])

                    if t_customer_clearly:
                        if do_action=="kj_back":
                            self.db_customer.execute("""
                                delete from t_customer_clearly_milepost where clearly_id=%s
                            """, t_customer_clearly.id)
                            t_type = self.db_customer.get(u"select * from t_type where tag='汇算流程' and `order_int`=2")
                            update_sql +="state_id=%s,state_id_name='%s',state_id_at='%s',state_id_uid=%s,state_id_uid_name='%s',rollback_uid=%s,rollback_uid_name='%s',rollback_uid_at='%s',rollback_state=2,rollback_uid_remark='%s', "%(t_type.order_int,
                            t_type.name,dt,uid,uid_name,uid,uid_name,dt,kj_rollback_remark)
                        if  item["state"]==2:
                            self.db_customer.execute("""
                                delete from t_customer_clearly_milepost where clearly_id=%s
                            """, t_customer_clearly.id)
                            self.db_customer.execute("""
                                insert into t_customer_clearly_milepost(
                                    clearly_id, uid, uid_name, uid_at, mbtype_id,
                                    mbtype_id_name, mstate_id, mstate_id_name,
                                    mstate_uid_at, mstate_uid, mstate_uid_name)
                                    select %s,%s,%s,%s,order_int,name,%s,%s,%s,%s,%s from t_type where tag=%s
                            """, t_customer_clearly.id, t_user.id, t_user.name,
                                                     dt, t_type2.order_int,
                                                     t_type2.name, dt, uid,
                                                     uid_name, curr_year)

                        result = self.db_customer.execute(
                            """
                       update  t_customer_clearly set """ + update_sql +
                            """ data_check=%s,ss_num=%s,data_company=%s,btype_id_name=%s,
                       uid=%s,uid_name=%s,uid_at=%s,income=%s,btype_id=%s,is_check=%s,cremark=%s
                       where curr_year=%s and customer_id=%s
                        """,
                            item["data_check"],
                            item["ss_num"],
                            item["data_company"],
                            btype_id_name,
                            uid,
                            uid_name,
                            dt,
                            item["income"],
                            btype_id,
                            item["is_check"],
                            item["cremark"],
                            curr_year,
                            item["customer_id"],
                        )

                        if result==0:
                            self.db_customer.execute("delete from t_linkman where  curr_year=%s and customer_id=%s",curr_year,item["customer_id"])
                            for row in item["lkman"]:
                                if row:
                                    self.db_customer.execute("""
                                        insert into t_linkman(name,tel,remark,gender,
                                        acc_uid_name,acc_uid,created_at,updated_at,
                                        customer_id,guid,clearly_id,curr_year)

                                        values(%s,%s,%s,%s,
                                        %s,%s,%s,%s,
                                        %s,uuid(),%s,%s)
                                    """,row["name"],row["tel"],row["remark"],row["gender"],
                                    uid_name, uid,dt,dt,
                                    item["customer_id"],t_customer_clearly.id,curr_year)

                    else:
                        t_type = self.db_customer.get(u"select * from t_type where tag='汇算流程' and `order_int`=1 ")
                        c_id = self.db_customer.execute(
                            """
                            insert into t_customer_clearly(cremark,data_check,ss_num,data_company,btype_id_name,curr_year,
                            customer_id,uid,uid_name,uid_at,income,is_check,btype_id,state_id,state_id_name,state_id_at,state_id_uid,state_id_uid_name)
                            values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
                            """, item["cremark"],item["data_check"], item["ss_num"],
                            item["data_company"], btype_id_name, curr_year,
                            item["customer_id"], uid, uid_name, dt,
                            item["income"], item["is_check"], btype_id,
                            t_type.order_int, t_type.name, dt,uid,uid_name)
                        if item["state"] == 2:
                            self.db_customer.execute("""
                                delete from t_customer_clearly_milepost where clearly_id=%s
                            """, c_id)
                            self.db_customer.execute("""
                                insert into t_customer_clearly_milepost(
                                    clearly_id, uid, uid_name, uid_at, mbtype_id,
                                    mbtype_id_name, mstate_id, mstate_id_name,
                                    mstate_uid_at, mstate_uid, mstate_uid_name)
                                    select %s,%s,%s,%s,order_int,name,%s,%s,%s,%s,%s from t_type where tag=%s
                            """, c_id, t_user.id, t_user.name, dt,
                                                     t_type2.order_int,
                                                     t_type2.name, dt, uid,
                                                     uid_name, curr_year)
                        if c_id > 0:
                            for row in item["lkman"]:
                                if row:
                                    self.db_customer.execute("""
                                        insert into t_linkman(name,tel,remark,gender,
                                        acc_uid_name,acc_uid,created_at,updated_at,
                                        customer_id,guid,clearly_id,curr_year)

                                        values(%s,%s,%s,%s,
                                        %s,%s,%s,%s,
                                        %s,uuid(),%s,%s)
                                    """,row["name"],row["tel"],row["remark"],row["gender"],
                                    uid_name, uid,dt,dt,
                                    item["customer_id"],c_id,curr_year)


            self.write("0")
        
        elif tag=="delete_file":
            milepost_id=self.get_argument('milepost_id','')
            file_type=self.get_argument('file_type','')
            file_path=self.get_argument('file_path','')
            if file_type=='clearly_end_file':
                sql='clearly_end_file=replace(clearly_end_file,"%s",""),clearly_end_file=replace(clearly_end_file,"%s","")'%(file_path+'|',file_path)
            elif file_type=='year_end_file':
                sql='year_end_file=replace(year_end_file,"%s",""),year_end_file=replace(year_end_file,"%s","")'%(file_path+'|',file_path)

            self.db_customer.execute('''
            update t_customer_clearly_milepost set '''+sql+''' where id=%s
            ''',milepost_id)