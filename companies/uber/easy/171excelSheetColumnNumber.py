class Solution:
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        colsum = 0
        for i, val in enumerate(s[::-1]):
            colsum += 26**i * (ord(val)-64)
        return colsum
