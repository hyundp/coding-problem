import sys
from collections import deque
import copy

def main():
    n = int(sys.stdin.readline().rstrip())
    graph = []
    m = -1
    
    for n_ in range(n):
        temp = list(map(int, sys.stdin.readline().split()))
        for n__ in range(n):
            if temp[n__] > m:
                m = temp[n__]
        graph.append(temp)
        
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    
    
    def bfs(x,y,rain,graph):
        if graph[x][y] <= rain:
            return 0
        q = deque()
        q.append((x,y))
        
        while(q):
            x,y = q.popleft()
            
            for i in range(4):
                nx = x+dx[i]
                ny = y+dy[i]
                
                if nx < 0 or ny < 0 or nx > n-1 or ny > n-1:
                    continue
                
                if graph[nx][ny] > rain:
                    graph[nx][ny] = rain
                    q.append((nx,ny))
        return 1
    
    last = 0
    r = 0
    while(r<m):
        result = 0
        g = copy.deepcopy(graph)
        for i in range(n):
            for j in range(n):
                result += bfs(i,j,r,g)
        
        if result > last:
            last = result        
        r += 1
        
    print(last)
    
if __name__=='__main__':
    main()