# from socket import *
#
# HOST = '127.0.0.1'  # or 'localhost'
# PORT = 21567
# BUFSIZ = 1024
# ADDR = (HOST, PORT)
#
# tcpCliSock = socket(AF_INET, SOCK_STREAM)
# tcpCliSock.connect(ADDR)
# while True:
#     data = input('> ')
#     if not data:
#         break
#     tcpCliSock.sendall(bytes(data, 'utf-8'))
#     data = tcpCliSock.recv(BUFSIZ)
#     if not data:
#         break
#     print(data.decode('utf-8'))
# tcpCliSock.close()

# --------------------------------------------------------------------------------------------
# Создание клиента с применением модуля SocketServer

# from socket import *
# HOST = 'localhost'
# PORT = 21567
# BUFSIZ = 1024
# ADDR = (HOST, PORT)
#
# while True :
#    tcpCliSock = socket(AF_INET, SOCK_STREAM)
#    tcpCliSock.connect(ADDR)
#    data = input('> ')
#    if not data:
#        break
#    tcpCliSock.sendall(bytes(data, 'utf-8'))
#    data = tcpCliSock.recv(BUFSIZ)
#    if not data:
#        break
#    print(data.strip())
#    tcpCliSock.close()

# -----------------------------------------------------------------------------------------------

# Хабр-хабр
import socket

sock = socket.socket()
sock.connect(('localhost', 9090))
sock.send(b'hello, world!')

data = sock.recv(1024)
sock.close()

print(data)
