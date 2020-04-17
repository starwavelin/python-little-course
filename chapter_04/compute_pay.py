def computepay(hour, rate):
    if hour <= 40:
        return rate * hour
    else:
        return rate * 40 + rate * 1.5 * (hour - 40)

hrs = float(input("Enter Hours:"))
rate = float(input("Enter Hours:"))
p = computepay(hrs, rate)
print("Pay", p)
