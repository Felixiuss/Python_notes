def unique(iterable, seen=None):
    seen = set(seen or [])
    for item in iterable:
        if item not in seen:
            seen.add(item)
            yield item


xs = [1, 1, 2, 3]
print(unique(xs))
print(list(unique(xs)))
print(1 in unique(xs))

print(list(set(xs)))
res = []
t = [res.append(i) for i in xs if i not in res]
print(res)
