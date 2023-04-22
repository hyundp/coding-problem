import sys
from collections import deque

def main():
    
    n, m, v = map(int, sys.stdin.readline().split())
    dfs_visited = [False]*(n+1)
    bfs_visited = [False]*(n+1)
    
    graph = [[] for _ in range(n+1)]
    for _ in range(m):
        a,b = map(int, sys.stdin.readline().split())
        graph[a].append(b)
        graph[a].sort()
        graph[b].append(a) # 노드 연결은 양방향이므로 추가해야함
        graph[b].sort() # 탐색은 작은 노드부터 방문하니 그에 맞춰 정렬해줘야함
    

    
    def dfs(graph,v, visited):
        visited[v] = True
        print(v, end=" ")
        for i in graph[v]:
            if visited[i] == False:
                dfs(graph, i, visited) # 재귀 함수 특성으로 인해 끝까지 간 뒤 돌아오면서 실행됨.
                

    def bfs(graph, v, visited):
        queue = deque([v])
        visited[v] = True
        
        while queue:
            cur = queue.popleft()
            print(cur, end=" ")
            for i in graph[cur]:
                if visited[i] == False:
                    visited[i] = True
                    queue.append(i)
        

    dfs(graph, v, dfs_visited)
    print()
    bfs(graph, v, bfs_visited)
    
        
if __name__=='__main__':
    main()