from typing import List
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        c_nums = {}
        for i in arr:
            c_nums[i] = c_nums.get(i,0)+1
        return len(c_nums.values())==len(set(c_nums.values()))
arr = [1,2,2,1,1,3]
solution = Solution()
result = solution.uniqueOccurrences(arr)
print(result)