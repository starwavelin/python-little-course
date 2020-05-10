filename = input('Please enter your file name:')  # ie. ../files/mbox-short.txt
try:
    fhand = open(filename)
except Exception:
    print('File name not found!')
    exit()

count = 0
for line in fhand:
    line = line.rstrip()
    if line.startswith('Subject:'):
        count = count + 1
print('There were', count, 'subject lines in', filename)
