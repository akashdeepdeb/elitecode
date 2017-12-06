class Solution:
    def replaceWords(self, dict, sentence):
        """
        :type dict: List[str]
        :type sentence: str
        :rtype: str
        """
        slist = sentence.split(' ')
        track = [0 for _ in range(len(slist))]
        dict.sort(key = len)
        for item in dict:
            for i, s in enumerate(slist):
                if item == s[0:len(item)] and track[i] != -1:
                    track[i] = -1
                    slist[i] = item
        return ' '.join(slist)

        
