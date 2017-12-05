def isPalindrome(s):
    """
    :type s: str
    :rtype: bool
    """
    s_new = ''
    for ch in s:
        if ch.isalnum():
            s_new += ch.lower()
    if s_new == s_new[::-1]:
        return True
    return False

if __name__ == '__main__':
    tests = ("A man, a plan, a canal: Panama", "race a car")
    for test in tests:
        print(isPalindrome(test))
