# пример выполнения программы без применения потоков
"""
from time import sleep, ctime


def loop0():
    print('start loop 0 at: ', ctime())
    sleep(4)
    print('loop 0 done at: ', ctime())


def loop1():
    print('start loop 1 at: ', ctime())
    sleep(2)
    print('loop 1 done at: ', ctime())


def main():
    print('starting at: ', ctime())
    loop0()
    loop1()
    print('all DONE at: ', ctime())


main()
"""
# ---------------------------------------------------------------------------------------------------

# Создание экземпляра Thread с передачей функции
"""
import threading
from time import sleep, ctime

loops = [4, 2]          # секунды


def loop(nloop, nsec):
    print('start loop', nloop, 'at:', ctime())
    sleep(nsec)
    print('loop', nloop, 'done at:', ctime())


def main():
    print('starting at:', ctime())
    threads = []
    nloops = range(len(loops))

    for i in nloops:
        t = threading.Thread(target=loop, args=(i, loops[i]))  # создание потоков
        threads.append(t)

    for i in nloops:            # запуск потоков
        threads[i].start()

    for i in nloops:            # ожидание завершения
        threads[i].join()       # всех потоков

    print('all DONE at:', ctime())


main()
"""
# ---------------------------------------------------------------------------------------------------

# Создание зкэемпnяра Thread и передача вызываемого зкэемпnяра кnасса
"""
import threading
from time import sleep, ctime

loops = [4, 2]


class ThreadFunc(object):

    def __init__(self, func, args, name=''):
        self.name = name
        self.func = func
        self.args = args

    def __call__(self, *args, **kwargs):
        self.func(*self.args)


def loop(nloop, nsec):
    print('start loop', nloop, 'at:', ctime())
    sleep(nsec)
    print('loop', nloop, 'done at:', ctime())


def main():
    print('starting at:', ctime())
    threads = []
    nloops = range(len(loops))

    for i in nloops:
        t = threading.Thread(target=ThreadFunc(loop, (i, loops[i]), loop.__name__))
        threads.append(t)

    for i in nloops:
        threads[i].start()

    for i in nloops:
        threads[i].join()

    print('all DONE at:', ctime())


main()
"""
# -------------------------------------------------------------------------------------------------

# Подкласс Thread и создание экземпляра подкласса
"""
import threading
from time import sleep, ctime

loops = [4, 2]


class MyThread(threading.Thread):

    def __init__(self, func, args, name=''):
        threading.Thread.__init__(self)
        self.name = name
        self.func = func
        self.args = args

    def run(self):
        self.func(*self.args)


def loop(nloop, nsec):
    print('start loop', nloop, 'at:', ctime())
    sleep(nsec)
    print('loop', nloop, 'done at:', ctime())


def main():
    print('starting at:', ctime())
    threads = []
    nloops = range(len(loops))

    for i in nloops:
        t = MyThread(loop, (i, loops[i]), loop.__name__)
        threads.append(t)

    for i in nloops:
        threads[i].start()

    for i in nloops:
        threads[i].join()

    print('all DONE at:', ctime())


main()
"""

# -----------------------------------------------------------------------------------------------

# Сравнение однопоточного и многопоточного выполнения
"""
from time import ctime, sleep
import threading


class MyThread(threading.Thread):

    def __init__(self, func, args, name=''):
        threading.Thread.__init__(self)
        self.name = name
        self.func = func
        self.args = args

    def getResult(self):
        return self.res

    def run(self):
        print('starting', self.name, 'at:', ctime())
        self.res = self.func(*self.args)
        print(self.name, 'finished at:', ctime())


def fib(x):
    sleep(0.005)
    if x < 2:
        return 1
    return fib(x-2) + fib(x-1)


def fac(x):
    sleep(0.1)
    if x < 2:
        return 1
    return x * fac(x-1)


def sum(x):
    sleep(0.1)
    if x < 2:
        return 1
    return x + sum(x-1)


funcs = [fib, fac, sum]
n = 12


def main():
    nfunc = range(len(funcs))

    print('***SINGLE THREAD')
    for i in nfunc:
        print('starting', funcs[i].__name__, 'at:', ctime())
        print(funcs[i](n))
        print(funcs[i].__name__, 'finished at:', ctime())

    print()
    print('***MULTIPLE THREADS')
    threads = []
    for i in nfunc:
        t = MyThread(funcs[i], (n,), funcs[i].__name__)
        threads.append(t)

    for i in nfunc:
        threads[i].start()

    for i in nfunc:
        threads[i].join()
        print(threads[i].getResult())

    print('all DONE')


main()
"""

# -------------------------------------------------------------------------------------------------

