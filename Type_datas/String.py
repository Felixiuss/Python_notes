# -*- coding: utf-8 -*-
import unittest

""" Список задач

    01. Вывести количество наиболее частого символа в строке: "afCgGtkgttat" == 4
    02. Перевести переданную в функцию строку в верхний регистр, если строка содержит больше двух заглавных символа в первых четырех символах.
    03. Дан текст, который содержит различные английские буквы и знаки препинания. Вам необходимо найти самую частую букву в тексте. Результатом должна быть буква в нижнем регистре.
            При поиске самой частой буквы, регистр не имеет значения, так что при подсчете считайте, что "A" == "a". Убедитесь, что вы не считайте знаки препинания, цифры и пробелы, а только буквы.
            Если в тексте две и больше буквы с одинаковой частотой, тогда результатом будет буква, которая идет первой в алфавите. Для примера, "one" содержит "o", "n", "e" по одному разу, так что мы выбираем "e".
    04. Функция принимает строку и возвращает копию двух последних символов умноженых на 4
    05. Функция принимает строку и если длина строки больше трех символов возвращает первые три символа иначе всю строку
    06. Функция для получения первой половины преданной строки.
    07. Функция f(str, word) - вставить word в середину str
    08. func(str) - если длинна строки равно 4, вернуть перевернутую строку.
    09. func(some_text) - вернуть тот же текст но с шириной строки 70 и префиксом перед каждой строкой '> '
    10. Вернуть строку в которой поменяны местами первый и последний символ.
    11. Шифр Цезаря func(слово, шаг смещения)
    12. Есть некое предложение, найти в нем две подстроки : 'not' и 'poor'. Если 'poor' следует после 'not' - то заменить все от 'not'  до 'poor' подстрокой 'good' (function)
    13. Функция принимает две строки: 'abc' , 'xyz' и после манипуляции возвращает одну строку 'xyc abz'
    14. Функция принимет строку и суффикс - вернуть новую строку без суффикса. Второй вариант - тоже но с префиксом
    15. Убрать из строки гласные буквы.
    16. Стефан и София забывают о безопасности и используют простые пароли для всего. Помогите Николе разработать модуль для проверки паролей на безопасность. Пароль считается достаточно стойким, 
            если его длина больше или равна 10 символам, он содержит, как минимум одну цифру, одну букву в верхнем и одну в нижнем регистре. Пароль может содержать только латинские буквы и/или цифры.
    17. Из последовательности '1010010100010000100101000100000100101000' извлечь наибольшую последовательность '0' между единицами - включая единицы ('10000...01')
    18. Посчитать количество строчных (маленьких) и прописных (больших) букв в введенной строке. Учитывать только английские буквы.
    19. Вводятся строки. Определить самую длинную строку и вывести ее номер на экран. Если самых длинных строк несколько, то вывести номера всех таких строк.
    20. Найти в строке указанную подстроку и заменить ее на новую. Строку, ее подстроку для замены и новую подстроку вводит пользователь.
    21. Вводится строка. Требуется удалить из нее повторяющиеся символы и все пробелы. Например, если было введено "abc cde def", то должно быть выведено "abcdef".
    22. Вводится строка. Удалить из нее все пробелы. После этого определить, является ли она палиндромом (перевертышем), т.е. одинаково пишется как с начала, так и с конца.
    23. Вводится ненормированная строка, у которой могут быть пробелы в начале, в конце и между словами более одного пробела. Привести ее к нормированному виду, т.е. удалить все пробелы в начале и конце, а между словами оставить только один пробел.
    24. Вам предлагается некоторый текст, который может содержать осмысленные слова. Вы должны подсчитать количество таких слов в этом тексте. Слово может стоять отдельно, 
            а может присутствовать как часть другого слова. Регистр букв не имеет значения. Слова даны в нижнем регистре и не повторяются. Если слово встречается в тексте несколько раз, 
            оно должно быть посчитано только один раз. Например, текст "How aresjfhdskfhskd you?", слова - ("how", "are", "you", "hello"). Результат должен быть равен 3.
    25. Вам необходимо найти длину самой длинной подстроки, которая состоит из одинаковых букв. Например, строка "aaabbcaaaa" состоит из четырех подстрок с одинаковыми буквами "aaa", "bb","c" и "aaaa". Последняя подстрока является самой длинной, что и делает ее ответом.
    26. Написать алгоритм сжатия, который сжимает повторяющиеся символы в строке. Кодирование осуществляется следующим образом:
        s = 'aaaabbсaa' преобразуется в 'a4b2с1a2', то есть группы одинаковых символов исходной строки заменяются на этот символ и количество его повторений в этой позиции строки. Кодирование должно учитывать регистр символов.
    27. Реализация шифра Цезаря v2
    28. проверка защищенности пешки в шахматах  https://py.checkio.org/ru/mission/pawn-brotherhood/

"""


