import heapq
import sys # input 보다 가능하면 무조건 sys.stdin.readline()을 쓰자. 훨씬 빠르다.

v, e = map(int, sys.stdin.readline().split())
start = int(sys.stdin.readline())
graph = [[] for _ in range(v+1)]
shortest = [10e7]*(v+1) # 1부터니까 0은 안쓰는거


for _ in range(e):
    a,b,c = map(int, sys.stdin.readline().split())
    graph[a].append((b,c))

q = []
heapq.heappush(q, (0,start))
shortest[start] = 0

while(q):
    dist, now_node = heapq.heappop(q)
    if dist > shortest[now_node]:
        continue
    
    for nxt, cost in graph[now_node]:
        if dist+cost >= shortest[nxt]:
            continue
        else:
            shortest[nxt] = dist+cost
            heapq.heappush(q, (shortest[nxt],nxt)) # 만약 갱신 필요없으면 전에 한번 체크했다는 것이고 지금 가장 빨리 돌아 온건데 그것보다 느리다는 뜻이므로 고려대상x가 됨
            # 만약 또 갱신된다면 전에 넣어놨던 친구는 pop하고 바로 있는 if문에서 걸러짐.
            
for k in range(1,v+1):
    if shortest[k] == 10e7:
        print("INF")
    else:
        print(shortest[k])