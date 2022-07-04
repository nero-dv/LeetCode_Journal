class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 1:
            return 1
        result = ""
        result_compare = []

        for x in s:
            if x not in result:
                result += x
            else:
                result_compare.append(result)
                result = ""
                result += x
        count = [len(j) for j in result_compare]
        print(count)
        if count:
            count = max(count)
        else:
            count = 0

        return count


s = " "
print(Solution().lengthOfLongestSubstring(s))
