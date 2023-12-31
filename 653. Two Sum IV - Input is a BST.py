'''
653. Two Sum IV - Input is a BST
Given the root of a binary search tree and an integer k, return true if there exist two elements in the BST such that their sum is equal to k, or false otherwise.

 

Example 1:


Input: root = [5,3,6,2,4,null,7], k = 9
Output: true
Example 2:


Input: root = [5,3,6,2,4,null,7], k = 28
Output: false
 

Constraints:

The number of nodes in the tree is in the range [1, 104].
-104 <= Node.val <= 104
root is guaranteed to be a valid binary search tree.
-105 <= k <= 105
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget1(self, root: Optional[TreeNode], k: int) -> bool:
        def dfs(root, seen):
            if root == None: return False
            complement = k - root.val
            if complement in seen: return True
            seen.add(root.val)
            return dfs(root.left, seen) or dfs(root.right, seen)
        
        return dfs(root, set())

    def findTarget(self, root: TreeNode, k: int) -> bool:
        if not root:
            return False
        queue, seen = deque([root]),set()
        while queue:
            cur = queue.popleft()
            if cur.val in seen:
                return True
            else:
                seen.add(k-cur.val)
                if cur.left: queue.append(cur.left)
                if cur.right: queue.append(cur.right)
        return False        
