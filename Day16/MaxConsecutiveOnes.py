from typing import List
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left=0
        count_zero=0
        max_array=0
        for right in range(len(nums)):
            if nums[right] == 0:
                count_zero+=1
                while count_zero > k:
                    if nums[left] == 0:
                        count_zero-=1
                    left+=1
            
            max_array=max(max_array,right-left+1)

        return max_array
nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1]
k = 3
solution = Solution()
result = solution.longestOnes(nums, k)
print(result)