import socket

# 1. 创建一个udp套接字
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# 2. 发送数据
s.sendto("helloworld123".encode("utf-8"), ("192.168.205.68", 8080))

# 3. 关闭套接字
s.close()