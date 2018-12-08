""" Список задач

    01. Функция принимает два списка, если есть совпадения, то возвращает кортеж (True, количество совпавших элементов
        и список совпавших элементов), если совпадений нет - просто False.
    02. Есть список, some_list = ['egg', 'spam', 'hi', 'hello', 'banana', 'roma', 'sun']. Также есть список индексов,
        indexes = [0,2,4,5]. Как получить список элементов some_list с индексами в indexes ?
    03. Дан список целых чисел, нужно вернуть список, состоящий только из неуникальных элементов данного списка. Для
        решения этой задачи не меняйте оригинальный порядок элементов.
        Пример: [1, 2, 3, 1, 3], где 1 и 3 неуникальные элементы и результат будет [1, 3, 1, 3].
    04. Проверить является ли один список последовательным подсписком другого.
    05. Функция f(list, min, max) - вернуть количество элементов из списка которые находятся в диапазоне min и max
    06. Функция f(n, str) - вернуть список сторок, которые больше чем аргумент n. Если в строке есть запятые, они должны
        быть удалены.
    07.
"""
"""
'''Примеры создания списков'''

empty_list = []     # пустой список
empty_list2 = list()    # создание пустого списка с помощью метода
l1 = list('spam')   # список литералов
l2 = list(range(-5, 5))
l3 = [0] * 5  # создание списка с пятью нулями

st = 'hello world'  # строка
l4 = list(st)    # преобразование строки в список

'''Генераторы списков'''

lst1 = [i for i in range(10)]
lst2 = [0 for i in range(10)]
lst3 = [i for i in range(10) if i % 2 == 1]  #  нечетные числа
lst4 = [i for i in range(10) if i % 2 == 0]  #  четные числа
lst5 = [i * i for i in range(10)]  # квадраты чисел
lst6 = [a + b for a in 'list' if a != 's' for b in 'soup' if b != 'u']

'''Базовая работа со списком'''

students1 = ['ira', 'roma', 'vika', 'sergey', 'andrey', 'vova']
students2 = ['luda', 'sveta', 'oleg', 'dima']

print(students1[3])      # доступ к элементам списка
print(students1[-1])     # доступ к элементам списка
print(students1[:3])     # срез
print(students1[2:4])    # срез
print(students1[::-1])   # инверсия
students1 += ['sasha']  # конкатенация списков
all_students = students1 + students2    # конкатенация списков
students2 += 'anton'    # конкатенация списка и строки которая будет разбита на элементты(символы)
students1[2] = 'lena'   # изменение элемента списка по индексу

print(students1)

''' Методы списков '''

students1.append('gena')        # добавляет елемент в конец списка
students1.insert(1, 'tanya')    # вставляет елемент на указанную позицию

print(students1)
"""

# ----------------------------------------------------------------------------------------------------------------------
"""01"""
# def comon_data(lst1, lst2):
#     res = []
#     result = False
#     for x in lst1:
#         for y in lst2:
#             if x==y:
#                 result = True
#                 res.append(y)
#     if result:
#         return result, len(res), res
#     return result
#
#
# print(comon_data([1, 2, 7, 3, 4, 5], [5, 6, 7, 8, 9, 5]))
# print(comon_data([1, 2, 3, 4, 5], [6, 7, 8, 9]))


# Тестирование с помощью py.test
"""02"""
# some_list = ['egg', 'spam', 'hi', 'hello', 'banana', 'roma', 'sun']
# indexes = [0, 2, 4, 5]
#
#
# def find_index(some_list, indexes):
#     result = []
#
#     for i in indexes:
#         result.append(some_list[i])
#
#     # result_2 = [some_list[i] for i in indexes]
#
#     return result
#     # return result_2
#
#
# print(find_index(some_list, indexes))
"""03"""
# def func(lst):
#     # res = []
#     # for i in lst:
#     #     if lst.count(i) > 1:
#     #         res.append(i)
#     res = [i for i in lst if lst.count(i)>1]
#     return res
#
# print(func([1, 2, 3, 1, 3]))
# print(func([1, 2, 3, 4, 5]))




