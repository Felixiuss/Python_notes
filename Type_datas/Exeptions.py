import itertools

print(itertools.__name__)
print(itertools.__doc__)
print(dir(itertools))
print(itertools.__spec__)
print(itertools.__package__)
print(itertools.__loader__)

for i in dir(itertools):
    if i.startswith('__'):
        print(i)

# help(itertools)

res = [1, 2, 3, 4, 4, 5, 6, 6, 77, 88]

x = list(itertools.accumulate(res))
print(x[-1])

print(globals())