def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    m1 = {}
    for i in nums:
        if m1.get(i) == None:
            m1[i]=0
        m1[i]+=1
    for i in nums:
        curr = target - i
        if curr == i and m1[i] >= 2:
            return [i for i,j in enumerate(nums) if j == curr]
        if curr != i and m1.get(curr, None) != None:
            return [nums.index(i), nums.index(curr)]

if __name__ == '__main__':
    print(twoSum([2, 7, 11, 15], 9))
