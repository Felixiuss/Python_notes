# -*- coding: utf-8 -*-


def find_value(f, x):
    print('x = ', x, '-> f(x) =', f(x))   # функция для отображения значения другой функции


my_func = lambda x: 1/(1 + x ** 2)   # переменной присваивается ссылка на лямбда-функцию


find_value(my_func, 2.0)   # проверяем результат

find_value(lambda x: x * (1-x), 0.5)   # аргументом функции передана лямбда-функция

z = 1 + (lambda x, y: x * y - x ** 2)(2, 3) ** 2   # использование лямбда-функции в выражении
print('z = ', z)


""" простой пример нахождения площади прямоугольника с помощью lambda"""
s = int(input())
v = int(input())

x = (lambda a, b: v * s)(v, s)

print(x)

'''функция в качестве результата возвращает другую функцию'''


def my_pow(n):
    return lambda x: x ** n


for n in range(1, 4):
    for x in range(1, 11):
        print(my_pow(n)(x))
