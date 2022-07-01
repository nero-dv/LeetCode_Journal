class Solution:
    def maxArea(self, height: list[int]) -> int:
        ret, l, r = 0, 0, len(height) - 1        
        
        while l < r:
            h = [height[l], height[r]]            
            area = min(h) * (r - l)
            ret = max(area, ret)
            
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
            
        return ret
    
    
height = [1,8,6,2,5,4,8,3,7]
print(Solution().maxArea(height=height))