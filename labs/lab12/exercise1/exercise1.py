correct_password = "python123"

attempts_used =0

for attempts in range(3):
    password =input("Enter password:")

    attempts_used +=1

    if password == correct_password:
        login_successful = True
        break
    else:
        login_successful = False


print(login_successful)
print(attempts_used)
