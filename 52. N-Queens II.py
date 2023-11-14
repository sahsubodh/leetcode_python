'''
52. N-Queens II
The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.

Given an integer n, return the number of distinct solutions to the n-queens puzzle.

 

Example 1:


Input: n = 4
Output: 2
Explanation: There are two distinct solutions to the 4-queens puzzle as shown.
Example 2:

Input: n = 1
Output: 1
 

Constraints:

1 <= n <= 9
'''

class Solution:
    def totalNQueens(self, n: int) -> int:
        answer = 0

        cols = set()
        posdiag = set()
        negdiag = set()

        def backtrack(i):
            if i == n:
                nonlocal answer
                answer += 1
                return
            
            for j in range(n):
                if j in cols or (i+j) in posdiag or (i-j) in negdiag:
                    continue

                cols.add(j)
                posdiag.add(i+j)
                negdiag.add(i-j)

                backtrack(i+1)
                
                cols.remove(j)
                posdiag.remove(i+j)
                negdiag.remove(i-j)
        
        backtrack(0)
        return answer