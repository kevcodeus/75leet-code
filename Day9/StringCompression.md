

# 75 LeetCode Challenge - Day 9

## Problem 443: String Compression

**Problem Statement:**
Given an array of characters `chars`, compress it using the following algorithm:

1. Begin with an empty string `s`.
2. For each group of consecutive repeating characters in `chars`:
   - If the group's length is 1, append the character to `s`.
   - Otherwise, append the character followed by the group's length.
3. The compressed string `s` should not be returned separately but instead be stored in the input character array `chars`. 
   - Group lengths that are 10 or longer will be split into multiple characters in `chars`.

After you are done modifying the input array, return the new length of the array.

**Constraints:**
- You must write an algorithm that uses only constant extra space.

**Example 1:**
```python
Input: chars = ["a","a","b","b","c","c","c"]
Output: Return 6, and the first 6 characters of the input array should be: ["a","2","b","2","c","3"]
Explanation: The groups are "aa", "bb", and "ccc". This compresses to "a2b2c3".
```

**Example 2:**
```python
Input: chars = ["a"]
Output: Return 1, and the first character of the input array should be: ["a"]
Explanation: The only group is "a", which remains uncompressed since it's a single character.
```

**Example 3:**
```python
Input: chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
Output: Return 4, and the first 4 characters of the input array should be: ["a","b","1","2"].
Explanation: The groups are "a" and "bbbbbbbbbbbb". This compresses to "ab12".
```

---

## Solution Approach

### Step-by-Step Explanation

1. **Initialize Variables:**
   - `idx`: Tracks the current index in the input array.
   - `res`: A list to store the compressed characters.

2. **Iterate Through the Array:**
   - Use a `while` loop to iterate through the characters in the `chars` array.
   - For each character, count consecutive occurrences and append the character and its count (if greater than 1) to `res`.

3. **Handle Edge Cases:**
   - If the last character group has only one occurrence, append it directly to `res`.

4. **Update the Input Array:**
   - Clear the original `chars` array and update it with the compressed characters from `res`.

5. **Return Result:**
   - Return the length of the updated `chars` array.

---

## Code with Detailed Explanation

```python
class Solution:
    def compress(self, chars: List[str]) -> int:
        idx = 0
        res = []
        while idx < len(chars) - 1:
            c = 1
            while idx + 1 < len(chars) and chars[idx] == chars[idx + 1]:
                c += 1
                idx += 1
            if c == 1:
                res.append(chars[idx])
            else:
                res.append(chars[idx])
                res += list(str(c))
            idx += 1
        if idx == len(chars) - 1:
            res.append(chars[idx])
        chars.clear()
        for i in res:
            chars.append(i)
```

### Breakdown of the Code:

1. **Class Definition and Method:**
   ```python
   class Solution:
       def compress(self, chars: List[str]) -> int:
           idx = 0
           res = []
   ```
   - The `compress` method is defined within the `Solution` class.
   - `idx` is initialized to 0, and `res` is an empty list to store the compressed characters.

2. **Iterating and Compressing:**
   - The loop checks each character and counts how many times it repeats consecutively.
   - If a character repeats, it is followed by its count in the `res` list.

3. **Handling Edge Cases:**
   - The final character is added to the result list `res` to handle cases where the loop ends with a single character.

4. **Updating the Input Array:**
   - The original `chars` array is cleared and updated with the compressed characters from `res`.

5. **Returning the New Length:**
   - The function returns the length of the updated `chars` array.

### Example Usage

To run the solution, you can use the following code snippet:

```python
if __name__ == "__main__":
    chars = list(input("Enter the characters separated by spaces: ").split())
    solution = Solution()
    length = solution.compress(chars)
    print(f"Compressed array: {chars}")
    print(f"New length: {length}")
```

- This snippet takes input from the user for the array `chars`.
- Creates an instance of the `Solution` class.
- Calls the `compress` method with the input array.
- Prints the compressed array and its new length.

