""" Список задач

    01. Найти позицию(индексы) двух наименьших элементов в не отсортированном списке
    02.

"""

# ----------------------------------------------------------------------------------------------------------------------
"""01"""
# counts_01 = [809, 834, 477, 478, 307, 122, 96, 102, 324,  476]


# def find_two_smallest_v1(l):
#     """
#     Поиск, удаление, поиск. Поиск индекса минимального элемента в списке, удаление его, снова поиск минимального,
#     возвращаем удаленный элемент в список.
#     """
#     smallest = min(l)
#     min1 = l.index(smallest)
#     l.remove(smallest)  # удаляем первый минимальный элемент
#
#     next_smallest = min(l)
#     min2 = l.index(next_smallest)
#     l.insert(min1, smallest)  # возвращаем первый минимальный обратно
#     if min1 <= min2:  # проверяем индекс второго минимального из-за смещения
#         min2 += 1
#     return min1, min2  # возвращаем кортеж
#
#
# def find_two_smallest_v2(l):
#     """
#     Сортировка, поиск минимальных, определение индексов. Оптимальный вариант
#     """
#     temp_list = sorted(l)  # возвращаем КОПИЮ отсортированного списка
#     smallest = temp_list[0]
#     next_smallest = temp_list[1]
#     min1 = l.index(smallest)
#     min2 = l.index(next_smallest)
#     return min1, min2
#
#
# def find_two_smallest_v3(l):
#     """
#     Перебор всего списка. Сравниваем каждый элемент по порядку, получаем два наименьших значения,
#     обновляем значения, если найдены наименьшие.
#     """
#     if l[0] < l[1]:
#         min1, min2 = 0, 1  # устанавливаем начальные значения
#     else:
#         min1, min2 = 1, 0
#     for i in range(2, len(l)):
#         if l[i] < l[min1]:  # «первый вариант»
#             min2 = min1
#             min1 = i
#         elif l[i] < l[min2]:  # «второй вариант»
#             min2 = i
#     return min1, min2

# print(find_two_smallest_v1(counts_01))
# print(find_two_smallest_v2(counts_01))
# print(find_two_smallest_v3(counts_01))

# ----------------------------------------------------------------------------------------------------------------------
#                                                    * 02 *



