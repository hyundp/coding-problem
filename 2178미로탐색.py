import sys
from collections import deque

def main():
    # 가장 가까운 것 부터 차근차근 탐색하는 BFS를 통해 내 주변의 길을 가는 최단경로를 갱신한다.
    # 이렇게 하면 이상한 곳으로 간다하더라도 분기점까지의 거리는 고정되므로 목표까지 최단거리가 계산가능하다.
    # 첫 방문인지 아닌지는 1인지 아닌지로 확인.
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    
    n,m = map(int, sys.stdin.readline().split())
    graph = []
    for _ in range(n):
        graph.append(list(map(int, sys.stdin.readline().rstrip()))) #readline은 문자열 변환과 줄바꿈을 제거하지 않는다.
    
    # q = deque((0,0)) # deque([0,0]) 처럼 동작

    q = deque()
    q.append((0,0)) # deque([(0,0)]) 처럼 동작 -> 하나 씩 꺼내 쓰려면 이걸로 사용

    
    while(q):
        x, y = q.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
        
            if nx < 0 or nx > n-1 or ny < 0 or ny > m-1:
                continue
            if graph[nx][ny] == 0:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                q.append((nx,ny))
                
    print(graph[n-1][m-1])
        
        
    
    
if __name__ == '__main__':
    main()