# Find the Fibonacci Series up to Nth Term in Python
num=int(input("Enter a Number:"))
n1,n2=0,1
print("Fibonacci Series:",n1,n2,end=" ")
for i in range(2,num):
    n3=n1+n2
    print(n3,end=" ")
    n1=n2
    n2=n3



# Nth Term of a Fibonacci Series
def Fibonacci(n):
    if n < 2:
        return n

    fs = [0, 1]

    for i in range(1, n):
        fs.append(fs[i] + fs[i - 1])

    return fs[n]

n = 10
print(Fibonacci(n - 1))