"""Виртуальная машина (интерпретатор Python) исполняет инструкции байт-кода, полученные из команд языка Python: """
import dis
print(dis.dis('a = 7'))  # операцию присваивания a=7 перевели в байт-код
print()
# ----------------------------------------------------------------------------

"""Функция id() возвращает идентификатор объекта, переданного в качестве аргумента функции. 
В реализации CPython возвращаемое число является адресом объекта в памяти."""
print('ФУНКЦИЯ ID')
x = '12334'
print('ID x is: ', id(x))
# Для экономии ресурсов при работе с небольшими целыми значениями Python ссылается на уже существующие в памяти объекты:
i = 3
j = 3
k = 4 - 1
id(i) >> 1647399712
id(j) >> 1647399712
id(k) >> 1647399712
i = 3000000000
j = 3000000000
id(i) >> 13786168
id(j) >> 49195536
print()
# ----------------------------------------------------------------------------
"""примеры Функций"""
print('ПРИМЕРЫ ФУНКЦИЙ')
print(pow(abs(-5) + abs(-3), round(5.8)))
print(int(round(pow(round(5.777, 2), abs(-2)), 1)))
print()

def convert_to_cels(farengeit):  # пример перевода фаренгетов в цельсии
    return (farengeit - 32) * 5/9
print(round(convert_to_cels(72)))
print()
# -------------------------------------------------------------------------------

"""Области видимости"""
print('ОБЛАСТИ ВИДИМОСТИ')
a = 3  # глобальная переменная
print('глобальная переменная a =', a)
y = 8  # глобальная переменная
print('глобальная переменная y = ', y)


def func ():
    print('func: глобальная переменная a = ', a)
    y = 5  # локальная переменная
    print('func: локальная переменная y = ', y)


func()  # вызываем функцию func()
print('??? y = ', y)  # отобразится глобальная переменная
print()
# -------------------------------------------------------------------------------------

"""Пример замыкания"""
print('пример замыкания')
def kn(a):
    def inner():        # замыкание не использует аргументов
        return a + 5    # но использует внешний параметр kn()
    return inner        # возвращает имя функции вместо её вызова

print(kn(4))
a = kn(4)
print(a)
print(a())  # запомнилось значение в момент создания a
print()
# --------------------------------------------------------------------------------------

"""Модули"""
'''
import imp
imp.reload(some_modul)  # принудительная перезагрузка модуля

def func(x):
    return x**2+7
if __name_ _ == "__main__":
    x=int(input("Введите значение: "))
    print(func(x))
'''
# --------------------------------------------------------------------------------------

"""Тесты"""
print('Тестирование')
def func_m (v1, v2, v3):
    """Вычисляет среднее арифметическое трех чисел.
    >>> func_m (20, 30, 70)
    60.0                        #  указана ошибка
    >>> func_m (1, 5, 8)
    4.667
    """
    return round((v1+v2+v3)/3, 3)

import doctest  # автоматически проверяет тесты в документации. Если ошибки нет ничего не выводится
doctest.testmod()
print()
# --------------------------------------------------------------------------------------------
"""
     Методы списков

Функции, которые находятся внутри класса, называются методами. Их главное отличие от вызова функций из модуля 
заключается в том, что в качестве первого аргумента метод принимает, например, строковый объект, если это метод 
строкового класса:
>>> str.capitalize('hello')
'Hello'
>>>
По аналогии с вызовом функции из модуля указываем имя класса – str, затем через точку пишем имя строкового 
метода capitalize(), который принимать один строковый аргумент, Метод – это обычная функция, 
расположенная внутри класса.
"""
print('Методы списков')
# методы можно вызывать подряд в одну строку:
print('ПРИВЕТ'.swapcase().endswith('т'))
# --------------------------------------------
# Объединим две строки:
print('TT' + 'rr')

# На самом деле, в этот момент Python вызывает специальный строковый метод __add__() и
# передает ему в качестве первого аргумента строку 'rr':
print('TT'.__add__('rr'))

# Напомню, что этот вызов затем преобразуется Python в полную форму (результат будет аналогичный):
print(str.__add__("TT", 'rr'))
print()
# ---------------------------------------------------------------------------------------------------------------
""" Функция Range"""

print('Функция Range')
print(sum(list(range(1, 101))))  # сумма всех чисел диапазона

# изменение элементов списка
# Необходимо пройти в цикле по всем элементам списка lst, для этого перебираются и изменяются последовательно
# элементы списка через указание их индекса. В качестве аргумента range() задается длина списка.
# В этом случае создаваемый диапазон будет от 0 до len(lst)-1.
lst = [4, 10, 5, -1.9]
print(lst)
for i in range(len(lst)):
    lst[i] = lst[i] * 2
