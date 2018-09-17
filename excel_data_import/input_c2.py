#-*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
import openpyxl
import torndb
import re
import uuid,time
from datetime import datetime
from decimal import Decimal
db = torndb.Connection("192.168.2.169", "","root","deng")
wb = openpyxl.load_workbook(u"111.xlsx",data_only=True)
#print wb.get_sheet_names()
product_sheet =wb.get_sheet_by_name(u'楼盘客户')
i = 0
def is_valid_date(strdate):
    '''判断是否是一个有效的日期字符串'''
    dd=''
    try:
        if "年" in strdate:
            dd=strdate.split('年')[0]+'-'+strdate.split('年')[1]+'-01 00:00:00'
            time.strptime(dd,"%Y-%m-%d %H:%M:%S")
            
        elif '.' in strdate:
            dd=strdate.split('.')[0]+'-'+strdate.split('.')[1]+'-'+strdate.split('.')[2]+' 00:00:00'
            time.strptime(dd,"%Y-%m-%d %H:%M:%S")
            
        else:
            time.strptime(strdate, "%Y-%m-%d %H:%M:%S")
        return True,dd
    except:
        return False,dd
companys=['=======客户系统没有找到公司名=======']
types=[['=======付费方式不明确=======']]
types_status=['=======不存在的月付=======']
result=''
for item in product_sheet:
        sp_id=0
        i = i+1
        lines=[1,2,3]

        if i in lines:
            continue  # 跳过第一行
        company = item[2].value
        pay_type= item[3].value
        service_amount=item[4].value
        service_month_amount=item[5].value
        book_amount=item[6].value
        acc_end=item[7].value
        acc_book_end=item[8].value
        reg_date=item[10].value
        hetong_start=item[11].value
        hetong_end=item[12].value
        al_remark=item[13].value
        guid = uuid.uuid4()
        if is_valid_date(str(acc_end))[0]:
            if is_valid_date(str(acc_end))[1]:
                acc_end=is_valid_date(str(acc_end))[1]
        else:
            acc_end=None

        if is_valid_date(str(acc_book_end))[0]:
            if is_valid_date(str(acc_book_end))[1]:
                acc_book_end=is_valid_date(str(acc_book_end))[1]
        else:
            acc_book_end=None
     
        if is_valid_date(str(hetong_start))[0]:
            if is_valid_date(str(hetong_start))[1]:
                hetong_start=is_valid_date(str(hetong_start))[1]
        else:
            hetong_start=None
        
        if is_valid_date(str(hetong_end))[0]:
            if is_valid_date(str(hetong_end))[1]:
                hetong_end=is_valid_date(str(hetong_end))[1]
        else:
            hetong_end=None
        if is_valid_date(str(reg_date))[0]:
            if is_valid_date(str(reg_date))[1]:
                reg_date=is_valid_date(str(reg_date))[1]
        else:
            reg_date=None
        if not str(book_amount).isdigit():
            book_amount=0
        if company:
            if '-' in company:
                company=company.split('-')[1]
        t_customer=db.get('''
        select * from t_customer where company=%s
        ''',company)
        if t_customer:
            if service_month_amount in ['注销中','逾期','停账']:
                pass
            elif str(service_month_amount).isdigit() or '=' in str(service_month_amount):
                service_month_amount='正常'
            t_pyte_status=db.get('''
                select * from t_type where tag='付费方式' and name=%s
            ''',service_month_amount)
    
            if not t_pyte_status:
                types_status.append(service_month_amount)
                
            t_pyte=db.get('''
                select * from t_type where tag='付费方式' and name=%s
            ''',pay_type)
            if not t_pyte:
                pay_type='无'
                types.append([company,service_month_amount])
            else:
                service_month_amount=format(float(service_amount)/float(t_pyte.fee),'.2f')
            if t_pyte and t_pyte_status:
                exit_customer=db.get('''
                    select * from t_customer where paytype_id=%s and id=%s and paytype_status_id=%s and paytype_status_id_name=%s
                ''',t_pyte.id,t_customer.id,t_pyte_status.id,t_pyte_status.name)
                exit_customer_payment=db.get('''
                    select * from t_customer_payment where  pay_typeid=%s and customer_id=%s 
                ''',t_pyte.id,t_customer.id)
                if  hetong_start and hetong_end:
                    exit_contract=db.get('''
                        select * from t_contract where customer_id=%s and title=%s and start_time=%s and end_time=%s and uid=0
                    ''',t_customer.id,'记账合同',hetong_start,hetong_end)
                elif not hetong_start and hetong_end:
                    exit_contract=db.get('''
                        select * from t_contract where customer_id=%s and title=%s and end_time=%s and start_time is null and uid=0
                    ''',t_customer.id,'记账合同',hetong_end)
                elif  hetong_start and not hetong_end:
                    exit_contract=db.get('''
                        select * from t_contract where customer_id=%s and title=%s and  start_time=%s and end_time is null and uid=0
                    ''',t_customer.id,'记账合同',hetong_start)
                if not exit_customer:
                    result=db.execute('''
                        update t_customer set paytype_id=%s,paytype_id_name=%s,fee=%s,service_amount=%s,
                        service_month_amount=%s,book_amount=%s,paytype_status_id=%s,paytype_status_id_name=%s,reg_date=%s where company=%s
                    ''',t_pyte.id,t_pyte.name,t_pyte.fee,service_amount,
                    service_month_amount,book_amount,t_pyte_status.id,t_pyte_status.name,reg_date,company)
                    if result==0:
                        print('t_customer '+company+' 写入成功')
                    else:
                        print('t_customer '+company+' 写入失败')
                if not exit_customer_payment:
                    result=db.execute('''
                        insert into t_customer_payment
                        (customer_id,pay_typeid,pay_typeid_name,service_amount,
                        service_month_amount,book_amount,acc_end,acc_book_end,created_at,fee,al_remark)
                        values(%s,%s,%s,%s,%s,%s,%s,%s,now(),%s,%s)
                    ''',t_customer.id,t_pyte.id,t_pyte.name,service_amount,service_month_amount,
                    book_amount,acc_end,acc_book_end,t_pyte.fee,al_remark)
                    if result>0:
                        print('t_customer_payment '+company+' 写入成功')
                    else:
                        print('t_customer_payment '+company+' 写入失败')
                if not exit_contract:
                    result=db.execute('''
                        insert into t_contract(customer_id,guid,title,start_time,end_time,updated_at,uid)
                        values(%s,%s,%s,%s,%s,now(),%s)''',t_customer.id,guid,'记账合同',hetong_start,hetong_end,0)
                    if result>0:
                        print('t_contract '+company+' 写入成功')
                    else:
                        print('t_contract '+company+' 写入失败')
                
            
        else:
            companys.append(company)
for item in companys:
    print(item)
for item in types:
    for row in item:
        print(row)
for item in types_status:
    print(item)
        