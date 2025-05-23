import requests
from bs4 import BeautifulSoup
import selenium
#url1 = "http://www.crazyant.net"
#r=requests.get(url1)
#print(r.status_code,"\n")
#print(r.headers,"\n")
#print(r.encoding,"\n")
#print(r.text,"\n")
#print(r.cookies,"\n")
#print("ok","\n")

#url2="http://www.baidu.com"
#w=requests.get(url2)
#print(w.status_code,"\n")
#print(w.headers,"\n")
#print(w.encoding,"\n")
#w.encoding="UTF-8"
#print(w.encoding,"\n")
#print(w.text,"\n")

#print("ok")

url3="http://www.httpcn.com"
g=requests.get(url3)
print(g.status_code,"\n")
print(g.encoding,"\n")
print(g.headers,"\n")
g.encoding="UTF-8"
print(g.text,"\n")