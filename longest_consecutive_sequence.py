# Beats 90% in runtime, beats 70% in memory.


class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        num_set = set(nums)
        ans = 0

        for num in num_set:

            if num - 1 not in num_set:
                curr = num

                while curr + 1 in num_set:
                    curr += 1
                ans = max(ans, curr - num + 1)

        return ans


# Test cases

test = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
test2 = [-3, -2, -1, 0, 1, 2, 3, 4]
test3 = [1, 2, 4, 5, 7, 9, 10, 11, 11, 12, 13, 14, 15, 16]

Solution().longestConsecutive(test3)
