# Python-request[官方文档](https://requests.readthedocs.io/zh_CN/latest/)
----------


## 安装requests
> `pip install requests`

## 使用requests

### 导入requests

> `import requests`

* requests的7种方法

| 方法                 | 说明                                           |
| -------------------- | ---------------------------------------------- |
| `requests.request()` | 构造一个请求，支撑以下各方法的基础方法         |
| `requests.get()`     | 获取HTML网页的主要方法，对应于HTTP的GET        |
| `requests.head()`    | 获取HTML网页头信息的方法，对应于HTTP的HEAD     |
| `requests.post()`    | 向HTML网页提交POST请求的方法，对应于HTTP的POST |
| `requests.put()`     | 向HTML网页提交PUT请求的方法，对应于HTTP的PUT   |
| `requests.patch()`   | 向HTML网页提交局部修改请求，对应于HTTP的PATCH  |
| `requests.delete()`  | 向HTML页面提交删除请求，对应于HTTP的DELETE     |

### Response对象的属性

>`r = requests.get('https://www.baidu.com')`

| 属性                  | 说明                                             |
| --------------------- | ------------------------------------------------ |
| `r.status_code`       | HTTP请求的返回状态，200表示连接成功，404表示失败 |
| `r.text`              | HTTP响应内容的字符串形式，即，url对应的页面内容  |
| `r.encoding`          | 从HTTP header中猜测的响应内容编码方式            |
| `r.apparent_encoding` | 从内容中分析出的响应内容编码方式（备选编码方式） |
| `r.content`           | HTTP响应内容的二进制形式                         |

### 参数使用

* **kwargs:控制访问的参数，均为可选项

> `requests.request(method,url,**kwargs)`

#### params:字典或字节序列，作为参数增加到url中
```python
kv = { 
        'key1' : 'value1',
        'key2 ': 'value2'
     }
r = requests.request('GET','http://python123.io/ws',params=kv)
print(r.url)
# http://python123.io/ws?key1=value1&key2=value2
```

>`requests.request(method,url,**kwargs)`

#### cookies:向服务器发送cookie

```python
cookie = { ' key1' : 'value1', 'key2 ' : 'value2'}
r = requests.request('POST','http://python123.io/ws',cookies=cookie)
>>>r = requests.request( 'POST'，'http://python123.io/ws ', cookies=cookie)
```



> `requests.request(method,url,**kwargs)`

#### data:字典、字节序列或文件对象，作为Request的内容
```python
kv = { ' key1' : 'value1', 'key2 ' : 'value2'}
r = requests.request('POST','http://python123.io/ws',data=kv)

>>>r = requests.request( 'POST'，'http://python123.io/ws ', data=body)
```

> `requests.request(method,url,**kwargs)`

#### headers:字典，HTTP定制头
```python
hd = { ' user-agent' : 'Chrome/10'}
r = requests.request( 'POST'， 'http://python123.io/ws ', headers=hd)
```

> `requests.request(method,url,**kwargs)`

#### files:字典类型，传输文件
```python
fs = { 'file' : open( 'data.xls', 'rb' )}
r = requests.request( ' POST','http://python123.io/ws',files=fs)
```

> `requests.request(method,url,**kwargs)`

#### timeout:设定超时时间，秒为单位
```python
r = requests.request( 'GET'， 'http:/ /www.baidu.com', timeout=10)
```

> `requests.request(method,url,**kwargs)`

#### proxies:字典类型，设定访问代理服务器，
```python
pxs = { 'http' : 'http: //user:pass@10.10.10.1:1234'}
r = requests.request( 'GET'， 'http:/ /www.baidu.com'， proxies=pxs)
```