# В этом примере демонстрируется использование блокировок и других
# инструментов обеспечения многопоточного функционирования.
"""
from atexit import register
from random import randrange
from threading import Thread, Lock, current_thread
from time import sleep, ctime


class CleanOutputSet(set):
    def __str__(self):
        return ', '.join(x for x in self)


lock = Lock()
loops = (randrange(2, 5) for x in range(randrange(3, 7)))
remaining = CleanOutputSet()


def loop(nsec):
    myname = current_thread().name
    with lock:
        remaining.add(myname)
        print('{} Started {}'.format(ctime(), myname))
    sleep(nsec)
    with lock:
        remaining.remove(myname)
        print('{} Completed {} ({} secs)'.format(ctime(), myname, nsec))
    print('     (remaining: {})'.format(remaining or 'NONE'))


def _main():
    for pause in loops:
        Thread(target=loop, args=(pause, )).start()


@register
def _atexit():
    print('all DONE at:', ctime())


_main()
"""

# ---------------------------------------------------------------------------------------------------


# В этом сценарии блокировки и семафоры используются
# для моделирования автомата для торговли конфетами.
"""
from atexit import register
from random import randrange
from threading import BoundedSemaphore, Lock, Thread
from time import sleep, ctime

lock = Lock()
MAX = 5
candytray = BoundedSemaphore(MAX)


def refill():
    lock.acquire()
    print('Заправка конфеты...')
    try:
        candytray.release()
    except ValueError:
        print('полный, пропуск')
    else:
        print('OK')
    lock.release()


def buy():
    lock.acquire()
    print('Покупка конфет...')
    if candytray.acquire(False):
        print('OK')
    else:
        print('полный, пропуск')
    lock.release()


def producer(loops):
    for i in range(loops):
        refill()
        sleep(randrange(3))


def consumer(loops):
    for i in range(loops):
        buy()
        sleep(randrange(3))


def _main():
    print('starting at: ', ctime())
    nloops = randrange(2, 6)
    print('THE CANDY MACHINE (full with {} bars)!'.format(MAX))
    Thread(target=consumer, args=(randrange(nloops, nloops+MAX+2),)).start()  # покупатель
    Thread(target=producer, args=(nloops,)).start()  # продвец


@register
def _atexit():
    print('all DONE at: ', ctime())


_main()
"""

# ---------------------------------------------------------------------------------------------

# В этой реализации принципа "производитель-потребитель" используются объек­ты Queue
# и вырабатывается случайным образом количество произведенных (и потребленных) товаров.
# Производитель и потребитель моделируются с помощью потоков, действующих отдельно и одновременно.
"""
from random import randint
from time import sleep, ctime
from queue import Queue
import threading


class MyThread(threading.Thread):

    def __init__(self, func, args, name=''):
        threading.Thread.__init__(self)
        self.name = name
        self.func = func
        self.args = args

    def getResult(self):
        return self.res

    def run(self):
        print('starting', self.name, 'at:', ctime())
        self.res = self.func(*self.args)
        print(self.name, 'finished at:', ctime())


def writeQ(queue):
    print('producing object for Q...')
    queue.put('xxx', 1)
    print('size now', queue.qsize())


def readQ(queue):
    val = queue.get(1)
    print('consumed object from Q... size now', queue.qsize())


def writer(queue, loops):
    for i in range(loops):
        writeQ(queue)
        sleep(randint(1, 3))


def reader(queue, loops):
    for i in range(loops):
        readQ(queue)
        sleep(randint(2, 5))


funcs = [writer, reader]
nfuncs = range(len(funcs))


def main():
    nloops = randint(2, 5)
    q = Queue(32)
    threads = []

    for i in nfuncs:
        t = MyThread(funcs[i], (q, nloops), funcs[i].__name__)
        threads.append(t)

    for i in nfuncs:
        threads[i].start()

    for i in nfuncs:
        threads[i].join()

    print('all DONE')


main()
"""

# -----------------------------------------------------------------------------------------------
# В этом участке кода осуществляется сбор с экрана данных о рангах книг, с помощью
# модуля concurrent.futures

from concurrent.futures import ThreadPoolExecutor
from re import compile
from time import ctime
from urllib.request import urlopen as uopen


REGEX = compile(b'#([\d,]+) in Books ')
AMZN = 'http://amazon.com/dp/'
ISBNs = {
    '0132269937': 'Core Python Prograrnming',
    '0132356139': 'PythonWebDevelopmentwithDjango',
    '0137143419': 'Python Fиndarnentals',
}


def getRanking(isbn):
    with uopen('{0} {1}'.format(AMZN, isbn)) as page:
        return str(REGEX.findall(page.read())[0], 'utf-8')


def _main():
    print('At ', ctime(), 'on Amazon...')
    with ThreadPoolExecutor(3) as executor:
        for isbn, ranking in zip(ISBNs, executor.map(getRanking, ISBNs)):
            print('- {} ranked {}'.format(ISBNs[isbn], ranking))
    print('all DONE at:', ctime())

_main()


# Должен получится такой вывод

# $ python3 bookrank3CF.py
# At WedApr 600:21:502011 оп Amazon...
# - 'Core Python Programming' ranked 43,992
# - 'Python Fundamentals' ranked 1,018,454
# - 'Python Web Development with Django' ranked 502,566
# all DONE at: Wed Apr 6 00:21:55 2011
