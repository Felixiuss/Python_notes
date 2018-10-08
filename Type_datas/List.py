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