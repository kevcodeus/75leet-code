

# 75 LeetCode Challenge - Day 19

## Problem 724: Find Pivot Index

### Problem Statement:

Given an array of integers `nums`, calculate the pivot index. The pivot index is the index where the sum of all the numbers strictly to the left of the index is equal to the sum of all the numbers strictly to the index's right. If no such index exists, return `-1`.

If the index is on the left edge of the array, then the left sum is `0` because there are no elements to the left. This also applies to the right edge of the array.

### Examples:

**Example 1:**

```python
Input: nums = [1, 7, 3, 6, 5, 6]  
Output: 3  
Explanation: The pivot index is 3.  
Left sum = nums[0] + nums[1] + nums[2] = 1 + 7 + 3 = 11  
Right sum = nums[4] + nums[5] = 5 + 6 = 11
```

**Example 2:**

```python
Input: nums = [1, 2, 3]  
Output: -1  
Explanation: There is no index that satisfies the conditions in the problem statement.
```

**Example 3:**

```python
Input: nums = [2, 1, -1]  
Output: 0  
Explanation: The pivot index is 0.  
Left sum = 0 (no elements to the left of index 0)  
Right sum = nums[1] + nums[2] = 1 + (-1) = 0
```

---

## Solution Approach

### Algorithm:

1. **Initialize Left and Right Sums:**
   - Start with the `left` sum set to `0` and the `right` sum set to the total sum of the array.

2. **Iterate Through the Array:**
   - For each element, adjust the `right` sum by subtracting the current element.
   - Check if the `left` sum is equal to the `right` sum. If true, return the current index.
   - If not, add the current element to the `left` sum and move to the next element.

3. **Return `-1` if No Pivot Found:**
   - If no pivot index is found after checking all elements, return `-1`.

### Code:

```python
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left = 0
        right = sum(nums)

        for i in range(len(nums)):
            right -= nums[i]
            if right == left:
                return i
            left += nums[i]

        return -1
```

### Explanation:

- **Step 1:** Initialize the total `right` sum as the sum of all elements in the array, and `left` sum as `0`.
- **Step 2:** For each index, subtract the element from `right` and compare it with `left`. If they are equal, the current index is the pivot index.
- **Step 3:** If no pivot is found by the end, return `-1`.

### Complexity:

- **Time Complexity:** `O(n)`, where `n` is the length of the array. We traverse the array only once.
- **Space Complexity:** `O(1)`, as no extra space is used apart from variables for the sums.

---

## Example Usage:

```python
if __name__ == "__main__":
    nums = [1, 7, 3, 6, 5, 6]
    solution = Solution()
    result = solution.pivotIndex(nums)
    print(result)  # Output will be 3
```

---
