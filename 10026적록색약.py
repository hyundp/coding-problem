import sys
import heapq

def main():
    n = int(sys.stdin.readline())
    graph = []
    for _ in range(n):
        graph.append(list(map(str, sys.stdin.readline().rstrip())))
    q=[]
    heapq.heappush(q, (0,(0,0)))
    
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    
    result = []
    visited = [[False]*n for _ in range(n)]
    visited[0][0] = True
    cnt = 0
    while(q):
        pri,(x,y) = heapq.heappop(q)
        print(pri,x,y,graph[x][y])
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < 0 or ny < 0 or nx > n-1 or ny > n-1:
                continue
            
            if visited[nx][ny] == True:
                continue
            
            if graph[nx][ny] == graph[x][y]:
                cnt+=1
                heapq.heappush(q, (0,(nx,ny)))
            else:
                if cnt != 0:
                    result.append(cnt)
                cnt = 0
                heapq.heappush(q, (1,(nx,ny)))
            visited[nx][ny] = True
        print(q)
            
    if cnt != 0:
        result.append(cnt)
    print(result)
        
    print(len(result))
        
    
    
if __name__=='__main__':
    main()