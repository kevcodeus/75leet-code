# 75 LeetCode Challenge - Day 6

## Problem 151: Reverse Words in a String

**Problem Statement:**
Given an input string `s`, reverse the order of the words. A word is defined as a sequence of non-space characters. The words in `s` will be separated by at least one space.

Return a string of the words in reverse order concatenated by a single space. Note that `s` may contain leading or trailing spaces or multiple spaces between two words. The returned string should only have a single space separating the words. Do not include any extra spaces.

**Example 1:**
```python
Input: s = "the sky is blue"
Output: "blue is sky the"
```

**Example 2:**
```python
Input: s = "  hello world  "
Output: "world hello"
```
**Explanation:** Your reversed string should not contain leading or trailing spaces.

**Example 3:**
```python
Input: s = "a good   example"
Output: "example good a"
```
**Explanation:** You need to reduce multiple spaces between two words to a single space in the reversed string.

---

## Solution Approach

### Step-by-Step Explanation

1. **Split the String:**
   - Use the `split` method to divide the string into words. This handles multiple spaces by default and removes leading/trailing spaces.

2. **Reverse the Words:**
   - Reverse the list of words using slicing (`[::-1]`).

3. **Join the Words:**
   - Use the `join` method to concatenate the reversed list of words into a single string with a single space separating the words.

---

## Code with Detailed Explanation

```python
class Solution:
    def reverseWords(self, s: str) -> str:
        # Split the string into words, handles multiple spaces and trims leading/trailing spaces
        words = s.split()[::-1]  # Split and reverse the list of words
        result = " ".join(words)  # Join the reversed list with a single space
        return result
```

### Breakdown of the Code:

1. **Class Definition and Method:**
   ```python
   class Solution:
       def reverseWords(self, s: str) -> str:
           words = s.split()[::-1]  # Split the string into words and reverse the list
           result = " ".join(words)  # Join the reversed list with a single space
           return result
   ```

2. **Splitting the String:**
   - The `split` method divides the string into words based on spaces, removing any leading or trailing spaces and handling multiple spaces between words.

3. **Reversing the List of Words:**
   - The slicing method `[::-1]` reverses the list of words.

4. **Joining the Words:**
   - The `join` method concatenates the words into a single string, with a single space between each word.

### Example Usage

To run the solution, you can use the following code snippet:

```python
if __name__ == "__main__":
    s = input("Enter the string: ")
    solution = Solution()
    result = solution.reverseWords(s)
    print(result)
```

- This snippet takes input from the user for the string `s`.
- Creates an instance of the `Solution` class.
- Calls the `reverseWords` method with the input string.
- Prints the result.