"""Экранирование последовательностей
\' - одинарная кавычка
\" - двойная кавычка
\t - символ вертикальной табуляции
\n - символ переноса строки

    Сырая строка
print("\tell me")
>>      ell me
print(r"\tell me") - экранирование не обрабаттывается
>> \tell me
"""
'''
print(list(map(ord, "hello")))
print(list(map(ord, 'привет')))
print(list(map(chr, [104, 101, 108, 108, 111])))

# удаление символов
print(']>>foo bar<<['.lstrip(']>'))
print(']>>foo bar<<['.rstrip('[<'))
print(']>>foo bar<<['.strip('[]<>'))
print('\t foo bar \r\n'.strip())

# разделение
print("foo,bar".split(","))
print("foo,,,bar".split(","))
print("\t foo bar \r\n".split())
print("file.name.cout.txt".rsplit(".", 1))
#  возвращает кортеж из трех элементов(подстрока до разделителя, разделитель, и подстрока после)
print("foo,bar,baz".partition(","))
print("foo,bar,baz".rpartition(","))

# соединение
print(",".join(['foo', 'bar', 'baz']))
print(",".join(filter(None, ['', 'foo'])))
print(",".join("bar"))

# проверка на вхождение
print('foo' in 'foobar')
# True
print('yada' not in 'foobar')
# True
print('foobar'.startswith('foo'))
# True
print('foobar'.endswith(('boo', 'bar', 'egg')))  # можно проверять сразу несколько
# True

# поиск подстроки
'abracadabra'.find('ra')  # >> 2
'abracadabra'.find('ra', 0, 3)  # >> -1    # ищет наличие в срезе, если нет то -1
'abracadabra'.index('ra', 0, 3)  # >> ValueError    # если не находит - Error

# замена подстроки
'abracadabra'.replace('ra', '**')  # >> 'ab**cadab**'
'abracadabra'.replace('ra', '**', 1)  # >> 'ab**cadabra'
translation_map = {ord('a'): '*', ord('b'): '?'}
'abracadabra'.translate(translation_map)
# '*?r*c*d*?r*'

# Предикаты
'100500'.isdigit()  # >> True
'foo100500'.isalnum()  # >> True
'foobar'.isalpha()  # >> True
'foobar'.islower()  # >> True
'FOOBAR'.isupper()  # >> True
'Foo Bar'.istitle()  # >> True
'\r  \n\t \r\n'.isspace()  # True

# Форматирование строк
'{}, {}, how are you?'.format('Hello', 'Sally')  # >> Hello, Sally, how are you?
'Today is September, {}th'.format(28)  # >> Today is September, 28th
point = 0, 10
'x = {0[0]}, y = {0[1]}'.format(point)  # >> x = 0, y = 10
dct = {'x': 0, 'y': 10}
'x = {0[x]}, y = {0[y]}'.format(dct)  # >> x = 0, y = 10
# TODO

# Спецификация формата TODO
'''

# ----------------------------------------------------------------------------------------------------------------------
"""01"""
# string = "aCgGtgttat"
#
# res = []
# for i in string:
#     res.append(string.count(i))
# print(max(res))
"""02"""
# def to_uppercase(st):
#     num_upper = 0
#     for letter in st[:4]:
#         if letter.upper() == letter:
#             num_upper += 1
#     if num_upper >= 2:
#         return st.upper()
#     return st
#
# print(to_uppercase('Python'))
# print(to_uppercase('PyThon'))
"""03"""
# def checkio(text: str) -> str:
#     text = text.lower()
#     res = {}
#     res = {i: text.count(i) for i in text if i not in res and i.isalpha()}
#     rest = sorted(res.items(), key=lambda x: x[1])
#     result = []
#     [result.append(i[0]) for i in rest if i[1] == rest[-1][1]]
#     return min(result)


# def checkio(text: str) -> str:
#     from collections import Counter
#     c = Counter(b for b in text.lower() if b.isalpha())
#     e = c.most_common(1)[0][1]
#     return sorted(f for f in c.most_common() if f[1] == e)[0][0]


# def checkio(text: str) -> str:
#     import string
#     return max(string.ascii_lowercase, key=text.lower().count)


