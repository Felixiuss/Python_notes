import itertools
import doctest

'''
- Хороший тест:
    * корректный
    * понятный читателю
    * конкретный, то есть проверяет что-то одно
- Модуль doctest позволяет проверить реализацию функции на
     соответствие записаному сеансу интерпретатора
   - автоматически проверяет тесты в документации. Если ошибки нет ничего не выводится
'''

# Тестирование с помощью doctest


def rle(iterable):
    """применяет кодировку длины выполнения к последовательности."""
    """
    Doctest:
    >>> list(rle(''))
    []
    >>> list(rle('mississippi'))
    ... # doctest: +NORMALIZE_WHITESPACE
    [('m', 1), ('i', 1), ('s', 2), ('i', 1), ('s', 2),
    ('i', 1), ('p', 2), ('i', 1)]
    """
    for item, g in itertools.groupby(iterable):
        yield item, sum(1 for _ in g)


def func_m (v1, v2, v3):
    """Вычисляет среднее арифметическое трех чисел.
    >>> func_m (20, 30, 70)
    40.0
    >>> func_m (1, 5, 8)
    4.667
    """
    return round((v1+v2+v3)/3, 3)


if __name__ == '__main__':
    doctest.testmod()

# ------------------------------------------------------------------

# Тестирование с помощью assert


def test_rle():
    assert list(rle('mississippi')) == [('m', 1), ('i', 1), ('s', 2), ('i', 1), ('s', 2), ('i', 1), ('p', 2), ('i', 1)]
    assert list(rle('rraddiaatoor')) == [('r', 2), ('a', 1), ('d', 2), ('i', 1), ('a', 2), ('t', 1), ('o', 2), ('r', 1)]


def test_rle_empty():
    assert not list(rle(''))


def test_func_m():
    assert func_m(20, 30, 70) == 40
    assert func_m(2, 3, 7) == 4
    assert func_m(200, 300, 700) == 400


test_rle_empty()
test_rle()
test_func_m()

# ------------------------------------------------------------------

# Тестирование с помощью unittest
import unittest


class TestHomework(unittest.TestCase):
    # это можно использовать например для работы сресурсами: сокетами,
    # файлами, временными директориями
    # def setUp(self):
    #     self.oracle = RleOracle('http://oracle.rle.com')

    def test_rle(self):
        self.assertEqual(list(rle('mississippi')), [('m', 1), ('i', 1), ('s', 2), ('i', 1), ('s', 2), ('i', 1), ('p', 2), ('i', 1)])

    def test_rle_empty(self):
        self.assertEqual(list(rle('')), [])

    def test_func_m(self):
        self.assertEqual(func_m(10, 20, 30), 20)

    # def tearDown(self):
    #     self.oracule.close()


if __name__ == '__main__':
    unittest.main()

# ------------------------------------------------------------------

# Тестирование с помощью py.test
"""
Для использования в терминале установить pip install pytest
- python -m pytest директория/файл.py - запуск теста
- python -m pytest - q директория/файл.py - запуск теста - компактный вариант
- python -m pytest директория/файл.py :: test_some_func - запуск теста для конкретного объекта
- если запущен с параметром --doctest -modules - запустит доктесты
"""
import pytest


def test_rle():
    assert list(rle('mississippi')) == [
        ('m', 1), ('i', 1), ('s', 2), ('i', 1),
        ('s', 2), ('i', 1), ('p', 2), ('i', 1)
    ]


def test_rle_empty():
    assert not list(rle(''))


def test_func_m():
    assert func_m(11, 22, 33) == 22
    assert func_m(111, 222, 333) == 222


@pytest.mark.parametrize('s, suffix, expected', [
    ('foobar', 'bar', 'foo'),
    ('foobar', 'boo', 'foobar'),
    ('foobarbar', 'bar', 'foobar')
])
def cut_suffix(s, suffix):
    return s[:s.find(suffix)]
