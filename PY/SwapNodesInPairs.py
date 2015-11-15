# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        p = head
        while p and p.next:
            p.val,p.next.val = p.next.val,p.val
            p = p.next.next
        return head
    def printli(self,node):
        while node:
            print node.val
            node = node.next

l = ListNode(1)
l.next = ListNode(2)
l.next.next = ListNode(3)
l.next.next.next = ListNode(4)

s = Solution()
s.printli(s.swapPairs(l))