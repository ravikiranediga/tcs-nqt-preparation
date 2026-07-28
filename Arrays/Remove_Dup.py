arr=[1,2,1,3,2,4]
result=[]


for num in arr:
    if num not in result:
        result.append(num)
print(result)


#Complexity 
# Time : O(n²)
#Space: O(n)