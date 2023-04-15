import sys
import heapq

def main():
    n, e = map(int, sys.stdin.readline().split())
    graph = [[] for _ in range(n+1)]
    result = True
    for _ in range(e):
          a, b, c = map(int, sys.stdin.readline().split())
          graph[a].append((b,c))
          graph[b].append((a,c))
    v1, v2 = map(int, sys.stdin.readline().split())
    def dijkstra(start, end):
        
        shortest = [1e10]*(n+1)
        q = []
        heapq.heappush(q, (0,start))
        shortest[start] = 0
        while(q):
            dist, now = heapq.heappop(q)
            if now == end:
                  return shortest[now]
            if dist > shortest[now]:
                    continue
            for nxt, cost in graph[now]:
                    if cost + dist < shortest[nxt]:
                        shortest[nxt] = cost+dist
                        heapq.heappush(q, (cost+dist, nxt))
        return -10000
                 
    case1 = dijkstra(1, v1) + dijkstra(v1, v2) + dijkstra(v2,n)
    case2 = dijkstra(1, v2) + dijkstra(v2, v1) + dijkstra(v1,n)
    
    if case1<0 and case2<0:
          print(-1)
    elif case1<0:
          print(case2)
    elif case2<0:
          print(case1)
    else:
          print(min(case1,case2))
    
    
    
if __name__ == '__main__':
        main()