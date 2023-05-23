import sys

sys.setrecursionlimit(10**6)


cnt = 0
m,n = map(int, sys.stdin.readline().split())
visited = [[0 for _ in range(n)]for _ in range(m)]

def main():
    graph = []
    for _ in range(m):
        graph.append(list(map(int, sys.stdin.readline().split())))
        
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    
    if m == 1 and n == 1:
        print(1)
        return
    
    if graph[m-2][n-1] > graph[m-1][n-1]:
        visited[m-2][n-1] = 1
    if graph[m-1][n-2] > graph[m-1][n-1]:
        visited[m-1][n-2] = 1
    
    
    def dfs(x,y):
        global cnt
        global visited
        
        # print(x,y)
        # print(visited)
        
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            
            if nx < 0 or ny < 0 or nx > m-1 or ny > n-1:
                continue
        
            if graph[nx][ny] < graph[x][y]:
                if visited[nx][ny] != 0:
                    visited[x][y] += visited[nx][ny]
                    continue
                dfs(nx,ny)
                visited[x][y] += visited[nx][ny]
    
    if visited[m-2][n-1] == 1 or visited[m-1][n-2] == 1:
        dfs(0,0)             
    
    # print(visited)
    print(visited[0][0])
    
    
if __name__=='__main__':
    main()