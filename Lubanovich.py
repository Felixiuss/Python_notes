# -*- coding: utf-8 -*-
# Функция проверки на None

# def is_none(thing):
#     if thing is None:
#         print('Its none')
#     elif thing:
#         print('Its True')
#     else:
#         print('Its False')

###############################################################
# Устранение проблемы с передачей словоря в функцию

# def lst(arg, result=[]):
#     ''' это строка
#     документации'''
#     if result:
#         result = []
#     result.append(arg)
#     print(result)

###############################################################
# Пример передачи функции как объекта

# def sum_args(*args):
#     print(sum(args))
#
# def calc_func(func, *args):
#     return func(*args)
#
# calc_func(sum_args, 1, 2, 3, 4, 5)
# print(type(calc_func))
# a = calc_func
# a(sum_args, 2, 4)
# print(type(a))
# b = sum_args
# b(1, 2, 3, 4, 5)

###############################################################
# Пример использования внутренней функции

# def func(a, b):
#     def inner_func(c, d):
#         print(c + d)
#     return inner_func(a, b)

# func(4, 7)

###############################################################
# Замыкание

# def func(saying):
#     def inner():
#         return 'Мы говорим вам : {}'.format(saying)
#     return inner
#
# print(func('hello'))
# a = func('hello')
# b = func('goodby')
# print(a)
# print(b)
# print(a())
# print(b())

# ----------------------------------------------------------------

# def func(x):
#     def add(a):
#         return a + x
#     return add
#
# test = func(100)
# print(test(200))

# ------------------------------------------------------------------

################################################################
# Пример lambda функции

# l = ['vika', 'roma', 'ira', 'luda', 'tolya']
#
# def func(lst, fun):
#     for i in lst:
#         print(fun(i))
#
# func(l, lambda word: word.capitalize() + '!')
# #----------------------------------------------------------------

# add = lambda x, y: x + y
# print(add(6, 9))

# -------------------------------------------------------------------

# print((lambda x, y: x * y)(2, 6))

# -------------------------------------------------------------------

# fun = lambda *args: args
# print(fun(2, 4, 6.7, 'hello'))

# ------------------------------------------------------------------
################################################################

# Пример создания функции генератора на примере создания собственной
# функции range()

# def my_range(first=0, last=10, step=1):
#     i = first
#     while i < last:
#         yield i
#         i += step
# # генератор можно использовать только один раз
# print(my_range)
# ranger = my_range(1, 5)
# print(ranger)
# # print(list(ranger))
# for i in ranger:
#     print(i)

################################################################
# Пример декоратора

# def document_it(func):
#     def new_function(*args, **kwargs):
#         print('Running function: ', func.__name__)
#         print('Positional arguments: ', args)
#         print('Keyword argument :', kwargs)
#         result = func(*args, **kwargs)
#         print('Result: ', result)
#         print(result)
#     return new_function
#
#
# def square_it(func):
#     def new_function(*args, **kwargs):
#         result = func(*args, **kwargs)
#         return result * result
#     return new_function
#
#
# @square_it
# @document_it
# def add_ints(a, b):
#     return a + b
#
#
# add_ints(3, 5)

#-------------------------------------------------------------

# def decor(func):
#     def wrap():
#         print('============')
#         func()
#         print('============')
#     return wrap
#
#
# @decor
# def print_text():
#     print('Hello world !')
#
#
# print_text()

#--------------------------------------------------------------

# def makebold(fn):
#     def wrapped():
#         return "<b>" + fn() + "</b>"
#
#     return wrapped


# def makeitalic(fn):
#     def wrapped():
#         return "<i>" + fn() + "</i>"
#
#     return wrapped
#
#
# @makebold
# @makeitalic
# def hello():
#     return "hello habr"
#
# print hello() ## выведет <b><i>hello habr</i></b>
#
# #-----------------------------------------------------------------
#
# def dec(fn):
#     def wrap():
#         print('start')
#         print('----------------')
#         fn()
#         print('----------------')
#         print('end')
#     return wrap
#
# @dec
# def func():
#     print('hello world')
#
# func()

###############################################################
# Пример использования оператора global

# animal = 'fruitbat'
#
# def change_and_print_global():
#     global animal
#     animal = 'wombat'
#     print('inside change_and_print_global:', animal)
#     print(locals())
#
# print(animal)
#
# change_and_print_global()
#
# print(animal)

################################################################
# Обработка исключительных ситуаций

# short_list = [1, 2, 3]
# position = 5
# try:
#     short_list[position]
# except IndexError:
#     print('Need a position between 0 and', len(short_list)-1, ' but got', position)

# -------------------------------------------------------------------------------------

# short_list = [1, 2, 3]
# while True:
#     value = input('Position [q to quit]? ')
#     if value == 'q':
#         break
#     try:
#         position = int(value)
#         print(short_list[position])
#     except IndexError as err:
#         print('Bad index:', position)
#     except Exception as other:
#         print('Something else broke:', position)

#################################################################

#                  Импорт

# from collections import defaultdict
# food_counter = defaultdict(int)                    # определяет значение по умолчанию для новых ключей
# for food in ['spam', 'spam', 'eggs', 'spam']:
#     food_counter[food] += 1
#
# for food, count in food_counter.items():
#     print(food, count)
#
#
# from collections import Counter                  # Счетчик
# breakfast = ['spam', 'spam', 'eggs', 'spam']
# breakfast_counter = Counter(breakfast)
# print(breakfast_counter)
#
# print(breakfast_counter.most_common())    # Функция most_common() возвращает все элементы в убывающем порядке или лишь
# print(breakfast_counter.most_common(1))   # те элементы, количество которых больше, чем заданный аргумент count:
#
# lunch = ['eggs', 'eggs', 'bacon']
# lunch_counter = Counter(lunch)
# print(lunch_counter)
#
# # с счетчиками можно проводить различные операции ( +, -, &, |, ...)
#
# print(breakfast_counter + lunch_counter)
# print(lunch_counter - breakfast_counter)
# print(breakfast_counter & lunch_counter)
# print(breakfast_counter | lunch_counter)
#
#
# from collections import OrderedDict      # запоминает порядок добавления ключей всловарь
# quotes = OrderedDict([                   # и выводит их в том же порядке
#      ('Moe', 'A wise guy, huh?'),
#      ('Larry', 'Ow!'),
#      ('Curly', 'Nyuk nyuk!'),
#      ])
#
# for stooge in quotes:
#     print(stooge)
#
# # Проверка палиндрома
# def palindrome(word):
#     from collections import deque     # двухсторонняя очередь  стр. 152
#     dq = deque(word)
#     while len(dq) > 1:
#         if dq.popleft() != dq.pop():
#             return False
#         return True
#
# print(palindrome('radar'))
#
# # Более проще
# def enother_palindrom(word):
#     return word == word[::-1]
#
# print(enother_palindrom('radar'))

#_---------------------------------------------------------------------------------------------------


