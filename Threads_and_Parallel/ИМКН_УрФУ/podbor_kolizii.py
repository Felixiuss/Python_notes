
# Однопоточное исполнение
'''
from hashlib import md5
from itertools import product
from string import ascii_lowercase

def all_words(alphabet, length):
    return (''.join(letters) for letters in product(alphabet, repeat=length))

def is_collision(passwd, hash_value):
    return md5(passwd.encode('ascii')).hexdigest() == hash_value

def brute_force(hash_value, alphabet, length, begin=0, end=None):
    end = len(alphabet) if end is None else end
    for first_letter in alphabet[begin: end]:
        for word in all_words(alphabet, length - 1):
            passwd = first_letter + word
            if is_collision(passwd, hash_value):
                return passwd

print(brute_force('95ebc3c7b3b9f1d2c40fec14415d3cb8', ascii_lowercase, 5))
'''
# ------------------------------------------------------------------------------
'''
# Использование потоков

import threading
from hashlib import md5
from itertools import product, tee, islice
from string import ascii_lowercase

def all_words(alphabet, length):
    return (''.join(letters) for letters in product(alphabet, repeat=length))

def is_collision(passwd, hash_value):
    return md5(passwd.encode('ascii')).hexdigest() == hash_value

def brute_force(hash_value, alphabet, length, begin=0, end=None):
    end = len(alphabet) if end is None else end
    for first_letter in alphabet[begin: end]:
        for word in all_words(alphabet, length - 1):
            passwd = first_letter + word
            if is_collision(passwd, hash_value):
                print(passwd)
                return passwd

def pairs(iterable):
    items, nexts = tee(iterable, 2)
    nexts = islice(nexts, 1, None)
    return zip(items, nexts)

def parallel_brute_force(hash_value, alphabet, length):
    pool = []
    partition = [0, 13, 26]
    for p in pairs(partition):
        worker = threading.Thread(target=brute_force, args=(hash_value, alphabet, length, p[0], p[1]))
        worker.start()
        pool.append(worker)
    for worker in pool:
        worker.join()

print(brute_force('95ebc3c7b3b9f1d2c40fec14415d3cb8', ascii_lowercase, 5))
'''

# --------------------------------------------------------------------------------------------

# модуль multiprocessing
'''
import multiprocessing
from hashlib import md5
from itertools import product, tee, islice
from string import ascii_lowercase

def all_words(alphabet, length):
    return (''.join(letters) for letters in product(alphabet, repeat=length))

def is_collision(passwd, hash_value):
    return md5(passwd.encode('ascii')).hexdigest() == hash_value

def brute_force(hash_value, alphabet, length, begin=0, end=None):
    end = len(alphabet) if end is None else end
    for first_letter in alphabet[begin: end]:
        for word in all_words(alphabet, length - 1):
            passwd = first_letter + word
            if is_collision(passwd, hash_value):
                print(passwd)
                return passwd

def pairs(iterable):
    items, nexts = tee(iterable, 2)
    nexts = islice(nexts, 1, None)
    return zip(items, nexts)

def parallel_brute_force(hash_value, alphabet, length):
    pool = []
    partition = [0, 13, 26]
    for p in pairs(partition):
        worker = multiprocessing.Process(target=brute_force, args=(hash_value, alphabet, length, p[0], p[1]))
        worker.start()
        pool.append(worker)
    for worker in pool:
        worker.join()

print(brute_force('95ebc3c7b3b9f1d2c40fec14415d3cb8', ascii_lowercase, 5))
'''
# --------------------------------------------------------------------------------

# модуль concurrent.future

from concurrent.futures import ProcessPoolExecutor
from hashlib import md5
from itertools import product, tee, islice
from string import ascii_lowercase

def all_words(alphabet, length):
    return (''.join(letters) for letters in product(alphabet, repeat=length))

def is_collision(passwd, hash_value):
    return md5(passwd.encode('ascii')).hexdigest() == hash_value

def brute_force(hash_value, alphabet, length, begin=0, end=None):
    end = len(alphabet) if end is None else end
    for first_letter in alphabet[begin: end]:
        for word in all_words(alphabet, length - 1):
            passwd = first_letter + word
            if is_collision(passwd, hash_value):
                print(passwd)
                return passwd

def pairs(iterable):
    items, nexts = tee(iterable, 2)
    nexts = islice(nexts, 1, None)
    return zip(items, nexts)

def parallel_brute_force(hash_value, alphabet, length):
    futures = []
    with ProcessPoolExecutor(max_workers=2) as executor:
        partition = range(len(alphabet + 1))
        for p in pairs(partition):
            future = executor.submit(brute_force, hash_value, alphabet, length, p[0], p[1])
            future.append(future)
    results = [future.result() for future in futures]
    collisions = [r for r in results if r is not None]
    if collisions:
        return collisions[0]

print(brute_force('95ebc3c7b3b9f1d2c40fec14415d3cb8', ascii_lowercase, 5))
