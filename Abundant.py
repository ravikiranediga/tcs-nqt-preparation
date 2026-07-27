# Check Whether or Not the Number is an Abundant Number in Python

num=18
sum=1
for i in range(2,num):
    if num%i==0:
        sum+=i
if sum>num:
    print(f"{num} is an Abundant number.")
else:
    print(f"{num} is not an Abundant number.")