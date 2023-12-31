'''
1448. Count Good Nodes in Binary Tree
https://leetcode.com/problems/count-good-nodes-in-binary-tree/

Given a binary tree root, a node X in the tree is named good if in the path from root to X there are no nodes with a value greater than X.

Return the number of good nodes in the binary tree.

Example 1:


Input: root = [3,1,4,3,null,1,5]
Output: 4
Explanation: Nodes in blue are good.
Root Node (3) is always a good node.
Node 4 -> (3,4) is the maximum value in the path starting from the root.
Node 5 -> (3,4,5) is the maximum value in the path
Node 3 -> (3,1,3) is the maximum value in the path.
Example 2:



Input: root = [3,3,null,4,2]
Output: 3
Explanation: Node 2 -> (3, 3, 2) is not good, because "3" is higher than it.
Example 3:

Input: root = [1]
Output: 1
Explanation: Root is considered as good.
 

Constraints:

The number of nodes in the binary tree is in the range [1, 10^5].
Each node's value is between [-10^4, 10^4].
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        stack = [(root, float("-inf"))]
        res = 0
        while stack:
            node, max_so_far = stack.pop()
            if max_so_far <= node.val:
                res += 1
            if node.left:
                stack.append((node.left,max(node.val,max_so_far)))
            if node.right:
                stack.append((node.right,max(node.val,max_so_far)))     

        return res           

    def goodNodes1(self, root: TreeNode) -> int:
        res = 0
        def dfs(node,maxVal):
            if node is None:
                return 0
            res = 1 if node.val >= maxVal else 0
            maxVal = max(maxVal,node.val)
            res += dfs(node.left,maxVal)
            res += dfs(node.right,maxVal)
            
            return res
        return dfs(root,root.val)