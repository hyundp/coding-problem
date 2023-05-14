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

    shortest = [[[1e6 for _ in range(m)]for _ in range(n)] for _ in range(2)]

# 모든 벽을 다 돌면서 하나 씩 없애는 방법 : O((n*m)^2) -> 시간 초과 발생
# bfs 속에서 벽을 없애가며 확인해 보는 방법 : O(2*n*m)
# -> 벽을 안 부순 친구를 처리해주는 n*m matrix, 벽을 부순 친구를 처리해주는 n*m matrix가 존재하며, 벽을 부순 친구들끼리도 역시 shortest경쟁을 하기 때문에 서로 같은 matrix에 존재해야 한다.

    def bfs():
        q = []
        heapq.heappush(q, (0, 0,0, 0)) # heapq로 좌표 넣을 때는 그냥 이렇게 풀어 써도 됨.
        dx = [-1,1,0,0]
        dy = [0,0,-1,1]

        shortest[0][0][0] = 0
            
        while(q):
            dist,x,y,wall = heapq.heappop(q)
            if (x,y) == (n-1,m-1):
                return dist
            
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                
                if nx < 0 or ny < 0 or nx > n-1 or ny > m-1:
                    continue
                
                if graph[nx][ny] == 0:
                    if dist+1 < shortest[wall][nx][ny]:
                        shortest[wall][nx][ny] = dist+1
                        heapq.heappush(q, (dist+1,nx,ny,wall))
                else:
                    if wall == 0:
                        if dist+1 < shortest[1][nx][ny]:
                            shortest[1][nx][ny] = dist+1
                            heapq.heappush(q, (dist+1,nx,ny,1))
        return min(shortest[0][n-1][m-1],shortest[1][n-1][m-1])
                        

    result = bfs()
                
    if result == 1e6:
        print(-1)
    else:
        print(result+1)


    
if __name__=='__main__':
    main()