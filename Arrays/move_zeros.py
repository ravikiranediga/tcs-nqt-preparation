arr=[1,2,0,3,0,5,0,6]
res=[]

for num in arr:
    if num!=0:
        res.append(num)
zeros=len(arr)-len(res)

res.extend[0]*zeros
print(res)


#complexity

#Time  : O(n)
#Space : O(1)