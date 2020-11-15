# Docker使用

----------
### Docker配置

* CentOS配置，其他系统请查看文档

#### 安装所需的软件包

> `sudo yum install yum-utils device-mapper-persistent-data lvm2`

#### 使用官方源地址下载(可换成其他源)

>`sudo yum-config-manager --add-repo https://download.docker.com/linux/centos/docker-ce.repo`

#### 下载docker

>`sudo yum install docker-ce`

#### 启动docker

>`sudo systemctl start docker`

#### 设置开机自启

>`sudo systemctl enable docker`

#### 配置镜像仓库源

>`sudo vim /etc/docker/daemon.json`

```shell
{
	"registry-mirrors": 
	[
	"https://l6exhyvs.mirror.aliyuncs.com",
	"https://registry.docker-cn.com"
	]
}
# 保存后重启docker
```
-------
### Docker使用
#### 检验docker是否安装成功

>`docker -v`

>`docker run hello-world`

#### 查看日志

>`docker logs <容器名或ID>`

#### 拉取镜像

>`docker pull [镜像名]:[标签Tag]`

#### 列出镜像

> `docker images`

#### 删除镜像

>`docker rmi <imagename>`

#### 新建并启动容器    

>`docker run [option] [容器名]`

>`docker run -d –p 80:80 nginx`

```shell
-a stdin: #指定标准输入输出内容类型，可选 STDIN/STDOUT/STDERR 三项；

-d: #后台运行容器，并返回容器ID；

-i: #以交互模式运行容器，通常与 -t 同时使用；

-P: #随机端口映射，容器内部端口随机映射到主机的端口

-p: #指定端口映射，格式为：主机(宿主)端口:容器端口

-t: #为容器重新分配一个伪输入终端，通常与 -i 同时使用；

--name="nginx-lb": #为容器指定一个名称；

--dns 8.8.8.8: #指定容器使用的DNS服务器，默认和宿主一致；

--dns-search example.com: #指定容器DNS搜索域名，默认和宿主一致；

-h "mars": #指定容器的hostname；

-e username="ritchie": #设置环境变量；

--env-file=[]: #从指定文件读入环境变量；

--cpuset="0-2" or --cpuset="0,1,2": #绑定容器到指定CPU运行；

-m :#设置容器使用内存最大值；

--net="bridge": #指定容器的网络连接类型，支持 bridge/host/none/container: 四种类型；

--link=[]: #添加链接到另一个容器；

--expose=[]: #开放一个端口或一组端口；

--volume , -v: #绑定一个卷

-v /xxx:/yyy 映射命令，把本机的 xxx 目录映射到容器中的 yyy 目录，也就是说改变本机的 xxx 目录下的内容， 容器 yyy 目录中的内容也会改变；

bash #容器启动以后，内部第一个执行的命令。这里启动 bash，保证用户可以使用 Shell；

--rm #在容器终止运行后自动删除容器文件；

--restart=always #设置容器自启动；

# 设置容器在docker启动时自动启动
docker container update --restart=always [容器名字]
```

* 启动容器

>`docker start [容器ID]/[容器Names]`

* 重启容器

>`docker restart [容器ID]/[容器Names]`

* 终止容器运行

>`docker kill [容器ID] # 强行终止，相当于向容器里面的主进程发出 SIGKILL 信号，那些正在进行中的操作会全部丢失`

* 从容终止
>`docker stop [容器ID] # 从容终止，相当于向容器里面的主进程发出 SIGTERM 信号，然后过一段时间再发出 SIGKILL 信号`


* 删除容器
>`docker rm [容器ID]`

```shell
# 终止运行的容器文件，依然会占据硬盘空间，可以使用 docker container rm 命令删除，-f 强制删除可以删除正在运行的容器
```

* 在容器中拷贝文件到外部

>`docker cp [容器ID]/[容器Names]:[要拷贝的文件目录] [本机目录] # 容器文件拷贝到本机`

>`docker cp [本机目录] [容器ID]/[容器Names]:[要拷贝的文件目录] # 本机文件拷贝到容器`

* 进入容器

>`docker attach <容器ID>`

* 在运行的容器中执行命令

