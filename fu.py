import socket

sk = socket.socket()
address = ("127.0.0.1", 9000)
sk.bind(address)
sk.listen(3)
print("等待...")

while True:
    conn, addr = sk.accept()
    print("连接到",addr)
    while True:
        data = conn.recv(1024)
        if not data:
            print("连接断开!")
            conn.close()
            break
        print(str(data, "utf8"))
        inp = input(">>")
        conn.send(bytes(inp, "utf8"))

#制作:权家乐  想法提供:权家乐
#版权所有 侵权必究
