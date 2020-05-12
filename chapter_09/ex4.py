file_name = input('Enter a text file name:')  # ie. '../files/mbox-short.txt'
try:
    file = open(file_name)
except FileNotFoundError:
    print(file_name, 'does not exist!')
    exit()

max_value = None
max_email = None
map = dict()
for line in file:
    line = line.rstrip()
    if line.startswith('From '):
        words = line.split()
        email_addr = words[1]
        map[email_addr] = map.get(email_addr, 0) + 1
        if max_value is None or map[email_addr] > max_value:
            max_value = map[email_addr]
            max_email = email_addr

print(max_email, max_value)
