arr=[10,20,30,40,50,60]
target=40

found=False

for i in range(len(arr)):
    if arr[i]==target:
        print("Found at index:" ,i )
        found=True
        break
if not found:
    print("NOT FOUND")



# Complexity
#Time : O(n)
#Space: O(1)