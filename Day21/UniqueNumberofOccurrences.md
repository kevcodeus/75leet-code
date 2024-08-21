
# 75 LeetCode Challenge - Day 21

## Problem 1207: Unique Number of Occurrences

### Problem Statement:

Given an array of integers `arr`, return `true` if the number of occurrences of each value in the array is unique, or `false` otherwise.

### Examples:

**Example 1:**

```python
Input: arr = [1,2,2,1,1,3]  
Output: true  
Explanation: The value 1 has 3 occurrences, 2 has 2, and 3 has 1. No two values have the same number of occurrences.
```

**Example 2:**

```python
Input: arr = [1,2]  
Output: false  
Explanation: The value 1 has 1 occurrence, and the value 2 has 1 occurrence. Both values have the same frequency.
```

**Example 3:**

```python
Input: arr = [-3,0,1,-3,1,1,1,-3,10,0]  
Output: true  
Explanation: The value -3 has 2 occurrences, 0 has 2, 1 has 4, and 10 has 1. No two values have the same number of occurrences.
```

---

## Solution Approach

### Algorithm:

1. **Count Occurrences:**
   - Use a dictionary to count the occurrences of each integer in the array.

2. **Check Uniqueness:**
   - Convert the counts to a set to filter out duplicate counts and compare its length with the length of the original counts. If they match, the counts are unique.

### Code:

```python
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        c_nums = {}
        for i in arr:
            c_nums[i] = c_nums.get(i,0)+1
        return len(c_nums.values()) == len(set(c_nums.values()))
```

### Explanation:

- **Step 1:** Count the occurrences of each integer in the array using a dictionary.
- **Step 2:** Check if all counts are unique by comparing the length of the dictionary values with the length of the set created from these values.

### Complexity:

- **Time Complexity:** `O(n)`, where `n` is the length of the array, as we iterate through the array once.
- **Space Complexity:** `O(m)`, where `m` is the number of distinct elements in the array, as space is used for storing counts and their frequencies.

---

### Example Usage:

```python
if __name__ == "__main__":
    arr = [1,2,2,1,1,3]
    solution = Solution()
    result = solution.uniqueOccurrences(arr)
    print(result)  # Output will be true
```

---
