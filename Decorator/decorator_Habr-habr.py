# -*- coding: utf-8 -*-

# def makebold(fn):
#     def wrapped():
#         return "<b>" + fn() + "</b>"
#
#     return wrapped
#
#
# def makeitalic(fn):
#     def wrapped():
#         return "<i>" + fn() + "</i>"
#
#     return wrapped
#
#
# @makebold
# @makeitalic
# def hello():
#     return "hello habr"
#
#
# print hello()  ## выведет <b><i>hello habr</i></b>

# # ---------------------------------------------------

# def shout(word="да"):
#     return word.capitalize() + "!"
#
#
# print shout()
# # выведет: 'Да!'
#
# # Так как функция - это объект, вы связать её с переменнной,
# # как и любой другой объект
# scream = shout
#
# # Заметьте, что мы не используем скобок: мы НЕ вызываем функцию "shout",
# # мы связываем её с переменной "scream". Это означает, что теперь мы
# # можем вызывать "shout" через "scream":
#
# print scream()
# # выведет: 'Да!'
#
# # Более того, это значит, что мы можем удалить "shout", и функция всё ещё
# # будет доступна через переменную "scream"
#
# del shout
# try:
#     print shout()
# except NameError, e:
#     print e
#     # выведет: "name 'shout' is not defined"
#
# print scream()

# выведет: 'Да!'

# # /----------------------------------------------------

# def talk():
#     # Внутри определения функции "talk" мы можем определить другую...
#     def whisper(word="да"):
#         return word.lower() + "...";
#
#     # ... и сразу же её использовать!
#     print whisper()
#
#
# # Теперь, КАЖДЫЙ РАЗ при вызове "talk", внутри неё определяется а затем
# # и вызывается функция "whisper".
# talk()
# # выведет: "да..."
#
# # Но вне функции "talk" НЕ существует никакой функции "whisper":
# try:
#     print whisper()
# except NameError, e:
#     print e
#     # выведет : "name 'whisper' is not defined"

# ----------------------------------------------------

# def getTalk(type="shout"):
#     # Мы определяем функции прямо здесь
#     def shout(word="да"):
#         return word.capitalize() + "!"
#
#     def whisper(word="да"):
#         return word.lower() + "..."
#
#     # Затем возвращаем необходимую
#     if type == "shout":
#         # Заметьте, что мы НЕ используем "()", нам нужно не вызвать функцию,
#         # а вернуть объект функции
#         return shout
#     else:
#         return whisper
#
#
# # Как использовать это непонятное нечто?
# # Возьмём функцию и свяжем её с переменной
# talk = getTalk()
#
# # Как мы можем видеть, "talk" теперь - объект "function":
# print talk
# # выведет: <function shout at 0xb7ea817c>
#
# # Который можно вызывать, как и функцию, определённую "обычным образом":
# print talk()
#
# # Если нам захочется - можно вызвать её напрямую из возвращаемого значения:
# print getTalk("whisper")()

# ------------------------------------------------------------------------------

# def shout(word="да"):
#     return word.capitalize() + "!"
#
#
# scream = shout
#
#
# def doSomethingBefore(func):
#     print "Я делаю что-то ещё, перед тем как вызвать функцию, которую ты мне передал"
#     print func()
#
#
# doSomethingBefore(scream)
# # выведет:
# # Я делаю что-то ещё, перед тем как вызвать функцию, которую ты мне передал
# # Да!

# ---------------------------------------------------------------------------------

