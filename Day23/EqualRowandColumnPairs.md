# Day 23

# LeetCode Challenge - Problem 2352: Equal Row and Column Pairs

## Problem Description

Given a 0-indexed `n x n` integer matrix `grid`, the task is to find the number of pairs `(r_i, c_j)` such that row `r_i` and column `c_j` are equal.

A row and column pair is considered equal if they contain the same elements in the same order.

### Examples

#### Example 1:

**Input:**

```python
grid = [[3,2,1],
        [1,7,6],
        [2,7,7]]
```

**Output:** `1`

**Explanation:**  
There is 1 equal row and column pair:  
- (Row 2, Column 1): `[2, 7, 7]`

#### Example 2:

**Input:**

```python
grid = [[3,1,2,2],
        [1,4,4,5],
        [2,4,2,2],
        [2,4,2,2]]
```

**Output:** `3`

**Explanation:**  
There are 3 equal row and column pairs:  
- (Row 0, Column 0): `[3, 1, 2, 2]`  
- (Row 2, Column 2): `[2, 4, 2, 2]`  
- (Row 3, Column 2): `[2, 4, 2, 2]`

---

## Solution Approach

### Algorithm

1. **Dictionary Counting:**  
   - Traverse each row of the grid and store it as a tuple in a dictionary, counting the occurrences of each unique row.
  
2. **Column Matching:**  
   - For each column in the grid, convert it into a tuple and check if it exists in the dictionary. Count the occurrences to find matches.
  
3. **Result Calculation:**  
   - Sum up all matches to get the total number of equal row-column pairs.

### Code

```python
from collections import defaultdict
from typing import List

class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        d = defaultdict(int)
        ans = 0

        for row in grid:
            d[tuple(row)] += 1

        for col in zip(*grid):
            ans += d[tuple(col)]

        return ans
```

### Explanation

- **Dictionary Initialization:**  
  We use a dictionary (`d`) to store each row as a tuple and count its occurrences.
  
- **Row Counting:**  
  Iterate through each row of the grid, converting it into a tuple, and update the dictionary with the count of each tuple.
  
- **Column Matching:**  
  Use the `zip(*grid)` function to transpose the grid and get each column. Convert these columns into tuples and check against the dictionary to find the number of matches.

- **Return the Count:**  
  The variable `ans` accumulates the count of matches, which is then returned as the final result.

### Complexity

- **Time Complexity:** `O(n^2)` - We traverse each row and column, which takes linear time relative to the number of elements.
- **Space Complexity:** `O(n^2)` - The dictionary stores every unique row and its count, which could be up to `n^2` elements in the worst case.

---

