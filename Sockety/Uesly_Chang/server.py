# Создание сокета

from socket import *
from time import ctime

# HOST = '127.0.0.1'
# PORT = 21567
# BUFSIZ = 1024
# ADDR = (HOST, PORT)
#
# tcpSerSock = socket(AF_INET, SOCK_STREAM)
# tcpSerSock.bind(ADDR)
# tcpSerSock.listen(5)
#
# while True:
#     print('ожидаю подключение... ')
#     tcpCliSock, addr = tcpSerSock.accept()
#     print('...подключен по адресу:', addr)
#
#     while True:
#         data = tcpCliSock.recv(BUFSIZ)
#         if not data:
#             break
#         tcpCliSock.sendall(bytes(ctime(), 'utf-8'))
#         tcpCliSock.sendall(data)
#
#     tcpCliSock.close()
# # tcpSerSock.close()

# -------------------------------------------------------------------------------------------

# Создание сервера ТСР с применением модуля SocketServer

# from socketserver import TCPServer as TCP, StreamRequestHandler as SRH
# from time import ctime
#
# HOST = ''
# PORT = 21567
# ADDR = (HOST, PORT)
#
#
# class MyRequestHandler(SRH):
#     def handler(self):
#         print('...conected from: ', self.client_address, self.write('[%s %s' % (ctime(), self.rfile.readline())))
#
#
# tcpServ = TCP(ADDR, MyRequestHandler)
# print('waiting for connection...')
# tcpServ.serve_forever()

# ------------------------------------------------------------------------------------------------

# Хабр-хабр

import socket

sock = socket.socket()
sock.bind(('', 9090))
sock.listen(1)
conn, addr = sock.accept()

print('connected: ', addr)

while True:
    data = conn.recv(1024)
    if not data:
        break
    conn.send((data.upper()))

conn.close()
