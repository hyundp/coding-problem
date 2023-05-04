import sys
from collections import deque

def main():

    m, n = map(int, sys.stdin.readline().split())
    graph = []
    start = deque()
    visited = []
    for a in range(n):
        temp = list(map(int, sys.stdin.readline().split()))
        for b in range(m):
            if temp[b] == 1:
                start.append((a,b))
                visited.append((a,b))
        graph.append(temp)
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    
    def spread(x,y,visited):
        if graph[x][y] == 1:
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                
                if nx < 0 or ny < 0 or nx > n-1 or ny > m-1:
                    continue
                
                if (nx,ny) in visited or graph[nx][ny] == -1:
                    continue
            
                if graph[nx][ny] == 0:
                    graph[nx][ny] = 1
                    visited.append((nx,ny))
                    start.append((nx,ny))
    
    cnt = -1
    while(start):
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