def maxProfit(prices):
    """
    :type prices: List[int]
    :rtype: int
    """
    maxGain = 0
    if len(prices) == 0:
        return maxGain
    minBuy = prices[0]
    for val in prices[1:]:
        tempGain = val - minBuy
        if tempGain > maxGain:
            maxGain = tempGain
        if val < minBuy:
            minBuy = val
    return maxGain

if __name__ == '__main__':
    tests = ([7, 1, 5, 3, 6, 4],[7, 6, 4, 3, 1],[34, 2, 3, 67, 23, 15])
    for test in tests:
        print(maxProfit(test))
