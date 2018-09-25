#-*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
import openpyxl
import torndb
import re
from datetime import datetime
from decimal import Decimal
db = torndb.Connection("192.168.2.168", "db_income2","root","deng")
t_projects=db.query('''
                select a.id,a.created_at,a.busniess_from_id_name,a.all_income
                ,b.member_id,b.member_name from t_projects a
                inner join t_projects_member b on b.project_id=a.id and 
                b.team_name='客服顾问' and b.member_id<>0  where a.all_income>0
            ''')
          
for item in t_projects:
    is_exit=db.get('''
        select * from t_kf_count where project_id=%s
        ''',item.id)
    if not is_exit:
        db.execute('''
                insert into t_kf_count(uid,uid_name,created_at,project_id,busniess_from_id_name,all_income) 
                values(%s,%s,%s,%s,%s,%s)
                ''',item.member_id,item.member_name,
            item.created_at,item.id,item.busniess_from_id_name,item.all_income)

t_projects1=db.query('''
                select a.id,a.created_at,b.member_id,b.member_name from t_projects a
                 inner join t_projects_member b 
                 on a.id=b.project_id and b.team_id=38 and b.member_id<>0
            ''')
for item in t_projects1:
    is_exit=db.query('''
            select * from t_gs_count where project_id=%s''',item.id)
    if not is_exit:
        db.execute('''
                insert into t_gs_count(uid,uid_name,created_at,project_id)
                values(%s,%s,%s,%s)''',item.member_id,item.member_name,item.created_at,item.id)