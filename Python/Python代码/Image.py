import requests
from bs4 import BeautifulSoup
main_html = requests.get('https://www.umei.cc/meinvtupian/meinvxiezhen/8.htm')
main_html.encoding = 'utf-8'
main_page = BeautifulSoup(main_html.text, "html.parser")
a_list = main_page.find("div", class_="TypeList").find_all(
    "a", class_="TypeBigPics")
n = 1
for a in a_list:
    child_url = a.get("href")
    child_html = requests.get(child_url)
    child_html.encoding = 'utf-8'
    child_page = BeautifulSoup(child_html.text, "html.parser")
    img = child_page.find("div", class_="ImageBody").find("img")
    if img:
        # 下载图片
        jpg_src = img.get("src")
        with open(f"./Image/lookk{n}.jpg", 'wb') as f:
            f.write(requests.get(jpg_src).content)
        print("下完第%d张" % n)
        n += 1
