# -*- coding: utf-8 -*-
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
import events
reload(sys)
sys.setdefaultencoding('utf8')

class Account_receiveHandler(BaseHandler):

    @tornado.web.authenticated
    def get(self):
        tag = self.get_argument("tag","")
        uid = self.get_secure_cookie("uid")
        role = self.get_secure_cookie("role")
        all_manage=self.get_secure_cookie('all_manage')
        uid_name = self.get_secure_cookie("name")
        page=int(self.get_argument('page',1))
        pre_page=20

        if tag=="account_receive":
            s_id=self.get_argument('s_id','')
            s_company=self.get_argument('s_company','')
            s_kf_kuaiji=self.get_argument('s_kf_kuaiji','')
            s_sale_guwen=self.get_argument('s_sale_guwen','')
            s_kf_guwen=self.get_argument('s_kf_guwen','')
            s_jiesuan_cycle=self.get_argument('s_jiesuan_cycle','')
            s_chengli_start=self.get_argument('s_chengli_start','')
            s_chengli_end=self.get_argument('s_chengli_end','')
            s_account_charge_end_start=self.get_argument('s_account_charge_end_start','')
            s_account_charge_end_end=self.get_argument('s_account_charge_end_end','')
            s_zhangce_charge_end_start=self.get_argument('s_zhangce_charge_end_start','')
            s_zhangce_charge_end_end=self.get_argument('s_zhangce_charge_end_end','')
            s_new_yishou_detail=self.get_argument('s_new_yishou_detail','')
            s_yingshou_detail=self.get_argument('s_yingshou_detail','')
            s_last_updated_msg=self.get_argument('s_last_updated_msg','')
            sql=''
            if s_id:
                sql=' where a.id=%s '%s_id
            else:
                if s_company:
                    sql+=' and a.company like "%%'+s_company+'%%" '
                if s_kf_kuaiji:
                    sql+=' and a.kf_kuaiji="%s" '%s_kf_kuaiji
                if s_sale_guwen:
                    sql+=' and a.sale_guwen="%s" '%s_sale_guwen
                if s_kf_guwen:
                    sql+=' and a.kf_guwen="%s" '%s_kf_guwen
                if s_jiesuan_cycle:
                    sql+=' and a.kf_guwen="%s" '%s_kf_guwen
                if s_jiesuan_cycle:
                    sql+=' and a.jiesuan_cycle="%s" '%s_jiesuan_cycle
                if s_chengli_start and s_chengli_end:
                    sql+=' and a.chengli_date between "%s" and "%s" '%(s_chengli_start,s_chengli_end)
                if s_account_charge_end_start and s_account_charge_end_end:
                    sql+=' and a.account_charge_end_date between "%s" and "%s" '%(s_account_charge_end_start,s_account_charge_end_end)
                if s_zhangce_charge_end_start and s_zhangce_charge_end_end:
                    sql+=' and  a.zhangce_charge_end_date between "%s" and "%s" '%(s_zhangce_charge_end_start,s_zhangce_charge_end_end)
                if s_new_yishou_detail:
                    sql+=' and  a.new_yishou_detail like "%%'+s_new_yishou_detail+'%%" '
                if s_yingshou_detail:
                    sql+=' and a.yingshou_detail like "%%'+s_yingshou_detail+'%%"'
                if s_last_updated_msg:
                    sql+=' and a.last_updated_msg like "%%'+s_last_updated_msg+'%%" '
                if sql:
                    sql=' where '+sql[4:]
            params={
                's_id':s_id,
                's_company':s_company,
                's_kf_kuaiji':s_kf_kuaiji,
                's_sale_guwen':s_sale_guwen,
                's_kf_guwen':s_kf_guwen,
                's_jiesuan_cycle':s_jiesuan_cycle,
                's_chengli_start':s_chengli_start,
                's_chengli_end':s_chengli_end,
                's_account_charge_end_start':s_account_charge_end_start,
                's_account_charge_end_end':s_account_charge_end_end,
                's_zhangce_charge_end_start':s_zhangce_charge_end_start,
                's_zhangce_charge_end_end':s_zhangce_charge_end_end,
                's_new_yishou_detail':s_new_yishou_detail,
                's_yingshou_detail':s_yingshou_detail,
                's_last_updated_msg':s_last_updated_msg
            } 
            count=self.db.get(''' select count(*) count from t_account_receive a
                inner join t_account_receive_record b on a.id=b.account_id 
                 and b.id=(select max(c.id) from t_account_receive_record c where b.account_id=c.account_id )'''+sql)
            
            pagination=Pagination(page,pre_page,count.count,self.request)  
            start_page=(page-1)*pre_page
            account_receive=self.db.query('''
                select a.*,b.jiesuan_cycle new_jiesuan_cycle,b.year_charge new_year_charge,
                b.month_charge new_month_charge,b.zhangce_charge new_zhangce_charge,b.account_charge_end_date
                 new_account_charge_end_date,b.zhangce_charge_end_date new_zhangce_charge_end_date,b.new_yishou_detail
                  new_new_yishou_detail,b.yingshou_detail new_yingshou_detail
                 from t_account_receive a
                 inner join t_account_receive_record b on a.id=b.account_id 
                  and b.id=(select max(c.id) from t_account_receive_record c where b.account_id=c.account_id )'''+sql+'''
                 order by a.created_at desc limit %s,%s
            ''',start_page,pre_page)
            self.render(
                'account_receive/account_receive_list.html',
                account_receive=account_receive,
                tag=tag,
                pagination=pagination,
                params=params,
                search_key=""
            )
        elif tag=="show":
            id=self.get_argument('id')
            guid=self.get_argument('guid')
            account_receive=self.db.get('''
                select * from t_account_receive where id=%s and guid=%s
            ''',id,guid)
            if not account_receive:
                self.write('项目不存在'+id+guid)
            else:
                account_receive_record=self.db.query('''
                    select * from t_account_receive_record where  account_id=%s order by created_at desc
                ''',id)
                account_receive_msg=self.db.query('''
                    select * from t_account_receive_msg where account_id=%s order by created_at desc
                ''',id)
                self.render(
                    'account_receive/account_receive_show.html',
                    search_key="",
                    account_receive=account_receive,
                    account_receive_record=account_receive_record,
                    account_receive_msg=account_receive_msg
                    )

    @tornado.web.authenticated
    def post(self):
        tag = self.get_argument("tag","")
        uid = self.get_secure_cookie("uid")
        role = self.get_secure_cookie("role")
        all_manage=self.get_secure_cookie('all_manage')
        uid_name = self.get_secure_cookie("name")
        dt = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        guid=uuid.uuid4()

        if tag=="account_receive":
            company=self.get_argument('company','')
            kf_kuaiji=self.get_argument('kf_kuaiji','')
            sale_guwen=self.get_argument('sale_guwen','')
            kf_guwen=self.get_argument('kf_guwen','')
            jiesuan_cycle=self.get_argument('jiesuan_cycle','')
            year_charge=self.get_argument('year_charge','') or int(0)
            month_charge=self.get_argument('month_charge','') or int(0)
            zhangce_charge=self.get_argument('zhangce_charge','') or int(0)
            chengli_date=self.get_argument('chengli_date','')
            account_charge_end_date=self.get_argument('account_charge_end_date','')
            zhangce_charge_end_date=self.get_argument('zhangce_charge_end_date','')
            new_yishou_detail=self.get_argument('new_yishou_detail','')
            yingshou_detail=self.get_argument('yingshou_detail','')
            account_id=self.get_argument('account_id','')
            account_guid=self.get_argument('account_guid','')
            delete_id=self.get_argument('delete_id','')
            delete_guid=self.get_argument('delete_guid','')
            is_loupan=self.get_argument('is_loupan')
            register_addr_type=self.get_argument('register_addr_type','')
            kp_addr_date_start=self.get_argument('kp_addr_date_start','')
            kp_addr_date_end=self.get_argument('kp_addr_date_end','')
            if not account_charge_end_date:
                account_charge_end_date=None
            if not zhangce_charge_end_date:
                zhangce_charge_end_date=None
            if not kp_addr_date_start:
                kp_addr_date_start=None
            if not kp_addr_date_end:
                kp_addr_date_end=None
            if account_id:
                self.db.execute('''
                    update t_account_receive set company=%s,kf_kuaiji=%s,sale_guwen=%s,
                    kf_guwen=%s,chengli_date=%s,is_loupan=%s,register_addr_type=%s,
                    kp_addr_date_start=%s,kp_addr_date_end=%s,jiesuan_cycle=%s,year_charge=%s,month_charge=%s,zhangce_charge=%s where id=%s and guid=%s
                ''',company,kf_kuaiji,sale_guwen,kf_guwen,chengli_date,is_loupan,register_addr_type,kp_addr_date_start,
                kp_addr_date_end,jiesuan_cycle,year_charge,month_charge,zhangce_charge,account_id,account_guid)
            
            elif delete_id:
                self.db.execute('''
                    delete a.*,b.*,c.* from t_account_receive a 
                    left join t_account_receive_record b on a.id=b.account_id 
                    left join t_account_receive_msg c on a.id=c.account_id
                    where a.id=%s and a.guid=%s
                ''',delete_id,delete_guid)
            else:
                result=self.db.execute('''
                    insert into t_account_receive
                    (company,kf_kuaiji,sale_guwen,kf_guwen,jiesuan_cycle,year_charge,
                    month_charge,zhangce_charge,chengli_date,account_charge_end_date,zhangce_charge_end_date,
                    new_yishou_detail,yingshou_detail,created_at,guid,uid_name,uid,is_loupan,register_addr_type,kp_addr_date_start,kp_addr_date_end)
                    values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
                    ''',company,kf_kuaiji,sale_guwen,kf_guwen,jiesuan_cycle,year_charge,month_charge,zhangce_charge,chengli_date,
                    account_charge_end_date,zhangce_charge_end_date,'',yingshou_detail,dt,guid,uid_name,uid,is_loupan,
                    register_addr_type,kp_addr_date_start,kp_addr_date_end)
                self.db.execute('''
                    insert into t_account_receive_record
                    (jiesuan_cycle,year_charge,month_charge,zhangce_charge,account_charge_end_date,
                    zhangce_charge_end_date,new_yishou_detail,yingshou_detail,created_at,account_id,uid_name,uid)
                    values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
                ''',jiesuan_cycle,year_charge,month_charge,zhangce_charge,account_charge_end_date,
                zhangce_charge_end_date,new_yishou_detail,yingshou_detail,dt,result,uid_name,uid)
        
        elif tag=="account_receive_record":
            jiesuan_cycle=self.get_argument('jiesuan_cycle')
            year_charge=self.get_argument('year_charge') or int(0)
            month_charge=self.get_argument('month_charge') or int(0)
            zhangce_charge=self.get_argument('zhangce_charge') or int(0)
            account_charge_end_date=self.get_argument('account_charge_end_date')
            zhangce_charge_end_date=self.get_argument('zhangce_charge_end_date')
            new_yishou_detail=self.get_argument('new_yishou_detail')
            yingshou_detail=self.get_argument('yingshou_detail')
            account_id=self.get_argument('account_id')
            account_guid=self.get_argument('account_guid','')
            id=self.get_argument('id','')
            if not account_charge_end_date:
                account_charge_end_date=None
            if not zhangce_charge_end_date:
                zhangce_charge_end_date=None
            if id:
                self.db.execute('''
                    update t_account_receive_record set jiesuan_cycle=%s,year_charge=%s,month_charge=%s,
                    zhangce_charge=%s,account_charge_end_date=%s,zhangce_charge_end_date=%s,new_yishou_detail=%s,
                    yingshou_detail=%s,updated_at=%s,uid_name=%s,uid=%s where id=%s
                ''',jiesuan_cycle,year_charge,month_charge,zhangce_charge,account_charge_end_date,zhangce_charge_end_date,new_yishou_detail,
                yingshou_detail,dt,uid_name,uid,id)
                # max_record=self.db.get(' select id from t_account_receive_record where account_id=%s order by id desc limit 1',account_id)
                # if max_record.id==int(id):
                #     self.db.execute('''
                #     update t_account_receive set jiesuan_cycle=%s,year_charge=%s,
                #     month_charge=%s,zhangce_charge=%s,account_charge_end_date=%s,zhangce_charge_end_date=%s,new_yishou_detail=%s,
                #     yingshou_detail=%s where id =%s and guid=%s
                # ''',jiesuan_cycle,year_charge,month_charge,zhangce_charge,account_charge_end_date,
                #     zhangce_charge_end_date,new_yishou_detail,yingshou_detail,account_id,account_guid)
            else:
                self.db.execute('''
                    insert into t_account_receive_record(jiesuan_cycle,year_charge,
                    month_charge,zhangce_charge,account_charge_end_date,zhangce_charge_end_date,new_yishou_detail,
                    yingshou_detail,account_id,created_at,uid_name,uid) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
                ''',jiesuan_cycle,year_charge,month_charge,zhangce_charge,account_charge_end_date,
                    zhangce_charge_end_date,new_yishou_detail,yingshou_detail,account_id,dt,uid_name,uid)
            
                # self.db.execute('''
                #     update t_account_receive set jiesuan_cycle=%s,year_charge=%s,
                #     month_charge=%s,zhangce_charge=%s,account_charge_end_date=%s,zhangce_charge_end_date=%s,new_yishou_detail=%s,
                #     yingshou_detail=%s where id =%s and guid=%s
                # ''',jiesuan_cycle,year_charge,month_charge,zhangce_charge,account_charge_end_date,
                #     zhangce_charge_end_date,new_yishou_detail,yingshou_detail,account_id,account_guid)
            
        
        elif tag=="account_receive_msg":
            msg=self.get_argument('msg')
            account_id=self.get_argument('account_id')
            account_guid=self.get_argument('account_guid')
            self.db.execute('''
                insert into t_account_receive_msg(account_id,msg,created_at,uid_name,uid)
                values(%s,%s,%s,%s,%s)''',account_id,msg,dt,uid_name,uid)
            self.db.execute('''
                update t_account_receive set last_updated=%s,last_updated_msg=%s where id =%s and guid=%s
            ''',dt,msg,account_id,account_guid)