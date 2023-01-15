from itertools import product
def maxAreaOfIsland(self, grid): # time : O(RC), space : O(RC)
    """
    :type grid: List[List[int]]
    :rtype: int
    """
    # 2D 이상에서 연결성을 찾는 문제
    n = len(grid)
    m = len(grid[0])
    res = 0
    def dfs(x, y):
        if x < 0 or y < 0 or x >= n or y >=m or grid[x][y] == 0:
            return 0 # 벗어났거나 0인경우는 disconnected
        grid[x][y] = 0 # visited 처리
        return 1 + dfs(x+1, y) + dfs(x-1, y) + dfs(x, y+1) + dfs(x, y-1) # 본인에다가 사방위 결과물들을 더해줌
    for x, y in product(range(n), range(m)):
        if grid[x][y]: # 0인건 방문할 필요가 없음
            res = max(res, dfs(x, y)) # 1인것중에 새로 만들어진 친구들로 계산해서 가장 긴거 찾음
    return res