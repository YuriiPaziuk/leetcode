# https://leetcode.com/problems/reverse-linked-list/description/

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        new_list = None
        t = None
        while head:
            t = head
            head = head.next
            t.next = new_list
            new_list = t
        return new_list