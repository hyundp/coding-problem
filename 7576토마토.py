import sys
from collections import deque

flag = True

def main():
    global flag
    m, n = map(int, sys.stdin.readline().split())
    graph = []
    for _ in range(n):
        graph.append(list(map(int, sys.stdin.readline().split())))
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    start = deque()
    
    for i in range(m):
        for j in range(n):
            if graph[j][i] == 1:
                start.append((j,i))
    
    def spread(x,y,visited):
        global flag
        if graph[x][y] == 1:
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                
                if nx < 0 or ny < 0 or nx > n-1 or ny > m-1 or (nx,ny) in visited:
                    continue
                
                if graph[nx][ny] == 0:
                    graph[nx][ny] = 1
                    flag = True
                    visited.append((nx,ny))
                    start.append((nx,ny))
    
    cnt = -1
    while(flag):
        visited = []
        flag = False
        t = len(start)
        for _ in range(t):
            x,y = start.popleft()        
            spread(x,y,visited)
        cnt+=1
        
    if any(0 in g for g in graph):
        print(-1)
    else:
        print(cnt)
            
    
if __name__=='__main__':
    main()