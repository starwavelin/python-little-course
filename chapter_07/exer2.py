fname = input('Please enter your file name:') # ie. mbox-short.txt
try:
    finput = open(fname)
except:
    print(fname, 'cannot be found!')
    exit()

spam_conf = 0.0
count = 0
for line in finput:
    if line.startswith('X-DSPAM-Confidence:'):
        spam_conf += float(line.split(':')[1])
        count += 1

avg = spam_conf / count
print('Average spam confidence:', avg)


# Solution 2
fname = input("Enter file name: ")
try:
    fh = open(fname)
except:
    print(fname, 'cannot be found!')
    exit()

spam_conf = 0.0
count = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    spam_conf += float(line[line.find(':') + 1 :].strip())
    count += 1
print("Average spam confidence:", spam_conf / count)
