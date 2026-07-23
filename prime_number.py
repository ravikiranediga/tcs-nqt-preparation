# Check Whether a Number is a Prime or Not
num = 15

if num < 2:
    print("Not Prime")
else:
    for i in range(2, num):
        if num % i == 0:
            print("Not Prime")
            break
    else:
        print("Prime")