# -*- coding: utf-8 -*-


def fact(n: int) -> int:
    """ факториал - рекурсия"""
    if n == 1:
        return 1
    return fact(n-1) * n


print(fact(5))

# ---------------------------------------------------------------------------------


def fib(n):
    """Пример работы рекурсии на примере чисел Фибоначчи"""
    if n == 1 or n == 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)


# for i in range(1, 16):
#     print(fib(i), sep='*')

# ---------------------------------------------------------------------------------


def mysum(l):
    """суммирование элементов колекции с помощью рекурсии"""
    first, *rest = l
    return first if not rest else first + mysum(rest)


# print(mysum([1, 2, 3, 4, 5]))
# print(mysum(('s', 'p', 'a', 'm')))
# print(mysum([1]))

# -----------------------------------------------------------------------------------


def sumtree(L):
    """суммирование элементов колекции произвольной вложенности с помощью рекурсии"""
    tot = 0
    for x in L:                              # Обход элементов одного уровня
        if not isinstance(x, list):
            tot += x                         # Числа суммируются непосредственно
        else:
            tot += sumtree(x)                # Списки обрабатываются рекурсивными вызовами
    return tot


# L = [1, [2, [3, 4], 5], 6, [7, 8]]           # Произвольная глубина вложения
# print(sumtree(L))                            # Выведет 36
#
# # Патологические случаи
# print(sumtree([1, [2, [3, [4, [5]]]]]))      # Выведет 15 (центр тяжести справа)
# print(sumtree([[[[[1], 2], 3], 4], 5]))      # Выведет 15 (центр тяжести слева)

# -----------------------------------------------------------------------------------


def flatten(L):
    """распаковка колекции произвольной вложенности в одномерный массив"""
    rest = []
    for x in L:
        rest.append(x) if not isinstance(x, (list, tuple)) else rest.extend(flatten(x))
    return rest


L = [1, [2, [3, 4], 5], 6, [7, 8]]           # Произвольная глубина вложения
print(flatten(L))

print(flatten([1, [2, [3, 4], 5], [], 6, [7, 8], 4, [55, [66, 77], 88], 99, [70, 85]]))
print(flatten((1, (2, (3, 4), 5), 6, (7, 8), (), 4, (55, (66, 77), 88), 99, (70, 85))))
print(sum(flatten((1, (2, (3, 4), 5), 6, (7, 8), (), 4, (55, (66, 77), 88), 99, (70, 85)))))

# -----------------------------------------------------------------------------------
