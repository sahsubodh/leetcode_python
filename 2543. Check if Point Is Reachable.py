'''
2543. Check if Point Is Reachable
There exists an infinitely large grid. You are currently at point (1, 1), and you need to reach the point (targetX, targetY) using a finite number of steps.

In one step, you can move from point (x, y) to any one of the following points:

(x, y - x)
(x - y, y)
(2 * x, y)
(x, 2 * y)
Given two integers targetX and targetY representing the X-coordinate and Y-coordinate of your final position, return true if you can reach the point from (1, 1) using some number of steps, and false otherwise.

 

Example 1:

Input: targetX = 6, targetY = 9
Output: false
Explanation: It is impossible to reach (6,9) from (1,1) using any sequence of moves, so false is returned.
Example 2:

Input: targetX = 4, targetY = 7
Output: true
Explanation: You can follow the path (1,1) -> (1,2) -> (1,4) -> (1,8) -> (1,7) -> (2,7) -> (4,7).
 

Constraints:

1 <= targetX, targetY <= 109
'''

class Solution:

    def isReachable(self, targetX: int, targetY: int) -> bool:
        g = gcd(targetX, targetY)
        return g & (g - 1) == 0 # check g is power of 2

    def isReachable2(self, targetX: int, targetY: int) -> bool:
        while targetX % 2 == 0: 
            targetX //= 2
        while targetY % 2 == 0: 
            targetY //= 2

        return gcd(targetX, targetY) == 1
        
    def isReachable1(self, x: int, y: int) -> bool:
        return (
            True if x == 1 and y == 1 else
            self.isReachable(x / 2, y) if x % 2 == 0 else
            self.isReachable(x, y / 2) if y % 2 == 0 else
            self.isReachable(x - y, y) if x > y else
            self.isReachable(x, y - x) if y > x else False
        )
     