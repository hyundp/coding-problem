import sys
import heapq
# from queue import PriorityQueue
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
                

    # p = PriorityQueue()
    # p.put((0,(0,0)))
    normal = bfs(graph,n)
    weakness = bfs(graph2,n)
    
    print(normal, weakness)
        
def bfs(graph, n):
    q=[]
    heapq.heappush(q, (0,(0,0,0)))
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    visited = [[False]*n for _ in range(n)]
    visited[0][0] = True
    result = []
    bx,by = 0,0
    cnt = 0
    while(q):
        pri,(_,x,y) = heapq.heappop(q)
        # pri,(x,y) = p.get()
        # print(x,y,graph[x][y])
        if graph[x][y] == graph[bx][by]:
            cnt+=1
        else:
            result.append(cnt)
            cnt = 1
            
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < 0 or ny < 0 or nx > n-1 or ny > n-1:
                continue
            
            if visited[nx][ny] == True:
                continue
            
            if graph[nx][ny] == graph[x][y]:
                heapq.heappush(q, (0,(_+1,nx,ny)))
                # p.put((0,(nx,ny)))
            else:
                heapq.heappush(q, (1,(_+1,nx,ny)))
            visited[nx][ny] = True
        bx, by = x,y
        # print(q)
            
    if cnt != 0:
        result.append(cnt)
    # print(result)
        
    return (len(result))    
    
if __name__=='__main__':
    main()