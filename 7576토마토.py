import sys
from collections import deque

def main():

    m, n = map(int, sys.stdin.readline().split())
    graph = []
    start = deque()
    for a in range(n):
        temp = list(map(int, sys.stdin.readline().split()))
        for b in range(m):
            if temp[b] == 1:
                start.append((a,b))
        graph.append(temp)
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    result = -1
    
    while(start):
        x,y = start.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < 0 or ny < 0 or nx > n-1 or ny > m-1:
                continue
        
            if graph[nx][ny] == 0:
                graph[nx][ny] = graph[x][y]+1
                if result < graph[nx][ny]:
                    result = graph[nx][ny]
                start.append((nx,ny))
                    
    for g in graph:
        if 0 in g:
            print(-1)
            return
    if result > 0: # 2차원 배열에서 전체 최댓값을 찾는 방법은 max(max(graph))가 아니라 그냥 돌면서 max값을 찾는 것이다.
        print(result-1)
    else:
        print(0)
            

if __name__=='__main__':
    main()