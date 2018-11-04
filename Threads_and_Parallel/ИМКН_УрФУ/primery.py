import threading

"""
Пример показывает создание и запуск потоков и передачу в них функции
"""

'''
def action():
    for _ in range(100):
        print('hello from action', threading.current_thread().name)


for _ in range(10):
    thread = threading.Thread(target=action)  # создание и передача потока в функцию
    thread.start()  # запуск потока

"""
Тот же пример но с использыванием класса
"""


class Worker(threading.Thread):
    def run(self):      # метод который необходимо переопределить для автозапуска при вызове потока
        for _ in range(100):
            print('hello from Worker', threading.current_thread().name)


for _ in range(10):
    thread = Worker()  # создание экземрляра класса
    thread.start()  # автозапуск метода run()
'''

# -------------------------------------------------------------------------------

import time
"""
Пример показывает проблему - если не использовать блокировку тогда 
несколько потоков захватывают выполнение и вывод искажается
"""
'''
counter = 0  # по логике должно получится 1000

def inc():
    global counter
    v = counter
    time.sleep(0.001)
    counter = v + 1

pool = []

for _ in range(1000):
    th = threading.Thread(target=inc)
    th.start()
    pool.append(th)

for th in pool:
    th.join()  # закрытие потока и освобождение памяти

print(counter)  # вывод будет около 100


"""
Тот же пример но с использованием блокировок который выводит ожыдаемый результат
"""

counter = 0
lock = threading.Lock()  # создание блокировки

def inc():
    global counter
    lock.acquire()  # захват объекта выполнения
    v = counter
    time.sleep(0.001)
    counter = v + 1
    lock.release()  # освобождение

pool = []

for _ in range(1000):
    th = threading.Thread(target=inc)
    th.start()
    pool.append(th)

for th in pool:
    th.join()  # закрытие потока и освобождение памяти

print(counter)

"""
Тот же пример но с использованием менеджера контекста для 
автоматического освобождения(закрытия) ресурсов
"""

counter = 0
lock = threading.Lock()  # создание блокировки

def inc():
    global counter
    with lock:          # менеджер контекста
        v = counter
        time.sleep(0.001)
        counter = v + 1

pool = []

for _ in range(1000):
    th = threading.Thread(target=inc)
    th.start()
    pool.append(th)

for th in pool:
    th.join()  # закрытие потока и освобождение памяти

print(counter)
'''
# ------------------------------------------------------------------------------

"""
Пример взаимной блокировки
"""
'''
lock1 = threading.Lock()
lock2 = threading.Lock()

def good():
    with lock1:
        time.sleep(0.001)
        with lock2:
            print('good')

def bad():
    with lock2:
        with lock2:
            print('bad')

threading.Thread(target=good).start()
threading.Thread(target=bad).start()
'''