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
    
    
    def dfs(x,y):
        global cnt
        global visited
        
        print(x,y, visited[x][y])
        print(visited)
        
        if visited[x][y] != 0:
            cnt += visited[x][y]
            return
        
        if (x,y) == (m-1,n-1):
           cnt+=1
           return
        
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if nx < 0 or ny < 0 or nx > m-1 or ny > n-1:
                continue
            if graph[nx][ny] < graph[x][y]:
                dfs(nx,ny)
        visited[x][y] += cnt             
        return
    dfs(0,0)
    print(visited[0][0])
    
    
if __name__=='__main__':
    main()