arr=[10,5,20,30,50]
largest =second=float("-inf")

for num in arr:
    if num>largest:
        second=largest
        largest=num

    elif num>second and num!=largest:
        second =num

print(second)


#Complexity
#Time : O(n)
#Space: O(1)