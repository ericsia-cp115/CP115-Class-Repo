income = float(input())
if income > 50000:
    if income > 100000:
        totalTax = income - 100000 * 2 / 100 + income - 50000 - 100000 * 1 / 100
    else:
        totalTax = income - 50000 * 1 / 100
else:
    totalTax = 0
print(totalTax)
