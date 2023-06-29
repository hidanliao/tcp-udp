import socket

# 1. 创建套接字(TCP)
# socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client_s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 2. 链接服务器
client_s.connect(("192.168.205.68",8080))

# 3. 发送数据
client_s.send("hello  world".encode("utf-8"))

# 4.关闭套接字
client_s.close()