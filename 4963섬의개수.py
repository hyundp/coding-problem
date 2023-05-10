import sys
from collections import deque

def main():
    
    w, h = map(int,sys.stdin.readline().split())
    if w == 0 and h == 0:
        return False
    graph = []
    for _ in range(h):
        graph.append(list(map(int, sys.stdin.readline().split())))
    
    dx = [-1,1,0,0,-1,1,-1,1]
    dy = [0,0,-1,1,-1,1,1,-1]
    
    def bfs(x,y):
        
        if graph[x][y] == 0:
            return 0
        graph[x][y] = 0
        q = deque()
        q.append((x,y))
        
        while(q):
            x,y = q.popleft()
            for i in range(8):
                nx = x+dx[i]
                ny = y+dy[i]
                
                if nx < 0 or ny < 0 or nx > h-1 or ny > w-1:
                    continue
                
                if graph[nx][ny] == 1:
                    graph[nx][ny] = 0
                    q.append((nx,ny))
    
        return 1
    
    result = 0
    for h_ in range(h):
        for w_ in range(w):
            result += bfs(h_,w_)
    print(result)
    return True
    
if __name__=='__main__':
    flag = True
    while(flag):
        flag = main()
        