from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prev_value: dict[int, int] = {}
        for idx, num in enumerate(nums):
            value: int = target - num
            if value in prev_value:
                return [idx, prev_value[idx]]
            prev_value[num] = idx
        return []