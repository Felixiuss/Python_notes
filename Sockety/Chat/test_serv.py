import socket
import time

host = "127.0.0.1"  # правильней писать так(если поменяется адресс)
port = 9090

# список в котором хранятся адреса клиента(для того чтобы при отправке сообщения - оно приходило
# только другим, а ему не дублировалось)
clients = []

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # объявление протокола (UDP)
s.bind((host, port))  # создание порта

print("[ Server Started ]")

while True:
    try:
        data, addr = s.recvfrom(1024)  # данные сообщения, адресс отправителя и в байтах максимальный размер сообщения

        if addr not in clients:  # если адреса нет в списке клиентов(новый клиент)
            clients.append(addr)  # добавить адрес

        # переменная нужна для того чтобы отобразить текущее время(когда сообщение было отправлено)
        itsatime = time.strftime("%Y-%m-%d-%H.%M.%S", time.localtime())

        # ip адресс отправителя, личный адресс и время(отправки, выхода...)
        print("[" + addr[0] + "]=[" + str(addr[1]) + "]=[" + itsatime + "]/", end="")
        print(data.decode("utf-8"))  # декодирование сообщения которое отправил пользователь

        for client in clients:  # если адрес не равняется тому кто отпрвляет
            if addr != client:  # сообщение - тогда отправляем
                s.sendto(data, client)
    except:
        print("\n[ Server Stopped ]")
        break

s.close()
