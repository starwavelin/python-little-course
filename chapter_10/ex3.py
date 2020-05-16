'''
Write a program that reads a file and prints the letters
in decreasing order of frequency. Your program should convert all the
input to lower case and only count the letters a-z. Your program should
not count spaces, digits, punctuation, or anything other than the letters
a-z. Find text samples from several different languages and see how
letter frequency varies between languages. Compare your results with
the tables at https://wikipedia.org/wiki/Letter_frequencies.
'''
import string

file_name = input('Enter a text file name:')  # ie. '../files/mbox.txt'
try:
    file = open(file_name)
except FileNotFoundError:
    print(file_name, 'does not exist!')
    exit()

map = dict()
total_chars = 0
for line in file:
    line = line.strip()
    # remove punctuations
    line = line.translate(line.maketrans('', '', string.punctuation))
    # remove digits
    line = line.translate(line.maketrans('', '', string.digits))
    # remove spaces
    line = line.translate(line.maketrans('', '', string.whitespace))
    line = line.lower()
    total_chars += len(line)
    for char in line:
        map[char] = map.get(char, 0) + 1

lst = list()
for char, freq in map.items():
    lst.append((freq, char))

lst.sort(reverse=True)

for item in lst:
    print(item[1], item[0], format(item[0] / total_chars, '%'))
