import requests
from bs4 import BeautifulSoup
import re
n = 55


def dow(url):
    global n
    html = (requests.get(url)).text
    page = BeautifulSoup(html, 'html.parser')
    pic_list = page.find(
        'div', class_='ug-album-detail-content').find_all('img')
    for j in pic_list:
        pic_url = j.get('src')
        with open(f'./Image/look{n}.jpg', 'wb') as f:
            f.write(requests.get(pic_url).content)
        n = n+1


page = (requests.get('https://www.ugirl.com/meinvtupian/p-8.html')).text
html = BeautifulSoup(page, 'html.parser')
text = html.find('div', class_='ug-album').find_all('div',
                                                    class_='ug-album-item-cover')
url_list = re.findall('<a[^>]+href=["\'](.*?)["\']', str(text))
for i in url_list:
    dow(i)
