arr=[10,5,20,30,50]
max=arr[0]
min=arr[0]


for num in arr:
    if num>max:
        max=num
    if num<min:
        min=num
print("Maximum:" ,max)
print("Minimum:" ,min)


#Complexity
#Time:O(n)
#Space:O(1)