import re

def isPalindrome( s: str) -> bool:
        
    s = (re.sub(r'[^a-zA-Z0-9\s]', '', s)).lower().replace(" ", "")

    return s == s[::-1]