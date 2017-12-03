def arrayPairSum(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    nums.sort()
    sums = 0
    for i in range(0, len(nums), 2):
        sums += nums[i]
    return sums

if __name__ == '__main__':
    print(arrayPairSum([1,2,3,2]))
