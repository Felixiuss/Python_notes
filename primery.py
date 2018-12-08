# -*- coding: utf-8 -*-


# пример декоратора

# def decor(func):
#     def wrap(*args, **kwargs):
#         print('============')
#         func(*args, **kwargs)
#         print('============')
#     return wrap
#
#
# @decor
# def print_text():
#     print('hello world!')


# print_text()
#------------------------------------------------
# примеры рекурсии на числах Фибоначчи


# def fib(x):
#     if x == 0 or x == 1:
#         return x
#     else:
#         return fib(x-1) + fib(x-2)
#
# print(fib(10))

# пример рекурсии на факториале

# def fuct(x):
#     if x == 0 | x == 1:
#         return x
#     else:
#         return x * fuct(x-1)
#
# print(fuct(5))
#
#-------------------------------------------------
# class Car:
#     def __init__(self, brand, name):
#         self.brand = brand
#         self.name = name
#
#     def __str__(self):
#         return 'производитель {}, модель {}'.format(self.brand, self.name)
#
#     # def __new__(cls, *args, **kwargs):
#     #     print('hello')
#
#     def __del__(self):
#         print('хрен удалишь')
#
#
# car = Car('kia', 'soul')
# print(car.brand)
# print(car.name)
# print(car)
# del car


# f = open('text.txt')
# for line in f:
#     print(line)

t = ('1', '2', '3', 'hello', 'world', 'egg', 'foo', 'spam')
a = slice(3)
print(t[a])
print(t[:3])

xs = []
def f():
    xs.append(42)


print(f())
print(xs)