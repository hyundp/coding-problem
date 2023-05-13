import sys
import heapq

def main():
    
    n,m = map(int, sys.stdin.readline().split())
    graph = []
    start = []
    for k in range(n):
        temp = list(map(int, sys.stdin.readline().rstrip()))
        for g in range(m):
            if temp[g] == 1:
                start.append((k,g))
        
        graph.append(temp)

    shortest = [[[1e6 for _ in range(m)]for _ in range(n)] for _ in range(len(start)+1)]
    
    
    def bfs(short_):
        q = []
        heapq.heappush(q, (0, 0,0)) # heaq로 좌표 넣을 때는 그냥 이렇게 풀어 써도 됨.
        dx = [-1,1,0,0]
        dy = [0,0,-1,1]

        short_[0][0] = 0
            
        while(q):
            dist,x,y = heapq.heappop(q)
            if dist > short_[x][y]:
                continue
            
            if (x,y) == (n-1,m-1):
                return short_[n-1][m-1]
            
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                
                if nx < 0 or ny < 0 or nx > n-1 or ny > m-1:
                    continue
                
                if graph[nx][ny] == 0:
                    if dist+1 < short_[nx][ny]:
                        short_[nx][ny] = dist+1
                        heapq.heappush(q, (dist+1,nx,ny))                
        return short_[n-1][m-1]

    result = 1e6
    if start == []:
        short = bfs(shortest[0])
        if short < result:
            result = short
    else:        
        for s in range(len(start)):
            graph[start[s][0]][start[s][1]] = 0 
            short = bfs(shortest[s])           
            if short != 1e6:
                if short < result:
                    result = short
            graph[start[s][0]][start[s][1]] = 1
                
    if result == 1e6:
        print(-1)
    else:
        print(result+1)


    
if __name__=='__main__':
    main()