# encoding=utf8
from handlers.base import BaseHandler
import logging
import json
from tornado.concurrent import run_on_executor
import tornado.web
import tornado.gen
import urllib2
import tornado.httpclient
import sys, re,uuid,datetime
import urllib, os
from tornado.options import define, options
import qrcode,xlwt
import concurrent.futures
import events
reload(sys)
sys.setdefaultencoding('utf8')
from Pagination import Pagination
logger = logging.getLogger('boilerplate.' + __name__)
executor = concurrent.futures.ThreadPoolExecutor(20)

#客户
class CustomerHandler(BaseHandler):
    def get_payment_info(self,customer_id):
        payment_info=''
        t_customer_payment=self.db_customer.get('''
        select   if(c.pb_remark,c.pb_remark,'无') pb_remark from  t_customer_payment c
                               
                            INNER JOIN
                            (
                                SELECT `customer_id`, MAX(id) max_id
                                FROM t_customer_payment
                                GROUP BY customer_id
                            ) b ON c.customer_id = b.customer_id AND
                                    b.max_id = c.id
                    where c.customer_id=%s
        ''',customer_id)
        if t_customer_payment:
            if t_customer_payment.pb_remark:
              
                if len(t_customer_payment.pb_remark)>20:
                    payment_info='待收明细:<span title="'+t_customer_payment.pb_remark+'">'+t_customer_payment.pb_remark[:20]+'...</span>'
                else:
                    payment_info='待收明细:<span title="'+t_customer_payment.pb_remark+'">'+t_customer_payment.pb_remark+'</span>'
            else:
                payment_info='待收明细:<span>无</span>'
        return payment_info
    _thread_pool = executor
    @tornado.web.authenticated
    @tornado.web.asynchronous
    @tornado.gen.engine
    @tornado.web.authenticated
    def get(self):
        tag = self.get_argument("tag","all")
        uid = self.get_secure_cookie("uid")
        uid_name = self.get_secure_cookie("name")
        role=self.get_secure_cookie('role')
        is_manager=self.get_secure_cookie("is_manager")
        from_tag = self.get_argument("from_tag","")
        check_under=self.get_argument('check_under','')
        dt = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        page_count=self.get_argument('page_count','')
        logger.info("%s : %s  - %s " % (dt, uid_name, self.request.uri))

        if tag == "list":
            sql=""
            qtype = self.get_argument("qtype","")
            keyword = self.get_argument("keyword","")
            jz = self.get_argument("jz","")
            lp = self.get_argument("lp", "")
            page_count=self.get_argument('page_count','')
            if keyword:
                sql = " and (company like '%%" + keyword + "%%') or (company like '%%" + keyword + "%%')"
            if jz:
                sql =  sql+ " and (customer_type_name like '%%" + jz + "%%')"
            if lp:
                sql = sql + " and (customer_type_name like '%%" + lp + "%%')"
            page = int(self.get_argument("page", 1))
            pre_page = 20
            if page_count:
                pre_page=int(page_count)
            count = self.db_customer.get(
                '''SELECT count(*) count FROM t_customer   where acc_uid=%s and is_close=0
            ''' +sql, uid)
            pagination = Pagination(page, pre_page, count.count, self.request)
            startpage = (page - 1) * pre_page
            customers = self.db_customer.query('''
            select * from t_customer where acc_uid=%s and is_close=0 ''' + sql + '''
                                    order by created_at desc limit %s,%s
                ''', uid, startpage, pre_page)

            self.render(
                'c/customer/customer_list.html',
                t_user_relation='',
                check_under=check_under,
                customers=customers,
                pagination=pagination,
                tag=tag,
                page_count=page_count,
                keyword=keyword,lp=lp,jz=jz,qtype=qtype)


        elif tag =="customer_list_rec":
            sql = ""
            keyword = self.get_argument("keyword", "")
            qtype = self.get_argument("qtype", "")
            curr = self.get_argument("curr", "customer_tab")
            kj_manage = self.get_secure_cookie("kj_manage")
            jz = self.get_argument("jz", "")
            lp = self.get_argument("lp", "")
            kj = self.get_argument('kj', '')
            my = self.get_argument("my", None)
            t_user = self.db_customer.query(
                "select * from  "+
                        options.mysql_database + ".t_user where role=10 ")
            if keyword:
                sql = " and (company like '%%" + keyword + "%%')"
            if jz:
                sql = sql + " and (customer_type_name like '%%" + jz + "%%')"
            if lp:
                sql = sql + " and (customer_type_name like '%%" + lp + "%%')"

            if my:
                sql = sql + " and acc_uid = " + uid
            if kj:
                sql = sql + " and acc_uid_name='" + kj + "' "
            query_str = ""
            query_str_count = ""
            customers = None
            page = int(self.get_argument("page", 1))
            pre_page = 20
            count = 0
            orderby_str ="created_at"
            if qtype == "lname":
                count = self.db_customer.get(
                    '''SELECT count(*) count FROM t_customer a inner join (select customer_id,(concat(name,' '))
                        customer_name from t_linkman )  b on a.id=b.customer_id

                        where customer_name like  '%%''' + keyword +
                    '''%%' ''' + sql)
                pagination = Pagination(page, pre_page, count.count,
                                        self.request)
                startpage = (page - 1) * pre_page
                customers = self.db_customer.query(
                    '''SELECT a.*,b.customer_name FROM t_customer a inner join (select customer_id,(concat(name,' '))
                        customer_name from t_linkman )  b on a.id=b.customer_id

                        where customer_name like  '%%''' + keyword +
                    '''%%' ''' + sql + ''' limit %s,%s''', startpage, pre_page)

            elif qtype == "tel":
                count = self.db_customer.get(
                    '''SELECT count(*) count FROM t_customer a inner join (select customer_id,(concat(tel,' '))
                        ctel from t_linkman )  b on a.id=b.customer_id

                        where ctel like  '%%''' + keyword + '''%%'  ''' + sql +
                    ''' ''')
                pagination = Pagination(page, pre_page, count.count,
                                        self.request)
                startpage = (page - 1) * pre_page
                customers = self.db_customer.query(
                    '''SELECT a.*,b.ctel FROM t_customer a inner join (select customer_id,(concat(tel,' '))
                        ctel from t_linkman )  b on a.id=b.customer_id

                        where ctel like  '%%''' + keyword+ '''%%'   ''' +
                    sql + ''' limit %s,%s''', startpage, pre_page)

            else:
                if not my and kj_manage:
                    orderby_str = "manager_confirm_at"
                    if curr=="customer_todo":
                        # if page==1:
                        #     if self.request.host.split(':')[1]=='9000':
                        #         database=" db_customer.t_customer "
                        #     else:
                        #         database=" db_customer_test.t_customer "
                        #     project_milepost_type = self.db.query(
                        # """select  c.customer_company,b.btype_name,b.uid from t_projects_type a
                        # inner join t_projects_milepost b on b.type_id=a.id and b.type_name='办结'
                        # and b.confirm_at is not null
                        # inner join t_projects c on b.project_id=c.id
                        # inner join """+database+""" d on c.customer_company=d.company and is_wait is null
                        # where a.income_category='办结' and a.is_hide=0
                        #     order by b.order_int"""
                        # )
                        #     if project_milepost_type:
                        #         for item in project_milepost_type:
                        #             self.db_customer.execute('''
                        #             update t_customer set is_wait=0,is_wait_at=%s,is_wait_uid=%s,
                        #             wait_from_type=CONCAT(wait_from_type,%s)
                        #             where company=%s
                        #         ''',dt,item.uid,item.btype_name+',',item.customer_company)
                        yield tornado.gen.Task(self.runSql)
                        sql += " and is_wait=0 "

                    elif curr == "customer_tab":
                        sql += " and manager_confirm_at is null and acc_confirm_at is not  null "
                    elif curr == "tb_manager_confirm":
                        sql += " and manager_confirm_at is not  null and acc_confirm_at is not  null  "

                    count = self.db_customer.get(
                        '''SELECT count(*) count FROM t_customer where is_close=0 and customer_type_name like "%%记账%%" '''
                        + sql)
                    pagination = Pagination(page, pre_page, count.count,
                                            self.request)
                    startpage = (page - 1) * pre_page

                    customers = self.db_customer.query(
                        '''select * from t_customer  where is_close=0 and customer_type_name like "%%记账%%" '''
                        + sql + '''
                    order by ''' + orderby_str + ''' desc limit %s,%s''',
                        startpage, pre_page)

                elif my:

                    orderby_str = "acc_uid_at"
                    if curr=="customer_tab":
                        sql +=" and acc_confirm_at is null"
                    elif curr == "tab_confirm":
                        sql += " and acc_confirm_at is not  null and manager_confirm_at is   null "
                    elif curr == "tb_manager_confirm":
                        sql += " and manager_confirm_at is not  null  and acc_confirm_at is not  null "
                    print(sql)

                    count = self.db_customer.get(
                        '''SELECT count(*) count FROM t_customer where is_close=0 and customer_type_name like "%%记账%%"'''
                        + sql)
                    pagination = Pagination(page, pre_page, count.count,
                                            self.request)
                    startpage = (page - 1) * pre_page

                    customers = self.db_customer.query(
                        '''select * from t_customer  where is_close=0 and customer_type_name like "%%记账%%"'''
                        + sql + '''
                    order by ''' + orderby_str + ''' desc limit %s,%s''',
                        startpage, pre_page)

            self.render(
                'c/customer/customer_list_rec.html',
                customers=customers,
                pagination=pagination,
                tag=tag,
                keyword=keyword,
                lp=lp,
                jz=jz,
                my=my,
                kj=kj,
                t_user=t_user,
                curr=curr,
                qtype=qtype)
            self.finish()
        elif tag == "customer_list_uid":
            sql = ""
            keyword = self.get_argument("keyword", "")
            qtype = self.get_argument("qtype","")
            jz = self.get_argument("jz", "")
            tyctype = self.get_argument("tyctype", "0")
            lp = self.get_argument("lp", "")
            kj=self.get_argument('kj','')
            my = self.get_argument("my",None)
            t_user = self.db_customer.query("select * from "+  options.mysql_database + ".t_user where role=10 ")
            if keyword:
                sql = " and (company like '%%" + keyword + "%%')"
            if jz:
                sql = sql + " and (customer_type_name like '%%" + jz + "%%')"
            if lp:
                sql = sql + " and (customer_type_name like '%%" + lp + "%%')"

            if my:
                sql = sql + " and acc_uid = " + uid
            if kj:
                sql =  sql+" and acc_uid_name='"+kj+"' "
            query_str = ""
            query_str_count =""
            customers = None
            tyctype_sql= ""
            if tyctype:
                tyctype_sql = " and is_get=%s" % (tyctype)

            page= int(self.get_argument("page",1))
            pre_page = 20
            count = 0
            if qtype=="lname":
                count = self.db_customer.get(
                    '''SELECT count(*) count FROM t_customer a inner join (select customer_id,(concat(name,' '))
                        customer_name from t_linkman )  b on a.id=b.customer_id

                        where customer_name like  '%%''' + keyword +
                    '''%%' ''' + sql)
                pagination = Pagination(page, pre_page, count.count, self.request)
                startpage = (page - 1) * pre_page
                customers = self.db_customer.query('''SELECT a.*,b.customer_name FROM t_customer a inner join (select customer_id,(concat(name,' '))
                        customer_name from t_linkman )  b on a.id=b.customer_id

                        where customer_name like  '%%''' + keyword + '''%%' ''' + sql+''' limit %s,%s''', startpage, pre_page)

            elif qtype=="tel":
                count = self.db_customer.get( '''SELECT count(*) count FROM t_customer a inner join (select customer_id,(concat(tel,' '))
                        ctel from t_linkman )  b on a.id=b.customer_id

                        where ctel like  '%%''' + keyword + '''%%'  ''' + sql+''' ''')
                pagination = Pagination(page, pre_page, count.count, self.request)
                startpage = (page - 1) * pre_page
                customers = self.db_customer.query(
                    '''SELECT a.*,b.ctel FROM t_customer a inner join (select customer_id,(concat(tel,' '))
                        ctel from t_linkman )  b on a.id=b.customer_id

                        where ctel like  '%%''' + keyword + '''%%'   ''' +
                    sql + ''' limit %s,%s''', startpage, pre_page)


            else:
                if my==None and is_manager=='1':
                    count = self.db_customer.get(
                        '''SELECT count(*) count FROM t_customer where is_close=0 and is_get <> 0 and company_reguid_new is not  null'''
                        + sql + tyctype_sql)
                    pagination = Pagination(page, pre_page, count.count, self.request)
                    startpage = (page - 1) * pre_page

                    customers = self.db_customer.query(
                        '''select * from t_customer  where is_close=0 and is_get <> 0
                    and company_reguid_new is not  null ''' + sql +
                        tyctype_sql + '''
                    order by is_get_at desc limit %s,%s''', startpage,
                        pre_page)

                elif my:
                    count = self.db_customer.get(
                        '''SELECT count(*) count FROM t_customer where is_close=0'''
                        + sql + tyctype_sql)
                    pagination = Pagination(page, pre_page, count.count, self.request)
                    startpage = (page - 1) * pre_page

                    customers = self.db_customer.query(
                        '''select * from t_customer  where is_close=0  and is_get <> 0 and company_guid_new <> null'''
                        + sql  + tyctype_sql +
                        ''' order by created_at desc limit %s,%s''', startpage,
                        pre_page)



        #  customers = self.db_customer.query(query_str, startpage, pre_page)
            self.render(
                'c/customer/customer_list_uid.html',
                customers=customers,
                pagination=pagination,
                tag=tag,
                keyword=keyword,
                lp=lp,
                jz=jz,
                my=my,
                kj=kj,
                t_user=t_user,
                tyctype=tyctype,
                qtype=qtype)


        elif tag == "all":
            sql = ""
            keyword = self.get_argument("keyword", "")
            qtype = self.get_argument("qtype","")
            by_tag = self.get_argument("by_tag","")
            tag_id = int(self.get_argument("tag_id",0))
            jz = self.get_argument("jz", "")
            lp = self.get_argument("lp", "")
            kj=self.get_argument('kj','')
            my = self.get_argument("my",None)
            check_kj=self.get_argument('check_kj','')
            check_under=self.get_argument('check_under','')
            output = self.get_argument("output","")
            page_count=self.get_argument('page_count','')
            new_tag = self.get_argument("new_tag","1")
            tag_parent_id = int(self.get_argument("tag_parent_id",1))
            acc_uids=[]
            t_user_relation=''
            t_user = self.db_customer.query("select * from "+  options.mysql_database + ".t_user where role=10 ")
            mysql=""
            if keyword:
                sql = " and (a.company like '%%" + keyword + "%%')"
            if jz:
                sql = sql + " and (a.customer_type_name like '%%" + jz + "%%')"
            if lp:
                sql = sql + " and (a.customer_type_name like '%%" + lp + "%%')"
            if by_tag:
                sql = sql + " and (a.customer_type_name like '%%" + by_tag + "%%')"
            if my:
                mysql =  " and a.acc_uid = " + uid
            sql +=sql+mysql
            if kj and not check_under:

                if kj and  kj=="100000":
                     sql =  sql+" and a.acc_uid=0 "
                else:
                    sql =  sql+" and a.acc_uid_name='"+kj+"' "
            if check_kj and check_under and kj!="100000":
                sql=sql+" and a.acc_uid_name='"+check_kj+"' "

            query_str = ""
            query_str_count =""
            customers = None
            page= int(self.get_argument("page",1))
            pre_page = 20
            if page_count:
                pre_page=int(page_count)
            count = 0
            if tag_id:
                if tag_id==9:
                    sql+=" and is_year=1"
                elif tag_id==10:
                    sql+=" and is_clearly=1"    
                elif tag_id==5:
                    sql+=" and is_building=1"                        
                elif tag_id==11:
                    sql+=" and tag_id =0 "   
                else:
                    sql+=" and tag_id={}  ".format(tag_id)
            tag_parent_id_sql=""
            if tag_parent_id:
                tag_parent_id_sql=" and tag_parent_id={}".format(tag_parent_id)
                sql+=tag_parent_id_sql


            if qtype=="lname":
                count = self.db_customer.get(
                    '''SELECT count(*) count FROM t_customer a inner join (select customer_id,(concat(name,' '))
                        customer_name from t_linkman )  b on a.id=b.customer_id

                        where customer_name like  '%%''' + keyword +
                    '''%%' ''' + sql)
                pagination = Pagination(page, pre_page, count.count, self.request)
                startpage = (page - 1) * pre_page
                customers = self.db_customer.query('''SELECT a.*,
                 bb.is_check,bb.btype_id,bb.btype_id_name,bb.income,bb.ss_num
                ,b.customer_name FROM t_customer a 
                inner join (select customer_id,(concat(name,' '))
                        customer_name from t_linkman )  b on a.id=b.customer_id
                    left join t_customer_clearly bb on a.id=bb.customer_id
                    left join t_linkman c on  c.customer_id=a.id and c.id=(select id from t_linkman where customer_id=a.id order by is_first desc,id  limit 1 )

                        where customer_name like  '%%''' + keyword + '''%%' ''' + sql+''' limit %s,%s''', startpage, pre_page)

            elif qtype=="tel":
                count = self.db_customer.get( '''SELECT count(*) count FROM t_customer a inner join (select customer_id,(concat(tel,' '))
                        ctel from t_linkman )  b on a.id=b.customer_id

                        where ctel like  '%%''' + keyword + '''%%'  ''' + sql+''' order by id desc ''')
                pagination = Pagination(page, pre_page, count.count, self.request)
                startpage = (page - 1) * pre_page
                customers = self.db_customer.query(
                    '''SELECT a.*,
                    bb.is_check,bb.btype_id,bb.btype_id_name,bb.income,bb.ss_num,
                    b.ctel FROM t_customer a inner join (select customer_id,(concat(tel,' '))
                    ctel from t_linkman )  b on a.id=b.customer_id
                    left join t_customer_clearly bb on a.id=bb.customer_id
                    left join t_linkman c on  c.customer_id=a.id and c.id=(select id from t_linkman where customer_id=a.id order by is_first desc,id  limit 1 )
                 
                        where ctel like  '%%''' + keyword + '''%%'   ''' +
                    sql + ''' order by a.id desc limit %s,%s''', startpage, pre_page)


            else:
                t_user_relation=self.db.query('''
                    select a.* from t_user_relation a
                    inner join t_user_relation b on
                    find_in_set(a.department_name,b.department_name)
                    and b.uid=%s and b.is_leader<>0
                    where a.uid!=b.uid and a.is_leader=0
                    ''',uid)
                if t_user_relation and check_under:
                    for item in t_user_relation:
                        acc_uids.append(int(item.uid))
                    acc_uids=tuple(acc_uids)
                
                    if str(acc_uids)[-2]==',':
                        acc_uids=str(acc_uids)[:-2]+')'
                    else:
                        acc_uids=str(acc_uids)
                    count = self.db_customer.get(
                    '''SELECT count(*) count FROM t_customer a  where a.acc_uid in '''+acc_uids+''' and a.is_close=0
                ''' +sql)

                    pagination = Pagination(page, pre_page, count.count, self.request)
                    startpage = (page - 1) * pre_page
                    customers = self.db_customer.query('''
                    select a.*,bb.is_check,bb.btype_id,bb.btype_id_name,bb.income,bb.ss_num,c.name,c.tel
                    from t_customer a
                     left join t_customer_clearly bb on a.id=bb.customer_id
                    left join t_linkman c on  c.customer_id=a.id and c.id=(select id from t_linkman where customer_id=a.id order by is_first desc,id  limit 1 )
                 
                    where a.acc_uid in  '''+acc_uids+'''  and a.is_close=0 ''' + sql + '''
                                            order by a.id desc limit %s,%s
                        ''', startpage, pre_page)
                if my==None and is_manager=='1':
                    count = self.db_customer.get( '''SELECT count(*) count FROM t_customer a where a.is_close=0''' + sql)
                    pagination = Pagination(page, pre_page, count.count, self.request)
                    startpage = (page - 1) * pre_page
                    customers = self.db_customer.query('''
                    select a.*,bb.is_check,bb.btype_id,bb.btype_id_name,bb.income,bb.ss_num,c.name,c.tel
                    from t_customer a
                    left join t_customer_clearly bb on a.id=bb.customer_id
                    left join t_linkman c on  c.customer_id=a.id and c.id=(select id from t_linkman where customer_id=a.id order by is_first desc,id   limit 1 )
       
                     where is_close=0 ''' + sql + '''
                    order by a.id desc limit %s,%s''', startpage, pre_page)
                    print '''
                    select a.*,bb.is_check,bb.btype_id,bb.btype_id_name,bb.income,bb.ss_num,c.name,c.tel
                    from t_customer a
                    left join t_customer_clearly bb on a.id=bb.customer_id
                    left join t_linkman c on  c.customer_id=a.id and c.id=(select id from t_linkman where customer_id=a.id order by id desc limit 1 )
       
                               

                     where is_close=0 ''' + sql + '''
                    order by a.id desc limit %s,%s''',(startpage, pre_page)

                elif my:
                    count = self.db_customer.get( '''SELECT count(*) count FROM t_customer a where a.is_close=0''' + sql)
                    pagination = Pagination(page, pre_page, count.count, self.request)
                    startpage = (page - 1) * pre_page

                    customers = self.db_customer.query('''
                    select  a.*,bb.is_check,bb.btype_id,bb.btype_id_name,bb.income,bb.ss_num,c.name,c.tel
                   FROM t_customer a
                    left join t_customer_clearly bb on a.id=bb.customer_id
                    left join t_linkman c on  c.customer_id=a.id and c.id=(select id from t_linkman where customer_id=a.id order by is_first desc,id   limit 1 )
                  
                    where a.is_close=0 ''' + sql + '''
                    order by a.id desc limit %s,%s''', startpage, pre_page)



            t_count_all = self.db_customer.get("select count(*) c from t_customer a where   a.is_close=0  " +tag_parent_id_sql+mysql)  
            type_count_map= {}
            type_count_map[0] = ("全部",t_count_all.c)              
            if new_tag:
                t_customer_type = self.db_customer.query(
                "select * from t_type where tag='客户标签' and is_show=1  order by `order` ")
                for row in t_customer_type:
                    if row.order_int==9:
                        t_count = self.db_customer.get("select count(*) c  from t_customer a where is_year=1" +tag_parent_id_sql+mysql)
                    elif row.order_int==10:
                        t_count = self.db_customer.get("select count(*) c  from t_customer a where is_clearly=1" +tag_parent_id_sql+mysql)
                    elif row.order_int==5:
                        t_count = self.db_customer.get("select count(*) c  from t_customer a where is_building=1" +tag_parent_id_sql+mysql)                
                    elif row.order_int==11:
                        t_count = self.db_customer.get("select count(*) c  from t_customer a where tag_id=0"  +tag_parent_id_sql+mysql)                

                    else:
                        t_count = self.db_customer.get("select count(*) c from t_customer a where   tag_id={} ".format(row.order_int)+tag_parent_id_sql+mysql)

                    type_count_map[row.order_int] = (row.name,t_count.c)
                    print type_count_map
            else:
                t_customer_type = self.db_customer.query(
                "select * from t_type where tag='客户类型'")
                for row in t_customer_type:
                  
                    t_count = self.db_customer.get("select count(*) c from t_customer a where    (customer_type_name like '%%" + row.name + "%%') "+mysql)
                    type_count_map[row.id] = (row.name,t_count.c)


            t_customer_tags = self.db_customer.query("select * from t_type where tag='客户标签'  and is_show=1  ")

            if output:
                if not  my and is_manager=='1' or (role=="3" or role=="8"):
                    customers = self.db_customer.query('''select * from t_customer a  where a.is_close=0 ''' + sql + '''
                    order by a.id desc ''')
                elif my:

                    customers = self.db_customer.query('''select * from t_customer a  where a.is_close=0 ''' + sql + '''
                    order by a.id''')

                wb=xlwt.Workbook()
                sh=wb.add_sheet(u'客户列表')
                sh.write(0,0,u'编号')
                sh.write(0,1,u'公司名称')
                sh.write(0,2,u'客户类型')
                sh.write(0,3,u'地址类型')
                sh.write(0,4,u'注册区域')
                sh.write(0,5,u'社会信用代码')
                sh.write(0,6,u'客服会计')
                sh.write(0,7,u'创建时间')
                for idx,row in enumerate(customers):
                    idx=idx+1
                    sh.write(idx,0,row.id)
                    sh.write(idx,1,row.company)
                    sh.write(idx,2,row.customer_type_name)
                    sh.write(idx,3,row.addr_type)
                    sh.write(idx,4,row.zone)
                    sh.write(idx,5,row.company_reguid)
                    sh.write(idx,6,row.acc_uid_name)
                    sh.write(idx,7,row.created_at.strftime('%Y-%m-%d'))
                    print row
                wb.save('media/output/customer_-'+uid_name+'.xls')
                self.write({'output_path':'static/output/customer_-'+uid_name+'.xls'})

            else:
                self.render(
                    'c/customer/customer_list.html',
                    get_payment_info=self.get_payment_info,
                    customers=customers,
                    type_count_map=type_count_map,
                    t_user_relation=t_user_relation,
                    pagination=pagination,
                    check_under=check_under,
                    tag_parent_id=tag_parent_id,
                    tag=tag,
                    page_count=page_count,
                    keyword=keyword,
                    tag_id=tag_id,
                    t_customer_tags=t_customer_tags,
                    lp=lp,
                    jz=jz,
                    my=my,
                    new_tag=new_tag,
                    kj=kj,
                    by_tag=by_tag,
                    check_kj=check_kj,
                    t_customer_type=t_customer_type,
                    t_user=t_user,
                    qtype=qtype)

        elif tag=="customer_list_except":
            page= int(self.get_argument("page",1))
            pre_page = 20

            count = self.db_customer.get( '''select count(*) count from  '''+  options.mysql_database + '''.t_projects a   
,t_customer b 
                where customer_company=company and  (customer_company <> "")
                           and (project_name like '%%账%%' or project_name like '%%帐%%'  or 
                            a.id in (select aa.id from '''+  options.mysql_database + '''.t_projects aa ,'''+  options.mysql_database + '''.t_projects_income_detail bb
                             where aa.id=bb.project_id and service_name in ('记账','续帐费','帐册费')))
                and customer_company    in (
                    select company from t_customer  where acc_uid_name 
                    not in (select name from '''+  options.mysql_database + '''.t_user )
                ) ''' )
            pagination = Pagination(page, pre_page, count.count, self.request)
            startpage = (page - 1) * pre_page

            customers = self.db_customer.query('''select a.*,b.id customer_id ,b.guid customer_guid from '''+  options.mysql_database + '''.t_projects a   
,t_customer b 
                where customer_company=company and  (customer_company <> "")
                           and (project_name like '%%账%%' or project_name like '%%帐%%'  or 
                            a.id in (select aa.id from '''+  options.mysql_database + '''.t_projects aa ,'''+  options.mysql_database + '''.t_projects_income_detail bb
                             where aa.id=bb.project_id and service_name in ('记账','续帐费','帐册费')))
                and customer_company    in (
                    select company from t_customer  where acc_uid_name 
                    not in (select name from '''+  options.mysql_database + '''.t_user )
                )   limit %s,%s''', startpage, pre_page)
 
            self.render(
                'c/customer/customer_list_except.html',
                customers=customers,
                pagination=pagination,
                                tag=tag,
                                kj=None

               )


        elif tag=="add":
            if role=='3' or role=='2' or role=='5' or role=='8':

                company_id = self.get_argument("company_id","")
                num=self.get_argument('num','6')
                t_credit_type = self.db_customer.query(
                    "select * from t_type where tag='信用评级'")
                t_customer_rating = self.db_customer.query(
                    "select * from t_type where tag='客户等级'")

                t_customer_type = self.db_customer.query(
                    "select * from t_type where tag='客户类型'")

                t_city = self.db_customer.query(
                    "select * from t_type where tag='地市'")

                t_zone = self.db_customer.query(
                    "select * from t_type where tag='区域'")
                t_payment_type = self.db_customer.query(
                    "select * from t_type where tag='付费方式'")
                t_project = None
                t_projects=None
                if company_id:
                    t_project = self.db.get("select * from t_projects where id=%s",company_id)
                    t_projects=self.db.query("""select * from t_projects where customer_company=%s limit %s """,t_project.customer_company,int(num))
                t_user = self.db.query("select * from t_user where role=10 ")
                t_promo_types = self.db.query(
                    """select * from t_projects_type where income_category='套餐' order by order_int  """
                )
                t_type_new_parents=self.db_customer.query('''
                    select * from t_type where tag='客户标签1'
                    ''')
                t_type_new=self.db_customer.query('''
                    select * from t_type where tag='客户标签' and parent_id in (1,2) and name!='楼盘'
                    ''')
                self.render(
                    'c/customer/customer_add.html',
                    t_city=t_city,
                    t_type_new_parents=t_type_new_parents,
                    t_type_new=t_type_new,
                    t_payment_type=t_payment_type,
                    company_id=company_id,
                    t_zone = t_zone,
                    t_promo_types=t_promo_types,
                    t_project=t_project,
                    t_projects=t_projects,
                    t_credit_type=t_credit_type,
                    t_customer_type=t_customer_type,
                    t_customer_rating=t_customer_rating,
                    t_user=t_user,tag=tag,num=num)


        elif tag=="edit":

            customer_id = self.get_argument("id","")
            guid = self.get_argument("guid","")

            t_customer = self.db_customer.get(
                "select * from t_customer where id=%s and guid=%s",
                customer_id, guid)
            if not  t_customer:
                self.write("not customer")
            else:
                t_credit_type = self.db_customer.query(
                    "select * from t_type where tag='信用评级'")
                t_customer_rating = self.db_customer.query(
                    "select * from t_type where tag='客户等级'")
                t_user = self.db.query("select * from  t_user where role=10 ")
                t_customer_type = self.db_customer.query(
                    "select * from t_type where tag='客户类型'")
                t_city = self.db_customer.query(
                    "select * from t_type where tag='地市'")

                t_zone = self.db_customer.query(
                    "select * from t_type where tag='区域'")
                t_promo_types = self.db.query(
                """select * from t_projects_type where income_category='套餐' order by order_int  """
                )

                t_payment_type = self.db_customer.query(
                "select * from t_type where tag='付费方式'")
                self.render(
                    'c/customer/customer_edit.html',
                    t_city=t_city,
                    t_zone=t_zone,
                    t_promo_types=t_promo_types,
                    t_customer=t_customer,
                    t_credit_type=t_credit_type,
                    t_customer_type=t_customer_type,
                    t_customer_rating=t_customer_rating,
                    t_payment_type=t_payment_type,
                    t_user=t_user,
                    tag=tag)

        elif tag=="contract_expire":
            key=self.get_argument('keyword2','')
            page = int(self.get_argument("page", 1))
            pre_page = 20
            startpage = (page - 1) * pre_page
            expire_day=self.get_argument('expire_day','')
            all=self.get_argument('all','')
            sql=''
            if expire_day=='90':
                sql=' and a.state_id=0 and (TO_DAYS(a.end_time) - TO_DAYS(now())) >= 60 and (TO_DAYS(a.end_time) - TO_DAYS(now())) <= %s '%expire_day
            elif expire_day=='60':
                sql=' and a.state_id=0 and (TO_DAYS(a.end_time) - TO_DAYS(now())) >= 30 and (TO_DAYS(a.end_time) - TO_DAYS(now())) <= %s '%expire_day
            elif expire_day=='30':
                sql=' and a.state_id=0 and (TO_DAYS(a.end_time) - TO_DAYS(now())) >=0 and (TO_DAYS(a.end_time) - TO_DAYS(now())) <= %s '%expire_day
            elif expire_day=='0':
                sql=' and a.state_id=0 and (TO_DAYS(a.end_time) - TO_DAYS(now())) =0 '
            elif expire_day=='-1':
                sql=' and a.state_id=0 and (TO_DAYS(a.end_time) - TO_DAYS(now())) < 0 '
            if key:
                key=int(key)
                if is_manager=='1':
                    count = self.db_customer.get(
                    '''SELECT count(*) count from t_contract where (TO_DAYS(end_time) - TO_DAYS(now()))>0 and (TO_DAYS(end_time) - TO_DAYS(now())) < %s

                ''',key)
                    pagination = Pagination(page, pre_page, count.count, self.request)
                    t_contracts=self.db_customer.query(
                    '''
                    select a.*,(TO_DAYS(a.end_time) - TO_DAYS(now()))  expire_day,b.company,b.id cus_id,b.guid cus_guid, b.acc_uid_name from t_contract a
                    inner join t_customer b on a.customer_id=b.id
                    where (TO_DAYS(a.end_time) - TO_DAYS(now()))>0 and (TO_DAYS(a.end_time) - TO_DAYS(now())) < %s
                    order by (TO_DAYS(a.end_time) - TO_DAYS(now())) limit %s,%s
                    ''',key,startpage,pre_page
                    )

                else:
                    count = self.db_customer.get(
                    '''SELECT count(*) count from t_contract where (TO_DAYS(end_time) - TO_DAYS(now()))>0 and (TO_DAYS(end_time) - TO_DAYS(now())) < %s
                        and uid=%s
                ''',key,int(uid))
                    pagination = Pagination(page, pre_page, count.count, self.request)
                    t_contracts=self.db_customer.query(
                    '''
                    select a.*,(TO_DAYS(a.end_time) - TO_DAYS(now()))  expire_day,b.company,b.id cus_id,b.guid cus_guid, b.acc_uid_name from t_contract a
                    inner join t_customer b on a.customer_id=b.id
                    where (TO_DAYS(a.end_time) - TO_DAYS(now()))>0 and (TO_DAYS(a.end_time) - TO_DAYS(now())) < %s  and a.uid=%s
                    order by (TO_DAYS(a.end_time) - TO_DAYS(now())) limit %s,%s
                    ''',key,int(uid),startpage,pre_page
                    )
            else:
                if is_manager=='1' and all:
                    if sql:
                        sql=' where '+sql[4:]
                elif role=='10' and not all:
                    if sql:
                        sql=' and b.acc_uid_name="%s" where '%uid_name+sql[4:]
                    else:
                        sql=' and b.acc_uid_name="%s" '%uid_name
                else:
                    sql=' where a.uid=%s '%int(uid)+sql
                count = self.db_customer.get(
                '''SELECT count(*) count from t_contract a
                 inner join t_customer b on a.customer_id=b.id
            '''+sql)
                pagination = Pagination(page, pre_page, count.count, self.request)

                t_contracts=self.db_customer.query(
                '''
                select a.*,(TO_DAYS(end_time) - TO_DAYS(now()))  expire_day,b.company,b.id cus_id,b.guid cus_guid,b.acc_uid_name from t_contract a
                inner join t_customer b on a.customer_id=b.id  '''+sql+''' order by end_time desc limit %s,%s
                ''',startpage,pre_page
                )
            self.render(
                "c/customer/contract_expire.html",
                tag=tag,
                key=key,
                all=all,
                expire_day=expire_day,
                t_contracts=t_contracts,
                pagination=pagination,
            )

        elif tag =="company":
            sql=''
            qtype=self.get_argument('qtype','')
            keyword=self.get_argument('keyword1','')
            page= int(self.get_argument("page",1))
            state = int(self.get_argument("state", 1))
            company = self.get_argument('company', '')
            where_sql=""
            if state==1:
                sql = """ 
                inner join (
                    select group_concat(btype_id_name) gc,project_id from """ + options.mysql_database + """.t_projects_member
                    where team_id=38 group by project_id
                ) c on c.project_id=a.id
                """
                where_sql=""" and a.id not in 
                (
                select project_id from """ + options.mysql_database + """.t_projects_member
                where btype_id=155 and last_milepost_id  in ('167','162')
                and is_cancel=0   group by project_id 
                ) """
            elif state==2:
                sql="""  
           
                     inner join (
                    select group_concat(btype_id_name) gc,project_id from """ + options.mysql_database + """.t_projects_member
                    where team_id=38 group by project_id
                ) c on c.project_id=a.id
              """
            else:
                sql = """  
                   inner join (
                select project_id from """ + options.mysql_database + """.t_projects_member
                where btype_id=155 and last_milepost_id  in ('167','162')
                and is_cancel=0   group by project_id 
                ) b on  b.project_id=a.id
                     inner join (
                    select group_concat(btype_id_name) gc,project_id from """ + options.mysql_database + """.t_projects_member
                    where team_id=38 group by project_id
                ) c on c.project_id=a.id
                """
            pre_page = 20
            count = 0

            if keyword:
                sql += " and (customer_company like '%%" + keyword + "%%')"
            count = self.db_customer.get(
            """select count(*) count from """+options.mysql_database+""".t_projects a  """+sql+""" where 
            (customer_company <> "")
             """+where_sql+"""
            and (customer_company <> "无")  and (customer_company IS NOT NULL)
                and customer_company not in (select company from t_customer where company=customer_company )   order by a.created_at desc""" )
            pagination=Pagination(page,pre_page,count.count,self.request)
            startpage = (page - 1) * pre_page
            customers = self.db_customer.query(
            """select a.*,c.gc from """+options.mysql_database+""".t_projects a """+sql+"""
                where (customer_company <> "")
                """+where_sql+"""
            and (customer_company <> "无")  and (customer_company IS NOT NULL)
                and customer_company not in (select company from t_customer where company=customer_company )  order by a.created_at desc limit %s,%s""",startpage,pre_page)
            
            
            print     """select * from """+options.mysql_database+""".t_projects a """+sql+"""
                where (customer_company <> "")
                          """+where_sql+"""
            and (customer_company <> "无")  and (customer_company IS NOT NULL)
                and customer_company not in (select company from t_customer where company=customer_company )  order by a.created_at desc limit %s,%s"""

            self.render(
                'c/customer/customer_company.html',
                customers=customers,
                pagination=pagination,
                qtype=qtype,
                keyword=keyword,
                state=state,
                tag=tag)

        elif tag =="qrcode":
            id = self.get_argument("id")
            guid = self.get_argument("guid")
            qtag = self.get_argument("qtag")
            url =""
            url_path= "1"
            if qtag=="trans":
                trans_id = self.get_argument("trans_id")
                url = "http://192.168.2.168:8888/mobile?tag=uploader_trans&id=%s&guid=%s&trans_id=%s" % (
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
        elif tag == "show":
            id = self.get_argument("id")
            guid = self.get_argument("guid")
            to_tag = self.get_argument("to_tag", "customer_tab")
            gen_tag=self.get_argument('gen_tag',"all_msg")
            old_tag=self.get_argument('old_tag','')
            if not id:
                self.write("not id")
            elif not guid:
                self.write("not guid")
            else:
                t_customer = self.db_customer.get(
                    """select a.*,c.*,a.id customer_id,c.id customer_other_id,bb.is_check,
                    bb.btype_id,bb.btype_id_name,bb.income,bb.ss_num,
                    d.gc
                    from  t_customer a 
                    left join t_customer_clearly bb on a.id=bb.customer_id
                    left join t_customer_other_data c on a.id=c.customer_id
                    left join (select group_concat(genjin_state_id,'|',created_at) gc,customer_id from 
                     t_customer_genjin_milepost group by customer_id) d on a.id=d.customer_id
                    where a.id=%s and a.guid=%s""",
                    id, guid)
               
                if not t_customer:
                    self.write("not customer")
                else:
                    #  print "t_customer",t_customer.company


                    t_projects_query = self.db.query(
                        """
                            select *,ifnull(all_income,0) all_income,ifnull(aa,0) income_money3 from  """ +
                        options.mysql_database + """.t_projects b left join
(SELECT project_id,GROUP_CONCAT(concat(team_name,':',member_name)) team_view
                            FROM """ + options.mysql_database +
                        """.t_projects_member group by project_id)
                            c on  c.project_id=b.id

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

            left join ( select ifnull(sum(income_money),0) sim,project_id from t_projects_income_other  group by project_id) cc on cc.project_id=b.id


                            where b.customer_company='""" +
                        t_customer.company + """'
                     and c.project_id=b.id

                     order by b.created_at desc


                    """)
                    t_linkman = self.db_customer.query(
                        "select * from t_linkman where customer_id=%s order by is_first desc,id ",
                        id)
                    t_contract = self.db_customer.query(
                        "select *,(TO_DAYS(end_time) - TO_DAYS(now()))  expire_day from t_contract where customer_id=%s order by id desc",
                        id)
                    t_file = self.db_customer.query(
                        "select * from t_file where customer_id=%s", id)
                    t_transition = self.db_customer.query(
                        "select * from t_transition where customer_id=%s order by id desc",
                        id)
                    t_credit_type = self.db_customer.query(
                        "select * from t_type where tag='信用等级'")
                    t_account_type = self.db_customer.query(
                        "select * from t_type where tag='网站类型'")

                    t_customer_account = self.db_customer.query("select * from t_customer_account where customer_id=%s order by id desc",id)

                    t_project_income_title = self.db.query(
                        """
                                    select c.project_name, a.*,b.income_money income_money_total,b.income_title from t_projects_income_title a , (
                        select parent_id,sum(income_money) income_money,GROUP_CONCAT(concat(income_name,'|',income_money))  income_title
                        from t_projects_income group by parent_id) b ,t_projects c
                        where a.id=b.parent_id and customer_company=%s and a.project_id=c.id
                        order by created_at desc

                """, t_customer.company)
                    t_company_name = self.db_customer.query("select * from t_company_name where customer_id=%s",id)
                    t_acc = self.db_customer.query(
                        "select * from t_acc_his where customer_id=%s", id)

                    project_note = self.db_customer.query("""
                        select a.*,b.note_id,b.read_name,a.id as aid,c.remark,c.state_id from t_projects_note a
                        left join ( select note_id,GROUP_CONCAT(concat(created_name,','))  read_name
                        from t_projects_note_confirm  group by note_id) b

                         on a.id=b.note_id
                         left join (select note_id,remark,state_id from t_projects_note_check) c
                         on a.id=c.note_id
                         where a.project_id=%s order by creatd_at desc
                        """, t_customer.customer_id)
                    project_note_unread = self.db_customer.query("""
                        select * from t_projects_note a

                         where project_id=%s

                         and id not in(
								select note_id from t_projects_note_confirm where note_id=a.id and created_by=%s
                         )

                         order by creatd_at desc
                        """, t_customer.customer_id,uid)

                    t_projects_note_check=self.db_customer.query(
                    """
                    select * from t_projects_note a where project_id=%s and is_check=1
                       and id not in(
								select note_id from t_projects_note_check where note_id=a.id
                         )
                         order by creatd_at desc
                    """,t_customer.customer_id)
                    t_customer_exchange=self.db_customer.query(
                        """
                        select * from t_customer_exchange where customer_id=%s and etype=1 order by created_at desc
                        """,t_customer.customer_id
                    )
                    
                    express_type=self.db.query('''
                    select * from t_projects_type where income_category='快递类型'
                ''')
                    payment_type=self.db.query('''
                    select * from t_projects_type where income_category='快递付费'
                ''')
                    t_express=self.db.query('''
                select * from t_express where project_id=%s and guid=%s order by created_at desc''',t_customer.customer_id,t_customer.guid)
                    t_projects_type=self.db.query(
                    """
                    select * from t_projects_type where income_category='移交资料' and jiaojie_order>0 order by order_int
                    """
                    )

                    t_cutomer_addr_msg=self.db.query('''
                    select * from t_customer_addr_msg where company=%s
                ''',t_customer.company)
                    visible_other_relation=self.db.query('''
                        SELECT a.id  FROM t_projects a
                 inner join t_projects_member c on a.id=c.project_id
                 inner join  t_user_visible_other d on d.be_checker_id=member_id and d.checker_id=%s and a.uid!=d.be_checker_id
                and a.customer_company=%s''',uid,t_customer.company)
                    visible_other=self.db.query('''
                SELECT a.id  FROM t_projects a
                inner join  t_user_visible_other d on  a.uid=d.be_checker_id and d.checker_id=%s and a.customer_company=%s
                    ''',uid,t_customer.company)
                    t_customer_his_income = self.db_customer.query("select * from t_customer_his_income where company=%s",t_customer.company)
                    t_customer_genjin_state=self.db_customer.query('''
                        select * from t_customer_genjin_state order by order_int 
                    ''')
                    t_type_new_parents=self.db_customer.query('''
                    select * from t_type where tag='客户标签1'
                    ''')
                    t_type_new=self.db_customer.query('''
                    select * from t_type where tag='客户标签' and parent_id in (1,2) and name!='楼盘'
                    ''')
                    t_customer_payment=self.db_customer.get('''
                    select acc_end,id from t_customer_payment where customer_id=%s order by id desc limit 1
                    ''',t_customer.customer_id)
                    t_payment_type = self.db_customer.query(
                    "select * from t_type where tag='付费方式'")
                    t_city = self.db_customer.query(
                    "select * from t_type where tag='地市'")

                    t_zone = self.db_customer.query(
                    "select * from t_type where tag='区域'")
                    t_customer_type = self.db_customer.query(
                    "select * from t_type where tag='客户类型'")
                    
                    t_customer_genjin_msg=self.db_customer.query('''
                        select * from t_customer_genjin_msg where customer_id=%s order by created_at desc
                        ''',t_customer.customer_id)
                    t_customer_genjin_msg1=self.db_customer.query('''
                        select * from t_customer_genjin_msg where customer_id=%s and genjin_type=1 order by created_at desc
                        ''',t_customer.customer_id)
                    t_customer_genjin_msg2=self.db_customer.query('''
                        select * from t_customer_genjin_msg where customer_id=%s and genjin_type=2 order by created_at desc
                        ''',t_customer.customer_id)
                    t_customer_genjin_msg3=self.db_customer.query('''
                        select * from t_customer_genjin_msg where customer_id=%s and genjin_type=3 order by created_at desc
                        ''',t_customer.customer_id)
                    t_customer_genjin_msg4=self.db_customer.query('''
                        select * from t_customer_genjin_msg where customer_id=%s and genjin_type=4 order by created_at desc
                        ''',t_customer.customer_id)
                    

              
                    t_projects_events=self.db.query('''
                    select a.*,b.guid project_guid,c.guid customer_guid from t_projects_events a
                    left join t_projects b on a.project_id=b.id
                    left join '''+options.mysql_database_customer+'''.t_customer c 
                    on a.customer_id=c.id
                    where a.customer_id=%s
                    order by created_at desc
                    ''',t_customer.customer_id)
                    self.render(
                        "c/customer/customer_show.html",
                        t_customer_his_income=t_customer_his_income,
                        t_projects_events=t_projects_events,
                        t_acc=t_acc,
                        t_city=t_city,
                        t_zone=t_zone,
                        t_customer_type=t_customer_type,
                        t_payment_type=t_payment_type,
                        t_customer_payment=t_customer_payment,
                        t_type_new_parents=t_type_new_parents,
                        t_type_new=t_type_new,
                        old_tag=old_tag,
                        t_customer_genjin_state=t_customer_genjin_state,
                        visible_other_relation=visible_other_relation,
                        visible_other=visible_other,
                        t_cutomer_addr_msg=t_cutomer_addr_msg,
                        t_projects_type=t_projects_type,
                        t_express=t_express,
                        express_type=express_type,
                        payment_type=payment_type,
                        project_note=project_note,
                        project_note_unread=project_note_unread,
                        t_projects_note_check=t_projects_note_check,
                        from_tag=from_tag,
                        t_company_name=t_company_name,
                        t_project_income_title=t_project_income_title,
                        t_account_type=t_account_type,
                        t_customer_account=t_customer_account,
                        t_credit_type=t_credit_type,
                        customer=t_customer,
                        t_transition=t_transition,
                        t_projects_query=t_projects_query,
                        t_linkman=t_linkman,
                        t_contract=t_contract,
                        t_customer_exchange=t_customer_exchange,
                        t_file=t_file,
                        tag=tag,
                        to_tag=to_tag,
                        gen_tag=gen_tag,
                        t_customer_genjin_msg=t_customer_genjin_msg,
                         t_customer_genjin_msg1=t_customer_genjin_msg1,
                          t_customer_genjin_msg2=t_customer_genjin_msg2,
                           t_customer_genjin_msg3=t_customer_genjin_msg3,
                            t_customer_genjin_msg4=t_customer_genjin_msg4,)


        elif tag == "query_project":
            key = self.get_argument("key")
            if not key:
                self.write(u"请输入关键词！")
            else:

                search_sql = "%" + key + "%"
                projects = self.db.query(
                    '''select * from t_projects where project_name like "%'''
                    + search_sql + '''%" or customer_tel like "%''' +
                    search_sql + '''%" or customer_name like "%''' +
                    search_sql + '''%" or customer_company like "%''' +
                    search_sql + '''%" limit 50''')
                projects_order = self.db.query(
                    '''select * from t_projects where id=%s''',key)
                self.render(
                    "c/customer/customer_query.html",
                    projects=projects,
                    projects_order=projects_order,
                    key=key,
                    tag=tag)

        elif tag=="show_customer_exchange":
            customer_id=self.get_argument('customer_id','')
            project_id=self.get_argument('project_id','')
            department_name=self.get_secure_cookie('department_name')
            jd_at=self.get_argument('jd_at','')
            show_more='1'
            sel_sql=''
            if project_id:
                show_more=''
                t_customer_exchange=self.db.query('''
                select * from  t_projects_economic_census_exchange where project_id=%s  order by created_at desc
                ''',project_id)
            else:
                if department_name=='销售部':
                    if not jd_at or jd_at=='None':
                        show_more=''
                # elif department_name!='销售部' and role!='8':
                #     sel_sql=' ,if(isvisible=2,"*** (未协助完不可见)",msg) as msg '

                t_customer_exchange = self.db_customer.query(
                    """select *  from t_customer_exchange where customer_id=%s and etype=2
                    order by created_at desc limit 5""",
                    customer_id)
            self.render('c/customer/show_customer_exchange.html',
                t_customer_exchange=t_customer_exchange,
                customer_id=customer_id,show_more=show_more)

        elif tag=='operation_record':
            page=int(self.get_argument('page','1'))
            pre_page=20
            count=self.db.get('''
            select count(*) count from t_projects_events
            ''')
            pagination=Pagination(page,pre_page,count.count,self.request)
            startpage=(page-1)*pre_page
            t_projects_events=self.db.query('''
            select a.*,b.guid project_guid,c.guid customer_guid from t_projects_events a
            left join t_projects b on a.project_id=b.id
            left join '''+options.mysql_database_customer+'''.t_customer c 
            on a.customer_id=c.id
             order by created_at desc limit %s,%s
            ''',startpage,pre_page)
            self.render('c/customer/operation_record.html',
            t_projects_events=t_projects_events,
            pagination=pagination,
            tag=tag
            )

    # "company_reguid":company_reguid,
    # "industry_name":industry_name,
    # "is_general":is_general,
    # "credit_rating":credit_rating,
    # "credit_rating_name":credit_rating_name,
    # "customer_rating":customer_rating,
    # "customer_type_name":customer_type_name,
    # "customer_type":customer_type,
    # "customer_rating_name":customer_rating_name,
    @tornado.web.authenticated
    def post(self):
        tag = self.get_argument("tag")
        uid = self.get_secure_cookie("uid")
        uid_name = self.get_secure_cookie("name")
        is_manager=self.get_secure_cookie("is_manager")
        dt = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        role=self.get_secure_cookie('role')
        if tag =="check_company":
            company = self.get_argument("company")
            if company:
                t_customer= self.db_customer.get(
                    "select * from t_customer where company=%s", company)

                self.write(
                    tornado.escape.json_encode({
                        "code": len(incomes),
                        "incomes": income_arr
                    }))
        elif tag=='add_relation':
            idstr=self.get_argument('idstr')
            ids=re.split(',',idstr)
            for id in ids:
                self.db_customer.execute('''
                    insert into t_acc_his(uid,uid_name,created_at,customer_id)
                    values(%s,%s,%s,%s)
                ''',uid,uid_name,dt,id)
        elif tag == "group_confirm_kj":
            idstr=self.get_argument('idstr')
            ids=re.split(',',idstr)
            for id in ids:
                self.db_customer.execute('''
                    update t_customer set acc_confirm_at=%s,acc_confirm_uid_name=%s,acc_confirm_uid=%s
                    where id=%s and acc_uid=%s
                ''',dt,uid_name,uid, id, uid)
        elif tag == "group_confirm_manager":
            idstr=self.get_argument('idstr')
            ids=re.split(',',idstr)
            for id in ids:
                self.db_customer.execute('''
                    update t_customer set  manager_confirm_at=%s , manager_confirm_name=%s,  manager_confirm_uid=%s
                    where id=%s
                ''',dt,uid_name, uid, id)
        elif tag=="add":
            company_reguid = self.get_argument("company_reguid")
            industry_name = self.get_argument('industry_name')
            is_general = self.get_argument("is_general",0)
            credit_rating = self.get_argument("credit_rating",0)
            credit_rating_name = self.get_argument("credit_rating_name","")
            customer_rating = self.get_argument("customer_rating",0)
            customer_rating_name = self.get_argument("customer_rating_name","")
            customer_type = self.get_argument("customer_type",0)
            customer_type_name = self.get_argument("customer_type_name","")
            company = self.get_argument("company")
            reg_addr = self.get_argument('reg_addr', "")
            reg_number = self.get_argument("reg_number", "")
            reg_person = self.get_argument("reg_person", "")
            reg_bank = self.get_argument('reg_bank', "")
            reg_bank_account = self.get_argument("reg_bank", "")
            addr_type = self.get_argument("addr_type", "")
            addr_expire = self.get_argument("addr_expire", None)
            addr_cp = self.get_argument("addr_cp", "")
            remark = self.get_argument("remark", "")
            reg_tel = self.get_argument("reg_tel", "")
            land_tax = self.get_argument("land_tax", "")
            national_tax = self.get_argument("national_tax", "")
            saic = self.get_argument("saic", "")
            reg_date = self.get_argument("reg_date", None)
            end_date = self.get_argument("end_date", None)
            acc_uid_name = self.get_argument("acc_uid_name","")
            zone = self.get_argument("zone","")
            city = self.get_argument("city","")
            customer_id = self.get_argument("customer_id",0)
            customer_guid = self.get_argument("customer_guid","")
            customer_name=self.get_argument('customer_name',"")
            customer_tel=self.get_argument('customer_tel',"")
            promo_id_str=self.get_argument('promo_id','')
            service_amount_month = self.get_argument("service_amount_month",0)
            service_amount  = self.get_argument("service_amount",0)
            book_amount = self.get_argument("book_amount",0)
            pay_type_id = self.get_argument("pay_type_id",0)
            pay_typeid_name = self.get_argument("pay_typeid_name","")
            fee = self.get_argument("fee",0)
            project_id=self.get_argument('project_id')
            is_building=self.get_argument('is_building','0')
            is_clearly=self.get_argument('is_clearly','0')
            is_year=self.get_argument('is_year','0')
            tag_parent_id=self.get_argument('tag_parent_id','')
            tag_parent_name=self.get_argument('tag_parent_name','')
            tag_id=self.get_argument('tag_id','')
            tag_name=self.get_argument('tag_name','')
            if not addr_expire:
                addr_expire = None
            if not reg_date:
                reg_date = None
            if not end_date:
                end_date = None
            acc_uid = 0

            if acc_uid_name:
                acc_user = self.db.get("select id from t_user where name=%s",acc_uid_name)
                if not acc_user:
                    return self.write("会计 %s 不存在"%(acc_uid_name))
                else:
                    acc_uid = acc_user.id




            promo_id =0
            promo_id_name =""
            if promo_id_str and promo_id_str!="0":
                promo_id = promo_id_str.split("|")[0]
                promo_id_name = promo_id_str.split("|")[1]
                
            var_uuid = uuid.uuid4()
            t_customer = None
            t_customer_info= None

            if customer_id:

                t_customer_info = self.db_customer.get("select * from t_customer where id=%s and guid=%s",customer_id,customer_guid)

            if company:
                if t_customer_info:
                    if t_customer_info.company.strip() != company.strip():
                        t_customer = self.db_customer.get(
                            "select * from t_customer where company=%s", company)
                else:
                    t_customer = self.db_customer.get(
                            "select * from t_customer where company=%s", company)

            if not company:
                self.write("公司名为空。")
            elif t_customer:
                self.write({'status':'-100','id':t_customer.id,'guid':t_customer.guid})
            else:
                if customer_id:
                    #    print "customer_id", customer_id
                    if not t_customer_info:
                        self.write('-110')
                    else:
                        if t_customer_info.acc_uid_name!=acc_uid_name:
                            result = self.db_customer.execute("""
                            INSERT INTO `t_acc_his`
                                (customer_id,
                                `name`,
                                `uid`,
                                `uid_name`,
                                `created_at`,`remark`)
                                VALUES
                                (%s,%s,%s,%s,%s,'')""", customer_id, t_customer_info.acc_uid_name, uid,
                                                    uid_name,dt)
                        result = self.db_customer.execute(
                            """
                        update  `t_customer`
                                set zone=%s,city=%s, company_reguid=%s,industry_name=%s,is_general=%s,
                                credit_rating=%s,credit_rating_name=%s,customer_rating=%s,
                                customer_rating_name=%s,customer_type=%s,customer_type_name=%s,
                                `company`=%s,`reg_addr`=%s,  `reg_tel`=%s,`reg_number`=%s,`reg_person`=%s,`reg_bank`=%s, `reg_bank_account`=%s,
                                `addr_type`=%s,`addr_expire`=%s,`addr_cp`=%s,`acc_uid`=%s, `acc_uid_name`=%s,`updated_at`=%s,
                                remark=%s,`reg_date`=%s,`end_date`=%s,`saic`=%s,`national_tax`=%s,
                                `land_tax`=%s,updated_uid=%s,updated_uid_name=%s,acc_uid_at=%s,promo_id=%s,promo_id_name=%s,
                                service_amount_month=%s,service_amount=%s,book_amount=%s,paytype_id=%s,paytype_id_name=%s,fee=%s
                                where id=%s and guid=%s;

                        """, zone, city, company_reguid, industry_name,
                            is_general, credit_rating, credit_rating_name,
                            customer_rating, customer_rating_name,
                            customer_type, customer_type_name, company,
                            reg_addr, reg_tel, reg_number, reg_person,
                            reg_bank, reg_bank_account, addr_type, addr_expire,
                            addr_cp, acc_uid, acc_uid_name,dt, remark, reg_date,
                            end_date, saic, national_tax, land_tax, uid,
                            uid_name,dt, promo_id, promo_id_name,
                            service_amount_month, service_amount, book_amount,
                            pay_type_id, pay_typeid_name, fee, customer_id,
                            customer_guid)
                        if result==0:
                            event_txt=''
                            if company!=t_customer_info.company:
                                event_txt+='公司名称:'+t_customer_info.company+' 修改为 '+company
                            if reg_person!=t_customer_info.reg_person:
                                event_txt+=',法人:'+t_customer_info.reg_person+' 修改为 '+reg_person
                            if company_reguid!=t_customer_info.company_reguid:
                                event_txt+=',统一社会信用代码:'+t_customer_info.company_reguid+' 修改为 '+company_reguid
                            if industry_name!=t_customer_info.industry_name:
                                event_txt+=',行业性质:'+t_customer_info.industry_name+' 修改为 '+industry_name
                            if reg_bank!=t_customer_info.reg_bank:
                                event_txt+=',开户行:'+t_customer_info.reg_bank+' 修改为 '+reg_bank
                            if reg_bank_account!=t_customer_info.reg_bank_account:
                                event_txt+=',银行账号:'+t_customer_info.reg_bank_account+' 修改为 '+reg_bank_account
                            if acc_uid_name!=t_customer_info.acc_uid_name:
                                event_txt+=',客服会计:'+t_customer_info.acc_uid_name+' 修改为 '+acc_uid_name
                            if addr_cp!=t_customer_info.addr_cp:
                                event_txt+=',供应商:'+t_customer_info.addr_cp+' 修改为 '+addr_cp
                          
                            if int(promo_id)!=t_customer_info.promo_id:
                                event_txt+=',优惠活动:'+t_customer_info.promo_id_name+' 修改为 '+promo_id_name
                            if int(is_general)!=t_customer_info.is_general:
                                if int(is_general)==0:
                                    event_txt+=',一般纳税人改为否'
                                else:
                                    event_txt+=',一般纳税人改为是'
                            if not t_customer_info.city:
                                t_customer_info.city=''
                            if not t_customer_info.zone:
                                t_customer_info.zone=''
                            if not t_customer_info.reg_addr:
                                t_customer_info.reg_addr=''
                            if city!=t_customer_info.city or zone!=t_customer_info.zone or reg_addr!=t_customer_info.reg_addr:
                                event_txt+=',注册地址:'+t_customer_info.city+t_customer_info.zone+t_customer_info.reg_addr+' 修改为 '+city+zone+reg_addr
                            if int(credit_rating)!=t_customer_info.credit_rating:
                                event_txt+=',信用评级:'+t_customer_info.credit_rating_name+' 修改为 '+credit_rating_name
                            if int(customer_rating)!=t_customer_info.customer_rating:
                                event_txt+='.客户评级:'+t_customer_info.customer_rating_name+' 修改为 '+customer_rating    
                            if customer_type_name!=t_customer_info.customer_type_name:
                                event_txt+=',客户类型:'+t_customer_info.customer_type_name+' 修改为 '+customer_type_name
                            if int(pay_type_id)!=t_customer_info.paytype_id:
                                event_txt+=',付款方式:'+t_customer_info.paytype_id_name+' 修改为 '+pay_typeid_name
                            if float(service_amount)!=t_customer_info.service_amount:
                                event_txt+=',总服务费:'+str(t_customer_info.service_amount)+' 修改为 '+str(service_amount)

                            if float(book_amount)!=t_customer_info.book_amount:
                                event_txt+=',帐册费'+str(t_customer_info.book_amount)+' 修改为 '+str(book_amount)
                            if not t_customer_info.addr_type:
                                t_customer_info.addr_type=''
                            if addr_type!=t_customer_info.addr_type:
                                event_txt+=',地址类型:'+t_customer_info.addr_type+' 修改为 '+addr_type
                            if not t_customer_info.addr_expire:
                                t_customer_info.addr_expire=None
                            else:
                                t_customer_info.addr_expire=str(t_customer_info.addr_expire)
                            if addr_expire!=t_customer_info.addr_expire:
                                event_txt+=',地址期限:'+str(t_customer_info.addr_expire)+' 修改为 '+addr_expire
                            if  not t_customer_info.reg_date:
                                t_customer_info.reg_date=None
                            else:
                                t_customer_info.reg_date=str(t_customer_info.reg_date)
                            if reg_date!=t_customer_info.reg_date:
                                event_txt+=',成立日期:'+str(t_customer_info.reg_date)+' 修改为 '+reg_date
                            if  not t_customer_info.end_date:
                                t_customer_info.end_date=None
                            else:
                                t_customer_info.end_date=str(t_customer_info.end_date)
                            if end_date!=t_customer_info.end_date:
                                event_txt+=',执照期限:'+str(t_customer_info.end_date)+' 修改为 '+end_date
                            
                            if not t_customer_info.reg_number:
                                t_customer_info.reg_number=''
                            if reg_number!=t_customer_info.reg_number:
                                event_txt+=',注册号:'+t_customer_info.reg_number+' 修改为 '+reg_number
                            if not t_customer_info.saic:
                                t_customer_info.saic=''
                            if saic!=t_customer_info.saic:
                                event_txt+=',工商分局:'+t_customer_info.saic+' 修改为 '+saic
                            if not t_customer_info.land_tax:
                                t_customer_info.land_tax=''
                            if land_tax!=t_customer_info.land_tax:
                                event_txt+=',地税分局:'+t_customer_info.land_tax+' 修改为 '+land_tax
                            if not t_customer_info.national_tax:
                                t_customer_info.national_tax=''
                            if national_tax!=t_customer_info.national_tax:
                                event_txt+=',国税分局:'+t_customer_info.national_tax+' 修改为 '+national_tax
                            if not t_customer_info.remark:
                                t_customer_info.remark=''
                            if remark!=t_customer_info.remark:
                                event_txt+=',备注:'+t_customer_info.remark+' 修改为 '+remark
                            if event_txt:
                                if event_txt[0]==',':
                                    event_txt=event_txt[1:]
                                events.add_project_event(self,'0','修改客户',event_txt,uid,uid_name,t_customer_info.id)
                        t_projects=self.db.query(''' select * from  t_projects where customer_company=%s''',t_customer_info.company)
                        if t_projects and t_customer_info.company.strip() != company.strip():
                            self.db_customer.execute("""
                                    INSERT INTO `t_company_name`
                                        (customer_id,
                                        `name`,
                                        `uid`,
                                        `uid_name`,
                                        `created_at`,
                                        `remark`)
                                        VALUES
                                (%s,%s,%s,%s,%s,%s)""",customer_id, t_customer_info.company, uid, uid_name,dt,'')
                            self.db.execute('''
                                update t_projects set customer_company=%s,company_history=CONCAT(company_history,%s) where customer_company=%s
                            ''',company,t_customer_info.company,t_customer_info.company)
                            for t_project in t_projects:
                                self.db.execute('''
                            insert into t_projects_company_history(project_id,company,uid_name,uid,created_at)
                            values(%s,%s,%s,%s,%s)
                        ''',t_project.id,t_customer_info.company,uid_name,uid,dt)
                    
                        self.write("/customer?tag=show&id=%s&guid=%s"%(customer_id, customer_guid))
                else:
                    print('总服务费'+service_amount)
                    result = self.db_customer.execute(
                        """
                    INSERT INTO `t_customer`
                            (zone,city, company_reguid,industry_name,is_general,
                            credit_rating,credit_rating_name,customer_rating,
                            customer_rating_name,customer_type,customer_type_name,
                            `company`,
                            `reg_addr`,
                            `reg_tel`,
                            `reg_number`,
                            `reg_person`,
                            `reg_bank`,
                            `reg_bank_account`,
                            `addr_type`,
                            `addr_expire`,
                            `addr_cp`,
                            `acc_uid`,
                            `acc_uid_name`,
                            `created_at`,
                            `updated_at`,
                            `guid`,remark,`reg_date`,`end_date`,`saic`,`national_tax`,`land_tax`,uid,uid_name,acc_uid_at,promo_id,promo_id_name,
                            service_amount_month,service_amount,book_amount,paytype_id,paytype_id_name,fee,project_id,paytype_status_id,paytype_status_id_name,
                            tag_id,tag_id_name,tag_parent_id,tag_parent_id_name,is_building,is_clearly,is_year)
                            VALUES
                            (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,
                            %s,%s,%s,%s,%s,%s,%s,0,0,%s,%s,%s,%s,%s,%s,%s);

                    """,zone,city, company_reguid, industry_name, is_general, credit_rating,
                        credit_rating_name, customer_rating, customer_rating_name,
                        customer_type, customer_type_name, company, reg_addr,
                        reg_tel, reg_number, reg_person, reg_bank,
                        reg_bank_account, addr_type, addr_expire, addr_cp, acc_uid,
                        acc_uid_name,dt,dt,var_uuid, remark, reg_date, end_date, saic,
                        national_tax, land_tax,uid,uid_name,dt,promo_id,promo_id_name,service_amount_month,service_amount,book_amount,pay_type_id,pay_typeid_name,fee,project_id,
                        tag_id,tag_name,tag_parent_id,tag_parent_name,is_building,is_clearly,is_year)
                    if customer_name:
                        is_exist = self.db_customer.query(
                            """
                            select * from t_linkman a inner join t_customer b on a.customer_id=b.id
                            where a.name=%s and a.tel=%s and b.company=%s
                        """, customer_name, customer_tel, company)
                        if not is_exist:
                            self.db_customer.execute(
                            """insert into t_linkman (name,tel,remark,acc_uid,acc_uid_name,created_at,updated_at,guid,customer_id)
                    values(%s,%s,%s,%s,%s,%s,%s,uuid(),%s)""", customer_name, customer_tel,'',
                            uid, uid_name,dt,dt, result)
                if result > 0:

                    self.write("/customer?tag=show&id=%s&guid=%s"%(result,
                               var_uuid))

        elif tag=="add_kj":
            customer_ids=self.get_argument('customer_ids')
            kj_id=self.get_argument('kj_id')
            kj_name=self.get_argument('kj_name')
            customer_ids=customer_ids.split(',')
            for item in customer_ids:
                self.db_customer.execute('''
                update t_customer set acc_uid=%s,acc_uid_name=%s where id=%s
                ''',kj_id,kj_name,item)

        elif tag =="del_relation_project":
            project_id = self.get_argument("project_id")
            customer_id = self.get_argument("customer_id")
            if not project_id:
                self.write("not project_id")
            elif not customer_id:
                self.write("not customer_id")
            else:
                result = self.db_customer.execute("""
                    delete from t_customer_projects
                    where
                    project_id=%s  and customer_id=%s
                """, project_id, customer_id)
                self.write(str(result))
        elif tag =="delete_file":
            customer_id = self.get_argument("customer_id")
            file_id = self.get_argument("file_id")
            if not file_id:
                self.write("not file_id")
            elif not file_id:
                self.write("not customer_id")
            else:
                result = self.db_customer.execute("""
                    delete from t_file
                    where
                    customer_id=%s  and id=%s
                """, customer_id, file_id)
                self.write(str(result))

        elif tag == "upload":
            title = self.get_argument("file_title")
            file_remark = self.get_argument("file_remark")
            customer_id = self.get_argument("customer_id")
            file_path = None
            if not title:
                self.write("not file_title")
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

                    uuid_str = ori_filename
                    fname = "{0}_{1}{2}".format(uuid_str, customer_id,
                                                extension)

                    save_full_path = filename_full + fname
                    url_fname = "{0}{1}".format(url_path, fname)

                    output_file = open(save_full_path, 'w')
                    output_file.write(file1["body"])
                    file_path = url_fname
                result = self.db_customer.execute("""
                        INSERT INTO `t_file`
                        (
                        `customer_id`,
                        `guid`,
                        `title`,
                        `file_remark`,
                        `file_name`,
                        `created_at`,
                        `uid`,
                        `uid_name`)
                        VALUES
                        (%s, uuid(),  %s, %s, %s,%s,%s,%s);
                """, customer_id, title, file_remark, file_path,dt, uid, uid_name)
                self.write(str(result))
        elif tag =="delete_customer":
            customer_id = self.get_argument("customer_id")
            guid  = self.get_argument("guid")
            if not customer_id:
                self.write("not customer_id")
            elif not guid:
                self.write("not guid")
            else:
                self.db_customer.execute(""" delete from t_contract where customer_id =%s """,customer_id)
                self.db_customer.execute(""" delete from t_linkman where customer_id =%s """,customer_id)
                self.db_customer.execute("""delete from t_customer_projects where customer_id =%s """,customer_id)
                self.db_customer.execute(""" delete from t_file where customer_id =%s""",customer_id)
                self.db_customer.execute(""" delete from  t_transition where customer_id =%s""",customer_id)
                self.db_customer.execute(""" delete from t_acc_his where customer_id =%s""",customer_id)
                self.db_customer.execute(""" delete from t_customer_account where customer_id =%s""",customer_id)
                self.db_customer.execute("delete from t_customer where guid=%s and  id =%s",guid,customer_id)
                self.write('1')

        elif tag == "relation_project":
            project_id = self.get_argument("project_id")
            customer_id = self.get_argument("customer_id")
            if not project_id:
                self.write("not project_id")
            elif not customer_id:
                self.write("not customer_id")
            else:
                project = self.db.get("select * from t_projects where  id=%s",
                                       project_id)
                if not project:
                    self.write("not project")
                else:
                    result = self.db_customer.execute("""
                    INSERT INTO `t_customer_projects`
                        (
                        `project_id`,
                        `customer_id`,
                        `created_at`,
                        `uid_name`,
                        `uid`)
                        VALUES
                        (%s,%s,%s,%s,%s);
                    """, project_id, customer_id,dt ,uid_name, uid)

                    self.write(str(result))
        elif tag =="delete_account":
            account_id = self.get_argument("account_id")
            customer_id = self.get_argument("customer_id")
            if not  account_id:
                self.write("not accountid")
            elif not customer_id:
                self.write("not customer_id")
            else:
                result = self.db_customer.execute("delete from t_customer_account where customer_id=%s and id=%s",customer_id,account_id)
                self.write(str(result))
        # elif tag == "add_company":
        #     company_name = self.get_argument("company_name")
        #     company_remark = self.get_argument("company_remark")
        #     company_id = self.get_argument("company_id",0)
        #     customer_id = self.get_argument("customer_id")
        #     if not company_name:
        #         self.write("company_name is null")
        #     elif not customer_id:
        #         self.write("not customer_id ")
        #     else:
        #         if company_id :
        #             result = self.db_customer.execute("""
        #               update t_company_name set
        #                 `name`=%s,
        #                 `uid`=%s,
        #                 `uid_name`=%s,
        #                 `created_at`=now(),
        #                 `remark`=%s where id=%s """, company_name, uid, uid_name,
        #                                      company_remark,company_id)


        #         else:
        #             result = self.db_customer.execute("""
        #                INSERT INTO `t_company_name`
        #                 (customer_id,
        #                 `name`,
        #                 `uid`,
        #                 `uid_name`,
        #                 `created_at`,
        #                 `remark`)
        #                 VALUES
        #                 (%s,%s,%s,%s,now(),%s)""",customer_id, company_name, uid, uid_name,
        #                                      company_remark)
        #         self.write(str(result))
        elif tag == "delete_company":
            company_id = self.get_argument("company_id")
            customer_id = self.get_argument("customer_id")
            if not company_id:
                self.write("not company_id")
            elif not customer_id:
                self.write("not customer_id")
            else:
                result = self.db_customer.execute(
                    "delete from t_company_name where customer_id=%s and id=%s",
                    customer_id, company_id)
                self.write(str(result))
        elif tag == "add_company":
            company_name = self.get_argument("company_name")
            company_remark = self.get_argument("company_remark")
            company_id = int(self.get_argument("company_id"))
            customer_id = self.get_argument("customer_id")
            if not company_name:
                self.write("company_name is null")
            elif not customer_id:
                self.write("not customer_id ")
            else:
                if company_id :
                    result = self.db_customer.execute("""
                      update t_company_name set
                        `name`=%s,
                        `uid`=%s,
                        `uid_name`=%s,
                        `created_at`=%s,
                        `remark`=%s where id=%s """, company_name, uid, uid_name,dt,
                                             company_remark,company_id)


                else:
                    result = self.db_customer.execute("""
                       INSERT INTO `t_company_name`
                        (customer_id,
                        `name`,
                        `uid`,
                        `uid_name`,
                        `created_at`,
                        `remark`)
                        VALUES
                        (%s,%s,%s,%s,%s,%s)""",customer_id, company_name, uid, uid_name,dt,
                                             company_remark)
                self.write(str(result))
        # elif tag == "delete_company":
        #     company_id = self.get_argument("company_id")
        #     customer_id = self.get_argument("customer_id")
        #     if not company_id:
        #         self.write("not company_id")
        #     elif not customer_id:
        #         self.write("not customer_id")
        #     else:
        #         result = self.db_customer.execute(
        #             "delete from t_company_name where customer_id=%s and id=%s",
        #             customer_id, company_id)
        #         self.write(str(result))
        elif tag == "add_acc":
            acc_name = self.get_argument("acc_name")
            acc_remark = self.get_argument("acc_remark")
            acc_id = int(self.get_argument("acc_id", 0))
            customer_id = self.get_argument("customer_id")
            if not acc_name:
                self.write("acc_name is null")
            elif not customer_id:
                self.write("not customer_id ")
            else:
                if acc_id:
                    result = self.db_customer.execute("""
                      update t_acc_his set
                        `name`=%s,
                        `uid`=%s,
                        `uid_name`=%s,
                        `created_at`=%s,
                        `remark`=%s where id=%s """, acc_name, uid, uid_name,dt,
                                             acc_remark, acc_id)

                else:
                    result = self.db_customer.execute("""
                       INSERT INTO `t_acc_his`
                        (customer_id,
                        `name`,
                        `uid`,
                        `uid_name`,
                        `created_at`,
                        `remark`)
                        VALUES
                        (%s,%s,%s,%s,%s,%s)""", customer_id, acc_name, uid,dt,
                                             uid_name, acc_remark)
                self.write(str(result))

        elif tag == "delete_acc":
            acc_id = self.get_argument("acc_id")
            customer_id = self.get_argument("customer_id")
            if not acc_id:
                self.write("not acc_id")
            elif not customer_id:
                self.write("not customer_id")
            else:
                result = self.db_customer.execute(
                    "delete from t_acc_his where customer_id=%s and id=%s",
                    customer_id, acc_id)
                self.write(str(result))

        elif tag== "customer_note":
            note_content=self.get_argument('note_content','')
            customer_id=self.get_argument('customer_id','')
            is_cancel=self.get_argument('is_cancel','')
            note_id=self.get_argument('note_id','')
            if is_cancel:
                self.db_customer.execute('''
                    update t_projects_note set is_cancel=%s where id=%s
                ''',is_cancel,note_id)
            else:
                if note_id:
                    self.db_customer.execute(
                        '''
                        update t_projects_note set msg=%s,uid=%s,uid_name=%s where id=%s
                        ''',note_content,uid,uid_name,note_id
                    )
                else:
                    self.db_customer.execute("""
                    insert into t_projects_note(msg,creatd_at,uid,uid_name,project_id)
                    values(%s,%s,%s,%s,%s)
                    """, note_content,dt, uid, uid_name, customer_id)

        elif tag=="customer_note_confirm":
            check_val=self.get_argument('check_val')
            check_val=check_val.split(',')
            for item in check_val:
                self.db_customer.execute(
                    """
                    insert into t_projects_note_confirm(note_id,created_by,created_at,created_name)
                     values(%s,%s,%s,%s)
                    """,item,uid,dt,uid_name)

        elif tag== "delete_note":
            id = self.get_argument('id')
            self.db_customer.execute("""
                delete from t_projects_note where id=%s
                """, id)
            self.db_customer.execute(
                """
                delete from t_projects_note_confirm where note_id=%s
                """,id)

        elif tag == "add_customer_account":
            account = self.get_argument("account")
            psw = self.get_argument("psw")
            remark = self.get_argument("remark", "")
            type_id = self.get_argument("type_id")
            type_id_name = self.get_argument("type_id_name", "")
            customer_id = self.get_argument("customer_id")
            account_id = int(self.get_argument("account_id", "0"))
            # print account_id, "account_id", type(account_id)
            if not customer_id:
                self.write("customer is null")
            elif not account:
                self.write('not account')
            elif not psw:
                self.write('not psw')
            else:
                if not account_id:
                    #  print "account_id......"
                    result = self.db_customer.execute("""
                    INSERT INTO `t_customer_account`
                        (`account`,
                        `psw`,
                         created_by_uid,
                        `created_by`,
                        `updated_by`,
                         updated_by_uid,
                        `remark`,
                        `type_id`,
                        `type_id_name`,
                        `customer_id`,
                        `updated_at`,
                         `created_at`)
                        VALUES
                        (
                        %s,
                     %s,
                    %s,
                    %s,
                    %s,
                    %s,
                    %s,
                    %s,%s,%s,%s,%s)""", account, psw, uid, uid_name,
                                             uid_name, uid, remark, type_id,
                                             type_id_name, customer_id,dt,dt)
                else:
                    result = self.db_customer.execute("""
                    update `t_customer_account` set
                      `account`=%s,
                        `psw`=%s,

                        `updated_at`=%s,
                        `updated_by`=%s,
                        updated_by_uid=%s,
                        `remark`=%s,
                        `type_id`=%s,
                        `type_id_name`=%s,
                        `customer_id`=%s

                        where id=%s and customer_id=%s
                    """, account, psw, uid, uid_name, remark, type_id,
                                             type_id_name, customer_id,
                                             account_id, customer_id)

                self.write(str(result))

        elif tag=="customer_exchange":
            msg=self.get_argument('msg')
            etype=self.get_argument("etype",1)
            customer_id=self.get_argument('customer_id','')
            msg_time=self.get_argument('msg_time','')
            sale_end_at=self.get_argument('sale_end_at','')
            department_name=self.get_secure_cookie("department_name")
            assist_id=self.get_argument('assist_id','')
            isvisible=1
            project_id=self.get_argument('project_id','')
            if project_id:
                self.db.execute('''
                insert into t_projects_economic_census_exchange(msg,project_id,created_at,uid,uid_name)
                values(%s,%s,%s,%s,%s)
                ''',msg,project_id,dt,uid,uid_name)
                t_customer_exchange=self.db.query('''
                    select * from t_projects_economic_census_exchange where project_id=%s order by created_at desc
                ''',project_id)
                return self.render('c/customer/show_customer_exchange.html',
                t_customer_exchange=t_customer_exchange,
                show_more='',
                customer_id=customer_id)
            else:
                if department_name=='销售部' and (sale_end_at=='None' or sale_end_at==''):
                    isvisible=2
                if not msg_time:
                    msg_time=None
                is_upload = False
                file_path=''
                try:
                    file1 = self.request.files['file'][0]
                    is_upload = True
                except:
                    pass
                if is_upload:
                    ori_filename = file1["filename"]
                    filename_full = options.upload_path + "/customer_record/%s/" % (
                        customer_id)
                    url_path = "/static/customer_record/%s/" % (customer_id)
                    try:
                        os.makedirs(filename_full)
                    except OSError:
                        if not os.path.isdir(filename_full):
                            raise
                    extension = os.path.splitext(ori_filename)[1]

                    uuid_str = str(uuid.uuid4())
                    fname = "{0}_{1}{2}".format(uuid_str, customer_id, extension)

                    save_full_path = filename_full + fname
                    url_fname = "{0}{1}".format(url_path, fname)

                    output_file = open(save_full_path, 'w')
                    output_file.write(file1["body"])
                    file_path = url_fname
                result=self.db_customer.execute('''
                    insert into  t_customer_exchange(msg_time,msg,customer_id,created_at,uid,uid_name,file_path,etype,isvisible)
                    values(%s,%s,%s,%s,%s,%s,%s,%s,%s)''',msg_time, msg, customer_id,dt, uid,
                                        uid_name, file_path, etype,isvisible)
                if result and assist_id:
                    sale_genjin=self.db_customer.get('''
                    SELECT count(*) count,b.sale_id FROM 
                        t_customer_exchange a inner join 
                        t_customer_payment_assist b on a.customer_id=b.customer_id and a.uid=b.sale_id
                        where date_format(a.created_at,'%%Y-%%m-%%d')=date_format(now(),'%%Y-%%m-%%d') and a.customer_id=%s and b.id=%s
                        group by date_format(a.created_at,'%%Y-%%m-%%d')
                    ''',customer_id,assist_id)
                    if  sale_genjin:
                        if sale_genjin.count==1 and sale_genjin.sale_id==int(uid):
                            self.db_customer.execute('''
                        update t_customer_payment_assist set sale_genjin_count=sale_genjin_count+1 where customer_id=%s and id=%s
                        ''',customer_id,assist_id)
                        

                if result >0 and str(etype)=='2' and department_name!='销售部':
                    self.db_customer.execute('''
                    update t_customer set last_cuikuan_at=%s,last_cuikuan_msg=%s where id=%s
                    ''',dt,msg,customer_id)
                elif result >0 and str(etype)=='2' and department_name=='销售部':
                    self.db_customer.execute('''
                    update t_customer set sale_last_cuikuan_at=%s,sale_last_cuikuan_msg=%s where id=%s
                    ''',dt,msg,customer_id)

                sel_sql=''
                if department_name!='销售部' and role!='8':
                    sel_sql=' ,if(isvisible=2,"*** (未协助完不可见)",msg) as msg '

                t_customer_exchange = self.db_customer.query(
                    """select * """+sel_sql+""" from t_customer_exchange where customer_id=%s and etype=2 order by created_at desc limit 5""",
                    customer_id)
                return self.render('c/customer/show_customer_exchange.html',
                t_customer_exchange=t_customer_exchange,
                show_more='1',
                customer_id=customer_id)


        elif tag=="confirm_msg_time":
            today_exchange_ids=self.get_argument('today_exchange_ids')
            for item in str(today_exchange_ids)[1:-1].split(','):
                self.db_customer.execute('''
                    update t_customer_exchange set confirm_msg_time=1 where id=%s
                ''',item[:-1])

        elif tag=='show_customer_exchange':
            customer_id=self.get_argument('customer_id')
            t_customer_exchange = self.db_customer.get(
                """select * from t_customer_exchange where customer_id=%s and etype=2 order by created_at desc limit 1""",
                customer_id)
            self.write({'created_at':str(t_customer_exchange.created_at),'msg':t_customer_exchange.msg})

        elif tag=='more_projects':
            num=self.get_argument('num')
            customer_company=self.get_argument('customer_company')
            t_projects=self.db.query('select id,guid,project_name from t_projects where customer_company=%s limit %s',customer_company,int(num))
            self.write({'t_projects':t_projects,'num':int(num)})

        elif tag == "export_customer":
            if role == "8" or role=="3":
                pass
            else:
                return  self.write("0")
            sql = ""
            keyword = self.get_argument("keyword", "")
            qtype = self.get_argument("qtype","")

            jz = self.get_argument("jz", "")
            lp = self.get_argument("lp", "")
            kj=self.get_argument('kj','')
            my = self.get_argument("my","")
            by_tag = self.get_argument("by_tag","")
            kj_tag = ""
            if kj:
                    sql =  sql+" and acc_uid_name='"+kj+"' "
                    kj_tag="- "+kj
            if by_tag:
                sql = sql + " and (customer_type_name like '%%" + by_tag + "%%')"

            print '''select * from t_customer  where is_close=0 ''' + sql + '''
                        order by id '''               
            customers = self.db_customer.query('''select * from t_customer  where is_close=0 ''' + sql + '''
                        order by id ''')

            wb=xlwt.Workbook()
            if not by_tag:
                by_tag="_全部"
            else:
                by_tag="_"+by_tag
            file_name=u'客户列表{}{}'.format(by_tag,kj_tag)
            sh=wb.add_sheet(u'客户列表{}{}'.format(by_tag,kj_tag))
            sh.write(0,0,u'编号')
            sh.write(0,1,u'公司名称')
            sh.write(0,2,u'客户类型')
            sh.write(0,3,u'地址类型')
            sh.write(0,4,u'注册区域')
            sh.write(0,5,u'社会信用代码')
            sh.write(0,6,u'客服会计')
            sh.write(0,7,u'创建时间')
            for idx,row in enumerate(customers):
                idx=idx+1
                sh.write(idx,0,row.id)
                sh.write(idx,1,row.company)
                sh.write(idx,2,row.customer_type_name)
                sh.write(idx,3,row.addr_type)
                sh.write(idx,4,row.zone)
                sh.write(idx,5,row.company_reguid)
                sh.write(idx,6,row.acc_uid_name)
                if row.created_at:
                    sh.write(idx,7,row.created_at.strftime('%Y-%m-%d'))
                else:

                    sh.write(idx,7,"")

            wb.save('media/output/{}_'.format(file_name)+uid_name+'_导出.xls')
            self.write({'output_path':'static/output/{}_'.format(file_name)+uid_name+'_导出.xls'})

        elif tag=="edit_customer_other":
            company=self.get_argument('company','')
            acc_uid_name=self.get_argument('acc_uid_name','')
            current_acc_uid_name=self.get_argument('current_acc_uid_name','')
            hangye=self.get_argument('hangye','')
            reg_bank=self.get_argument('reg_bank','')
            saic=self.get_argument('saic','')
            addr_type=self.get_argument('addr_type','')
            national_tax=self.get_argument('national_tax','')
            land_tax=self.get_argument('land_tax','')
            zg_name=self.get_argument('zg_name','')
            zg_tel=self.get_argument('zg_tel','')
            business_scope=self.get_argument('business_scope','')
            attention=self.get_argument('attention','')
            zg_option=self.get_argument('zg_option','')
            customer_id=self.get_argument('customer_id')
            customer_other_id=self.get_argument('customer_other_id','')
            step=self.get_argument('step','')
            reg_bank_account=self.get_argument('reg_bank_account','')
            is_general=self.get_argument('is_general','')
            survey=self.get_argument('survey','')
            is_check=self.get_argument('is_check','')
            btype_id=self.get_argument('btype_id','')
            btype_id_name=self.get_argument('btype_id_name','')
            shuizhong_detail=self.get_argument('shuizhong_detail','')
            zhengshou_way=self.get_argument('zhengshou_way','')
            shuikong_type=self.get_argument('shuikong_type','')
            ss_num=self.get_argument('ss_num','')
            fixed_assets=self.get_argument('fixed_assets','')
            legal_id_card=self.get_argument('legal_id_card','')
            rel_name_collect_account=self.get_argument('rel_name_collect_account','')
            rel_name_collect_password=self.get_argument('rel_name_collect_password','')
            shuipan_password=self.get_argument('shuipan_password','')
            shuipan_command=self.get_argument('shuipan_command','')
            per_income_apply_password=self.get_argument('per_income_apply_password','')
            receipt_card_password=self.get_argument('receipt_card_password','')
            accumulation_fund_password=self.get_argument('accumulation_fund_password','')
            txt=''
            t_customer=self.db_customer.get(' select * from t_customer where id=%s ',customer_id)
            t_customer_other_data=self.db_customer.get(' select * from t_customer_other_data where id=%s ',customer_other_id)
            t_customer_clearly=self.db_customer.get(' select * from t_customer_clearly where customer_id=%s '%customer_id)
            if step=='1':
                
                acc_user=''
                acc_uid=0
                if acc_uid_name:
                    acc_user = self.db.get("select id from t_user where name=%s",acc_uid_name)
                    if not acc_user:
                        self.write({'error_acc':"会计 %s 不存在"%(acc_uid_name)})
                    else:
                        acc_uid = acc_user.id
                result=self.db_customer.execute('''
                        update t_customer set company=%s,acc_uid_name=%s,acc_uid=%s,reg_bank=%s,
                        saic=%s,addr_type=%s,reg_bank_account=%s,national_tax=%s,land_tax=%s where id=%s
                    ''',company,acc_uid_name,acc_uid,reg_bank,saic,addr_type,reg_bank_account,national_tax,land_tax,customer_id)
                if current_acc_uid_name!=acc_uid_name:
                    self.db_customer.execute('''
                    insert into t_acc_his(name,uid,uid_name,created_at,customer_id,remark)
                    values(%s,%s,%s,%s,%s,%s)
                    ''',current_acc_uid_name,uid,uid_name,dt,customer_id,'')
                if not customer_other_id :
                    result1=self.db_customer.execute('''
                    insert into t_customer_other_data(hangye,zg_name,zg_tel,business_scope,attention,zg_option,customer_id,update_at)
                    values(%s,%s,%s,%s,%s,%s,%s,%s)
                    ''',hangye,zg_name,zg_tel,business_scope,attention,zg_option,customer_id,dt)
                else:
                    result1=self.db_customer.execute('''
                    update t_customer_other_data set hangye=%s,zg_name=%s,zg_tel=%s,business_scope=%s,attention=%s,zg_option=%s,update_at=%s
                    where id=%s
                    ''',hangye,zg_name,zg_tel,business_scope,attention,zg_option,dt,customer_other_id)
                if result==0:
                    if t_customer.company!=company:
                        txt+=',公司名称:'+t_customer.company+' 修改为 '+company
                    
                    if t_customer.acc_uid_name!=acc_uid_name:
                        txt+=',客服会计:'+t_customer.acc_uid_name+' 修改为 '+acc_uid_name
                    if t_customer.reg_bank!=reg_bank:
                        txt+=',开户行:'+t_customer.reg_bank+' 修改为 '+reg_bank
                    if t_customer.saic!=saic:
                        txt+=',工商分局:'+t_customer.saic+' 修改为 '+saic
                    if t_customer.addr_type!=addr_type:
                        txt+=',地址类型:'+t_customer.addr_type+' 修改为 '+addr_type
                    if t_customer.reg_bank_account!=reg_bank_account:
                        txt+=',银行账号:'+t_customer.reg_bank_account+' 修改为 '+reg_bank_account
                    if t_customer.national_tax!=national_tax:
                        txt+=',国所属分局:'+t_customer.national_tax+' 修改为 '+national_tax
                    if t_customer.land_tax!=land_tax:
                        txt+=',地所属分局:'+t_customer.land_tax+' 修改为 '+land_tax

                if result1>0:
                    if hangye:
                       txt+=',所属行业:修改为 '+hangye
                    if zg_name:
                        txt+=',专管员姓名:修改为 '+zg_name
                    if zg_tel:
                        txt+=',专管员联系方式:修改为 '+zg_tel
                    if business_scope:
                        txt+=',经营范围:修改为 '+business_scope
                    if attention:
                        txt+=',情况和注意事项:修改为 '+attention
                    if zg_option:
                        txt+=',主管意见:修改为 '+zg_option
                if result1==0:
                    if (t_customer_other_data.hangye if t_customer_other_data.hangye else '')!=hangye:
                        txt+=',所属行业:'+t_customer_other_data.hangye+' 修改为 '+hangye
                    if (t_customer_other_data.zg_name if t_customer_other_data.zg_name else '')!=zg_name:
                        txt+=',专管员姓名:'+t_customer_other_data.zg_name+' 修改为 '+zg_name
                    if (t_customer_other_data.zg_tel if t_customer_other_data.zg_tel else '')!=zg_tel:
                        txt+=',专管员联系方式:'+t_customer_other_data.zg_tel+' 修改为 '+zg_tel

                    if (t_customer_other_data.business_scope if t_customer_other_data.business_scope else '')!=business_scope:
                        txt+=',经营范围:'+t_customer_other_data.business_scope+' 修改为 '+business_scope
                    if (t_customer_other_data.attention if t_customer_other_data.attention else '')!=attention:
                        txt+=',情况和注意事项:'+t_customer_other_data.attention+' 修改为 '+attention
                    if (t_customer_other_data.zg_option if t_customer_other_data.zg_option else '')!=zg_option:
                        txt+=',主管意见:'+t_customer_other_data.zg_option+' 修改为 '+zg_option

                if txt:
                    events.add_project_event(self,0, "修改客户", txt[1:],
                                         uid, uid_name,customer_id)


            elif step=='2':
                result=self.db_customer.execute('''
                        update t_customer set is_general=%s where id=%s
                    ''',is_general,customer_id)
                result1=self.db_customer.execute('''
                        update t_customer_clearly set is_check=%s,btype_id=%s,
                        btype_id_name=%s,ss_num=%s where customer_id=%s
                ''',is_check,btype_id,btype_id_name,ss_num,customer_id)
                if not customer_other_id :
                    result2=self.db_customer.execute('''
                    insert into t_customer_other_data(survey,shuizhong_detail,zhengshou_way,shuikong_type,fixed_assets,customer_id,update_at)
                    values(%s,%s,%s,%s,%s,%s,%s)
                    ''',survey,shuizhong_detail,zhengshou_way,shuikong_type,fixed_assets,customer_id,dt)
                else:
                    result2=self.db_customer.execute('''
                    update t_customer_other_data set survey=%s,shuizhong_detail=%s,zhengshou_way=%s,shuikong_type=%s,fixed_assets=%s,update_at=%s
                    where id=%s
                    ''',survey,shuizhong_detail,zhengshou_way,shuikong_type,fixed_assets,dt,customer_other_id)
                if result==0:
                    if t_customer.is_general!=int(is_general):
                        if is_general=='0':
                            txt+=',纳税类型:一般纳税人 修改为 小规模'
                        elif is_general=='1':
                            txt+=',纳税类型:小规模 修改为 一般纳税人'
                if result1==0 and t_customer_clearly:
                    if t_customer_clearly.is_check!=int(is_check):
                        if is_check=='0':
                            txt+=',税种:是('+t_customer_clearly.btype_id_name+') 修改为 否'
                        elif is_check=='1':
                            txt+=',税种:否 修改为 是('+btype_id_name+')'
                    if t_customer_clearly.ss_num!=ss_num:
                        txt+=',社保:'+t_customer_clearly.ss_num+' 修改为 '+ss_num
                if result2>0:
                    if survey:
                        txt+=',税务概况:修改为 '+survey
                    if shuizhong_detail:
                        txt+=',税种明细:修改为 '+shuizhong_detail
                    if zhengshou_way:
                        txt+=',征收方式:修改为 '+zhengshou_way
                    if shuikong_type:
                        txt+=',税控盘类别:修改为 '+shuikong_type
                    if fixed_assets:
                        txt+=',固定资产:修改为 '+fixed_assets

                elif result2==0:
                    t_customer_other_data.survey=t_customer_other_data.survey if t_customer_other_data.survey else ''
                    t_customer_other_data.shuizhong_detail=t_customer_other_data.shuizhong_detail if t_customer_other_data.shuizhong_detail else ''
                    t_customer_other_data.zhengshou_way=t_customer_other_data.zhengshou_way if t_customer_other_data.zhengshou_way else ''
                    t_customer_other_data.shuikong_type=t_customer_other_data.shuikong_type if t_customer_other_data.shuikong_type else ''
                    t_customer_other_data.fixed_assets=t_customer_other_data.fixed_assets if t_customer_other_data.fixed_assets else ''
                    if t_customer_other_data.survey!=survey:
                        txt+=',税务概况:'+t_customer_other_data.survey+' 修改为 '+survey
                    if t_customer_other_data.shuizhong_detail!=shuizhong_detail:
                        txt+=',税种明细:'+t_customer_other_data.shuizhong_detail+' 修改为 '+shuizhong_detail

                    if t_customer_other_data.zhengshou_way!=zhengshou_way:
                        txt+=',征收方式:'+t_customer_other_data.zhengshou_way+' 修改为 '+zhengshou_way                   
                    if t_customer_other_data.shuikong_type!=shuikong_type:
                        txt+=',税控盘类别:'+t_customer_other_data.shuikong_type+' 修改为 '+shuikong_type                    
                    if t_customer_other_data.fixed_assets!=fixed_assets:
                        txt+=',固定资产:'+t_customer_other_data.fixed_assets+' 修改为 '+fixed_assets
                
                if txt:
                    events.add_project_event(self,0, "修改客户", txt[1:],
                                         uid, uid_name,customer_id)

            elif step=='3':
                if not customer_other_id :
                    result=self.db_customer.execute('''
                    insert into t_customer_other_data(legal_id_card,rel_name_collect_account,
                    rel_name_collect_password,shuipan_password,
                    shuipan_command,per_income_apply_password,receipt_card_password,accumulation_fund_password,
                    customer_id,update_at)
                    values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
                    ''',legal_id_card,rel_name_collect_account,rel_name_collect_password,shuipan_password,
                    shuipan_command,per_income_apply_password,receipt_card_password,accumulation_fund_password,customer_id,dt)
                else:
                    result=self.db_customer.execute('''
                    update t_customer_other_data set legal_id_card=%s,rel_name_collect_account=%s,
                    rel_name_collect_password=%s,shuipan_password=%s,
                    shuipan_command=%s,per_income_apply_password=%s,receipt_card_password=%s,accumulation_fund_password=%s,update_at=%s
                    where id=%s
                    ''',legal_id_card,rel_name_collect_account,rel_name_collect_password,shuipan_password,
                    shuipan_command,per_income_apply_password,receipt_card_password,accumulation_fund_password,dt,customer_other_id)

                if result>0:
                    if legal_id_card:
                        txt+=',法人身份证号:修改为 '+legal_id_card
                    if rel_name_collect_account:
                        txt+=',实名采集账号:修改为 '+rel_name_collect_account
                    if rel_name_collect_password:
                        txt+=',实名采集密码:修改为 '+rel_name_collect_password
                    if shuipan_password:
                        txt+=',税控盘密码:修改为 '+shuipan_password
                    if shuipan_command:
                        txt+=',税控盘口令:修改为 '+shuipan_command
                    if per_income_apply_password:
                        txt+=',个税申报密码:修改为 '+per_income_apply_password
                    if receipt_card_password:
                        txt+=',回单卡密码:修改为 '+receipt_card_password
                    if accumulation_fund_password:
                        txt+=',公积金证书密码:修改为 '+accumulation_fund_password
                elif result==0:
                    t_customer_other_data.legal_id_card=t_customer_other_data.legal_id_card if t_customer_other_data.legal_id_card else ''
                    t_customer_other_data.rel_name_collect_account=t_customer_other_data.rel_name_collect_account if t_customer_other_data.rel_name_collect_account else ''
                    t_customer_other_data.rel_name_collect_password=t_customer_other_data.rel_name_collect_password if t_customer_other_data.rel_name_collect_password else ''
                    t_customer_other_data.shuipan_password=t_customer_other_data.shuipan_password if t_customer_other_data.shuipan_password else ''
                    t_customer_other_data.shuipan_command=t_customer_other_data.shuipan_command if t_customer_other_data.shuipan_command else ''
                    t_customer_other_data.per_income_apply_password=t_customer_other_data.per_income_apply_password if t_customer_other_data.per_income_apply_password else ''
                    t_customer_other_data.receipt_card_password=t_customer_other_data.receipt_card_password if t_customer_other_data.receipt_card_password else ''
                    t_customer_other_data.accumulation_fund_password=t_customer_other_data.accumulation_fund_password if t_customer_other_data.accumulation_fund_password else ''
                    if t_customer_other_data.legal_id_card!=legal_id_card:
                        txt+=',法人身份证号:'+t_customer_other_data.legal_id_card+' 修改为 '+legal_id_card
                    if t_customer_other_data.rel_name_collect_account!=rel_name_collect_account:
                        txt+=',实名采集账号:'+t_customer_other_data.rel_name_collect_account+' 修改为 '+rel_name_collect_account

                    if t_customer_other_data.rel_name_collect_password!=rel_name_collect_password:
                        txt+=',实名采集密码:'+t_customer_other_data.rel_name_collect_password+' 修改为 '+rel_name_collect_password

                    if t_customer_other_data.shuipan_password!=shuipan_password:
                        txt+=',税控盘密码:'+t_customer_other_data.shuipan_password+' 修改为 '+shuipan_password

                    if t_customer_other_data.shuipan_command!=shuipan_command:
                        txt+=',税控盘口令:'+t_customer_other_data.shuipan_command+' 修改为 '+shuipan_command

                    if t_customer_other_data.per_income_apply_password!=per_income_apply_password:
                        txt+=',个税申报密码:'+t_customer_other_data.per_income_apply_password+' 修改为 '+per_income_apply_password

                    if t_customer_other_data.receipt_card_password!=receipt_card_password:
                        txt+=',回单卡密码:'+t_customer_other_data.receipt_card_password+' 修改为 '+receipt_card_password

                    if t_customer_other_data.accumulation_fund_password!=accumulation_fund_password:
                        txt+=',公积金证书密码:'+t_customer_other_data.accumulation_fund_password+' 修改为 '+accumulation_fund_password                  
                if txt:
                    events.add_project_event(self,0, "修改客户", txt[1:],
                                         uid, uid_name,customer_id)

        elif tag=="edit_customer_head":
            company=self.get_argument("company",'')
            reg_person=self.get_argument("reg_person",'')
            company_reguid=self.get_argument("company_reguid",'')
            reg_date=self.get_argument("reg_date",'')
            link_name=self.get_argument("link_name",'')
            link_tel=self.get_argument("link_tel",'')
            link_id=self.get_argument("link_id",'')
            is_general=self.get_argument("is_general",'0')
            addr_type=self.get_argument("addr_type",'')
            payment_id=self.get_argument("payment_id",'')
            pay_type_id=self.get_argument("pay_type_id",'')
            fee=self.get_argument("fee",'')
            pay_typeid_name=self.get_argument("pay_typeid_name",'')
            service_amount=self.get_argument("service_amount",'0')
            service_amount_month=self.get_argument('service_amount_month','0')
            book_amount=self.get_argument("book_amount",'0')
            acc_end=self.get_argument("acc_end",'')
            city=self.get_argument("city",'')
            zone=self.get_argument("zone",'')
            reg_addr=self.get_argument("reg_addr",'')
            old_tag=self.get_argument("old_tag",'')
            customer_type = self.get_argument("customer_type",0)
            customer_type_name = self.get_argument("customer_type_name","")
            tag_parent_id=self.get_argument('tag_parent_id','')
            tag_parent_name=self.get_argument('tag_parent_name','')
            tag_id=self.get_argument('tag_id','')
            tag_name=self.get_argument('tag_name','')
            customer_id=self.get_argument('customer_id')
            is_building=self.get_argument('is_building','0')
            is_clearly=self.get_argument('is_clearly','0')
            is_year=self.get_argument('is_year','0')
            t_customer=self.db_customer.get(''' select * from t_customer where id=%s ''',customer_id)
            t_linkman=self.db_customer.get(' select * from t_linkman where id=%s ',link_id)
            t_customer_payment=self.db_customer.get(' select * from t_customer_payment where id=%s ',payment_id)
            sql=',customer_type="%s",customer_type_name="%s"'%(customer_type,customer_type_name)
            result=None
            result1=None
            result2=None
            if not reg_date:
                reg_date=None
            if not acc_end:
                acc_end=None
            if not old_tag:
                sql=''',tag_id=%s,tag_id_name='%s',
                tag_parent_id=%s,tag_parent_id_name='%s',is_building=%s,is_clearly=%s,is_year=%s
                '''%(tag_id,tag_name,tag_parent_id,tag_parent_name,is_building,is_clearly,is_year)
            if link_id:
                result=self.db_customer.execute('''
                update t_linkman set name=%s,tel=%s where id=%s
                ''',link_name,link_tel,link_id)
            if payment_id:
                result1=self.db_customer.execute('''
                    update t_customer_payment set fee=%s,pay_typeid=%s,pay_typeid_name=%s,service_month_amount=%s,
                    service_amount=%s,book_amount=%s,acc_end=%s where id=%s
                ''',fee,pay_type_id,pay_typeid_name,service_amount_month,service_amount,book_amount,acc_end,payment_id)
                sql+='''
                ,paytype_id=%s,paytype_id_name="%s",fee=%s,service_amount=%s,service_amount_month=%s,book_amount=%s
                '''%(pay_type_id,pay_typeid_name,fee,service_amount,service_amount_month,book_amount)
            result2=self.db_customer.execute('''
            update t_customer set  company=%s,reg_person=%s,company_reguid=%s,reg_date=%s,is_general=%s,
            addr_type=%s,city=%s,zone=%s,reg_addr=%s '''+sql+''' where id=%s
            ''',company,reg_person,company_reguid,reg_date,is_general,addr_type,city,zone,reg_addr,customer_id)
            txt=''
            if result==0:
                if t_linkman.name!=link_name:
                    txt+=',首要联系人:'+t_linkman.name+' 修改为 '+link_name
                if t_linkman.tel!=link_tel:
                    txt+=',首要联系电话:'+t_linkman.tel+' 修改为 '+link_tel
            if result1==0:
                if t_customer_payment.pay_typeid_name!=pay_typeid_name:
                    txt+=',付费方式:'+t_customer_payment.pay_typeid_name+' 修改为 '+pay_typeid_name
                if int(t_customer_payment.service_amount)!=int(service_amount):
                    txt+=',总服务费:'+str(t_customer_payment.service_amount)+' 修改为 '+str(service_amount)
                    txt+=',月服务费:'+str(t_customer_payment.service_month_amount)+' 修改为 '+str(service_amount_month)
                if int(t_customer_payment.book_amount)!=int(book_amount):
                    txt+=',账册费:'+str(t_customer_payment.book_amount)+' 修改为 '+str(book_amount)
                if  not t_customer_payment.acc_end:
                    t_customer_payment.acc_end=None
                else:
                    t_customer_payment.acc_end=str(t_customer_payment.acc_end.strftime("%Y-%m-%d"))
                if t_customer_payment.acc_end!=acc_end:
                    txt+=',账费到期:'+t_customer_payment.acc_end+' 修改为 '+str(acc_end)

            if result2==0:
                if t_customer.company!=company:
                    txt+=',公司名:'+t_customer.company+' 修改为 '+company
                if t_customer.reg_person!=reg_person:
                    txt+=',法人:'+t_customer.reg_person+' 修改为 '+reg_person
                if t_customer.company_reguid!=company_reguid:
                    txt+=',信用代码'+t_customer.company_reguid+' 修改为 '+company_reguid
                if not t_customer.reg_date:
                    t_customer.reg_date=str(None)
                else:
                    t_customer.reg_date=str(t_customer.reg_date.strftime("%Y-%m-%d"))
                if t_customer.reg_date!=reg_date:
                    txt+=',执照成立日期:'+t_customer.reg_date+' 修改为 '+str(reg_date)
                if t_customer.is_general!=int(is_general):
                    if is_general=='0':
                        txt+=',纳税类型:一般纳税人 修改为 小规模'
                    elif is_general=='1':
                         txt+=',纳税类型:小规模 修改为 一般纳税人'
                if t_customer.addr_type!=addr_type:
                    txt+=',地址类型:'+t_customer.addr_type+' 修改为 '+addr_type
                if t_customer.city!=city or t_customer.zone!=zone or t_customer.reg_addr!=reg_addr:
                    txt+=',注册地址:'+t_customer.city+t_customer.zone+t_customer.reg_addr+' 修改为 '+city+zone+reg_addr
                if not old_tag:
                    if t_customer.tag_id_name!=tag_name or t_customer.tag_parent_id_name!=tag_parent_name or \
                    t_customer.is_building!=int(is_building) or t_customer.is_clearly!=int(is_clearly) or t_customer.is_year!=int(is_year):
                        if t_customer.tag_id_name=='非记账':
                            parent_tag_name=''
                        else:
                            parent_tag_name=','+t_customer.tag_id_name
                        if tag_name=='非记账':
                            childrent_tag_name=''
                        else:
                            childrent_tag_name=','+tag_name
                        if t_customer.is_building:
                            parent_is_building=',楼盘'
                        else:
                            parent_is_building=''
                        if t_customer.is_clearly:
                            parent_is_clearly=',汇算清缴'
                        else:
                            parent_is_clearly=''
                        if t_customer.is_year:
                            parent_is_year=',工商年检'
                        else:
                            parent_is_year=''
                        if is_building:
                            childrent_is_building=',楼盘'
                        else:
                            childrent_is_building=''
                        if is_clearly:
                            childrent_is_clearly=',汇算清缴'
                        else:
                            childrent_is_clearly=''
                        if is_year:
                            childrent_is_year=',工商年检'
                        else:
                            childrent_is_year=''
                        parent=parent_tag_name+parent_is_building+parent_is_clearly+parent_is_year
                        childrent=childrent_tag_name+childrent_is_building+childrent_is_clearly+childrent_is_year
                        txt+=',标签类型:'+t_customer.tag_parent_id_name+parent+' 修改为 '+tag_parent_name+childrent
            if txt:
                if txt[0]==',':
                    txt=txt[1:]
                events.add_project_event(self,0, "修改客户", txt,
                                         uid, uid_name,customer_id)

        elif tag=="add_customer_state":
            state_id=self.get_argument('state_id','')
            customer_id=self.get_argument('customer_id')
            update_state_ids=self.get_argument('update_state_ids','')
            if update_state_ids:
                for item in update_state_ids.split(','):
                    t_customer_genjin_milepost=self.db_customer.get('''
                    select * from t_customer_genjin_milepost where customer_id=%s and genjin_state_id=%s
                ''',customer_id,item)
                    if not t_customer_genjin_milepost:
                        self.db_customer.execute('''
                    insert into t_customer_genjin_milepost(customer_id,genjin_state_id,uid,uid_name,created_at)
                    values(%s,%s,%s,%s,%s)
                    ''',customer_id,item,uid,uid_name,dt)
            else:
                t_customer_genjin_milepost=self.db_customer.get('''
                    select * from t_customer_genjin_milepost where customer_id=%s and genjin_state_id=%s
                ''',customer_id,state_id)
                if not t_customer_genjin_milepost:
                    self.db_customer.execute('''
                    insert into t_customer_genjin_milepost(customer_id,genjin_state_id,uid,uid_name,created_at)
                    values(%s,%s,%s,%s,%s)
                    ''',customer_id,state_id,uid,uid_name,dt)
        
        elif tag=="dongtai_genjin":
            customer_id=self.get_argument('customer_id')
            dongtai_msg=self.get_argument('dongtai_msg','')
            genjin_type=self.get_argument('genjin_type')
            file_path = None
            is_upload = False
            try:
                file1 = self.request.files['file'][0]
                is_upload = True
            except:
                pass
            if is_upload:
                ori_filename = file1["filename"]
                filename_full = options.upload_path + "/customer/genjin/%s/" % (
                    customer_id)
                url_path = "/static/customer/genjin/%s/" % (customer_id)
                try:
                    os.makedirs(filename_full)
                except OSError:
                    if not os.path.isdir(filename_full):
                        raise
                extension = os.path.splitext(ori_filename)[1]

                uuid_str = ori_filename
                fname = "{0}_{1}{2}".format(uuid_str, customer_id,
                                            extension)

                save_full_path = filename_full + fname
                url_fname = "{0}{1}".format(url_path, fname)

                output_file = open(save_full_path, 'w')
                output_file.write(file1["body"])
                file_path = url_fname
            self.db_customer.execute('''
            insert into t_customer_genjin_msg(customer_id,file_path,created_at,uid_name,uid,msg,genjin_type)
            values(%s,%s,%s,%s,%s,%s,%s)
            ''',customer_id,file_path,dt,uid_name,uid,dongtai_msg,genjin_type)

    @run_on_executor(executor="_thread_pool")
    def runSql(self):
        dt = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        if self.request.host.split(':')[1]=='9000':
            database=" db_customer.t_customer "
        else:
            database=" db_customer_test.t_customer "
        project_milepost_type = self.db.query(
        """select  c.customer_company,b.btype_name,b.uid from t_projects_type a
    inner join t_projects_milepost b on b.type_id=a.id and b.type_name='办结'
    and b.confirm_at is not null
    inner join t_projects c on b.project_id=c.id
    inner join """+database+""" d on c.customer_company=d.company and is_wait is null
    where a.income_category='办结' and a.is_hide=0
        order by b.order_int"""
        )
        if project_milepost_type:
            for item in project_milepost_type:
                self.db_customer.execute('''
                update t_customer set is_wait=0,is_wait_at=%s,is_wait_uid=%s,
                wait_from_type=CONCAT(wait_from_type,%s)
                where company=%s
            ''',dt,item.uid,item.btype_name+',',item.customer_company)

class CustomerForm(object):
    def __init__(self):
        self.customer_id = "(^\d+$)"

    def check_valid(self, request):
        flag = True
        form_dict = self.__dict__
        allerror_message = {}
        error_message = {}
        for key, regular in form_dict.items():
            post_value = request.get_argument(key)
            ret = re.match(regular, post_value)
            if not ret:
                flag = False
        return flag





class InsertcustomerHandler(BaseHandler):
    @tornado.web.authenticated
    def get(self):
        dt = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        logger.info("%s : %s  - %s " % (dt, uid_name, self.request.uri))
        return self.render('insertcustomer.html')

    @tornado.web.authenticated
    def post(self):
        dt = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        logger.info("%s : %s  - %s " % (dt, uid_name, self.request.uri))
        cusform = CustomerForm()
        cus = cusform.check_valid(self)
        if not cus:
            self.redirect('/insert_customer')
        db = self.application.db
        customer_id = self.get_argument('customer_id')
        customers = db.query(
            'select * from t_customer where customer_id=%s', customer_id)
        if len(customers) != 0:
            self.render('insertcustomer.html', error_id=customer_id)
        company = self.get_argument('company')
        linkman = self.get_argument('linkman')
        phone = self.get_argument('phone')
        yewu_content = self.get_argument('yewu_content')
        address_style = self.get_argument('address_style')
        start_hetong = self.get_argument('start_hetong') or None
        end_hetong = self.get_argument('end_hetong') or None
        date_chengli = self.get_argument('date_chengli') or None
        date_zhizhao = self.get_argument('date_zhizhao') or None
        date_address = self.get_argument('date_address') or None
        kf_name = self.get_argument('kf_name')
        sale_name = self.get_argument('sale_name')
        zhuanshang = self.get_argument('zhuanshang')
        kuaiji = self.get_argument('kuaiji')
        address_gongying = self.get_argument('address_gongying')
        if start_hetong != None:
            start_hetong = re.sub('/', '-', start_hetong, 2)
        if end_hetong != None:
            end_hetong = re.sub('/', '-', end_hetong, 2)
        if date_chengli != None:
            date_chengli = re.sub('/', '-', date_chengli, 2)
        if date_zhizhao != None:
            date_zhizhao = re.sub('/', '-', date_zhizhao, 2)
        if date_address != None:
            date_address = re.sub('/', '-', date_address, 2)
        db.execute(
            'insert into t_customer('
            'customer_id,company,linkman,phone,yewu_content,address_style,start_hetong,'
            'end_hetong,date_chengli,date_zhizhao,date_address,kf_name,sale_name,'
            'zhuanshang,kuaiji,address_gongying) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',
            customer_id, company, linkman, phone, yewu_content, address_style,
            start_hetong, end_hetong, date_chengli, date_zhizhao, date_address,
            kf_name, sale_name, zhuanshang, kuaiji, address_gongying)
        self.redirect('/customer')


class ChangeCustomerHandler(BaseHandler):
    @tornado.web.authenticated
    def get(self, id):
        db = self.application.db
        customers = db.query('select * from t_customer where id=%s',
                             int(id))
        customer = customers[0]
        self.render('insertcustomer.html', customer=customer)

    @tornado.web.authenticated
    def post(self, id):
        cusform = CustomerForm()
        cus = cusform.check_valid(self)
        if not cus:
            self.redirect('/insert_customer')
        db = self.application.db
        customer = db.query('select * from t_customer where id=%s',
                            int(id))
        customer = customer[0]
        customer_id = self.get_argument('customer_id')
        if int(customer_id) != customer.customer_id:
            customers = db.query(
                'select * from t_customer where customer_id=%s',
                int(customer_id))
            if len(customers) != 0:
                self.render(
                    'insertcustomer.html',
                    customer=customer,
                    error_id=customer_id)
            company = self.get_argument('company')
            linkman = self.get_argument('linkman')
            phone = self.get_argument('phone')
            yewu_content = self.get_argument('yewu_content')
            address_style = self.get_argument('address_style')
            start_hetong = self.get_argument('start_hetong') or None
            end_hetong = self.get_argument('end_hetong') or None
            date_chengli = self.get_argument('date_chengli') or None
            date_zhizhao = self.get_argument('date_zhizhao') or None
            date_address = self.get_argument('date_address') or None
            kf_name = self.get_argument('kf_name')
            sale_name = self.get_argument('sale_name')
            zhuanshang = self.get_argument('zhuanshang')
            kuaiji = self.get_argument('kuaiji')
            address_gongying = self.get_argument('address_gongying')
            if start_hetong != None:
                start_hetong = re.sub('/', '-', start_hetong, 2)
            if end_hetong != None:
                end_hetong = re.sub('/', '-', end_hetong, 2)
            if date_chengli != None:
                date_chengli = re.sub('/', '-', date_chengli, 2)
            if date_zhizhao != None:
                date_zhizhao = re.sub('/', '-', date_zhizhao, 2)
            if date_address != None:
                date_address = re.sub('/', '-', date_address, 2)
            db.execute(
                'update  t_customer set customer_id=%s,company=%s,'
                'linkman=%s,phone=%s,yewu_content=%s,address_style=%s,start_hetong=%s,'
                'end_hetong=%s,date_chengli=%s,date_zhizhao=%s,date_address=%s,kf_name=%s,sale_name=%s,'
                'zhuanshang=%s,kuaiji=%s,address_gongying=%s where id=%s',
                int(customer_id), company, linkman, phone, yewu_content,
                address_style, start_hetong, end_hetong, date_chengli,
                date_zhizhao, date_address, kf_name, sale_name, zhuanshang,
                kuaiji, address_gongying, int(id))
            self.redirect('/customer')
        else:
            company = self.get_argument('company')
            linkman = self.get_argument('linkman')
            phone = self.get_argument('phone')
            yewu_content = self.get_argument('yewu_content')
            address_style = self.get_argument('address_style')
            start_hetong = self.get_argument('start_hetong') or None
            end_hetong = self.get_argument('end_hetong') or None
            date_chengli = self.get_argument('date_chengli') or None
            date_zhizhao = self.get_argument('date_zhizhao') or None
            date_address = self.get_argument('date_address') or None
            kf_name = self.get_argument('kf_name')
            sale_name = self.get_argument('sale_name')
            zhuanshang = self.get_argument('zhuanshang')
            kuaiji = self.get_argument('kuaiji')
            address_gongying = self.get_argument('address_gongying')
            if start_hetong != None:
                start_hetong = re.sub('/', '-', start_hetong, 2)
            if end_hetong != None:
                end_hetong = re.sub('/', '-', end_hetong, 2)
            if date_chengli != None:
                date_chengli = re.sub('/', '-', date_chengli, 2)
            if date_zhizhao != None:
                date_zhizhao = re.sub('/', '-', date_zhizhao, 2)
            if date_address != None:
                date_address = re.sub('/', '-', date_address, 2)
            db.execute(
                'update  t_customer set customer_id=%s,company=%s,'
                'linkman=%s,phone=%s,yewu_content=%s,address_style=%s,start_hetong=%s,'
                'end_hetong=%s,date_chengli=%s,date_zhizhao=%s,date_address=%s,kf_name=%s,sale_name=%s,'
                'zhuanshang=%s,kuaiji=%s,address_gongying=%s where id=%s',
                int(customer_id), company, linkman, phone, yewu_content,
                address_style, start_hetong, end_hetong, date_chengli,
                date_zhizhao, date_address, kf_name, sale_name, zhuanshang,
                kuaiji, address_gongying, int(id))
            self.redirect('/customer')


class CustomerdetailHandlder(BaseHandler):
    @tornado.web.authenticated
    def get(self, id):
        dt = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        logger.info("%s : %s  - %s " % (dt, uid_name, self.request.uri))
        db = self.application.db
        customer = db.query('select * from t_customer where id=%s',
                            int(id))
        customer = customer[0]
        self.render('customer_detail.html', customer=customer)


class CustomerdeleteHandler(BaseHandler):
    @tornado.web.authenticated
    def get(self, id):
        dt = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        logger.info("%s : %s  - %s " % (dt, uid_name, self.request.uri))

        db = self.application.db
        db.execute('delete from t_customer where id=%s', int(id))



class SearchDateHandler(BaseHandler):
    @tornado.web.authenticated
    def get(self):
        dt = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        logger.info("%s : %s  - %s " % (dt, uid_name, self.request.uri))
        db = self.application.db
        timedate = self.get_argument('select_date')
        start_time = self.get_argument('start_time')
        end_time = self.get_argument('end_time')
        time_list = [timedate, start_time, end_time]
        start_time = re.sub('/', '-', start_time, 2)
        end_time = re.sub('/', '-', end_time, 2)
        customers = db.query(
            'select * from t_customer where ' + timedate + ' >=' + '"' +
            start_time + '" and ' + timedate + ' <=' + '"' + end_time + '"')
        # customers=db.query('select * from customer_manage where %s >="%s" and %s <="%s"',timedate,start_time,timedate,end_time)
        self.render(
            'admin/customer.html', customers=customers, time_list=time_list)
