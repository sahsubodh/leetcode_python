'''
61. Rotate List
Given the head of a linked list, rotate the list to the right by k places.

 

Example 1:


Input: head = [1,2,3,4,5], k = 2
Output: [4,5,1,2,3]
Example 2:


Input: head = [0,1,2], k = 4
Output: [2,0,1]
 

Constraints:

The number of nodes in the list is in the range [0, 500].
-100 <= Node.val <= 100
0 <= k <= 2 * 109
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:

    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        
        if not head:
            return None
        
        lastElement = head
        length = 1
        # get the length of the list and the last node in the list
        while ( lastElement.next ):
            lastElement = lastElement.next
            length += 1

        # If k is equal to the length of the list then k == 0
        # ElIf k is greater than the length of the list then k = k % length
        k = k % length
            
        # Set the last node to point to head node
        # The list is now a circular linked list with last node pointing to first node
        lastElement.next = head
        
        # Traverse the list to get to the node just before the ( length - k )th node.
        # Example: In 1->2->3->4->5, and k = 2
        #          we need to get to the Node(3)
        tempNode = head
        for _ in range( length - k - 1 ):
            tempNode = tempNode.next
        
        # Get the next node from the tempNode and then set the tempNode.next as None
        # Example: In 1->2->3->4->5, and k = 2
        #          tempNode = Node(3)
        #          answer = Node(3).next => Node(4)
        #          Node(3).next = None ( cut the linked list from here )
        answer = tempNode.next
        tempNode.next = None
        
        return answer

    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k == 0:
            return head

        old_head = head

        curr, size = head, 0
        while curr:
            curr, size = curr.next, size + 1

        if k % size == 0:
            return head

        k %= size
        slow = fast = head
        while fast and fast.next:
            if k <= 0:
                slow = slow.next
            fast = fast.next
            k -= 1

        new_tail, new_head, old_tail = slow, slow.next, fast
        new_tail.next, old_tail.next = None, old_head

        return new_head
