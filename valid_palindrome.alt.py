import re

def isPalindrome(s):
    """
    :type s: str
    :rtype: bool
    """
    
    if len(s) == 1:
        return True
    
    s = s.lower()
    abc_map = 'abcdefghijklmnopqrstuvwxyz0123456789'
    cleaned_string = ''
    
    for letter in s:
        if letter in abc_map:
            cleaned_string += letter
    reversed_cs = cleaned_string[::-1]
    
    if cleaned_string == reversed_cs:
        return True
    return False
