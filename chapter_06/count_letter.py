def count_letter(str, letter):
    if str is None or str == '':
        return 0
    count = 0
    for char in str:
        if char == letter:
            count = count + 1
    return count

print(count_letter('', 'a'))

print(count_letter(None, 'a'))

print(count_letter('apple', 'a'))

print(count_letter('activity', 't'))
