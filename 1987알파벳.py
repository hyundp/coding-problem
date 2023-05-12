import sys
import copy
sys.setrecursionlimit(10**6) #파이썬 재귀함수 갯수제한 처리 (런타임에러 핸들링)

result = 0
def main():
    global result
    
    r, c = map(int, sys.stdin.readline().split())
    graph = []
    for _ in range(r):
        temp = list(map(str, sys.stdin.readline().rstrip()))
        graph.append(temp)
        
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    
    def dfs(cur,cnt,record): # dfs로 끝까지 가본 뒤 백트래킹으로 돌아올 수 있게 함.
        global result
        x,y = cur
        cur_record = copy.deepcopy(record) # record가 다른 깊이에서 변형되지 않게 함.
        cur_record.append(graph[x][y]) #visited가 아닌 record로 같은 문자가 있었는지 관리.
        if cnt > result:
            result = cnt
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            
            if nx < 0 or ny < 0 or nx > r-1 or ny > c-1:
                continue
            
            if graph[nx][ny] not in cur_record:
                dfs((nx,ny),cnt+1,cur_record)
                
    
    dfs((0,0),1,[]) # 시작 칸도 포함하니 1부터 시작
    print(result)
    
if __name__=='__main__':
    main()