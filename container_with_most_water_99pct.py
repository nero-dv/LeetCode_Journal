class Solution:
    def maxArea(self, height: list[int]) -> int:
        l = 0
        r = len(height) - 1
        width = len(height) - 1
        result = 0
        
        for w in range(width, 0, -1):
            if height[l] < height[r]:
                result, l = max(result, height[l] * w), l + 1
            else:
                result, r = max(result, height[r] * w), r - 1
        return result
    
height = [1,8,6,2,5,4,8,3,7]
print(Solution().maxArea(height=height))