#coding=utf8
import torndb
import time
from pyquery import PyQuery as pq
import requests
db = torndb.Connection("192.168.2.168", "db_income2","root","deng")
db1 = torndb.Connection("192.168.2.168", "db_customer","root","deng")
from random import randint


def addNew(name, company, company_id):
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
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36",
        "Accept":
        "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "Referer":
        "https://www.tianyancha.com/",
        "Accept-Encoding":
        "gzip, deflate, br",
        "Accept-Language":
        "zh-CN,zh;q=0.9",
        "Cookie":
        "TYCID=a7511930f38511e8ac10d31168af962d; undefined=a7511930f38511e8ac10d31168af962d; ssuid=4016186264; _ga=GA1.2.1585521434.1543461602; _gid=GA1.2.365761508.1545014447; __insp_wid=677961980; __insp_nv=true; __insp_targlpu=aHR0cHM6Ly93d3cudGlhbnlhbmNoYS5jb20vc2VhcmNoP2tleT0lRTUlQjklQkYlRTUlQjclOUUlRTYlOTglOUYlRTUlQTUlODclRTclQTclOTElRTYlOEElODAlRTYlOUMlODklRTklOTklOTAlRTUlODUlQUMlRTUlOEYlQjgmcm5kPSZybmQ9JnJuZD0mcm5kPSZybmQ9JnJuZD0mcm5kPSZybmQ9JnJuZD0mcm5kPSZybmQ9JnJuZD0mcm5kPSZybmQ9JnJuZD0mcm5kPSZybmQ9JnJuZD0mcm5kPQ%3D%3D; __insp_targlpt=5bm%2F5bee5pif5aWH56eR5oqA5pyJ6ZmQ5YWs5Y_4X_ebuOWFs_aQnOe0oue7k_aenC3lpKnnnLzmn6U%3D; __insp_norec_sess=true; aliyungf_tc=AQAAAC35bjpr0A0A5RmMPYm9WOe4Asnq; csrfToken=-w8hA9i4CJSXiQbygq8QN4V6; Hm_lvt_e92c8d65d92d534b0fc290df538b4758=1543461602,1545014446,1545109876; RTYCID=85f7164c9b6742548df2ea761e5cb3e5; CT_TYCID=3dbeede0a633496cbbb817286edcdfda; cloud_token=4e228ffdf3f348b8a7485512bf993248; cloud_utm=1f0e59ac73274334ba6d8850f453457e; _gat_gtag_UA_123487620_1=1; tyc-user-info=%257B%2522myQuestionCount%2522%253A%25220%2522%252C%2522integrity%2522%253A%25220%2525%2522%252C%2522state%2522%253A%25220%2522%252C%2522vipManager%2522%253A%25220%2522%252C%2522onum%2522%253A%25220%2522%252C%2522monitorUnreadCount%2522%253A%25220%2522%252C%2522discussCommendCount%2522%253A%25220%2522%252C%2522token%2522%253A%2522eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxODAyNzMxODY2OCIsImlhdCI6MTU0NTExMDIzOSwiZXhwIjoxNTYwNjYyMjM5fQ.LbHiFyZi0nHAI-c23DGTrqGSUV_oDhW9SwFSmSklkMDXQxO2Seygup2C_v9kQVAEM_ZgIq7Y8PYni3Lf7Porhw%2522%252C%2522redPoint%2522%253A%25220%2522%252C%2522pleaseAnswerCount%2522%253A%25220%2522%252C%2522vnum%2522%253A%25220%2522%252C%2522bizCardUnread%2522%253A%25220%2522%252C%2522mobile%2522%253A%252218027318668%2522%257D; auth_token=eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxODAyNzMxODY2OCIsImlhdCI6MTU0NTExMDIzOSwiZXhwIjoxNTYwNjYyMjM5fQ.LbHiFyZi0nHAI-c23DGTrqGSUV_oDhW9SwFSmSklkMDXQxO2Seygup2C_v9kQVAEM_ZgIq7Y8PYni3Lf7Porhw; __insp_slim=1545110258939; Hm_lpvt_e92c8d65d92d534b0fc290df538b4758=1545110259"
    }


    doc = pq('https://www.tianyancha.com/search?key='+name,headers=hd)
    print 'https://www.tianyancha.com/search?key='+name
    link_company = doc(".name").eq(0).text().replace(" ", "")

    # print "tyc_company_name", link_company,

    if link_company:
        is_good =6
        if link_company == company:
            is_good= 5
        print link_company,"对比中:::",company, link_company == company
        db1.execute(
            "update t_customer set is_get=%s,is_get_at=now(),tyc_name=%s where id=%s",
            is_good, link_company, company_id)
    else:
        print  "天眼查抓取失败,需打码" ,link_company
        time.sleep(15)

def dowork():
    num =1
    for item in db1.query(
            "select  id,company_reguid_new,company from t_customer where  company_reguid_new is not  null and (is_get =1 or is_get=3 or is_get=6) order by created_at "):
        num = num+1
        print "开始 ", item.company_reguid_new, num,item.id, item.company
        if item.company and item.company_reguid_new != "-":
            db1.execute(
             "update t_customer set is_get=7,is_get_at=now() where id=%s", item.id)
            addNew(item.company_reguid_new,item.company, item.id)
            time.sleep(1)



dowork()
print "done"