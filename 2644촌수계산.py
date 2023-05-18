import sys

sys.setrecursionlimit(10**6)
cnt = 0
flag = False

def main(): # O(N)
    
    n = int(sys.stdin.readline().rstrip())
    start, end = map(int, sys.stdin.readline().split())
    m = int(sys.stdin.readline().rstrip())
    parent = [0 for _ in range(n+1)]
    child = [[] for _ in range(n+1)]
    for _ in range(m):
        a,b = map(int, sys.stdin.readline().split())
        child[a].append(b)
        parent[b] = a
    def dfs(x):
        global cnt
        global flag
        
        if x == end:
            print(cnt)
            flag = True
            return
        
        if end in child[x]:
            print(cnt+1)
            flag = True
            return
        
        if parent[x] != 0:
            cnt+=1
            dfs(parent[x])
            
        
    
    dfs(start)
    if flag == False:
        print(-1)
    
    
    
if __name__=='__main__':
    main()