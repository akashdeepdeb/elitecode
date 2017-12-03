def findComplement(num):
    """
    :type num: int
    :rtype: int
    """
    opp = ''
    for bit in bin(num)[2:]:
        opp += str(1-int(bit))
    return int(opp, 2)

if __name__ == '__main__':
    print(findComplement(43))
