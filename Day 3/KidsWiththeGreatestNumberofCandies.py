class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
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
