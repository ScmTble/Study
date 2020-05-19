import requests
import re
from bs4 import BeautifulSoup
def get():
	#模拟浏览器，防止请求被拒绝
    url='https://www.tianqi.com/xiangyang/15/'
    headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 \
    (KHTML, like Gecko) Chrome/57.0.2987.98 Safari/537.36 LBBROWSER"}
	#获取网络内容
    r=requests.get(url,headers=headers)
    r.raise_for_status()
    r.encoding ='utf-8'
    data=r.text
    #用Beautiful库解析
    soup=BeautifulSoup(data,'html.parser')
    temp=soup.p.string
    #替换
    temp=temp.replace('，','.')
    temp=temp.replace(',','.')
    #将字符串分割，分割符号为".",其结果为列表类型
    lst=temp.split('.')
    return lst
print(get())
