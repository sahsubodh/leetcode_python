'''
1293. Shortest Path in a Grid with Obstacles Elimination
You are given an m x n integer matrix grid where each cell is either 0 (empty) or 1 (obstacle). You can move up, down, left, or right from and to an empty cell in one step.

Return the minimum number of steps to walk from the upper left corner (0, 0) to the lower right corner (m - 1, n - 1) given that you can eliminate at most k obstacles. If it is not possible to find such walk return -1.

 

Example 1:


Input: grid = [[0,0,0],[1,1,0],[0,0,0],[0,1,1],[0,0,0]], k = 1
Output: 6
Explanation: 
The shortest path without eliminating any obstacle is 10.
The shortest path with one obstacle elimination at position (3,2) is 6. Such path is (0,0) -> (0,1) -> (0,2) -> (1,2) -> (2,2) -> (3,2) -> (4,2).
Example 2:


Input: grid = [[0,1,1],[1,1,1],[1,0,0]], k = 1
Output: -1
Explanation: We need to eliminate at least two obstacles to find such a walk.
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 40
1 <= k <= m * n
grid[i][j] is either 0 or 1.
grid[0][0] == grid[m - 1][n - 1] == 0
'''

class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:

        rows, cols = len(grid), len(grid[0])
        target = (rows - 1, cols - 1)

        def manhattan_distance(row, col):
            return target[0] - row + target[1] - col

        # (row, col, remaining_elimination)
        state = (0, 0, k)

        # (estimation, steps, state)
        # h(n) = manhattan distance,  g(n) = 0
        queue = [(manhattan_distance(0, 0), 0, state)]
        seen = set([state])

        while queue:
            estimation, steps, (row, col, remain_eliminations) = heapq.heappop(queue)

            # we can reach the target in the shortest path (manhattan distance),
            #   even if the remaining steps are all obstacles
            remain_min_distance = estimation - steps
            if remain_min_distance <= remain_eliminations:
                return estimation

            # explore the four directions in the next step
            for new_row, new_col in [(row, col + 1), (row + 1, col), (row, col - 1), (row - 1, col)]:
                # if (new_row, new_col) is within the grid boundaries
                if (0 <= new_row < rows) and (0 <= new_col < cols):
                    new_eliminations = remain_eliminations - grid[new_row][new_col]
                    new_state = (new_row, new_col, new_eliminations)

                    # if the next direction is worth exploring
                    if new_eliminations >= 0 and new_state not in seen:
                        seen.add(new_state)
                        new_estimation = manhattan_distance(new_row, new_col) + steps + 1
                        heapq.heappush(queue, (new_estimation, steps + 1, new_state))

        # did not reach the target
        return -1