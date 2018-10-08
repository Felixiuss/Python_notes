
class Tracer:
    """
    Пример декоратора на основе класса, для троссировки вызова функции
    Не подходит для декорирования методов класса из-за 'self'(непонятно чей это экземпляр)
    """
    def __init__(self, func):   # На этапе декорирования @:
        self.calls = 0          # сохраняет оригинальную функцию func
        self.func = func

    def __call__(self, *args, **kwargs):  # При последующих вызовах: вызывает
        self.calls += 1         # оригинальную функцию func
        print('функция {1} была вызвана {0} раз(а)'.format(self.calls, self.func.__name__))
        self.func(*args, **kwargs)


@Tracer
def spam(a, b, c):    # spam = tracer(spam)
    print(a + b + c)  # Обертывает функцию spam объектом декоратора


# spam(3, 4, 5)
# print(spam.calls)
# print(spam)
# spam.calls = 100
# print(spam.calls)
# spam(1, 2, c=3)

# ---  Эквивалентная реализация без использования декоратора:  --- #

# calls = 0
#
#
# def tracer(func, *args):
#     global calls
#     calls += 1
#     print('call %s to %s' % (calls, func.__name__))
#     func(*args)
#
#
# def spam(a, b, c):
#     print(a, b, c)


# spam(1, 2, 3)          # Обычный вызов без трассировки: невнимательность?
# tracer(spam, 1, 2, 3)  # Вызов с трассировкой без применения декоратора call 1 to spam


def tracer(func):
    """
    Пример декоратора на основе функции, для троссировки вызова функций.
    Хорошо подходит как для функций, так и для классов к их меттодам
    """
    calls = 0

    def wrapper(*args, **kwargs):
        nonlocal calls
        calls += 1
        print('функция {} была вызвана {} раз(а)'.format(func.__name__, calls))
        return func(*args, **kwargs)

    return wrapper

#  может применятся к простым функциям


@tracer
def eggs(x, y):
    return x ** y


# print(eggs(5, 6))
# print(eggs(6, 6))
# print(eggs(x=3, y=2))

#  может применятся к методам классов


class Person:
    def __init__(self, name, pay):
        self.name = name
        self.pay = pay

    @tracer
    def giveRaise(self, percent):
        self.pay *= (1.0 + percent)

    @tracer
    def lastName(self):
        return self.name.split()[-1]


# print('methods...')
# bob = Person('Bob Smith', 50000)
# sue = Person('Sue Jones', 100000)
# print(bob.name, sue.name)
# sue.giveRaise(.10)
# print(sue.pay)
# print(bob.lastName(), sue.lastName())
# bob.giveRaise(.10)
# print(bob.pay)

# -------------------------------------------------------------------------------------------

import time


class Timer:
    """
    декоратор на основе класса который реализует хронометраж выполнения декорируемых
    функций – время единственного вызова и накопленное время всех вызовов.
    """
    def __init__(self, func):
        self.func = func
        self.alltime = 0

    def __call__(self, *args, **kwargs):
        start = time.clock()
        result = self.func(*args, **kwargs)
        elapsed = time.clock() - start
        self.alltime += elapsed
        print('%s: %.5f, %.5f' % (self.func.__name__, elapsed, self.alltime))
        return result


@Timer
def listcomp(n):
    return [x * 2 for x in range(n)]


@Timer
def mapcall(n):
    return list(map((lambda x: x * 2), range(n)))


# result = listcomp(5)
# listcomp(50000)
# listcomp(500000)
# listcomp(1000000)
# print(result)
# print('allTime = {}'.format(listcomp.alltime))  # общее время вызовов listcomp
#
# print('')
# result = mapcall(5)
# mapcall(50000)
# mapcall(500000)
# mapcall(1000000)
# print(result)
# print('allTime = {}'.format(mapcall.alltime))  # Общее время всех вызовов mapcall
#
# print('')
# print('map/comp = {}'.format(round(mapcall.alltime / listcomp.alltime, 3)))


# --------------------------  Добавление аргументов декоратора  ------------------------------------ #

def timer(label='', trace=True):              # Аргументы декоратора сохраняются
    class Timer:
        """
        Добавляет по желанию метку для вывода, а также может включать или отключать
        вывод трассировочный сообщений
        """
        def __init__(self, func):
            self.func = func                  # на этапе декорирования сохраняется
            self.alltime = 0                  # декорируемая функция

        def __call__(self, *args, **kwargs):  # При вызове вызывается оригинал
            start = time.clock()
            result = self.func(*args, **kwargs)
            elapsed = time.clock() - start
            self.alltime += elapsed
            if trace:
                format = '%s %s: %.5f, %.5f'
                values = (label, self.func.__name__, elapsed, self.alltime)
                print(format % values)
            return result
    return Timer


