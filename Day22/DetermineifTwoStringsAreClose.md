## Day 22 Of 75 Leet Code


# LeetCode Challenge - Problem 1657: Determine if Two Strings Are Close

## Problem Statement:

Two strings are considered close if you can attain one from the other using the following operations:

1. **Swap any two existing characters.**  
   Example: `"abcde" -> "aecdb"`

2. **Transform every occurrence of one existing character into another existing character, and do the same with the other character.**  
   Example: `"aacabb" -> "bbcbaa"` (all `a`s turn into `b`s, and all `b`s turn into `a`s).

You can use these operations on either string as many times as necessary.

Given two strings, `word1` and `word2`, return `true` if `word1` and `word2` are close, and `false` otherwise.

### Examples:

**Example 1:**

```python
Input: word1 = "abc", word2 = "bca"
Output: true
Explanation: You can attain word2 from word1 in 2 operations.
Apply Operation 1: "abc" -> "acb"
Apply Operation 1: "acb" -> "bca"
```

**Example 2:**

```python
Input: word1 = "a", word2 = "aa"
Output: false
Explanation: It is impossible to attain word2 from word1, or vice versa, in any number of operations.
```

**Example 3:**

```python
Input: word1 = "cabbba", word2 = "abbccc"
Output: true
Explanation: You can attain word2 from word1 in 3 operations.
Apply Operation 1: "cabbba" -> "caabbb"
Apply Operation 2: "caabbb" -> "baaccc"
Apply Operation 2: "baaccc" -> "abbccc"
```

---

## Solution Approach

### Algorithm:

1. **Frequency Dictionary:**
   - Use two dictionaries to count the frequency of each character in both `word1` and `word2`.
   
2. **Set Comparison:**
   - Convert the keys (unique characters) of both frequency dictionaries into sets and compare them. If the sets don’t match, return `false`.

3. **Frequency Matching:**
   - Convert the frequency values into lists and compare them by checking if all frequency values in `word1` are present in `word2` and vice versa. If not, return `false`.

4. **Return True:**
   - If both the unique character sets and their frequency distributions match, return `true`.

### Code:

```python
from collections import defaultdict

class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        freq_dict1 = defaultdict(int)
        freq_dict2 = defaultdict(int)

        if len(word1) != len(word2):
            return False

        for x in word1:
            freq_dict1[x] += 1
        for x in word2:
            freq_dict2[x] += 1
        
        freq_key1 = set(freq_dict1.keys())
        freq_key2 = set(freq_dict2.keys())

        freq_val1 = list(freq_dict1.values())
        freq_val2 = list(freq_dict2.values())
        
        if len(freq_val1) != len(freq_val2):
            return False

        for x in freq_val1:
            if x not in freq_val2:
                return False
            freq_val2.remove(x)
     
        return True if freq_key1 == freq_key2 else False
```

### Explanation:

- **Step 1:** Count the frequency of each character in both `word1` and `word2`.
- **Step 2:** Ensure that both strings have the same set of unique characters.
- **Step 3:** Ensure that the frequency of these characters can be matched between the two strings.
- **Step 4:** Return `true` if the strings can be transformed into one another; otherwise, return `false`.

### Complexity:

- **Time Complexity:** `O(n)`, where `n` is the length of the strings, as we iterate through each string to build the frequency dictionaries.
- **Space Complexity:** `O(1)`, since the extra space used is proportional to the number of unique characters, which is constant for a fixed alphabet.

---

### Example Usage:

```python
if __name__ == "__main__":
    word1 = "cabbba"
    word2 = "abbccc"
    solution = Solution()
    result = solution.closeStrings(word1, word2)
    print(result)  # Output will be True
```

---
