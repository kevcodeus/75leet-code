from typing import List
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        total_product=1
        product_x_zeros=1
        zeros=0
        for i in nums:
            total_product*=i
            if i == 0: zeros+=1
            if i != 0 :product_x_zeros*=i


        result=[]
    
        for j in nums:
            if j!=0: result.append(total_product//j)
            else: 
                if zeros<=1: result.append(product_x_zeros)
                else: result.append(0)
        return result
nums = list(map(int, input("Enter the numbers, separated by spaces: ").split()))
solution = Solution()
result = solution.productExceptSelf(nums)
print(result)