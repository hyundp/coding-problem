import sys

def main(): #모든점<->모든점 최단거리: 플로이드워셜 => O(N^3)
    n,m = map(int,sys.stdin.readline().split())
    graph = [[1e6 for _ in range(n)] for _ in range(n)]
    for _ in range(m):
        a,b = map(int,sys.stdin.readline().split())
        graph[a-1][b-1] = 1
        graph[b-1][a-1] = 1
    
    for i in range(n):
        graph[i][i] = 0
    
    for k in range(n):
        for i in range(n):
            for j in range(n):
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])
    
    
    result = 1e6
    idx = -1
    for g in range(n):
        r = sum(graph[g])
        if r < result:
            result = r
            idx = g+1            
                
    print(idx)
    
if __name__=='__main__':
    main()