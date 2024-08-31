
# Odd Even Linked List (LeetCode 328) - Python Solution

## Problem Description

Given the head of a singly linked list, the task is to group all nodes with odd indices together followed by the nodes with even indices, and return the reordered list. 

The challenge is to:
- Maintain O(1) extra space complexity.
- Achieve O(n) time complexity.

The first node is considered odd, the second node is even, and so on. The relative order inside both the odd and even groups should remain as it was in the input list.

### Example 1:
- **Input:** `head = [1,2,3,4,5]`
- **Output:** `[1,3,5,2,4]`

### Example 2:
- **Input:** `head = [2,1,3,5,6,4,7]`
- **Output:** `[2,3,6,7,1,5,4]`

## Solution

To solve this problem, I used two pointers to separate the odd and even indexed nodes while maintaining their relative order. The odd-indexed nodes are linked together first, followed by the even-indexed nodes.

### Steps:
1. **Initialization:** Use two pointers, one for odd nodes and one for even nodes.
2. **Traversal:** Iterate through the list, adjusting the `next` pointers to group odd and even nodes together.
3. **Reconnection:** After reordering, link the last odd node to the first even node to complete the reordered list.

### Code Implementation

```python
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next == None or head.next.next == None:
            return head
        
        odd, even = head, head.next
        pointer1, pointer2 = odd, even
        prev = None
        while pointer1 != None and pointer2 != None:
            pointer1.next = pointer2.next
            prev = pointer1
            pointer1 = pointer1.next
            if pointer1 == None:
                pointer2.next = None
            else:
                pointer2.next = pointer1.next
            pointer2 = pointer2.next
        if pointer1 == None:
            prev.next = even
        else:
            pointer1.next = even
        return odd
```

