from typing import List
class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> bool:
        l = len(candies)
        maximum = max(candies)
        result = []
        for i in range(l):
            value = candies[i] + extraCandies
            if value >= maximum:
                result.append(True)
            else:
                result.append(False)
        return result

candies = list(map(int, input("Enter the number of candies: ").split()))
extraCandies = int(input("Enter the extra candies: "))
solution = Solution()
print(solution.kidsWithCandies(candies, extraCandies))
