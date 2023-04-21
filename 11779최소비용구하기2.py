import sys
import heapq

def main():
    n = int(sys.stdin.readline())
    m = int(sys.stdin.readline())
    graph = [[] for _ in range(n+1)]
    for _ in range(m):
        a,b,c = map(int, sys.stdin.readline().split())
        graph[a].append((b,c))
    
    start, end = map(int, sys.stdin.readline().split())
    
    shortest = [1e10]*(n+1)
    shortest[start] = 0
    q = []
    heapq.heappush(q, (0, start))
    
    parents = [i for i in range(n+1)] # 나 == 나 로 저장해둠
    parents[start] = 0 # 시작 시점은 0으로 만들어서 나중에 역추적할 때 조건으로 사용함.
    
    while(q):
        dist, now = heapq.heappop(q)
        if now == end:
            print(shortest[end])
            break
        if dist > shortest[now]:
            continue
        
        for nxt, cost in graph[now]:
            if cost + dist < shortest[nxt]:
                shortest[nxt] = cost+dist
                heapq.heappush(q, (cost+dist, nxt))
                parents[nxt] = now
                
                    
    path = []
    cur = end
    while cur != 0:
        path.append(cur)
        cur = parents[cur]
    print(len(path))
    for i in range(len(path)-1,-1,-1):
        print(path[i], end=' ') # 역추적한거 거꾸로 출력하면 경로 산출
    
if __name__ == '__main__':
    main()