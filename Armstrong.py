# Check Whether a Given Number is an Armstrong Number or Not
num=int(input("Enter a Number:"))
sum=0

length=len(str(num))
for i in range(length):
    digit=num%10
    sum+=digit**length
    num=num//10
if sum==num:
    print("The number is an Armstrong number:",sum)
else:
    print("The number is not an Armstrong number:",sum)


# Find the Armstrong Numbers in a given Range in Python
low, high = 10, 1000

for n in range(low, high + 1):

    # order of number
    order = len(str(n))

    # initialize sum
    sum = 0

    temp = n
    while temp > 0:
        digit = temp % 10
        sum += digit ** order
        temp //= 10

    if n == sum:
        print(n, end=", ")

