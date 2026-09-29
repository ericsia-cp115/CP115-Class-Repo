speed = int(input())

total_readings=0
streak = 0

while speed >= 0:
    total_readings +=1

    if speed <20:
        streak +=1
        streak1 = streak

        speed = int(input())

        if speed >=0 and speed <20:
            total_readings +=1
            streak +=1

        else:
            streak = 0

            if streak1 > streak:
                longest_streak = streak1
            else:
                longest_streak = streak

    else:
        streak = 0

speed = int(input())

print(total_readings)
print(longest_streak)
