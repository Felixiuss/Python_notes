"""доступ и печать содержимого URL-адреса на консоль"""
# from http.client import HTTPConnection
#
# conn = HTTPConnection('tproger.ru')
# conn.request('GET', '/curriculum/python-how-to-learn-2')
# result = conn.getresponse()
# # извлекает все содержимое
# print(result.status)
#
# contents = result.read()
# print(contents)
# # -------------------------------------------------------------------

"""переменные среды доступа"""
# import os
#
# print('*-------------------------------------------*')
# print(os.environ)  # доступ ко всем переменным среды
# print('*-------------------------------------------*')
#
# print(os.environ['HOME'])  # доступ к конкретной переменной
# print('*-------------------------------------------*')
# print(os.environ['PATH'])  # доступ к конкретной переменной
# print('*-------------------------------------------*')
# -------------------------------------------------------------------

"""Вычислить середину линии"""
# print('\nCalculate the midpoint of a line :')

# x1 = float(input('The value of x (the first endpoint) '))
# y1 = float(input('The value of y (the first endpoint) '))
#
# x2 = float(input('The value of x (the first endpoint) '))
# y2 = float(input('The value of y (the first endpoint) '))

# x_m_point = (x1 + x2) / 2
# y_m_point = (y1 + y2) / 2
# print()
# print("The midpoint of line is :")
# print("The midpoint's x value is: ", x_m_point)
# print("The midpoint's y value is: ", y_m_point)
# print()
# -----------------------------------------------------------------------

"""рассчитать количество дней между двумя датами"""
# from datetime import date
#
# f_date = date(2018, 7, 2)
# l_date = date(2018, 7, 11)
# delta = l_date - f_date
# print(delta.days)
# -----------------------------------------------------------------------

"""Вычисление длины гипотенузы прямоугольного треугольника"""
# from math import sqrt
#
# print('введите длину коротких сторон треугольника')
# a = float(input('a: '))
# b = float(input('b: '))
#
# c = sqrt(a**2 + b**2)
# print("Длина гипотенузы равна : ", c)

# --------------------------------------------------------------------------
"""вычислить сумму цифр в целых числах"""

# num = int(input("Введите четырехзначное число : "))
#
# x = num // 1000
# x1 = (num - x*1000) // 100
# x2 = (num - x*1000 - x1*100) // 10
# x3 = num - x*1000 - x1*100 - x2*10
# print("сумма цифр числа равна : ", x + x1 + x2 + x3)
# # 2  вариант
# res = []
# [res.append(int(i)) for i in str(num)]
# print(sum(res))
# -------------------------------------------------------------------------------------------------
"""функция возвращает сумму переданных чисел, если все числа одинаковы - сумма умножается на 3"""

# def sum_thrice(x, y, z):
#     sum = x+y+z
#     if x == y == z:
#         sum *= 3
#     return sum
#
# print(sum_thrice(1, 2, 3))
# print(sum_thrice(3, 3, 3))
# ------------------------------------------------------------------------------------------------
"""проверяет, выполняется ли оболочка python в 32-битном или 64-битном режиме на ОС"""
# import struct
# print(struct.calcsize('P') * 8)
# ----------------------------------------------------------------------------------------------
"""Вывод гистограммы переданных чисел"""

def histogram(items):
    for i in items:
        output = ''
        times = i
        while times > 0:
            output += '*'
            times -= 1
        print(output)
histogram([2, 3, 6, 5])
