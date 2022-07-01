# Time: o(n^2)
# Space: o(n)

class Solution:
    def threeSum(self, nums: list[int]):
        # sort the input array
        nums.sort()
        
        # create a list to store the returned values
        ret = []
        
        # iterate through the input array
        for idx, num in enumerate(nums):
            
            # This is checking if the current number is the same as the previous number. If it is,
            # then we don't need to check it again.
            if idx > 0 and num == nums[idx-1]:
                continue
            
            # Create variables to iterate through the remaining numbers
            left, right  = idx + 1, len(nums) - 1
            while left < right:
                
                # Calculate the sum of the current number, the left number, and the right number
                ans = num + nums[left] + nums[right]
                
                # If the sum is 0, then we've found a solution
                # Else, we need to adjust the left and right indices
                # If the sum is less than 0, then we need to increase the left index
                # If the sum is greater than 0, then we need to decrease the right index
                if ans > 0:
                    right -= 1
                elif ans < 0:
                    left += 1
                    
                # If the sum is 0, then we've found a solution
                # add the current number, the left number, and the right number to the list of solutions
                # then, increase the left index unless we've already checked the left number
                else:
                    ret.append([num, nums[left], nums[right]])
                    left += 1
                    while nums[left] == nums[left-1] and left < right:
                        left += 1
        
        return ret
                    
        
        
        
# nums = [-1,0,1,2,-1,-4]
nums = [9,-15,6,6,10,-2,8,8,0,-6,-4,-2,14,-6,-14,-2,12,5,-2,-8,13,13,-10,4,-6,8,6,-15,-5,11,-15,11,3,-2,-6,-10,11,-12,13,-12,-11,-5,2,10,-4,-5,-15,-7,7,-2,0,5,-11,-3,-13,-10,-9,0,-10,-7,-12,12,-11,7,-5,-1,12,-8,-6,3,-13,-10,5,-4,-14,-14,6,8,-14,-9,-8,-7,3,-4,6,5,1,12,-9,6,-10,-6,-5,-14,-14,5,-8,6,4,1]

print(Solution().threeSum(nums))

        
