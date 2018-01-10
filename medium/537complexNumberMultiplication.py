class Solution(object):
    def convertToParts(self, imag):
        parts = imag.split('+')
        return int(parts[0]), int(parts[1][0:-1])
    
    def complexNumberMultiply(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: str
        """
        a,b = self.convertToParts(A)
        c,d = self.convertToParts(B)
        m = str(a*c - b*d)
        n = str(a*d + b*c)
        return m+'+'+n+'i'