fname = input('Enter your file name:')
try:
    finput = open(fname)
except:
    print(fname, 'cannot be found!')
    exit()

for line in finput:
    print(line.upper())
