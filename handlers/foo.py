# -*- coding: utf-8 -*-
from handlers.base import BaseHandler
import urllib
import json
import datetime
import time
import logging
import tornado
import tornado.httpclient
import os
import random
import string

logger = logging.getLogger('boilerplate.' + __name__)
from tornado.web import asynchronous, RequestHandler, Application
from concurrent.futures import ThreadPoolExecutor
from tornado.concurrent import run_on_executor
from tornado import gen

class mDemoHandler(BaseHandler):
    def get(self):
        self.redirect("/project")

class DemoHandler(BaseHandler):
    def get(self):
        self.render("demo/demo.html")


class FooHandler1(BaseHandler):

    @tornado.web.asynchronous
    @gen.coroutine
    def get(self):
        res = yield self.db.get('select * from t_user limit 1')

        self.write(res.name)
        self.finish()


class uploadHandler(tornado.web.RequestHandler):
    def post(self):
        file = self.request.files["upload"][0]
        callback = self.get_argument("CKEditorFuncNum")
        file_type= "photo"
        extension = os.path.splitext(file.filename)[1]

        if file_type is 'photo':
            type_list = ['.png','.jpg','.jpeg','.gif']
        elif file_type is 'attachment':
            type_list = ['.pdf','.doc','.docx','.xls']
        msg = "0"
        file_name_full=""
        if extension in type_list:
            file_name = ''.join(random.choice(string.ascii_lowercase + string.digits) for x in range(16))
            file_name_full =  file_name + extension
            output_file = open("media/public/" + file_name_full, 'wb')
            output_file.write(file.body)
            msg = "1"
        # self.write (file.filename + " has been uploaded."+msg)
        # self.write('<script>parent.ckeditorUpload("/static/public/'+file_name_full+'");</script>')
        output = "<script type=\"text/javascript\">parent.ckeditorUpload(\"/static/public/"+file_name_full+"\");"
        output =output+"window.parent.CKEDITOR.tools.callFunction(" + callback + ",'/static/public/" +file_name_full+ "','')"

        self.write(output+'</script>')



class DemoHandler(BaseHandler):
    def get(self):
        self.render("demo/demo.html")

class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        query = self.get_argument('q')
        client = tornado.httpclient.HTTPClient()
        response = client.fetch("http://www.bwlc.net/bulletin/prevtrax.html")
        body = response.body
        doc = pq(body)
        str_new= ""
        for tr in doc('.tb  tr').items():
            print tr.html()
            if tr("th").eq(0).text() == u"期号":
                continue
            else:
                qnum_full = tr("td").eq(0).text()
                knum_full = tr("td").eq(1).text()
                open_at = tr("td").eq(2).text()
                qnum = int(qnum_full[::-1][:1])
                if qnum==0:
                    qnum = 10
                pos = 0
                print knum_full
                sbq=[]
                xbq =[]
                for item in knum_full.split(","):
                    pos= pos+1
                    print qnum,pos,'===',int(item)

                    if pos <6:
                        sbq.append(item)
                    else:
                        xbq.append(item)
                    xbq_str = ','.join(str(e) for e in xbq)
                    sbq_str= ','.join(str(e) for e in sbq)
                    print xbq_str,sbq_str
                    if qnum ==int(item):
                        if pos > 5:
                            pos_result= "后期"
                            print pos,"后期",item
                            if qnum >5:
                                print "对"
                                result = "对"
                            else:
                                print "错"
                                result = "错"

                        else:
                            pos_result= "前期"
                            print pos,"前期",item
                            if qnum <=5:
                                print "对"
                                result = "对"
                            else:
                                print "错"
                                result = "错"
        # insert(qnum_full,knum_full,qnum,pos,pos_result,result,open_at,sbq_str,xbq_str)
                str_new=str_new+"<tr><td>{0}</td><td>{1}</td><td>{2}</td><td>{3}</td><td>{4}</td><td>{5}</td></tr>".format(qnum_full,knum_full,result,open_at,sbq_str,xbq_str)
        # self.write(str_new)
        return self.render('home.html',str_new=str_new)
