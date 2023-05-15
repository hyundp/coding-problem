import sys
from collections import deque

def main(): # O(n^3)
    n = int(sys.stdin.readline().rstrip())
    graph = [[]for _ in range(n)]
    for i in range(n):
        temp = list(map(int, sys.stdin.readline().split()))
        for j in range(n):
            if temp[j] == 1:
                graph[i].append(j)
        
    result = [[0 for _ in range(n)] for _ in range(n)]
    
    for j in range(n):
        q = deque(graph[j])
        while(q):
            x = q.popleft()
            if result[j][x] == 0:
                result[j][x] = 1                
                q.extend(graph[x]) # deque는 안에 리스트가 들어있는 형태, 그 안에 리스트를 추가하려면 extend가 맞다.
    
    for r1 in range(n):
        for r2 in range(n):
            print(result[r1][r2], end=' ')
        print()
    
if __name__=='__main__':
    main()