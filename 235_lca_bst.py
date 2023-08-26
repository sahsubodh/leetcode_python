'''
235. Lowest Common Ancestor of a Binary Search Tree
https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:

      def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        #question solved using 4 cases below
        
        #1.both values are less than root
        if p.val < root.val and q.val < root.val :
            return self.lowestCommonAncestor(root.left, p, q)
        
        #2.both values are greater than root
        if p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)
        
        #3.one of x or y is equal to the root
        #4.one is less than root and other is greater than root
        
        return root

        def lowestCommonAncestor1(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

            cur = root
            while cur:
                if cur.val < p.val and cur.val < q.val:
                    cur = cur.right
                elif cur.val > p.val and cur.val > q.val:
                    cur = cur.left
                else:
                    return cur
