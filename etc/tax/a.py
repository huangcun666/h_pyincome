#coding=utf8
import requests

headers = {
"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.90 Safari/537.36",
"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
"Referer": "https://www.etax-gd.gov.cn/sso/login?service=https://www.etax-gd.gov.cn/xxmh/html/index_login.html?bszmFrom=1&t=1562144801212",
"Accept-Language": "zh-CN,zh;q=0.9",
"Cookie": "JSESSIONID=1873CFD0E86BFC282A42627F0566E31C; acw_tc=2f6a1fde15620550374206570ed451b6aa90bf5770817f16a648cd920c5d77; TY_SESSION_ID=58ea6962-e143-4f74-850f-c2d7c7a068fe; DZSWJ_TGC=481BCA4D85CEDD20F51C0DBCEF54CE93; TGC=TGT-155668-YdF3rmpmFZmfTZZlc9C73uas2O26PiMBJMur1jhVguQzG1blYm-gddzswj; SERVERID=e78e6f59ff8c1f4281cdd80f4f43e870|1562226941|1562121912"
}



r = requests.get("https://www.etax-gd.gov.cn/xxmh/html/index_login.html",headers=headers)
print r.content
