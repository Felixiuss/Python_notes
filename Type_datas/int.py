# Функция поиска минимума

def mins(*args):
    res, *rest = args
    for i in rest:
        res = i if i < res else res
    return res



lst = [3, 4, 5, 1]
print(mins(*lst))
