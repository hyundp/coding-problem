import sys
import heapq


def main():
    n, m ,x = map(int, sys.stdin.readline().split())
    graph = [[] for _ in range(n+1)]
    long_time = 0
    for _ in range(m):
        a, b, c = map(int, sys.stdin.readline().split())
        graph[a].append((b,c))
        
    def dijkstra(start, end):
        shortest = [1e10]*(n+1)
        q = []
        heapq.heappush(q, (0, start))
        shortest[start] = 0
        while(q):
            dist, now = heapq.heappop(q)
            if now == end:
                return shortest[end]
            if dist > shortest[now]:
                    continue
            for nxt, cost in graph[now]:
                    if cost+dist < shortest[nxt]:
                        shortest[nxt] = cost + dist
                        heapq.heappush(q, (cost+dist, nxt))
        
    for i in range(1, n+1):
          go = dijkstra(i,x)         
          back = dijkstra(x,i)
          if long_time < go+back:
                long_time = go+back
    print(long_time)
    



if __name__ == '__main__':
        main()