# # Декоратор - это функция, ожидающая ДРУГУЮ функцию в качестве параметра
# def my_shiny_new_decorator(a_function_to_decorate):
#     # Внутри себя декоратор определяет функцию-"обёртку".
#     # Она будет (что бы вы думали?..) обёрнута вокруг декорируемой,
#     # получая возможность исполнять произвольный код до и после неё.
#
#     def the_wrapper_around_the_original_function():
#         # Поместим здесь код, который мы хотим запускать ДО вызова
#         # оригинальной функции
#         print "Я - код, который отработает до вызова функции"
#
#         # ВЫЗОВЕМ саму декорируемую функцию
#         a_function_to_decorate()
#
#         # А здесь поместим код, который мы хотим запускать ПОСЛЕ вызова
#         # оригинальной функции
#         print "А я - код, срабатывающий после"
#
#     # На данный момент функция "a_function_to_decorate" НЕ ВЫЗЫВАЛАСЬ НИ РАЗУ
#
#     # Теперь, вернём функцию-обёртку, которая содержит в себе
#     # декорируемую функцию, и код, который необходимо выполнить до и после.
#     # Всё просто!
#     return the_wrapper_around_the_original_function
#
#
# # Представим теперь, что у нас есть функция, которую мы не планируем больше трогать.
# def a_stand_alone_function():
#     print "Я простая одинокая функция, ты ведь не посмеешь меня изменять?.."
#
#
# a_stand_alone_function()
# # выведет: Я простая одинокая функция, ты ведь не посмеешь меня изменять?..
#
# # Однако, чтобы изменить её поведение, мы можем декорировать её, то есть
# # Просто передать декоратору, который обернет исходную функцию в любой код,
# # который нам потребуется, и вернёт новую, готовую к использованию функцию:
#
# a_stand_alone_function_decorated = my_shiny_new_decorator(a_stand_alone_function)
# a_stand_alone_function_decorated()
# # выведет:
# # Я - код, который отработает до вызова функции
# # Я простая одинокая функция, ты ведь не посмеешь меня изменять?..
# # А я - код, срабатывающий после
#
# # Наверное, теперь мы бы хотели, чтобы каждый раз, во время вызова a_stand_alone_function, вместо неё вызывалась
# # a_stand_alone_function_decorated. Нет ничего проще, просто перезапишем a_stand_alone_function функцией, которую
# # нам вернул my_shiny_new_decorator:
#
# a_stand_alone_function = my_shiny_new_decorator(a_stand_alone_function)
# a_stand_alone_function()
# #выведет:
# # Я - код, который отработает до вызова функции
# # Я простая одинокая функция, ты ведь не посмеешь меня изменять?..
# # А я - код, срабатывающий после
#
# @my_shiny_new_decorator
# def another_stand_alone_function():
#     print "Оставь меня в покое"
#
#
# another_stand_alone_function()
# # выведет:
# # Я - код, который отработает до вызова функции
# # Оставь меня в покое
# # А я - код, срабатывающий после

# -------------------------------------------------------------------------

# Конечно, можно вкладывать декораторы друг в друга, например так:


# def bread(func):
#     def wrapper():
#         print "</------\>"
#         func()
#         print "<\______/>"
#
#     return wrapper
#
#
# def ingredients(func):
#     def wrapper():
#         print "#помидоры#"
#         func()
#         print "~салат~"
#
#     return wrapper
#
#
# def sandwich(food="--ветчина--"):
#     print food
#
#
# sandwich()
# # выведет: --ветчина--
# sandwich = bread(ingredients(sandwich))
# sandwich()
# # выведет:
# # </------\>
# # #помидоры#
# # --ветчина--
# # ~салат~
# # <\______/>
#
#
# # И используя синтаксис декораторов:
#
# @bread
# @ingredients
# def sandwich(food="--ветчина--"):
#     print food
#
#
# sandwich()
# # выведет:
# # </------\>
# # #помидоры#
# # --ветчина--
# # ~салат~
# # <\______/>
#
#
# # Следует помнить о том, что порядок декорирования ВАЖЕН:
#
#
# @ingredients
# @bread
# def sandwich(food="--ветчина--"):
#     print food
#
#
# sandwich()
# # выведет:
# # #помидоры#
# # </------\>
# # --ветчина--
# # <\______/>
# # ~салат~


