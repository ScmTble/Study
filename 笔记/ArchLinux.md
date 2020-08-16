字体: setfont /usr/share/kdb/consolefonts/LatGrCyr-12x22. psfu. gz

loadkeys改键盘布局

esc和caps互换: 编辑keys.conf(可选)文件
keycode 1 = Caps_Lock
keycode 58 = Escape
然后    loadkeys keys.conf

ip link查看设备
ip link set wlan0 up
iwlist wlan0 scan 扫描wifi
iwlist wlan0 scan | grep ESSID
wpa_passphrase wifi名字 密码 > internet. conf
wpa_supplican -c internet. conf -i wlan0 &
(dhcpcd &)分配ip地址
timedatectl set-ntp true 更新时间


分区：
fdisk -l   查看设备
fdisk 分区
g  

n创建分区：
1：启动分区
编号
开始位置
结束位置(+多少M)
y

     2：swap交换分区
     3号

3：主分区

p查看分区

系统引导分区格式：mkfs. fat -F32 分区
主分区：mkfs. ext4 主分区
swap分区：mkswap 分区
swapon swap分区

配置pacman配置文件：
/etc/pacman.conf
/etc/pacman.d/mirrorlist

挂载：
mount 主分区 /mnt
mkdir /mnt/boot
mount 引导分区 /mnt/boot
开始安装：
pasctrap /mnt base linux linux-firmware
genfstab -U /mnt >> /mnt/etc/fstab

进入系统
arch-chroot /mnt
改时区
ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime
同步时间
hwclock --systohc 
exit退出

改/mnt/etc/local.gen中en_US. UTF-8
进入arch-chroot /mnt
locale-gen
exit

改/mnt/etc/locale.conf
LANG=en_US. UTF-8
如果用Colman
(grup-mkconfig > /boot/grub/grub.cfg)

vim /mnt/etc/hostname
写入名字(sx)

vim /mnt/etc/hosts
127.0.0.1          localhost
::1                       localhost
127.0.0.1          sx. localdomain sx

root密码：
arch-chroot /mnt
passwd

安装引导软件
pacman -S grub efibootmgr intel-ucode os-prober
放grup配置：mkdir /boot/grub
生成配置文件：grub-mkconfig > /boot/grub/grub.cfg

unarmed -m 查看架构
安装: grub-insta……

vim链接到vi
ln -s /usr/bin/vim /usr/bin/vi