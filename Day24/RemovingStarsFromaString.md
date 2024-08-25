

# Removing Stars From a String (LeetCode 2390)

## Problem Statement

You are given a string `s`, which contains stars (`*`). In one operation, you can:

- Choose a star in `s`.
- Remove the closest non-star character to its left, as well as remove the star itself.

Return the string after all stars have been removed.

**Note:**

- The input will be generated such that the operation is always possible.
- It can be shown that the resulting string will always be unique.

### Examples

**Example 1:**

```python
Input: s = "leet**cod*e"
Output: "lecoe"
Explanation: 
- The closest character to the 1st star is 't' in "leet**cod*e". s becomes "lee*cod*e".
- The closest character to the 2nd star is 'e' in "lee*cod*e". s becomes "lecod*e".
- The closest character to the 3rd star is 'd' in "lecod*e". s becomes "lecoe".
There are no more stars, so we return "lecoe".
```

**Example 2:**

```python
Input: s = "erase*****"
Output: ""
Explanation: 
- The closest characters to the stars are 'e', 'r', 'a', 's', 'e'. The string becomes empty.
```

---

## Solution Approach

### Algorithm:

1. **Stack Utilization:**
   - Initialize an empty stack to keep track of the characters in the string.
   - Traverse through each character in the string `s`:
     - If the character is a star (`*`), pop the last character from the stack (this represents removing the closest non-star character to the left).
     - If the character is not a star, push it onto the stack.
   - After processing all characters, the stack will contain the final string without any stars.

2. **Return the Result:**
   - Join the characters remaining in the stack to form the final result string.

### Code Implementation:

```python
class Solution: 
    def removeStars(self, s: str) -> str:
        stack = []
        for ch in s: 
            if ch == '*': 
                stack.pop()
            else: 
                stack.append(ch)
        return ''.join(stack)
```

### Explanation:

- **Step 1:** Iterate over each character in the string `s`.
- **Step 2:** Use the stack to manage the removal of characters as stars are encountered.
- **Step 3:** Join the characters left in the stack to get the resulting string after all operations.

### Complexity Analysis:

- **Time Complexity:** `O(n)`, where `n` is the length of the string `s`. We process each character once.
- **Space Complexity:** `O(n)`, as we use a stack to store the characters in the worst case.

---

