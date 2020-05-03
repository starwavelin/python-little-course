filename = input('Please enter your file name:') # ie. mbox-short.txt
try:
    fhand = open(filename)
except:
    print('File name not found!')
    exit()

count = 0
for line in fhand:
    line = line.rstrip()
    # skip the lines that we're not interested in
    if not line.startswith('From:'):
        continue
    # print out interesting lines
    print(line)
