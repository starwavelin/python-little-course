'''
This program counts the distribution of the hour of the day
for each of the messages. You can pull the hour from the “From” line
by finding the time string and then splitting that string into parts using
the colon character. Once you have accumulated the counts for each
hour, print out the counts, one per line, sorted by hour as shown below.
'''

file_name = input('Enter a text file name:')  # ie. '../files/mbox.txt'
try:
    file = open(file_name)
except FileNotFoundError:
    print(file_name, 'does not exist!')
    exit()

map = dict()
for line in file:
    line = line.rstrip()
    if line.startswith('From '):
        words = line.split()
        time = words[5]
        hour = time.split(':')[0]
        # print('hour is:', hour)
        map[hour] = map.get(hour, 0) + 1

lst = list()

for hour, freq in map.items():
    lst.append((hour, freq))

lst.sort()

for item in lst:
    print(item[0], item[1])
