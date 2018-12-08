'''Решение проблемы с подменой атрибутов в декорируемой функции'''

import functools


trace_enabled = False


def trace(func):
    @functools.wraps(func)
    def inner(*args, **kwargs):
        print(func.__name__, args, kwargs)
        return func(*args, **kwargs)
    inner.__module__ = func.__module__
    inner.__name__ = func.__name__
    inner.__doc__ = func.__doc__
    return inner if trace_enabled else func


@trace
def f(x):
    '''я функция которая ничего не делает'''
    return x


print(f(42))

# -------------------------------------------------------------------

import time

def timethis(func=None, *, n_iter=100):
    if func is None:
        return lambda func: timethis(func, n_iter=n_iter)

    @functools.wraps(func)
    def inner(*args, **kwargs):
        print(func.__name__, end=" ... ")
        acc = float("inf")
        for i in range(n_iter):
            tick = time.perf_counter()
            result = func(*args, **kwargs)
            acc = min(acc, time.perf_counter() - tick)
        print(acc)
        return result
    return inner


result = timethis(sum)(range(10 ** 6))

# -------------------------------------------------------------------

"""Подсчитывает количество вызовов конкретной функции"""

def profiled(func):
    @functools.wraps(func)
    def inner(*args, **kwargs):
        inner.ncalls += 1
        return func(*args, **kwargs)

    inner.ncalls = 0  # создает атрибут функции (счетчик)
    return inner

@profiled
def identity(x):
    return x


@profiled
def identity2(x):
    return x

print(identity(42))
print(identity.ncalls)

print(identity2(42))
print(identity2.ncalls)

# -------------------------------------------------------------------

"""Декоратор - когда нужно что-то сделать один раз например инициализация"""


def once(func):
    @functools.wraps(func)
    def inner(*args, **kwargs):
        if not inner.called:
            func(*args, **kwargs)
            inner.called = True
    inner.called = False
    return inner


@once
def initialize_settings():
    print("Settings initialized.")


print(initialize_settings())
print(initialize_settings())

# -------------------------------------------------------------------

"""Декоратор для авттоматической мемоизации функции
    Мемоизация - сохранение результатов выполнения функции 
    для предотвращения избыточных вычислений"""


def memoized(func):
    cache = {}

    @functools.wraps(func)
    def inner(*args, **kwargs):
        key = args, kwargs
        if key not in cache:
            cache[key] = func(*args, **kwargs)
        return cache[key]
    return inner

# -------------------------------------------------------------------

import logging


def log(func):
    """
    Логируем какая функция вызывается
    """

    def wrap_log(*args, **kwargs):
        name = func.__name__
        logger = logging.getLogger(name)
        logger.setLevel(logging.INFO)

        # Открываем файл логов для записи
        fh = logging.FileHandler("%s.log" % name)
        fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        formatter = logging.Formatter(fmt)
        fh.setFormatter(formatter)
        logger.addHandler(fh)

        logger.info("Вызов функции: %s" % name)
        result = func(*args, **kwargs)
        logger.info("Результат: %s" % result)
        return func

    return wrap_log


@log
def double_function(a):
    """
    Умножаем полученный параметр
    """
    return a * 2


print(double_function(2))