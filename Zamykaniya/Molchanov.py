# -*- coding: utf-8 -*-

# Oleg Molchanov   https://www.youtube.com/watch?v=wKyUZY4-Dxc&t=5s


def one():
    x = ['one', 'two']
    y = ['free', 'four']

    def inner():
        print(x)
        print(y)
        print(id(x))
        print(id(y))
    return inner


o = one()
o()

print(dir(o))
print(o.__closure__)   # возвращает кортеж объектов из объемлюющей области видимости (на которые есть ссылки)
print(o.__closure__[0])
print(o.__closure__[1])
print(dir(o.__closure__[0]))
print(o.__closure__[0].cell_contents)  # способ вызвать объект который недоступен из глобальной области
print(o.__closure__[1].cell_contents)
a = o.__closure__[0].cell_contents
b = o.__closure__[1].cell_contents
print(id(a))
print(id(b))

print(a)
print(b)

b.append('five')  # теперь можно производить манипуляции
print(b)


