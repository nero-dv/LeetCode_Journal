class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        n = len(nums)
        l, r = 0, n-1
        res = [0] * n
        idx = n-1

        while r > -1 and idx > -1:
            if abs(nums[l]) > abs(nums[r]):
                res[idx] = nums[l] ** 2
                l += 1
            else:
                res[idx] = nums[r] ** 2
                r -= 1
            idx -= 1
        return res
        
nums = [-4, 1, 0, 3, 10]
print(Solution().sortedSquares(nums))