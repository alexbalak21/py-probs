import re

def is_palindrome(s: str) -> bool:
    s = re.sub(r'[^a-zA-Z]', '', s).lower()
    return s == s[::-1]