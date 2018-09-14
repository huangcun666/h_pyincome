# encoding=utf8
from handlers.base import BaseHandler
import logging
import json
import tornado.web
import urllib2
import tornado.httpclient
import sys,re
import urllib
reload(sys)
sys.setdefaultencoding('utf8')

logger = logging.getLogger('boilerplate.' + __name__)


class MainHandler(BaseHandler):
    @tornado.web.authenticated
    def get(self):
        db = self.application.db
        indents = db.query("select * from t_receipt order by cus_id asc")
        self.render('main.html', indents=indents)
        

# 收据
class DetailHandler(BaseHandler):
    def get(self,id):
        db=self.application.db
        customers=db.query("select * from t_receipt where id=%s",int(id))
        customer=customers[0]
        self.render('show_table.html',customer=customer)




class NewInsertHandler(BaseHandler):
    @tornado.web.authenticated
    def get(self):
        self.render('insert.html')

class InsertHandler(BaseHandler):
    @tornado.web.authenticated
    def get(self):
        try:
            id=self.get_argument('insert')
            client=tornado.httpclient.HTTPClient()
            response=client.fetch("http://192.168.2.168:9000/capi?"+\
            urllib.urlencode({'tag':'project','id':id}))
            customer=json.loads(response.body)
            if customer['code']==0 and id!='':
                self.render('insert.html',err_id=id)
            self.render('insert.html',customer=customer['customer'])
        except:
            self.redirect('/newinsert')


    @tornado.web.authenticated
    def post(self):
        m=MainForm()
        if m.check_valid(self):
            db=self.application.db
            sale_name=self.get_argument('sale_name')
            craeted_at=self.get_argument('craeted_at')
            project_name=self.get_argument('project_name')
            all_income=self.get_argument('all_income') or None
            kf_name=self.get_argument('kf_name')
            customer_company=self.get_argument('customer_company')
            cus_id=self.get_argument('cus_id')
            customer_name=self.get_argument('customer_name')
            income_type=self.get_argument('income_type')
            income_name=self.get_argument('income_name')
            customers=db.query('select * from t_receipt where cus_id=%s',int(cus_id))
            if len(customers)!=0:
                self.render('insert.html',err_id2=cus_id)
            if all_income!=None:
                all_income=float(all_income)
            db.execute(
                "insert into t_receipt(sale_name,craeted_at,project_name,all_income,kf_name,customer_company,cus_id,"
                "customer_name,income_type,income_name)"
                "values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", sale_name, craeted_at,
                project_name, all_income, kf_name, customer_company, cus_id,
                customer_name, income_type, income_name)
            self.redirect('/')
        else:
            self.redirect('/newinsert')

class DeleteHandler(BaseHandler):
    @tornado.web.authenticated
    def get(self,id):
        db=self.application.db
        indents=db.query("select * from t_receipt where id=%s",int(id))
        indent=indents[0]
        if not indent:
            return None
        db.execute('delete from t_receipt where id=%s',int(id))

class ChangeHandler(BaseHandler):
    @tornado.web.authenticated
    def get(self,id):
        db=self.application.db
        indents=db.query("select * from t_receipt where id=%s",int(id))
        indent=indents[0]
        if not indent:
            return None
        self.render('change.html',indent=indent)

    @tornado.web.authenticated
    def post(self,id):
        m1=MainForm()
        db=self.application.db
        indents=db.query("select * from t_receipt where id=%s",int(id))
        indent=indents[0]
        if m1.check_valid(self)==False:
            self.render('change.html',indent=indent)

        cus_id=self.get_argument('cus_id')
        if int(cus_id)!=int(indent.cus_id):
            customers=db.query('select * from t_receipt where cus_id=%s',int(cus_id))
            if len(customers)!=0:
                self.render('change.html',indent=indent,error_id=customers[0].cus_id)
            else:
                sale_name=self.get_argument('sale_name')
                craeted_at=self.get_argument('craeted_at')
                project_name=self.get_argument('project_name')
                all_income=self.get_argument('all_income') or None
                kf_name=self.get_argument('kf_name')
                customer_company=self.get_argument('customer_company')
                customer_name=self.get_argument('customer_name')
                income_type=self.get_argument('income_type')
                income_name=self.get_argument('income_name')
                if all_income!=None:
                    all_income=float(all_income)
                db.execute(
                    "update t_receipt set sale_name=%s,craeted_at=%s,project_name=%s,all_income=%s,kf_name=%s,"
                    "customer_company=%s,cus_id=%s,customer_name=%s,income_type=%s,income_name=%s where id=%s",
                    sale_name, craeted_at, project_name, all_income, kf_name,
                    customer_company, cus_id, customer_name, income_type,
                    income_name, int(id))
                self.redirect("/")
        else:
            sale_name=self.get_argument('sale_name')
            craeted_at=self.get_argument('craeted_at')
            project_name=self.get_argument('project_name')
            all_income=self.get_argument('all_income') or None
            kf_name=self.get_argument('kf_name')
            customer_company=self.get_argument('customer_company')
            customer_name=self.get_argument('customer_name')
            income_type=self.get_argument('income_type')
            income_name=self.get_argument('income_name')
            if all_income!=None:
                all_income=float(all_income)
            db.execute("update t_receipt set sale_name=%s,craeted_at=%s,project_name=%s,all_income=%s,kf_name=%s,"
            "customer_company=%s,cus_id=%s,customer_name=%s,income_type=%s,income_name=%s where id=%s",
            sale_name,craeted_at,project_name,all_income,kf_name,customer_company,cus_id,customer_name,income_type,income_name,int(id)
            )
            print('7')
            self.redirect("/")
