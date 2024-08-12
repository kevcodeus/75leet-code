
# LeetCode Challenge - Day 12

## Problem 11: Container With Most Water

### Problem Statement:
You are given an integer array `height` of length `n`. There are `n` vertical lines drawn such that the two endpoints of the `i-th` line are `(i, 0)` and `(i, height[i])`.

Find two lines that, together with the x-axis, form a container that contains the most water.

Return the maximum amount of water a container can store.

**Example 1:**
```python
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The vertical lines represented by the array [1,8,6,2,5,4,8,3,7] form a container with the maximum area of 49 units of water.
```

**Example 2:**
```python
Input: height = [1,1]
Output: 1
Explanation: The maximum area is achieved with the two lines at indices 0 and 1, containing 1 unit of water.
```

---

## Solution Approach

### Two-Pointer Technique

The problem is solved using the two-pointer approach, which efficiently finds the maximum area in O(n) time complexity.

### Step-by-Step Explanation:

1. **Initialize Two Pointers:**
   - `l`: Start at the beginning of the array.
   - `r`: Start at the end of the array.
   - `area`: A variable to keep track of the maximum area found so far.

2. **Calculate Area:**
   - The area between the two pointers is calculated using the formula:
     \[
     \text{Area} = (\text{r} - \text{l}) \times \min(\text{height[l]}, \text{height[r]})
     \]

3. **Move Pointers:**
   - If the height at `l` is less than the height at `r`, move the `l` pointer to the right to potentially find a taller line.
   - Otherwise, move the `r` pointer to the left to potentially find a taller line.

4. **Update Maximum Area:**
   - Continuously update the `area` with the maximum value found during the iteration.

5. **Return the Result:**
   - After iterating through the array, return the maximum area found.

### Solution Code:
```python
class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r, area = 0, len(height) - 1, 0
        while l < r:
            area = max(area, (r - l) * min(height[l], height[r]))
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
                
        return area
```

### Example Usage:

To run the solution, you can use the following code snippet:

```python
if __name__ == "__main__":
    height = [1,8,6,2,5,4,8,3,7]  # Example input
    solution = Solution()
    result = solution.maxArea(height)
    print(f"Maximum water the container can store: {result}")
```

---



