# encoding=utf8
from handlers.base import BaseHandler
import logging
import json
import tornado.web
import urllib2
import tornado.httpclient
import sys, re
import urllib
reload(sys)
sys.setdefaultencoding('utf8')

logger = logging.getLogger('boilerplate.' + __name__)

# 出库
class OutHandler(BaseHandler):
    @tornado.web.authenticated
    def get(self):
        db = self.application.db
        outs = db.query('select * from t_out_warehouse')
        self.render('out.html', outs=outs)


class InsertOutHandler(BaseHandler):
    @tornado.web.authenticated
    def get(self):
        self.render('insertout.html')

    @tornado.web.authenticated
    def post(self):
        db = self.application.db
        serial_num = self.get_argument('serial_num')
        num = self.get_argument('num')
        rev_time = self.get_argument('rev_time') or None
        dis_time = self.get_argument('dis_time') or None
        saleman = self.get_argument('saleman')
        telemark = self.get_argument('telemark')
        group_leader = self.get_argument('group_leader')
        gen_dan = self.get_argument('gen_dan')
        source_bus = self.get_argument('source_bus')
        customer_name = self.get_argument('customer_name')
        company_name = self.get_argument('company_name')
        regist_id = self.get_argument('regist_id')
        bus_content = self.get_argument('bus_content')
        company_type = self.get_argument('company_type')
        legal_person = self.get_argument('legal_person')
        supervisor = self.get_argument('supervisor')
        share_holder = self.get_argument('share_holder')
        regist_money = self.get_argument('regist_money')
        address_type = self.get_argument('address_type')
        progress = self.get_argument('progress')
        tally = self.get_argument('tally')
        server_money = self.get_argument('server_money')
        rec_money = self.get_argument('rec_money')
        contract_confirm = self.get_argument('contract_confirm')
        baijie_time = self.get_argument('baijie_time') or None
        remarks = self.get_argument('remarks')
        move_time = self.get_argument('move_time') or None
        zhizhao_detail = self.get_argument('zhizhao_detail')
        accept_man = self.get_argument('accept_man')
        other_remarks = self.get_argument('other_remarks')
        out_time = self.get_argument('out_time') or None
        date_kaipiao = self.get_argument('date_kaipiao') or None
        phone = self.get_argument('phone')
        retainage = self.get_argument('retainage')
        banjie_cycle = self.get_argument('banjie_cycle')

        if rev_time != None:
            rev_time = re.sub('/', '-', rev_time, 2)
        if dis_time != None:
            dis_time = re.sub('/', '-', dis_time, 2)
        if baijie_time != None:
            baijie_time = re.sub('/', '-', baijie_time, 2)
        if move_time != None:
            move_time = re.sub('/', '-', move_time, 2)
        if out_time != None:
            out_time = re.sub('/', '-', out_time, 2)
        if date_kaipiao != None:
            date_kaipiao = re.sub('/', '-', date_kaipiao, 2)

        db.execute(
            'insert into t_out_warehouse(serial_num,num,rev_time,dis_time,saleman,'
            'telemark,group_leader,gen_dan,source_bus,customer_name,company_name,regist_id,bus_content,company_type,'
            'legal_person,supervisor,share_holder,regist_money,address_type,progress,tally,server_money,rec_money,'
            'contract_confirm,baijie_time,remarks,move_time,zhizhao_detail,accept_man,other_remarks,out_time,date_kaipiao,'
            'phone,retainage,banjie_cycle) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,'
            '%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)', serial_num, num,
            rev_time, dis_time, saleman, telemark, group_leader, gen_dan,
            source_bus, customer_name, company_name, regist_id, bus_content,
            company_type, legal_person, supervisor, share_holder, regist_money,
            address_type, progress, tally, server_money, rec_money,
            contract_confirm, baijie_time, remarks, move_time, zhizhao_detail,
            accept_man, other_remarks, out_time, date_kaipiao, phone,
            retainage, banjie_cycle)
        self.redirect('/out')


