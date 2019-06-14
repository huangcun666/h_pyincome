# encoding=utf8
from handlers.base import BaseHandler
import logging
import json
import tornado.web
import urllib2
import tornado.httpclient
import sys, re,os,uuid
import urllib,datetime
import xlwt
reload(sys)
from tornado.options import define, options
sys.setdefaultencoding('utf8')
from Pagination import Pagination
from dateutil import rrule
from calendar import monthrange
import datetime

logger = logging.getLogger('boilerplate.' + __name__)
import tools
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
            # #print add_sql
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
            # #print add_sql
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
            # #print add_sql
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
            # #print add_sql
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
            # #print add_sql
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
                select uid ,uid_name from t_statis_cq  group by uid_name,uid
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
            #print add_sql
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
            count = self.db.get('''select  count(*) count,sum(sc) ssc,
            (   select group_concat(uid_name,'|',total_income) gc from (
                  select uid_name,sum(all_income) total_income
               from t_statis_kf
               ''' + add_sql + ''' group by uid_name order by total_income desc)aa

            )every_count
             from (
             select ct ,GROUP_CONCAT( uid_name,"|",gc1) gc,sum(gc1)  sc from (
            select  DATE_FORMAT(project_created_at,'%%Y-%%m') ct,uid_name ,sum(all_income) gc1
               from t_statis_kf
              ''' + add_sql + '''         group by
                 ct,uid_name

                 ) b group by ct
                    ) count
                    ''')
            pagination = Pagination(page, pre_page, count.count, self.request)
            startpage = (page-1) * pre_page
            dt = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            t_statis_kf = self.db.query('''
            select ct ,GROUP_CONCAT( uid_name,"|",gc1) gc,sum(gc1)  sc from (
 select  DATE_FORMAT(project_created_at,'%%Y-%%m') ct,uid_name ,sum(all_income) gc1
               from t_statis_kf
              ''' + add_sql + '''         group by
                 ct,uid_name

                 ) b group by ct order by ct desc

                ''')
            #print add_sql
            # t_statis_kf_total = self.db.query(
            #     '''      select uid_name,sum(all_income) total_income
            #    from t_statis_kf
            #    ''' + add_sql + '''     group by uid_name

            #     ''')
            # t_statis_kf_total_day = self.db.query(
            #     '''
            #     select   DATE_FORMAT(project_created_at,'%%Y-%%m') ct,sum(all_income) gc1
            #    from t_statis_kf
            #     ''' + add_sql + '''
            #      group by
            #       DATE_FORMAT(project_created_at,'%%Y-%%m')

            #     ''')

            # t_statis_kf_total_day_all = self.db.get(
            #     '''
            #     select ifnull(sum(all_income),0) gc1
            #    from t_statis_kf
            #     ''' + add_sql + '''

            #     ''')


            t_kf = self.db.query("""
                select uid ,uid_name from t_statis_kf   """+add_sql+""" group by uid_name,uid
            """)
            btype = self.db.query ("select * from t_projects_type where income_category='业务来源'")
            # t_user_gw = self.db.query(
            #     "SELECT * FROM t_user_teams a , t_user b where b.id=a.uid and team_id=2 "
            # )
            return self.render(
                'statis/statis_kf.html',
                # t_statis_kf_total=t_statis_kf_total,
                exists='',
                # t_user_gw=t_user_gw,
                # t_statis_kf_total_day=t_statis_kf_total_day,
                # t_statis_kf_total_day_all=t_statis_kf_total_day_all,
                btype=btype,
                t_kf=t_kf,
                dt=datetime.datetime.now(),
                params=params,
                user_name=uid_name,
                pagination=pagination,
                t_statis_kf=t_statis_kf,
                count=count,
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
            exists= self.db.get("""
                select uid_name,role from t_statis_kf where uid_name=%s limit 1
            """,uid_name)
            if exists:
                role=exists.role
                
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
                if role=='13':
                    add_sql += " and (role=%s or uid=380 )"% (role)
                else:
                    add_sql += " and role=%s"% (role)

            if exists:
                add_sql += " and uid_name = '%s' " %uid_name
            
            count = self.db.get('''select  count(*) count,sum(sc) ssc,
              (select group_concat(uid_name,'|',total_income) gc from (select uid_name,sum(all_income) total_income
               from t_statis_kf
               ''' + add_sql + ''' group by uid_name order by total_income desc)aa)every_count
               from (
                select ct ,GROUP_CONCAT( uid_name,"|",gc1) gc,sum(gc1) sc from (
            select  date(project_created_at) ct,uid_name ,sum(all_income) gc1
               from t_statis_kf
              ''' + add_sql + '''
                 group by
                 ct,uid_name
                 ) b group by ct)aa
                    ''')
            pagination = Pagination(page, pre_page, count.count, self.request)
            startpage = (page-1) * pre_page
            dt = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            t_statis_kf = self.db.query('''
            select ct ,GROUP_CONCAT( uid_name,"|",gc1) gc,sum(gc1) sc from (
 select  date(project_created_at) ct,uid_name ,sum(all_income) gc1
               from t_statis_kf
              ''' + add_sql + '''
                 group by
                 ct,uid_name
                 ) b group by ct order by ct desc

                ''')
            print('''
             select ct ,GROUP_CONCAT( uid_name,"|",gc1) gc,sum(gc1) sc from (
 select  date(project_created_at) ct,uid_name ,sum(all_income) gc1
               from t_statis_kf
              ''' + add_sql + '''
                 group by
                 ct,uid_name
                 ) b group by ct order by ct desc
            ''')
            # t_statis_kf_total = self.db.query(
            #     '''      select uid_name,sum(all_income) total_income
            #    from t_statis_kf
            #    ''' + add_sql + '''     group by uid_name

            #     ''')
            # t_statis_kf_total_day = self.db.query(
            #     '''
            #     select  date(project_created_at) ct,sum(all_income) gc1
            #    from t_statis_kf
            #     ''' + add_sql + '''
            #      group by
            #      date(project_created_at)

            #     ''')

            # t_statis_kf_total_day_all = self.db.get(
            #     '''
            #     select ifnull(sum(all_income),0) gc1
            #    from t_statis_kf
            #     ''' + add_sql + '''

            #     ''')


            t_kf = self.db.query("""
                select uid ,uid_name from t_statis_kf   """+add_sql+""" group by uid_name,uid
            """)
            btype = self.db.query ("select * from t_projects_type where income_category='业务来源'")
            # t_user_gw = self.db.query(
            #     "SELECT * FROM t_user_teams a , t_user b where b.id=a.uid and team_id=2 "
            # )
            return self.render(
                'statis/statis_kf.html',
                exists=exists,
                # t_statis_kf_total_day_all=t_statis_kf_total_day_all,
                # t_statis_kf_total=t_statis_kf_total,
                # t_statis_kf_total_day=t_statis_kf_total_day,
                # t_user_gw=t_user_gw,
                btype=btype,
                t_kf=t_kf,
                dt=datetime.datetime.now(),
                params=params,
                user_name=uid_name,
                pagination=pagination,
                t_statis_kf=t_statis_kf,
                count=count,
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
            project_id=self.get_argument('project_id','')
            daokuan_start=self.get_argument('daokuan_start','')
            daokuan_end=self.get_argument('daokuan_end','')
            sale=self.get_argument('sale','')
            kf=self.get_argument('kf','')
            step=self.get_argument('step','')
            keyword = self.get_argument("keyword","")
            income_output = self.get_argument("income_output","")
            output = self.get_argument("output","")


            sql=''
            if keyword:
                sql += ''' and  (project_name like   "%%''' + keyword + '''%%"  or customer_name like   "%%''' + keyword + '''%%"  or customer_tel like   "%%''' + keyword + '''%%" or customer_company like   "%%''' + keyword + '''%%")'''

            if project_id:
                sql+=' and a.project_id=%s '%project_id
            if daokuan_start and daokuan_end:
                sql+=' and a.income_at between "%s" and "%s" '%(daokuan_start,daokuan_end)

            if sale:
                sql+=' and  c.member_name="%s" '%sale
            if kf:
                sql+='  and d.member_name="%s" '%kf
            if step=='1':
                sql+=' and (e.income_name="合同定金" or e.income_name="尾款") and e.income_money > 0'
            elif step=='2':
                sql+=' and (e.income_name!="合同定金" and e.income_name!="尾款" and e.income_name!="退款" and e.income_money > 0) '
            elif step=='3':
                sql+=' and  (income_money < 0) '

            params={
                'daokuan_start':daokuan_start,
                'daokuan_end':daokuan_end,
                'sale':sale,
                'kf':kf,
                'project_id':project_id,
                'step':step,
                'keyword':keyword
            }

            count=self.db.get('''
                select count(*) count
                from t_projects_income_title a
                inner join t_projects b on a.project_id=b.id
                inner join t_projects_member c on b.id=c.project_id and c.team_id=34 and c.member_name <>''
                inner join t_projects_member d on b.id=d.project_id and d.team_id=36 and d.member_name <>''
                inner join t_projects_income e on a.id=e.parent_id and a.project_id=e.project_id
                where a.fi_confirm_at is not null
            '''+sql)

            pagination=Pagination(page,pre_page,count.count,self.request)
            start_page=(page-1)*pre_page
            limit_sql =""
            if not output:
                limit_sql="limit %s,%s"%(start_page,pre_page)
         
            projects_income_title=self.db.query('''
                select a.income_at,b.id,b.project_name,b.customer_company,b.customer_name,b.guid project_guid,
                e.income_money,e.income_name,e.income_num,pay_type_name,a.company_id_name,
                mbs
                from t_projects_income_title a
                inner join t_projects b on a.project_id=b.id
                inner join 
                 (select project_id,group_concat(team_name,"|",member_name)  mbs   from t_projects_member where member_id > 0 group by project_id) b
                 on b.id= b.project_id 
                inner join t_projects_income e on a.id=e.parent_id and a.project_id=e.project_id
                where a.fi_confirm_at is not null '''+sql+''' order by a.income_at desc 
            '''+limit_sql)

            if output:
                wb=xlwt.Workbook()
                sh=wb.add_sheet(u'到款结算')
                sh.write(0,0,u'订单号')
                sh.write(0,1,u'业务内容')
                sh.write(0,2,u'到款笔数')
                sh.write(0,3,u'支付方式')
                sh.write(0,4,u'到款日期')
                sh.write(0,5,u'公司名称')
                sh.write(0,6,u'客户姓名')
                sh.write(0,7,u'到款内容')
                sh.write(0,8,u'到款金额')
                sh.write(0,9,u'销售顾问')
                sh.write(0,10,u'客服顾问')
                for idx,row in enumerate(projects_income_title):
                    idx=idx+1
                    sh.write(idx,0,row.id)
                    sh.write(idx,1,row.project_name)
                    sh.write(idx,2,row.income_num)
                    sh.write(idx,3,"%s-%s"%(row.company_id_name,row.pay_type_name))                      
                    sh.write(idx,4,row.income_at.strftime("%Y-%m-%d"))
                    sh.write(idx,5,row.customer_company)
                    sh.write(idx,6,row.customer_name)
                    sh.write(idx,7,row.income_name)
                    sh.write(idx,8,row.income_money)
                    sh.write(idx,9,tools.get_member(row.mbs,u"销售顾问"))
                    sh.write(idx,10,tools.get_member(row.mbs,u"客服顾问"))
                wb.save('media/output/到款结算.xls')
                return self.redirect("/static/output/到款结算.xls")
            self.render('statis/projects_income_title.html',
                search_key="",
                tag=tag,
                params=params,
                output_path="static/output/到款统计.xls",
                pagination=pagination,
                get_member = tools.get_member,
                projects_income_title=projects_income_title
                )

        elif tag=="income_output":
            params=eval(self.get_argument('params'))
            sql=''

            if params['project_id']:
                sql+=' and a.project_id=%s '%params['project_id']
            if params['daokuan_start'] and params['daokuan_end']:
                sql+=' and a.income_at between "%s" and "%s" '%(params['daokuan_start'],params['daokuan_end'])

            if params['sale']:
                sql+=' and  c.member_name="%s" '%params['sale']
            if params['kf']:
                sql+='  and d.member_name="%s" '%params['kf']

            if params['step']=='1':
                sql+=' and (e.income_name="合同定金" or e.income_name="尾款") '
            elif params['step']=='2':
                sql+=' and e.income_name!="合同定金" and e.income_name!="尾款" and e.income_name!="退款" '
            elif params['step']=='3':
                sql+=' and  e.income_name="退款" '


            projects_income_title=self.db.query('''
                select a.income_at,b.id,b.project_name,b.customer_company,b.customer_name,
                e.income_money,e.income_name,
                c.member_name  sale_name,d.member_name kf_name
                from t_projects_income_title a
                inner join t_projects b on a.project_id=b.id
                inner join t_projects_member c on b.id=c.project_id and c.team_id=34 and c.member_name <>''
                inner join t_projects_member d on b.id=d.project_id and d.team_id=36 and d.member_name <>''
                inner join t_projects_income e on a.id=e.parent_id and a.project_id=e.project_id
                where a.fi_confirm_at is not null '''+sql+''' order by a.created_at desc
            ''')
            wb=xlwt.Workbook()
            sh=wb.add_sheet(u'到款结算')
            sh.write(0,0,u'订单号')
            sh.write(0,1,u'业务内容')
            sh.write(0,2,u'到款日期')
            sh.write(0,3,u'公司名称')
            sh.write(0,4,u'客户姓名')
            sh.write(0,5,u'到款内容')
            sh.write(0,6,u'到款金额')
            sh.write(0,7,u'销售顾问')
            sh.write(0,8,u'客服顾问')
            for idx,row in enumerate(projects_income_title):
                idx=idx+1
                sh.write(idx,0,row.id)
                sh.write(idx,1,row.project_name)
                sh.write(idx,2,row.income_at.strftime("%Y-%m-%d"))
                sh.write(idx,3,row.customer_company)
                sh.write(idx,4,row.customer_name)
                sh.write(idx,5,row.income_name)
                sh.write(idx,6,row.income_money)
                sh.write(idx,7,row.sale_name)
                sh.write(idx,8,row.kf_name)
            wb.save('media/output/到款结算.xls')
            self.write({'output_path':'static/output/到款结算.xls'})
        elif  tag=="projects_incomes":
            page=int(self.get_argument('page',1))
            step=self.get_argument('step','0')
            date_type=self.get_argument('date_type','day')
            date_sql=''
            count_sql=''
            sql=" DATE_FORMAT(ca,'%%Y-%%m-%%d') ca,ssim,us "
            pre_page=20
            params={
                'date_type':date_type,
                'step':step
            }

            title_name='销售顾问'

            if step=='1':
                title_name='客服顾问'

            elif step=='2':
                title_name='客服会计'

            if date_type=='day':
                date_sql=" order by ca "
                count_sql=" t_projects_income_count where team_name='%s' and  ca is not null "%title_name+date_sql

            elif date_type=='month':
                date_sql= " group by DATE_FORMAT(ca,'%%Y-%%m') order by DATE_FORMAT(ca,'%%Y-%%m') "
                sql=" DATE_FORMAT(ca,'%%Y-%%m') ca, sum(ssim) ssim,GROUP_CONCAT(concat(us,'')) us "
                count_sql=" (select sum(ssim) ssim from  t_projects_income_count where team_name='%s' and  ca is not null "%title_name+date_sql +") aa"
            elif date_type=='week':
                sql=" DATE_FORMAT(ca,'%%Y-%%m-%%u') ca, sum(ssim) ssim,GROUP_CONCAT(concat(us,'')) us "
                date_sql=" group by DATE_FORMAT(ca,'%%Y-%%m-%%u') order by DATE_FORMAT(ca,'%%Y-%%m-%%u') "
                count_sql=" (select  sum(ssim) ssim from t_projects_income_count where team_name='%s' and ca is not null "%title_name+date_sql+") aa"


            count=self.db.get('''
                select count(*) count,sum(ssim) sssim,
               (select us from t_projects_income_count where team_name=%s and type_name='个人总额' ) every_sum
                 from '''+count_sql,title_name)

            pagination=Pagination(page,pre_page,count.count,self.request)
            start_page=(page-1)*pre_page
            self.db.execute('''
                SET GLOBAL group_concat_max_len=102400;
                SET SESSION group_concat_max_len=102400;
            ''')
            projects_incomes=self.db.query('''
                
                select '''+sql+''' from t_projects_income_count where team_name=%s and  ca is not null '''+date_sql+''' desc limit %s,%s
            ''',title_name,start_page,pre_page)
            # if step=='0':

            #     count=self.db.get('''
            #     select count(*) count,sum(ssim)  sssim,
            #     (select group_concat(uid_name,'|',sim) es from (select sum(c.income_money) sim,member_name uid_name from t_projects_income c
            #     inner join t_projects_member d on c.project_id=d.project_id and d.team_name='销售顾问' group by d.member_name)cc ) every_sum

            #     from(
            #         select ca,group_concat(uid_name,'|',sim) us,sum(sim) ssim
            #         from (select DATE_FORMAT(a.created_at,'%%Y-%%m-%%d') ca,b.member_name uid_name, sum(income_money) sim
            #         from t_projects_income a
            #         inner join t_projects_member b on a.project_id=b.project_id and b.team_name='销售顾问'  and b.member_id!=0
            #         where  a.project_id=b.project_id
            #         group by DATE_FORMAT(a.created_at,'%%Y-%%m-%%d'),member_name )aa
            #         group by aa.ca  order by aa.ca)bb
            #     ''')
            #     pagination=Pagination(page,pre_page,count.count,self.request)
            #     start_page=(page-1)*pre_page
            #     projects_incomes=self.db.query('''
            #         select ca,group_concat(uid_name,'|',sim) us,sum(sim) ssim
            #         from (select DATE_FORMAT(a.created_at,'%%Y-%%m-%%d') ca,b.member_name uid_name, sum(income_money) sim
            #         from t_projects_income a
            #         inner join t_projects_member b on a.project_id=b.project_id and b.team_name='销售顾问' and b.member_id!=0
            #         where  a.project_id=b.project_id
            #         group by DATE_FORMAT(a.created_at,'%%Y-%%m-%%d'),member_name )aa
            #         group by aa.ca  order by aa.ca desc limit %s,%s
            #     ''',start_page,pre_page)
            # else:
            #     count=self.db.get('''
            #     select count(*) count,sum(ssim)  sssim,
            #     (select group_concat(uid_name,'|',sim) es from (select sum(c.income_money) sim,uid_name from t_projects_income c
            #     inner join t_user d on c.uid_name=d.name and d.title_name=%s group by c.uid_name)cc ) every_sum
            #     from (select ca,group_concat(uid_name,'|',sim) us,sum(sim) ssim
            #     from (select DATE_FORMAT(created_at,'%%Y-%%m-%%d') ca,uid_name, sum(income_money) sim
            #         from t_projects_income a
            #         inner join t_user b on a.uid_name=b.name and b.title_name=%s
            #         group by DATE_FORMAT(created_at,'%%Y-%%m-%%d'),uid_name )aa group by aa.ca )bb
            #     ''',title_name,title_name)
            #     pagination=Pagination(page,pre_page,count.count,self.request)
            #     start_page=(page-1)*pre_page
            #     projects_incomes=self.db.query('''
            #         select ca,group_concat(uid_name,'|',sim) us,sum(sim) ssim
            #         from (select DATE_FORMAT(created_at,'%%Y-%%m-%%d') ca,uid_name, sum(income_money) sim
            #         from t_projects_income a
            #         inner join t_user b on a.uid_name=b.name and b.title_name=%s
            #         group by DATE_FORMAT(created_at,'%%Y-%%m-%%d'),uid_name )aa
            #         group by aa.ca  order by aa.ca desc limit %s,%s
            #     ''',title_name,start_page,pre_page)
            self.render('statis/projects_incomes.html',

                count=count,
                projects_incomes=projects_incomes,
                pagination=pagination,
                search_key="",
                tag=tag,
                params=params
                )

        elif tag=="customer_exchange":
            show_tag=self.get_argument('show_tag','')
            page=int(self.get_argument('page',1))
            pre_page=20
            if not show_tag:
                count=self.db_customer.get('''
                select count(*) count,
                (select concat(group_concat(uid_name,'|',count),',','总数','|',sum(count)) from ( select uid_name,count(*) count from 
                (select uid_name,DATE_FORMAT(created_at,'%%Y-%%m-%%d')ct,customer_id from t_customer_exchange
                where  etype=2 group by customer_id,DATE_FORMAT(created_at,'%%Y-%%m-%%d'),uid_name
                            )aa group by uid_name order by count desc)bb) every_gc
                
                 from ( select ct,group_concat(c_uid_name,'|',count) gc from ( select ct,concat(uid_name) c_uid_name,count(*) count from 
                (select uid_name,DATE_FORMAT(created_at,'%%Y-%%m-%%d')ct,customer_id from t_customer_exchange
                    where  etype=2 group by customer_id,ct,uid_name
               )a group by ct,uid_name)b group by ct)c 
            
            ''')
                pagination=Pagination(page,pre_page,count.count,self.request)
                start_page=(page-1)*pre_page
                t_customer_exchange = self.db_customer.query("""
                select ct,group_concat(c_uid_name,'|',count) gc,sum(count) sc from ( select ct,concat(uid_name) c_uid_name,count(*) count from 
                (select uid_name,DATE_FORMAT(created_at,'%%Y-%%m-%%d')ct,customer_id from t_customer_exchange
                    where  etype=2 group by customer_id,ct,uid_name
               )a group by ct,uid_name)b group by ct order by ct desc limit %s,%s
            """,start_page,pre_page)
            elif show_tag=='1':
                count=self.db_customer.get('''
                    select count(*) count from  t_customer_exchange a 
                    inner join t_customer b on a.customer_id=b.id
                     left JOIN t_customer_payment c
                                ON a.id = c.customer_id
                            INNER JOIN
                            (
                                SELECT `customer_id`, MAX(id) max_id
                                FROM t_customer_payment
                                GROUP BY customer_id
                            ) b ON c.customer_id = b.customer_id AND
                                    b.max_id = c.id
                        left join '''+options.mysql_database+'''.t_projects_member f on
                                    c.project_id=f.project_id and f.team_id=34 
                            left join '''+options.mysql_database+'''.t_projects_member e on
                                    c.project_id=e.project_id and e.team_id=36  
                     where  etype=2 order by a.created_at desc
                ''')
                pagination=Pagination(page,pre_page,count.count,self.request)
                start_page=(page-1)*pre_page
                t_customer_exchange=self.db_customer.query('''
                    select a.*,b.company,c.sale_man sale_man1,c.kf_man kf_man1,f.member_name sale_man,
                    e.member_name kf_man from  t_customer_exchange a 
                    inner join t_customer b on a.customer_id=b.id
                     left JOIN t_customer_payment c
                                ON a.id = c.customer_id
                            INNER JOIN
                            (
                                SELECT `customer_id`, MAX(id) max_id
                                FROM t_customer_payment
                                GROUP BY customer_id
                            ) b ON c.customer_id = b.customer_id AND
                                    b.max_id = c.id
                        left join '''+options.mysql_database+'''.t_projects_member f on
                                    c.project_id=f.project_id and f.team_id=34 
                            left join '''+options.mysql_database+'''.t_projects_member e on
                                    c.project_id=e.project_id and e.team_id=36  
                     where  etype=2 order by a.created_at desc limit %s,%s
                ''',start_page,pre_page)
            self.render('statis/customer_exchange_count.html',
                search_key="",
                tag=tag,
                count=count,
                t_customer_exchange=t_customer_exchange,
                pagination=pagination,
                show_tag=show_tag
                )

        elif tag=="payment_count":
            page = int(self.get_argument("page", 1))

            pre_page = 20
            count = self.db_customer.get('''
                    select count(*) count
                            FROM  t_customer a
                                INNER JOIN t_customer_payment c
                                    ON a.id = c.customer_id
                                INNER JOIN
                                (
                                    SELECT `customer_id`, MAX(id) max_id
                                    FROM t_customer_payment
                                    GROUP BY customer_id
                                ) b ON c.customer_id = b.customer_id AND
                                        b.max_id = c.id  where c.wait_pay_amount <> 0 and c.pb_remark <> '' and req_uid > 0
               ''')
            pagination = Pagination(page, pre_page, count.count, self.request)
            startpage = (page - 1) * pre_page
            customers = self.db_customer.query("""
                    SELECT  *,c.updated_at pay_updated_at,c.uid_name pay_uid_name,c.wait_pay_amount,
                    c.pay_typeid_name pay_pay_typeid_name,c.service_amount pay_service_amount,c.service_month_amount pay_service_amount_month, c.book_amount pay_book_amount,
                    a.acc_uid_name,req_at 
                    FROM  t_customer a
                        INNER JOIN t_customer_payment c
                            ON a.id = c.customer_id
                        INNER JOIN
                        (
                            SELECT `customer_id`, MAX(id) max_id
                            FROM t_customer_payment
                            GROUP BY customer_id
                        ) b ON c.customer_id = b.customer_id AND
                                b.max_id = c.id 
                        where c.wait_pay_amount <> 0 and c.pb_remark <> '' and req_uid > 0
                        order by req_at desc
                        limit %s,%s
            """, startpage, pre_page)


            self.render(
                'statis/payment_count.html',
                search_key="",
                customers=customers,
                pagination=pagination,
                tag=tag)

        elif tag=="payment_count_list":
            page = int(self.get_argument("page", 1))
            pre_page = 20
            count=self.db_customer.get("""
            select count(*) count from(
                   select a.acc_uid_name,ifnull(sum(b.wait_pay_amount),0) wait_pay_amount_now,
            ifnull(sum(c.wait_pay_amount),0) wait_pay_amount_bef ,ifnull(sum(e.income_list),0) income_list from t_customer a 
            left join t_customer_payment b on a.id=b.customer_id and
            b.wait_pay_amount <> 0 and b.pb_remark <> '' and b.req_at is not null and date_format(b.req_at,'%%Y-%%m')=date_format(now(),'%%Y-%%m')
            and b.id=(SELECT  MAX(id) max_id FROM t_customer_payment where  customer_id = b.customer_id)
            left join t_customer_payment c on a.id=c.customer_id and
            c.wait_pay_amount <> 0 and c.pb_remark <> '' and c.req_at is not null and date_format(c.req_at,'%%Y-%%m')<date_format(now(),'%%Y-%%m')
            and c.id=(SELECT  MAX(id) max_id FROM t_customer_payment where  customer_id = c.customer_id)
            inner join t_customer_payment d on a.id=d.customer_id and d.wait_pay_amount <> 0 and d.pb_remark <> '' and d.req_at is not null
            left join (select a.acc_uid_name, income_list
                                from  `t_customer` a 
                   
                    inner join """+options.mysql_database+""".t_projects b on a.company = b.customer_company     and reg_state <> 1 
                    inner join """+options.mysql_database+""".t_projects_income_title e  on e.project_id=b.id and fi_confirm_uid > 0 and
                    is_handler=0 and date_format(fi_confirm_at,'%%Y-%%m')=date_format(now(),'%%Y-%%m')
                					inner join
                     (select parent_id,income_num,
                      sum(income_money)
                      income_list   from """+options.mysql_database+""".t_projects_income dd 
                     
                     group by parent_id,income_num
                      
                     ) c on c.parent_id=e.id
                    inner join (select title_id, GROUP_CONCAT(concat( service_name,"|",service_money)) pay_list from """+options.mysql_database+""".t_projects_income_detail d where
                    (d.`service_id`=10 or d.service_id=204 or d.service_id=131)
                    group by title_id) d on e.id=d.title_id and b.id=e.project_id  )e on e.acc_uid_name=a.acc_uid_name
					group by a.acc_uid_name)aa
            """)
            pagination = Pagination(page, pre_page, count.count, self.request)
            startpage = (page - 1) * pre_page
            customers = self.db_customer.query("""
          select a.acc_uid_name,ifnull(sum(b.wait_pay_amount),0) wait_pay_amount_now,
            ifnull(sum(c.wait_pay_amount),0) wait_pay_amount_bef ,ifnull(sum(e.income_list),0) income_list
            ,ifnull(sum(e.income_list_all),0) income_list_all
             from t_customer a 
            left join t_customer_payment b on a.id=b.customer_id and
            b.wait_pay_amount <> 0 and b.pb_remark <> '' and b.req_at is not null and date_format(b.req_at,'%%Y-%%m')=date_format(now(),'%%Y-%%m')
            and b.id=(SELECT  MAX(id) max_id FROM t_customer_payment where  customer_id = b.customer_id)
            left join t_customer_payment c on a.id=c.customer_id and
            c.wait_pay_amount <> 0 and c.pb_remark <> '' and c.req_at is not null and date_format(c.req_at,'%%Y-%%m')<date_format(now(),'%%Y-%%m')
            and c.id=(SELECT  MAX(id) max_id FROM t_customer_payment where  customer_id = c.customer_id)
            inner join t_customer_payment d on a.id=d.customer_id and d.wait_pay_amount <> 0 and d.pb_remark <> '' and d.req_at is not null
            left join (select a.acc_uid_name, income_list,income_list_all
                                from  `t_customer` a 
                   
                    inner join """+options.mysql_database+""".t_projects b on a.company = b.customer_company     and reg_state <> 1 

                    inner join """+options.mysql_database+""".t_projects_income_title e  on e.project_id=b.id and e.fi_confirm_uid > 0 and
                    e.is_handler=0 
                					left join
                     (select dd.parent_id,dd.income_num,
                      sum(dd.income_money)
                      income_list   from """+options.mysql_database+""".t_projects_income dd 
                     
                     group by dd.parent_id,dd.income_num
                      
                     ) c on c.parent_id=e.id and  date_format(e.fi_confirm_at,'%%Y-%%m')=date_format(now(),'%%Y-%%m')

                    	left join
                     (select dd.parent_id,dd.income_num,
                      sum(dd.income_money)
                      income_list_all   from """+options.mysql_database+""".t_projects_income dd 
                     
                     group by dd.parent_id,dd.income_num
                      
                     ) cc on cc.parent_id=e.id 

                    inner join (select title_id, GROUP_CONCAT(concat( service_name,"|",service_money)) pay_list from """+options.mysql_database+""".t_projects_income_detail d where
                    (d.`service_id`=10 or d.service_id=204 or d.service_id=131)
                    group by title_id) d on e.id=d.title_id and b.id=e.project_id  )e on e.acc_uid_name=a.acc_uid_name


					group by a.acc_uid_name limit %s,%s
                        """,startpage, pre_page)

            self.render(
            'statis/payment_count_list.html',
                search_key="",
                customers=customers,
                pagination=pagination,
                tag=tag
            )

        elif tag=='statis_cq_banli':
            page = int(self.get_argument("page", 1))
            btype=self.get_argument('btype','')
            pre_page = 20
            gs_name=self.get_argument('gs_name','')
            start_time=self.get_argument('start_time','')
            end_time=self.get_argument('end_time','')
            way=self.get_argument('way','day')
           
            sql=''
            way_sql=" '%%Y-%%m-%%d' " 
            params={
                'gs_name':gs_name,
                'btype':btype,
                'way':way,
                'start_time':start_time,
                'end_time':end_time
            }
            if btype:
                sql+=' and btype_id=%s '%btype
            if way=='month':
                way_sql=" '%%Y-%%m' " 
            elif way=='week':
                way_sql=" '%%Y-%%m-%%u' "
            if gs_name:
                sql+=' and a.uid_name="%s" '%gs_name
            if start_time and end_time:
                if way=='week':
                    sql+=' and  date_format(confirm_at,'+way_sql+') between date_format("'+start_time+'",'+way_sql+') and date_format("'+end_time+'",'+way_sql+') '
                else:
                    sql+=' and  date_format(confirm_at,'+way_sql+') between "%s" and "%s" '%(start_time,end_time)
            count=self.db.get('''
            select count(*) count,sum(sc) ssc,
            ( select group_concat(uid_name,'|',count) from (
                   select a.uid_name ,count(*) count from  t_projects_milepost a
                   inner join t_projects b on a.project_id=b.id
                where a.confirm_at is not null and a.order_int=2 '''+sql+'''  group by a.uid_name order by count desc
                )aa
            )every_count
             from (
             select group_concat(uid_name,'|',count) gc,sum(count) sc,df_confirm_at from(
                SELECT date_format(a.confirm_at,'''+way_sql+''') df_confirm_at,a.uid_name,a.btype_name,count(*) count 
                FROM t_projects_milepost a
                inner join t_projects b on a.project_id=b.id
                where a.confirm_at is not null and a.order_int=2 '''+sql+'''
                group by df_confirm_at,a.uid_name,a.btype_name)aa group by df_confirm_at)bb
            ''')
                
            pagination = Pagination(page, pre_page, count.count, self.request)
            startpage = (page - 1) * pre_page
            t_projects_milepost=self.db.query('''
            select group_concat(uid_name,'|',count) gc,sum(count) sc,df_confirm_at from(
                SELECT date_format(a.confirm_at,'''+way_sql+''') df_confirm_at,a.uid_name,count(*) count 
                FROM t_projects_milepost a
                inner join t_projects b on a.project_id=b.id
                where a.confirm_at is not null and a.order_int=2 '''+sql+'''
                group by df_confirm_at,uid_name)aa group by df_confirm_at order by df_confirm_at desc limit %s,%s
            ''',startpage,pre_page)
            t_projects_type=self.db.query('''
                select id,income_name from t_projects_type where income_category='业务分类'
            ''')
            member_gs=self.db.query('''
                select member_name uid_name,member_id from t_projects_member
                 where team_id=38 and last_milepost_id is not null and last_milepost_id <> 0  group by member_name
            ''')

            self.render(
            'statis/statis_cq_banli.html',
                search_key="",
                t_projects_milepost=t_projects_milepost,
                pagination=pagination,
                member_gs=member_gs,
                params=params,
                t_projects_type=t_projects_type,
                count=count,
                tag=tag
            )

        elif tag=="todo_arrange_count":
            todo=self.get_argument('todo','')
            page = int(self.get_argument("page", 1))
            gb=self.get_argument('gb','')
            way=self.get_argument('way','day')
            person_name=self.get_argument('person_name','')
            start_time=self.get_argument('start_time','')
            end_time=self.get_argument('end_time','')
            person_name=self.get_argument('person_name','')
            department=self.get_argument('department','')
            pre_page = 20
            sql=''

            gb_sql=' a.responsible_per '
            way_sql=" '%%Y-%%m-%%d' "
            person_sql=''
            if way=='month':
                way_sql=" '%%Y-%%m' "
            elif way=='week':
                way_sql=" '%%Y-%%m-%%u' "

            departments=self.db.query(
                """
                select name department_name from t_user_department where parent_id=0
                """
            )
            if gb=='bs':
                gb_sql=' a.banshi_per '
                departments=self.db.query('''
                select department_name from t_user where department_name is not null and department_name <>''  group by department_name
            ''')
            if not todo and gb:
                sql=' and banshi_per is not null '
            if todo == '1':
                sql = 'and d.created_at is NULL and d.updated_at is NULL and (banshi_per  is not null) '
            elif todo == '2':
                sql = 'and d.created_at is not NULL and d.updated_at is NULL '
            elif todo == '3':
                sql = 'and d.created_at is not NULL and d.updated_at is not NULL '
            elif todo=='-1000':
                sql = " and banshi_per is null"

            if person_name:
                if gb=='bs':
                    sql+=' and banshi_per="%s" '%person_name
                else:
                    sql+=' and responsible_per="%s" '%person_name
            if start_time and end_time:
                sql+=' and a.created_at between "%s" and "%s" '%(start_time,end_time)
            if department:
                if gb=='bs':
                    sql+=' and c.department_name="%s" '%department
                    person_sql=' inner join t_user c on a.banshi_per=c.name and c.department_name="%s" '%department
                else:
                    sql+=' and b.department_name="%s" '%department
                    person_sql='inner join t_user b on a.responsible_per=b.name and b.department_name="%s" '%department

            params={
                'gb':gb,
                'way':way,
                'person_name':person_name,
                'end_time':end_time,
                'start_time':start_time,
                'department':department
            }
        
            count=self.db.get("""
                 select count(*) count,sum(sc) ssc,
                 (
                    select group_concat(gb_name,'|',ifnull(count,0)) from(
                     select count(*) count,"""+gb_sql+""" gb_name
                        from t_todo_arrange a inner join t_user b
                        on a.responsible_per=b.name
                        left join t_user c on a.banshi_per=c.name
                        inner join t_todo_arrange_status d
                        on a.id=d.todo_id 
                        where is_hide=0 """+sql+"""
                        group by """+gb_sql+"""order by count desc
                  )aa)every_count
                        from (select sum(count) sc,df_created from (
                select date_format(a.created_at,"""+way_sql+""") df_created,count(*) count,"""+gb_sql+""" gb_name
                        from t_todo_arrange a inner join t_user b
                        on a.responsible_per=b.name
                        left join t_user c on a.banshi_per=c.name
                        inner join t_todo_arrange_status d
                        on a.id=d.todo_id
                         where is_hide=0 """+sql+"""
                        group by df_created,"""+gb_sql+"""
                       )aa  group by df_created
                        )bb
            """)
            pagination = Pagination(page, pre_page, count.count, self.request)
            startpage = (page - 1) * pre_page
            todo_arranges = self.db.query("""
            select group_concat(gb_name,'|',count) gcgc,sum(count) sc,df_created from (
                select date_format(a.created_at,"""+way_sql+""") df_created,count(*) count,"""+gb_sql+""" gb_name
                        from t_todo_arrange a inner join t_user b
                        on a.responsible_per=b.name
                        left join t_user c on a.banshi_per=c.name
                        inner join t_todo_arrange_status d
                        on a.id=d.todo_id
                         where is_hide=0 """+sql+"""
                        group by df_created,"""+gb_sql+"""
                       )aa group by df_created
                        order by df_created desc limit %s,%s
            """,startpage,pre_page)

            todo_arrange_name=self.db.query('''
                select '''+gb_sql+''' name from  t_todo_arrange a '''+person_sql+''' 
                 inner join t_todo_arrange_status d
                 on a.id=d.todo_id  where '''+gb_sql+''' is not null group by name
            ''')
            self.render('statis/todo_arrange_count.html',
                search_key="",
                todo_arrange_name=todo_arrange_name,
                todo_arranges=todo_arranges,
                pagination=pagination,
                todo=todo,
                count=count,
                tag=tag,
                params=params,
                departments=departments
                )
        
        elif tag=="customer_exchange_count":
            page = int(self.get_argument("page", 1))
            pre_page=20
            way=self.get_argument('way','')
            show_tag=self.get_argument('show_tag','1')
            sql=' and c.department_name!="销售部" '
            params={
                'show_tag':show_tag,
                'way':way
            }
            if show_tag=='2':
                sql=''' 
                    and c.department_name='销售部'
                '''


            if way:
                if way=='day':
                    df_format=' "%%Y-%%m-%%d" '
                elif way=='month':
                    df_format=' "%%Y-%%m" '
                elif way=='week':
                    df_format=' "%%Y-%%m-%%u" '
                count=self.db_customer.get('''
                select count(*) count ,sum(sc) ssc,
                (select group_concat(uid_name,'|',count) from
                (select a.uid_name,count(*) count  FROM t_customer_exchange a
                inner join  '''+options.mysql_database+'''.t_user c on
                a.uid=c.id '''+sql+'''  where etype=2 group by uid_name order by count desc)aa) every_count
                 from (
                select group_concat(uid_name,'|',count),df,sum(count) sc  from
                ( SELECT count(*) count,a.uid_name,date_format(a.created_at,'''+df_format+''') df
                FROM t_customer_exchange a
                inner join  '''+options.mysql_database+'''.t_user c on
                a.uid=c.id '''+sql+'''
                 where etype=2 group by df,uid_name)aa group by df)bb
                ''')

                pagination = Pagination(page, pre_page, count.count, self.request)
                startpage = (page - 1) * pre_page

                t_customer_exchange=self.db_customer.query('''
                select group_concat(uid_name,'|',count) gc,df,sum(count) sc from
                ( SELECT count(*) count,a.uid_name,date_format(a.created_at,'''+df_format+''') df
                FROM t_customer_exchange a
                inner join  '''+options.mysql_database+'''.t_user c on
                a.uid=c.id '''+sql+'''
                 where etype=2 group by df,uid_name)aa group by df order by df desc limit %s,%s
                ''',startpage,pre_page)
            else:
                count=self.db_customer.get('''
            select count(*) count from t_customer_exchange a
            inner join t_customer b on a.customer_id=b.id
             inner join  '''+options.mysql_database+'''.t_user c on
            a.uid=c.id
            '''+sql+'''
             where etype=2
            ''')
                pagination = Pagination(page, pre_page, count.count, self.request)
                startpage = (page - 1) * pre_page
                t_customer_exchange=self.db_customer.query('''
            select a.*,b.company,b.reg_person,b.acc_uid_name from t_customer_exchange a
            inner join t_customer b on a.customer_id=b.id
             inner join '''+options.mysql_database+'''.t_user c on
                    a.uid=c.id
             '''+sql+'''
             where etype=2 order by a.created_at desc limit %s,%s
            ''',startpage,pre_page)
            self.render('statis/customer_exchange_ck_count.html',
            search_key="",
            params=params,
            count=count,
            t_customer_exchange=t_customer_exchange,
            pagination=pagination
            )

        elif tag=="receive_remind_count":
            show_tag=self.get_argument('show_tag','1')
            page = int(self.get_argument("page", 1))
            distribute_at_start=self.get_argument('distribute_at_start','')
            distribute_at_end=self.get_argument('distribute_at_end','')
            jd_at_start=self.get_argument('jd_at_start','')
            jd_at_end=self.get_argument('jd_at_end','')
            banjie_at_start=self.get_argument('banjie_at_start','')
            banjie_at_end=self.get_argument('banjie_at_end','')
            company=self.get_argument('company','')
            sale=self.get_argument('sale','')
            genjin_at_start=self.get_argument('genjin_at_start','')
            genjin_at_end=self.get_argument('genjin_at_end','')
            way=self.get_argument('way','day')
            pre_page=20
            sql=''
            sel_sql=''
            order_sql=' a.distribute_at '
            params={
                "show_tag":show_tag,
                "distribute_at_start":distribute_at_start,
                "distribute_at_end":distribute_at_end,
                "jd_at_start":jd_at_start,
                "jd_at_end":jd_at_end,
                "banjie_at_start":banjie_at_start,
                "banjie_at_end":banjie_at_end,
                "company":company,
                "sale":sale,
                "genjin_at_start":genjin_at_start,
                "genjin_at_end":genjin_at_end,
                "way":way

            }
            t_user_sales=self.db.query('''
                    select * from t_user where department_name='销售部'
                ''')
            if show_tag=='5':
                if way=='day':
                    df_format=' "%%Y-%%m-%%d" '
                elif way=='month':
                    df_format=' "%%Y-%%m" '
                elif way=='week':
                    df_format=' "%%Y-%%m-%%u" '
                if sale:
                    sql+=' and c.sale_id=%s '%sale
                if banjie_at_start and banjie_at_end:
                    sql+=' and c.check_at between "%s" and "%s" '%(banjie_at_start,banjie_at_end)
                count=self.db_customer.get('''
                select count(*) count ,sum(ssw) sssw,
                (select group_concat(sale_name,'|',sw) from(
                  select c.sale_name,sum(a.wait_pay_amount) sw
                from t_customer_payment a 
                INNER JOIN
                (
                    SELECT customer_id, MAX(id) max_id
                    FROM t_customer_payment
                    GROUP BY customer_id
                ) b ON a.customer_id = b.customer_id AND
                        b.max_id = a.id 
                inner join t_customer_payment_assist c on a.customer_id=c.customer_id
                and is_check=1 '''+sql+''' group by sale_name order by sw desc
                 )aa)every_count
                  from (
                       select group_concat(sale_name,'|',sw),df,sum(sw) ssw from (
                select c.sale_name,date_format(c.check_at,'''+df_format+''') df,sum(a.wait_pay_amount) sw
                from t_customer_payment a 
                INNER JOIN
                (
                    SELECT customer_id, MAX(id) max_id
                    FROM t_customer_payment
                    GROUP BY customer_id
                ) b ON a.customer_id = b.customer_id AND
                        b.max_id = a.id 
                inner join t_customer_payment_assist c on a.customer_id=c.customer_id
                and is_check=1 '''+sql+''' group by sale_name,df)aa group by df )aaa
                ''')
                pagination=Pagination(page,pre_page,count.count,self.request)
                startpage=(page-1)*pre_page
                wait_pay_amount_count=self.db_customer.query('''
                select group_concat(sale_name,'|',sw) gc,df,sum(sw) ssw from (
                select c.sale_name,date_format(c.check_at,'''+df_format+''') df,sum(a.wait_pay_amount) sw
                from t_customer_payment a 
                INNER JOIN
                (
                    SELECT customer_id, MAX(id) max_id
                    FROM t_customer_payment
                    GROUP BY customer_id
                ) b ON a.customer_id = b.customer_id AND
                        b.max_id = a.id 
                inner join t_customer_payment_assist c on a.customer_id=c.customer_id
                and is_check=1 '''+sql+''' group by sale_name,df)aa group by df order by df desc limit %s,%s
                ''',startpage,pre_page)
                self.render('statis/receive_remind_count.html',
                search_key="",
                t_user_sales=t_user_sales,
                pagination=pagination,
                params=params,
                tag=tag,
                count=count,
                wait_pay_amount_count=wait_pay_amount_count
                )
            else:
                if show_tag=='2':
                    sql=' and a.is_check=1  '
                elif show_tag=='3':
                    order_sql=' c.created_at'
                    sel_sql=' c.created_at new_genjin_at,c.msg,d.count genjin_count,  '
                    sql="""
                    inner join t_customer_exchange c on c.customer_id=a.customer_id and c.uid=a.sale_id and c.etype=2
                    and c.id=(select max(id) from t_customer_exchange where a.customer_id=customer_id and a.sale_id=uid and etype=2)
                    inner join (select count(*) count,customer_id,uid,etype from t_customer_exchange
                    group by customer_id,uid,etype) d 
                    on  d.customer_id=a.customer_id and d.uid=a.sale_id and d.etype=2
                    """
                elif show_tag=='4':
                    order_sql=' c.created_at'
                    sel_sql=' c.created_at  new_genjin_at,c.msg,'
                    sql='''
                        inner join t_customer_exchange c on c.customer_id=a.customer_id and c.uid=a.sale_id and c.etype=2
                    '''
                if distribute_at_start and distribute_at_end:
                    sql+=' and  distribute_at between "%s" and "%s" '%(distribute_at_start,distribute_at_end)
                if jd_at_start and jd_at_end:
                    sql+=' and jd_at between "%s" and "%s" '%(jd_at_start,jd_at_end)
                if banjie_at_start and banjie_at_end:
                    sql+=' and check_at between "%s" and "%s" '%(banjie_at_start,banjie_at_end)
                if company:
                    sql+=' and b.company like "%%'+company+'%%" '
                if sale:
                    sql+=' and a.sale_id=%s '%sale
                if genjin_at_start and genjin_at_end:
                    sql+=' and  c.created_at between "%s" and "%s" '%(genjin_at_start,genjin_at_end)
                count=self.db_customer.get('''
                    select count(*) count
                    from t_customer_payment_assist a 
                    inner join t_customer b on a.customer_id=b.id  and  a.jd_at is not null
                '''+sql)
                pagination=Pagination(page,pre_page,count.count,self.request)
                startpage=(page-1)*pre_page
                t_customer_payment_assist=self.db_customer.query('''
                    select a.*,b.company,b.id customer_id,'''+sel_sql+'''
                    datediff(DATE_FORMAT(jd_at, '%%Y-%%m-%%d'),DATE_FORMAT(distribute_at,'%%Y-%%m-%%d')) jd_day,
                    datediff(DATE_FORMAT(check_at, '%%Y-%%m-%%d'),DATE_FORMAT(distribute_at,'%%Y-%%m-%%d')) banjie_day
                    from t_customer_payment_assist a 
                    inner join t_customer b on a.customer_id=b.id
                    and a.jd_at is not null '''+sql+'''
                    order by '''+order_sql+''' desc limit %s,%s
                ''',startpage,pre_page)
               
                self.render('statis/receive_remind_count.html',
                search_key="",
                t_user_sales=t_user_sales,
                pagination=pagination,
                params=params,
                tag=tag,
                t_customer_payment_assist=t_customer_payment_assist,
                )

        elif tag=="customer_clearly_count":
            way=self.get_argument('way','')
            show_tag=self.get_argument('show_tag','')
            page = int(self.get_argument("page", 1))
            sql=''
            every_count=''
            pre_page=20
            params={
                'way':way,
                'show_tag':show_tag
            }
            if way:
                if show_tag=='customer':
                    if way=='day':
                        df_format=' "%%Y-%%m-%%d" '
                    elif way=='month':
                        df_format=' "%%Y-%%m" '
                    elif way=='week':
                        df_format=' "%%Y-%%m-%%u" '

                    every_count=self.db_customer.query('''
                        select uid_name, count(*) count from
                        (select date_format(uid_at,'''+df_format+''') df,uid_name 
                        from t_customer_clearly_msg group by df,uid_name,clearly_id)aa
                        group by uid_name order by  count desc
                        ''')
                    count=self.db_customer.get('''
                    select count(*) count,sum(ssc) all_count
                     from (
                        select df,sum(sc)ssc from (select date_format(df1,'''+df_format+''') df,uid_name,count(*) sc from (
                        select date_format(uid_at,'%%Y-%%m-%%d') df1,uid_name 
                        from t_customer_clearly_msg group by df1,uid_name,clearly_id)aa 
                        group by df,uid_name)bb group by df)cc   
                    ''')
                    pagination=Pagination(page,pre_page,count.count,self.request)
                    startpage=(page-1)*pre_page                    
                    t_customer_clearly=self.db_customer.query('''
                        select df,group_concat(uid_name,'|',sc) gc,sum(sc) ssc from
                        (select date_format(df1,'''+df_format+''') df,uid_name,count(*) sc from (
                        select date_format(uid_at,'%%Y-%%m-%%d') df1,uid_name 
                        from t_customer_clearly_msg group by df1,uid_name,clearly_id)aa 
                        group by df,uid_name)bb group by df order by df desc limit %s,%s   
                    ''',startpage,pre_page)


                elif show_tag=='record':
                    if way=='day':
                        df_format=' "%%Y-%%m-%%d" '
                    elif way=='month':
                        df_format=' "%%Y-%%m" '
                    elif way=='week':
                        df_format=' "%%Y-%%m-%%u" '
                        
                    every_count=self.db_customer.query('''
                        select uid_name,sum(sc) count from(
                        select date_format(uid_at,'''+df_format+''') df,uid_name,count(*) sc
                        from t_customer_clearly_msg group by df,uid_name)aa group by uid_name order by count desc
                        ''')
                    count=self.db_customer.get('''
                    select count(*) count,sum(ssc) all_count from
                        (select date_format(df1,'''+df_format+''') df,sum(sc) ssc from(
                        select date_format(uid_at,'%%Y-%%m-%%d') df1,uid_name,count(*) sc
                        from t_customer_clearly_msg group by df1,uid_name)aa group by df)bb 
                    ''')
                    pagination=Pagination(page,pre_page,count.count,self.request)
                    startpage=(page-1)*pre_page                                            
                    t_customer_clearly=self.db_customer.query('''
                        select date_format(df1,'''+df_format+''') df,group_concat(uid_name,'|',sc) gc,sum(sc) ssc from(
                        select date_format(uid_at,'%%Y-%%m-%%d') df1,uid_name,count(*) sc
                        from t_customer_clearly_msg group by df1,uid_name)aa group by df order by df desc
                        limit %s,%s''',startpage,pre_page)
       
            else:
                count=self.db_customer.get('''
                select count(*) count from t_customer_clearly_msg a 
                inner join t_customer_clearly b on a.clearly_id=b.id
                inner join t_customer c on b.customer_id=c.id 
                ''')
                pagination=Pagination(page,pre_page,count.count,self.request)
                startpage=(page-1)*pre_page
                t_customer_clearly=self.db_customer.query('''
                select a.uid,a.uid_name,a.uid_at,a.ass_msg,c.company  from t_customer_clearly_msg a 
                inner join t_customer_clearly b on a.clearly_id=b.id
                inner join t_customer c on b.customer_id=c.id 
                order by a.uid_at desc limit %s,%s
                ''',startpage,pre_page)
            self.render('statis/customer_clearly_count.html',
             search_key="",
             pagination=pagination,
             t_customer_clearly=t_customer_clearly,
             every_count=every_count,
             params=params,
             count=count
            )