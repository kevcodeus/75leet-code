

# 75 LeetCode Challenge - Day 18

## Problem 1732: Find the Highest Altitude

### Problem Statement:

There is a biker going on a road trip. The road trip consists of `n + 1` points at different altitudes. The biker starts his trip at point `0` with an altitude of `0`.

You are given an integer array `gain` of length `n` where `gain[i]` is the net gain in altitude between points `i` and `i + 1`. Your task is to return the highest altitude of a point during the trip.

### Examples:

**Example 1:**

```python
Input: gain = [-5, 1, 5, 0, -7]
Output: 1
Explanation: The altitudes are [0, -5, -4, 1, 1, -6]. The highest is 1.
```

**Example 2:**

```python
Input: gain = [-4, -3, -2, -1, 4, 3, 2]
Output: 0
Explanation: The altitudes are [0, -4, -7, -9, -10, -6, -3, -1]. The highest is 0.
```

---

## Solution Approach

### Algorithm:

1. **Initialize the Altitude:**  
   - Start at point `0` with an altitude of `0`.  
   
2. **Compute Altitudes:**  
   - Iterate through the `gain` array, calculating the altitude at each point using the previous altitude and the net gain for that step.

3. **Track the Maximum Altitude:**  
   - Keep track of the highest altitude reached during the trip.

### Code:

```python
class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        n = len(gain)
        res = [0] * (n + 1)   
        
        for i in range(n):
            res[i + 1] = res[i] + gain[i]
            
        return max(res)
```

### Explanation:

- **Step 1:** Start the journey at altitude `0`. 
- **Step 2:** For each point, add the gain to the previous altitude to get the new altitude.
- **Step 3:** Use the `max()` function to find the highest altitude encountered during the journey.

### Complexity:

- **Time Complexity:** `O(n)`, where `n` is the length of the `gain` array.
- **Space Complexity:** `O(n + 1)` for storing the altitudes at each point.

---

### Example Usage:

```python
if __name__ == "__main__":
    gain = [-5, 1, 5, 0, -7]
    solution = Solution()
    result = solution.largestAltitude(gain)
    print(result)  # Output will be 1
```

---

