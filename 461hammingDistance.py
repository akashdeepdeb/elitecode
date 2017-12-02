def hammingDistance(x, y):
    """
    :type x: int
    :type y: int
    :rtype: int
    """
    '''
    #naive solution
    dist = 0
    while x != 0 or y != 0:
        if not((x%2 == 0 and y%2 == 0) or (x%2 != 0 and y%2 != 0)):
            dist+=1
        x = int(x/2)
        y = int(y/2)
    return dist
    '''
    return bin(x^y).count('1')

if __name__ == '__main__':
    print(hammingDistance(1,4))
