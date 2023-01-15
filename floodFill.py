class Solution(object):
    def floodFill1(self, image, sr, sc, color): # time : O(n), space : O(n)
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type color: int
        :rtype: List[List[int]]
        """
        # recursion을 활용해 사방위를 모두 돌며 색을 칠해주는 방식
        # dfs의 일종
        n = len(image)
        m = len(image[0])
        first_color = image[sr][sc]
        if first_color == color:
            return image
        def fill(x, y):
            image[x][y] = color
            if x + 1 < n and image[x+1][y] == first_color:
                fill(x+1, y)
            if x - 1 >= 0 and image[x-1][y] == first_color:
                fill(x-1, y)
            if y + 1 < m and image[x][y+1] == first_color:
                fill(x, y+1)
            if y - 1 >= 0 and image[x][y-1] == first_color:
                fill(x, y-1)
        fill(sr,sc)
        return image
    
