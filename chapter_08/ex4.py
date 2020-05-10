# In this exercise, two words with different cases are considered different.
# ie. "it" and "It" are considered different

fname = input('Please enter your file name (romeo.txt):')
try:
    finput = open(fname)
except FileNotFoundError:
    print(fname, 'cannot be found!')
    exit()


def add_words_to_list(file):
    t = list()
    for line in file:
        line = line.rstrip()
        if len(line) == 0:
            continue
        words = line.split()
        for w in words:
            if (not(w in t)):
                t.append(w)
    t.sort()
    return t


print(add_words_to_list(finput))
