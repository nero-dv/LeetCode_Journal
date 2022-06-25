def threeSum(nums):
        left = 0
        right = len(nums) - 1
        
        while left < right:
            summed = nums[left] + nums[right]
            missing = -1 * summed
            if left != right and missing != nums[left] and missing != nums[right] and missing in nums:
                return [nums[left], missing, nums[right]]
            else:
                if summed > 0:
                    right -= 1
                else:
                    left += 1