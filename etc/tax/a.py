#coding=utf8
import requests,datetime,time
dt_query_year = datetime.datetime.now().strftime("%Y")  
dt_query_month = datetime.datetime.now().strftime("%m")  
qdate = "%s年%s月"%(dt_query_year,dt_query_month)
get_date = datetime.datetime.now().strftime("%Y-%m-01")  
dt_query = datetime.datetime.now().strftime("%Y-%m-%d")  
get_url = u"https://www.etax-gd.gov.cn/web-tycx/tycx/query.do?t={0}&bw=%7B%22taxML%22:%7B%22head%22:%7B%22gid%22:%22311085A116185FEFE053C2000A0A5B63%22,%22sid%22:%22yhscx.SBZS.SBXXCX%22,%22tid%22:%22+%22,%22version%22:%22%22%7D,%22body%22:%7B%22sbny%22:%22%22,%22skssqq%22:%222015-01-01%22,%22skssqz%22:%22{1}%22,%22gdbz%22:%22%22%7D%7D%7D".format(str(int(time.time())),dt_query)
# s="TGC=TGT-81787-BOORxgbVbJ0cl4qK7ooo2zDIKe6JfICrfA2UbGgITcY4OfeHvP-gddzswj;DZSWJ_TGC=F4CA0C9BAD9B26667799B9DC36294AE9;JSESSIONID=F26F2F631A3587C457975FDE2E8166A9;SERVERID=86cdeeb042bfa50e4e2f6cfb3d39739e|1564819888|1564819876;acw_tc=2f6a1fd615648198766872081ed6d376c79388e56b06d2f8999d7dee7dfcc4;_uab_collina=156481987691289959050809"
# s="DZSWJ_TGC=28926062B245ECD33694C2AB9057539C;SERVERID=823f90608ae6d7ab4c770fa4123d4607|1564976766|1564976756;TGC=TGT-105844-b4tBQoFiqePBd4TEHxTIxnRLlEyxKx76U2pPOwdRkEZdvQk4Jk-gddzswj;acw_tc=2f6a1fe615649767569833157ef1f1d013d31339ad2adbffa1ed357c43f58c;JSESSIONID=E74F5FAE4D90D2E26205B286CD940DE1"
s = "DZSWJ_TGC=2AABEEDF9BA4313412394D3D0A42B135;SERVERID=36c2818b5ac0d4483a0fe23231e6f85e|1564977996|1564977959;TGC=TGT-106939-PXnS5RmN4czS9gVimhu2ig1YdhzYiPscKWAOUeSr1yn6zpcbDs-gddzswj;acw_tc=2f6a1fdc15649779592098648e121287f3da0e1e9c8b3c1bb31d857fde0d0a;JSESSIONID=4F52DF745488249DFBCED90A0336CD1D"
print get_url
headers = {
"Connection":
"keep-alive",
"Pragma":
"no-cache",
"Cache-Control":
"no-cache",
"Upgrade-Insecure-Requests":
"1",
"User-Agent":
"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.90 Safari/537.36",
"Accept":
"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
"Referer":
"www.etax-gd.gov.cn",
"Accept-Encoding":
"gzip, deflate, br",
"Accept-Language":
"zh-CN,zh;q=0.9",
"Referer":"https://www.etax-gd.gov.cn/sbzs-cjpt-web/biz/sbqc/sbqc_aqsb/setting/lhSbbbs.jsp",
"Cookie": s}            

r = requests.get(get_url,headers=headers)
print r.content
