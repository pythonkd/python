import socket

def clientFunc():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    text = '你说的啥'
    data = text.encode()
    sock = text.encode()
    sock.sendto(data, ("127.0.0.1", 7852))
    data, addr = sock.recvfrom(200)
    data = data.decode()
    print(text)

if __name__ == '__main__':
    clientFunc()