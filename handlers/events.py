from datetime import datetime, timedelta
def add_project_event(self,project_id,event_type,txt,uid,uid_name,customer_id=0,business_id=0):
    self.db.execute("""insert into t_projects_events(project_id,event_type,txt,created_at,uid,uid_name,customer_id,business_id) 
                values(%s,%s,%s,%s,%s,%s,%s,%s)""",
                project_id,event_type,txt,datetime.now(),uid,uid_name,customer_id,business_id
                )


def add_project_event_ext(self, project_id, event_type, txt, uid, uid_name,ext_id):
    self.db.execute(
        """insert into t_projects_events(project_id,event_type,txt,created_at,uid,uid_name,ext_id) 
                values(%s,%s,%s,%s,%s,%s,%s)""", project_id, event_type,
        txt,datetime.now(), uid, uid_name, ext_id)
