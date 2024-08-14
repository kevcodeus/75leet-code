from typing import List
class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r, area = 0, len(height) - 1, 0
        while l < r:
            area = max(area, (r - l) * min(height[l], height[r]))
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
				
        return area
height = [1,8,6,2,5,4,8,3,7]  
solution = Solution()
result = solution.maxArea(height)
print(f"Maximum water the container can store: {result}")