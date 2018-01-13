# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def recurse(self, root, h):
        if root is None:
            return
        self.recurse(root.left, h+1)
        self.recurse(root.right, h+1)
        if h > self.md:
            self.md = h
            self.ans = root.val
        
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.md = 0
        self.ans = root.val
        self.recurse(root, 0)
        return self.ans
        