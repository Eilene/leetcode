# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        l = ListNode(0)
        carry = 0
        if l1:
            l.val = l1.val+l.val
        if l2:
            l.val = l.val+l2.val
        if(l.val>9):
            carry = 1
            l.val = l.val-10
        l1 = l1.next
        l2 = l2.next
        head = l
        while l1 or l2 :
            l.next = ListNode(0)
            l = l.next
            if(l1):
                l.val = l1.val
                l1 = l1.next
            if(l2):
                l.val = l.val+l2.val
                l2 = l2.next
            l.val = l.val+carry
            carry = 0
            if (l.val > 9):
                carry = 1
                l.val = l.val - 10
        if(carry):
            l.next = ListNode(carry)

        return head

