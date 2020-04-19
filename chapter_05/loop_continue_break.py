while True:
    line = input('< ')
    if line[0] == '#':
        continue
    elif line == 'done':
        break
    print(line)
print('Done!')
