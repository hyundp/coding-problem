import sys
import copy
from string import ascii_uppercase
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
    
    record = {}
    
    for i in ascii_uppercase:
        record[i] = 0 #record를 한번에 접근할 수 있도록 dict생성
        
    
    def dfs(cur,cnt,rrecord): # dfs로 끝까지 가본 뒤 백트래킹으로 돌아올 수 있게 함.
        global result
        x,y = cur
        sign = graph[x][y]
        cur_record = copy.deepcopy(rrecord) # record가 다른 깊이에서 변형되지 않게 함.
        cur_record[sign] = 1 #visited가 아닌 record로 같은 문자가 있었는지 관리.
        if cnt > result:
            result = cnt
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            
            if nx < 0 or ny < 0 or nx > r-1 or ny > c-1:
                continue
            n_sign = graph[nx][ny]
            if cur_record[n_sign] == 0:
                dfs((nx,ny),cnt+1,cur_record)
                
    
    dfs((0,0),1,record) # 시작 칸도 포함하니 1부터 시작
    print(result)
    
if __name__=='__main__':
    main()