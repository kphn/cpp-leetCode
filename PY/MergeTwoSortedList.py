# Definition for singly-linked list.
from matplotlib.cbook import Null
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head = ListNode(0)
        p = head
        
        while (l1!=None and l2!=None):
            if l1.val < l2.val:
                p.next = l1
                l1 = l1.next
            else:
                p.next = l2
                l2 = l2.next
            p = p.next
        if l1!=None:p.next=l1
        if l2!=None:p.next=l2
        return head.next
def pp(l):
    while l!=None:
        print l.val
        l=l.next
    
s = Solution()
l1 = ListNode(1)
l2 = ListNode(2)
l11 = l1
l22 = l2
l11.next = ListNode(3)
l11 = l11.next
l22.next = ListNode(4)
l22=l22.next

pp(s.mergeTwoLists(l1, l2))