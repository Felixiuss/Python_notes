'''Кладов примеры декораторов'''

import time
import functools


def profile(f):
    """
    Декоратор - подсчитывает количество вызовов функции и время выполнения
    """
    @functools.wraps(f)
    def inner(*args, **kwargs):
        start = time.perf_counter()
        res = f(*args, **kwargs)
        elapsed = time.perf_counter() - start
        inner.__n_calls__ += 1
        inner.__total_time__ += elapsed
        return res

    inner.__n_calls__ = 0
    inner.__total_time__ = 0
    return inner


def memoize(f):
    """
    Декоратор - для мемоизации вызовов функции (сокращение вызовов)
    """
    cache = {}  # если значения вызовов есть к словаре, они берутся от туда, а не делается вызов функции

    @functools.wraps(f)
    def inner(*args, **kwargs):
        key = (args, frozenset((kwargs.items())))
        if key not in cache:
            cache[key] = f(*args, **kwargs)
        return cache[key]

    inner.__cache__ = cache
    return inner


@profile
# @memoize
@functools.lru_cache(maxsize=None)
def fib(n):
    return 1 if n <= 1 else fib(n - 1) + fib(n - 2)

print(fib(22))
print(fib.__total_time__)
print(fib.__n_calls__)


# @profile
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
#
# print(func.__total_time__)
# print(func.__n_calls__)
