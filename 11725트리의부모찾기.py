import sys
import heapq

def main():
    n = int(sys.stdin.readline().rstrip())
    graph = [[] for _ in range(n+1)]
    root = 1
    for _ in range(n-1):
        a,b = map(int, sys.stdin.readline().split())
        graph[a].append(b)
        graph[b].append(a)
    
    def bfs(start, end): # 부모를 건너지 않고는 자식을 찾아갈 수 없기 때문에 shortest 배열이 필요가 없다.
        q = []
        heapq.heappush(q, (0,start))
        
        while(q):
            dist, cur = heapq.heappop(q)
            
            for g in graph[cur]:
                if g == end:
                    return cur
                heapq.heappush(q, (dist+1, g))
                    
    
    for i in range(2,n+1):
        print(bfs(root, i))
    
if __name__=='__main__':
    main()