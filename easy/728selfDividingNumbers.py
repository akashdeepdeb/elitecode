def selfDividingNumbers(left, right):
    """
    :type left: int
    :type right: int
    :rtype: List[int]
    """
    selfdivnum = []
    curr = left
    while curr <= right:
        digits = list(str(curr))
        flag = 0
        if not '0' in digits:
            for digit in digits:
                if curr % int(digit) != 0:
                    flag = 1
                    break
            if not flag:
                selfdivnum.append(curr)
        curr+=1
    return selfdivnum


if __name__ == '__main__':
    print(selfDividingNumbers(1,22))
