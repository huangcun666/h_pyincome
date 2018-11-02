# encoding=utf8
from handlers.base import BaseHandler
import logging
import json
import tornado.web
import urllib2
import tornado.httpclient
import sys, re,os,uuid
import urllib,datetime

reload(sys)
from tornado.options import define, options
sys.setdefaultencoding('utf8')
from Pagination import Pagination
from dateutil import rrule
from calendar import monthrange
import datetime

logger = logging.getLogger('boilerplate.' + __name__)

class StatisHandler(BaseHandler):

    def workdays(self,start, end, holidays=0, days_off=None):
        if days_off is None:
            days_off = 5, 6
        workdays = [x for x in range(7) if x not in days_off]
        days = rrule.rrule(rrule.DAILY, dtstart=start,until=end, byweekday=workdays)
        return days.count() - holidays


    def get_datetime_range(self,year, month):
        nb_days = monthrange(year, month)[1]
        return [datetime.date(year, month, day) for day in range(1, nb_days + 1)]

    @tornado.web.authenticated
    def get(self):
        tag = self.get_argument("tag", "list")
        uid_name= self.get_secure_cookie('name')
        dt = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        dt_last =datetime.datetime.now().strftime("%Y-12-31 23:59:59")
        #statis_cq_work_month

        if tag =="statis_cq_work_month":
            pre_page = 30
            keyword = self.get_argument("key", "")
            gw = self.get_argument("gw","")
            type_id = self.get_argument("type_id", "")
            role = self.get_argument("role",13)
            btype_id = self.get_argument("btype_id","")
            start = self.get_argument(
                "start",
                datetime.datetime.now().strftime("%Y-01-01 00:00:00"))
            end = self.get_argument(
                "end",
                 datetime.datetime.now().strftime("%Y-12-31 23:59:59"))
            params = {
                "start": start,
                "end": end,
                "gw": gw,
                "key": keyword,
                "type_id": type_id,
                "tag": tag,
                "role": role,
                "datatype":"month",
                "datatype_name":"月报",
                "btype_id":btype_id
            }
            page = int(self.get_argument("page", 1))
            add_sql = " where created_at between  '%s' and '%s' " % (
                start, end)

            if type_id:
                add_sql += " and  busniess_from_id = %s"%(type_id)
            if gw and gw != "0" :
                add_sql += " and uid = %s " % (gw)
            if btype_id:
                add_sql += " and  btype_id = %s "%(btype_id)
            print add_sql
            count = self.db.get('''select  count(*) count from (
                 select ct ,GROUP_CONCAT( uid_name,"|",gc1) gc from
 (select  DATE_FORMAT(created_at,'%%Y-%%m') ct,uid_name , sum(project_count) gc1
               from t_statis_cq_work
                 ''' + add_sql + '''
                  group by
                 DATE_FORMAT(created_at,'%%Y-%%m'),uid_name
                 ) b group by ct order by ct desc
                    ) count
                    ''')
            pagination = Pagination(page, pre_page, count.count, self.request)
            startpage = (page-1) * pre_page
            dt = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            t_statis_kf = self.db.query('''
                select ct ,GROUP_CONCAT( uid_name,"|",gc1) gc from
 (select  DATE_FORMAT(created_at,'%%Y-%%m') ct,uid_name , sum(project_count) gc1
               from t_statis_cq_work
                                ''' + add_sql + '''
                 group by
                 DATE_FORMAT(created_at,'%%Y-%%m'),uid_name
                 ) b group by ct order by ct desc

                ''')
            t_statis_kf_total = self.db.query(
                '''      select uid_name, sum(project_count) total_income
               from t_statis_cq_work
               ''' + add_sql + '''     group by uid_name

                ''')



            t_kf = self.db.query("""
                select uid ,uid_name from t_statis_cq_work   """+add_sql+""" group by uid_name,uid
            """)
            btype = self.db.query ("select * from t_projects_type where income_category='业务来源'")
            project_btype = self.db.query ("select btype_id ,btype_name from t_statis_cq_work  "+add_sql+" group by btype_id ,btype_name")

            # t_user_gw = self.db.query(
            #     "SELECT * FROM t_user_teams a , t_user b where b.id=a.uid and team_id=2 "
            # )
            t_statis_cq_total_day = self.db.query(
                '''
                select   DATE_FORMAT(created_at,'%%Y-%%m') ct, sum(project_count) gc1
               from t_statis_cq_work
                ''' + add_sql + '''
                 group by
                  DATE_FORMAT(created_at,'%%Y-%%m')
                ''')

            t_statis_cq_total_day_all = self.db.get(
                '''
                select sum(project_count)  gc1
               from t_statis_cq_work
                ''' + add_sql + '''
                ''')
            return self.render(
                'statis/statis_cq_work.html',
                t_statis_cq_total_day=t_statis_cq_total_day,
                t_statis_cq_total_day_all=t_statis_cq_total_day_all,
                t_statis_kf_total=t_statis_kf_total,
                # t_user_gw=t_user_gw,
                btype=btype,
                project_btype=project_btype,
                t_kf=t_kf,
                dt=datetime.datetime.now(),
                params=params,
                user_name=uid_name,
                pagination=pagination,
                t_statis_kf=t_statis_kf,
                search_key="",
                )
        
        elif tag=="statis_project_detail":
            step=self.get_argument('step','')
            type=self.get_argument('type','')
            date_type=self.get_argument('date_type','')
            page = int(self.get_argument("page", 1))
            pre_page=20
            params={
                'step':step,
                'type':type,
                'date_type':date_type
            }
            sql=''
            if type:
                sql=' where  service_name="%s" '%type
            t_projects_type=self.db.query('''
                select income_name from t_projects_type where income_category='业务类型'
             ''')
            t_account_names=self.db.query('''
                select uid_name,sum(all_money) ta,sum(all_count) ac from t_account_project_detail '''+sql+''' group by uid_name
            ''')

            if step in ['2','3']:
                count=self.db.get('''
                    select count(*) count
                    from  (select count(*) from t_account_project_detail '''+sql+''' group by created_at )  count
                ''')
                pagination = Pagination(page, pre_page, count.count, self.request)
                startpage = (page-1) * pre_page
                t_account_project_detail=self.db.query('''
                    select ct,GROUP_CONCAT( uid_name,"|",all_money,'|',all_count) tapd ,sum(all_money) am,sum(all_count) ac
                    from (select DATE_FORMAT(created_at,'%%Y-%%m-%%d') ct,all_money, uid_name,all_count,service_name from t_account_project_detail '''+sql+''') b
                    group by ct order by ct desc limit %s,%s
                ''',startpage,pre_page)
            else:
                if date_type=='month':
                    dd=" DATE_FORMAT(created_at,'%%Y-%%m') "
                elif date_type=='day':
                    dd=" DATE_FORMAT(created_at,'%%Y-%%m-%%d') "
                count=self.db.get('''
                    select count(*) count
                    from  (select count(*) from t_account_project_detail  group by '''+dd+''' )  count
                ''')
                pagination = Pagination(page, pre_page, count.count, self.request)
                startpage = (page-1) * pre_page
                t_account_project_detail=self.db.query('''
                    select ct,service_name,GROUP_CONCAT( service_name,"|",all_moneys,'|',all_counts) tapd,
                     sum(all_moneys) am,sum(all_counts) ac
                    from(select service_name,sum(all_money) all_moneys,'''+dd+''' ct ,
                    sum(all_count) all_counts
                    from t_account_project_detail group by '''+dd+''',service_name) bb
                    group by ct order by ct desc limit %s,%s
                ''',startpage,pre_page)
            t_account_project_detail_type_all=self.db.query('''
                    select sum(all_money) am,sum(all_count) ac,service_name
                from t_account_project_detail group by service_name
                ''')
            t_account_project_detail_all=self.db.get('''
                    select sum(all_money) tapda,sum(all_count) ac
                from t_account_project_detail
                '''+sql)
            self.render(
                'statis/statis_project_detail.html',
                search_key="",
                params=params,
                t_account_project_detail_type_all=t_account_project_detail_type_all,
                t_projects_type=t_projects_type,
                t_account_names=t_account_names,
                t_account_project_detail_all=t_account_project_detail_all,
                t_account_project_detail=t_account_project_detail,
                pagination=pagination
            )

        elif tag =="statis_cq_building_month":
            pre_page = 30
            keyword = self.get_argument("key", "")
            gw = self.get_argument("gw","")
            type_id = self.get_argument("type_id", "")
            role = self.get_argument("role",13)
            btype_id = self.get_argument("btype_id","")
            start = self.get_argument(
                "start",
                datetime.datetime.now().strftime("%Y-01-01 00:00:00"))
            end = self.get_argument(
                "end",
                datetime.datetime.now().strftime("%Y-12-30 23:59:59"))
            params = {
                "start": start,
                "end": end,
                "gw": gw,
                "key": keyword,
                "type_id": type_id,
                "tag": tag,
                "role": role,
                "datatype":"day",
                "datatype_name":"日报",
                "btype_id":btype_id
            }
            page = int(self.get_argument("page", 1))
            add_sql = " where created_at between  '%s' and '%s' " % (
                start, end)

            if type_id:
                add_sql += " and  busniess_from_id = %s"%(type_id)
            if gw and gw != "0" :
                add_sql += " and uid = %s " % (gw)
            if btype_id:
                add_sql += " and  btype_id = %s "%(btype_id)
            print add_sql
            count = self.db_building.get('''select  count(*) count from (
                 select ct ,GROUP_CONCAT( uid_name,"|",gc1) gc from
 (select  DATE_FORMAT(created_at,'%%Y-%%m') ct,uid_name ,sum(project_count) gc1
               from t_statis_cq_work
                 ''' + add_sql + '''
                  group by
                DATE_FORMAT(created_at,'%%Y-%%m'),uid_name
                 ) b group by ct order by ct desc
                    ) count
                    ''')
            pagination = Pagination(page, pre_page, count.count, self.request)
            startpage = (page-1) * pre_page
            dt = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            t_statis_kf = self.db_building.query('''
                select ct ,GROUP_CONCAT( uid_name,"|",gc1) gc from
 (select  DATE_FORMAT(created_at,'%%Y-%%m') ct,uid_name ,sum(project_count)  gc1
               from t_statis_cq_work
                                ''' + add_sql + '''
                 group by
                 DATE_FORMAT(created_at,'%%Y-%%m'),uid_name
                 ) b group by ct order by ct desc


                ''')
            t_statis_kf_total = self.db_building.query(
                '''      select uid_name,count(*) total_income
               from t_statis_cq_work
               ''' + add_sql + '''     group by uid_name

                ''')



            t_kf = self.db_building.query("""
                select uid ,uid_name from t_statis_cq_work   """+add_sql+""" group by uid_name,uid
            """)

            # t_user_gw = self.db.query(
            #     "SELECT * FROM t_user_teams a , t_user b where b.id=a.uid and team_id=2 "
            # )

            t_statis_cq_total_day = self.db_building.query(
                '''
                select   DATE_FORMAT(created_at,'%%Y-%%m') ct,sum(project_count)  gc1
               from t_statis_cq_work
                ''' + add_sql + '''
                 group by
                  DATE_FORMAT(created_at,'%%Y-%%m')
                ''')

            t_statis_cq_total_day_all = self.db_building.get(
                '''
                select sum(project_count)   gc1
               from t_statis_cq_work
                ''' + add_sql + '''
                ''')
            return self.render(
                'statis/statis_cq_building.html',
                t_statis_cq_total_day=t_statis_cq_total_day,
                t_statis_cq_total_day_all=t_statis_cq_total_day_all,
                t_statis_kf_total=t_statis_kf_total,
                # t_user_gw=t_user_gw,
                t_kf=t_kf,
                dt=datetime.datetime.now(),
                params=params,
                user_name=uid_name,
                pagination=pagination,
                t_statis_kf=t_statis_kf,
                search_key="",
                )
        elif tag =="statis_cq_building":
            pre_page = 30
            keyword = self.get_argument("key", "")
            gw = self.get_argument("gw","")
            type_id = self.get_argument("type_id", "")
            role = self.get_argument("role",13)
            btype_id = self.get_argument("btype_id","")
            start = self.get_argument(
                "start",
                datetime.datetime.now().strftime("%Y-%m-01 00:00:00"))
            end = self.get_argument(
                "end",
                datetime.datetime.now().strftime("%Y-%m-30 23:59:59"))
            params = {
                "start": start,
                "end": end,
                "gw": gw,
                "key": keyword,
                "type_id": type_id,
                "tag": tag,
                "role": role,
                "datatype":"day",
                "datatype_name":"日报",
                "btype_id":btype_id
            }
            page = int(self.get_argument("page", 1))
            add_sql = " where created_at between  '%s' and '%s' " % (
                start, end)

            if type_id:
                add_sql += " and  busniess_from_id = %s"%(type_id)
            if gw and gw != "0" :
                add_sql += " and uid = %s " % (gw)
            if btype_id:
                add_sql += " and  btype_id = %s "%(btype_id)
            print add_sql
            count = self.db_building.get('''select  count(*) count from (
                 select ct ,GROUP_CONCAT( uid_name,"|",gc1) gc from
 (select  date(created_at) ct,uid_name ,sum(project_count)  gc1
               from t_statis_cq_work
                 ''' + add_sql + '''
                  group by
                 date(created_at),uid_name
                 ) b group by ct order by ct desc
                    ) count
                    ''')
            pagination = Pagination(page, pre_page, count.count, self.request)
            startpage = (page-1) * pre_page
            dt = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            t_statis_kf = self.db_building.query('''
                select ct ,GROUP_CONCAT( uid_name,"|",gc1) gc from
 (select  date(created_at) ct,uid_name ,sum(project_count) gc1
               from t_statis_cq_work
                                ''' + add_sql + '''
                 group by
                 date(created_at),uid_name
                 ) b group by ct order by ct desc


                ''')
            t_statis_kf_total = self.db_building.query(
                '''      select uid_name,sum(project_count)  total_income
               from t_statis_cq_work
               ''' + add_sql + '''     group by uid_name

                ''')



            t_kf = self.db_building.query("""
                select uid ,uid_name from t_statis_cq_work   """+add_sql+""" group by uid_name,uid
            """)
            btype = self.db.query ("select * from t_projects_type where income_category='业务来源'")

            # t_user_gw = self.db.query(
            #     "SELECT * FROM t_user_teams a , t_user b where b.id=a.uid and team_id=2 "
            # )
            t_statis_cq_total_day = self.db_building.query(
                '''
                select   date(created_at) ct,sum(project_count)  gc1
               from t_statis_cq_work
                ''' + add_sql + '''
                 group by
                  date(created_at)
                ''')

            t_statis_cq_total_day_all = self.db_building.get(
                '''
                select sum(project_count)   gc1
               from t_statis_cq_work
                ''' + add_sql + '''
                ''')
            return self.render(
                'statis/statis_cq_building.html',
                t_statis_cq_total_day=t_statis_cq_total_day,
                t_statis_cq_total_day_all=t_statis_cq_total_day_all,
                t_statis_kf_total=t_statis_kf_total,
                # t_user_gw=t_user_gw,
                btype=btype,
                t_kf=t_kf,
                dt=datetime.datetime.now(),
                params=params,
                user_name=uid_name,
                pagination=pagination,
                t_statis_kf=t_statis_kf,
                search_key="",
                )
        elif tag =="statis_cq_work":
            pre_page = 30
            keyword = self.get_argument("key", "")
            gw = self.get_argument("gw","")
            type_id = self.get_argument("type_id", "")
            role = self.get_argument("role",13)
            btype_id = self.get_argument("btype_id","")
            start = self.get_argument(
                "start",
                datetime.datetime.now().strftime("%Y-%m-01 00:00:00"))
            end = self.get_argument(
                "end",
                datetime.datetime.now().strftime("%Y-%m-30 23:59:59"))
            params = {
                "start": start,
                "end": end,
                "gw": gw,
                "key": keyword,
                "type_id": type_id,
                "tag": tag,
                "role": role,
                "datatype":"month",
                "datatype_name":"月报",
                "btype_id":btype_id
            }
            page = int(self.get_argument("page", 1))
            add_sql = " where created_at between  '%s' and '%s' " % (
                start, end)

            if type_id and type_id!="0":
                add_sql += " and  busniess_from_id = %s"%(type_id)
            if gw and gw != "0" :
                add_sql += " and uid = %s " % (gw)
            if btype_id and btype_id!="0":
                add_sql += " and  btype_id = %s "%(btype_id)
            print add_sql
            count = self.db.get('''select  count(*) count from (
                 select ct ,GROUP_CONCAT( uid_name,"|",gc1) gc from
 (select  date(created_at) ct,uid_name ,sum(project_count) gc1
               from t_statis_cq_work
                 ''' + add_sql + '''
                  group by
                 date(created_at),uid_name
                 ) b group by ct order by ct desc
                    ) count
                    ''')
            pagination = Pagination(page, pre_page, count.count, self.request)
            startpage = (page-1) * pre_page
            dt = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            t_statis_kf = self.db.query('''
                select ct ,GROUP_CONCAT( uid_name,"|",gc1) gc from
 (select  date(created_at) ct,uid_name ,sum(project_count) gc1
               from t_statis_cq_work
                                ''' + add_sql + '''
                 group by
                 date(created_at),uid_name
                 ) b group by ct order by ct desc


                ''')
            t_statis_kf_total = self.db.query(
                '''      select uid_name,sum(project_count) total_income
               from t_statis_cq_work
               ''' + add_sql + '''     group by uid_name

                ''')



            t_kf = self.db.query("""
                select uid ,uid_name from t_statis_cq_work   """+add_sql+""" group by uid_name,uid
            """)
            btype = self.db.query ("select * from t_projects_type where income_category='业务来源'")
            project_btype = self.db.query ("select btype_id ,btype_name from t_statis_cq_work  "+add_sql+" group by btype_id ,btype_name")

            # t_user_gw = self.db.query(
            #     "SELECT * FROM t_user_teams a , t_user b where b.id=a.uid and team_id=2 "
            # )

            t_statis_cq_total_day = self.db.query(
                '''
                select   date(created_at) ct,sum(project_count) gc1
               from t_statis_cq_work
                ''' + add_sql + '''
                 group by
                  date(created_at)
                ''')

            t_statis_cq_total_day_all = self.db.get(
                '''
                select sum(project_count)  gc1
               from t_statis_cq_work
                ''' + add_sql + '''
                ''')
            return self.render(
                'statis/statis_cq_work.html',
                t_statis_cq_total_day=t_statis_cq_total_day,
                t_statis_cq_total_day_all=t_statis_cq_total_day_all,
                t_statis_kf_total=t_statis_kf_total,
                # t_user_gw=t_user_gw,
                btype=btype,
                project_btype=project_btype,
                t_kf=t_kf,
                dt=datetime.datetime.now(),
                params=params,
                user_name=uid_name,
                pagination=pagination,
                t_statis_kf=t_statis_kf,
                search_key="",
                )
        elif tag =="statis_cq":
            pre_page = 31
            keyword = self.get_argument("key", "")
            gw = self.get_argument("gw","")
            type_id = self.get_argument("type_id", "")
            btype_id = self.get_argument("btype_id","")
            start = self.get_argument(
                "start",
                datetime.datetime.now().strftime("%Y-%m-01 00:00:00"))
            end = self.get_argument(
                "end",
                datetime.datetime.now().strftime("%Y-%m-30 23:59:59"))
            params = {
                "start": start,
                "end": end,
                "gw": gw,
                "key": keyword,
                "type_id": type_id,
                "tag": tag,
                "datatype":"day",
                "datatype_name":"日报",
                "btype_id":btype_id
            }
            page = int(self.get_argument("page", 1))
            add_sql = " where confirm_at between  '%s' and '%s' " % (
                start, end)

            if type_id and type_id!="0":
                add_sql += " and  busniess_from_id = %s"%(type_id)
            if gw and gw != "0" :
                add_sql += " and uid = %s " % (gw)
            if btype_id and btype_id!="0":
                add_sql += " and  btype_id = %s "%(btype_id)
            print add_sql
            count = self.db.get('''select  count(*) count from (
              select ct ,GROUP_CONCAT( uid_name,"|",gc1) gc from
 (select  date(confirm_at) ct,uid_name ,count(*) gc1
               from t_statis_cq
                 ''' + add_sql + '''
                 group by
                 date(confirm_at),uid_name
                 ) b group by ct order by ct desc
                    ) count
                    ''')
            pagination = Pagination(page, pre_page, count.count, self.request)
            startpage = (page-1) * pre_page
            dt = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            t_statis_kf = self.db.query('''
            select ct ,GROUP_CONCAT( uid_name,"|",gc1) gc from
 (select  date(confirm_at) ct,uid_name ,count(*) gc1
               from t_statis_cq
                 ''' + add_sql + '''
                 group by
                 date(confirm_at),uid_name
                 ) b group by ct order by ct desc

                ''')
            t_statis_kf_total = self.db.query(
                '''      select uid_name,count(*) total_income
               from t_statis_cq
               ''' + add_sql + '''     group by uid_name

                ''')



            t_kf = self.db.query("""
                select uid ,uid_name from t_statis_cq   """+add_sql+""" group by uid_name,uid
            """)
            btype = self.db.query ("select * from t_projects_type where income_category='业务来源'")
            project_btype = self.db.query ("select btype_id ,btype_name from t_statis_cq  "+add_sql+" group by btype_id ,btype_name")

            # t_user_gw = self.db.query(
            #     "SELECT * FROM t_user_teams a , t_user b where b.id=a.uid and team_id=2 "
            # )
            t_statis_cq_total_day = self.db.query(
                '''
                select   date(confirm_at) ct,count(*) gc1
               from t_statis_cq
                ''' + add_sql + '''
                 group by
                  date(confirm_at)
                ''')

            t_statis_cq_total_day_all = self.db.get(
                '''
                select count(*)  gc1
               from t_statis_cq
                ''' + add_sql + '''
                ''')
            return self.render(
                'statis/statis_cq.html',
                t_statis_kf_total=t_statis_kf_total,
                t_statis_cq_total_day=t_statis_cq_total_day,
                t_statis_cq_total_day_all=t_statis_cq_total_day_all,
                # t_user_gw=t_user_gw,
                btype=btype,
                project_btype=project_btype,
                t_kf=t_kf,
                dt=datetime.datetime.now(),
                params=params,
                user_name=uid_name,
                pagination=pagination,
                t_statis_kf=t_statis_kf,
                search_key="",
                )
        elif tag =="statis_cq_month":
            pre_page = 31
            keyword = self.get_argument("key", "")
            gw = self.get_argument("gw","")
            type_id = self.get_argument("type_id", "")
            role = self.get_argument("role",13)
            btype_id = self.get_argument("btype_id","")
            start = self.get_argument(
                "start",
                datetime.datetime.now().strftime("%Y-01-01 00:00:00"))
            end = self.get_argument(
                "end",
                datetime.datetime.now().strftime("%Y-12-31 23:59:59"))
            params = {
                "start": start,
                "end": end,
                "gw": gw,
                "key": keyword,
                "type_id": type_id,
                "tag": tag,
                "role": role,
                "datatype":"month",
                "datatype_name":"月报",
                "btype_id":btype_id
            }
            page = int(self.get_argument("page", 1))
            add_sql = " where confirm_at between  '%s' and '%s' " % (
                start, end)

            if type_id and type_id!="0":
                add_sql += " and  busniess_from_id = %s"%(type_id)
            if gw and gw != "0" :
                add_sql += " and uid = %s " % (gw)
            if btype_id and btype_id!="0":
                add_sql += " and  btype_id = %s "%(btype_id)
            print add_sql
            count = self.db.get('''select  count(*) count from (
              select ct ,GROUP_CONCAT( uid_name,"|",gc1) gc from
 (select   DATE_FORMAT(confirm_at,'%%Y-%%m')  ct,uid_name ,count(*) gc1
               from t_statis_cq
                 ''' + add_sql + '''
                 group by
                 date(confirm_at),uid_name
                 ) b group by ct order by ct desc
                    ) count
                    ''')
            pagination = Pagination(page, pre_page, count.count, self.request)
            startpage = (page-1) * pre_page
            dt = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            t_statis_kf = self.db.query('''
            select ct ,GROUP_CONCAT( uid_name,"|",gc1) gc from
            (select  DATE_FORMAT(confirm_at,'%%Y-%%m')  ct,uid_name ,count(*) gc1
               from t_statis_cq
                 ''' + add_sql + '''
                 group by
                  DATE_FORMAT(confirm_at,'%%Y-%%m'), uid_name
                 ) b group by ct order by ct desc

                ''')
            t_statis_kf_total = self.db.query(
                '''      select uid_name,count(*) total_income
               from t_statis_cq
               ''' + add_sql + '''     group by uid_name

                ''')



            t_kf = self.db.query("""
                select uid ,uid_name from t_statis_cq   """+add_sql+""" group by uid_name,uid
            """)
            btype = self.db.query ("select * from t_projects_type where income_category='业务来源'")
            # t_user_gw = self.db.query(
            #     "SELECT * FROM t_user_teams a , t_user b where b.id=a.uid and team_id=2 "
            # )
            project_btype = self.db.query ("select btype_id ,btype_name from t_statis_cq  "+add_sql+" group by btype_id ,btype_name")
            t_statis_cq_total_day = self.db.query(
                '''
                select   DATE_FORMAT(confirm_at,'%%Y-%%m') ct,count(*) gc1
               from t_statis_cq
                ''' + add_sql + '''
                 group by
                  DATE_FORMAT(confirm_at,'%%Y-%%m')
                ''')

            t_statis_cq_total_day_all = self.db.get(
                '''
                select count(*)  gc1
               from t_statis_cq
                ''' + add_sql + '''
                ''')
            return self.render(
                'statis/statis_cq.html',
                t_statis_cq_total_day=t_statis_cq_total_day,
                t_statis_cq_total_day_all=t_statis_cq_total_day_all,
                project_btype=project_btype,
                t_statis_kf_total=t_statis_kf_total,
                # t_user_gw=t_user_gw,
                btype=btype,
                t_kf=t_kf,
                dt=datetime.datetime.now(),
                params=params,
                user_name=uid_name,
                pagination=pagination,
                t_statis_kf=t_statis_kf,
                search_key="",
                )
        elif tag =="statis_kf_month":
            pre_page = 12
            keyword = self.get_argument("key", "")
            gw = self.get_argument("gw","")
            type_id = self.get_argument("type_id", "")
            role = self.get_argument("role",13)


            start = self.get_argument(
                "start",
                datetime.datetime.now().strftime("%Y-01-01 00:00:00"))
            end = self.get_argument(
                "end",
                datetime.datetime.now().strftime("%Y-12-30 23:59:59"))
            params = {
                "start": start,
                "end": end,
                "gw": gw,
                "key": keyword,
                "type_id": type_id,
                "tag": tag,
                "role": role,
                "datatype":"month",
                "datatype_name":"月报"
            }
            page = int(self.get_argument("page", 1))
            add_sql = " where project_created_at between  '%s' and '%s' " % (
                start, end)

            if type_id and type_id!="0":
                add_sql += " and  busniess_from_id = %s"%(type_id)
            if gw and gw != "0" :
                add_sql += " and uid = %s " % (gw)
            if role:
                add_sql += " and role=%s" % (role)
            count = self.db.get('''select  count(*) count from (
              select DATE_FORMAT(project_created_at,'%%Y-%%m')  ct ,GROUP_CONCAT( uid_name,"|",all_income) gc
               from t_statis_kf '''
                                + add_sql + '''  group by
                DATE_FORMAT(project_created_at,'%%Y-%%m')
                    ) count
                    ''')
            pagination = Pagination(page, pre_page, count.count, self.request)
            startpage = (page-1) * pre_page
            dt = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            t_statis_kf = self.db.query('''
            select ct ,GROUP_CONCAT( uid_name,"|",gc1) gc from (
 select  DATE_FORMAT(project_created_at,'%%Y-%%m') ct,uid_name ,sum(all_income) gc1
               from t_statis_kf
              ''' + add_sql + '''         group by
                 DATE_FORMAT(project_created_at,'%%Y-%%m'),uid_name

                 ) b group by ct order by ct desc

                ''')
            print add_sql
            t_statis_kf_total = self.db.query(
                '''      select uid_name,sum(all_income) total_income
               from t_statis_kf
               ''' + add_sql + '''     group by uid_name

                ''')
            t_statis_kf_total_day = self.db.query(
                '''
                select   DATE_FORMAT(project_created_at,'%%Y-%%m') ct,sum(all_income) gc1
               from t_statis_kf
                ''' + add_sql + '''
                 group by
                  DATE_FORMAT(project_created_at,'%%Y-%%m')

                ''')

            t_statis_kf_total_day_all = self.db.get(
                '''
                select ifnull(sum(all_income),0) gc1
               from t_statis_kf
                ''' + add_sql + '''

                ''')


            t_kf = self.db.query("""
                select uid ,uid_name from t_statis_kf   """+add_sql+""" group by uid_name,uid
            """)
            btype = self.db.query ("select * from t_projects_type where income_category='业务来源'")
            # t_user_gw = self.db.query(
            #     "SELECT * FROM t_user_teams a , t_user b where b.id=a.uid and team_id=2 "
            # )
            return self.render(
                'statis/statis_kf.html',
                t_statis_kf_total=t_statis_kf_total,
                # t_user_gw=t_user_gw,
                t_statis_kf_total_day=t_statis_kf_total_day,
                t_statis_kf_total_day_all=t_statis_kf_total_day_all,
                btype=btype,
                t_kf=t_kf,
                dt=datetime.datetime.now(),
                params=params,
                user_name=uid_name,
                pagination=pagination,
                t_statis_kf=t_statis_kf,
                search_key="",
                )
        elif tag =="statis_kf":
            pre_page = 50
            keyword = self.get_argument("key", "")
            gw = self.get_argument("gw","")
            type_id = self.get_argument("type_id", "")
            role = self.get_argument("role",13)
            start = self.get_argument(
                "start",
                datetime.datetime.now().strftime("%Y-%m-01 00:00:00"))
            end = self.get_argument(
                "end",
                datetime.datetime.now().strftime("%Y-%m-%d 23:59:59"))
            params = {
                "start": start,
                "end": end,
                "gw": gw,
                "key": keyword,
                "type_id": type_id,
                "tag": tag,
                "role": role,
                "datatype":"day",

                "datatype_name":"日报"

            }
            page = int(self.get_argument("page", 1))
            add_sql = " where project_created_at between  '%s' and '%s' " % (
                start, end)

            if type_id and type_id!="0":
                add_sql += " and  busniess_from_id = %s"%(type_id)
            if gw and gw != "0" :
                add_sql += " and uid = %s " % (gw)
            if role:
                add_sql += " and role=%s" % (role)
            count = self.db.get('''select  count(*) count from (
              select  date(project_created_at) ct ,GROUP_CONCAT( uid_name,"|",all_income) gc
               from t_statis_kf '''
                                + add_sql + '''  group by
                 date(project_created_at)
                    ) count
                    ''')
            pagination = Pagination(page, pre_page, count.count, self.request)
            startpage = (page-1) * pre_page
            dt = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            t_statis_kf = self.db.query('''
            select ct ,GROUP_CONCAT( uid_name,"|",gc1) gc from (
 select  date(project_created_at) ct,uid_name ,sum(all_income) gc1
               from t_statis_kf
              ''' + add_sql + '''
                 group by
                 date(project_created_at),uid_name
                 ) b group by ct order by ct desc

                ''')
            t_statis_kf_total = self.db.query(
                '''      select uid_name,sum(all_income) total_income
               from t_statis_kf
               ''' + add_sql + '''     group by uid_name

                ''')
            t_statis_kf_total_day = self.db.query(
                '''
                select  date(project_created_at) ct,sum(all_income) gc1
               from t_statis_kf
                ''' + add_sql + '''
                 group by
                 date(project_created_at)

                ''')

            t_statis_kf_total_day_all = self.db.get(
                '''
                select ifnull(sum(all_income),0) gc1
               from t_statis_kf
                ''' + add_sql + '''

                ''')


            t_kf = self.db.query("""
                select uid ,uid_name from t_statis_kf   """+add_sql+""" group by uid_name,uid
            """)
            btype = self.db.query ("select * from t_projects_type where income_category='业务来源'")
            # t_user_gw = self.db.query(
            #     "SELECT * FROM t_user_teams a , t_user b where b.id=a.uid and team_id=2 "
            # )
            return self.render(
                'statis/statis_kf.html',
                t_statis_kf_total_day_all=t_statis_kf_total_day_all,
                t_statis_kf_total=t_statis_kf_total,
                t_statis_kf_total_day=t_statis_kf_total_day,
                # t_user_gw=t_user_gw,
                btype=btype,
                t_kf=t_kf,
                dt=datetime.datetime.now(),
                params=params,
                user_name=uid_name,
                pagination=pagination,
                t_statis_kf=t_statis_kf,
                search_key="",
                )
        elif tag =="building":
            pre_page = 10
            keyword = self.get_argument("key", "")
            params= {"start":"","end":"","key":keyword}
            page = int(self.get_argument("page", 1))
            addsql=""
            if keyword:
                addsql = ''' and (b.company like "%%'''+keyword+'''%%"    or b.name like "%%'''+keyword+'''%%")'''

            count = self.db_building.get('''

                SELECT count(*) count from t_statis a ,t_customer b,t_user
                    c where a.customer_id=b.id
                    and b.created_uid=c.id and c.name=%s
                    ''' + addsql ,uid_name)
            pagination = Pagination(page, pre_page, count.count, self.request)
            startpage = (page-1) * pre_page
            dt = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            t_customers = self.db_building.query('''
                SELECT  a.*,b.name, b.company,b.tel,c.name building_name,b.guid customer_guid,b.id customer_id from t_statis a ,t_customer b,t_user
                    c where a.customer_id=b.id
                    and b.created_uid=c.id and c.name=%s
                    ''' + addsql + '''
                    order by start_date desc limit %s,%s
                ''',uid_name, startpage, pre_page)
            return self.render(
                'statis/building_trans_v1.html',
                workdays=self.workdays,
                dt=datetime.datetime.now(),
                key=keyword,
                params=params,
                user_name=uid_name,
                pagination=pagination,
                msg="",
                t_customers=t_customers,
                search_key="")
        elif tag =="all_building":
            pre_page = 20
            keyword = self.get_argument("key", "")
            params= {"start":"","end":"","key":keyword}
            page = int(self.get_argument("page", 1))
            todo=self.get_argument('todo','')
            start = self.get_argument("start","")
            end = self.get_argument("end","")
            key = self.get_argument("key","")
            gw=self.get_argument("gw",'')
            params = {"tag":tag,"start":start,"end":end,"key":key,"gw":gw,"todo":todo}

            addsql=""
            if keyword:
                addsql += ''' and (b.company like "%%'''+keyword+'''%%"    or b.name like "%%'''+keyword+'''%%")'''
            if gw:
                addsql+=''' and c.id=%s '''%gw
            if start and end:
                addsql+=''' and a.start_date between '%s' and '%s' '''%(start,end)
            sums=self.db_building.get('''
                    SELECT count(*) a,
                      ( SELECT count(*) count from t_statis a ,t_customer b,t_user
                    c where a.customer_id=b.id
                    and b.created_uid=c.id  and (a.get_openaccount_day_date is null or a.start_date is null)) b,
                    (SELECT count(*) count from t_statis a ,t_customer b,t_user
                    c where a.customer_id=b.id
                    and b.created_uid=c.id  and a.get_openaccount_day_date is not null and a.start_date is not null) c
                     from t_statis aa ,t_customer bb,t_user
                    cc where aa.customer_id=bb.id
                    and bb.created_uid=cc.id
            ''')
            t_kf =self.db_building.query('''
                   SELECT  c.* from t_statis a ,t_customer b,t_user
                    c,t_user d where a.customer_id=b.id and b.uid=d.id
                    and b.created_uid=c.id group by c.name
            ''')
            if todo=='1':
                count = self.db_building.get('''

                SELECT count(*) count from t_statis a ,t_customer b,t_user
                    c where a.customer_id=b.id
                    and b.created_uid=c.id  and (a.get_openaccount_day_date is null or a.start_date is null)
                    ''' + addsql )
                pagination = Pagination(page, pre_page, count.count, self.request)
                startpage = (page-1) * pre_page
                dt = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

                t_customers = self.db_building.query('''
                SELECT  a.*,b.name,c.name created_by,b.qid, b.company,b.tel,d.name building_name,
                b.guid customer_guid from t_statis a ,t_customer b,t_user
                    c,t_user d where a.customer_id=b.id and b.uid=d.id
                    and b.created_uid=c.id and (a.get_openaccount_day_date is null or a.start_date is null)
                    ''' + addsql + '''
                    order by start_date desc limit %s,%s
                ''', startpage, pre_page)
            elif todo=='2':
                count = self.db_building.get('''

                SELECT count(*) count from t_statis a ,t_customer b,t_user
                    c where a.customer_id=b.id
                    and b.created_uid=c.id  and a.get_openaccount_day_date is not null and a.start_date is not null
                    ''' + addsql )
                pagination = Pagination(page, pre_page, count.count, self.request)
                startpage = (page-1) * pre_page
                dt = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

                t_customers = self.db_building.query('''
                SELECT  a.*,b.name,c.name created_by,b.qid, b.company,b.tel,d.name building_name,
                b.guid customer_guid from t_statis a ,t_customer b,t_user
                    c,t_user d where a.customer_id=b.id and b.uid=d.id
                    and b.created_uid=c.id and a.get_openaccount_day_date is not  null and a.start_date is not null
                    ''' + addsql + '''
                    order by start_date desc limit %s,%s
                ''', startpage, pre_page)
            else:
                count = self.db_building.get('''

                SELECT count(*) count from t_statis a ,t_customer b,t_user
                    c where a.customer_id=b.id
                    and b.created_uid=c.id
                    ''' + addsql )
                pagination = Pagination(page, pre_page, count.count, self.request)
                startpage = (page-1) * pre_page
                dt = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

                t_customers = self.db_building.query('''
                SELECT  a.*,b.name,c.name created_by,b.qid, b.company,b.tel,d.name building_name,
                b.guid customer_guid from t_statis a ,t_customer b,t_user
                    c,t_user d where a.customer_id=b.id and b.uid=d.id
                    and b.created_uid=c.id
                    ''' + addsql + '''
                    order by start_date desc limit %s,%s
                ''', startpage, pre_page)
                
            return self.render(
                'statis/all_building_trans_v1.html',
                t_kf=t_kf,
                workdays=self.workdays,
                dt=datetime.datetime.now(),
                key=keyword,
                todo=todo,
                sums=sums,
                params=params,
                user_name=uid_name,
                pagination=pagination,
                msg="",
                t_customers=t_customers,
                search_key="")


        elif tag == "cq_trans":
            todo=self.get_argument('todo','')
            page=int(self.get_argument('page',1))
            pre_page=20
            sums=self.db.get('''
                  select count(*) a,
                   (select count(*) count from t_statis aa
                 inner join t_projects_member bb on aa.project_id=bb.project_id
                 and  bb.btype_id <> 0 and  bb.last_milepost_id!=151) b,
                (select count(*) count from t_statis aaa
                 inner join t_projects_member bbb on aaa.project_id=bbb.project_id
                 and  bbb.btype_id <> 0 and  bbb.last_milepost_id!=151) c
                from t_statis
            ''')
            if todo=='1':
                count=self.db.get('''
                    select count(*) count from t_statis a
                 inner join t_projects_member b on a.project_id=b.project_id
                 and  b.btype_id <> 0 and  b.last_milepost_id!=151
                ''')
                pagination=Pagination(page,pre_page,count.count,self.request)
                start_page=(page-1)*pre_page
                t_statis=self.db.query('''
                select a.*,b.member_name,c.customer_name,c.customer_company
                from t_statis a
                 inner join t_projects_member b on a.project_id=b.project_id
                 and  b.btype_id <> 0 and  b.last_milepost_id!=151
                inner join t_projects c on a.project_id=c.id
                order by a.updated_at desc limit %s,%s
            ''',start_page,pre_page)

            elif todo=='2':
                count=self.db.get('''
                    select count(*) count from t_statis a
                 inner join t_projects_member b on a.project_id=b.project_id
                 and  b.btype_id <> 0 and b.last_milepost_id=151
                ''')
                pagination=Pagination(page,pre_page,count.count,self.request)
                start_page=(page-1)*pre_page
                t_statis=self.db.query('''
                select a.*,b.member_name,c.customer_name,c.customer_company
                from t_statis a
                inner join t_projects_member b on a.project_id=b.project_id
                and  b.btype_id <> 0 and b.last_milepost_id=151
                inner join t_projects c on a.project_id=c.id
                order by a.updated_at desc limit %s,%s
            ''',start_page,pre_page)
            else:
                count=self.db.get('''
                select count(*) count from t_statis a
                 inner join t_projects_member b on a.project_id=b.project_id
                 and  b.btype_id <> 0
                ''')
                pagination=Pagination(page,pre_page,count.count,self.request)
                start_page=(page-1)*pre_page
                t_statis=self.db.query('''
                select a.*,b.member_name,c.customer_name,c.customer_company
                from t_statis a
                inner join t_projects_member b on a.project_id=b.project_id
                and  b.btype_id <> 0
                inner join t_projects c on a.project_id=c.id
                order by a.updated_at desc limit %s,%s
            ''',start_page,pre_page)

            return self.render(
                'statis/cq_trans_v1.html',
                t_statis=t_statis,
                dt=datetime.datetime.now(),
                sums=sums,
                pagination=pagination,
                search_key="",
                workdays=self.workdays,
                todo=todo,
                tag=tag)
        
        elif tag=="projects_income_title":
            page=int(self.get_argument('page',1))
            pre_page=20
            count=self.db.get('''
                select count(*) count
                from t_projects_income_title a
                inner join t_projects b on a.project_id=b.id
                inner join t_projects_member c on b.id=c.project_id and c.team_id=34 and c.member_name <>''
                inner join t_projects_member d on b.id=d.project_id and d.team_id=36 and d.member_name <>''
                inner join t_projects_income e on a.id=e.parent_id and a.project_id=e.project_id
                where a.fi_confirm_at is not null
            ''')
            pagination=Pagination(page,pre_page,count.count,self.request)
            start_page=(page-1)*pre_page
            projects_income_title=self.db.query('''
                select a.income_at,b.id,b.project_name,b.customer_company,b.customer_name,
                e.income_money,e.income_name,
                c.member_name  sale_name,d.member_name kf_name
                from t_projects_income_title a
                inner join t_projects b on a.project_id=b.id
                inner join t_projects_member c on b.id=c.project_id and c.team_id=34 and c.member_name <>''
                inner join t_projects_member d on b.id=d.project_id and d.team_id=36 and d.member_name <>''
                inner join t_projects_income e on a.id=e.parent_id and a.project_id=e.project_id
                where a.fi_confirm_at is not null  order by a.created_at desc limit %s,%s
            ''',start_page,pre_page)
            self.render('statis/projects_income_title.html',
                search_key="",
                tag=tag,
                pagination=pagination,
                projects_income_title=projects_income_title
                )
        
        elif  tag=="projects_incomes":
            page=int(self.get_argument('page',1))
            step=self.get_argument('step','0')
            pre_page=20
            params={
                
                'step':step
            }
            title_name='销售顾问'
            if step=='1':
                title_name='客服顾问'
            elif step=='2':
                title_name='客服会计'

                
            t_user=self.db.query('''
            select * from t_user where title_name=%s
            ''',title_name)

            count=self.db.get('''
            select count(*) count,sum(ssim)  sssim, 
            (select group_concat(uid_name,'|',sim) es from (select sum(c.income_money) sim,uid_name from t_projects_income c 
            inner join t_user d on c.uid_name=d.name and d.title_name=%s group by c.uid_name)cc ) every_sum 
            from (select ca,group_concat(uid_name,'|',sim) us,sum(sim) ssim
             from (select DATE_FORMAT(created_at,'%%Y-%%m-%%d') ca,uid_name, sum(income_money) sim 
                from t_projects_income a
                inner join t_user b on a.uid_name=b.name and b.title_name=%s
                 group by DATE_FORMAT(created_at,'%%Y-%%m-%%d'),uid_name )aa group by aa.ca )bb
            ''',title_name,title_name)
            pagination=Pagination(page,pre_page,count.count,self.request)
            start_page=(page-1)*pre_page
            projects_incomes=self.db.query('''
                select ca,group_concat(uid_name,'|',sim) us,sum(sim) ssim 
                from (select DATE_FORMAT(created_at,'%%Y-%%m-%%d') ca,uid_name, sum(income_money) sim 
                from t_projects_income a
                inner join t_user b on a.uid_name=b.name and b.title_name=%s
                 group by DATE_FORMAT(created_at,'%%Y-%%m-%%d'),uid_name )aa
                group by aa.ca  order by aa.ca desc limit %s,%s
            ''',title_name,start_page,pre_page)
            self.render('statis/projects_incomes.html',
                t_user=t_user,
                count=count,
                projects_incomes=projects_incomes,
                pagination=pagination,
                search_key="",
                tag=tag,
                params=params
                ) 
