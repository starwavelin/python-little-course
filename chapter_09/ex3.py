file_name = '../files/mbox-short.txt'
file = open(file_name)
map = dict()
for line in file:
    line = line.rstrip()
    if line.startswith('From '):
        words = line.split()
        email_addr = words[1]
        map[email_addr] = map.get(email_addr, 0) + 1

print(map)
