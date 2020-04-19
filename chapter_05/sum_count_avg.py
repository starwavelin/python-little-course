def sum_count_average():
    sum = 0.0
    count = 0
    inp = None
    while inp != 'done':
        inp = input('Enter a number: ')
        try:
            num = float(inp)
            sum = sum + num
            count = count + 1
        except:
            print('Invalid input')
    return str(sum) + ' ' + str(count) + ' ' + str(sum / count)

print(sum_count_average())
