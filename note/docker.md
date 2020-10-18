# docker使用
----------
## 1.docker配置（CentOS）
* 安装所需的软件包

> `sudo yum install yum-utils device-mapper-persistent-data lvm2`

* 使用官方源地址下载(可换成其他源)

>`sudo yum-config-manager --add-repo https://download.docker.com/linux/centos/docker-ce.repo`

* 下载docker

>`sudo yum install docker-ce`

* 启动docker

>`sudo systemctl start docker`

* 设置开机自启

>`sudo systemctl enable docker`

* 配置镜像仓库源

>`sudo vi /etc/docker/daemon.json`

```
{

"registry-mirrors": [

"https://l6exhyvs.mirror.aliyuncs.com",
"https://registry.docker-cn.com"

]
}
保存后重启docker
```
-------
## docker使用
* 检验docker是否安装成功

>`docker -v`

>`docker run hello-world`

* 拉取镜像

>`docker pull [镜像名]:[标签Tag]`

* 列出镜像

> `docker images`

* 新建并启动容器    

>`docker run [option] [容器名]`

>`docker run -d –p 8800:80 nginx`

```
--name 为容器指定一个名称；
-d 容器启动后进入后台，并返回容器 ID，即启动守护式容器；
-P 随机端口映射；
-p 80:8080 将本地 80 端口映射到容器的 8080 端口；
bash 容器启动以后，内部第一个执行的命令。这里启动 bash，保证用户可以使用 Shell；
-i 以交互模式运行容器，通常与 -t 同时使用；
-t 为容器重新分配一个伪输入终端，容器的 Shell 会映射到当前的 Shell，然后在本机窗口输入的命令，就会传入容器，通常与 -i 同时使用；
--rm 在容器终止运行后自动删除容器文件；
--restart=always 设置容器自启动；
-v /xxx:/yyy 映射命令，把本机的 xxx 目录映射到容器中的 yyy 目录，也就是说改变本机的 xxx 目录下的内容， 容器 yyy 目录中的内容也会改变；


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

```
终止运行的容器文件，依然会占据硬盘空间，可以使用 docker container rm 命令删除，-f 强制删除可以删除正在运行的容器
```

* 在容器中拷贝文件到外部

>`docker cp [容器ID]/[容器Names]:[要拷贝的文件目录] [本机目录] # 容器文件拷贝到本机`

>`docker cp [本机目录] [容器ID]/[容器Names]:[要拷贝的文件目录] # 本机文件拷贝到容器`