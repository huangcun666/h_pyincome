#coding=utf8
import torndb
import time
from pyquery import PyQuery as pq
import requests
db = torndb.Connection("192.168.2.168", "db_income2", "root", "deng")
db1 = torndb.Connection("192.168.2.168", "db_customer", "root", "deng")


def addNew(name, company_id):
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
        "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "Referer":
        "https://www.tianyancha.com/",
        "Accept-Encoding":
        "gzip, deflate, br",
        "Accept-Language":
        "zh-CN,zh;q=0.9",
        "Cookie":
        "TYCID=a7511930f38511e8ac10d31168af962d; undefined=a7511930f38511e8ac10d31168af962d; ssuid=4016186264; _ga=GA1.2.1585521434.1543461602; aliyungf_tc=AQAAAOkoSWg4jQMATWx3ccebxDzFQ0Kz; csrfToken=yaDUD6M53ed6eDPTthKXyNwq; Hm_lvt_e92c8d65d92d534b0fc290df538b4758=1543461602,1545014446; _gid=GA1.2.365761508.1545014447; cloud_token=ecf6cbd932b54d35b0c7186e246ddba9; __insp_wid=677961980; __insp_nv=true; __insp_targlpu=aHR0cHM6Ly93d3cudGlhbnlhbmNoYS5jb20v; __insp_targlpt=5aSp55y85p_lLeS6uuS6uumDveWcqOeUqOWVhuS4muWuieWFqOW3peWFt1%2FkvIHkuJrkv6Hmga%2Fmn6Xor6Jf5YWs5Y_45p_l6K_iX_W3peWVhuafpeivol%2FkvIHkuJrkv6HnlKjkv6Hmga%2Fmn6Xor6Lns7vnu58%3D; __insp_norec_sess=true; token=4c8185a0979144fea4bafc4731fe664e; _utm=68c9808e85214433ba50a20aa9057732; tyc-user-info=%257B%2522myQuestionCount%2522%253A%25220%2522%252C%2522integrity%2522%253A%25220%2525%2522%252C%2522state%2522%253A%25220%2522%252C%2522vipManager%2522%253A%25220%2522%252C%2522onum%2522%253A%25220%2522%252C%2522monitorUnreadCount%2522%253A%25220%2522%252C%2522discussCommendCount%2522%253A%25220%2522%252C%2522token%2522%253A%2522eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxODAyNzMxODY2OCIsImlhdCI6MTU0NTA5NzE5OCwiZXhwIjoxNTYwNjQ5MTk4fQ.Gzx725ZpiHA0JMhv3aScXk0I_F7WG71u0w9oAGognsOLT5dQdNNibUEUnEU64w55UO4axvjHPlOWO1fVJBgNCA%2522%252C%2522redPoint%2522%253A%25220%2522%252C%2522pleaseAnswerCount%2522%253A%25220%2522%252C%2522vnum%2522%253A%25220%2522%252C%2522bizCardUnread%2522%253A%25220%2522%252C%2522mobile%2522%253A%252218027318668%2522%257D; auth_token=eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxODAyNzMxODY2OCIsImlhdCI6MTU0NTA5NzE5OCwiZXhwIjoxNTYwNjQ5MTk4fQ.Gzx725ZpiHA0JMhv3aScXk0I_F7WG71u0w9oAGognsOLT5dQdNNibUEUnEU64w55UO4axvjHPlOWO1fVJBgNCA; __insp_slim=1545097259580; Hm_lpvt_e92c8d65d92d534b0fc290df538b4758=1545097260"
    }

    doc = pq('https://www.tianyancha.com/search?key=' + name, headers=hd)
    print 'https://www.tianyancha.com/search?key=' + name
    
    link_company = doc(".name").eq(0).text().replace(" ", "")
    print type(link_company), link_company, "link_company", type(name), name, link_company == name


addNew("广东京卫",0)