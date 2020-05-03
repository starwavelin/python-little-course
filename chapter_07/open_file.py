filename = input('Please enter your file name:')
try:
    fhand = open(filename)
except:
    print('File', filename, 'is not found!')
    
count = 0
for line in fhand:
    count = count + 1
print('Line Count:', count)
