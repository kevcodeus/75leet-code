
---

# 75 LeetCode Challenge - Day 17

## Problem 1493: Longest Subarray of 1's After Deleting One Element

### Problem Statement:

Given a binary array `nums`, you should delete one element from it. Return the size of the longest non-empty subarray containing only 1's in the resulting array. If no such subarray exists, return `0`.

### Examples:

**Example 1:**

```python
Input: nums = [1,1,0,1]
Output: 3
Explanation: After deleting the number in position 2, [1,1,1] contains 3 numbers with value 1.
```

**Example 2:**

```python
Input: nums = [0,1,1,1,0,1,1,0,1]
Output: 5
Explanation: After deleting the number in position 4, the longest subarray of 1's is [1,1,1,1,1].
```

**Example 3:**

```python
Input: nums = [1,1,1]
Output: 2
Explanation: You must delete one element.
```

---

## Solution Approach

### Algorithm:

1. **Sliding Window:**  
   - Use two pointers, `left` and `right`, to track the subarray of 1's.
   - Keep a count of `0`'s within the window. If more than one `0` exists in the window, shift the `left` pointer to reduce the count.
   
2. **Max Tracking:**  
   - As you expand the window with the `right` pointer, keep track of the maximum subarray length that contains only one `0`.

### Code:

```python
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        left, count_zeros, max_length = 0, 0, 0
        
        for right in range(len(nums)):
            if nums[right] == 0:
                count_zeros += 1
            
            while count_zeros > 1:
                if nums[left] == 0:
                    count_zeros -= 1
                left += 1
                
            max_length = max(max_length, right - left)
        
        return max_length
```

### Explanation:

- **Step 1:** Use the sliding window technique to process subarrays and count the number of `0`'s.
- **Step 2:** If more than one `0` is found in the current subarray, shift the `left` pointer to exclude the excess `0`.
- **Step 3:** Track the maximum length of valid subarrays where exactly one element was deleted.

### Complexity:

- **Time Complexity:** `O(n)`, where `n` is the length of the array.
- **Space Complexity:** `O(1)`, as only constant extra space is used.

---

### Example Usage:

```python
if __name__ == "__main__":
    nums = [1,1,0,1]
    solution = Solution()
    result = solution.longestSubarray(nums)
    print(result)  # Output will be 3
```

---

