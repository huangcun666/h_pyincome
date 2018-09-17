#-*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
import openpyxl
import torndb
import re
from datetime import datetime
from decimal import Decimal
db = torndb.Connection("192.168.2.168", "db_customer","root","deng")
wb = openpyxl.load_workbook(u"customer.xlsx")
#print wb.get_sheet_names()
sheet2 =  wb.get_sheet_by_name(u'发业集团记账应收表（正常客户）')
product_sheet =wb.get_active_sheet()
i = 0
for item in product_sheet:
        sp_id=0
        i = i+1
        lines=[1,2]
        if i in lines:
            continue  # 跳过第一行

        code =  item[0].value
        company = item[1].value
        kj = item[2].value
        # addr_type = item[3].value
        # addr_date = item[4].value
        # if addr_date:
        #     addr_date=re.split('-',addr_date)[1]
        #     addr_date=re.sub(r'\.','-',addr_date,2)+' 00:00:00'
        #     addr_date=datetime.strptime(addr_date,'%Y-%m-%d %H:%M:%S')
        #     print(addr_date)
        c_start = item[5].value
        c_end = item[6].value
        if code:
            #todo 增加判断是不是存在
            is_company=db.query("""
                select company from t_customer where company=%s
            """,company)
            #todo 获取会计的uid
            if is_company:
                uid=db.query("""
                        select id from db_income2.t_user where name=%s
                    """,kj)
                if uid:
                    db.execute("""
                UPDATE t_customer set acc_uid_name=%s, acc_uid=%s where company=%s
                """,kj,uid[0]['id'],company)
            else:
                if company!=None and "公司" in company:
                    uid=db.query("""
                        select id from db_income2.t_user where name=%s
                    """,kj)
                    if uid:
                        db.execute("""
                        INSERT INTO `t_customer` ( `id`,`company`, `reg_addr`, `reg_tel`, `reg_number`, `reg_person`, `reg_bank`, `reg_bank_account`, `addr_type`, `addr_expire`, `addr_cp`, `acc_uid`, `acc_uid_name`, `created_at`, `updated_at`, `guid`, `remark`, `reg_date`, `end_date`, `saic`, `national_tax`, `land_tax`, `company_reguid`, `industry_name`, `is_general`, `credit_rating`, `customer_rating`, `credit_rating_name`, `customer_rating_name`, `updated_at_name`, `customer_type`, `customer_type_name`, `uid`, `uid_name`, `acc_uid_at`)
                        VALUES
                            (%s,%s, '', '', '', '', '', '', '', NULL, '', %s, %s,now(), now(), uuid(), NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, now());
                        """,code,company,uid[0]['id'],kj)

                    try:
                        if '年' in c_start:
                            c_start=re.sub(u"[\u4e00-\u9fa5]",'-',c_start)+'-1 00:00:00'
                            c_start=datetime.strptime(c_start,'%Y-%m-%d %H:%M:%S')
                            print(c_start)
                        if '年' in c_end: 
                            c_end=re.sub(u"[\u4e00-\u9fa5]",'-',c_end)+'-1 00:00:00'
                            c_end=datetime.strptime(c_end,'%Y-%m-%d %H:%M:%S')
                            print(c_end)
                    except:
                        pass
                       
                    if isinstance(c_start,datetime) and isinstance(c_end,datetime):
                        db.execute("""
                            INSERT INTO t_contract(customer_id,guid,title,start_time,end_time,updated_at)
                            VALUES(%s,uuid(),'记账合同',%s,%s,now())
                            """,code,c_start,c_end)
                    if  isinstance(c_start,datetime):
                        if isinstance(c_end,datetime)==False:
                            db.execute("""
                                INSERT INTO t_contract(customer_id,guid,title,start_time,updated_at)
                                VALUES(%s,uuid(),'记账合同',%s,now())
                                """,code,c_start)
                    if  isinstance(c_end,datetime): 
                        if isinstance(c_start,datetime)==False:
                            db.execute("""
                                INSERT INTO t_contract(customer_id,guid,title,end_time,updated_at)
                                VALUES(%s,uuid(),'记账合同',%s,now())
                                """,code,c_end)
                    if  isinstance(c_start,datetime)==False:
                        if isinstance(c_end,datetime)==False:
                            db.execute("""
                                INSERT INTO t_contract(customer_id,guid,title,updated_at)
                                VALUES(%s,uuid(),'记账合同',now())
                                """,code)


