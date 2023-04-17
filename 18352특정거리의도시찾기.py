import sys
import heapq

def main():
    n,m,k,x = map(int, sys.stdin.readline().split())
    
    graph = [[] for _ in range(n+1)]
    for _ in range(m):
        a, b = map(int, sys.stdin.readline().split())
        graph[a].append(b)
        
    q = []
    heapq.heappush(q, (0,x))
    shortest = [1e10]*(n+1)
    shortest[x] = 0
    result = []
    while(q):
        dist, now = heapq.heappop(q)
        if dist == k:
            result.append(now)
        if dist > shortest[now]:
            continue
        for nxt in graph[now]:
            if dist+1 < shortest[nxt]:
                shortest[nxt] = dist+1
                heapq.heappush(q, (dist+1, nxt))
                
    if result == []:
        print(-1)
    else:
        print(*sorted(result), sep='\n') # list.sort()는 리스트 자체를 변경하고 반환x sorted(list)하면 정렬된 리스트를 반환
    

if __name__=='__main__':
    main()