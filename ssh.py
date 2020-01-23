import paramiko
ssh = paramiko.SSHClient()  # 创建SSH对象
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())  # 允许连接不在know_hosts文件中的主机
ip = '192.168.1.9'
port = '22'
username = 'root'
passwd = 'toor'
cmd1 = 'init 6'
ssh.connect(ip, port, username, passwd)  # 连接服务器
def run(cmd):
    stdin, stdout, stderr = ssh.exec_command(cmd)
    print(stdout.read())
run(cmd1)
ssh.close()  # 关闭连接