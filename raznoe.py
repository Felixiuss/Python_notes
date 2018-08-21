# -*- coding: utf-8 -*-
# print('hello world')
# print(sorted(x.upper() for x in dir(str) if not x.startswith('__')))
#
# print([x ** 2 for x in range(10) if x % 2 == 0])
# gen = (x ** 2 for x in range(10))
# print(gen)
# print({x ** 2 for x in range(10)})
# x = {x: x ** 2 for x in range(10)}
# d = {c.upper(): ord(c) for c in 'spam'}
# print(d)
# a = dict(zip('123', 'abc'))
# z = dict(name='Bob', age=45, job=('mnr', 'dev'), exp=7)
# print(z)
# v = {'name': 'Roma', 2: 'age', ('a', 'b', 'c'): 'bob', (5, 6, 7): 'mgr'}
#
# with open(r'/home/felix/file.txt', 'w') as infile:
#     infile.write('hello world my name is Roman')
#
# infile = open(r'/home/felix/file.txt')
# print(infile.read())
# print(infile.name)
#
# mn = set(range(-5, 5))
# mn1 = set(range(10))
#
# l = ['h', 'e', 'l', 'lo world']
# print(l)
# l1 = '*'.join(l)
# print(l1)

# Проверка высокостности года
# x = int(input())
# print('Високосный') if x % 400 == 0 or x % 4 == 0 and x % 100 != 0 else print('Обычный')


# проверка палиндрома
# string = input()
# st = string[::-1]
# print('yes') if st == string else print('no')

# проверка счастливого билетика
# lst_num = [int(i) for i in input()]
# print('Счастливый') if sum(lst_num[:3]) == sum(lst_num[3:]) else print('Обычный')

# поиск чисел которые больше 15
# lst = [11, 18, 9, 12, 23, 4, 17]
# lost = []
# for idx in range(len(lst)):
#     val = lst[idx]
#     if val > 15:
#         lost.append(val)
#         lst[idx] = 15
# print("modif:", lst, "-lost:", lost)

# -------------------------------------
# #  Пример статического метода
# class MyObject:
#     class_attribute = 8
#
#     def __init__(self):
#         self.data_attribute = 42
#
#     def instance_method(self):
#         print(self.data_attribute)
#
#     # по сути играет роль того-же атрибута класса но выглядит как функция
#     @staticmethod
#     def static_method():
#         print(MyObject.class_attribute)
#
#
# MyObject.static_method()
# obj = MyObject()
# obj.instance_method()
# obj.static_method()


# пример метода класса
# class Rectangle:
#     def __init__(self, side_a, side_b):
#         self.side_a = side_a
#         self.side_b = side_b
#
#     def __repr__(self):
#         return 'Rectangle(%.1f, %.1f)' % (self.side_a, self.side_b)
#
#
# class Circle:
#     def __init__(self, radius):
#         self.radius = radius
#
#     def __repr__(self):
#         return 'Circle(%.1f)' % self.radius
#
#     @classmethod
#     def from_rectangle(cls, rectangle):
#         radius = (rectangle.side_a ** 2 + rectangle.side_b ** 2) ** 0.5 / 2
#         return cls(radius)
#
#
# rectangle = Rectangle(3, 4)
# print(rectangle)
#
# first_circle = Circle(1)
# print(first_circle)
#
# second_circle = Circle.from_rectangle(rectangle)
# print(second_circle)


#  как работает декоратор property
class MyObject:
    def __init__(self):
        self.__atribute = 0

    @property
    def attribute(self):
        return self.__atribute

    @attribute.setter
    def attribute(self, value):
        if value < 100:
            self.__atribute = value
        # else:
        #     print('value is not < 100')


obj = MyObject()
print(obj.attribute)
obj.attribute = 9000
print(obj.attribute)
obj.attribute = 10
print(obj.attribute)
























