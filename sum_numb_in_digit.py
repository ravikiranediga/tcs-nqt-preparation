# This program calculates the sum of the digits of a given number.
num = int(input("Enter a number: "))
sum_digits = 0

while num > 0:
    digit = num % 10
    sum_digits += digit
    num = num // 10

print(sum_digits)