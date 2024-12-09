import collections
import re

def is_anagram(s1: str, s2: str) -> bool:
    # Remove non-alphabetic characters and convert to lowercase
    s1 = re.sub(r'[^a-zA-Z]', '', s1).lower()
    s2 = re.sub(r'[^a-zA-Z]', '', s2).lower()
    
    # Compare the frequency of characters
    return collections.Counter(s1) == collections.Counter(s2)

# Test cases
print(is_anagram("listen", "silent"))  # Output: True
print(is_anagram("hello", "world"))    # Output: False
print(is_anagram("A gentleman", "Elegant man"))  # Output: True
print(is_anagram("Clint Eastwood", "Old West Action"))  # Output: True