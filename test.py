"""  Функции  """

# пример изменения элементов списка(сам список остаеттся оригинальным)

ls = [1, 2, 3, 4, 5, 6]

for i in range(len(ls)):
    ls[i] += 1
print(ls)

new_ls = [x + 10 for x in ls]  # тоже но с помощью генератора
print(new_ls)

res = []    # другой вариант
for i in ls:
    res.append(i + 100)
print(res)

# -------------------------------------

# Встроенная функция zip

l1 = [1, 2, 3, 4]
l2 = [6, 7, 8, 9]

print(list(zip(l1, l2)))

for x, y in zip(l1, l2):     # паралельный обход двух последовательностей
    print(x, y, '--', x+y)

# **************************************

keys = ['spam', 'eggs', 'toast']
vals = [1, 3, 5]

d = {}

for (key, value) in zip(keys, vals):   # создание словаря
    d[key] = value
print(d)

# --------------------------------------

# Встроенная функция enumerate

s = 'spam'
for (i, item) in enumerate(s):
    print(i, item)

e = enumerate(s)

print(next(e))
print(next(e))

# -----------------------------------------------

# Встроенная функция filter

print(list(filter(bool, ['spam', '', 1, 'eggs', False, None])))

# -------------------------------------------------

#  простой поиск совпадений в двух последовательносттях

s1 = 'spam'
s2 = 'scam'

x = [x for x in s1 if x in s2]  # с помощбю генератора
print(x)


def intersect(seq1, seq2):  # с помощью функции
    res = []
    for x in seq1:
        if x in seq2:
            res.append(x)
    return res


x2 = intersect([1, 2, 3], (1, 4))
print(x2)

# --------------------------------------------------------------------------
# вывод встроенных функций

import builtins

for i in dir(builtins):
    if i.startswith('__'):
        print(i)

# -------------------------------------------------------------------------

# Фабричные функции

# В зависимости от того, кому задается вопрос о том, как называется такое поведение,
# можно услышать такие термины, как замыкание или фабричная функция. Под этими терминами
# подразумевается объект функции, который сохраняет значения в объемлющих областях
# видимости, даже когда эти области могут прекратить свое существование.


def maker(n):
    def action(x):     # Создать и вернуть функцию
        return x ** n  # Функция action запоминает значение N в объемлющей
    return action      # области видимости


f = maker(2)           # Запишет 2 в N
print(f)     # вернет ссылку на созданную ею вложенную функцию, созданную при
             # выполнении вложенной инструкции def
             # <function maker.<locals>.action at 0x1045a2378>
print(f(3))
print(f(4))
g = maker(3)  # Функция g хранит число 3, а f – число 2
print(g(3))   # 3 ** 3
print(f(3))   # 3 ** 2

# ---------------------------------------------------------------------------------

# Сохранение информации в атрибутах функций


def tester(start):
    def nested(label):
        print(label, nested.state)  # # nested – объемлющая область видимости
        nested.state += 1           # Изменит атрибут, а не значение имени nested
    nested.state = start            # Инициализация после создания функции
    return nested


t = tester(0)
t('spam')           # t – это функция ‘nested’ с присоединенным атрибутом state
t('ham')
print(t.state)      # Атрибут state доступен за пределами функции
g = tester(42)      # g имеет собственный атрибут state,
g('eggs')           # отличный от одноименного атрибута функции t
t('ham')

# ---------------------------------------------------------------------------------

# Решение проблемы с изменяемыми объектами (списки, словари)


def changer(a, b):
    b = b[:]
    a = 2
    b[0] = 'spam'
    print(a, b, sep=',')


arg1 = 5
arg2 = [1, 2]

changer(arg1, arg2)  # changer(arg1, arg2[:])
print(arg2)

# второй вариант


def changer_2(a, b=None):
    if b is None:
        b = []
    a = 2
    b[0] = 'spam'
    print(a, b, sep=',')


arg3 = 5
arg4 = [1, 2]

changer_2(arg3, arg4)
print(arg4)

# ---------------------------------------------------------------------------------

# Функция поиска минимума (для поиска наибольшего числа поменять < на >)


def min1(*args):
    res = args[0]
    for arg in args[1:]:
        if arg < res:
            res = arg
    return res


def min2(first, *rest):
    for arg in rest:
        if arg < first:
            first = arg
    return first


def min3(*args):
    tmp = list(args)
    tmp.sort()
    return tmp[0]   # для наибольшего числа вернуть tmp[-1]


print(min1(3, 4, 1, 2))
print(min2('bb', 'aa'))
print(min3([2, 2], [1, 1], [3, 3]))


def minmax(test, *args):
    res = args[0]
    for arg in args[1:]:
        if test(arg, res):
            res = arg
    return res

def lessthan(x, y): return x < y
def grtrthan(x, y): return x > y


print(minmax(lessthan, 4, 2, 1, 5, 6, 3))
print(minmax(grtrthan, 4, 2, 1, 5, 6, 3))
