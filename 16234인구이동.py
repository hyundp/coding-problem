import sys

def main():
    n, l, r = map(int, sys.stdin.readline().split())
    
    graph = [[] for _ in range(n)]
    visited = [[]]
    
    for i in range(n):
        graph[i] = list(map(int, sys.stdin.readline().split()))
        
    
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    
    
    def dfs(x, y, cnt, total):
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            
            if nx < 0 or ny < 0 or nx > n-1 or ny > n-1:
                continue
            
            diff = abs(graph[nx][ny] - graph[x][y])
            
            if (diff >= l) and (diff <= r):
                cnt+=1
                total += graph[nx][ny]
                dfs(nx,ny,cnt,total)
                
    for i in range(n):
        for j in range(n):
            dfs(i,j,0,graph[i][j])
                
                
    
    
if __name__== '__main__':
    main()
    