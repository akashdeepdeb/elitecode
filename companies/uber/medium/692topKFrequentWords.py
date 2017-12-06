class Solution:
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        mp = {}
        for word in words:
            if mp.get(word) == None:
                mp[word] = 0
            mp[word]+=1
        frequency = [[] for _ in range(len(words))]
        for element in mp:
            frequency[mp[element]].append(element)
        ans = []
        #print(frequency)
        j = 0
        for item in frequency[::-1]:
            if len(item) != 0:
                temp = sorted(item)
                ans[j:] = temp[:]
                j+=len(temp)
                if len(ans) >= k:
                    break
        return ans[0:k]