# pytest
"""04"""
# def is_sublist(l: list, s: list) -> bool:
#
#     sub_set = False
#
#     if s is False:
#         sub_set = True
#     elif s == l:
#         sub_set = True
#     elif len(s) > len(l):
#         sub_set = False
#     else:
#         for i in range(len(l)):
#             if l[i] == s[0]:
#                 n = 1
#                 while n < len(s) and l[i+n] == s[n]:
#                     n += 1
#                 if n == len(s):
#                     sub_set = True
#     return sub_set
#
#
#
#
# a = [2, 4, 3, 5, 7]
# b = [4, 3]
# c = [3, 7]
#
# print(is_sublist(a, b))
# print(is_sublist(a, c))
#
# # 2 вариант
# def func(l, s):
#     l = [str(i) for i in l]
#     l = ''.join(l)
#
#     s = [str(i) for i in s]
#     s = ''.join(s)
#
#     return True if s in l else False
#
#
# a = [2, 4, 3, 5, 7]
# b = [4, 3]
# c = [3, 7]
#
# print(func(a, b))
# print(func(a, c))
"""05"""
# def count_range_in_list(lst: list, min: (int, str), max: (int, str)) -> tuple:
#
#     count = 0
#     res = []
#
#     for i in lst:
#         if min <= i <= max:
#             count += 1
#             res.append(i)
#     return count, res
#
#
# list1 = [10, 20, 30, 40, 40, 40, 70, 80, 99]
# print(count_range_in_list(list1, 40, 100))
#
# list2 = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
# print(count_range_in_list(list2, 'a', 'e'))
"""06"""
# def long_words(n: int, st: str) -> list:
#
#     res = []
#     txt = st.replace(',', '').split(' ')
#
#     for i in txt:
#         if len(i) > n:
#             res.append(i)
#     return res
#
#
# print(long_words(3, 'The quick brown fox, jumps over the, lazy dog'))
#
#
# s = 'The quick brown fox, jumps over tne, lazy dog'
# print(s.replace(',', '').split(' '))
"""07"""



def sub_list(my_list):
    subs = [[]]

    for i in range(len(my_list)):
        n = i+1

        while n <= len(my_list):
            sub = my_list[i:n]
            subs.append(sub)
            n += 1

        return subs


l1 = [10, 20, 30, 40]
print(sub_list(l1))



t = (1, 2, 3)
t = (4,) + t[1:]
print(t)









# import itertools
#
# def flatten(lst):
#     res = []
#
#     for i in lst:
#         if isinstance(i, list):
#             flatten(i)
#         else:
#             res.append(i)
#
#     return res
#
#
# lst = [[2, 4, 5], [1, 5, [6]], [9], [7, [5, [7, 8, [9]]], 9, 0]]
# # new_lst = list(itertools.chain(*lst))
# # print(new_lst)
#
# print(flatten(lst))
#
#
# def flatten(seq):
#     """
#     Функция, преобразующая вложенные последовательности любого уровня
#     вложенности в плоские, одноуровневые.
#
#     >>> flatten([])
#     []
#     >>> flatten([1, 2])
#     [1, 2]
#     >>> flatten([1, [2, [3]]])
#     [1, 2, 3]
#     >>> flatten([(1, 2), (3, 4)])
#     [1, 2, 3, 4]
#     """
#     result = []
#
#     def seq_expand(new_seq):
#         for new_item in new_seq:
#             if isinstance(new_item, (tuple, list)):
#                 return seq_expand(new_item)
#             else:
#                 result.append(new_item)
#
#     for item in seq:
#         if isinstance(item, (tuple, list)):
#             if seq_expand(item):
#                 result.append(seq_expand(item))
#         else:
#             result.append(item)
#     return result
#
# print(flatten([[2, 4, 5], [1, 5, [6]], [9], [7, [5, [7, 8, [9]]], 9, 0]]))


# print(count_range_in_list.__annotations__)
#
#
# def test():
#     assert count_range_in_list([10, 20, 30, 40, 40, 40, 70, 80, 99], 40, 100) == (6, [40, 40, 40, 70, 80, 99])
#     # assert is_sublist([2, 4, 3, 5, 7], [3, 7]) is False



# # unittest
# import unittest
#
#
# class TestHomework(unittest.TestCase):
#
#     def test_rle(self):
#         # self.assertEqual(is_sublist([2, 4, 3, 5, 7], [4, 3]))
#         self.assertNotEqual(is_sublist([2, 4, 3, 5, 7], [3, 7]))
#
#
# if __name__ == '__main__':
#     unittest.main()

