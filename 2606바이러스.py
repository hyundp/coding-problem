import sys
from collections import deque

def main():
    
    n = int(sys.stdin.readline())
    m = int(sys.stdin.readline())
    
    graph = [[] for _ in range(n+1)]
    
    for _ in range(m):
        a, b = map(int, sys.stdin.readline().split())
        graph[a].append(b)
        graph[b].append(a)
    
    q = deque()
    q.append(1)
    visited = [1]
    cnt = 0
    
    while(q):
        cur = q.popleft()
        
        for i in graph[cur]:
            if i not in visited:
                visited.append(i)
                q.append(i)
                cnt += 1
                
    print(cnt)
                
    
    
    
if __name__=="__main__":
    main()