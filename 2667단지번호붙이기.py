import sys
import heapq

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
    
    q = []
    heapq.heappush(q, (0,(0,0)))
    
    visited = [(0,0)]
    
    house = []
    parent = [[[] for _ in range(n)] for _ in range(n)] # 2차원 빈배열을 초기화하려면 이렇게 해야한다. 
    # parent = [[0]*n for _ in range(n)] -> 이 방식은 2차원이지만 빈 배열이 아닐때 초기화 하는 방법이다.
    cnt = 0
    
    while(q):
        _, point = heapq.heappop(q)
        x, y = point
        
        if graph[x][y] == 1:
            if parent[x][y] == 1:
                cnt += 1
            else:
                if cnt == 1:
                    house.append(cnt)
                else:
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
                parent[nx][ny] = graph[x][y]
            else:
                heapq.heappush(q, (1,(nx,ny)))
            visited.append((nx,ny))

    if cnt != 0:
        house.append(cnt)
    
    house.sort()
    print(len(house))
    for i in range(len(house)):
        print(house[i])
    
    
            
if __name__=='__main__':
    main()