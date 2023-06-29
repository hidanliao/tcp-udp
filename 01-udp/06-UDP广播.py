import socket

# 1. 创建套接字
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# 2. 设置允许广播
s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

# 3. 准备好对方的ip/port/内容
dest_info = ("<broadcast>", 2425)
send_content = "1:123456789:莉莉:水果电脑:32:有时间么?"
# send_content = "helloworld"

# 4. 发送
s.sendto(send_content.encode("gbk"), dest_info)

# 5. 关闭
s.close()

