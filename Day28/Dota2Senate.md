
# Dota2 Senate (LeetCode 649) - Python Solution

## Problem Description

In the world of Dota2, there are two parties: the Radiant and the Dire.

The Dota2 senate consists of senators coming from these two parties. The Senate wants to decide on a change in the Dota2 game through a round-based voting procedure. During each round, a senator can either:
- **Ban** another senator's rights, preventing them from voting in this and all future rounds.
- **Announce Victory** if all remaining senators belong to the same party.

Given a string `senate` representing the party of each senator, with 'R' indicating Radiant and 'D' indicating Dire, the task is to predict which party will eventually announce the victory.

### Example 1:
- **Input:** `senate = "RD"`
- **Output:** `"Radiant"`
- **Explanation:** The first senator bans the rights of the second senator. The Radiant party wins.

### Example 2:
- **Input:** `senate = "RDD"`
- **Output:** `"Dire"`
- **Explanation:** The first senator bans the rights of the second senator. The last senator, belonging to Dire, announces victory.

## Solution

The solution to this problem involves simulating the voting process using a deque (double-ended queue). The key idea is to keep track of the senators in the order they will vote, while removing the rights of the opposing party's senators as the process continues.

### Steps:
1. **Deque Initialization:** Store all senators in a deque.
2. **Voting Simulation:** Iteratively process each senator, removing the rights of the next senator from the opposing party.
3. **Determine Winner:** The process continues until only one party remains in the deque, at which point the victory is declared.

### Code Implementation

```python
from collections import deque

class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        Q = deque(senate)
        while len(Q) > 1:
            s = Q.popleft()
            try:
                Q.remove('R' if s == 'D' else 'D')
                Q.append(s)
            except ValueError:
                pass
        return "Dire" if Q.pop() == "D" else "Radiant"
```

