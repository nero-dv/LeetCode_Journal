"""
With this solution, I first tested for length equality between both strings as the two strings can not be anagrams if the lengths of each string differs from one another. I then created a dictionary object with all the letters in the alphabet and set the value to 0, then counted the number of times each letter appears in the string. If the dictionaries match, then the algorithm will True. If the dictionaries do not match, it returns False.

The three edge cases I have used lowered my memory usage by a marginal amount, roughly 100Kb, but it was enough to put this algorithm in the top 10% in terms of space.
"""


class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        slen = len(s)
        tlen = len(t)
        if slen != tlen:
            return False
        if s == t:
            return True
        if slen < 3 and reversed(s) == t or reversed(t) == s:
            return True

        al_map = "abcdefghijklmnopqrstuvwxyz "
        dict_measuring1 = {}
        dict_measuring2 = {}

        for letter in al_map:
            dict_measuring1[letter] = 0
            dict_measuring2[letter] = 0

        for s1 in s:
            if s1 in al_map:
                dict_measuring1[s1] = dict_measuring1[s1] + 1
        for s2 in t:
            if s2 in al_map:
                dict_measuring2[s2] = dict_measuring2[s2] + 1

        return dict_measuring1 == dict_measuring2
