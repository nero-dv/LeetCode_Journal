import re

def isPalindrome(s):
    """
    :type s: str
    :rtype: bool
    """
    
    if len(s) == 1:
        return True

    s = s.lower()
    cleaned_string = re.sub(r'[^\w\\s]|_', '', s)
    reversed_cs = cleaned_string[::-1]
    print(f"clean: {cleaned_string}\nreversed: {reversed_cs}")
    
    if cleaned_string == reversed_cs:
        return True
    return False
