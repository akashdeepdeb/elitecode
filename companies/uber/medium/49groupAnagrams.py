class Solution:
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        anagmap = {}
        for s in strs:
            new = ''.join(sorted(s))
            anagmap[new] = anagmap.get(new, []) + [s]
        return list(anagmap.values())
        
