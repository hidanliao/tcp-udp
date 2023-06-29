import socket

def send_msg(s):
    """发送数据"""
    # 1. 获取用户要发送的数据
    send_content = input("请输入要发送的数据内容:")

    # 2. 获取对方的ip
    send_ip = input("请输入要发送的目标ip:")

    # 3. 获取对方的port
    send_port = int(input("请输入要发送的目的port:"))

    # 4. 发送数据
    s.sendto(send_content.encode("utf-8"),(send_ip, send_port))
def recv_msg(s):
   """接受数据"""
   recv_content, client_info = s.recvfrom(1024)
   print(">>>%s(%s):%s" % (client_info[0], client_info[1], recv_content.decode("utf-8")))

def main():
    # 1. 创建套接字
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # 2. 绑定信息
    s.bind(("", 7890))

    # 3. 功能选择

    while True:
        print("1: 发送数据")
        print("2: 接受数据")
        print("3: 退出")
        op = input("要进行的操作符号:")

        if op == "1":
            send_msg(s)
        elif op == "2":
            recv_msg(s)
        elif op == "3":
            break

    # 4. 关闭套接字
    s.close()

if __name__ == '__main__':
    main()