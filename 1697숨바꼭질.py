import sys
from collections import deque

def main():
    n, k = map(int, sys.stdin.readline().split())
    q = deque()
    q.append((n,0))
    shortest = [1e10]*100001
    
    while(q):
        x, distance = q.popleft()
        dx = [-1,1,x]
        if x == k:
            print(distance)
            return
        for i in range(3):
            nx = x+dx[i]
            if nx < 0 or nx > 100000:
                continue
            if shortest[nx] > distance + 1:
                shortest[nx] = distance + 1
                q.append((nx,shortest[nx]))
            
    
if __name__=='__main__':
    main()