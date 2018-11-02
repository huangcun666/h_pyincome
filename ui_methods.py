from tornado.template import Template

def trim_string(self,data):
    return data[0:200]+'...'



def string_dateformat(self,data):
    return data.strftime( '%Y-%m-%d' )

def trim_string1(self,code,mod_id,t_articles,site_id,t_user_site,t_temp_nav):
    if mod_id==10 or mod_id==9:
        code =  Template(code).generate(t_articles=t_articles,site_id=site_id,t_user_site=t_user_site,t_temp_nav=t_temp_nav)
    return code

