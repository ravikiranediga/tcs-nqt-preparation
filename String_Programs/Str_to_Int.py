num="1234"
s=0

for ch in num:
    digit = ord(ch)-ord('0')
    s=s*10+digit
print(s)


#Complexitiy
#Time:O(n)
#Space:O(n)