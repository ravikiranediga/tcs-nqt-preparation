binary=1010
dec=0

for digit in binary:
    dec=dec*2+int(digit)
print(f"The decimal representation of the given binary number is: {dec}")
