"""
- Как и свойства, дескрипторы позволяют контролировать чтение,
  изменение и удаление атрибута, но в отличии от свойств, дескрипторы
  можно переиспользовать.
- Дескриптор - это экземпляр класса, реализующего любую комбинацию
  методов __get__, __set__, и __delete__.
- Все дескрипторы можно поделить на две группы:
  * дескрипторы данных, определяющие как минимум метод __set__ (для установки какого либо значения)
  * остальные non-data descriptors у которого например один метод __get__
    в него мы попадаем только если у __dict__ экземпляра нет одноименного атрибута
- Данные дескриптора лучше всего хранить в __dict__  самого экземпляра. Минус - их легко можно посмотреть (ex.__dict__)
"""


class Proxy:
    """
    Дескриптор - удаляет, возвращает, устанвливает значение если оно не ниже 0
    """
    def __init__(self, label):
        self.label = label  # метка дескриптора которая позволит легко идентифицировать его в __dict__ экземпляра

    def __get__(self, instance, owner):
        # ... do something ...
        return instance.__dict__[self.label]

    def __set__(self, instance, value):
        assert value >= 0, 'non-negative value required'
        instance.__dict__[self.label] = value

    def __delete__(self, instance):
        del instance.__dict__[self.label]


class Something:
    # данный атрибут теперь является дескриптором у которого переопределено поведение при доступе к атр., при
    # присваиванию значения и при удалении
    attr = Proxy('attr')


some = Something()
some.attr = 42
print(some.attr)
print(some.__dict__)
del some.attr
print(some.__dict__)


# Пример дескриптора: @property
class Property:
    def __init__(self, get=None, set=None, delete=None):
        self._get = get
        self._set = set
        self._delete = delete

    def __get__(self, instance, owner):
        if self._get is None:
            raise AttributeError("unreadable attribute")
        return self._get(instance)

    # __set__ и __delete__ аналогично


class Something2:
    @Property
    def attr(self):
        return 43


class ImportantValue:
    """
    Пример дескриптора который логирует (записывает) значение атрибута в файл
    """
    def __init__(self, amount):
        self.amount = amount

    def __get__(self, obj, obj_type):  # сам объект и тип_объекта
        return self.amount

    def __set__(self, obj, value):
        with open('log.txt', 'w') as f:  # 'a' - дозапись
            f.write(str(value))

        self.amount = value


class Acount:
    amount = ImportantValue(100)


bobs_account = Acount()
bobs_account.amount = 200

with open('log.txt', 'r') as f:
    print(f.read())

jenny = Acount()
print(jenny.amount)
jenny.amount = 300
print(jenny.amount)
print(bobs_account.amount)  # проблема хранения данных в дескрипторе


class Property_2:  # еще один пример @property от coursera
    def __init__(self, getter):
        self.getter = getter

    def __get__(self, obj, obj_type=None):
        if obj is None:
            return self
        return self.getter(obj)


class Class:
    @property
    def original(self):
        return 'original'

    @Property_2
    def custom_sugar(self):
        return 'custom sugar'

    def custom_pure(self):
        return 'custom pure'


obj = Class()
print(obj.original)
print(obj.custom_sugar)
print(obj.custom_pure())


