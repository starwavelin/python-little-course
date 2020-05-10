fname = input('Enter your file name: (../files/FILE_NAME.txt)')
try:
    finput = open(fname)
except FileNotFoundError:
    print(fname, 'cannot be found!')
    exit()

for line in finput:
    print(line.upper())
