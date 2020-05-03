fname = input('Please enter your file name:')
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
