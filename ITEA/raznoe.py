a = 1
b = 2
a, b = b, a+b

print(a)
print(b)


print(dir(object), sep='')

# --------------------------------------------------------

from random import randrange

loops = (randrange(2, 5) for x in range(randrange(3, 7)))

print(list(loops))
