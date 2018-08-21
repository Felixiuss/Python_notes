# -*- coding: utf-8 -*-
#                  Цыкл while
# ---------------------------------------------------------
# найти сумму всех натуральных чисел введенного числа
# number = int(input('Ведите число : '))
# i = 0
# sum = 0
# while i <= number:
#     sum += i
#     i += 1
# print(sum)

# то же, но с оператором break
# number = int(input('Type a number : '))
# i = 1
# s = 0
# while True:
#     s += i
#     i += 1
#     if i > number:
#         break
# print(s)
#                     Цыкл for
# --------------------------------------------------
# Нйти сумму всех натуральных чисел введенного числа
# number = int(input('Ведите чило : '))
# s = 0
# for i in range(number + 1):
#     s += i
# print(s)

# то же но с помощью всторенной функции sum()
# number = int(input('Ведите чило : '))
# print(sum(range(number + 1)))

#####################################################

# Текст в операторе цикла
# text = 'Python'
# i = 1
# for s in text:
#     txt = str(i) + ' - я буква'
#     i += 1
#     print(txt, s)
# print('Работа программы завершена !')

#####################################################

# Оператор цикла for c else блоком
# print('Проверяем содержимое списка :')
# mylist = [1, 3+2j, True, 4.0]
# # mylist = [1, 3+2j, 'Python', 4.0]
# print('Список ', mylist)
# for i in mylist:
#     if type(i) == str:
#         print('В списке есть текстовые элементы !')
#         break
# else:
#     print('В спике нет текстовых элементов !')
# print('Проверка закончена.')

######################################################

# Совпадение элементов в списке (вложенные циклы)
# ---------------------------------------------------------
# print('Поиск совпадающих элементов.')
# A = [2, False, 9.1, 2-1j, "hello", 5, "Python"]
# B = [5, 3, "HELL0", 7, 12.5, "Python", True, False]
# print('1-й список', A)
# print('2-й список', B)
# print('Совпадают :')
# i = 0
# for a in A:
#     i += 1
#     j = 0
#     for b in B:
#         j += 1
#         if a == b:
#             txt = str(i) + " -й элемент из 1-го списка и ", str(j) + " -й элемент из 2-го списка"
#             print(txt)
# print('Поиск закончен.')

#              Обработка исключительных ситуаций
# -------------------------------------------------------------

# print('Решаем уравнение a * x = b')
# try:
#     a = float(input('Введите число a : '))
#     b = float(input('Введите число b : '))
#     x = b / a
#     print('Решение уравнения x = ', x)
# except ValueError:
#     print('Нужно было ввести число !')
# except ZeroDivisionError:
#     print('Внимание! На ноль делить нельзя!')
# print('Работа программы завершена.')

##############################################################

                   # Функции
#---------------------------------------------------------------

# def your_name():
#     print('добрый день !')
#     name = input('как вас зовут ? ')
#     return name
#
#
# def say_hello(txt):
#     print('Hello ', txt + '!')
#
#
# may_name = your_name()
# say_hello(may_name)

# ---------------------------------------------------------------
# Сумма произвольно переданных чисел

# def get_sum(*args):
#     s = 0
#     for i in args:
#         s += i
#     return s
#
# print(get_sum(1, 90, 89, 3, 4, 5, 6))


#################################################################


#                   Вложенные функции
#-----------------------------------------------------------------

# def sq_sum():
#     def get_n():
#         n = int(input('Slagaemyh v summe : '))
#         return n
#
#     def find_sq_sum():
#         s = 0
#         for i in range(1, n + 1):
#             s += i ** 2
#             return s
#     n = get_n()
#     return find_sq_sum
#
# # z = sq_sum()()
# # print('Summa kvadratov ravna : ', z)
#
# print(sq_sum()())

####################################################################

#         Функция как резудьтата функции

#     Вычисление Факториала

# def factor(mode=True):
#     def sf(n):
#         s = 1
#         i = n
#         while i>1:
#             s *= i
#             i -= 1
#         return s
#
#     def df(n):
#         s = 1
#         i = n
#         while i>1:
#             s *= i
#             i -= 2
#         return s
#     if mode:
#         return sf
#     else:
#         return df
#
#
# print('5 ! = ', factor()(5))
# print('5 ! = ', factor(True)(5))
# print('5 !! = ', factor(False)(5))

#---------------------------------------------------------

#   Тоже самое но немного проще

# def factor(mode=True):
#     def f(n, d):
#         s = 1
#         i = n
#         while i>1:
#             s *= i
#             i -= d
#         return s
#
#     if mode:
#         d = 1
#     else:
#         d = 2
#
#     return lambda n: f(n, d)
#
#
# print('5 ! = ', factor()(5))
# print('5 ! = ', factor(True)(5))
# print('5 !! = ', factor(False)(5))

##############################################################

#         Тоже самое но еще проще

# def factorial(n):
#     if n == 1:
#         return 1
#     else:
#         return n * factorial(n-1)
#
#
# def dfactorial(n):
#     if n == 1 or n == 2:
#         return n
#     else:
#         return n * factorial(n-2)
#
#
# def factor(mode=True):
#     return factorial if mode else dfactorial
#
#
# # print('5 ! = ', factor()(5))
# # print('5 ! = ', factor(True)(5))
# # print('5 !! = ', factor(False)(5))
#
# z = factorial
# print(z(10))

#######################################################################################################

#                        Классы

#             Пример встроенного метода __call__

# class Box:
#     def __init__(self, width, height, depth):
#         self.width = width
#         self.height = height
#         self.depth = depth
#
#     # Срабатывает когда экземпляр класса вызывается как функция (obj=Box >> obj())
#     def __call__(self, *args, **kwargs):
#         volume = self.width * self.height * self.depth
#         print('Volume is : ', volume)
#
#
# obj = Box(10, 20, 30)
# obj()
#
# Box.__call__(obj)

# ------------------------------------------------------------------------------------------------------

# Пример работы встроенных методов __str__ , __setitem__ , __getitem__ , __delitem__

# class Myclass:
#     Nmax = 5
#
#     def __init__(self):
#         n = Myclass.Nmax
#         self.nums = [0 for i in range(n)]
#
#     def __str__(self):
#         txt = ""
#         for s in self.nums:
#             txt += " " + str(s) + " |"
#         return txt
#
#     def __setitem__(self, i, v):
#         k = i % len(self.nums)
#         self.nums[k] = v
#
#     def __getitem__(self, i):
#         k = i % len(self.nums)
#         return self.nums[k]
#
#     def __delitem__(self, i):
#         k = i % len(self.nums)
#         self.nums[k] = "*"
#
#
# obj = Myclass()
# print(obj)
# obj[0] = 100
# obj[2] = -3
# obj[24] = 123
# print(obj)
# print('element with index 4 : ', obj[4])
# print('element with index 7 : ', obj[7])
# del obj[0]
# del obj[9]
# print(obj)
# print(2%5)





















