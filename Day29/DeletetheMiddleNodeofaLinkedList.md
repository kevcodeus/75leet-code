

# Delete the Middle Node of a Linked List (LeetCode 2095) - Python Solution

## Problem Description

You are given the head of a linked list. The task is to delete the middle node and return the head of the modified linked list.

The middle node of a linked list of size `n` is the `⌊n / 2⌋`th node from the start using 0-based indexing, where `⌊x⌋` denotes the largest integer less than or equal to `x`.

### Example 1:
- **Input:** `head = [1, 3, 4, 7, 1, 2, 6]`
- **Output:** `[1, 3, 4, 1, 2, 6]`
- **Explanation:** The linked list has 7 nodes, and the middle node is the 3rd node (with value 7). This node is removed, resulting in the modified linked list.

### Example 2:
- **Input:** `head = [1, 2, 3, 4]`
- **Output:** `[1, 2, 4]`
- **Explanation:** The linked list has 4 nodes, and the middle node is the 2nd node (with value 3). This node is removed, resulting in the modified linked list.

### Example 3:
- **Input:** `head = [2, 1]`
- **Output:** `[2]`
- **Explanation:** The linked list has 2 nodes, and the middle node is the 1st node (with value 1). This node is removed, leaving only one node in the linked list.

## Solution

The solution involves finding the middle node of the linked list using a two-pointer technique. The `slow` pointer moves one step at a time, while the `fast` pointer moves two steps at a time. When the `fast` pointer reaches the end of the list, the `slow` pointer will be at the middle node. The middle node is then removed by adjusting the `next` pointer of the previous node.

### Steps:
1. **Edge Case Handling:** If the linked list has only one node, return `None`.
2. **Two-Pointer Technique:** Use `slow` and `fast` pointers to find the middle node.
3. **Remove Middle Node:** Adjust the `next` pointer of the previous node to skip the middle node.
4. **Return Head:** Return the head of the modified linked list.

### Code Implementation

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head.next:
            return None
        
        slow = head
        fast = head
        prev = head
        
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        
        prev.next = slow.next
        return head
```

## How to Run

To execute the solution:
1. Copy the provided code into a Python environment.
2. Create a linked list using the `ListNode` class.
3. Call the `deleteMiddle` method with the head of your linked list as the argument.
4. The method will return the head of the modified linked list.
