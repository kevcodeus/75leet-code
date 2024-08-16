

# 75 LeetCode Challenge - Day 16

## Problem 1004: Max Consecutive Ones III

### Problem Statement:

Given a binary array `nums` and an integer `k`, return the maximum number of consecutive `1`'s in the array if you can flip at most `k` `0`'s.

### Examples:

**Example 1:**

```python
Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2  
Output: 6  
Explanation: The bolded numbers were flipped from `0` to `1`. The longest subarray is [1,1,1,0,0,1,1,1,1,1,1], which contains 6 consecutive `1`'s.
```

**Example 2:**

```python
Input: nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3  
Output: 10  
Explanation: The longest subarray with at most `3` flips contains 10 consecutive `1`'s.
```

---

## Solution Approach

### Algorithm:

1. **Sliding Window Technique:**
   - Use two pointers (`left` and `right`) to maintain a sliding window that expands as long as the number of `0`'s in the window is at most `k`.
   
2. **Count and Track:**
   - Keep a count of the number of `0`'s in the current window.
   - If the count exceeds `k`, shrink the window from the left until the number of `0`'s is again at most `k`.

3. **Max Tracking:**
   - Track the maximum length of the window that contains at most `k` flipped `0`'s.

### Code:

```python
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = 0
        count_zero = 0
        max_array = 0

        for right in range(len(nums)):
            if nums[right] == 0:
                count_zero += 1
            
            while count_zero > k:
                if nums[left] == 0:
                    count_zero -= 1
                left += 1
            
            max_array = max(max_array, right - left + 1)

        return max_array
```

### Explanation:

- **Step 1:** Use a sliding window to count the number of `0`'s between `left` and `right` pointers.
- **Step 2:** If the number of `0`'s exceeds `k`, increment the `left` pointer until the number of `0`'s in the window is again valid (≤ `k`).
- **Step 3:** Track the maximum size of the valid window encountered.

### Complexity:

- **Time Complexity:** `O(n)`, where `n` is the length of the array `nums`.
- **Space Complexity:** `O(1)`, as only constant extra space is used.

---

### Example Usage:

```python
if __name__ == "__main__":
    nums = [1,1,1,0,0,0,1,1,1,1,0]
    k = 2
    solution = Solution()
    result = solution.longestOnes(nums, k)
    print(result)  # Output will be 6
```

---


