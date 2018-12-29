#coding=utf8
from pyquery import PyQuery as pq
import torndb,time
db = torndb.Connection("192.168.2.168","db_customer_test","root","deng")

for item in db.query ("select * from t_customer where company_reguid is null limit 1"):

    doc =  pq('https://www.tianyancha.com/search?key=' + item.company)
    print 'https://www.tianyancha.com/search?key=' + item.company
    print doc

    time.sleep(2)