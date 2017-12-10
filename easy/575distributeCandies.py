def distributeCandies(candies):
        """
        :type candies: List[int]
        :rtype: int
        """
        # ctyp = {}
        # each = int(len(candies)/2)
        # ctyp = {candy:ctyp.get(candy, 0)+1 for candy in candies}
        # return each if len(ctyp) >= each else len(ctyp)
        return min(int(len(candies)/2),len(set(candies)))
        
        
if __name__ == '__main__':
	tests = [[1,1,2,2,3,3], [1,1,2,3]]
	for test in tests:
		print(distributeCandies(test))