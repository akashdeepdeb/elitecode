def isHappy(n):
    """
    :type n: int
    :rtype: bool
    """
    num = n
    while True:
        sums = 0
        for i in str(num):
            sums += int(i)**2
        num = sums
        if num == 1:
            return True
        if num >= 2 and num <= 6:
            return False

if __name__ == '__main__':
    ans = [34, 19, 1, 45]
    for num in ans:
        print(isHappy(num))
