d = {'a': 10, 'b': 1, 'c': 22, 'd': 17}
t = list()
for key, val in d.items():
    t.append((val, key))
print(t)
t.sort(reverse=True)
print(t)
