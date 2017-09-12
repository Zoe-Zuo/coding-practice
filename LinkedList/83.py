# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head==None:
            return None
        if head.next==None:
            return head
        if head.val==head.next.val:
            head=self.deleteDuplicates(head.next)
        else: 
            head.next=self.deleteDuplicates(head.next)
        return head