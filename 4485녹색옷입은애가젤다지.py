import sys
import heapq

def main(cave_count): # 경로가 주어지지 않고 그래프가 주어진 형태
    shortest = [[1e10]*cave_count for _ in range(cave_count)] # 2차원으로 만드려면 이렇게 해줘야함
    graph = [[] for _ in range(cave_count)]
    for i in range(cave_count):
        temp = map(int, sys.stdin.readline().split())
        graph[i].extend(temp) # extend는 원소를 iter해서 넣고, append는 리스트 그 자체를 넣어버림.
    
    q = []
    shortest[0][0] = graph[0][0]
    heapq.heappush(q, (graph[0][0],0,0))
    
    while(q):
        now_cost, now_nodex, now_nodey = heapq.heappop(q)
        if (now_nodex == cave_count-1) and (now_nodey == cave_count-1):
            return now_cost
        if now_cost > shortest[now_nodex][now_nodey]:
            continue
        if now_nodex > 0:
            if shortest[now_nodex-1][now_nodey] > now_cost+graph[now_nodex-1][now_nodey]:
                shortest[now_nodex-1][now_nodey] = now_cost+graph[now_nodex-1][now_nodey]
                heapq.heappush(q, (now_cost+graph[now_nodex-1][now_nodey], now_nodex-1,now_nodey))
        if now_nodex < cave_count-1:
            if shortest[now_nodex+1][now_nodey] > now_cost+graph[now_nodex+1][now_nodey]:
                shortest[now_nodex+1][now_nodey] = now_cost+graph[now_nodex+1][now_nodey]
                heapq.heappush(q, (now_cost+graph[now_nodex+1][now_nodey], now_nodex+1,now_nodey))
        if now_nodey > 0:
            if shortest[now_nodex][now_nodey-1] > now_cost+graph[now_nodex][now_nodey-1]:
                shortest[now_nodex][now_nodey-1] = now_cost+graph[now_nodex][now_nodey-1]
                heapq.heappush(q, (now_cost+graph[now_nodex][now_nodey-1], now_nodex,now_nodey-1))
        if now_nodey < cave_count-1:
            if shortest[now_nodex][now_nodey+1] > now_cost+graph[now_nodex][now_nodey+1]:
                shortest[now_nodex][now_nodey+1] = now_cost+graph[now_nodex][now_nodey+1]
                heapq.heappush(q, (now_cost+graph[now_nodex][now_nodey+1], now_nodex,now_nodey+1))        
            
            
    
    
    
if __name__=='__main__':
    cnt = 0
    cave_cnt = int(sys.stdin.readline())
    result = []
    while cave_cnt != 0:
        result.append(main(cave_cnt))
        cnt+=1
        cave_cnt = int(sys.stdin.readline())
        
    for i in range(cnt):
        print(f"Problem {i+1}: {result[i]}")