def isAnagram(s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
    """
    m1 = {}
    m2 = {}
    if len(s) != len(t):
        return False
    for i in range(len(s)):
        if m1.get(s, None) == None:
            m1[s[i]]=0
        m1[s[i]]+=1
        if m2.get(t, None) == None:
            m2[t[i]]=0
        m2[t[i]]+=1
    return m1 == m2

if __name__ == '__main__':
    print(isAnagram('anagram','nagaram'))
