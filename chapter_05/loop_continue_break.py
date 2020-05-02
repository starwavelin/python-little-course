while True:
    line = input('< ')
    if line.startswith('#'):
        continue
    elif line == 'done':
        break
    print(line)
print('Done!')
