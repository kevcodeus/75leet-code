

# 75-Day LeetCode Challenge - Day 20

## Problem 2215: Find the Difference of Two Arrays

### Problem Statement:

Given two 0-indexed integer arrays `nums1` and `nums2`, return a list `answer` of size 2 where:

- `answer[0]` is a list of all distinct integers in `nums1` which are not present in `nums2`.
- `answer[1]` is a list of all distinct integers in `nums2` which are not present in `nums1`.

Note that the integers in the lists may be returned in any order.

### Examples:

**Example 1:**

```python
Input: nums1 = [1,2,3], nums2 = [2,4,6]
Output: [[1,3],[4,6]]
Explanation:
For nums1, nums1[1] = 2 is present in nums2, whereas nums1[0] = 1 and nums1[2] = 3 are not present in nums2. Therefore, answer[0] = [1,3].
For nums2, nums2[0] = 2 is present in nums1, whereas nums2[1] = 4 and nums2[2] = 6 are not present in nums1. Therefore, answer[1] = [4,6].
```

**Example 2:**

```python
Input: nums1 = [1,2,3,3], nums2 = [1,1,2,2]
Output: [[3],[]]
Explanation:
For nums1, nums1[2] and nums1[3] are not present in nums2. Since nums1[2] == nums1[3], their value is only included once and answer[0] = [3].
Every integer in nums2 is present in nums1. Therefore, answer[1] = [].
```

### Solution Approach

1. **Convert Lists to Sets:**
   - Convert `nums1` and `nums2` to sets to handle unique elements and simplify the difference operation.

2. **Find Unique Elements:**
   - Compute the difference between the sets to get elements in `nums1` not in `nums2` and vice versa.

3. **Format the Output:**
   - Return the results as a list of lists where each list contains distinct elements not present in the other array.

### Code:

```python
class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        n1 = set(nums1)
        n2 = set(nums2)
        r1 = list(set(x for x in nums1 if x not in n2))
        r2 = list(set(x for x in nums2 if x not in n1))
        return [r1, r2]
```

### Explanation:

- **Step 1:** Convert `nums1` and `nums2` to sets to eliminate duplicates and facilitate quick membership checks.
- **Step 2:** Use list comprehensions to identify elements in each list that are not present in the other.
- **Step 3:** Return the results in the required format.


