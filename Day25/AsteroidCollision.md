
#  Asteroid Collision (LeetCode 735)

## Problem Description

This problem involves simulating the collision of asteroids moving in a row. Each asteroid has:
- **Size**: Represented by the absolute value.
- **Direction**: Indicated by the sign (positive for right, negative for left).

Asteroids move at the same speed and may collide:
- When two asteroids collide, the smaller one explodes.
- If both asteroids are of equal size, they both explode.
- Asteroids moving in the same direction will never meet.

### Examples

#### Example 1:
```python
Input: asteroids = [5, 10, -5]
Output: [5, 10]
Explanation: 
- The asteroid 10 and -5 collide, resulting in 10.
- The asteroids 5 and 10 do not collide.
```

#### Example 2:
```python
Input: asteroids = [8, -8]
Output: []
Explanation: 
- The asteroids 8 and -8 collide, causing both to explode.
```

#### Example 3:
```python
Input: asteroids = [10, 2, -5]
Output: [10]
Explanation: 
- The asteroid 2 and -5 collide, resulting in -5.
- The asteroid 10 and -5 collide, resulting in 10.
```

---

## Approach

To solve this problem, we can use a **stack** data structure to simulate the collisions:

1. **Iterate through each asteroid**:
   - If the asteroid is moving to the right (`>0`), push it onto the stack.
   - If the asteroid is moving to the left (`<0`):
     - Check for collisions with the top asteroid on the stack (moving right).
     - Resolve the collision based on the sizes of the colliding asteroids.
     - If the left-moving asteroid survives, push it onto the stack.

2. The stack will contain the final state of the asteroids after all possible collisions.

### Code Implementation

```python
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for asteroid in asteroids:
            if asteroid > 0:
                stack.append(asteroid)
            else:
                while stack and stack[-1] > 0:
                    if stack[-1] + asteroid == 0:
                        stack.pop()
                        break
                    if stack[-1] + asteroid < 0:
                        stack.pop()
                        continue
                    else:
                        break
                else:
                    stack.append(asteroid)
        return stack
```

