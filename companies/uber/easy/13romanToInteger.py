class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        r = {'M': 1000,'D': 500 ,'C': 100,'L': 50,'X': 10,'V': 5,'I': 1}
        z = 0
        for i in range(0, len(s) - 1):
            if r[s[i]] < r[s[i+1]]:
                z -= r[s[i]]
            else:
                z += r[s[i]]
        return z + r[s[-1]]
        #obtained from leetcode (simple solution)
