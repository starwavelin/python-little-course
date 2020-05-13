'''
This program is a proof of concept of Decorate, Sort and Undecorate (DSU)
pattern.

Decorate: Create a sequence by building a list of tuples with one or
    more sort keys Preceding the elements from the sequence.
Sort: Sort the list of tuples using the python built-in sort() function.
Undecorate: extract the sorted elements of the sequence.
'''

txt = 'but soft what light in yonder window breaks'
words = txt.split()
lis = list()
for w in words:
    lis.append((len(w), w))  # Decorate
# print(lis)

lis.sort(reverse=True)  # Sort

res = list()
for length, w in lis:
    res.append(w)  # Undecorate

print(res)
