"""Пример проверки является ли  число простым"""
"""
import concurrent.futures
import math
import time

PRIMES = [
    112272535095293,
    112582705942171,
    112272535095293,
    115280095190773,
    115797848077099,
    1099726899285419]


def is_prime(n):
    if n % 2 == 0:
        return False

    sqrt_n = int(math.floor(math.sqrt(n)))
    for i in range(3, sqrt_n + 1, 2):
        if n % i == 0:
            return False
    return True


# многопоточное исполнение
def main():
    with concurrent.futures.ProcessPoolExecutor() as executor:
        result = executor.map(is_prime, PRIMES)
        print('is prime: %s' % (list(result)))


start_1 = time.time()
main()
end_1 = time.time()
print(f'Time to complete: {end_1 - start_1:.2f}s\n')

# простое исполнение
start = time.time()
lst = list(map(is_prime, PRIMES))
print(lst)
end = time.time()
print(f'Time to complete: {end - start:.2f}s\n')
"""

# ----------------------------------------------------------------------------------------------------------------------

"""Пример исполнения функций в последовательном и паралельном режиме"""
"""
from time import ctime, sleep
import threading
import concurrent.futures


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

    print()
    print('***CONCURRENT FUTURES')
    with concurrent.futures.ThreadPoolExecutor() as executor:
        for i in nfunc:
            print('starting', funcs[i].__name__, 'at:', ctime())
            future = executor.submit(funcs[i], n)
            print(future.result())
            print(funcs[i].__name__, 'finished at:', ctime())

    print('all DONE')


main()
"""

# ----------------------------------------------------------------------------------------------------------------------

import concurrent.futures
import math

# PRIMES = [93, 71, 293, 73, 99, 19]
#
#
# def is_prime(n):
#     if n % 2 == 0:
#         return False
#
#     sqrt_n = int(math.floor(math.sqrt(n)))
#     for i in range(3, sqrt_n + 1, 2):
#         if n % i == 0:
#             return False
#     return True


def func(x):
    print('Hello')


with concurrent.futures.ThreadPoolExecutor(max_workers=1) as executor:
    future = executor.submit(pow, 3, 3)
    if future.result() == 27:
        future.add_done_callback(func)
    else:
        print('goobay')
    # print(list(executor.submit(pow, 3, 3).result()))





