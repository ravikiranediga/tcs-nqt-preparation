# Find the Greatest of the Three Numbers​ in Python
# Using Loops
num1, num2, num3 = 10, 20, 30
if num1>num2 and num1>num3:
    print(num1,"is Greatest")
elif num2>num1 and num2>num3:
    print(num2,"is Greatest")
else:
    print(num3,"is Greatest")




# Using Ternary Operator
num1, num2, num3 = 10, 20, 90
max=num1 if num1>num2 else num2
max=num3 if num3>max else max
print(max,"is Greatest")