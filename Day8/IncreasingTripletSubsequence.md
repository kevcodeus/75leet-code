
# 75 LeetCode Challenge - Day 8

## Problem 334: Increasing Triplet Subsequence

**Problem Statement:**
Given an integer array `nums`, return `true` if there exists a triple of indices `(i, j, k)` such that `i < j < k` and `nums[i] < nums[j] < nums[k]`. If no such indices exist, return `false`.

**Example 1:**
```python
Input: nums = [1,2,3,4,5]
Output: true
Explanation: Any triplet where i < j < k is valid.
```

**Example 2:**
```python
Input: nums = [5,4,3,2,1]
Output: false
Explanation: No triplet exists.
```

**Example 3:**
```python
Input: nums = [2,1,5,0,4,6]
Output: true
Explanation: The triplet (3, 4, 5) is valid because nums[3] == 0 < nums[4] == 4 < nums[5] == 6.
```

---

## Solution Approach

### Step-by-Step Explanation

1. **Initialize Variables:**
   - `smallest`: Tracks the smallest value encountered so far, initialized to infinity.
   - `next_smallest`: Tracks the next smallest value, also initialized to infinity.

2. **Iterate Through the Array:**
   - For each element `num` in `nums`:
     - If `num` is less than or equal to `smallest`, update `smallest`.
     - Else if `num` is less than or equal to `next_smallest`, update `next_smallest`.
     - Else, if `num` is greater than both `smallest` and `next_smallest`, return `True` as it confirms the existence of the increasing triplet.

3. **Return Result:**
   - If no triplet is found during the iteration, return `False`.

---

## Code with Detailed Explanation

```python
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        smallest = next_smallest = float('inf')
        for num in nums:
            if num <= smallest:
                smallest = num
            elif num <= next_smallest:
                next_smallest = num
            else:
                return True
        return False
```

### Breakdown of the Code:

1. **Class Definition and Method:**
   ```python
   class Solution:
       def increasingTriplet(self, nums: List[int]) -> bool:
           smallest = next_smallest = float('inf')
           for num in nums:
               if num <= smallest:
                   smallest = num
               elif num <= next_smallest:
                   next_smallest = num
               else:
                   return True
           return False
   ```
   - The `increasingTriplet` function is defined within the `Solution` class.
   - It iterates over the array `nums` to find if an increasing triplet subsequence exists.

2. **Tracking the Smallest Values:**
   - The variables `smallest` and `next_smallest` help in tracking the first two smallest numbers encountered in order.
   - If a number greater than both is found, it confirms the existence of an increasing triplet.

3. **Returning the Result:**
   - The function returns `True` if a valid triplet is found, otherwise `False`.

### Example Usage

To run the solution, you can use the following code snippet:

```python
if __name__ == "__main__":
    nums = list(map(int, input("Enter the numbers separated by spaces: ").split()))
    solution = Solution()
    result = solution.increasingTriplet(nums)
    print(result)
```

- This snippet takes input from the user for the array `nums`.
- Creates an instance of the `Solution` class.
- Calls the `increasingTriplet` method with the input array.
- Prints the result.

