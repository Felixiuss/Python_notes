# обычная функция
def countdown(n):
    result = []
    while n != 0:
        result.append(n - 1)
        n -= 1
        return result


# таже функция но в качестве генератора
def gen_countdown(n):
    while n != 0:
        yield n - 1
        n -= 1


g = gen_countdown(4)
try:
    print(next(g))
    print(next(g))
    print(next(g))
    print(next(g))
    print(next(g))
except StopIteration:
    print('Data is end')

s = gen_countdown(10)
print(list(s))

for i in gen_countdown(10):
    print(i, end='*')
print('')

# ---------------------------------------------------------------\\

my_list = [x for x in range(1, 20)]


#  без генератора
def procces_list(my_list):
    for i in range(len(my_list)):
        my_list[i] += 2
    return my_list


# с генератором
def process_list_with_generator(my_list):
    for i in range(len(my_list)):
        yield my_list[i] + 2


for item in my_list:
    print(item, end=' ')
print('')

for item in procces_list(my_list):
    print(item, end=' ')
print('')

for item in process_list_with_generator(my_list):
    print(item, end=' ')
print('')
