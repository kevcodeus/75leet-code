

# 75 LeetCode Challenge - Day 11

## Problem 392: Is Subsequence

**Problem Statement:**
Given two strings `s` and `t`, return `true` if `s` is a subsequence of `t`, or `false` otherwise.

A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters.

**Example 1:**
```python
Input: s = "abc", t = "ahbgdc"
Output: true
```

**Example 2:**
```python
Input: s = "axc", t = "ahbgdc"
Output: false
```

---

## Solution Approach

### Step-by-Step Explanation

1. **Initialization:**
   - `l`: Length of the string `s`.
   - `c`: Counter to track the number of matching characters found in sequence.

2. **Edge Case Check:**
   - If `s` is empty, immediately return `True` as an empty string is a subsequence of any string.

3. **Iterate Through `t`:**
   - For each character in `t`, check if it matches the current character in `s` that we are tracking (`s[c]`).
   - If a match is found, increment the counter `c` to move to the next character in `s`.

4. **Check Completion:**
   - If all characters in `s` are matched in sequence (i.e., `c == l`), return `True`.
   - If the loop ends without a full match, return `False`.

---

## Code Implementation

```python
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        l = len(s)
        c = 0
        if not s:
            return True
        for i in t:
            if i == s[c]:
                c += 1
            if c == l:
                break
        return l == c
```

### Explanation:

- **Edge Case Handling:** The function immediately returns `True` if `s` is an empty string.
- **Character Matching:** The loop iterates through `t`, checking for matches with the current character in `s`. If a match is found, the counter is incremented to check the next character in `s`.
- **Final Check:** After the loop, the function compares the length of `s` with the counter to determine if `s` is a subsequence of `t`.

### Example Usage

To run the solution, you can use the following code snippet:

```python
if __name__ == "__main__":
    s = "abc"
    t = "ahbgdc"
    solution = Solution()
    result = solution.isSubsequence(s, t)
    print(result)  # Output: True
```

- This snippet checks if `s` is a subsequence of `t` and prints the result.

---

