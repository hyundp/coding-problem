import sys
from collections import deque

def main():
    n = int(sys.stdin.readline())
    
    graph = []
    for _ in range(n):
        graph.append(list(map(int, sys.stdin.readline().rstrip())))
        
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    
    q = deque()
    q.append((0,0))
    
    visited = []
    
    house = []
    cnt = 0
    
    while(q):
        x, y = q.popleft()
        visited.append((x,y))
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < 0 or nx > n-1 or ny < 0 or ny > n-1:
                continue
            
            if graph[nx][ny] == 0 or (nx,ny) in visited:
                continue
            
            if graph[nx][ny] == 1:
                cnt += 1
                q.append((nx,ny))
        if cnt != 0:
            house.append(cnt)
            cnt = 0
if __name__=='__main__':
    main()