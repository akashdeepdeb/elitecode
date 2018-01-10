# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def recursiveHelper(self, root, start, end, nums):
        if start == end:
            return
        mx_idx = nums.index(max(nums[start:end]))
        rt = TreeNode(max(nums[start:end]))
        rt.left = self.recursiveHelper(rt.left, start, mx_idx, nums)
        rt.right = self.recursiveHelper(rt.right, mx_idx+1, end, nums)
        return rt
        
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        return self.recursiveHelper(None, 0, len(nums), nums)