arr=[1,2,4,3,2,6]
seen={}

for num in arr:
    if num==seen:
        print(num)
        break
    seen.add(num)


#Complexity
#Time  : O(n)
#Space : O(n)