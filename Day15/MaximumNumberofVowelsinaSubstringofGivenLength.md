

# 75 LeetCode Challenge - Day 15

## Problem 1456: Maximum Number of Vowels in a Substring of Given Length

### Problem Statement:

Given a string `s` and an integer `k`, return the maximum number of vowel letters in any substring of `s` with length `k`.

Vowel letters in English are 'a', 'e', 'i', 'o', and 'u'.

### Examples:

**Example 1:**

```python
Input: s = "abciiidef", k = 3  
Output: 3  
Explanation: The substring "iii" contains 3 vowel letters.
```

**Example 2:**

```python
Input: s = "aeiou", k = 2  
Output: 2  
Explanation: Any substring of length 2 contains 2 vowels.
```

**Example 3:**

```python
Input: s = "leetcode", k = 3  
Output: 2  
Explanation: "lee", "eet", and "ode" contain 2 vowels.
```

---

## Solution Approach

### Algorithm:

1. **Initialize a Window:**
   - Start by calculating the number of vowels in the first window of length `k`.
   
2. **Sliding Window Technique:**
   - Slide the window across the string, adding the vowel count of the new character and subtracting the vowel count of the character that left the window.

3. **Max Tracking:**
   - Keep track of the maximum number of vowels found in any window.

### Code:

```python
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = 'aeiou'
        cur_v = max_v = sum([1 for x in s[:k] if x in vowels])
        
        for i in range(0, len(s) - k):
            cur_v += (s[i + k] in vowels) - (s[i] in vowels)
            if cur_v > max_v:
                max_v = cur_v
                
        return max_v
```

### Explanation:

- **Step 1:** Calculate the number of vowels in the first `k` characters of the string.
- **Step 2:** For each subsequent character, adjust the count by adding the vowel status of the new character entering the window and subtracting the vowel status of the character leaving the window.
- **Step 3:** Return the maximum vowel count encountered.

### Complexity:

- **Time Complexity:** `O(n)`, where `n` is the length of the string.
- **Space Complexity:** `O(1)`, as only constant extra space is used for counting vowels.

---

### Example Usage:

```python
if __name__ == "__main__":
    s = "abciiidef"
    k = 3
    solution = Solution()
    result = solution.maxVowels(s, k)
    print(result)  # Output will be 3
```

---

