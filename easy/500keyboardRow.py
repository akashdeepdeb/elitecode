first = 'qwertyuiop'
second = 'asdfghjkl'
third = 'zxcvbnm'
value = {first:1,second:2,third:3}

def findWords(words):
    """
    :type words: List[str]
    :rtype: List[str]
    """
    ans = []
    for word in words:
        oldwordval = 0
        wordval = 0
        flag = 0
        for letter in word:
            letter = letter.lower()
            oldwordval = wordval
            if letter in first:
                wordval = value[first]
            elif letter in second:
                wordval = value[second]
            elif letter in third:
                wordval = value[third]
            if oldwordval != 0 and (oldwordval != wordval):
                flag = 1
                break
        if not flag:
            ans.append(word)
    return ans

if __name__ == '__main__':
    print(findWords(["Hello", "Alaska", "Dad", "Peace"]))
    #return value: ["Alaska", "Dad"]
