# Python Program to Find the Sum of First N Natural Numbers

# Using Loops

num = 5
sum =0 
for i in range(num+1):
    sum+=i
print(sum)



# Using Formula Sum of Nth Term 
# Sum = n(n+1)/2

num=5
print(int (num*(num+1)/2))



#  Using Recursion

def getsum(num):
    if num==1:
        return 1 
    else :
        return num + getsum(num-1)
num=5 
print(getsum(num))

