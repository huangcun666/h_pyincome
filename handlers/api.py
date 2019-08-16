# -*- coding: utf-8 -*-
from handlers.base import BaseHandler
import logging
import tornado
from tornado.httpclient import AsyncHTTPClient
import os
import random
import string
import re
import hashlib
import json
import time
logger = logging.getLogger('boilerplate.' + __name__)
import datetime
class cAPiHandler(BaseHandler):
    def get(self):
        tag = self.get_argument("tag","")
        if tag=="ver":
            sxml="""<?xml version='1.0' encoding='UTF-8'?>
            <gupdate xmlns='http://www.google.com/update2/response' protocol='2.2'>
            <app appid='bckhabggdgemchofckhkadfmfjjdkkci'>
                <updatecheck codebase='http://192.168.2.168:9000/static/chrome/chrome_faye.crx' version='2.0' />
            </app>
            </gupdate>
            """      
            self.set_header('Content-Type', 'text/xml')
            self.write(sxml)     
              
    def check_xsrf_cookie(self):
        pass
    @tornado.web.asynchronous
    @tornado.gen.coroutine
    def post(self):
        self.set_header("Access-Control-Allow-Origin", "*")
        self.set_header("Access-Control-Allow-Headers", "x-requested-with")
        self.set_header('Access-Control-Allow-Methods', 'POST, GET, OPTIONS')
        dt = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")     
        tag = self.get_argument("tag","")
        dt_query = datetime.datetime.now().strftime("%Y-%m-%d")  
        if tag=="update":
            sxml="""
            <?xml version='1.0' encoding='UTF-8'?>
            <gupdate xmlns='http://www.google.com/update2/response' protocol='2.0'>
            <app appid='bckhabggdgemchofckhkadfmfjjdkkci'>
                <updatecheck codebase='http://myhost.com/mytestextension/mte_v2.crx' version='2.0' />
            </app>
            </gupdate>
            """    

        elif tag=="err_msg":
            customer_id = self.get_argument("customer_id")
            err_msg =self.get_argument("err_msg")
            self.db_customer.execute("update t_customer_other_data set get_at=now(), err_msg=%s where customer_id=%s",err_msg,customer_id)
        elif tag == "get_etax":
            s = self.get_argument("s","")
            customer_id = self.get_argument("customer_id")
            company = self.get_argument("company")
            is_del = self.get_argument("is_del","")

            if not customer_id:
                self.write("not customer_id")
            if not company:
                self.write("not company")
            if not s:
                 self.write("请求失败.")
            else:
                get_url = u"https://www.etax-gd.gov.cn/web-tycx/tycx/query.do?t={0}&bw=%7B%22taxML%22:%7B%22head%22:%7B%22gid%22:%22311085A116185FEFE053C2000A0A5B63%22,%22sid%22:%22yhscx.SBZS.SBXXCX%22,%22tid%22:%22+%22,%22version%22:%22%22%7D,%22body%22:%7B%22sbny%22:%22%22,%22skssqq%22:%222015-01-01%22,%22skssqz%22:%22{1}%22,%22gdbz%22:%22%22%7D%7D%7D".format(str(int(time.time())),dt_query)
                print get_url
                hd = {
                "Connection":
                "keep-alive",
                "Pragma":
                "no-cache",
                "Cache-Control":
                "no-cache",
                "Upgrade-Insecure-Requests":
                "1",
                "User-Agent":
                "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.90 Safari/537.36",
                "Accept":
                "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
                "Referer":
                "www.etax-gd.gov.cn",
                "Accept-Encoding":
                "gzip, deflate, br",
                "Accept-Language":
                "zh-CN,zh;q=0.9",
                "Referer":"https://www.etax-gd.gov.cn/sso/login?service=https://www.etax-gd.gov.cn/xxmh/html/index_login.html?bszmFrom=1&t="+str(time.time()),
                "Cookie": s}            
                http_client = AsyncHTTPClient()

                try:
                    response = yield http_client.fetch(get_url,method="POST",headers=hd,body=b'')
                except Exception as e:
                    print("Error: %s" % e)
                else:
                    print(response.body)
                    js = json.loads(response.body)
                    ysbxx = None
                    try:
                        ysbxx  =  js["taxML"]["body"]["taxML"]["ysbxxList"]["ysbxx"]
                        if not is_del:
                            self.db_customer.execute("delete from t_etax  where customer_id=%s",customer_id)
                        if not ysbxx:
                            self.write("not ysbxx")
                        else:
                            for item in  ysbxx:
                                # customer_id=0
                                # company = "测试公司"
                                sbqx= item.get('sbqx',"")
                                zgswskfjmc = item.get("zgswskfjmc","")
                                ybtse= item.get('ybtse',"")
                                pzxh = item.get("pzxh","")
                                skssqq = item.get('skssqq',"")
                                yzpzzl_dm = item.get("yzpzzl_dm","")
                                sbuuid = item.get('sbuuid',"")
                                sbrq_1 = item.get("sbrq_1","")
                                gdslx = item.get('gdslx',"")
                                djxh = item.get("djxh","")
                                yjse = item.get('yjse',"")
                                zgswskfj_dm = item.get('zgswskfj_dm',"")
                                ynse = item.get('ynse',"")
                                ysx = item.get("ysx","")
                                zspm_dm = item.get('zspm_dm',"")
                                sbfsmc = item.get("sbfsmc","")
                                skssqz= item.get('skssqz',"")
                                lrrq = item.get("lrrq","")
                                zsxm_dm = item.get("zsxm_dm","")
                                lrr_dm = item.get('lrr_dm',"")
                                sbzt = item.get("sbzt","")
                                sblx_dm = item.get('sblx_dm',"")
                                zszmmc = item.get("zszmmc","")
                                zsxmmc = item.get("zsxmmc","")
                                buuid = item.get('buuid',"")
                                sblxmc= item.get("sblxmc","")
                                jmse = item.get('jmse',"")
                                gdslxDm= item.get("gdslxDm","")
                                jsyj= item.get("jsyj","")
                                dzbzdszlmc= item.get("dzbzdszlmc","")
                                nsrsbh = item.get("nsrsbh","")
                                gzlx_dm= item.get("gzlx_dm","")
                                zspmmc = item.get("zspmmc","")
                                sbfs_dm= item.get("sbfs_dm","")
                                
                                result = self.db_customer.execute("""
                                        insert INTO  `t_etax`
                                        (
                                        `customer_id`,
                                        `company`,
                                        `ctime`,
                                        `sbqx`,
                                        `zgswskfjmc`,
                                        `ybtse`,
                                        `skssqq`,
                                        `yzpzzl_dm`,
                                        `buuid`,
                                        `sbrq_1`,
                                        `gdslx`,
                                        `djxh`,
                                        `yjse`,
                                        `ynse`,
                                        `ysx`,
                                        `zspm_dm`,
                                        `sblxmc`,
                                        `jmse`,
                                        `gdslxDm`,
                                        `jsyj`,
                                        `dzbzdszlmc`,
                                        `nsrsbh`,
                                        `gzlx_dm`,
                                        `zspmmc`,
                                        `sbfs_dm`,
                                        `skssqz`,
                                        `lrrq`,
                                        `zsxm_dm`,
                                        `lrr_dm`,
                                        `sbzt`,
                                        `sblx_dm`,
                                        `zszmmc`,
                                        `zsxmmc`,`up_at`)
                                        VALUES
                                        (%s, %s,%s,%s,%s,
                                        %s, %s,%s,%s,%s,
                                        %s, %s,%s,%s,%s,
                                        %s, %s,%s,%s,%s,
                                            %s, %s,%s,%s,%s,
                                            %s, %s,%s,%s,%s,
                                            %s,%s,%s,%s
                                    );
                                """,
                                    customer_id,
                                        company,
                                        dt,
                                        sbqx,
                                        zgswskfjmc,
                                        ybtse,
                                        skssqq,
                                        yzpzzl_dm,
                                        buuid,
                                        sbrq_1,
                                        gdslx,
                                        djxh,
                                        yjse,
                                        ynse,
                                        ysx,
                                        zspm_dm,
                                        sblxmc,
                                        jmse,
                                        gdslxDm,
                                        jsyj,
                                        dzbzdszlmc,
                                        nsrsbh,
                                        gzlx_dm,
                                        zspmmc,
                                        sbfs_dm,
                                        skssqz,
                                        lrrq,
                                        zsxm_dm,
                                        lrr_dm,
                                        sbzt,
                                        sblx_dm,
                                        zszmmc,
                                        zsxmmc,dt
                                
                                )
                    except Exception,e:
                        print str(e)

                self.write(str("0"))

        elif tag == "enterSbqc":
            s = self.get_argument("s","")
            customer_id = self.get_argument("customer_id")
            company = self.get_argument("company")
            is_del = self.get_argument("is_del","")
            print customer_id,company
            if not customer_id:
                self.write("not customer_id")
            if not company:
                self.write("not company")
            if not s:
                 self.write("请求失败.")
            else:
                dt_query_year = datetime.datetime.now().strftime("%Y")  
                dt_query_month = datetime.datetime.now().strftime("%m")  
                qdate = "%s年%s月"%(dt_query_year,dt_query_month)
                get_date = datetime.datetime.now().strftime("%Y-%m-01")  
                get_url = u"https://www.etax-gd.gov.cn/sbzs-cjpt-web/biz/sbqc/sbqc_aqsb/enterSbqc?tjNd={0}&tjYf={1}&gdslxDm=1".format(dt_query_year,dt_query_month)

                print get_url
                hd = {
                "Connection": "keep-alive",
                "Pragma":  "no-cache",
                "Cache-Control":  "no-cache",
                "Upgrade-Insecure-Requests": "1",
                "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.90 Safari/537.36",
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
                "Referer": "www.etax-gd.gov.cn",
                "Accept-Encoding": "gzip, deflate, br",
                "Accept-Language": "zh-CN,zh;q=0.9",
                "Referer":"https://www.etax-gd.gov.cn/sbzs-cjpt-web/biz/sbqc/sbqc_aqsb/setting/lhSbbbs.jsp",
                "Cookie": s}            
                http_client = AsyncHTTPClient()

                try:
                    response = yield http_client.fetch(get_url,method="POST",headers=hd,body=b'')
                except Exception as e:
                    print("Error: %s" % e)
                else:
                    print(response.body)
                    # try:
                    js = json.loads(response.body)
                    sbqcList = None
                    sbqcList  =  js["sbqcList"]
                    if not  is_del:
                        self.db_customer.execute("delete from t_etax_wfm  where customer_id=%s and qdate=%s",customer_id,qdate)

                    if not sbqcList:
                        self.write("not sbqcList")
                    else:
                        for item in  sbqcList:
                            zsxmDm=item.get("zsxmDm","")
                            jkztDm=item.get("jkztDm","")
                            gdslxDm=item.get("gdslxDm","")
                            sbztDm=item.get("sbztDm","")
                            pzxh=item.get("pzxh","")
                            nsqxDm=item.get("nsqxDm","")
                            zsxmMc=item.get("zsxmMc","")
                            sbrq=item.get("sbrq","")
                            skssqQ=item.get("skssqQ","")
                            yxcfsb=item.get("yxcfsb","")
                            url=item.get("url","")
                            ysqxxId=item.get("ysqxxId","")
                            sbyfIn=item.get("sbyfIn","")
                            lastzs=item.get("lastzs","")
                            sbbcxx=item.get("sbbcxx","")
                            yzpzzlDm=item.get("yzpzzlDm","")
                            ybtse=item.get("ybtse","")
                            sbqx=item.get("sbqx","")
                            sbgcztDm=item.get("sbgcztDm","")
                            skssqZ=item.get("skssqZ","")
                            sbywbm=item.get("sbywbm","")
                            uuid=item.get("uuid","")
                            zspmMc=item.get("zspmMc","")
                            zspmDm=item.get("zspmDm","")
                            result = self.db_customer.execute("""
                                    INSERT INTO `t_etax_wfm`
                                    (`customer_id`,
                                    `company`,
                                    `ctime`,
                                    `zsxmDm`,
                                    `jkztDm`,
                                    `gdslxDm`,
                                    `sbztDm`,
                                    `pzxh`,
                                    `nsqxDm`,
                                    `zsxmMc`,
                                    `sbrq`,              
                                    `skssqQ`,            
                                    `yxcfsb`,            
                                    `url`,
                                    `ysqxxId`,
                                    `sbyfIn`,
                                    `lastzs`,
                                    `sbbcxx`,
                                    `yzpzzlDm`,
                                    `ybtse`,
                                    `sbqx`,
                                    `sbgcztDm`,
                                    `skssqZ`,
                                    `sbywbm`,
                                    `uuid`,
                                    `zspmMc`,
                                    `zspmDm`,
                                    `up_at`,`qdate`,get_date)
                                    VALUES
                                    (%s,%s,%s,%s,%s,
                                    %s,%s,%s,%s,%s,
                                    %s,%s,%s,%s,%s,
                                    %s,%s,%s,%s,%s,
                                    %s,%s,%s,%s,%s,
                                    %s,%s,%s,%s,%s);

                            """,
                                customer_id,
                                    company,
                                    dt,
                                    zsxmDm,
                                    jkztDm,
                                    gdslxDm,
                                    sbztDm,
                                    pzxh,
                                    nsqxDm,
                                    zsxmMc,
                                    sbrq,
                                    skssqQ,
                                    yxcfsb,
                                    url,
                                    ysqxxId,
                                    sbyfIn,
                                    lastzs,
                                    sbbcxx,
                                    yzpzzlDm,
                                    ybtse,
                                    sbqx,
                                    sbgcztDm,
                                    skssqZ,
                                    sbywbm,
                                    uuid,
                                    zspmMc,
                                    zspmDm,dt,qdate,get_date
                            )
                    # except Exception,e:
                    #     print str(e)

                self.write(str("0"))
        elif tag == "get_etax_js":
            a= self.get_argument("a","")
            customer_id =self.get_argument("customer_id")
            qdate = self.get_argument("qdate")
            company = self.get_argument("company")
            get_date = self.get_argument("get_date")
            print customer_id,qdate,company,get_date
            if not a:
                self.write("not a")
            else:
                js = json.loads(a)
                print js
                ysbxx = None

                ysbxx  =  js["taxML"]["body"]["taxML"]["ysbxxList"]["ysbxx"]
                if not ysbxx:
                    self.write("not ysbxx")
                else:
                    self.db_customer.execute("delete from t_etax  where customer_id=%s",customer_id)
                    
                    for item in  ysbxx:
                        # customer_id=0
                        # company = "测试公司"
                        sbqx= item.get('sbqx',"")
                        zgswskfjmc = item.get("zgswskfjmc","")
                        ybtse= item.get('ybtse',"")
                        pzxh = item.get("pzxh","")
                        skssqq = item.get('skssqq',"")
                        yzpzzl_dm = item.get("yzpzzl_dm","")
                        sbuuid = item.get('sbuuid',"")
                        sbrq_1 = item.get("sbrq_1","")
                        gdslx = item.get('gdslx',"")
                        djxh = item.get("djxh","")
                        yjse = item.get('yjse',"")
                        zgswskfj_dm = item.get('zgswskfj_dm',"")
                        ynse = item.get('ynse',"")
                        ysx = item.get("ysx","")
                        zspm_dm = item.get('zspm_dm',"")
                        sbfsmc = item.get("sbfsmc","")
                        skssqz= item.get('skssqz',"")
                        lrrq = item.get("lrrq","")
                        zsxm_dm = item.get("zsxm_dm","")
                        lrr_dm = item.get('lrr_dm',"")
                        sbzt = item.get("sbzt","")
                        sblx_dm = item.get('sblx_dm',"")
                        zszmmc = item.get("zszmmc","")
                        zsxmmc = item.get("zsxmmc","")
                        buuid = item.get('buuid',"")
                        sblxmc= item.get("sblxmc","")
                        jmse = item.get('jmse',"")
                        gdslxDm= item.get("gdslxDm","")
                        jsyj= item.get("jsyj","")
                        dzbzdszlmc= item.get("dzbzdszlmc","")
                        nsrsbh = item.get("nsrsbh","")
                        gzlx_dm= item.get("gzlx_dm","")
                        zspmmc = item.get("zspmmc","")
                        sbfs_dm= item.get("sbfs_dm","")
                        
                        result = self.db_customer.execute("""
                                insert INTO  `t_etax`
                                (
                                `customer_id`,
                                `company`,
                                `ctime`,
                                `sbqx`,
                                `zgswskfjmc`,
                                `ybtse`,
                                `skssqq`,
                                `yzpzzl_dm`,
                                `buuid`,
                                `sbrq_1`,
                                `gdslx`,
                                `djxh`,
                                `yjse`,
                                `ynse`,
                                `ysx`,
                                `zspm_dm`,
                                `sblxmc`,
                                `jmse`,
                                `gdslxDm`,
                                `jsyj`,
                                `dzbzdszlmc`,
                                `nsrsbh`,
                                `gzlx_dm`,
                                `zspmmc`,
                                `sbfs_dm`,
                                `skssqz`,
                                `lrrq`,
                                `zsxm_dm`,
                                `lrr_dm`,
                                `sbzt`,
                                `sblx_dm`,
                                `zszmmc`,
                                `zsxmmc`,`up_at`)
                                VALUES
                                (%s, %s,%s,%s,%s,
                                %s, %s,%s,%s,%s,
                                %s, %s,%s,%s,%s,
                                %s, %s,%s,%s,%s,
                                    %s, %s,%s,%s,%s,
                                    %s, %s,%s,%s,%s,
                                    %s,%s,%s,%s
                            );
                        """,
                            customer_id,
                                company,
                                dt,
                                sbqx,
                                zgswskfjmc,
                                ybtse,
                                skssqq,
                                yzpzzl_dm,
                                buuid,
                                sbrq_1,
                                gdslx,
                                djxh,
                                yjse,
                                ynse,
                                ysx,
                                zspm_dm,
                                sblxmc,
                                jmse,
                                gdslxDm,
                                jsyj,
                                dzbzdszlmc,
                                nsrsbh,
                                gzlx_dm,
                                zspmmc,
                                sbfs_dm,
                                skssqz,
                                lrrq,
                                zsxm_dm,
                                lrr_dm,
                                sbzt,
                                sblx_dm,
                                zszmmc,
                                zsxmmc,dt
                        
                        )


                self.write(str(result))

        elif tag == "enterSbqc_js":
            a= self.get_argument("a","")
            customer_id =self.get_argument("customer_id")
            qdate = self.get_argument("qdate")
            company = self.get_argument("company")
            get_date = self.get_argument("get_date")
            if not a:
                self.write("not a")
            else:
             
                js = json.loads(a.encode('iso-8859-1').decode('UTF-8'))
                print js
                sbqcList  =  js["sbqcList"]
                if not sbqcList:
                    self.write("not sbqcList")
                else:
                    self.db_customer.execute("delete from t_etax_wfm  where customer_id=%s and qdate=%s",customer_id,qdate)
                    
                    for item in  sbqcList:
                        zsxmDm=item.get("zsxmDm","")
                        jkztDm=item.get("jkztDm","")
                        gdslxDm=item.get("gdslxDm","")
                        sbztDm=item.get("sbztDm","")
                        pzxh=item.get("pzxh","")
                        nsqxDm=item.get("nsqxDm","")
                        zsxmMc=item.get("zsxmMc","")
                        sbrq=item.get("sbrq","")
                        skssqQ=item.get("skssqQ","")
                        yxcfsb=item.get("yxcfsb","")
                        url=item.get("url","")
                        ysqxxId=item.get("ysqxxId","")
                        sbyfIn=item.get("sbyfIn","")
                        lastzs=item.get("lastzs","")
                        sbbcxx=item.get("sbbcxx","")
                        yzpzzlDm=item.get("yzpzzlDm","")
                        ybtse=item.get("ybtse","")
                        sbqx=item.get("sbqx","")
                        sbgcztDm=item.get("sbgcztDm","")
                        skssqZ=item.get("skssqZ","")
                        sbywbm=item.get("sbywbm","")
                        uuid=item.get("uuid","")
                        zspmMc=item.get("zspmMc","")
                        zspmDm=item.get("zspmDm","")
                        result = self.db_customer.execute("""
                                INSERT INTO `t_etax_wfm`
                                (`customer_id`,
                                `company`,
                                `ctime`,
                                `zsxmDm`,
                                `jkztDm`,
                                `gdslxDm`,
                                `sbztDm`,
                                `pzxh`,
                                `nsqxDm`,
                                `zsxmMc`,
                                `sbrq`,              
                                `skssqQ`,            
                                `yxcfsb`,            
                                `url`,
                                `ysqxxId`,
                                `sbyfIn`,
                                `lastzs`,
                                `sbbcxx`,
                                `yzpzzlDm`,
                                `ybtse`,
                                `sbqx`,
                                `sbgcztDm`,
                                `skssqZ`,
                                `sbywbm`,
                                `uuid`,
                                `zspmMc`,
                                `zspmDm`,
                                `up_at`,`qdate`,get_date)
                                VALUES
                                (%s,%s,%s,%s,%s,
                                %s,%s,%s,%s,%s,
                                %s,%s,%s,%s,%s,
                                %s,%s,%s,%s,%s,
                                %s,%s,%s,%s,%s,
                                %s,%s,%s,%s,%s);

                        """,
                            customer_id,
                                company,
                                dt,
                                zsxmDm,
                                jkztDm,
                                gdslxDm,
                                sbztDm,
                                pzxh,
                                nsqxDm,
                                zsxmMc,
                                sbrq,
                                skssqQ,
                                yxcfsb,
                                url,
                                ysqxxId,
                                sbyfIn,
                                lastzs,
                                sbbcxx,
                                yzpzzlDm,
                                ybtse,
                                sbqx,
                                sbgcztDm,
                                skssqZ,
                                sbywbm,
                                uuid,
                                zspmMc,
                                zspmDm,dt,qdate,get_date
                        )


            self.write(str("0"))
        else:
            print "=====",self.get_argument("a")
            self.write("00")