print(lst)
# тоже но с помощью генератора
lst1 = [4, 10, 5, -1.9]
print(lst1)
lst1 = [i*2 for i in lst1]
print(lst1)
print()

# Рассмотрим, как получить список, состоящий из случайных целых чисел:
# В данном примере функция range() выступает как счетчик числа повторений (цикл for сработает ровно 5 раз).
# Обратите внимание, что при формировании нового списка переменная i не используется.
# В результате пять раз будет произведен вызов функции randint(), которая сгенерирует целое случайное
# число из интервала, и уже это число добавится в новый список.
# from random import randint
from random import randint
A = [randint(1, 9) for i in range(5)]
print(A)
print()

# Зададим длину списка и введем с клавиатуры все его значения:
"""
a = []  # объявляем пустой список
n = int(input())  # считываем количество элемент в списке
for i in range(n):
    new_element = int(input())  # считываем очередной элемент
    a.append(new_element)  # добавляем его в список
    # последние две строки можно было заменить одной:
    # a.append(int(input()))
print(a)

Теперь запишем решение этой задачи через списковое включение в одну строку:
gen_list = [int(input()) for i in range(int(input()))]
print(gen_list)
"""
# -------------------------------------------------------------------------------------------------------------
"""ЦИКЛЫ, LAMBDA, YIELD"""
print('ЦИКЛЫ, LAMBDA, YIELD')

# В следующей программе реализован один из вариантов подсчета суммы чисел в строке:
s = 'aa3aBbb6ccc'
total = 0
for i in range(len(s)):
    if s[i].isalpha():   # посимвольно проверяем наличие буквы
        continue  # инструкция перехода к следующему шагу цикла
    total = total + int(s[i])  # накапливаем сумму, если встретилась цифра print ("сумма чисел:", total)
print("сумма чисел:", total)

# Пример lambda выражения
print('LAMBDA')
def edit_story(words, func):
    for word in words:
        print(func(word))

s = ['aaaaa', 'bbbbbb', 'cccccc']  # создали список
print(edit_story(s, lambda word: word.capitalize() + '!'))

# В предыдущих примерах мы уже встречались с функцией range(), которая генерирует последовательность целых чисел
# без необходимости создания всей последовательности и её хранения в памяти.
# Напишем собственную функцию-генератор, которая отличается тем, что вместо return использует инструкцию yield:
print('YIELD')
def my_range(first=0, last=10, step=1):
     number = first
     while number < last:
          yield number
          number += step
print(my_range)
ranger = my_range(1, 5)
# Видим, что функция my_range() вернула объект генератора:
print(ranger)
for i in ranger:
    print(i)

#  От себя - другими словами yield это тот же range но написан собственноручно со своими элементами

# Вложенные циклы
print('ВЛОЖЕННЫЕ ЦИКЛЫ')

lst = [[1, 2, 3],
       [4, 5, 6]]
for i in lst:    # цикл по элементам внешнего списка
    print()
    for j in i:  # цикл по элементам элементов внешнего списка
        print(j, end="")

# Рассмотрим следующий пример разложения числа на множители:

for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'равно', x, '*', n//x)
            break
    else:
        # циклу не удалось найти множитель
        print(n, '- простое число')
print()
# --------------------------------------------------------------------------------------------------------
"""СЛОВАРИ"""
print('СЛОВАРИ')

# Функция, которая возвращает словарь, содержащий статистику встречаемости элементов в последовательности:
def histogram(s):
    d = dict()
    for c in s:
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1
    return d

# Результат вызова функции histogram() для списка, строки, кортежа соответственно:
print(histogram([2,5,6,5,4,4,4,4,3,2,2,2,2]))
print(histogram("ywte3475eryt3478e477477474"))
print(histogram((5,5,5,6,5,'r',5)))
print()

# ключевые аргументы
# Пример функции подсчета всех переданных значений(чисел)
def total(initial=5, *numbers, **keywords):
    count = initial
    for number in numbers:
        count += number  # или count = count + number
    for key in keywords:
        count += keywords[key]  # или count = count + keywords[key]
    return count
# 1, 2, 3 – позиционные аргументы, vegetables и fruits – ключевые аргументы
print(total(10, 1, 2, 3, vegetables=50, fruits=100))
print()

# Если некоторые ключевые параметры должны быть доступны только по ключу, а не как позиционные аргументы,
# их можно объявить после параметра со звездочкой. Объявление параметров после параметра со звездочкой дает
# только ключевые аргументы. Если для таких аргументов не указано значение по умолчанию,
# и оно не передано при вызове, обращение к функции вызовет ошибку
def total (initial=5, *numbers, extra_number):
    count = initial
    for number in numbers:
        count += number
    count += extra_number
    print(count)
total (10, 1, 2, 3, extra_number=50)
# total (10, 1, 2, 3)  - вызовет ошибку
