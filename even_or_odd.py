num=int(input("Enter a Number:"))
if num%2==0:
    print("EVen")
else:
    print("Odd")


# Using Recursion 
def recursum(sum,num1,num2):
    if num1>num2:
        return sum
    return num1 +recursum(sum,num+1,num2)
num1,num2=3,6
print(recursum(sum,num1,num2))
