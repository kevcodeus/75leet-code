

# 75 LeetCode Challenge - Day 7

## Problem 238: Product of Array Except Self

**Problem Statement:**
Given an integer array `nums`, return an array `answer` such that `answer[i]` is equal to the product of all the elements of `nums` except `nums[i]`. The product of any prefix or suffix of `nums` is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

**Example 1:**
```python
Input: nums = [1, 2, 3, 4]
Output: [24, 12, 8, 6]
```

**Example 2:**
```python
Input: nums = [-1, 1, 0, -3, 3]
Output: [0, 0, 9, 0, 0]
```

---

## Solution Approach

### Step-by-Step Explanation

1. **Initialize Variables:**
   - `total_product`: To store the product of all elements in the array.
   - `product_x_zeros`: To store the product of all non-zero elements.
   - `zeros`: To count the number of zeros in the array.

2. **Calculate Products:**
   - Iterate through the array:
     - Multiply each element to `total_product`.
     - If the element is zero, increment the `zeros` count.
     - If the element is not zero, multiply it to `product_x_zeros`.

3. **Construct Result Array:**
   - Iterate through the array again:
     - If the current element is zero and there is more than one zero, append 0 to the result.
     - If the current element is zero and there is only one zero, append `product_x_zeros` to the result.
     - If the current element is not zero, append `total_product // current_element` to the result.

4. **Efficiency:**
   - This approach ensures O(n) time complexity without using the division operation.

---

## Code with Detailed Explanation

```python
from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        total_product = 1
        product_x_zeros = 1
        zeros = 0
        
        # Calculate total product and product excluding zeros
        for i in nums:
            total_product *= i
            if i == 0:
                zeros += 1
            else:
                product_x_zeros *= i
        
        result = []
        
        # Construct result array
        for j in nums:
            if j != 0:
                result.append(total_product // j)
            else:
                if zeros <= 1:
                    result.append(product_x_zeros)
                else:
                    result.append(0)
        
        return result
```

### Breakdown of the Code:

1. **Class Definition and Method:**
   - The `Solution` class contains the `productExceptSelf` method, which takes a list of integers `nums` and returns a list of integers as the result.

2. **Initialize Variables:**
   - `total_product`: To store the product of all elements in the array.
   - `product_x_zeros`: To store the product of all non-zero elements.
   - `zeros`: To count the number of zeros in the array.

3. **Calculate Products:**
   - Iterate through the array to compute `total_product` and `product_x_zeros`, and count zeros.

4. **Construct Result Array:**
   - Iterate again to construct the result based on whether the current element is zero or not.

5. **Efficiency:**
   - This approach ensures O(n) time complexity without using division.

### Example Usage

To run the solution, you can use the following code snippet:

```python
if __name__ == "__main__":
    nums = list(map(int, input("Enter the numbers, separated by spaces: ").split()))
    solution = Solution()
    result = solution.productExceptSelf(nums)
    print(result)
```

- This snippet takes input from the user for the array `nums`.
- Creates an instance of the `Solution` class.
- Calls the `productExceptSelf` method with the input array.
- Prints the result.

---

