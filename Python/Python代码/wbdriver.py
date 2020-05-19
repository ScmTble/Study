from selenium import webdriver

wd = webdriver.Chrome()
wd.implicitly_wait(10)

wd.get('https://www.baidu.com')

element = wd.find_element_by_id('kw')

element.send_keys('白月黑羽\n')

# id 为 1 的元素 就是第一个搜索结果
element = wd.find_element_by_id('1')

# 打印出 第一个搜索结果的文本字符串
print(element.get_attribute('innerHTML'))
