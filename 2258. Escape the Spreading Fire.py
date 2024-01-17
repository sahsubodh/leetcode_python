'''
2258. Escape the Spreading Fire

You are given a 0-indexed 2D integer array grid of size m x n which represents a field. Each cell has one of three values:

0 represents grass,
1 represents fire,
2 represents a wall that you and fire cannot pass through.
You are situated in the top-left cell, (0, 0), and you want to travel to the safehouse at the bottom-right cell, (m - 1, n - 1). Every minute, you may move to an adjacent grass cell. After your move, every fire cell will spread to all adjacent cells that are not walls.

Return the maximum number of minutes that you can stay in your initial position before moving while still safely reaching the safehouse. If this is impossible, return -1. If you can always reach the safehouse regardless of the minutes stayed, return 109.

Note that even if the fire spreads to the safehouse immediately after you have reached it, it will be counted as safely reaching the safehouse.

A cell is adjacent to another cell if the former is directly north, east, south, or west of the latter (i.e., their sides are touching).

 

Example 1:


Input: grid = [[0,2,0,0,0,0,0],[0,0,0,2,2,1,0],[0,2,0,0,1,2,0],[0,0,2,2,2,0,2],[0,0,0,0,0,0,0]]
Output: 3
Explanation: The figure above shows the scenario where you stay in the initial position for 3 minutes.
You will still be able to safely reach the safehouse.
Staying for more than 3 minutes will not allow you to safely reach the safehouse.
Example 2:


Input: grid = [[0,0,0,0],[0,1,2,0],[0,2,0,0]]
Output: -1
Explanation: The figure above shows the scenario where you immediately move towards the safehouse.
Fire will spread to any cell you move towards and it is impossible to safely reach the safehouse.
Thus, -1 is returned.
Example 3:


Input: grid = [[0,0,0],[2,2,0],[1,2,0]]
Output: 1000000000
Explanation: The figure above shows the initial grid.
Notice that the fire is contained by walls and you will always be able to safely reach the safehouse.
Thus, 109 is returned.
 

Constraints:

m == grid.length
n == grid[i].length
2 <= m, n <= 300
4 <= m * n <= 2 * 104
grid[i][j] is either 0, 1, or 2.
grid[0][0] == grid[m - 1][n - 1] == 0
'''

class Solution:
    def maximumMinutes(self, A: List[List[int]]) -> int:
        m, n = len(A), len(A[0])
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        ppl_time = [[-1] * n for _ in range(m)]
        fire_time = [[-1] * n for _ in range(m)]
        
        # BFS for people's arrival for each cell.
        ppl_front = collections.deque([(0, 0, 0)])
        while ppl_front:
            cx, cy, days = ppl_front.popleft()
            ppl_time[cx][cy] = days
            for dx, dy in dirs:
                nx, ny = cx + dx, cy + dy
                if 0 <= nx < m and 0 <= ny < n and A[nx][ny] == 0 and ppl_time[nx][ny] == -1:
                    ppl_front.append((nx, ny, days + 1))
        
        
        # BFS for fire's arrival for each cell.
        fire_front = collections.deque([(x, y, 0) for x in range(m) for y in range(n) if A[x][y] == 1])
        while fire_front:
            cx, cy, days = fire_front.popleft()
            fire_time[cx][cy] = days
            for dx, dy in dirs:
                nx, ny = cx + dx, cy + dy
                if 0 <= nx < m and 0 <= ny < n and A[nx][ny] == 0 and fire_time[nx][ny] == -1:
                    fire_front.append((nx, ny, days + 1))
        
        # Check the arrival days for the bottom-right cell.
        ppl_arrival = ppl_time[-1][-1]
        fire_arrival = fire_time[-1][-1]
        
        # Some edge cases.
        if ppl_arrival == -1:
            return -1
        if fire_arrival == -1:
            return 10 ** 9
        if fire_arrival < ppl_arrival:
            return -1

        # Whether we are 'followed' by fire on both two pathes toward bot-right cell.
        diff = fire_arrival - ppl_arrival
        ppl_1, ppl_2 = ppl_time[-1][-2], ppl_time[-2][-1]
        
        fire_1, fire_2 = fire_time[-1][-2], fire_time[-2][-1]
        if ppl_1 > -1 and ppl_2 > -1 and (fire_1 - ppl_1 > diff or fire_2 - ppl_2 > diff):
            return diff
        return diff - 1