from typing import List

class Solution:
    def canPlaceFlowers(self, bed: List[int], n: int) -> bool:
        left, right = -2, 0
        
        while n > 0 and right < len(bed):
            if bed[right] == 1:
                n -= (right-left-2)//2
                left = right
            right += 1
        if bed[-1] == 0 and right == len(bed):
            n -= (right-left-1)//2
        return n <= 0

# Example usage:
flowerbed = list(map(int, input("Enter the flowerbed: ").split()))
n = int(input("Enter the number of new flowers to plant: "))
solution = Solution()
print(solution.canPlaceFlowers(flowerbed, n))
