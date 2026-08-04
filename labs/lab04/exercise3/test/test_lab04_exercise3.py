hours = float(input())
if hours > 2:
    if hours > 5:
        parkingFee = 3 * 2 + hours - 2 - 3 * 3
    else:
        parkingFee = hours - 2 * 2
    if parkingFee > 30:
        parkingFee = 30
else:
    parkingFee = 0
print(parkingFee)
