def floodFillHelper(image, sr, sc, newColor, actualColor):
    if sr < 0 or sr > len(image)-1 or sc < 0 or sc > len(image)-1:
        return
    if image[sr][sc] == actualColor:
        image[sr][sc] = newColor
        floodFillHelper(image, sr-1, sc, newColor, actualColor)
        floodFillHelper(image, sr+1, sc, newColor, actualColor)
        floodFillHelper(image, sr, sc-1, newColor, actualColor)
        floodFillHelper(image, sr, sc+1, newColor, actualColor)
    return

'''
image sample:
[[1,1,1],
 [1,1,0],
 [1,0,1]]

'''

def floodFill(image, sr, sc, newColor):
    """
    :type image: List[List[int]]
    :type sr: int
    :type sc: int
    :type newColor: int
    :rtype: List[List[int]]
    """
    if newColor == image[sr][sc] or sr < 0 or sr > len(image)-1 or sc < 0 or sc > len(image[0])-1:
        return image
    floodFillHelper(image, sr, sc, newColor, image[sr][sc])
    return image


if __name__ == '__main__':
    print(floodFill(image = [[1,1,1],[1,1,0],[1,0,1]], sr = 1, sc = 1, newColor = 2))