# -------------------------------------------------------------------------------------------------------------------
#                                  Вторая часть
# -------------------------------------------------------------------------------------------------------------------


# # Передача («проброс») аргументов в декорируемую функцию
#
# def a_decorator_passing_arguments(function_to_decorate):
#     def a_wrapper_accepting_arguments(arg1, arg2):  # аргументы прибывают отсюда
#         print "Смотри, что я получил:", arg1, arg2
#         function_to_decorate(arg1, arg2)
#
#     return a_wrapper_accepting_arguments
#
#
# # Теперь, когда мы вызываем функцию, которую возвращает декоратор,
# # мы вызываем её "обёртку", передаём ей аргументы и уже в свою очередь
# # она передаёт их декорируемой функции
#
# @a_decorator_passing_arguments
# def print_full_name(first_name, last_name):
#     print "Меня зовут", first_name, last_name
#
#
# print_full_name("Питер", "Венкман")
# # выведет:
# # Смотри, что я получил: Питер Венкман
# # Меня зовут Питер Венкман

# --------------------------------------------------------------------------------------

# def method_friendly_decorator(method_to_decorate):
#     def wrapper(self, lie):
#         lie = lie - 3  # действительно, дружелюбно - снизим возраст ещё сильней :-)
#         return method_to_decorate(self, lie)
#
#     return wrapper
#
#
# class Lucy(object):
#
#     def __init__(self):
#         self.age = 32
#
#     @method_friendly_decorator
#     def sayYourAge(self, lie):
#         print "Мне {}, а ты бы сколько дал?".format(self.age + lie)
#
#
# l = Lucy()
# l.sayYourAge(10)
# # выведет: Мне 39, а ты бы сколько дал?

# ----------------------------------------------------------------------------------------

# def a_decorator_passing_arbitrary_arguments(function_to_decorate):
#     # Данная "обёртка" принимает любые аргументы
#     def a_wrapper_accepting_arbitrary_arguments(*args, **kwargs):
#         print "Передали ли мне что-нибудь?:"
#         print args
#         print kwargs
#         # Теперь мы распакуем *args и **kwargs
#         # Если вы не слишком хорошо знакомы с распаковкой, можете прочесть следующую статью:
#         # http://www.saltycrane.com/blog/2008/01/how-to-use-args-and-kwargs-in-python/
#         function_to_decorate(*args, **kwargs)
#
#     return a_wrapper_accepting_arbitrary_arguments
#
#
# @a_decorator_passing_arbitrary_arguments
# def function_with_no_argument():
#     print "Python is cool, no argument here."  # оставлено без перевода, хорошая игра слов:)
#
#
# function_with_no_argument()
#
#
# # выведет:
# # Передали ли мне что-нибудь?:
# # ()
# # {}
# # Python is cool, no argument here.
#
# @a_decorator_passing_arbitrary_arguments
# def function_with_arguments(a, b, c):
#     print a, b, c
#
#
# function_with_arguments(1, 2, 3)
#
#
# # выведет:
# # Передали ли мне что-нибудь?:
# # (1, 2, 3)
# # {}
# # 1 2 3
#
# @a_decorator_passing_arbitrary_arguments
# def function_with_named_arguments(a, b, c, platypus="Почему нет?"):
#     print "Любят ли %s, %s и %s утконосов? %s" % \
#           (a, b, c, platypus)
#
#
# function_with_named_arguments("Билл", "Линус", "Стив", platypus="Определенно!")
#
#
# # выведет:
# # Передали ли мне что-нибудь?:
# # ('Билл', 'Линус', 'Стив')
# # {'platypus': 'Определенно!'}
# # Любят ли Билл, Линус и Стив утконосов? Определенно!
#
# class Mary(object):
#
#     def __init__(self):
#         self.age = 31
#
#     @a_decorator_passing_arbitrary_arguments
#     def sayYourAge(self, lie=-3):  # Теперь мы можем указать значение по умолчанию
#         print "Мне %s, а ты бы сколько дал?" % (self.age + lie)
#
#
# m = Mary()
# m.sayYourAge()
# # выведет:
# # Передали ли мне что-нибудь?:
# # (<__main__ .Mary object at 0xb7d303ac>,)
# # {}
# # Мне 28, а ты бы сколько дал?

