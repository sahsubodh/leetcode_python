'''
109. Convert Sorted List to Binary Search Tree
Given the head of a singly linked list where elements are sorted in ascending order, convert it to a 
height-balanced
binary search tree.

 

Example 1:


Input: head = [-10,-3,0,5,9]
Output: [0,-3,9,-10,null,5]
Explanation: One possible answer is [0,-3,9,-10,null,5], which represents the shown height balanced BST.
Example 2:

Input: head = []
Output: []
 

Constraints:

The number of nodes in head is in the range [0, 2 * 104].
-105 <= Node.val <= 105
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        def length(head):
            cnt = 0
            while head:
                cnt += 1
                head = head.next
            return cnt
        
        def dfs(left, right):
            nonlocal head
            if left > right: return None
            mid = (left + right) // 2
            leftNode = dfs(left, mid - 1)
            
            root = TreeNode(head.val)
            head = head.next
            
            root.left = leftNode
            root.right = dfs(mid + 1, right)
            return root
        
        return dfs(0, length(head)-1)        