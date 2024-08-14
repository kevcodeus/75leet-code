
# LeetCode Challenge - Day 14

## Problem 643: Maximum Average Subarray I

### Problem Statement:

You are given an integer array `nums` consisting of `n` elements, and an integer `k`. Find a contiguous subarray whose length is equal to `k` that has the maximum average value and return this value. Any answer with a calculation error less than `10^-5` will be accepted.

### Example 1:
```python
Input: nums = [1,12,-5,-6,50,3], k = 4
Output: 12.75000
Explanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75
```

### Example 2:
```python
Input: nums = [5], k = 1
Output: 5.00000
```

---

## Solution Approach

### Sliding Window Technique

This problem is solved using the sliding window technique. The goal is to maintain a window of size `k` and continuously slide it across the array while calculating the sum of elements within the window and keeping track of the maximum sum.

### Steps:
1. **Initialize the Window:** Start by calculating the sum of the first `k` elements in the array.
2. **Sliding the Window:** Iterate through the rest of the array. For each new element that enters the window, subtract the element that is leaving the window and add the new element to the window's sum.
3. **Update Maximum Sum:** Keep track of the maximum sum encountered during the iteration.
4. **Return the Maximum Average:** Divide the maximum sum by `k` to get the maximum average.

---

## Code Implementation

```python
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        window = sum(nums[:k])
        max_sum = window
        
        for i in range(len(nums) - k):
            window = window - nums[i] + nums[i + k]
            max_sum = max(max_sum, window)
        
        return max_sum / k
```

### Explanation:
- **Initialization:** We first calculate the sum of the first `k` elements in the array.
- **Sliding Window:** By continuously updating the sum of the window as we iterate through the array, we efficiently keep track of the maximum sum.
- **Return Value:** Finally, we return the maximum sum divided by `k`, giving us the maximum average.

---

## Example Usage:

```python
if __name__ == "__main__":
    nums = [1,12,-5,-6,50,3]
    k = 4
    solution = Solution()
    print(solution.findMaxAverage(nums, k))  # Output: 12.75
```

---


