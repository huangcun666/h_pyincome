def add_project_event(self,project_id,event_type,txt,uid,uid_name):
    self.db.execute("""insert into t_projects_events(project_id,event_type,txt,created_at,uid,uid_name) 
                values(%s,%s,%s,now(),%s,%s)""",
                project_id,event_type,txt,uid,uid_name
                )