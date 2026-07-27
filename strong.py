# Check Whether or Not the Number is a Strong Number in Python Language
num=int(input("Enter a Number:"))
temp=num
sum=0
f=[0]*10
f[0]=f[1]=1
for i in range(2,10):
    f[i]=f[i-1]*i
while temp>0:
    digit=temp%10
    sum+=f[digit]
    temp//=10

if sum==num:
    print("The number is a Strong number.")
else:
    print("The number is not a Strong number.")