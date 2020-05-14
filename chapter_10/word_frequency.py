import string

file_path = '../files/romeo-full.txt'
file = open(file_path)
map = dict()
for line in file:
    line = line.rstrip()
    line = line.translate(line.maketrans('', '', string.punctuation)).lower()
    words = line.split()
    for w in words:
        map[w] = map.get(w, 0) + 1

t = list()
for word, freq in list(map.items()):
    t.append((freq, word))

t.sort(reverse=True)

# print the first 15 words with their frequencies
for freq, word in t[:15]:
    print(word, freq)
