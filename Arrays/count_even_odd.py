arr=[2,4,3,5,7,1,8,10]
even=0
odd=0

for num in arr:
    if num%2==0:
        even+=1
    else:
        odd+=1
print("Even:",even)
print("Odd:",odd)


#Complexity 
#Time : O(n)
#Space: O(1)