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
        
        # 먼저 계산해서 그 계산 결과가 0<= x <n 이 되는 것이 훨씬 구현하기 쉬움
        dx = [1,-1,0,0]
        dy = [0,0,1,-1]
        
        for j in range(4):
            nx = now_nodex+dx[j]
            ny = now_nodey+dy[j]
            
            if 0<=nx<cave_count and 0<=ny<cave_count:
                if shortest[nx][ny] > now_cost+graph[nx][ny]:
                    shortest[nx][ny] = now_cost+graph[nx][ny]
                    heapq.heappush(q, (now_cost+graph[nx][ny], nx, ny))
                
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