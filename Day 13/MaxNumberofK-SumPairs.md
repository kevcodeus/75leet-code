

# LeetCode Challenge - Day 13

## Problem 1679: Max Number of K-Sum Pairs

### Problem Statement:
Given an integer array `nums` and an integer `k`, your task is to find the maximum number of operations where you can pick two numbers from the array that sum up to `k` and remove them. Each number in the array can be used at most once in each operation.

### Example 1:
```python
Input: nums = [1, 2, 3, 4], k = 5
Output: 2
Explanation: 
- Remove numbers 1 and 4, then nums = [2, 3]
- Remove numbers 2 and 3, then nums = []
There are no more pairs that sum up to 5, hence a total of 2 operations.
```

### Example 2:
```python
Input: nums = [3, 1, 3, 4, 3], k = 6
Output: 1
Explanation: 
- Remove the first two 3's, then nums = [1, 4, 3]
There are no more pairs that sum up to 6, hence a total of 1 operation.
```

---

## Solution Approach

### Step-by-Step Explanation:
1. **Sorting the Array:**
   - The array `nums` is sorted to enable the use of the two-pointer technique.

2. **Two-Pointer Technique:**
   - **Initialization:** Start with two pointers, `i` at the beginning of the array and `j` at the end.
   - **Check Sum:** Calculate the sum of the elements at the two pointers.
     - If the sum equals `k`, increment the count, move both pointers inward, and continue.
     - If the sum is less than `k`, move the left pointer `i` to the right.
     - If the sum is greater than `k`, move the right pointer `j` to the left.
   
3. **Counting Valid Pairs:**
   - Every time a valid pair is found, the count is incremented.

4. **Return Result:**
   - The total count of valid pairs is returned as the result.

---

## Code Implementation

```python
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
```

### Explanation of the Code:
- **Sorting the Array:** The array is sorted to enable the two-pointer technique.
- **Using Two Pointers:** 
  - The `i` pointer starts from the beginning, and the `j` pointer starts from the end.
  - Depending on the sum of `nums[i]` and `nums[j]`, the pointers are adjusted.
  - The count is incremented each time a valid pair is found.

### Example Usage
To run the solution, use the following snippet:
```python
if __name__ == "__main__":
    nums = [1, 2, 3, 4]
    k = 5
    solution = Solution()
    result = solution.maxOperations(nums, k)
    print(result)  # Output: 2
```

---
