import sys
import heapq

def main():
    
    
    n,m = map(int, sys.stdin.readline().split())
    shortest = [[1e6 for _ in range(m)]for _ in range(n)]
    graph = []
    start = []
    for k in range(n):
        temp = list(map(int, sys.stdin.readline().rstrip()))
        for g in range(m):
            if temp[g] == 1:
                start.append((k,g))
        
        graph.append(temp)
    
    def bfs():
        q = []
        heapq.heappush(q, (0, 0,0)) # heaq로 좌표 넣을 때는 그냥 이렇게 풀어 써도 됨.
        dx = [-1,1,0,0]
        dy = [0,0,-1,1]
        
        while(q):
            dist,x,y = heapq.heappop(q)
            if dist > shortest[x][y]:
                continue
            
            if (x,y) == (n-1,m-1):
                return
            
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                
                if nx < 0 or ny < 0 or nx > n-1 or ny > m-1:
                    continue
                
                if graph[nx][ny] == 0:
                    if dist+1 < shortest[nx][ny]:
                        shortest[nx][ny] = dist+1
                        heapq.heappush(q, (dist+1,nx,ny))
        
    for s in start:
        graph[s[0]][s[1]] = 0
        bfs()
        graph[s[0]][s[1]] = 1
                
    
    if shortest[n-1][m-1] == 1e6:
        print(-1)
    else:
        print(shortest[n-1][m-1]+1)


    
if __name__=='__main__':
    main()