class OutChangeHandler(BaseHandler):
    @tornado.web.authenticated
    def get(self, id):
        db = self.application.db
        outs = db.query('select * from t_out_warehouse where id=%s', int(id))
        out = outs[0]
        self.render('insertout.html', out=out)

    @tornado.web.authenticated
    def post(self, id):
        db = self.application.db
        serial_num = self.get_argument('serial_num')
        num = self.get_argument('num')
        rev_time = self.get_argument('rev_time') or None
        dis_time = self.get_argument('dis_time') or None
        saleman = self.get_argument('saleman')
        telemark = self.get_argument('telemark')
        group_leader = self.get_argument('group_leader')
        gen_dan = self.get_argument('gen_dan')
        source_bus = self.get_argument('source_bus')
        customer_name = self.get_argument('customer_name')
        company_name = self.get_argument('company_name')
        regist_id = self.get_argument('regist_id')
        bus_content = self.get_argument('bus_content')
        company_type = self.get_argument('company_type')
        legal_person = self.get_argument('legal_person')
        supervisor = self.get_argument('supervisor')
        share_holder = self.get_argument('share_holder')
        regist_money = self.get_argument('regist_money')
        address_type = self.get_argument('address_type')
        progress = self.get_argument('progress')
        tally = self.get_argument('tally')
        server_money = self.get_argument('server_money')
        rec_money = self.get_argument('rec_money')
        contract_confirm = self.get_argument('contract_confirm')
        baijie_time = self.get_argument('baijie_time') or None
        remarks = self.get_argument('remarks')
        move_time = self.get_argument('move_time') or None
        zhizhao_detail = self.get_argument('zhizhao_detail')
        accept_man = self.get_argument('accept_man')
        other_remarks = self.get_argument('other_remarks')
        out_time = self.get_argument('out_time') or None
        date_kaipiao = self.get_argument('date_kaipiao') or None
        phone = self.get_argument('phone')
        retainage = self.get_argument('retainage')
        banjie_cycle = self.get_argument('banjie_cycle')

        if rev_time != None:
            rev_time = re.sub('/', '-', rev_time, 2)
        if dis_time != None:
            dis_time = re.sub('/', '-', dis_time, 2)
        if baijie_time != None:
            baijie_time = re.sub('/', '-', baijie_time, 2)
        if move_time != None:
            move_time = re.sub('/', '-', move_time, 2)
        if out_time != None:
            out_time = re.sub('/', '-', out_time, 2)
        if date_kaipiao != None:
            date_kaipiao = re.sub('/', '-', date_kaipiao, 2)

        db.execute(
            'update t_out_warehouse set serial_num=%s,num=%s,rev_time=%s,dis_time=%s,saleman=%s,telemark=%s,'
            'group_leader=%s,gen_dan=%s,source_bus=%s,customer_name=%s,company_name=%s,regist_id=%s,bus_content=%s,company_type=%s,'
            'legal_person=%s,supervisor=%s,share_holder=%s,regist_money=%s,address_type=%s,progress=%s,tally=%s,server_money=%s,'
            'rec_money=%s,contract_confirm=%s,baijie_time=%s,remarks=%s,move_time=%s,zhizhao_detail=%s,accept_man=%s,other_remarks=%s,'
            'out_time=%s,date_kaipiao=%s,phone=%s,retainage=%s,banjie_cycle=%s where id=%s',
            serial_num, num, rev_time, dis_time, saleman, telemark,
            group_leader, gen_dan, source_bus, customer_name, company_name,
            regist_id, bus_content, company_type, legal_person, supervisor,
            share_holder, regist_money, address_type, progress, tally,
            server_money, rec_money, contract_confirm, baijie_time, remarks,
            move_time, zhizhao_detail, accept_man, other_remarks, out_time,
            date_kaipiao, phone, retainage, banjie_cycle, int(id))
        self.redirect('/out')


class OutDetailHandler(BaseHandler):
    @tornado.web.authenticated
    def get(self, id):
        db = self.application.db
        outs = db.query('select * from t_out_warehouse where id=%s', int(id))
        out = outs[0]
        self.render('show_table2.html', out=out)


class OutDeleteHandler(BaseHandler):
    @tornado.web.authenticated
    def get(self, id):
        db = self.application.db
        db.execute('delete from t_out_warehouse where id=%s', int(id))


# 表单验证
class MainForm(object):
    def __init__(self):
        self.cus_id = r"^\d+$"
        self.craeted_at = r"^(\d{4}-\d{1,2}-\d{1,2}\s\d{1,2}:\d{1,2}:\d{1,2})$"
        self.all_income = r"^\d*\.*\d*$"

    def check_valid(self, request):
        flag = True
        form_dict = self.__dict__
        # allerror_message={'serice':'不能为空','company':'不能为空',
        #                 'money':'不能为空','receipt_account':'不能为空',
        #                 'cashier':'不能为空','sales_consultant':'不能为空',
        #                 'service_consultant':'不能为空'}
        error_message = {}
        for key, regular in form_dict.items():
            post_value = request.get_argument(key)
            ret = re.match(regular, post_value)
            if not ret:
                # error_message[key]=allerror_message[key]
                flag = False
        return flag


