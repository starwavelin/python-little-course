word = 'brontosaurus'
map = dict()
# for c in word:
#     if c not in map:
#         map[c] = 1
#     else:
#         map[c] += 1
# print(map)

for c in word:
    map[c] = map.get(c, 0) + 1
print(map)
# {'b': 1, 'r': 2, 'o': 2, 'n': 1, 't': 1, 's': 2, 'a': 1, 'u': 2}
