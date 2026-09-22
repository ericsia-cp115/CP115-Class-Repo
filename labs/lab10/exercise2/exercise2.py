num_days = int(input())
danger_threshold = float(input())

danger_days= 0
average_temp = 0

for i in range (num_days):
    temperature = float(input("Enter temperature:"))

    if temperature > danger_threshold:
        above_threshold = danger_days + 1

    average_temp += temperature

print(danger_days)
print(f"{average_temp:.1f}")
