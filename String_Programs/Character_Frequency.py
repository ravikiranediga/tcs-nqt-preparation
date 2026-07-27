text ="hello"
freq={}
for ch in text:
    if ch in freq:
        freq[ch]+=1
    else:
        freq[ch]=1
print(f"The frequency of characters in the given string is: {freq}")

# Complexity Analysis:
# Time:O(n)
# Space:O(n)