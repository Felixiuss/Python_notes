import socket
import threading
import time
from concurrent.futures import ThreadPoolExecutor

host = socket.gethostbyname(socket.gethostname())  # эквивалент '127.0.0.1'
port = 0  # 0 потомучто клиент подключается к сети, а не создает ее
server = ("127.0.0.1", 9090)  # кортеж - хост(адрес сервера к которому мы подключаемся) и порт
key = 8194  # служит ключем для шифрования данных
join = False  # проверяет статус подключения пользователя
shutdown = False


def receving(name, sock):  # name - играет роль как self
    """Функция позволяет принимать данные от другого пользователя"""
    while not shutdown:  # TODO
        try:
            while True:
                data, addr = sock.recvfrom(1024)  # принятие сообщения с другого клиента
                # print(data.decode("utf-8"))

                # Begin - блок для расфифровки сообщения
                decrypt = ""
                k = False
                for x in data.decode("utf-8"):
                    if x == ":":
                        k = True
                        decrypt += x
                    elif k is False or x == " ":
                        decrypt += x
                    else:
                        decrypt += chr(ord(x) ^ key)
                print(decrypt)
                # End

                time.sleep(0.2)
        except:  # если произойдет то просто пропустить
            pass #  TODO


with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:  # создаем сокет UDP
    s.bind((host, port))  # метод для подключения
    s.setblocking(0)  # защищает от ошибок

    alias = input("Enter You name: ")  #  созданте вводной строки

    rT = threading.Thread(target=receving, args=("RecvThread", s))  # создание потоков для того чтобы можно было
    rT.start()                                                      # отправлять и получать сообщения одновременно

    # цикл служит для отправки на сервер
    while shutdown is False:  # пока клиент не вышел
        if join is False:     # если пользователь еще не присоеденен
            s.sendto(("["+alias + "] => join chat ").encode("utf-8"), server)  # отправляем сообщение о присоединении
            join = True  # указываем то что мы подключились
        else:
            try:
                message = input()

                # Begin - блок для шифрования сообщения (xor шифрование)
                crypt = ""
                for i in message:
                    crypt += chr(ord(i) ^ key)
                message = crypt
                # End

                if message != "":  # если сообщение не пустое отправляет его на сервер, иначе - не отправляет
                    s.sendto(("["+alias + "] :: "+message).encode("utf-8"), server)  # имя, сообщение + закодировать и отпр.

                time.sleep(0.2)  # задержка чтобы связб небыла мгновенной ?
            except:  # например если пользователь вышел : ctl-c
                s.sendto(("["+alias + "] <= left chat ").encode("utf-8"), server)
                shutdown = True

    rT.join()
    rT.close()



 # with ThreadPoolExecutor() as executor:
 #        future = executor.submit(receving, s)
 #        # print(future.result())
