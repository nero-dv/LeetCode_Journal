def twoSum(nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        left = 0
        right = 1
        
        a_len = len(nums)
        
        if a_len == 2 and nums[0] + nums[1] == target:
            return [0, 1]
        if a_len == 2 and nums[0] + nums[1] != target:
            return []
        
        
        
        while left < a_len:
            if right == a_len:
                left += 1
                right = left + 1
            if nums[left] + nums[right] == target:
                return [left, right]
            else:
                right += 1
        return []
    
