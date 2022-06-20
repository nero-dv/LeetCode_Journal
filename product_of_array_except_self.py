class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        array_length = len(nums)
        result = [1] * array_length
        previous_index = 1
        last_index = 1
        for idx in range(len(nums)):
            result[idx] = previous_index
            previous_index *= nums[idx]
        for i in range(array_length - 1, -1, -1):
            result[i] *= last_index
            last_index *= nums[i]
        return result