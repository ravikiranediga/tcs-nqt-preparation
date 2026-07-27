text = " ravi kiran babu"
words=text.split()
result =""

for word in words:
    result+=word[0].upper()+word[1:]+" "
print(result)

# Complexity Analysis:  
# Time:O(n)
# Space:O(n)