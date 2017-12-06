import itertools

class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if len(digits) == 0:
            return []
        digmap = {'2': ['a', 'b', 'c'], '3': ['d', 'e', 'f'],
                  '4': ['g', 'h', 'i'], '5': ['j', 'k', 'l'], '6': ['m', 'n', 'o'],
                  '7': ['p', 'q', 'r', 's'], '8': ['t', 'u', 'v'], '9': ['w', 'x', 'y', 'z']}
        req = []
        for d in digits:
            req.append(digmap[d])
        ans = []
        for element in itertools.product(*req):
            ans.append(''.join(element))
        return ans
