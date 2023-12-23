'''
606. Construct String from Binary Tree
Given the root of a binary tree, construct a string consisting of parenthesis and integers from a binary tree with the preorder traversal way, and return it.

Omit all the empty parenthesis pairs that do not affect the one-to-one mapping relationship between the string and the original binary tree.

 

Example 1:


Input: root = [1,2,3,4]
Output: "1(2(4))(3)"
Explanation: Originally, it needs to be "1(2(4)())(3()())", but you need to omit all the unnecessary empty parenthesis pairs. And it will be "1(2(4))(3)"
Example 2:


Input: root = [1,2,3,null,4]
Output: "1(2()(4))(3)"
Explanation: Almost the same as the first example, except we cannot omit the first parenthesis pair to break the one-to-one mapping relationship between the input and the output.
 

Constraints:

The number of nodes in the tree is in the range [1, 104].
-1000 <= Node.val <= 1000
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#https://leetcode.com/problems/construct-string-from-binary-tree/solutions/2542372/python-solution-using-recursion-with-explanation/?envType=daily-question&envId=2023-12-08

class Solution:

    def tree2str(self, root: Optional[TreeNode]) -> str:
        
        string = str(root.val)
        if root.left: 
            string += "(" + self.tree2str(root.left) + ")"
        if root.right: 
            if not root.left: string += "()"
            string += "(" + self.tree2str(root.right) + ")"
        return string

    def tree2str1(self, root: Optional[TreeNode]) -> str:
        if not root: return ""

        res = ""
        stack = [root]

        while stack:

            node = stack.pop()

            if node == ")":
                res += ")"
                continue

            res +=  "(" + str(node.val)

            if not node.left and node.right:
                res += "()"
            
            if node.right:
                stack.append(")")
                stack.append(node.right)
            if node.left:
                stack.append(")")
                stack.append(node.left)                        

        return res[1:]