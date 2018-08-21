# -*- coding: utf-8 -*-

# Oleg Molchanov   https://www.youtube.com/watch?v=Ss1M32pp5Ew&index=6&list=PLlWXhlUMyooYqypXIju-5czBtppKaWimP

from datetime import datetime


def timeit(func):
    def wrapper(*args, **kwargs):
        start = datetime.now()
        result = func(*args, **kwargs)
        end = datetime.now() - start
        return result, end
    return wrapper


@timeit
def one(n):
    l = []
    for i in range(n):
        if i % 2 == 0:
            l.append(i)
    return l


@timeit
def two(n):
    l = [i for i in range(n) if i % 2 == 0]
    return l


print(one(100))
print(two(100))

l1 = timeit(one)
print(type(l1), l1.__name__)
a = l1(10)
print(a)

print(timeit(one)(10))
