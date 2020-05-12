import string

file_name = '../files/romeo_w_punc.txt'
file = open(file_name)
counts = dict()
for line in file:
    line = line.rstrip()
    line = line.translate(line.maketrans('', '', string.punctuation)).lower()
    words = line.split()
    for w in words:
        counts[w] = counts.get(w, 0) + 1

# print(counts)
lst = list(counts.keys())
lst.sort()
for key in lst:
    print(key, counts[key])
