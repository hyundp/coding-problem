import sys
from collections import deque
import math

def main():
    n, l, r = map(int, sys.stdin.readline().split())
    
    graph = [[] for _ in range(n)]
    # visited = [[0 for _ in range(n)] for _ in range(n)]
    
    
    for i in range(n):
        graph[i] = list(map(int, sys.stdin.readline().split()))
        

    def bfs(x,y):
        q = deque()
        q.append((x,y))
        dx = [-1,1,0,0]
        dy = [0,0,-1,1]
        total = graph[x][y]
        cnt = 1
        nei_list = [(x,y)]
        visited[x][y] = 1
        
        while(q):
            x, y = q.popleft()
            for i in range(4):
                nx = dx[i] + x
                ny = dy[i] + y
                if nx < 0 or ny < 0 or nx > n-1 or ny > n-1:
                    continue
                
                if visited[nx][ny] == 1:
                    continue
                
                diff = abs(graph[nx][ny] - graph[x][y])
                
                if (diff >= l) and (diff <= r):
                    cnt+=1
                    total += graph[nx][ny]
                    # visited가 여기가 아니라, 방문 후 체크라면 중복 방문하는 경우가 생김
                    # 왜냐하면 방문하기 전까지 다른 곳에서 제한없이 방문할 수 있기 때문
                    visited[nx][ny] = 1
                    q.append((nx,ny))
                    nei_list.append((nx,ny))
        return cnt, total, nei_list
    t = 0
    while(True):
        visited = [[0]*n for _ in range(n)]
        flag = False
        for i in range(n):
            for j in range(n):
                if visited[i][j] == 1:
                    continue
                cnt, total, nei_list = bfs(i,j)
                new_po = math.trunc(total / cnt)
                if cnt > 1:
                    flag = True
                    for nei in nei_list:
                        graph[nei[0]][nei[1]] = new_po
        if flag == False:
            break
        t+=1
    print(t)
                
    
    
if __name__== '__main__':
    main()
    