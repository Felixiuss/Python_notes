"""
Декоратор staticmethod позволяет объявить статический метод,
то есть просто функцию, внутри класса. Это метод который не связан с
состоянием экземпляра и не связан с состоянием класса - он ничего не принимает,
это самая обычная функция.
"""


class SomeClass:
    @staticmethod
    def do_somethig():
        print('spam')


SomeClass.do_somethig()
s = SomeClass()
s.do_somethig()

# -----------------------------------------------------------------------
"""
Для объявления методов класса используется похожий декоратор classmethod.
Первый аргумент метод класса - непосредственно сам класс, а не его экземпляр.
"""


class Setting:
    @classmethod
    def read_from(cls, path):
        return cls()  # noop


Setting.read_from('./settings.ini')
