import sys

sys.setrecursionlimit(10**6) #파이썬 재귀함수 갯수제한 처리 (런타임에러 핸들링)

cnt = 0
t = int(sys.stdin.readline())

def main():
    global cnt
   
    m, n, k = map(int, sys.stdin.readline().split())
    
    graph = [[0]*m for _ in range(n)]
    
    for _ in range(k):
        a,b = map(int, sys.stdin.readline().split())
        graph[b][a] = 1
        
    
    def dfs(x,y):
        global cnt
        dx = [-1,1,0,0]
        dy = [0,0,-1,1]
        if graph[y][x] == 1:
            graph[y][x] = 0
            
            for i in range(4):
                nx = x+dx[i]
                ny = y+dy[i]
                
                if nx<0 or ny<0 or nx>m-1 or ny>n-1:
                    continue
                
                if graph[ny][nx] == 1:
                    cnt += dfs(nx,ny)
            return 1
        return 0

    house = []
    
    for i in range(m):
        for j in range(n):
            if dfs(i,j) == 1:
                house.append(cnt)
                cnt = 0
                
    print(len(house))
    
if __name__=='__main__':
    for _ in range(t):
        main()