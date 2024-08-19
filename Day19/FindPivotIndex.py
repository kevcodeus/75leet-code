from typing import List
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left = 0
        right = sum(nums)

        for i in range(len(nums)):

            right-=nums[i]
            if right==left:
                return i
                
            left+=nums[i]

        return -1
nums = [1, 7, 3, 6, 5, 6]
solution = Solution()
result = solution.pivotIndex(nums)
print(result)