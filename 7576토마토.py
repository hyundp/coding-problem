import sys

flag = True

def main():
    global flag
    m, n = map(int, sys.stdin.readline().split())
    graph = []
    for _ in range(n):
        graph.append(list(map(int, sys.stdin.readline().split())))
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    
    def spread(x,y,visited):
        global flag
        if graph[y][x] == 1:
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                
                if nx < 0 or ny < 0 or nx > m-1 or ny > n-1:
                    continue
                
                if graph[ny][nx] == 0:
                    graph[ny][nx] = 1
                    flag = True
                    visited.append((nx,ny))
    
    cnt = -1
    while(flag):
        visited = []
        flag = False        
        for i in range(m):
            for j in range(n):
                if (i,j) not in visited:
                    spread(i,j,visited)
        cnt+=1
        
    if any(0 in g for g in graph):
        print(-1)
    else:
        print(cnt)
            
    
if __name__=='__main__':
    main()