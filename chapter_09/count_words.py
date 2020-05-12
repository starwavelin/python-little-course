file_name = '../files/romeo.txt'
file = open(file_name)
counts = dict()
for line in file:
    line = line.rstrip()
    words = line.split()
    for w in words:
        counts[w] = counts.get(w, 0) + 1

# print(counts)
lst = list(counts.keys())
lst.sort()
for key in lst:
    print(key, counts[key])
