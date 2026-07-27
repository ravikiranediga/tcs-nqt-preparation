# Find the Power of a Number in Python Language
num,power=int(input("Enter a Number:")),int(input("Enter the Power:"))
result=1
for i in range(power):
    result=result*num
print("The result of",num,"raised to the power of",power,"is:",result)


# using in-built pow() function
num,power=int(input("Enter a Number:")),int(input("Enter the Power:"))
result=pow(num,power)
print("The result of",num,"raised to the power of",power,"is:",result)