# if __name__ == '__main__':
#     assert checkio("Hello World!") == "l"
#     assert checkio("How do you do?") == "o"
#     assert checkio("One") == "e"
#     assert checkio("Oops!") == "o"
#     assert checkio("AAaooo!!!!") == "a"
#     assert checkio("abe") == "a"
#     print("Start the long test")
#     assert checkio("a" * 9000 + "b" * 1000) == "a"
#     print("The local tests are done.")
"""04"""
# def insert_end(st):
#     sub_str = st[-2:]
#     return sub_str * 4
#
# print(insert_end('hello'))
# print(insert_end('Python'))
"""05"""
# def f(st):
#     return st[:3] if len(st) > 3 else st
#
# print(f('hello'))
"""06"""
# def stritng_first_half(st):
#     return st[:len(st)//2]
#
# print(stritng_first_half('Python'))
# print(stritng_first_half('JavaScript'))
"""07"""
# def insert_string_middle(str, word):
#     return str[:2] + word + str[2:]
#
# print(insert_string_middle('{{}}', 'python'))
# print(insert_string_middle('[[]]', 'python'))
# print(insert_string_middle('<<>>', 'python'))
"""08"""
# def reverse_string(str):
#     if len(str) % 4 == 0:
#         return ''.join(reversed(str))
#     return str
#
# print(reverse_string('spam'))
# print(reverse_string('hello'))
"""09"""
# some_text = '''
#     Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmodtempor incididunt ut labore et dolore magna
#     aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo
#     consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.
#     Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
#     '''
# def func(text):
#     import textwrap
#
#     text_without_indentation = textwrap.dedent(text)
#     wrapped = textwrap.fill(text_without_indentation, width=70)
#     return textwrap.indent(wrapped, '> ')
#
# print(func(some_text))
"""10"""
# def change_string(str):
#     return str[-1] + str[1:-1] + str[:1]
#
# print(change_string('python'))
# print(change_string('spam'))
"""11"""
# from string import ascii_uppercase as app, ascii_lowercase as low
#
# def cesar_encrypt(realText, step):
#     outText = []
#     cryptText = []
#
#     uppercase = app
#     lowercase = low
#
#     for letter in realText:
#         if letter in uppercase:                 # если символ заглавный
#             index = uppercase.index(letter)     # узнаем его индекс в наборе заглавных символов
#             crypting = (index + step) % 26      # индекс + шаг % количество букв в алфавите
#             cryptText.append(crypting)          # добавляем в промежуточный список для декодировки
#             new_letter = uppercase[crypting]    # подставляем новую букву по полученному индексу
#             outText.append(new_letter)          # добавляем букву в список для выхода
#         elif letter in lowercase:
#             index = lowercase.index(letter)
#             crypting = (index + step) % 26
#             cryptText.append(crypting)
#             new_letter = lowercase[crypting]
#             outText.append(new_letter)
#     return ''.join(outText)
#
#
# code = cesar_encrypt('heLLo WorlD', 10)
# print(code)
"""12"""
# s = 'The lyrics is not that poor!'
#
# def not_poor(str):
#     snot = str.find('not')
#     spoor = str.find('poor')
#
#     if spoor > snot:
#         return str.replace(str[snot:(spoor+4)], 'good')  #  срез str помещенный в replace
#
# print(not_poor(s))
"""13"""
# def char_mix_up(a, b):
#     new_a = b[:2] + a[2:]
#     new_b = a[:2] + b[2:]
#
#     return new_a + ' ' + new_b
#
# print(char_mix_up('abc', 'xyz'))
"""14"""
# def cut_suffix(s, suffix):
#     return s[:s.find(suffix)]
#
# print(cut_suffix('foobar', 'bar'))
# print(cut_suffix('kolloborator', 'tor'))
"""15"""
# def strip(str, chars):
#     return ''.join(c for c in str if c not in chars)
#
# print(strip('hello world my name is roman', 'aeiou'))
"""16"""
# def checkio(data):
#     import string
#
#     dig = [i for i in data if i in string.digits]
#     str_low = [i for i in data if i in string.ascii_lowercase]
#     str_title = [i for i in data if i in string.ascii_uppercase]
#
#     return True if len(data) > 9 and dig and str_low and str_title else False
#
#
# if __name__ == '__main__':
#     assert checkio('A1213pokl') == False, "1st example"
#     assert checkio('bAse730onE4') == True, "2nd example"
#     assert checkio('asasasasasasasaas') == False, "3rd example"
#     assert checkio('QWERTYqwerty') == False, "4th example"
#     assert checkio('123456123456') == False, "5th example"
#     assert checkio('QwErTy911poqqqq') == True, "6th example"
#     print("Тест пройден")
"""17"""
# st = '1010010100010000100101000100000100101000'
# ss = sorted(st.split('1'))
# print('1' + ss[-1] + '1')

