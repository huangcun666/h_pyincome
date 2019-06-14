#coding=utf8
import torndb
import time
from pyquery import PyQuery as pq
import requests
db = torndb.Connection("192.168.2.168", "db_income2","root","deng")
db1 = torndb.Connection("192.168.2.168", "db_customer","root","deng")

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
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36",
        "Accept":
        "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "Referer":
        "https://www.tianyancha.com/login?from=https%3A%2F%2Fwww.tianyancha.com%2Fcompany%2F2320991369",
        "Accept-Encoding":
        "gzip, deflate, br",
        "Accept-Language":
        "zh-CN,zh;q=0.9",
        "Cookie":
        "TYCID=b357c9e0bbe511e8bdc5c3de6f3bb50e; undefined=b357c9e0bbe511e8bdc5c3de6f3bb50e; ssuid=9840529350; _ga=GA1.2.2097837523.1537345589; aliyungf_tc=AQAAAHUFyx/JeQAAXRiMPa46rFdBFQ91; csrfToken=-U8TU9Zp1Ua765CUOQwN5gxg; Hm_lvt_e92c8d65d92d534b0fc290df538b4758=1551325773,1551947032,1551947032; refresh_page=null; _gid=GA1.2.1788053445.1553666354; __insp_wid=677961980; __insp_nv=true; __insp_targlpu=aHR0cHM6Ly93d3cudGlhbnlhbmNoYS5jb20v; __insp_targlpt=5aSp55y85p_lLeWVhuS4muWuieWFqOW3peWFt1%2FkvIHkuJrkv6Hmga%2Fmn6Xor6Jf5YWs5Y_45p_l6K_iX_W3peWVhuafpeivol%2FkvIHkuJrkv6HnlKjkv6Hmga%2Fns7vnu58%3D; __insp_norec_sess=true; token=8498b21c4f60477bb63b672667f9ff4c; _utm=86acf79c96b44c63864e960a5e7c3314; tyc-user-info=%257B%2522claimEditPoint%2522%253A%25220%2522%252C%2522myAnswerCount%2522%253A%25220%2522%252C%2522myQuestionCount%2522%253A%25220%2522%252C%2522explainPoint%2522%253A%25220%2522%252C%2522privateMessagePointWeb%2522%253A%25220%2522%252C%2522nickname%2522%253A%2522%25E5%25B8%258C%25E7%2589%25B9%25E5%258B%2592%2522%252C%2522integrity%2522%253A%25220%2525%2522%252C%2522privateMessagePoint%2522%253A%25220%2522%252C%2522state%2522%253A%25225%2522%252C%2522announcementPoint%2522%253A%25220%2522%252C%2522surday%2522%253A%2522281%2522%252C%2522isClaim%2522%253A%25220%2522%252C%2522vipManager%2522%253A%25220%2522%252C%2522discussCommendCount%2522%253A%25221%2522%252C%2522monitorUnreadCount%2522%253A%252231%2522%252C%2522onum%2522%253A%25220%2522%252C%2522isExpired%2522%253A%25220%2522%252C%2522claimPoint%2522%253A%25220%2522%252C%2522token%2522%253A%2522eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxNTYyMjE2MDMxMyIsImlhdCI6MTU1MzY2NjQwOCwiZXhwIjoxNTY5MjE4NDA4fQ.LLVYc_KqrLTIO1VY06eLjFdbvJHvqWQVq1tN4VoIov5m_ROH60QLZYyYZHNBX54p3HUqS_X3qlmDa6s9E-OrWw%2522%252C%2522pleaseAnswerCount%2522%253A%25221%2522%252C%2522redPoint%2522%253A%25220%2522%252C%2522bizCardUnread%2522%253A%25220%2522%252C%2522vnum%2522%253A%252220%2522%252C%2522mobile%2522%253A%252215622160313%2522%257D; auth_token=eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxNTYyMjE2MDMxMyIsImlhdCI6MTU1MzY2NjQwOCwiZXhwIjoxNTY5MjE4NDA4fQ.LLVYc_KqrLTIO1VY06eLjFdbvJHvqWQVq1tN4VoIov5m_ROH60QLZYyYZHNBX54p3HUqS_X3qlmDa6s9E-OrWw; RTYCID=5c807feb417f4807969e5196f4b809b3; Hm_lpvt_e92c8d65d92d534b0fc290df538b4758=1553666410; __insp_slim=1553666410681; CT_TYCID=63ec7f3a099e45a987960662f1c7cdb6; cloud_token=3e84892a3da94473b5296cbe85a3479b; cloud_utm=a348c5542a6a4145878211425e3a9897"
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
            db1.execute("update t_customer set company_reguid_new=%s,is_get=%s,is_get_at=now() where id=%s",guid,is_good,company_id)

def dowork():
    num =1
    for item in db1.query("select  id,company from t_customer where  company_reguid_new is null and (is_get=0  or is_get=2) order by created_at "):
        num = num+1
        print "hello ",item.company,num
        if item.company:
            db1.execute(
                "update t_customer set is_get=2,is_get_at=now() where id=%s", item.id)
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