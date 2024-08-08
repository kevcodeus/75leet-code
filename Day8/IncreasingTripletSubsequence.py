from typing import List
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        smallest = next_smallest = float('inf')
        for num in nums:
            if num <= smallest:
                smallest = num
            elif num <= next_smallest:
                next_smallest = num
            else:
                return True
        return False
nums = list(map(int, input("Enter the numbers separated by spaces: ").split()))
solution = Solution()
result = solution.increasingTriplet(nums)
print(result)