# ----------------------------------------------------------------------------------------------

# # Декораторы - это просто функции
# def my_decorator(func):
#     print "Я обычная функция"
#
#     def wrapper():
#         print "Я - функция, возвращаемая декоратором"
#         func()
#
#     return wrapper
#
#
# # Так что, мы можем вызывать её, не используя "@"-синтаксис:
#
# def lazy_function():
#     print "zzzzzzzz"
#
#
# decorated_function = my_decorator(lazy_function)
#
#
# # выведет: Я обычная функция
#
# # Данный код выводит "Я обычная функция", потому что это ровно то, что мы сделали:
# # вызвали функцию. Ничего сверхъестественного
#
# @my_decorator
# def lazy_function():
#     print "zzzzzzzz"
#
# # выведет: Я обычная функция

# -------------------------------------------------------------------------------------------------

# def decorator_maker_with_arguments(decorator_arg1, decorator_arg2):
#     print "Я создаю декораторы! И я получил следующие аргументы:", decorator_arg1, decorator_arg2
#
#     def my_decorator(func):
#         print "Я - декоратор. И ты всё же смог передать мне эти аргументы:", decorator_arg1, decorator_arg2
#
#         # Не перепутайте аргументы декораторов с аргументами функций!
#         def wrapped(function_arg1, function_arg2):
#             print ("Я - обёртка вокруг декорируемой функции.\n"
#                    "И я имею доступ ко всем аргументам: \n"
#                    "\t- и декоратора: {0} {1}\n"
#                    "\t- и функции: {2} {3}\n"
#                    "Теперь я могу передать нужные аргументы дальше"
#                    .format(decorator_arg1, decorator_arg2,
#                            function_arg1, function_arg2))
#             return func(function_arg1, function_arg2)
#
#         return wrapped
#
#     return my_decorator
#
#
# @decorator_maker_with_arguments("Леонард", "Шелдон")
# def decorated_function_with_arguments(function_arg1, function_arg2):
#     print ("Я - декорируемая функция и я знаю только о своих аргументах: {0}"
#            " {1}".format(function_arg1, function_arg2))
#
#
# decorated_function_with_arguments("Раджеш", "Говард")

# ----------------------------------------------------------------------------------------------------

# def decorator_with_args(decorator_to_enhance):
#     """
#     Эта функция задумывается КАК декоратор и ДЛЯ декораторов.
#     Она должна декорировать другую функцию, которая должна быть декоратором.
#     Лучше выпейте чашку кофе.
#     Она даёт возможность любому декоратору принимать произвольные аргументы,
#     избавляя Вас от головной боли о том, как же это делается, каждый раз, когда этот функционал необходим.
#     """
#
#     # Мы используем тот же трюк, который мы использовали для передачи аргументов:
#     def decorator_maker(*args, **kwargs):
#         # создадим на лету декоратор, который принимает как аргумент только
#         # функцию, но сохраняет все аргументы, переданные своему "создателю"
#         def decorator_wrapper(func):
#             # Мы возвращаем то, что вернёт нам изначальный декоратор, который, в свою очередь
#             # ПРОСТО ФУНКЦИЯ (возвращающая функцию).
#             # Единственная ловушка в том, что этот декоратор должен быть именно такого
#             # decorator(func, *args, **kwargs)
#             # вида, иначе ничего не сработает
#             return decorator_to_enhance(func, *args, **kwargs)
#
#         return decorator_wrapper
#
#     return decorator_maker
#
#
# # Мы создаём функцию, которую будем использовать как декоратор и декорируем её :-)
# # Не стоит забывать, что она должна иметь вид "decorator(func, *args, **kwargs)"
# @decorator_with_args
# def decorated_decorator(func, *args, **kwargs):
#     def wrapper(function_arg1, function_arg2):
#         print "Мне тут передали...:", args, kwargs
#         return func(function_arg1, function_arg2)
#
#     return wrapper
#
#
# # Теперь декорируем любую нужную функцию нашим новеньким, ещё блестящим декоратором:
#
# @decorated_decorator(42, 404, 1024)
# def decorated_function(function_arg1, function_arg2):
#     print "Привет", function_arg1, function_arg2
#
#
# decorated_function("Вселенная и", "всё прочее")
# # выведет:
# # Мне тут передали...: (42, 404, 1024) {}
# # Привет Вселенная и всё прочее

