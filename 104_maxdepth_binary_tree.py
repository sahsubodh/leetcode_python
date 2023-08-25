'''
104. Maximum Depth of Binary Tree
https://leetcode.com/problems/maximum-depth-of-binary-tree/

Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Example 1:

Input: root = [3,9,20,null,null,15,7]
Output: 3
Example 2:

Input: root = [1,null,2]
Output: 2
 

Constraints:

The number of nodes in the tree is in the range [0, 104].
-100 <= Node.val <= 100
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        res = 0
        stack = [[root,1]]
        
        while stack:
            node,depth = stack.pop()
            if node:
                res = max(res,depth)
                stack.append([node.left, depth+1])
                stack.append([node.right, depth+1])


        return res

    def maxDepth2(self, root: Optional[TreeNode]) -> int:
        res = 0

        if not root:
            return 0
        
        q = deque([root])

        while q:
            for i in range(len(q)):
                cur = q.popleft()
                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)   
            res += 1 
        return res


    def maxDepth1(self, root: Optional[TreeNode]) -> int:
        res = 0

        if not root:
            return 0

        res = 1 + max(self.maxDepth(root.left), self.maxDepth(root.right)) 

        return res