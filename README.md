
# Problem1:Merge Strings Alternately

You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string.

Return the merged string.
## Example 1:
Input: word1 = "abc", word2 = "pqr"
Output: "apbqcr"
Explanation: The merged string will be merged as so:
word1:  a   b   c
word2:    p   q   r
merged: a p b q c r

## Example 2:
Input: word1 = "ab", word2 = "pqrs"
Output: "apbqrs"
Explanation: Notice that as word2 is longer, "rs" is appended to the end.
word1:  a   b 
word2:    p   q   r   s
merged: a p b q   r   s

## Example 3:
Input: word1 = "abcd", word2 = "pq"
Output: "apbqcd"
Explanation: Notice that as word1 is longer, "cd" is appended to the end.
word1:  a   b   c   d
word2:    p   q 
merged: a p b q c   d
 
 
# Logic of the Solution

### Initialize Variables:

Calculate the lengths of both strings, word1 and word2.
Initialize an index variable i to 0.
Create an empty list w3 to store the merged characters.
### Loop Through Characters:

Use a while loop that continues as long as i is less than the length of either string (l1 or l2).
### Within the loop:
If i is within the bounds of word1 (i < l1), append the character at index i from word1 to w3.
If i is within the bounds of word2 (i < l2), append the character at index i from word2 to w3.
Increment the index i by 1.
Return Result:

After the loop completes, join the list w3 into a single string and return it. This merged string contains characters from word1 and word2 in alternating order, with any remaining characters from the longer string appended at the end.