# ----------------------------------------------------------------------------------------------------

# def decorator_with_args(decorator_to_enhance):
#     """
#     Эта функция задумывается КАК декоратор и ДЛЯ декораторов.
#     Она должна декорировать другую функцию, которая должна быть декоратором.
#     Лучше выпейте чашку кофе.
#     Она даёт возможность любому декоратору принимать произвольные аргументы,
#     избавляя Вас от головной боли о том, как же это делается, каждый раз, когда этот функционал необходим.
#     """
#
#     def decorator_maker(*args, **kwargs):
#
#         def decorator_wrapper(func):
#             return decorator_to_enhance(func, *args, **kwargs)
#
#         return decorator_wrapper
#
#     return decorator_maker
#
#
# @decorator_with_args
# def decorated_decorator(func, *args, **kwargs):
#     def wrapper(*args, **kwargs):
#         print "Мне тут передали...:", args, kwargs
#         return func(*args, **kwargs)
#
#     return wrapper
#
#
# @decorated_decorator(42, 404, 1024)
# def decorated_function(*args, **kwargs):
#     print "Привет"
#     print '*args : ', args
#     print '**kwargs : ', kwargs
#
#
# decorated_function("hello", "Roman", papa='tolya', vika=3, rock='petya')
# print(decorator_with_args.__doc__)

# -----------------------------------------------------------------------------------------------------------

# def benchmark(func):
#     """
#     Декоратор, выводящий время, которое заняло
#     выполнение декорируемой функции.
#     """
#     import time
#     def wrapper(*args, **kwargs):
#         t = time.clock()
#         res = func(*args, **kwargs)
#         print func.__name__, time.clock() - t
#         return res
#
#     return wrapper
#
#
# def logging(func):
#     """
#     Декоратор, логирующий работу кода.
#     (хорошо, он просто выводит вызовы, но тут могло быть и логирование!)
#     """
#
#     def wrapper(*args, **kwargs):
#         res = func(*args, **kwargs)
#         print func.__name__, args, kwargs
#         return res
#
#     return wrapper
#
#
# def counter(func):
#     """
#     Декоратор, считающий и выводящий количество вызовов
#     декорируемой функции.
#     """
#
#     def wrapper(*args, **kwargs):
#         wrapper.count += 1
#         res = func(*args, **kwargs)
#         print "{0} была вызвана: {1}x".format(func.__name__, wrapper.count)
#         return res
#
#     wrapper.count = 0
#     return wrapper
#
#
# @benchmark
# @logging
# @counter
# def reverse_string(string):
#     return str(reversed(string))
#
#
# print reverse_string("hello world my name is Roman")
# print reverse_string(
#     "A man, a plan, a canoe, pasta, heros, rajahs, a coloratura, maps, snipe, percale, macaroni, a gag, a banana bag,"
#     " a tan, a tag, a banana bag again (or a camel), a crepe, pins, Spam, a rut, a Rolo, cash, a jar, sore hats,"
#     " a peon, a canal: Panama!")
