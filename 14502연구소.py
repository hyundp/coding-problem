import sys
from collections import deque
from itertools import combinations
import copy


def main():
    n,m = map(int, sys.stdin.readline().split())
    graph = []
    empty = []
    virus = []
    for i in range(n):
        temp = list(map(int, sys.stdin.readline().split()))
        for j in range(m):
            if temp[j] == 0:
                empty.append((i,j))
            elif temp[j] == 2:
              virus.append((i,j))
        graph.append(temp)

        
    result = -1
    wall = list(combinations(empty, 3))
    ori = len(empty) - 3
    for w in wall:
        temp_graph = copy.deepcopy(graph)
        for k in range(3):
            temp_graph[w[k][0]][w[k][1]] = 1
        r = bfs(virus, temp_graph, n, m, ori)
        if r > result:
            result = r
            
    print(result)
    
def bfs(virus, temp_graph, n, m, ori):
    cnt = 0
    start = deque()
    start.extend(virus)
    while(start):
        dx = [-1,1,0,0]
        dy = [0,0,-1,1]
        x,y = start.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            
            if nx < 0 or ny < 0 or nx > n-1 or ny > m-1:
                continue
            
            if temp_graph[nx][ny] == 0:
                temp_graph[nx][ny] = 2
                cnt += 1
                start.append((nx,ny))
    return ori - cnt
    
if __name__=="__main__":
    main()