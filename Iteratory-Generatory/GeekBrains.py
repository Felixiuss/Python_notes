import random


'''
Заметки:
- Чтобы объект был итерируемый - у него должен быть метод iter(),
  а метод iter() - должен вернуть объект next()
'''


my_list = [1, 4, 6, 10]
my_list_iter = iter(my_list)  # функция которая возвращает генератор
my_list.__iter__()            # тоже самое но подругому выглядит
# у любого генератора есть метод next()
# print(next(my_list_iter))
# print(next(my_list_iter))
# print(next(my_list_iter))
# print(my_list_iter.__next__())  # тот-же самый вызов но выглядет иначе

# ------------------------------------------------------------


class Colors:
    def __init__(self, colors):
        self.colors = colors

    def __iter__(self):  # этот метод возвращает генератор
        i = 0            # который сам запоминает состояние и сам вызывает метод  next()
        while True:
            yield self.colors[i]
            i += 1
            if i == len(self.colors):
                i = 0


colors = Colors(['red', 'green', 'blue'])

# for color in colors:        # for next(color) in iter(colors) - так на самом деле работает цикл for
#     print(color, end='')
#     input()


class Colors2:
    def __init__(self, colors):
        self.colors = colors
        self.i = 0          # здесь мы сами реализуем счетчик состояния

    def __iter__(self):
        return self

    def __next__(self):  # здесь метод next() - мы реализуем вручную
        self.i += 1
        if self.i == len(self.colors):
            self.i = 0
        return self.colors[self.i]

# -----------------------------------------------------------


class RandNumbers:
    num = 0

    def __iter__(self):
        return self

    def __next__(self):
        self.num += 1
        if self.num > 10:               # здесь так же переопределяется метод next() и
            raise StopIteration         # вручную генерируем исключение в конце последнего прохода
        return random.randint(-10, 10)


rnd = RandNumbers()

# for el in rnd:
#     print('random numbers = ', el, end='')
#     input()

# print(list(rnd))

# -----------------------------------------------------------------

import itertools
'''
itertools.chain() - позволяет объединить два разных итератора в один
itertools.cycle() - бесконечно повторяет заданную последовательность
itertools.count() - выдающий бесконечные числа, начиная с заданного
'''

l1 = iter([1, 2, 3])
l2 = iter([4, 5, 6])

# for i in itertools.chain(l1, l2):
#     print(i)

# ---------------------------------------

color = ['red', 'green', 'blue']

# for i in itertools.cycle(color):
#     print(i)
#     input()

# ---------------------------------------

# for i in itertools.count(5):
#     print(i)
#     if i == 100:
#         break

# ---------------------------------------------------------------


class Vector:
    def __init__(self, coords):
        self.x, self.y = coords

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector((x, y))

    def __str__(self):
        return 'вектор V {} {}'.format(self.x, self.y)
        #  очередность вызовов методов  unicode >> str >> repr


v1 = Vector((10, 20))
v2 = Vector((10, 30))

v3 = v1 + v2               # v1.__add__(v2)

print(v3.x, v3.y)

print(v1)  #   v1.__str__()