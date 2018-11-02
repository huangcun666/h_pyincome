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
import qrcode
import concurrent.futures
reload(sys)
sys.setdefaultencoding('utf8')
from Pagination import Pagination
logger = logging.getLogger('boilerplate.' + __name__)
executor = concurrent.futures.ThreadPoolExecutor(20)

#客户
class CustomerHandler(BaseHandler):
    _thread_pool = executor
    @tornado.web.authenticated
    @tornado.web.asynchronous
    @tornado.gen.engine
    def get(self):
        tag = self.get_argument("tag","all")
        uid = self.get_secure_cookie("uid")
        uid_name = self.get_secure_cookie("name")
        role=self.get_secure_cookie('role')
        is_manager=self.get_secure_cookie("is_manager")
        from_tag = self.get_argument("from_tag","")
        dt = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        logger.info("%s : %s  - %s " % (dt, uid_name, self.request.uri))


        if tag == "list":
            sql=""
            qtype = self.get_argument("qtype","")
            keyword = self.get_argument("keyword","")
            jz = self.get_argument("jz","")
            lp = self.get_argument("lp", "")
            if keyword:
                sql = " and (company like '%%" + keyword + "%%') or (company like '%%" + keyword + "%%')"
            if jz:
                sql =  sql+ " and (customer_type_name like '%%" + jz + "%%')"
            if lp:
                sql = sql + " and (customer_type_name like '%%" + lp + "%%')"
            page = int(self.get_argument("page", 1))
            pre_page = 20
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
                customers=customers,
                pagination=pagination,
                tag=tag,
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

        elif tag == "all":
            sql = ""
            keyword = self.get_argument("keyword", "")
            qtype = self.get_argument("qtype","")

            jz = self.get_argument("jz", "")
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
                    count = self.db_customer.get( '''SELECT count(*) count FROM t_customer where is_close=0''' + sql)
                    pagination = Pagination(page, pre_page, count.count, self.request)
                    startpage = (page - 1) * pre_page

                    customers = self.db_customer.query('''select * from t_customer  where is_close=0 ''' + sql + '''
                    order by created_at desc limit %s,%s''', startpage, pre_page)

                elif my:
                    count = self.db_customer.get( '''SELECT count(*) count FROM t_customer where is_close=0''' + sql)
                    pagination = Pagination(page, pre_page, count.count, self.request)
                    startpage = (page - 1) * pre_page

                    customers = self.db_customer.query('''select * from t_customer  where is_close=0 ''' + sql + '''
                    order by created_at desc limit %s,%s''', startpage, pre_page)



        #  customers = self.db_customer.query(query_str, startpage, pre_page)
            self.render(
                'c/customer/customer_list.html',
                customers=customers,
                pagination=pagination,
                tag=tag,
                keyword=keyword,
                lp=lp,
                jz=jz,
                my=my,
                kj=kj,
                t_user=t_user,
                qtype=qtype)

        # elif tag == "search":
        #     keyword = self.get_argument("keyword","")
        #     if keyword:
        #         sql = " and (tel like '%%" + keyword + "%%') or (company like '%%" + keyword + "%%') or (company like '%%" + keyword + "%%')or (company like '%%" + keyword + "%%')"

        #     page= int(self.get_argument("page",1))
        #     pre_page = 20
        #     count = self.db_customer.get(
        #         '''SELECT count(*) count FROM t_customer
        #        ''')
        #     pagination = Pagination(page, pre_page, count.count, self.request)
        #     startpage = (page - 1) * pre_page
        #     customers = self.db_customer.query('''
        #        select * from t_customer
        #         order by created_at desc limit %s,%s
        #         ''', startpage, pre_page)

        #     self.render(
        #         'c/customer/customer_search.html',
        #         customers=customers,
        #         pagination=pagination,
        #         tag=tag,
        #         keyword=keyword)
        elif tag=="add":
            company_id = self.get_argument("company_id","")
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
            if company_id:
                t_project = self.db.get("select * from t_projects where id=%s",company_id)
            t_user = self.db.query("select * from t_user where role=10 ")
            t_promo_types = self.db.query(
                """select * from t_projects_type where income_category='套餐' order by order_int  """
            )
            self.render(
                'c/customer/customer_add.html',
                t_city=t_city,
                t_payment_type=t_payment_type,
                company_id=company_id,
                t_zone = t_zone,
                t_promo_types=t_promo_types,
                t_project=t_project,
                t_credit_type=t_credit_type,
                t_customer_type=t_customer_type,
                t_customer_rating=t_customer_rating,
                t_user=t_user,tag=tag)

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
            pre_page = 20
            count = 0
            if keyword:
                sql = " and (customer_company like '%%" + keyword + "%%') or (customer_company like '%%" + keyword + "%%')"
            if qtype=='comfirm_id':
                count=self.db_customer.get(
                    """select count(*) count from """+options.mysql_database+""".t_projects  where (customer_company <> "")
                and (customer_company <> "无")  and (customer_company IS NOT NULL)
                    and customer_company not in (select company from t_customer ) and id=%s order by created_at desc""",int(keyword)
                )
                pagination=Pagination(page,pre_page,count.count,self.request)
                startpage = (page - 1) * pre_page
                customers = self.db_customer.query(
                """select * from """+options.mysql_database+""".t_projects  where (customer_company <> "")
                and (customer_company <> "无")  and (customer_company IS NOT NULL)
                    and customer_company not in (select company from t_customer ) and id=%s order by created_at desc limit %s,%s""",
                    int(keyword),startpage,pre_page)
            elif qtype=='company':
                count = self.db_customer.get(
                """select count(*) count from """+options.mysql_database+""".t_projects  where (customer_company <> "")
                and (customer_company <> "无")  and (customer_company IS NOT NULL)
                    and customer_company not in (select company from t_customer )
                    """+sql+"""order by created_at desc""")
                pagination=Pagination(page,pre_page,count.count,self.request)
                startpage = (page - 1) * pre_page
                customers = self.db_customer.query(
                """select * from """+options.mysql_database+""".t_projects  where (customer_company <> "")
                and (customer_company <> "无")  and (customer_company IS NOT NULL)
                    and customer_company not in (select company from t_customer )
                    """+sql+"""order by created_at desc limit %s,%s""",startpage,pre_page)
            else:
                count = self.db_customer.get(
                """select count(*) count from """+options.mysql_database+""".t_projects  where (customer_company <> "")
                and (customer_company <> "无")  and (customer_company IS NOT NULL)
                    and customer_company not in (select company from t_customer ) order by created_at desc""" )
                pagination=Pagination(page,pre_page,count.count,self.request)
                startpage = (page - 1) * pre_page
                customers = self.db_customer.query(
                """select * from """+options.mysql_database+""".t_projects  where (customer_company <> "")
                and (customer_company <> "无")  and (customer_company IS NOT NULL)
                    and customer_company not in (select company from t_customer ) order by created_at desc limit %s,%s""",startpage,pre_page)
            self.render(
                'c/customer/customer_company.html',
                customers=customers,
                pagination=pagination,
                qtype=qtype,
                keyword=keyword,
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
            if not id:
                self.write("not id")
            elif not guid:
                self.write("not guid")
            else:
                t_customer = self.db_customer.get(
                    "select * from  t_customer where id=%s and guid=%s",
                    id, guid)
                if not t_customer:
                    self.write("not customer")
                else:
                    #  print "t_customer",t_customer.company


                    t_projects_query = self.db.query(
                        """
                            select *,ifnull(aa,0) income_money3 from  """ +
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



                            where b.customer_company='""" +
                        t_customer.company + """'
                     and c.project_id=b.id

                     order by b.created_at desc


                    """)
                    t_linkman = self.db_customer.query(
                        "select * from t_linkman where customer_id=%s order by id desc",
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
                        """, t_customer.id)
                    project_note_unread = self.db_customer.query("""
                        select * from t_projects_note a

                         where project_id=%s

                         and id not in(
								select note_id from t_projects_note_confirm where note_id=a.id and created_by=%s
                         )

                         order by creatd_at desc
                        """, t_customer.id,uid)

                    t_projects_note_check=self.db_customer.query(
                    """
                    select * from t_projects_note a where project_id=%s and is_check=1
                       and id not in(
								select note_id from t_projects_note_check where note_id=a.id
                         )
                         order by creatd_at desc
                    """,t_customer.id)
                    t_customer_exchange=self.db_customer.query(
                        """
                        select * from t_customer_exchange where customer_id=%s and etype=1 order by created_at desc
                        """,t_customer.id
                    )
                    express_type=self.db.query('''
                    select * from t_projects_type where income_category='快递类型' 
                ''')
                    payment_type=self.db.query('''
                    select * from t_projects_type where income_category='快递付费' 
                ''')
                    t_express=self.db.query('''
                select * from t_express where project_id=%s and guid=%s order by created_at desc''',t_customer.id,t_customer.guid)
                    t_projects_type=self.db.query(
                    """
                    select * from t_projects_type where income_category='移交资料' and jiaojie_order>0 order by order_int
                    """
                )
                
                    t_cutomer_addr_msg=self.db.query('''
                    select * from t_customer_addr_msg where company=%s
                ''',t_customer.company)
                    self.render(
                        "c/customer/customer_show.html",
                        t_acc=t_acc,
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
                        to_tag=to_tag)


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
            customer_id=self.get_argument('customer_id')
            t_customer_exchange = self.db_customer.query(
                """select * from t_customer_exchange where customer_id=%s and etype=2 order by created_at desc limit 5""",
                customer_id)
            self.render('c/customer/show_customer_exchange.html',
            t_customer_exchange=t_customer_exchange,
            customer_id=customer_id)

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
        dt = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
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
            print(pay_type_id)
            if not addr_expire:
                addr_expire = None
            if not reg_date:
                reg_date = None
            if not end_date:
                end_date = None
            acc_uid = 0

            if acc_uid_name:
                acc_user = self.db.get("select id from t_user where name=%s",acc_uid_name)
                print "acc_user",acc_user
                if not acc_user:
                    return self.write("会计 %s 不存在"%(acc_uid_name))
                else:
                    acc_uid = acc_user.id




            promo_id =0,
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
                                `land_tax`=%s,uid=%s,uid_name=%s,acc_uid_at=%s,promo_id=%s,promo_id_name=%s,
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
                            service_amount_month,service_amount,book_amount,paytype_id,paytype_id_name,fee,project_id,paytype_status_id,paytype_status_id_name)
                            VALUES
                            (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,
                            %s,%s,%s,%s,%s,%s,%s,0,0);

                    """,zone,city, company_reguid, industry_name, is_general, credit_rating,
                        credit_rating_name, customer_rating, customer_rating_name,
                        customer_type, customer_type_name, company, reg_addr,
                        reg_tel, reg_number, reg_person, reg_bank,
                        reg_bank_account, addr_type, addr_expire, addr_cp, acc_uid,
                        acc_uid_name,dt,dt,var_uuid, remark, reg_date, end_date, saic,
                        national_tax, land_tax,uid,uid_name,dt,promo_id,promo_id_name,service_amount_month,service_amount,book_amount,pay_type_id,pay_typeid_name,fee,project_id)
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
            customer_id=self.get_argument('customer_id')
            msg_time=self.get_argument('msg_time','')
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
            self.db_customer.execute('''
                insert into  t_customer_exchange(msg_time,msg,customer_id,created_at,uid,uid_name,file_path,etype)
                values(%s,%s,%s,%s,%s,%s,%s,%s)''',msg_time, msg, customer_id,dt, uid,
                                     uid_name, file_path, etype)
            t_customer_exchange = self.db_customer.query(
                """select * from t_customer_exchange where customer_id=%s and etype=2 order by created_at desc limit 5""",
                customer_id)
            return self.render('c/customer/show_customer_exchange.html',
            t_customer_exchange=t_customer_exchange,
            customer_id=customer_id)
        
        elif tag=="confirm_msg_time":
            today_exchange_ids=self.get_argument('today_exchange_ids')
            for item in str(today_exchange_ids)[1:-1].split(','):
                self.db_customer.execute('''
                    update t_customer_exchange set confirm_msg_time=1 where id=%s
                ''',item[:-1])

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