@timer(label='[CCC]==>')
def listcomp(n):
    return [x * 2 for x in range(n)]


@timer(trace=True, label='[MMM]==>')
def mapcall(n):
    return list(map((lambda x: x * 2), range(n)))


@timer(trace=False, label='[trace=False]==>')
def add(a):
    return a ** 10


# for func in (listcomp, mapcall, add):
#     print('')
#     result = func(5)
#     func(50000)
#     func(500000)
#     func(1000000)
#     print('allTime = % s' % func.alltime)  # Общее время всех вызовов
#
# print(add.alltime)

# ----------------------------------------------------------------------------------------------------

# Этот пример реализует классический шаблон проектирования singleton (одиночка),
# когда в каждый конкретный момент во время работы программы может существовать не более
# одного экземпляра класса.

def singleton(aClass):
    """
    На основе функции
    """
    instance = None

    def oncall(*args, **kwargs):
        nonlocal instance
        if instance is None:
            instance = aClass(*args, **kwargs)
        return instance
    return oncall


class Singleton:
    """
    На основе класса
    """
    def __init__(self, aClass):
        self.aClass = aClass
        self.instance = None

    def __call__(self, *args, **kwargs):
        if self.instance is None:
            self.instance = self.aClass(*args, **kwargs)
        return self.instance


# Примеры:

@singleton
class Human:
    def __init__(self, name, hour, rate):
        self.name = name
        self.hour = hour
        self.rate = rate

    def pay(self):
        return self.hour * self.rate


@singleton
class Spam:
    def __init__(self, val):
        self.attr = val


# bob = Human('Bob', 40, 10)
# print(bob.name, bob.pay())
#
# sue = Human('Sue', 50, 20)  # экземпляр не будет создан
# print(sue.name, sue.pay())  # вернется значение первого созданного экземпляра
#
# print('')
# x = Spam(42)
# y = Spam(99)  # экземпляр не будет создан
#
# print(x.attr)
# print(y.attr)  # вернется значение первого созданного экземпляра

# ---------------------------------------------------------------------------------------------------

# Пример регистрации методов или классов, используемых приложением для последующей обработки.
# Возможно эти объекты будут вызыватся приложением в ответ на какие-либо события
# Этот прием можно использовать при создании пользовательского интерфейса, например чтобы
# зарегистрировать обработчики действий пользователя. Обработчики могут регистрироваться по имени
# функции или класса, как сделано здесь, или можно было бы определять обрабатываемые события
# с помощью аргументов декоратора – для сохранения этих аргументов можно было бы использовать
# дополнительную инструкцию def, обертывающую декоратор.


registry = {}


def register(obj):                      #  Дукоратор функций и классов
    """
    регистрация дукорируемых объектов
    """
    registry[obj.__name__] = obj        # Добфвить в реестр
    return obj                          # Возвращает сам объект obj, а не обертку


@register
def spam(x):
    return(x ** 2)


@register
def ham(x):
    return(x **3)


@register
class Egss:
    def __init__(self, x):
        self.data = x ** 4

    def __str__(self):
        return str(self.data)


# print('Registry:')
# for name in registry:
#     print(name, '=>', registry[name], type(registry[name]))
#
# print('\nManual calls:')
# print(spam(2))              # Вызов объекта вручную
# print(ham(2))               # Вызовы не перехватываются декоратором
# X = Egss(2)
# print(X)
#
# print('\nRegistry calls:')
# for name in registry:
#     print(name, '=>', registry[name](5))    # Вызов самих объектов как функций с передачей аргументов из реестра

#                                           ******

# Взгляните на следующие декораторы функций, – они присваивают функциям новые атрибуты, в которых
# сохраняется информация для последующего использования приложением, но не добавляют новый слой
# обертывающей логики, перехватывающей вызовы этих функций:

# Непосредственное расширение декорируемых объектов

def decorate(func):
    func.marked = True      # Присваиваетт функции атрибут
    return func             # для последующего использования

@decorate
def add(a, b):
    return a + b

print(add.marked)


def annotate(text):
    def decorate(func):
        func.lable = text
        return func
    return decorate

@annotate('some data')
def add2(a, b):
    return a + b

print(add2(1, 2), add2.lable)