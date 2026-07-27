# Check Whether or Not the Number is an Automorphic Number in Python
num=376
square=pow(num,2)
mod=pow(10,len(str(num)))
if square % mod == num:
    print(f"{num} is an automorphic number.")
else:
    print(f"{num} is not an automorphic number.")



# Using Endswith() Method
num=5
a=str(num)


num1=num**2
b=str(num1)

if b.endswith(a):
    print(f"{num} is an automorphic number.")
else:
    print(f"{num} is not an automorphic number.")