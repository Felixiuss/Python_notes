"""
Python Parallel Processing (in 60 seconds or less)
https://dbader.org/blog/python-parallel-computing-in-60-seconds
"""
# Пример выполнения функции в однопоточном и паралельном выполнении
"""
import collections
import multiprocessing
from time import ctime, sleep, time

Scientist = collections.namedtuple('Scientist', [
    'name',
    'born',
])

scientists = (
    Scientist(name='Ada Lovelace', born=1815),
    Scientist(name='Emmy Noether', born=1882),
    Scientist(name='Marie Curie', born=1867),
    Scientist(name='Tu Youyou', born=1930),
    Scientist(name='Ada Yonath', born=1939),
    Scientist(name='Vera Rubin', born=1928),
    Scientist(name='Sally Ride', born=1951),
)


def process_item(item):
    sleep(1)
    return {
        'name': item.name,
        'age': 2018 - item.born
    }


print('SINGLE THREAD')                      # пример выполнения в однопоточном режиме
start = time()

result = map(process_item, scientists)

for i in result:
    print(i)
end = time()
print(f'\nTIme to complete : {end - start:.2f}s\n')

print('PARALLEL')                           # пример выполнения в многопоточном режиме
starts = time()

pool = multiprocessing.Pool()
result = pool.map(process_item, scientists)

for i in result:
    print(i)
ends = time()
print(f'\nTIme to complete : {ends - starts:.2f}s\n')
"""
# ----------------------------------------------------------------------------------------------------------------------

# Тоже что и предыдущий пример, но боллее окуратная и рабочая версия
# с использованием модуля multiprocessing
"""
import collections
import multiprocessing
import time
from pprint import pprint  # более презентабельный вывод


Scientist = collections.namedtuple('Scientist', [
    'name',
    'field',
    'born',
    'nobel',
])

scientists = (
    Scientist(name='Ada Lovelace', field='math', born=1815, nobel=False),
    Scientist(name='Emmy Noether', field='math', born=1882, nobel=False),
    Scientist(name='Marie Curie', field='physics', born=1867, nobel=True),
    Scientist(name='Tu Youyou', field='chemistry', born=1930, nobel=True),
    Scientist(name='Ada Yonath', field='chemistry', born=1939, nobel=True),
    Scientist(name='Vera Rubin', field='astronomy', born=1928, nobel=False),
    Scientist(name='Sally Ride', field='physics', born=1951, nobel=False),
)

pprint(scientists)
print()


def transform(x):
    print(f'Processing record {x.name}')
    time.sleep(1)
    res = {'name': x.name, 'age': 2017 - x.born}
    print(f'Done processing record {x.name}')
    return res


start = time.time()

pool = multiprocessing.Pool()
result = pool.map(transform, scientists)

end = time.time()

print(f'\nTime to complete: {end - start:.2f}s\n')
pprint(result)  # вернет список
"""
# ----------------------------------------------------------------------------------------------------

# Тот-же пример но с использованием модуля concurrent.futures
# выполняется с использования менеджере контекста
# результат работы - итератор
"""
import collections
import concurrent.futures
import time
from pprint import pprint  # более презентабельный вывод


Scientist = collections.namedtuple('Scientist', [
    'name',
    'field',
    'born',
    'nobel',
])

scientists = (
    Scientist(name='Ada Lovelace', field='math', born=1815, nobel=False),
    Scientist(name='Emmy Noether', field='math', born=1882, nobel=False),
    Scientist(name='Marie Curie', field='physics', born=1867, nobel=True),
    Scientist(name='Tu Youyou', field='chemistry', born=1930, nobel=True),
    Scientist(name='Ada Yonath', field='chemistry', born=1939, nobel=True),
    Scientist(name='Vera Rubin', field='astronomy', born=1928, nobel=False),
    Scientist(name='Sally Ride', field='physics', born=1951, nobel=False),
)

pprint(scientists)
print()


def transform(x):
    print(f'Processing record {x.name}')
    time.sleep(1)
    res = {'name': x.name, 'age': 2017 - x.born}
    print(f'Done processing record {x.name}')
    return res


start = time.time()

with concurrent.futures.ProcessPoolExecutor() as executor:
    result = executor.map(transform, scientists)

end = time.time()

print(f'\nTime to complete: {end - start:.2f}s\n')
# pprint(result)   -  в отличии от модуля multiprocessing возвращает итератор
pprint(tuple(result))
"""
# ----------------------------------------------------------------------------------------------------------------------

from concurrent import futures
import concurrent.futures


class FooError(Exception):
    pass


def foo(x, y):
    if x > y:
        raise FooError
    return y - x


with futures.ProcessPoolExecutor() as pool:
    running = [pool.submit(foo, 15, 8),
               pool.submit(foo, 6, 9),
               pool.submit(foo, 10, 9)]
    # print(running[0].result())

    if running[0].cancel():
        print('Successfuly cancelled')
    else:
        # running[0].result()
        print('Too late')


with concurrent.futures.ThreadPoolExecutor(max_workers=1) as executor:
    future = executor.submit(pow, 3, 2)
    print(future.result())



# print(foo(10, 5))