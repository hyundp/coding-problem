import sys
from collections import deque
import copy

def main():
    n = int(sys.stdin.readline())
    graph = []
    graph2 = []
    for _ in range(n):
        temp = list(map(str, sys.stdin.readline().rstrip()))
        graph.append(temp)
        
        temp2 = copy.deepcopy(temp)
        for i in range(len(temp2)):
            if temp2[i] == 'G':
                temp2[i] = 'R'
        graph2.append(temp2)
                
    result1 = 0
    result2 = 0
    for a in range(n):
        for b in range(n):
            result1 += bfs(a,b,graph,n)
            result2 += bfs(a,b,graph2,n)
            
    
    print(result1, result2)
        
def bfs(x,y,graph, n):
    if graph[x][y] == 'X':
        return 0
    simbol = graph[x][y]
    q=deque()
    q.append((x,y))
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    graph[x][y] = 'X'
    while(q):
        x,y = q.popleft()
            
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < 0 or ny < 0 or nx > n-1 or ny > n-1:
                continue
            
            if graph[nx][ny] == simbol:
                q.append((nx,ny))
                graph[nx][ny] = 'X'
    return 1
    
if __name__=='__main__':
    main()