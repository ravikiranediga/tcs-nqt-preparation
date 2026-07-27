# Find the Reverse of a Number in Python Language
num=int(input("Enter a Number:"))
reverse =0

while num>0:
    remainder=num%10
    reverse=reverse*10+remainder
    num=num//10
print("The reverse of the number is:",reverse)


# Using String Slicing 
num=input("Enter a Number:")
reverse=num[::-1]
print("The reverse of the number is:",reverse)