>`docker exec -it [容器ID]/[容器Names] bash`

#### Docker命令

* 查看cpu占用

> `docker stats`

* 获取容器/镜像的元数据

> `docker inspect <NAME|ID>`









### Docker数据卷

#### 前言

> 数据卷是被设计用来持久化数据的，它的生命周期独立于容器，Docker 不会在容器被删除后自动删除 数据卷，并且也不存在垃圾回收这样的机制来处理没有任何容器引用的 数据卷.



#### 数据卷操作

```shell
[root@iZkujhw1coiih6Z ~]# docker volume --help

Usage:  docker volume COMMAND

Manage volumes

Commands:
  create      Create a volume   # 创建一个数据卷
  inspect     Display detailed information on one or more volumes # 显示一个或多个卷的详细信息
  ls          List volumes      # 列出所有的数据卷
  prune       Remove all unused local volumes # 移除所有的未使用的数据卷
  rm          Remove one or more volumes # 移除一个或多个数据卷

Run 'docker volume COMMAND --help' for more information on a command.
```

#### 数据卷实操示例

1. 创建一个数据卷

```shell
$ docker volume create my-vol
```

2. 列出所有的数据卷

```shell
$ docker volume ls

DRIVER              VOLUME NAME
local               my-vol
```

3. 查看数据卷信息

```shell
$ docker volume inspect my-vol
[
    {
        "Driver": "local",
        "Labels": {},
        "Mountpoint": "/var/lib/docker/volumes/my-vol/_data",
        "Name": "my-vol",
        "Options": {},
        "Scope": "local"
    }
]
```

4. 启动一个挂载数据卷的容器

```shell
$ docker run -d -P \
    --name web \
    # -v my-vol:/usr/share/nginx/html \
    --mount source=my-vol,target=/usr/share/nginx/html \
    nginx:alpine
    
# 在用 docker run 命令的时候，使用 --mount 标记来将 数据卷 挂载到容器里。在一次 docker run 中可以挂载多个 数据卷。

# 创建一个名为 web 的容器，并加载一个 数据卷 到容器的 /usr/share/nginx/html 目录。

# 如果未指定挂载到宿主的具体位置,docker会进行匿名挂载(挂载到随机生成名称的文件)
```

5. 查看 `web` 容器的信息

```shell
$ docker inspect web
```

```json
"Mounts": [
    {
        "Type": "volume",
        "Name": "my-vol",
        "Source": "/var/lib/docker/volumes/my-vol/_data",
        "Destination": "/usr/share/nginx/html",
        "Driver": "local",
        "Mode": "",
        "RW": true,
        "Propagation": ""
    }
],
```

6. 删除数据卷

```shell
$ docker volume prune
# 无主的数据卷可能会占据很多空间
# 如果需要在删除容器的同时移除数据卷。可以在删除容器的时候使用 docker rm -v 这个命令。
```

----------------







### DockerFile

#### Docker参数

```dockerfile
FROM ImageName          						# 基础镜像，一切从这里开始构建
```

```dockerfile
MAINTAINER <key>=<value> <key>=<value> ...		# 镜像信息（MAINTAINER已弃用改为LABEL）
```

```dockerfile
RUN <command>/["executable", "param1"]			# 镜像构建的时候需要运行的命令
CMD	<command>									# 指定这个容器启动的时候要运行的命令,只有最后一个会生效
                                                #CMD 在docker run 时运行。
                                                #RUN 是在 docker build。
```

```dockerfile
ADD (COPY) <源路径1>...  <目标路径>
ADD (COPY) ["<源路径1>",...  "<目标路径>"]
#ADD 指令和 COPY 的使用格式一致（同样需求下，官方推荐使用 COPY）。功能也类似，不同之处如下：
#ADD 优点：在执行 <源文件> 为 tar 压缩文件的话，压缩格式为 gzip, bzip2 以及 xz 的情况下，会自动复制并解压到 <目标路径>。
#ADD 缺点：在不解压的前提下，无法复制 tar 压缩文件。会令镜像构建缓存失效，从而可能会令镜像构建变得比较缓慢。具体是否使用，可以		  根据是否需要自动解压来决定。
```

