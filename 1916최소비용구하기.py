import heapq
import sys

def main():

      n = int(sys.stdin.readline())
      m = int(sys.stdin.readline())
      graph = [[] for _ in range(n+1)]
      shortest = [1e10]*(n+1)

      for _ in range(m):
            a, b, c = map(int, sys.stdin.readline().split())
            graph[a].append((b,c)) # 하나의 지점에 길이 여러개니까 append 해야한다. 빈[]에 append하면 그대로 채워진다. [(~~), (~~)]
                                   # 반면에 빈 []를 가지고 있는 []에 append 하면 [[], (~~)]가 되는 것.

      start, end = map(int, sys.stdin.readline().split())
      q = []
      heapq.heappush(q, (0, start))
      shortest[start] = 0 # 초기화

      while(q):
            dist, now_node = heapq.heappop(q)
            if now_node == end:
                  print(shortest[now_node])
                  return
            if shortest[now_node] < dist: # heapq로 우선순위만 빼다보면 이미 갱신이 다시 된 예전에 넣어둔 친구가 나올 수 있음. 이를 무시하기 위한 조건
                  continue
            else:
                  for nxt, cost in graph[now_node]:
                        if dist+cost < shortest[nxt]:
                              shortest[nxt] = dist+cost
                              heapq.heappush(q, (dist+cost, nxt))


if __name__ == '__main__':
      main()
        