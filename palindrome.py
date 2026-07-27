# Check Whether or Not the Number is a Palindrome in Python Language
num=int(input("Enter a Number:"))
reverse =0

while num>0:
    remainder=num%10
    reverse=reverse*10+remainder
    num=num//10

    if num==reverse:
        print("The number is palindrome:",reverse)
    else:
        print("The number is not palindrome:",reverse)


# Using in-built reversed() function
num=input("Enter a Number:")
reverse=''.join(reversed(num))
if num==reverse:
    print("The number is palindrome:",reverse)
else:
    print("The number is not palindrome:",reverse)