class ApiHandler(BaseHandler):
    def get(self):
            a = self.get_argument("a","")
            tag = self.get_argument("tag","")
            if tag=='users':
                q=self.get_argument('q','')
                response = []
                t_users = self.db.query("select * from t_user where is_lock=0  and  name like  '%%"+q+"%%' limit 10 ")
                for item in t_users:
                    response.append(item.name)  
                return self.write(tornado.escape.json_encode(response))
            print a
            return self.write(a)
        
    @tornado.web.authenticated
    def post(self):
        tag = self.get_argument("tag","user")
        query= self.get_argument("query",'')
        if tag =="user":

            response = []
            if query:
                t_users = self.db.query("select * from t_user where is_lock=0  and  name like  '%%"+query+"%%' ")

                for item in t_users:
                    response.append(item.name)  
            self.write(tornado.escape.json_encode(response))
        elif tag == "userandid":
            response = []
            if query:
                t_users = self.db.query(
                    "select * from t_user where name like  '%%" + query + "%%' ")

                for item in t_users:
                    response.append(item.name+","+str(item.id))
            self.write(tornado.escape.json_encode(response))

        elif tag=="addr":
            response = []
            if query:
                t_users = self.db.query(u"select * from t_projects_type where income_category='地址类型' and  income_name like  '%%"+query+"%%' ")

                for item in t_users:
                    response.append(item.income_name)
            self.write(tornado.escape.json_encode(response))

        elif tag=='company':
            response = []
            if query:
                query = query.replace("（","(").replace("）",")") 
            if len(query)>0:
                t_users = self.db.query("select * from t_projects where customer_company like  '%%"+query+"%%' limit 20")
                for item in t_users:
                    response.append(item.customer_company)
            self.write(tornado.escape.json_encode(response))
        elif tag=='customer_company':
            if query:
                query = query.replace("（","(").replace("）",")") 
            response = []
            if len(query)>0:
                t_users = self.db_customer.query("select * from t_customer where company like  '%%"+query+"%%' limit 20 ")
                for item in t_users:
                    response.append(item.company)
            self.write(tornado.escape.json_encode(response))
        elif tag=='customer_company_guid':
            if query:
                query = query.upper()
            response = []
            if len(query)>0:
                t_users = self.db_customer.query("select * from t_customer where company like  '%%"+query+"%%' limit 20 ")
                for item in t_users:
                    response.append(item.company+"-"+item.company_reguid)
            self.write(tornado.escape.json_encode(response))
        elif tag=='customer_company_one':
            if len(query)>0:
                query = query.replace("（","(").replace("）",")") 
                t_customer = self.db_customer.get("select company_reguid from t_customer where company='%s'  ",query)
                if not t_customer:
                    query = query.replace("(","（").replace(")","）") 
                    t_customer = self.db_customer.get("select company_reguid from t_customer where company = %s  ",query)
        
                if t_customer:
                    self.write(t_customer.company_reguid)
                else:
                    self.write("")

        elif tag == 'customer_company_acc_uid':

            uid =self.get_secure_cookie("uid")
            response = []
            if len(query) > 0:
                t_users = self.db_customer.query(
                    "select * from t_customer where acc_uid =%s and company like  '%%"
                    + query + "%%' limit 20 ", uid)
                for item in t_users:
                    response.append(item.company)
            print response,"lllll"
            self.write(tornado.escape.json_encode(response))

        elif tag=="department":
            department=self.get_argument('department')
            responsible_pers=self.db.query('''
                select responsible_per  from t_todo_arrange a
                inner join t_user b on a.responsible_per=b.name and department_name=%s group by department_name
            ''',department)
            self.write({'responsible_pers':responsible_pers})

        else:
            self.write(self.get_argument("a"))



