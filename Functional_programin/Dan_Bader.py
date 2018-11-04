"""
Используя парадигму функционального программирования, желательно использованть 'твердые'
данные которые нельзя изменить в ходе выполнения программы. Для этого хорошо подходят
namedtuple которые являются кортежем но с виду напоминают словарь
"""
import collections
from pprint import pprint

Scientist = collections.namedtuple('Scientist', [
    'name',
    'field',
    'born',
    'nobel'
])

print(Scientist)

scientists = (
    Scientist(name='Ada Lovelace', field='math', born=1815, nobel=False),
    Scientist(name='Emmy Noether', field='math', born=1882, nobel=False),
    Scientist(name='Marie Curie', field='physics', born=1867, nobel=True),
    Scientist(name='Tu Youyou', field='chemistry', born=1930, nobel=True),
    Scientist(name='Ada Yonath', field='chemistry', born=1939, nobel=True),
    Scientist(name='Vera Rubin', field='astronomy', born=1928, nobel=False),
    Scientist(name='Sally Ride', field='physics', born=1951, nobel=False),
)
# примеры работы с namedtuple
print(scientists)

for i in scientists:
    print(i)

print(scientists[0].name)
print(scientists[1])
print(scientists[6].born)


def func(x):
    name = (i.name for i in scientists)
    return x in name


print(func('Vera Rubin'))

born = (i.born for i in scientists)
print(1928 in born)

# -------------------------------------------------------------------------------------

# пример использования встроенной функции filter()  (example of using the built-in function)
# результат выполнения - List

pprint(scientists, indent=10, width=5)
print()
pprint(tuple(filter(lambda x: x.nobel is True, scientists)))
print()
pprint(tuple(filter(lambda x: x.field == 'physics', scientists)))
print()
pprint(tuple(filter(lambda x: x.field == 'physics' and x.nobel, scientists)))
print()
pprint([x for x in scientists if x.nobel is True])  # аналогия, но с помощью генератора списков
print()
res = []
for x in scientists:
    if x.field == 'physics' and x.nobel:  # тоже но цикл
        res.append(x)

# ------------------------------------------------------------------------------------------

# пример использования встроенной функции map()  (example of using the built-in function)
# результат выполнения - List
print('-' * 100)
print('пример использования функции map()', end='\n\n')


names_and_ages = tuple(map(
    lambda x: {'name': x.name.upper(), 'age': 2017 - x.born},
    scientists
))
pprint(names_and_ages)

print()

pprint(tuple({'name': x.name.upper(), 'age': 2017 - x.born}  # тоже но генератор
             for x in scientists))
print()

res = []
for x in scientists:
    res.append({'name': x.name.upper(), 'age': 2017 - x.born})  # тоже но цикл
pprint(tuple(res))

print()


def add(x, y):
    return x + y


print(list(map(add, [1, 2, 3], [1, 1, 1])))  # две последовательности
print('-' * 100)

# --------------------------------------------------------------------------------------------

# пример использования функции reduce()
from functools import reduce

print('пример использования функции reduce()', end='\n\n')

names_and_ages = tuple(map(
    lambda x: {'name': x.name, 'age': 2017 - x.born},   # базовый список
    scientists
))
pprint(names_and_ages)
print()

total_age = reduce(lambda acc, val: acc + val['age'],   # вывод суммы лет
                   names_and_ages,
                   0)
print(total_age)

print(sum(x['age'] for x in names_and_ages))        # тоже но генератор + sum
print()


def reducer(acc, val):                            # функция для передачи в reduce()
    acc[val.field].append(val.name)
    return acc


scientists_by_field = reduce(       # группировка имен по сфере деятельности
    reducer,
    scientists,
    {'math': [], 'physics': [], 'chemistry': [], 'astronomy': []}
)

pprint(scientists_by_field)
print()

scientists_by_field_2 = reduce(     # тоже но с помощью collections.defaultdict(list)
    reducer,
    scientists,
    collections.defaultdict(list)
    )
pprint(scientists_by_field_2)
print()

dd = collections.defaultdict(list)      # примеры  collections.defaultdict(list)
print(dd)
dd['doesntexist']
print(dd)
dd['doesntexist---2']
print(dd)
dd['xyz'].append(1)
print(dd)
dd['xyz'].append(2)
dd['xyz'].append(3)
print(dd)
