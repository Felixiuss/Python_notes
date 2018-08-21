# -*- coding: utf-8 -*-

roman = {'name': 'roman',
         'car': 'lanos'
         }

ira = {'name': 'ira',
       'car': 'kia'
       }

users = [roman, ira]

'''Предположим нам необходимо получить список всех машин клиентов. В стандартной реализации это выглядело так.'''

car = []

for user in users:
    car.append(user['car'])
print(car)

# С помощью генератора списков количество кода сократилось
us_car = [user['car'] for user in users]
print(us_car)

# если вдруг у когото неокажется авто, чтоб не выскочела ошибка
us_cars = [user.get('car', '') for user in users]
print(us_cars)


'''Получение списка имен которые начинаются с определенной буквы'''

names = ['ira', 'roma', 'jack', 'jonh', 'jacob']

l_names = [i for i in names if i.startswith('j')]
print(l_names)
