'''
250. Count Univalue Subtrees
Given the root of a binary tree, return the number of uni-value 
subtrees
.

A uni-value subtree means all nodes of the subtree have the same value.
Example 1:


Input: root = [5,1,5,5,5,null,5]
Output: 4
Example 2:

Input: root = []
Output: 0
Example 3:

Input: root = [5,5,5,5,5,null,5]
Output: 6
 

Constraints:

The number of the node in the tree will be in the range [0, 1000].
-1000 <= Node.val <= 1000
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countUnivalSubtrees(self, root: Optional[TreeNode]) -> int:
        def dfs(node,count):
            if not node:
                return True
            
            leftUniVal = dfs(node.left, count)
            rightUniVal = dfs(node.right, count)

            if leftUniVal and rightUniVal:
                if node.left and node.val != node.left.val:
                    return False
                if node.right and node.val != node.right.val:
                    return False                    
                self.count += 1
                return True
            return False
        
        self.count = 0
        dfs(root,count)
        return self.count
        
