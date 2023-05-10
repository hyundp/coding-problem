import sys
from collections import deque

def main():
    m,n,h = map(int, sys.stdin.readline().split())
    graph = []
    q = deque()
    for h_ in range(h):
        for n_ in range(n):
            temp = list(map(int, sys.stdin.readline().split()))
            for m_ in range(m):
                if temp[m_] == 1:
                    q.append((n_,m_,h_))
            graph.append(temp)
            
    dx = [-1,1,0,0,0,0]
    dy = [0,0,-1,1,0,0]
    dz = [0,0,0,0,-1,1]
    
    while(q):
        x,y,z = q.popleft()
        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]
            
            if nx < 0 or ny < 0 or nz < 0 or nx > n-1 or ny > m-1 or nz > h-1:
                continue
            
            
            if graph[nx+nz*n][ny] == 0:
                graph[nx+nz*n][ny] = graph[x+z*n][y] + 1
                q.append((nx,ny,nz))
    
    result = -1
    
    for k in range(n*h):
        for g in range(m):
            r = graph[k][g]
            if r == 0:
                print(-1)
                return
            if r > result:
                result = r
                
    print(result-1)
                

if __name__=='__main__':
    main()