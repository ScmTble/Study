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









### 安装portainer 

```shell
# Docker可视化管理工具
```



#### 安装portainer

```shell
docker run -d -p 8080:9000 --restart=always -v /var/run/docker.sock:/var/run/docker.sock --privileged=true portainer/portainer
```

#### 设置密码登录，选择local登录



### Docker数据卷





 

### DockerFile使用







### Docker网络















### Docker Compose使用

#### 安装Docker Compose

1. 下载源码编译安装

2. pip安装

>`pip install docker-compose`

3. 查看Docker-Compose版本

>`docker-compose version`




















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

>`docker run --name tmp-nginx-container -d nginx`

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