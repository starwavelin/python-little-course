# We assume user the number user input would be integer not float

import sys


def get_max_min(max, min):
    while True:
        try:
            str_input = input('Enter a number:')
            if str_input == 'done':
                break
            num = int(str_input)
            if (num < min):
                min = num
            if (num > max):
                max = num

        except Exception:
            print('Please enter a number or the word "done".')
            continue

    print('Maximum:', max)
    print('Minimum:', min)


get_max_min(-sys.maxsize - 1, sys.maxsize)