# второй вариант
# ss = st.split('1')
# print('1' + max(ss, key=len) + '1')
"""18"""
# s = '*ParAlLelEpIpeDNIy-TreUgOlNik*'
# let_s = 0
# let_b = 0
#
# for i in s:
#     if 'a' <= i <= 'z':
#         let_s += 1
#     else:
#         if 'A' <= i <= 'Z':
#             let_b += 1
# print(let_s)
# print(let_b)
#
# # второй вариант
# def func(st):
#     from string import ascii_uppercase as app, ascii_lowercase as low
#     lower = 0
#     upper = 0
#
#     for letter in st:
#         if letter in app:
#             upper +=1
#         elif letter in low:
#             lower += 1
#     return lower, upper
#
# print(func(s))
"""19"""
# def find_long_worlds(st):
#
#     split_str = st.replace(',', '').split(' ')
#     large_word = max(split_str, key=len)  # или - sorted(split_str, key=len)[-1]
#     # large_word = sorted(split_str, key=len)[-1]
#     print(large_word)
#     lst_words = [item for item in split_str if len(item) == len(large_word)]
#     res = [split_str.index(i) for i in lst_words]
#
#     return res, lst_words
#
#
# file = 'hello hgjfur, world roma, andrey sergey'
# se = "План на главу: изучить все необходимое, чтобы вы смогли изменить свое веб- приложение и организовать хранение журналируемых сведений в базе данных, а не в текстовом файле, как было в главе 6. После этого вы сможете ответитьна вопросы, заданные в прошлой главе: Сколько запросов было обработано? Какойсписок букв встречается чаще всего? С каких IP-адресов приходили запросы? Какой браузер использовался чаще?Вначале нужно решить, какой системой управления базами данных (СУБД) мы будем пользоваться. Выбор большой, можно потратить десятки страниц, обсуждая достоинства и недостатки каждой из технологий. Но мы не станем этого делать,а сразу выберем популярную базу данных MySQL.оцесс установки MySQL зависит от операционной системы. К счастью, разработчики MySQL (и родственной ей MariaDB) постарались на совесть, чтобы максимально упростить процесс установки."
# print(find_long_worlds(se))
# print(find_long_worlds(file))
# print(find_long_worlds('hello'))
"""20"""
# string = input('Введите строку: ')
# replace_word = input('Введите новое слово: ')
# del_word = input('На какое слово вы хотите его заменить: ')
#
# print(string.replace(del_word, replace_word))
"""21"""
# string = "abc cde def"
#
# res = ''
# format_string = string.replace(' ', '')
# for i in format_string:
#     if i not in res:
#         res += i
# print(res)
#
# # второй вариант
# def func(string):
#     res2 = []
#     format_string = string.replace(' ', '')
#     [res2.append(x) for x in format_string if x not in res2]
#     return ''.join(res2)
#
# print(func(string))
#
# # третий вариант
# s_new = ''
# for i in range(len(string)):
#     if s_new.find(string[i]) == -1 and string[i] != ' ':
#         s_new += string[i]
# print(s_new)
"""22"""
# string = 'as dff ds a'
#
#
# def is_palindrom(string):
#     string = string.replace(' ', '')
#     return True if string == string[::-1] else False
#
#
# print(is_palindrom(string))
"""23"""
# string = ' hello  my  name is  Roma hhb  hhh  hihi hhih  hihih'
# sf = string.strip().replace('  ', ' ')
# print(sf)
"""24"""
# def count_words(s, d):
#     res = 0
#     sl = s.lower()
#     for i in d:
#         if sl.find(i) != -1:
#             res += 1
#     return res
#
#
# print(count_words("How aresjfhdskfhskd you?", {"how", "are", "you", "hello"}))
"""25"""
# from itertools import groupby
# x = ['sdsffffse', '  ', '', 'ddvvrwwwrggg', 'hhffeeeeeeuujjcndjf']
#
#
# def long_repeat(line):
#     return max(len(list(g)) for i, g in groupby(line)) if line else 0
#
#
# for _ in x:
#     print(long_repeat(_))


