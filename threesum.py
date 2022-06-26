from itertools import combinations


class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        cbs = combinations(nums, 3)
        ren = []
        ret = [sorted(x) for x in cbs if sum(sorted(x)) == 0]
        for item in ret:
            if item not in ren:
                ren.append(item)
        return ren

# nums = [-1,0,1,2,-1,-4]
# nums = ['A', 'B', 'C', 'D', 'E']
nums = [9,-15,6,6,10,-2,8,8,0,-6,-4,-2,14,-6,-14,-2,12,5,-2,-8,13,13,-10,4,-6,8,6,-15,-5,11,-15,11,3,-2,-6,-10,11,-12,13,-12,-11,-5,2,10,-4,-5,-15,-7,7,-2,0,5,-11,-3,-13,-10,-9,0,-10,-7,-12,12,-11,7,-5,-1,12,-8,-6,3,-13,-10,5,-4,-14,-14,6,8,-14,-9,-8,-7,3,-4,6,5,1,12,-9,6,-10,-6,-5,-14,-14,5,-8,6,4,1]

print(Solution().threeSum(nums))

        
