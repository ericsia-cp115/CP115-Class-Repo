# Problem: This adds ALL numbers including 3
total = 0

for number in range(5):
    print(f'Processing: {number}')
    total += number
    print(f'Added to total. Current total: {total}')

print(f'Final total: {total}')