"""
r - открыть файл для чтения (используется по умолчанию). Также подразумевается, что файл для чтения уже существует.
w - открыть файл для записи. Если в файле уже есть данные, они удаляются. Если файл не существует, он будет создан.
a - открыть файл для добавления в конец. Сохраняет содержимое файла, добавляя данные в конец файла. Если файл не существует, он будет создан.
x - открыть новый файл для записи.Вызов завершается неудачей, если файл уже существует.
b - запись двоичных данных (медиа, фото, видео)
"""

# with open('file.txt', 'r') as f:
#     for i in f.readlines():
#         print(i.title(), end='')


def write_func(name, text):
    box = name + '.txt'
    with open(box, 'w') as file:
        file.write(text + '\n')


if __name__ == '__main__':
    nm = input('Type your name: ')
    tx = input('Type your masage: ')
    write_func(nm, tx)

# ---------------------------------------------------------------------------------------------

import pickle

data = {
    'a': [1, 2.0, 3, 4+6j],
    'b': ("character string", b"byte string"),
    'c': {None, True, False}
}

with open('data.pickle.txt', 'wb') as f:
    pickle.dump(data, f)

with open('data.pickle.txt', 'rb') as f:
    data_new = pickle.load(f)

print(data_new)


X, Y, Z = 43, 44, 45
S = 'Spam'
D = {'a': 1, 'b': 2}
L = [1, 2, 3]

with open('data.pickle.txt', 'wb') as f:
    pickle.dump((X, S, D, L), f)

with open('data.pickle.txt', 'rb') as f:
    data_new = pickle.load(f)

print(data_new)
