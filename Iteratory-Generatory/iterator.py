class SimpleIterator:
    """
    пример создания собственного класса итератора
    """

    def __init__(self, limit=5):
        self.limit = limit
        self.counter = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.counter < self.limit:
            result = self.counter + 1
            self.counter += 1
            return result
        else:
            raise StopIteration


iter = SimpleIterator(5)

for i in iter:
    print(i)


# def simple_generator(val):
#     """пример генератора"""
#     while val > 0:
#         val -= 1
#         yield 1
#
# gen_iter = simple_generator(5)
# print(type(gen_iter))
# print(next(gen_iter))
# print(next(gen_iter))
# print(next(gen_iter))
# print(next(gen_iter))
# print(next(gen_iter))
# # print(next(gen_iter))