#-*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
import openpyxl
import torndb
import re
from datetime import datetime
from decimal import Decimal
db = torndb.Connection("192.168.2.168", "db_customer","root","deng")
wb = openpyxl.load_workbook(u"customer.xlsx")
#print wb.get_sheet_names()
sheet2 =  wb.get_sheet_by_name(u'发业集团记账应收表（正常客户）')
product_sheet =wb.get_active_sheet()
i = 0
for item in product_sheet:
        sp_id=0
        i = i+1
        lines=[1,2]
        if i in lines:
            continue  # 跳过第一行

        code =  item[0].value
        company = item[1].value
        kj = item[2].value
        # addr_type = item[3].value
        # addr_date = item[4].value
        # if addr_date:
        #     addr_date=re.split('-',addr_date)[1]
        #     addr_date=re.sub(r'\.','-',addr_date,2)+' 00:00:00'
        #     addr_date=datetime.strptime(addr_date,'%Y-%m-%d %H:%M:%S')
        #     print(addr_date)
        c_start = item[5].value
        c_end = item[6].value
        if code:
            #todo 增加判断是不是存在
            is_company=db.query("""
                select company from t_customer where company=%s
            """,company)
            #todo 获取会计的uid
            if is_company:
                uid=db.query("""
                        select id from db_income2.t_user where name=%s
                    """,kj)
                if uid:
                    db.execute("""
                UPDATE t_customer set acc_uid_name=%s, acc_uid=%s where company=%s
                """,kj,uid[0]['id'],company)
            else:
                if company!=None and "公司" in company:
                    uid=db.query("""
                        select id from db_income2.t_user where name=%s
                    """,kj)
                    if uid:
                        db.execute("""
                        INSERT INTO `t_customer` ( `id`,`company`, `reg_addr`, `reg_tel`, `reg_number`, `reg_person`, `reg_bank`, `reg_bank_account`, `addr_type`, `addr_expire`, `addr_cp`, `acc_uid`, `acc_uid_name`, `created_at`, `updated_at`, `guid`, `remark`, `reg_date`, `end_date`, `saic`, `national_tax`, `land_tax`, `company_reguid`, `industry_name`, `is_general`, `credit_rating`, `customer_rating`, `credit_rating_name`, `customer_rating_name`, `updated_at_name`, `customer_type`, `customer_type_name`, `uid`, `uid_name`, `acc_uid_at`)
                        VALUES
                            (%s,%s, '', '', '', '', '', '', '', NULL, '', %s, %s,now(), now(), uuid(), NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, now());
                        """,code,company,uid[0]['id'],kj)

                    try:
                        if '年' in c_start:
                            c_start=re.sub(u"[\u4e00-\u9fa5]",'-',c_start)+'-1 00:00:00'
                            c_start=datetime.strptime(c_start,'%Y-%m-%d %H:%M:%S')
                            print(c_start)
                        if '年' in c_end: 
                            c_end=re.sub(u"[\u4e00-\u9fa5]",'-',c_end)+'-1 00:00:00'
                            c_end=datetime.strptime(c_end,'%Y-%m-%d %H:%M:%S')
                            print(c_end)
                    except:
                        pass
                       
                    if isinstance(c_start,datetime) and isinstance(c_end,datetime):
                        db.execute("""
                            INSERT INTO t_contract(customer_id,guid,title,start_time,end_time,updated_at)
                            VALUES(%s,uuid(),'记账合同',%s,%s,now())
                            """,code,c_start,c_end)
                    if  isinstance(c_start,datetime):
                        if isinstance(c_end,datetime)==False:
                            db.execute("""
                                INSERT INTO t_contract(customer_id,guid,title,start_time,updated_at)
                                VALUES(%s,uuid(),'记账合同',%s,now())
                                """,code,c_start)
                    if  isinstance(c_end,datetime): 
                        if isinstance(c_start,datetime)==False:
                            db.execute("""
                                INSERT INTO t_contract(customer_id,guid,title,end_time,updated_at)
                                VALUES(%s,uuid(),'记账合同',%s,now())
                                """,code,c_end)
                    if  isinstance(c_start,datetime)==False:
                        if isinstance(c_end,datetime)==False:
                            db.execute("""
                                INSERT INTO t_contract(customer_id,guid,title,updated_at)
                                VALUES(%s,uuid(),'记账合同',now())
                                """,code)



