import platform
import socket
import os
import threading
import time
import sys
IPList = []
PortList = []
def my_os():  # 1、获取本机操作系统名称
    return platform.system()
def my_ip():  # 2、获取本机IP地址
    return socket.gethostbyname(socket.gethostname())
def ping_ip(ip):  # 3、ping指定IP判断主机是否存活
    global IPList
    if my_os() == 'Windows':
        p_w = 'n'
    elif my_os() == 'Linux':
        p_w = 'c'
    else:
        print('不支持此操作系统')
        sys.exit()
    output = os.popen('ping -%s 1 %s' % (p_w, ip)).readlines()
    for w in output:
        if str(w).upper().find('TTL') >= 0:
            # print(ip,'Power On')
            IPList.append(ip)
def ping_all(ip):  # 4、ping所有IP获取所有存活主机
    pre_ip = (ip.split('.')[:-1])
    for i in range(1, 256):
        now_ip = ('.'.join(pre_ip) + '.' + str(i))
        # ping_ip(add)
        threading._start_new_thread(ping_ip, (now_ip,))
        time.sleep(0.01)
def scan_port(ip, port):  # 5、扫描主机指定端口
    try:
        s = socket.socket()  # （1）建立网络套接字
        s.settimeout(0.000001)  # （2）设置网络超时
        s.connect((ip, port))  # （3）建立连接
        print(ip,port,'Open')                                         #（4）打印端口
        PortList.append((ip, port))
        s.close()  # （5）关闭端口
    except:
        pass
def scan_all_port(ip, max_port):  # 6、扫描主机所有端口
    for port in range(1, max_port):  # （1）循环遍历1到最大端口
        threading._start_new_thread(scan_port, (ip, port))  # （2）启动多线程扫描端口
        time.sleep(0.000001)  # （3）短暂休眠等待
if __name__ == '__main__':
    ping_all(my_ip())
    for ip in IPList:
        print(ip)
        scan_all_port(ip, 8100)
    for port in PortList:
        print(port)