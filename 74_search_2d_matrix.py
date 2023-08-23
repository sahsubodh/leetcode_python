'''
74. Search a 2D Matrix
https://leetcode.com/problems/search-a-2d-matrix/
'''

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False
        
        r, c = len(matrix), len(matrix[0])
        left, right = 0, r * c - 1
        while left <= right:
            mid = (left + right) // 2
            mid_elem = matrix[mid//c][mid%c] 
            if mid_elem == target:
                return True
            if target > mid_elem:
                left = mid + 1
            else:
                right = mid - 1
        return False