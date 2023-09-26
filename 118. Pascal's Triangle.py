'''
118. Pascal's Triangle

Given an integer numRows, return the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

Example 1:

Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
Example 2:

Input: numRows = 1
Output: [[1]]
 

Constraints:

1 <= numRows <= 30
'''

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        l = []
        l.append([1])

        for i in range(1,numRows):
            m = []
            for j in range(i+1):
                if j == 0 or j == i:
                    m.append(1)
                else:
                    m.append(l[i-1][j-1] + l[i-1][j])
            l.append(m)
        return l
        