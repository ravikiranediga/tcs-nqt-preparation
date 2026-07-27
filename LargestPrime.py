num=84
largest=-1

while num%2==0:
    largest=2
    num=num//2

factor=3
while factor*factor<=num:
    while num%factor==0:
        largest=factor
        num=num//factor
    factor+=2

if num>1:
    largest=num

print(f"The largest prime factor of the given number is: {largest}")