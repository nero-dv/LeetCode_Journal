class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        if max(nums) < target:
            return len(nums)


        def chk(nums, target):
            if target in nums:
                return target
            return chk(nums, target+1)
        target = chk(nums, target)

        def bs(nums, target, low, high):
            if high >= low:
                mid = low + (high - low) // 2
            
                if nums[mid] == target:
                    return mid
                elif nums[mid] > target:
                    return bs(nums, target, low, mid-1)
                else:
                    return bs(nums, target, mid+1, high)
            else:
                return
            
        return bs(nums, target, 0, len(nums)-1)

nums = [1,1,1,4,5,6]
target = 37

print(Solution().searchInsert(nums, target))