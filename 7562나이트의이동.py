import sys
import heapq

def main():
    I = int(sys.stdin.readline().rstrip())
    start = tuple(map(int, sys.stdin.readline().split()))
    end = tuple(map(int, sys.stdin.readline().split()))
    
    dx = [-1,-1,-2,-2,1,1,2,2]
    dy = [2,-2,1,-1,2,-2,1,-1]
    q = []
    heapq.heappush(q, (0,start))
    shortest = [[1e10 for _ in range(I)] for _ in range(I)]
    while(q):
        dist,(x,y) = heapq.heappop(q)
        
        if (x,y) == end:
            print(dist)
            return
        
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < 0 or ny < 0 or nx > I-1 or ny > I-1:
                continue
            if shortest[nx][ny] > dist + 1:
                shortest[nx][ny] = dist+1
                heapq.heappush(q, (dist+1, (nx,ny)))
            
if __name__=='__main__':
    n = int(sys.stdin.readline().rstrip())
    for _ in range(n):
        main()