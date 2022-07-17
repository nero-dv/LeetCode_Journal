class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set: set[str] = set()
        l = res = 0
        for r in range(len(s)):

            # once all unique values are in the set, if the the current item
            # in the iterable 's' is already in the set, remove the item and
            # increase the left index.
            while s[r] in char_set:
                char_set.remove(s[l])
                l += 1
            char_set.add(s[r])

            # subtract the left index from the right index and add 1 (to
            # offset the zero indexed iterable 's')
            # update res if this value is higher than the current value in res.
            res = max(res, (r - l) + 1)

        return res


s = "abcabcbb"
# s = "bbbbb"
# s = "pwwkew"
# s = "dvdf"
# s = ""

ans = Solution().lengthOfLongestSubstring(s)
print(ans)
