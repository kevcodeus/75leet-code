from typing import List
class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        n1=set(nums1)
        n2=set(nums2)
        r1=list(set(x for x in nums1 if x not in n2))
        r2=list(set(x for x in nums2 if x not in n1))
        return [r1,r2]
nums1 = [1,2,3]
nums2 = [2,4,6]
solution = Solution()
result = solution.findDifference(nums1,nums2)
print(result)