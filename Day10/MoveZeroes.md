

# 75 LeetCode Challenge - Day 10

## Problem 283: Move Zeroes

**Problem Statement:**
Given an integer array `nums`, move all `0`s to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

**Example 1:**
```python
Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
```

**Example 2:**
```python
Input: nums = [0]
Output: [0]
```

---

## Solution Approach

### Step-by-Step Explanation

1. **Initialize a Zero Counter:**
   - Create a variable `oc` (which stands for "occupied") and initialize it to `0`. This variable keeps track of the position where the next non-zero element should be placed.

2. **Traverse the Array:**
   - Iterate over the array `nums` using a loop.
   - If the current element is not `0`, swap it with the element at the `oc` index, and then increment `oc`.

3. **In-Place Modification:**
   - This solution modifies the array in place, ensuring that all `0`s are moved to the end while maintaining the relative order of non-zero elements.

### Code with Detailed Explanation

```python
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        oc = 0  # Initialize the zero counter
        
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[oc], nums[i] = nums[i], nums[oc]  # Swap the current element with the element at index oc
                oc += 1  # Increment the zero counter to point to the next position
```

### Breakdown of the Code:

1. **Class Definition and Method:**
   - The `Solution` class contains the method `moveZeroes` which takes the array `nums` as input and modifies it in place.

2. **Zero Counter:**
   - The variable `oc` keeps track of where the next non-zero element should be placed in the array.

3. **Swapping Non-Zero Elements:**
   - The loop iterates over the array, and for each non-zero element, it swaps the current element with the element at the `oc` index, ensuring that all non-zero elements are moved to the front, while all `0`s are moved to the end.

4. **In-Place Modification:**
   - The array `nums` is modified directly, without using any additional space, making this an efficient solution.

### Example Usage

To use this solution, simply create an instance of the `Solution` class and call the `moveZeroes` method:

```python
if __name__ == "__main__":
    nums = [0, 1, 0, 3, 12]
    solution = Solution()
    solution.moveZeroes(nums)
    print(nums)  # Output should be [1, 3, 12, 0, 0]
```

- This example takes an array `nums`, moves all `0`s to the end while maintaining the order of non-zero elements, and then prints the modified array.

---
