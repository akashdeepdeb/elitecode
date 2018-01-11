class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        aux = [0,1]
        if num == 0:
            return [0]
        if num == 1:
            return aux
        for i in range(2, num+1):
            if i & (i-1) == 0:
                sub = i
            aux.append(aux[i-sub]+1)
        return aux
        