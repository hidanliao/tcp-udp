import socket
import time

# 1. 创建一个udp套接字
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# 2. 绑定一个ip和端口
# local_info = ("192.168.205.139", 7788)
local_info = ("", 6666)
s.bind(local_info)

# 2. 发送数据
s.sendto("helloworld123".encode("utf-8"), ("192.168.205.68", 8080))

time.sleep(20)

# 3. 关闭套接字
s.close()