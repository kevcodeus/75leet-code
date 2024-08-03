
# 75 LeetCode Challenge - Day 3

## Problem 1431: Kids With the Greatest Number of Candies

**Problem Statement:**
There are `n` kids with candies. You are given an integer array `candies`, where each `candies[i]` represents the number of candies the `i-th` kid has, and an integer `extraCandies`, denoting the number of extra candies that you have.

Return a boolean array `result` of length `n`, where `result[i]` is `true` if, after giving the `i-th` kid all the `extraCandies`, they will have the greatest number of candies among all the kids, or `false` otherwise.

**Example 1:**
```python
Input: candies = [2,3,5,1,3], extraCandies = 3
Output: [true, true, true, false, true]
```
**Explanation:**
- Kid 1: 2 + 3 = 5 (greatest)
- Kid 2: 3 + 3 = 6 (greatest)
- Kid 3: 5 + 3 = 8 (greatest)
- Kid 4: 1 + 3 = 4 (not greatest)
- Kid 5: 3 + 3 = 6 (greatest)

**Example 2:**
```python
Input: candies = [4,2,1,1,2], extraCandies = 1
Output: [true, false, false, false, false]
```
**Explanation:**
- Kid 1 will always have the greatest number of candies, even with just 1 extra candy.

**Example 3:**
```python
Input: candies = [12,1,12], extraCandies = 10
Output: [true, false, true]
```

---

## Solution Approach

### Step-by-Step Explanation

1. **Initialize Variables:**
   - `l`: Length of the `candies` list.
   - `maximum`: The maximum number of candies any kid currently has.
   - `result`: An empty list to store the boolean results.

2. **Determine the Greatest Number of Candies:**
   - Find the maximum value in the `candies` list using the `max()` function.

3. **Calculate Candies with ExtraCandies:**
   - Iterate through each kid's candies.
   - For each kid, add the `extraCandies` to their current number of candies.
   - Compare this new count to the current maximum.
   - Append `True` to `result` if the new count is greater than or equal to the maximum, otherwise append `False`.

4. **Return the Result:**
   - Return the `result` list.

---

## Code with Detailed Explanation

```python
from typing import List

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        # Step 1: Initialize variables
        l = len(candies)  # Get the number of kids
        maximum = max(candies)  # Find the maximum number of candies any kid currently has
        result = []  # Initialize an empty list to store the results

        # Step 2: Determine if each kid can have the greatest number of candies
        for i in range(l):
            value = candies[i] + extraCandies  # Add extraCandies to the current kid's candies
            if value >= maximum:  # Compare the new number of candies to the maximum
                result.append(True)  # Append True if the new count is greater than or equal to the maximum
            else:
                result.append(False)  # Append False otherwise

        return result  # Return the result list

if __name__ == "__main__":
    # User input
    candies = list(map(int, input("Enter the number of candies for each kid, separated by spaces: ").split()))
    extraCandies = int(input("Enter the number of extra candies: "))

    # Create an instance of the solution and get the result
    solution = Solution()
    result = solution.kidsWithCandies(candies, extraCandies)

    # Print the result
    print(result)
```

### Breakdown of the Code:

1. **Importing List from typing Module:**
   ```python
   from typing import List
   ```
   - This import allows us to use `List` for type hinting.

2. **Class Definition and Method:**
   ```python
   class Solution:
       def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
           l = len(candies)  # Get the number of kids
           maximum = max(candies)  # Find the maximum number of candies any kid currently has
           result = []  # Initialize an empty list to store the results

           for i in range(l):
               value = candies[i] + extraCandies  # Add extraCandies to the current kid's candies
               if value >= maximum:  # Compare the new number of candies to the maximum
                   result.append(True)  # Append True if the new count is greater than or equal to the maximum
               else:
                   result.append(False)  # Append False otherwise

           return result  # Return the result list
   ```

3. **User Input Handling:**
   ```python
   if __name__ == "__main__":
       candies = list(map(int, input("Enter the number of candies for each kid, separated by spaces: ").split()))
       extraCandies = int(input("Enter the number of extra candies: "))

       solution = Solution()
       result = solution.kidsWithCandies(candies, extraCandies)

       print(result)
   ```
   - Takes input from the user for the number of candies each kid has and the number of extra candies.
   - Creates an instance of the `Solution` class and prints the result.

---
