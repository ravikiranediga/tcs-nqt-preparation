# Find the Factors of a Number in Python Language


def factors(num):
    result=1
    while result<=num:
        if num%result==0:
            print(result,end=" ")
        result+=1
print("The factors of the number are:")
num=int(input("Enter a Number:"))
factors(num)


# ANOTHER METHOD
def factors(num):
    result=1
    for result in range(1,num+1):
        if num%result==0:
            print(result,end=" ")
print("The factors of the number are:")
num=int(input("Enter a Number:"))
factors(num)


