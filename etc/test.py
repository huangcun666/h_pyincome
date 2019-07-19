#coding=utf8
import torndb
import time
from pyquery import PyQuery as pq
import requests
def addNew():
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
        "Referer":"https://www.etax-gd.gov.cn/sso/login?service=https://www.etax-gd.gov.cn/xxmh/html/index_login.html?bszmFrom=1&t=1562144801212",
        "Cookie":
        "JSESSIONID=0967E8DAF721F8643EA1EF435780EECE;acw_tc=2f6a1fde15620550374206570ed451b6aa90bf5770817f16a648cd920c5d77;TY_SESSION_ID=95c1ff5e-eb25-4d1a-9e0f-ac73a0ddae95;DZSWJ_TGC=a9487c832d374f7caacf40c83f5b5420;TGC=TGT-526916-jgc0ShtnstqCJDDwDtUk0Yfhw6xe7neUlpPA6Dv1jmfD32s3Es-gddzswj;SERVERID=86cdeeb042bfa50e4e2f6cfb3d39739e|1562928083|1562902729"}

    doc = requests.get('https://www.etax-gd.gov.cn/web-tycx/tycx/query.do?t=1562656843866&bw=%7B%22taxML%22:%7B%22head%22:%7B%22gid%22:%22311085A116185FEFE053C2000A0A5B63%22,%22sid%22:%22yhscx.SBZS.SBXXCX%22,%22tid%22:%22+%22,%22version%22:%22%22%7D,%22body%22:%7B%22sbny%22:%22%22,%22skssqq%22:%222019-01-01%22,%22skssqz%22:%222019-06-30%22,%22gdbz%22:%22%22%7D%7D%7D' ,
    data={"bw":'{"taxML":{"head":{"gid":"311085A116185FEFE053C2000A0A5B63","sid":"yhscx.SBZS.SBXXCX","tid":" ","version":""},"body":{"sbny":"","skssqq":"2011-01-01","skssqz":"2019-06-30","gdbz":""}}}'}, headers=hd)
    print doc.content


addNew()