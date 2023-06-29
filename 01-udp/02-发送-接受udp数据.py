import socket

# 1. 创建一个udp套接字
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# 2. 获取需要发送的数据
msg = input("请输入要发送的数据:")

# 3. 发送数据
s.sendto(msg.encode("utf-8"), ("192.168.205.68", 8081))
s.sendto(msg.encode("utf-8"), ("192.168.205.68", 8081))
s.sendto(msg.encode("utf-8"), ("192.168.205.68", 8081))

# 4.接受数据并且打印
recv_msg = s.recvfrom(1024)
# print(recv_msg)
print("%s(%d)>>>%s" % (recv_msg[1][0], recv_msg[1][1], recv_msg[0].decode("gbk")))

# 5. 关闭套接字
s.close()