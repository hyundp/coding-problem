import sys

sys.setrecursionlimit(10**6)

def main():
    
    n,m = map(int, sys.stdin.readline().split())
    graph = [[]for _ in range(n+1)]
    start = []
    visited = [False]*(n+1)
    cnt = 0
    for _ in range(m):
        a, b = map(int, sys.stdin.readline().split())
        start.append(a)
        graph[a].append(b)
        graph[b].append(a)
    def dfs(x):
        visited[x] = True
        for g in graph[x]:
            if visited[g] == False:
                dfs(g)
    for i in start:
        if visited[i] == False:
            dfs(i)
            cnt+=1
    if cnt == 0:
        print(1)
        return
    print(cnt)
    
    
if __name__=='__main__':
    main()