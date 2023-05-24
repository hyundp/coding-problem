import sys

sys.setrecursionlimit(10**6)

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
    
    def dfs(x,y):
        global visited
        
        # print(x,y)
        # print(visited)
        
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            
            if nx < 0 or ny < 0 or nx > m-1 or ny > n-1:
                continue
        
            if graph[nx][ny] < graph[x][y]:
                if (nx,ny) == (m-1,n-1): #끝점에 인접한 두개의 지점이 1개 이상의 경로를 가질 수 있기 때문
                    visited[x][y] += 1
                    continue
                if visited[nx][ny] > 0:
                    visited[x][y] += visited[nx][ny]
                    continue
                dfs(nx,ny)
                visited[x][y] += visited[nx][ny]
        if visited[x][y] == 0: #그 점을 다 탐색했는데 길이 없다면, 높게 만들어서 다시 방문하지 않게 만듦
            graph[x][y] = 1e6
    
    dfs(0,0)             
    
    # print(visited)
    print(visited[0][0])
    
    
if __name__=='__main__':
    main()