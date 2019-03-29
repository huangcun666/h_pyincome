#coding=utf8
import torndb
import time
from pyquery import PyQuery as pq
import requests
db = torndb.Connection("192.168.2.169", "db_customer","root","deng")

def addNew(name,company_id):
    print name
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
        "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0 .8",
        "Referer":
        "https://www.tianyancha.com/",
        "Accept-Encoding":
        "gzip, deflate, br",
        "Accept-Language":
        "zh-CN,zh;q=0.9",
        "Cookie":
        "aliyungf_tc=AQAAANO8OWbRIw8ATWx3ceE5q7huSrDp; csrfToken=Qw3VkVDGDavVhaKdAPsQxcpP; TYCID=e18a580001d611e9857bb3db62d2e876; undefined=e18a580001d611e9857bb3db62d2e876; ssuid=2992908032; __insp_wid=677961980; __insp_slim=1545036548242; __insp_nv=true; __insp_targlpu=aHR0cHM6Ly93d3cudGlhbnlhbmNoYS5jb20v; __insp_targlpt=5aSp55y85p_lLeS6uuS6uumDveWcqOeUqOWVhuS4muWuieWFqOW3peWFt1%2FkvIHkuJrkv6Hmga%2Fmn6Xor6Jf5YWs5Y_45p_l6K_iX_W3peWVhuafpeivol%2FkvIHkuJrkv6HnlKjkv6Hmga%2Fmn6Xor6Lns7vnu58%3D; Hm_lvt_e92c8d65d92d534b0fc290df538b4758=1545035805; Hm_lpvt_e92c8d65d92d534b0fc290df538b4758=1545036549; __insp_norec_sess=true; _ga=GA1.2.1399497296.1545035808; _gid=GA1.2.709530492.1545035808; token=247936aea8a841309fcd7ba0cfd475f4; _utm=946a089c2c0349a89ed4b1a06ba4123b; tyc-user-info=%257B%2522myQuestionCount%2522%253A%25220%2522%252C%2522integrity%2522%253A%25220%2525%2522%252C%2522state%2522%253A%25225%2522%252C%2522vipManager%2522%253A%25220%2522%252C%2522monitorUnreadCount%2522%253A%252233%2522%252C%2522discussCommendCount%2522%253A%25221%2522%252C%2522onum%2522%253A%252245%2522%252C%2522renewalText%2522%253A%2522%25E4%25B9%25B01%25E9%2580%25811%2522%252C%2522isExpired%2522%253A%25221%2522%252C%2522token%2522%253A%2522eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxODYyMDkwOTUxOSIsImlhdCI6MTU0NTAzNTgzOCwiZXhwIjoxNTYwNTg3ODM4fQ.zIUGXHQn3qtjv7inG4kQtLUgaEbYZmg-fU66SQebSRcRX4fYfvgKiiA6TDKrShh24xPbojDmDRgNzNf9Bemo_w%2522%252C%2522redPoint%2522%253A%25220%2522%252C%2522pleaseAnswerCount%2522%253A%25221%2522%252C%2522renewal%2522%253A%25221%2522%252C%2522bizCardUnread%2522%253A%25220%2522%252C%2522vnum%2522%253A%252220%2522%252C%2522mobile%2522%253A%252218620909519%2522%257D; auth_token=eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxODYyMDkwOTUxOSIsImlhdCI6MTU0NTAzNTgzOCwiZXhwIjoxNTYwNTg3ODM4fQ.zIUGXHQn3qtjv7inG4kQtLUgaEbYZmg-fU66SQebSRcRX4fYfvgKiiA6TDKrShh24xPbojDmDRgNzNf9Bemo_w; RTYCID=d7be9861bd4e4e508295acc63eaccfef; CT_TYCID=4ea00e1e6ef745bfbedda294536145ea; cloud_token=b81e311fffec45019dba39ac2fdda6e4; cloud_utm=de4e109ec25f4f2b8e93cb9035613e09"
    }


    doc = pq('https://www.tianyancha.com/search?key='+name,headers=hd)
    print 'https://www.tianyancha.com/search?key='+name
    link  =  doc(".name").attr("href")
    link_company = doc(".name").eq(0).text().replace(" ", "")
    print  type(link_company),link_company,"link_company",type(name),name ,link_company == name
    #    return False
    if link :
        doc_d = pq(link,headers=hd)
        guid  = doc_d("#_container_baseInfo > table.table.-striped-col.-border-top-none > tbody > tr:nth-child(3) > td:nth-child(2)").text()
        if guid and link_company:
            is_good =3
            if link_company == name:
                is_good= 1

            print guid,link_company
            db1.execute("update t_customer set company_reguid=%s where id=%s",guid,is_good,company_id)

def dowork():
    num =1
    for item in db1.query("select  id,company from t_customer where  company_reguid is null order by created_at "):
        num = num+1
        print "hello ",item.company,num
        if item.company:
            new_guid = addNew(item.company,item.id)


        time.sleep(1)
    #        if new_guid:
#            db.execute("update  t_projects set new_company_uid=%s where id =%s",new_guid,item.id)





#                data = json.loads(txt)
#                for row in data["rows"]:
#                    if u"公司" in row["entTypeStr"] :
#                        print row["entName"]



# while (True):

dowork()
print "done"