class Solution:
    def trap(self, height: list[int]) -> int:
        result, l, r = 0, 0, len(height) - 1
        ml, mr = height[l], height[r]
        
        while l < r:
            if ml < mr:
                l = l + 1
                ml = max(ml, height[l])
                result += ml - height[l]
            else:
                r = r - 1
                mr = max(mr, height[r])
                result += mr - height[r]
                
        return result

height = [0,1,0,2,1,0,1,3,2,1,2,1]
print(Solution().trap(height))