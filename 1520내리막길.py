import sys

sys.setrecursionlimit(10**6)


cnt = 0
m,n = map(int, sys.stdin.readline().split())
visited = [[0 for _ in range(n)]for _ in range(m)]
flag = False

def main():
    graph = []
    
    for _ in range(m):
        graph.append(list(map(int, sys.stdin.readline().split())))
        
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]    
    
    
    def dfs(x,y):
        global cnt
        global flag
        global visited
        
        if (x,y) == (m-1,n-1):
           cnt+=1
           return 1
        
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            
            if nx < 0 or ny < 0 or nx > m-1 or ny > n-1:
                continue
            
            if graph[nx][ny] < graph[x][y]:
                if visited[nx][ny] == 1:
                    cnt+=1
                    return 1
                else:
                    flag = False
                    r = dfs(nx,ny)
                    if r == 1:
                        flag = True
                    if flag == True:
                        visited[nx][ny] = 1               
        return 0
    dfs(0,0)
    print(cnt)
    
    
if __name__=='__main__':
    main()