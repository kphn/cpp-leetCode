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
        res = ListNode(0)
        carry = 0
        p = res
        p1 = l1
        p2 = l2
        while p1 or p2:
            v1=v2=0
            if p1:v1=p1.val
            if p2:v2=p2.val
            digit = v1 + v2 + carry
            p.next = ListNode(digit%10)
            carry = int(digit/10)
            if p1:p1 = p1.next
            if p2:p2 = p2.next
            p = p.next
        if carry==1:
            p.next = ListNode(1)
        return res.next
    
    def pp(self,l):
        while l:
            print l.val
            l = l.next
l1 = ListNode(1)
l2 = ListNode(2)
l4= ListNode(4)
l3 = ListNode(3)
l5 = ListNode(5)
L6 = ListNode(6)
l4 = ListNode(4)
l8=ListNode(8)
l0=ListNode(0)
l2.next = l4
l4.next = l3
#l5.next = L6
L6.next = l4

l1.next=l8

s = Solution()
s.pp(s.addTwoNumbers(l5,l5))
            