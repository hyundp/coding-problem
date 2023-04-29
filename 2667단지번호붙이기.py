import sys
import heapq

# 반례
# 5
# 10101
# 01010
# 10101
# 01010
# 10101

def main():
    n = int(sys.stdin.readline())
    
    graph = []
    for _ in range(n):
        graph.append(list(map(int, sys.stdin.readline().rstrip())))
        
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    
    q = []
    heapq.heappush(q, (0,(0,0)))
    
    visited = [(0,0)]
    
    house = []
    cnt = 0
    
    while(q):
        _, point = heapq.heappop(q)
        x, y = point
        
        if graph[x][y] == 1:
            cnt += 1
        else:
            if cnt != 0:
                house.append(cnt)
            cnt = 0
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < 0 or nx > n-1 or ny < 0 or ny > n-1:
                continue
            
            if (nx,ny) in visited:
                continue
            
            if graph[nx][ny] == 1:
                heapq.heappush(q, (0,(nx,ny)))
            else:
                heapq.heappush(q, (1,(nx,ny)))
            visited.append((nx,ny))
    
    house.sort()
    print(len(house))
    for i in range(len(house)):
        print(house[i])
    
    
            
if __name__=='__main__':
    main()