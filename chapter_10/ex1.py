'''
Revise a previous program as follows: Read and parse the
“From” lines and pull out the addresses from the line. Count the num-
ber of messages from each person using a dictionary.

After all the data has been read, print the person with the most commits
by creating a list of (count, email) tuples from the dictionary. Then
sort the list in reverse order and print out the person who has the most
commits.

code below is mimicked from ../chapter_09/ex4.py
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
        email_addr = words[1]
        map[email_addr] = map.get(email_addr, 0) + 1

lst = list()

'''
if just use map insted of map.items(),
too many values to unpack error will occur.
cuz each default element in map data structure is key-value pairs instead
of a tuple
'''
for email, count in map.items():
    lst.append((count, email))

lst.sort(reverse=True)

print(lst[0][1], lst[0][0])
