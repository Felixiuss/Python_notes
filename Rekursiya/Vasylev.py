# -*- coding: utf-8 -*-
'''Пример работы рекурсии на примере чисел Фибоначчи'''


def fib(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)


for i in range(1, 16):
    print(fib(i))