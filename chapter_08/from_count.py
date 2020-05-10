fname = input('Please enter your file name (../files/mbox-short.txt):')
try:
    finput = open(fname)
except FileNotFoundError:
    print(fname, 'cannot be found!')
    exit()


def print_from_list(file):
    count = 0
    for line in file:
        line = line.rstrip()
        if len(line) == 0 or not line.startswith('From '):
            continue
        words = line.split()
        print(words[1])
        count += 1
    print('There were', count, 'lines in the file with From as the first word')


print_from_list(finput)
