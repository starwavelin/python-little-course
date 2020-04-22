def count_letter(str, letter):
    if str is None:
        return 0
    return str.count(letter)

print(count_letter('', 'a'))

print(count_letter(None, 'a'))

print(count_letter('apple', 'a'))

print(count_letter('activity', 't'))
