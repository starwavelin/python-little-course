hours = float(input('Enter Hours:'))
rate = float(input('Enter Rate:'))
if hours <= 40:
    print(rate * hours)
else:
    print(rate * 40 + rate * 1.5 * (hours - 40))
