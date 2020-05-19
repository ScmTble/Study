import re
import requests
from bs4 import BeautifulSoup


def dowmloadPicture(url, num, word):
    for i in range(0, num):
        with open(f"Image/{word}_{i}.jpg", 'wb') as f:
            f.write(requests.get(url[i]).content)


if __name__ == '__main__':  # 主函数入口
    word = input("请输入搜索关键词(可以是人名，地名等): ")
    print("正在查找下载.....")
    page = 'http://image.baidu.com/search/flip?tn=baiduimage&ie=utf-8&word=' + word + '&pn='
    html = requests.get(page)
    url = re.findall('"objURL":"(.*?)",', html.text, re.S)  # 先利用正则表达式找到图片url
    dowmloadPicture(url, 10, word)
    print("下载成功!")
