import socket

# 1. 创建tcp套接字
server_s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 2. 绑定本地信息
server_s.bind(("",7890))

# 3. 将套接字由默认的主动链接模式改为被动模式（监听模块）
server_s.listen(128)

# 4. 等待客户端进行链接(创建新的套接字)
new_s, client_info = server_s.accept()
print(client_info)

# 5. 接受/发送数据
recv_content = new_s.recv(1024)
print(recv_content)

# 6. 关闭套接字
new_s.close()
server_s.close()