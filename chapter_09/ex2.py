file_name = '../files/mbox-short.txt'
file = open(file_name)
map = dict()
for line in file:
    line = line.rstrip()
    if line.startswith('From '):
        words = line.split()
        day_of_week = words[2]
        map[day_of_week] = map.get(day_of_week, 0) + 1

print(map)
