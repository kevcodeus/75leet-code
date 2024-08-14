from typing import List 
class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        count = 0
        i, j = 0, len(nums) - 1
        nums.sort()

        while i < j:
            temp = nums[i] + nums[j]
            if temp == k:
                count += 1
                i += 1
                j -= 1
            elif temp < k:
                i += 1
            else:
                j -= 1
        return count
nums = [1, 2, 3, 4]
k = 5
solution = Solution()
result = solution.maxOperations(nums, k)
print(result)