import sys

sys.setrecursionlimit(10**6)
flag = False

def main(): # O(N)
    
    n = int(sys.stdin.readline().rstrip())
    start, end = map(int, sys.stdin.readline().split())
    m = int(sys.stdin.readline().rstrip())
    parent = [0 for _ in range(n+1)]
    child = [[] for _ in range(n+1)]
    visited = [False for _ in range(n+1)] # dfs할땐 visited 필요.
    for _ in range(m):
        a,b = map(int, sys.stdin.readline().split())
        child[a].append(b)
        parent[b] = a
    def dfs(x,cnt):
        global flag
        
        visited[x] = True
        
        if x == end:
            print(cnt)
            flag = True
            return
        
        if end in child[x]:
            print(cnt+1)
            flag = True
            return
        
        if parent[x] != 0 and visited[parent[x]] == False: # 위로 가는 경우
            dfs(parent[x],cnt+1)
        
        if child[x] != []: # 아래로 가는 경우
            for c in child[x]:
                if visited[c] == False:
                    dfs(c,cnt+1)
            
        
    dfs(start,0)
    if flag == False:
        print(-1)
    
    
    
if __name__=='__main__':
    main()