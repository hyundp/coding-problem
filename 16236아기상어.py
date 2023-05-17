import sys
import heapq

def main(): # O(n*n*n^2logn^2)
    
    n = int(sys.stdin.readline().rstrip())
    graph=[]
    start = (0,0)
    for i in range(n):
        temp = list(map(int, sys.stdin.readline().split()))
        for j in range(n):
            if temp[j] == 9:
                start = (i,j)
        graph.append(temp)
    dx = [-1,0,1,0]
    dy = [0,-1,0,1]

    
    
    def bfs(x,y,size):
        shortest = [[1e6]*n for _ in range(n)]
        q = []
        heapq.heappush(q, (0,x,y,size))
        shortest[x][y] = 0
    
        while(q):
            time,x,y,size = heapq.heappop(q)
            
            if graph[x][y] != 0 and graph[x][y] < size:
                graph[x][y] = 0
                return x, y, time
            
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                
                if nx<0 or ny < 0 or nx > n-1 or ny > n-1:
                    continue        
                
                if graph[nx][ny] > size:
                    continue
                
                if time+1 < shortest[nx][ny]:
                    shortest[nx][ny] = time+1
                    heapq.heappush(q, (time+1,nx,ny,size))
        return x,y,0
    
    cnt = 0
    size = 2
    flag = True
    result = 0
    x,y = start
    graph[x][y] = 0
    while(flag):
        x,y,t = bfs(x,y,size)
        if t != 0:
            cnt += 1
            if cnt == size:
                cnt = 0
                size += 1
            result+=t
        else:
            flag = False
    print(result)
    
if __name__=='__main__':
    main()