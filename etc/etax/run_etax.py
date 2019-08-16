#coding=utf8
import subprocess
import time
import torndb
import random

db = torndb.Connection("192.168.2.168", "db_customer","root","deng")
for item in range(1,1000):
    sql = """SELECT a.id,a.company,b.rel_name_collect_account,b.rel_name_collect_password FROM t_customer a 
    inner join t_customer_other_data b on a.id=b.customer_id where rel_name_collect_account 
    is not  null and rel_name_collect_password is not  null and date(get_at) = date('2019-07-01')  order by rand() limit 5 """;
    for item in db.query(sql):
        try:
            err_msg=""
            print u'node /home/domizzi/dev/nweb/ex.js {0} {1} {2} {3}'.format(item.rel_name_collect_account,item.rel_name_collect_password,item.id,item.company.replace("(",u"（").replace(")",u"）"))
            db.execute("update t_customer_other_data  set get_at=now() where customer_id=%s ",item.id)
            if  item.rel_name_collect_account==u"无" or item.rel_name_collect_account==u"未做"  :
                err_msg = "无帐号"
                db.execute("update t_customer_other_data  set get_at=now(),err_msg=%s where customer_id=%s ",err_msg,item.id)
            elif item.rel_name_collect_account and item.rel_name_collect_password  :
                subprocess.call(u'node /home/domizzi/dev/nweb/ex.js {0} {1} {2} {3}'.format(item.rel_name_collect_account,item.rel_name_collect_password,item.id,item.company.replace("(",u"（").replace(")",u"）")), shell=True)
            
            # db.execute("update t_customer_other_data  set get_at=now(),err_msg=%s where customer_id=%s ",err_msg,item.id)
        except:
            print "err"
            pass
    time.sleep(random.randint(3,5))

#node ex.js 启房地产  Nba619354  656 广州启房房地产代理有限公司