```dockerfile
ENV <key> <value>
ENV <key1>=<value1> <key2>=<value2>...
```

```dockerfile
EXPOSE <port> [<port>/<protocol>...] 
#EXPOSE 指令实际上并不发布端口。它作为一种文档，介于构建映像的人和运行容器的人之间，关于打算发布哪些端口。要在运行容器时实际发布端口，可以使用 docker run 上的-p 标志发布和映射一个或多个端口，或使用-p 标志发布所有公开的端口并将它们映射到高阶端口。
```

```dockerfile
VOLUME            #挂载的目录
ENTRYPOINT        #指定这个容器启动的时候要运行的命令，可以追加命令
ONBUILD           #当构建一个被继承DockerFile这个时候就会运行ONBUILD的指令。触发指令。
WORKDIR           #镜像的工作目录
```

#### Dockerfile使用

```shell
docker build -f /path/to/a/Dockerfile .		   #-f 指定Dockerfile文件位置
docker build -t runoob/ubuntu:v1 .			   #-t 为镜像打上标签
docker build github.com/creack/docker-firefox  #使用网络位置的Dockerfile创建镜像。
```



#### Dockerfile示例

**Dockerfile构建nginx镜像**

```dockerfile
FROM centos
 
RUN ping -c 1 www.baidu.com
RUN yum -y install gcc make pcre-devel zlib-devel tar zlib && yum -y install vim
ADD nginx-1.15.2.tar.gz /usr/src/
RUN cd /usr/src/nginx-1.15.2 \
    && mkdir /usr/local/nginx \
    && ./configure --prefix=/usr/local/nginx && make && make install \
    && ln -s /usr/local/nginx/sbin/nginx /usr/local/sbin/ \
    && nginx
 
RUN rm -rf /usr/src/nginx-1.15.2
 
EXPOSE 80
```

















-----------------------------------------------


### Docker网络

#### Docker网络模式

**安装Docker时，它会自动创建三个网络，bridge（创建容器默认连接到此网络）、 none 、host**

| 网络模式  | 简介                                                         |
| --------- | ------------------------------------------------------------ |
| Host      | 容器将不会虚拟出自己的网卡，配置自己的IP等，而是使用宿主机的IP和端口。 |
| Bridge    | 此模式会为每一个容器分配、设置IP等，并将容器连接到一个docker0虚拟网桥，通过docker0网桥以及Iptables nat表配置与宿主机通信。（默认模式）（自己创建也用） |
| None      | 该模式关闭了容器的网络功能。                                 |
| Container | 创建的容器不会创建自己的网卡，配置自己的IP，而是和一个指定的容器共享IP、端口范围。（用出少，局限大） |

#### Docker网络操作

```shell
[root@iZkujhw1coiih6Z ~]# docker network --help

Usage:  docker network COMMAND

Manage networks

Commands:
  connect     Connect a container to a network   #将容器连接到一个网络
  create      Create a network					 #创建一个自定义网络
  disconnect  Disconnect a container from a network #断开容器与网络的连接
  inspect     Display detailed information on one or more networks # 显示一个或多个网络上的详细信息
  ls          List networks # 列出所有docker网络
  prune       Remove all unused networks # 删除所有未使用的网络
  rm          Remove one or more networks # 移除一个或者多个网络

Run 'docker network COMMAND --help' for more information on a command.

```

1. 创建一个新的 Docker 网络

```shell
docker network create -d bridge my-net
docker network create --driver bridge --subnet 192.168.0.0/16 --getway 192.168.0.1 my-net
# -d 指定 上述的网络模式（bridge）
```

2. 运行一个容器并连接到自建的网络

```shell
docker run -it --rm --name busybox1 --network my-net busybox sh
```

