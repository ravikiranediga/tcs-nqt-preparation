text="MADAM"
palindrome=True
for i in text:
    reverse=i+reverse
if text==reverse:
    print(f"The given string is a palindrome")
else:
    print(f"The given string is not a palindrome")

# Complexity Analysis:
# Time:O(n)
# Space:O(n)