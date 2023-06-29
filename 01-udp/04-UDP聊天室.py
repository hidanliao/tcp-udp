import socket

# 1. 创建套接字
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# 2. 绑定信息
s.bind(("",7890))

# 3. 接受数据并且打印
while True:
    content, client_info = s.recvfrom(1024)
    print(s.recvfrom(1024))
    try:
        print("%s(%d):%s" % (client_info[0], client_info[1], content.decode("utf-8")))
    except:
        print("格式有误")
# 4. 关闭套接字
s.close()