import sys

sys.setrecursionlimit(10**6)

def main():
    
    n,m = map(int, sys.stdin.readline().split()) # 간선이 없다고 노드가 존재하지 않는게 아님. 따라서 1~n의 노드 모두 존재
    graph = [[]for _ in range(n+1)]
    visited = [False]*(n+1)
    cnt = 0
    for _ in range(m):
        a, b = map(int, sys.stdin.readline().split())
        graph[a].append(b)
        graph[b].append(a)
    def dfs(x):
        visited[x] = True
        for g in graph[x]:
            if visited[g] == False:
                dfs(g)
    for i in range(1,n+1):
        if visited[i] == False:
            dfs(i)
            cnt+=1
    print(cnt)
    
    
if __name__=='__main__':
    main()