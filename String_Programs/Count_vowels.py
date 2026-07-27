text="Ravi Kiran"
count=0
for ch in text:
    if ch.lower() in 'aeiou':
        count+=1
print(f"The number of vowels in the given string is: {count}")




# Complexity Analysis:
# Time:O(n)
#Space:O(1)