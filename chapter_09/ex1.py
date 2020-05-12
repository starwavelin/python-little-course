file_name = '../files/words.txt'
file = open(file_name)
map = dict()
for line in file:
    line = line.rstrip()
    if len(line) == 0:
        continue
    words = line.split()
    for w in words:
        map[w] = 'haha'
# print(map)
print('we' in map)  # True
print('We' in map)  # True
print('\em' in map)  # False
print('{\em' in map)  # True