```shell
[root@iZkujhw1coiih6Z ~]# docker network create --help

Usage:  docker network create [OPTIONS] NETWORK

Create a network

Options:
      --attachable           Enable manual container attachment
      --aux-address map      Auxiliary IPv4 or IPv6 addresses used by Network driver (default map[])
      --config-from string   The network from which copying the configuration
      --config-only          Create a configuration only network
  -d, --driver string        Driver to manage the Network (default "bridge")
      --gateway strings      IPv4 or IPv6 Gateway for the master subnet #主子网的IPv4或IPv6网关
      --ingress              Create swarm routing-mesh network
      --internal             Restrict external access to the network
      --ip-range strings     Allocate container ip from a sub-range
      --ipam-driver string   IP Address Management Driver (default "default")
      --ipam-opt map         Set IPAM driver specific options (default map[])
      --ipv6                 Enable IPv6 networking
      --label list           Set metadata on a network
  -o, --opt map              Set driver specific options (default map[])
      --scope string         Control the network's scope
      --subnet strings       Subnet in CIDR format that represents a network segment # 表示网络段的CIDR格式子网
```



--------------------------------

### Docker Compose

#### 安装Docker Compose

1. 下载源码编译安装

2. pip安装

>`pip install docker-compose`

3. 查看Docker-Compose版本

>`docker-compose version`

#### Docker Compose三步骤

- 使用 Dockerfile 定义应用程序的环境。
- 使用 docker-compose.yml 定义构成应用程序的服务，这样它们可以在隔离环境中一起运行。
- 最后，执行 docker-compose up 命令来启动并运行整个应用程序。

#### Compose实操

##### 1.为项目创建目录

```shell
$ mkdir composetest
$ cd composetest
```

##### 2.创建app.py

```python
import time

import redis
from flask import Flask

app = Flask(__name__)
cache = redis.Redis(host='redis', port=6379)

def get_hit_count():
    retries = 5
    while True:
        try:
            return cache.incr('hits')
        except redis.exceptions.ConnectionError as exc:
            if retries == 0:
                raise exc
            retries -= 1
            time.sleep(0.5)

@app.route('/')
def hello():
    count = get_hit_count()
    return 'Hello World! I have been seen {} times.\n'.format(count)
```

> 在此示例中，“ redis”是应用程序网络上的redis容器的主机名。我们使用Redis的默认端口6379

##### 3.创建requirements.txt

```shell
flask
redis
```

##### 4.创建Dockerfile

```dockerfile
FROM python:3.7-alpine
WORKDIR /code
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
RUN apk add --no-cache gcc musl-dev linux-headers
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
EXPOSE 5000
COPY . .
CMD ["flask", "run"]
```

##### 5.创建docker-compoes.yml

```yml
version: "3.8"
services:
  web:
    build: .
    ports:
      - "5000:5000"
  redis:
    image: "redis:alpine"
```

##### 6.启动服务

```shell
$ docker-compose up
```
























----------
### Docker安装nginx

#### 了解docker中默认路径

```shell
conf# 配置文件位置
/etc/nginx/nginx.conf

html# 静态文件位置
/usr/share/nginx/html

log# 日志文件位置
/var/log/nginx
```

#### 启动临时容器

>`docker run --rm --name tmp-nginx-container -d nginx`

#### 新建本地目录

* 用来获取nginx配置文件，如果有可不需要此操作

>`mkdir -p /docker/nginx/`

#### 拷贝临时容器默认文件到默认路径

* 用来获取nginx配置文件，如果有可不需要此操作

>`docker cp tmp-nginx-container:/etc/nginx/nginx.conf /docker/nginx/nginx.conf`

>`docker cp -a tmp-nginx-container:/usr/share/nginx/html /docker/nginx`

>`docker cp tmp-nginx-container:/etc/nginx/conf.d /docker/nginx/conf.d`


>`docker rm -f tmp-nginx-container`

#### 重新映射容器启动

```shell
docker run --name mynignx -e TZ="Asia/Shanghai" -d -p 80:80 -v /
/docker/nginx/html:/usr/share/nginx/html -v /docker/nginx/nginx.conf:/etc/nginx/nginx.conf/
-v /docker/nginx/conf.d:/etc/nginx/conf.d -v /docker/nginx/logs:/var/log/nginx nginx
```











### Docker安装mysql

>`docker run -itd --name mysql -p 3306:3306 -e MYSQL_ROOT_PASSWORD=123456 mysql`





### Docker安装teamspeak

```shell
docker pull teamspeak
docker run -p 9987:9987/udp -p 10011:10011 -p 30033:30033 -e TS3SERVER_LICENSE=accept teamspeak
```

