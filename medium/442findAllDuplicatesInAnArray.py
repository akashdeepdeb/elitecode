class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans = []
        for x in nums:
            if nums[abs(x)-1] < 0:
                ans.append(abs(x))
            else:
                nums[abs(x)-1] *= -1
        return ans