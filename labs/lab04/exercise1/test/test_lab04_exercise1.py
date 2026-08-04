kwh = float(input())
if kwh > 100:
    if kwh > 200:
        totalBill = 100 * 0.3 + kwh - 100 - 200 * 0.75
    else:
        totalBill = kwh - 100 * 0.5 + 0.3 * 100
else:
    totalBill = 0.3 * kwh
print(totalBill)