# второй вариант (не будет работать с вариантом x = '  ') ------------------------------------


# def long_repeat(line):
#     if not line: return 0
#     line += ' '
#     res = []
#     count = 1
#
#     for i in range(len(line) - 1):
#         if line[i] == line[i + 1]:
#             count += 1
#             continue
#         res.append(count)
#         count = 1
#     return max(res)
#
#
# x = ['sdsffffse', '', 'ddvvrwwwrggg', 'hhffeeeeeeuujjcndjf']
#
# for _ in x:
#     print(long_repeat(_))

# третий вариант (не будет работать с вариантом x = '  ') ------------------------------------


# def long_repeat(line):
#     if not line: return 0
#     genome = line + ' '
#     res = []
#     s = 0
#     n = genome[0]
#     for i in genome:
#         if n != i:
#             res.append(s)
#             s = 0
#             n = i
#         s += 1
#     return max(res)
#
# x = ['sdsffffse', '', 'ddvvrwwwrggg', 'hhffeeeeeeuujjcndjf']
#
# for _ in x:
#     print(long_repeat(_))
"""26"""
# string = ['aaaabbсaa', 'nnHHssKKKrrBBJJJ', '11KKjjHHHoOOODd^^77^']
#
#
# def genome(line):
#
#     line += ' '
#     s = 0
#     n = line[0]
#     result = ''
#
#     for i in line:
#         if n != i:
#             result += n + str(s)
#             s = 0
#             n = i
#         s += 1
#     return result
#
#
# for i in string:
#     print(genome(i))
"""27"""
# def to_encrypt(text: str, delta: int) -> str:
#
#     result = ''
#
#     for i in text:
#         if 'a' <= i <= 'z':
#             c = chr((ord(i) + delta - ord('a')) % 26 + ord('a'))
#             # c = chr(ord('a') + (ord(i) - ord('a') + delta) % 26)
#             result += c
#         else:
#             result += i
#
#     return result
#
#
# class MyTest(unittest.TestCase):
#     def test(self):
#         self.assertEqual(to_encrypt("a b c", 3), "d e f")
#         self.assertEqual(to_encrypt("a b c", -3), "x y z")
#         self.assertEqual(to_encrypt("simple text", 16), "iycfbu junj")
#         self.assertEqual(to_encrypt("important text", 10), "swzybdkxd dohd")
#         self.assertEqual(to_encrypt("state secret", -13), "fgngr frperg")
#
#
# if __name__ == '__main__':
#     unittest.main()
"""28"""
def safe_pawns(pawns: set) -> int:
    res = 0

    for i in pawns:
        pos1: str = chr(ord(i[0])-1) + str(int(i[1]) - 1)
        pos2: str = chr(ord(i[0])+1) + str(int(i[1]) - 1)
        if pos1 in pawns or pos2 in pawns:
            res += 1

    return res


class MyTest(unittest.TestCase):
    def test(self):
        self.assertEqual(safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}), 6)
        self.assertEqual(safe_pawns({"b4", "c4", "d4", "e4", "f4", "g4", "e5"}), 1)


if __name__ == '__main__':
    unittest.main()





''
# class MyTest(unittest.TestCase):
#     def test(self):
#         self.assertEqual(safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}), 6)
#         self.assertEqual(safe_pawns({"b4", "c4", "d4", "e4", "f4", "g4", "e5"}), 1)
        # self.assertEqual(to_encrypt("simple text", 16), "iycfbu junj")
        # self.assertEqual(to_encrypt("important text", 10), "swzybdkxd dohd")
        # self.assertEqual(to_encrypt("state secret", -13), "fgngr frperg")
        #
        #
        # self.assertTrue(checkio('abe'))  # на булевое значение
        #
        # self.assertRaises(TypeError, checkio, 'kkkk', 8)  # на выброс исключения TypeError
        # self.assertGreater(checkio("Bananas, give me bananas!!!", {"banana", "bananas"}), 1)  # на больше чем (a > b)


# if __name__ == '__main__':
#     unittest.main()


"""
# --------------__*************************  TESTS  ***************************_-----------------

# pytest
def test():
    assert find_long_worlds(file) == ([1, 4, 5], ['hgjfur', 'andrey', 'sergey'])
    assert find_long_worlds(se) == ([16, 57, 69, 99], ['журналируемых', 'использовался', 'пользоваться.', 'операционной'])
    assert find_long_worlds('hello') == ([0], ['hello'])
    assert find_long_worlds('test') != ([1], ['hello'])



"""