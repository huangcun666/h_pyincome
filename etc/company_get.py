#coding=utf8
import torndb
import time
from pyquery import PyQuery as pq
import requests
db1 = torndb.Connection("192.168.2.168", "db_customer","root","deng")


def addNew(name,company_id):
    print "开始抓取...",name

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
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36",
        "Accept":
        "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "Referer":
        "https://www.tianyancha.com/",
        "Accept-Encoding":
        "gzip, deflate, br",
        "Accept-Language":
        "zh-CN,zh;q=0.9",
        "Cookie":
        "TYCID=b357c9e0bbe511e8bdc5c3de6f3bb50e; undefined=b357c9e0bbe511e8bdc5c3de6f3bb50e; ssuid=9840529350; _ga=GA1.2.2097837523.1537345589; __insp_wid=677961980; __insp_nv=true; __insp_targlpu=aHR0cHM6Ly93d3cudGlhbnlhbmNoYS5jb20v; __insp_targlpt=5aSp55y85p_lLeWVhuS4muWuieWFqOW3peWFt1%2FkvIHkuJrkv6Hmga%2Fmn6Xor6Jf5YWs5Y_45p_l6K_iX_W3peWVhuafpeivol%2FkvIHkuJrkv6HnlKjkv6Hmga%2Fns7vnu58%3D; __insp_norec_sess=true; __insp_slim=1554772416097; aliyungf_tc=AQAAAHvjZUvJTw0ABhiMPQcxqdNsJxK6; bannerFlag=undefined; csrfToken=b6q-awi8BQy70w7jNlLaI4jS; Hm_lvt_e92c8d65d92d534b0fc290df538b4758=1557971816; _gid=GA1.2.94558782.1557971816; RTYCID=564e96776e8e47f7874c6b4ed9d2e67e; CT_TYCID=4a50e8ba7ec74416b0698194951863de; token=cca616471a844fd496a2a49819c9ba30; _utm=555a40400d8d4a2c819adcac4098ee96; tyc-user-info=%257B%2522claimEditPoint%2522%253A%25220%2522%252C%2522explainPoint%2522%253A%25220%2522%252C%2522integrity%2522%253A%25220%2525%2522%252C%2522state%2522%253A%25225%2522%252C%2522surday%2522%253A%2522231%2522%252C%2522announcementPoint%2522%253A%25220%2522%252C%2522vipManager%2522%253A%25220%2522%252C%2522onum%2522%253A%252263%2522%252C%2522monitorUnreadCount%2522%253A%2522169%2522%252C%2522discussCommendCount%2522%253A%25221%2522%252C%2522token%2522%253A%2522eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxODYyMDkwOTUxOSIsImlhdCI6MTU1Nzk4NTkyOSwiZXhwIjoxNTg5NTIxOTI5fQ.TIn71PFAYqeZjOjhDyiUu6CpfhNFVXwJ1nX54zpccDi0oou9RQ2LOZ3rFED3Eg5RfWj_Zei_S8ompxg4TVv0og%2522%252C%2522claimPoint%2522%253A%25220%2522%252C%2522redPoint%2522%253A%25220%2522%252C%2522myAnswerCount%2522%253A%25220%2522%252C%2522myQuestionCount%2522%253A%25220%2522%252C%2522signUp%2522%253A%25220%2522%252C%2522nickname%2522%253A%2522%25E7%25AC%259B%25E7%25A6%258F%2522%252C%2522privateMessagePointWeb%2522%253A%25220%2522%252C%2522privateMessagePoint%2522%253A%25220%2522%252C%2522isClaim%2522%253A%25220%2522%252C%2522isExpired%2522%253A%25220%2522%252C%2522pleaseAnswerCount%2522%253A%25221%2522%252C%2522vnum%2522%253A%252240%2522%252C%2522bizCardUnread%2522%253A%25220%2522%252C%2522mobile%2522%253A%252218620909519%2522%257D; auth_token=eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxODYyMDkwOTUxOSIsImlhdCI6MTU1Nzk4NTkyOSwiZXhwIjoxNTg5NTIxOTI5fQ.TIn71PFAYqeZjOjhDyiUu6CpfhNFVXwJ1nX54zpccDi0oou9RQ2LOZ3rFED3Eg5RfWj_Zei_S8ompxg4TVv0og; Hm_lpvt_e92c8d65d92d534b0fc290df538b4758=1557991533; _gat_gtag_UA_123487620_1=1; cloud_token=5548b97f260e4532a0b3645d0d43cd5c; cloud_utm=3f68e47f307041e0b609077251841f1d"
    }

    name=name.strip().replace("(",u"（").replace(")",u"）")
    doc = pq('https://www.tianyancha.com/search?key='+name,headers=hd)
    print 'https://www.tianyancha.com/search?key='+name
    # print doc.text()
    link  =  doc(".search-result-single a").attr("href")
    company = doc(".name").eq(0).text().replace(" ", "")
    company_his = doc("#web-content > div > div.container-left > div.search-block.header-block-container > div.result-list.sv-search-container > div > div > div.content > div.match.row.text-ellipsis > span:nth-child(3) > em").text()
    company_his_txt = doc("#web-content > div > div.container-left > div.search-block.header-block-container > div.result-list.sv-search-container > div > div > div.content > div.match.row.text-ellipsis > span.label").text()
    if u"历史名称" not in company_his_txt:
        company_his=""

    print company,link
    if not link:
        print "not link",link,name
        return False
    elif not company:
        print "没有抓到公司名",name
        return False
    else:
        doc_d = pq(link,headers=hd)
        company_uid  = doc_d("#_container_baseInfo > table.table.-striped-col.-border-top-none > tbody > tr:nth-child(3) > td:nth-child(2)").text()
        created = doc_d("#_container_baseInfo > table.table.-striped-col.-border-top-none.-breakall > tbody > tr:nth-child(1) > td:nth-child(4) > div").text()
        gs_uid = doc_d("#_container_baseInfo > table.table.-striped-col.-border-top-none.-breakall > tbody > tr:nth-child(2) > td:nth-child(4)").text()
        reg_dep = doc_d("#_container_baseInfo > table.table.-striped-col.-border-top-none.-breakall > tbody > tr:nth-child(8) > td:nth-child(4)").text()
        reg_addr =doc_d("#_container_baseInfo > table.table.-striped-col.-border-top-none.-breakall > tbody > tr:nth-child(10) > td:nth-child(2)").text()
        reg_scope = doc_d("#_container_baseInfo > table.table.-striped-col.-border-top-none.-breakall > tbody > tr:nth-child(11) > td:nth-child(2) > span > div > div").text()
        reg_by = doc_d("#_container_baseInfo > table:nth-child(1) > tbody > tr:nth-child(1) > td.left-col.shadow > div > div:nth-child(1) > div.humancompany > div.name > a").text()
        reg_money = doc_d("#_container_baseInfo > table.table.-striped-col.-border-top-none.-breakall > tbody > tr:nth-child(1) > td:nth-child(2) > div").text()
        industry = doc_d("#_container_baseInfo > table.table.-striped-col.-border-top-none.-breakall > tbody > tr:nth-child(5) > td:nth-child(4)").text()
        err_type = ""
        company_new=""

        if company ==name:
            print 'ok'
        elif company_his==name:
            err_type=u"当前为历史公司名称"
            company_new =company
            company = name
            print u"当前为历史公司名称:%s != %s != %s  update %s || %s"%(name,company,company_his,company_new,company)

        elif company != name :
            err_type=u"当前公司名称不一致"
            print u"当前公司名称不一致:%s != %s"%(name,company)
            company_new =company
            company= name
        company = company.strip().replace(u"（","(").replace(u"）",")")
        if company:
            print err_type,company_new,company,company_his
            company_new = company_new.strip().replace(u"（","(").replace(u"）",")")
            company = company.strip().replace(u"（","(").replace(u"）",")")

            print industry,reg_money,reg_by,company_uid,created,gs_uid,reg_dep,reg_scope,company_his,err_type

            db1.execute("""INSERT INTO `t_company_tyc` (`company`, `company_uid`, `created`, `reg_dep`, `reg_addr`, `reg_scope`, `reg_by`, `url`, `company_id`,`reg_money`,`industry`,err_type,company_new)
VALUES
	(%s,%s,%s,%s,%s,%s,%s,%s, %s,%s,%s,%s,%s);

            """,company,company_uid,created,reg_dep,reg_addr,reg_scope,reg_by,link,company_id,reg_money,industry,err_type,company_new)
            print company,name,"抓取成功..."
            return True
        else:
            print company,name ,"失败..."
            return False



def dowork():
    while 1:
        try:
            num =1
            for item in db1.query("select  id,company from t_customer where   id not in (select company_id from t_company_tyc) order by RAND() limit 3  "):
                print item
                num = num+1
                print 1
                #print "hello ",item.company,num
                if item.company:
                    result = addNew(item.company,item.id)
                    if result==False:
                        continue
                time.sleep(3)
            time.sleep(3)
        except:
            time.sleep(120)
            print "wait ",120

dowork()
print "done"