
# 75 LeetCode Challenge - Day 5

## Problem 345: Reverse Vowels of a String

**Problem Statement:**
Given a string `s`, reverse only all the vowels in the string and return it. The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

**Example 1:**
```python
Input: s = "hello"
Output: "holle"
```

**Example 2:**
```python
Input: s = "leetcode"
Output: "leotcede"
```

---

## Solution Approach

### Step-by-Step Explanation

1. **Initialize Pointers:**
   - `i`: A pointer starting at the beginning of the string.
   - `j`: A pointer starting at the end of the string.
   - Convert the string `s` to a list for easier manipulation.

2. **Check and Swap:**
   - Use a while loop that runs as long as `i` is less than `j`.
   - If both `s[i]` and `s[j]` are vowels, swap them and move both pointers towards the center.
   - If `s[i]` is a vowel but `s[j]` is not, move the `j` pointer towards the center.
   - If `s[j]` is a vowel but `s[i]` is not, move the `i` pointer towards the center.

3. **Return Result:**
   - Join the list back into a string and return the result.

---

## Code with Detailed Explanation

```python
class Solution:
    def reverseVowels(self, s: str) -> str:
        i = 0 
        j = len(s) - 1
        s = list(s)

        while i < j:
            if s[i] in "aeiouAEIOU" and s[j] in "aeiouAEIOU":
                s[i], s[j] = s[j], s[i]
                i = i + 1
                j = j - 1
            elif s[i] in "aeiouAEIOU":
                j = j - 1
            else:
                i = i + 1
        return "".join(s)
```

### Breakdown of the Code:

1. **Class Definition and Method:**
   ```python
   class Solution:
       def reverseVowels(self, s: str) -> str:
           i = 0 
           j = len(s) - 1
           s = list(s)

           while i < j:
               if s[i] in "aeiouAEIOU" and s[j] in "aeiouAEIOU":
                   s[i], s[j] = s[j], s[i]
                   i = i + 1
                   j = j - 1
               elif s[i] in "aeiouAEIOU":
                   j = j - 1
               else:
                   i = i + 1
           return "".join(s)
   ```

2. **Initialize Pointers and Convert String to List:**
   - The string `s` is converted to a list for easier manipulation.
   - Pointers `i` and `j` are initialized to the start and end of the string respectively.

3. **Swapping Vowels:**
   - The while loop checks if both `s[i]` and `s[j]` are vowels and swaps them if true.
   - The pointers are then adjusted based on whether they point to vowels or not.

4. **Final Result:**
   - The list is joined back into a string, and the result is returned and printed.

### Example Usage

To run the solution, you can use the following code snippet:

```python
if __name__ == "__main__":
    s = input("Enter the string: ")
    solution = Solution()
    result = solution.reverseVowels(s)
    print(result)
```

- This snippet takes input from the user for the string `s`.
- Creates an instance of the `Solution` class.
- Calls the `reverseVowels` method with the input string.
- Prints the result.

