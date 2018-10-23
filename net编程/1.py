import socket
def serverFunc():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    addr = ("127.0.0.1", 7852)
    sock.bind(addr)
    data, addr = sock.recvfrom(500)
    print(data)
    print(type(data))

    text = data.decode()
    print(text)
    print(type(text))

    rsp = '我不知道'
    data = rsp.encode()
    sock.sendto(data, addr)

if __name__ == '__main__':
    print("Starting server.......")
    serverFunc()
    print("Ending server......")