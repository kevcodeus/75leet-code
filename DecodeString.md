

# Decode String (LeetCode 394)

## Problem Description

**Difficulty:** Medium

The problem requires decoding a string that is encoded in a specific format. The encoding rule is `k[encoded_string]`, where the `encoded_string` inside the square brackets is repeated exactly `k` times. 

Given a string `s`, return the decoded string.

### Example Scenarios

1. **Example 1:**
   - **Input:** `s = "3[a]2[bc]"`
   - **Output:** `"aaabcbc"`

2. **Example 2:**
   - **Input:** `s = "3[a2[c]]"`
   - **Output:** `"accaccacc"`

3. **Example 3:**
   - **Input:** `s = "2[abc]3[cd]ef"`
   - **Output:** `"abcabccdcdcdef"`

## Solution Explanation

This solution uses a stack-based approach to decode the string. The stack is used to manage the characters and numbers as we traverse through the encoded string. 

### Steps:
1. Traverse the string character by character.
2. Push all characters except `]` onto the stack.
3. When encountering `]`, start popping from the stack to build the encoded substring and repeat it according to the number preceding it.
4. Push the decoded string back onto the stack and continue until the string is fully decoded.

### Python Code:

```python
class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        for c in s:
            if c != ']':
                stack.append(c)
            else:
                res = ''
                while stack[-1] != '[':
                    res += stack.pop()
                stack.pop()
                n = ''
                while stack and stack[-1].isdigit():
                    n += stack.pop()
                stack.append(res * int(n[::-1]))

        return ''.join([word[::-1] for word in stack])
```