class OApiHandler(BaseHandler):
    # @tornado.web.authenticated
    # def post(self):
    #     tag = self.get_argument("tag", "user")
    #     query = self.get_argument("query")
    #     if tag == "user":
    #         response = []
    #         if query:
    #             t_users = self.db.query(
    #                 "select * from t_user where name like  '%%" + query +
    #                 "%%' ")

    #             for item in t_users:
    #                 response.append(item.name)
    #         self.write(tornado.escape.json_encode(response))

    def get(self):


        tag = self.get_argument("tag")
        if tag =="auth":
            f_email = self.get_argument("username", None)
            f_password = self.get_argument("password", None)

            error = None
            role = 0
            uid= 0
            is_manager = 0
            if not f_email:
                error = "登录帐户不能为空."
            # elif not self.validate(f_email):
            # 	error="您的帐户格式不正确."
            elif not f_password:
                error = "登录密码不能为空."

            elif self.authenticate(f_email, f_password):
                t_user = self.get_user_info(f_email)
                if t_user:
                    uid = t_user.id
                    is_manager= t_user.is_manager
                    t_role = self.db.get("select * from t_user_group where id=%s",
                                        t_user.role)
                    if not t_role:
                        error = "还没有分配用户组"
                    else:
                        error=""
                        role = t_role.name
                else:
                    error = "登录帐户已经过期,请与我们联系."
            else:
                error = "登录帐户信息不正确,请效验后再重试."

            response = {
                "error": error,
                "username": f_email,
                "role": role,
                "uid": uid,
                "is_manager": is_manager
            }
            self.write(tornado.escape.json_encode(response))

    def get_user_info(self, name):
        t_user = self.db.get('''
				SELECT * FROM t_user
				WHERE name=%s
			''', name)
        return t_user

    def validate(self, f_email):
        regex = re.compile(r'^[\w\.=-]+@[\w\.-]+\.[\w]{2,3}$')
        return regex.match(f_email)

    def authenticate(self, username, password):
        logger.info(username, password)
        hashPassword = self.db.get(
            'SELECT pass user_pass FROM t_user WHERE name = %s', username)
        if hashPassword:
            return hashlib.md5(password).hexdigest() == hashPassword.user_pass
