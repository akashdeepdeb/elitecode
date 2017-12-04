def wordPattern(pattern, string):
    """
    :type pattern: str
    :type str: str
    :rtype: bool
    """
    '''
    map1 = {}
    map2 = {}
    stringlist = string.split(' ')
    if len(pattern) != len(stringlist): return False
    for i, element in enumerate(pattern):
        if map1.get(element, None) != map2.get(stringlist[i], None):
            return False
        map1[element] = i+1
        map2[stringlist[i]] = i+1
    return True
    '''
    stringlist = string.split()
    return len(set(zip(stringlist, pattern))) == len(set(stringlist)) == len(set(pattern)) and len(stringlist) == len(pattern)

if __name__ == '__main__':
    testcases = [["abba", "dog cat cat dog"], ["abba", "dog cat cat fish"], ["aaaa", "dog cat cat dog"], ["abba", "dog dog dog dog"], ["abc", "b c a"]]
    for test in testcases:
        print(wordPattern(test[0], test[1]))
