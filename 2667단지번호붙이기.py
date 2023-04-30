import sys
import heapq
from collections import deque

# 반례
# 5
# 10101
# 01010
# 10101
# 01010
# 10101

# 5
# 11111
# 11111
# 11111
# 11111
# 11111

def main():
    n = int(sys.stdin.readline())
    
    graph = []
    for _ in range(n):
        graph.append(list(map(int, sys.stdin.readline().rstrip())))
        
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    
    def bfs(x,y, cnt):
        
        if graph[x][y] == 0:
            return 0
        
        graph[x][y] = 0
        q = deque()
        q.append((x,y))
        
        
        while(q):
            x, y = q.popleft()
            cnt+=1
            
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                
                if nx < 0 or nx > n-1 or ny < 0 or ny > n-1:
                    continue
                
                if graph[nx][ny] == 1:
                    q.append((nx,ny))
                    graph[nx][ny] = 0
                    
        return cnt
        

    
    house = []
    for i in range(n):
        for j in range(n):
            result = bfs(i,j,0)
            if result != 0:
                house.append(result)
                
    
    house.sort()
    print(len(house))
    for i in range(len(house)):
        print(house[i])
    
    
            
if __name__=='__main__':
    main()