from typing import List
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        oc = 0
        
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[oc], nums[i] = nums[i], nums[oc]
                oc += 1
        
nums = [0]
solution = Solution()
solution.moveZeroes(nums)
print(nums)