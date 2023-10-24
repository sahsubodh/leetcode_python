'''
515. Find Largest Value in Each Tree Row

Given the root of a binary tree, return an array of the largest value in each row of the tree (0-indexed).

Example 1:

Input: root = [1,3,2,5,3,null,9]
Output: [1,3,9]
Example 2:

Input: root = [1,2,3]
Output: [1,3]
 

Constraints:

The number of nodes in the tree will be in the range [0, 104].
-231 <= Node.val <= 231 - 1

'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        res = []
        queue = deque([root])

        while queue:
            cur_len = len(queue)
            cur_max = float("-inf")

            for _ in range(cur_len):
                node = queue.popleft()
                cur_max = max(cur_max, node.val)

                if node.left:
                    queue.append(node.left)
                
                if node.right:
                    queue.append(node.right)
                
            res.append(cur_max)
        
        return res

    def largestValues1(self, root: Optional[TreeNode]) -> List[int]:
        def dfs(node, depth):
            if not node:
                return
            
            if depth == len(ans):
                ans.append(node.val)
            else:
                ans[depth] = max(ans[depth], node.val)
            
            dfs(node.left, depth + 1)
            dfs(node.right, depth + 1)
        
        ans = []
        dfs(root, 0)
        return ans        