def matrixReshape(nums, r, c):
    """
    :type nums: List[List[int]]
    :type r: int
    :type c: int
    :rtype: List[List[int]]
    """
    oldr = len(nums)
    oldc = len(nums[0])
    if r*c != oldr * oldc:
    	return nums
    ans = []
    for i in range(r):
    	ans.append([])
    	for j in range(c):
    		ans[-1].append(nums[c*i + int(j/oldc)][r*i + j%oldc])
    return ans


if __name__ == '__main__':
	tests = [([[1,2],[3,4]], 1, 4), ([[1,2],[3,4]], 2, 4), ([[1, 2, 3, 4]], 2,2), , ([[1],[2],[3],[4]], 2, 2)]
	for t in tests:
		print(matrixReshape(t[0], t[1], t[2]))

'''
m = [[1, 2, 3, 4]], 2,2
o = [[1],[2],[3],[4]], 2, 2
n = [[1 2], []]
'''