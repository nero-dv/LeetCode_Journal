# Beats 90% in runtime, beats 70% in memory.

class Solution:
    def longestConsecutive(nums: list[int]) -> int:
        # Create a set to store the numbers
        nums = set(nums)
        # Set the longest consecutive sequence to 0
        ans = 0
        # Iterate through the set of numbers to find the longest consecutive sequence
        for num in nums:
            # if the number minus 1 is in the set, then the number is part of a consecutive sequence
            if num - 1 not in nums:
                curr = num
                # If the number plus 1 is in the set, then the number is part of a consecutive sequence
                while curr + 1 in nums:
                    curr += 1
                # Update the longest consecutive sequence
                ans = max(ans, curr - num + 1)
        return ans
        
# Test cases
        
nums = [0,3,7,2,5,8,4,6,0,1]
nums2 = [-3, -2, -1, 0, 1, 2, 3, 4]

print(Solution.longestConsecutive(nums))

