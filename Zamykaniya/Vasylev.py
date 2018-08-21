# -*- coding: utf-8 -*-


# def sq_sum():
#     def get_n():
#         n = int(input("Slagaemyh v summe : "))
#         return n
#
#     def find_sq_sum():
#         s = 0
#         for i in range(1, n+1):
#             s += i**2
#         return s
#
#     n = get_n()
#     return find_sq_sum
#
#
# z = sq_sum()()
# print("Summa kvadratov ravna : ", z)


"""Функция как результата другой функции"""

# Функция для вычисления факториала и двойного факториала


# def factor(mode=True):
#     # вложенная функция для вычисления факториала
#     def sf(n):
#         s = 1
#         i = n
#         while i > 1:
#             s *= i
#             i -= 1
#         return s
#
#     def df(n):
#         # вложенная функция для вычисления двойного факториала
#         s = 1
#         i = n
#         while i > 1:
#             s *= i
#             i -= 2
#         return s
#
#     # Если аргумент равен True
#     if mode:
#         return sf
#     # Если аргумент равен False
#     else:
#         return df
#
#
# print("5! =", factor()(5))
# print("5! =", factor(True)(5))
# print("5!! =", factor(False)(5))


"""Тот же пример но проще"""


# def factor(mode=True):
#     def f(n, d):
#         s = 1
#         i = n
#         while i > 1:
#             s *= i
#             i -= d
#         return s
#
#     d = 1 if mode else 2
#     return lambda n: f(n, d)
#
#
# print("5! =", factor()(5))
# print("5! =", factor(True)(5))
# print("5!! =", factor(False)(5))


"""Тот же пример но еще проще с использованием рекурсии"""


def factorial(n):
    if n == 1:
        return n
    else:
        return n * factorial(n - 1)


def dfactorial(n):
    if n == 1 or n == 2:
        return n
    else:
        return n * dfactorial(n - 2)


def factor(mode=True):
    return factorial if mode else dfactorial


print("5! =", factor()(5))
print("5! =", factor(True)(5))
print("5!! =", factor(False)(5))
