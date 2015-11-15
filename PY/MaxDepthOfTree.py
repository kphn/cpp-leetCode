# Definition for a binary tree node.
from idlelib.TreeWidget import TreeNode
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        :左右分支的最大深度加1
        """
        if root == None:
            return 0
        else:
            return max(self.maxDepth(root.left),self.maxDepth(root.right))+1

t = TreeNode(1)
node1 = TreeNode(2)
node2 = TreeNode(3)
node3 = TreeNode(4)
node4 = TreeNode(5)
node5 = TreeNode(6)
node6 = TreeNode(7)
t.left = node1
t.right = node2
node1.left = node3
node1.right = node4
node2.left = node5
#node3.left = node6

s = Solution()
print s.maxDepth(t)