import sys
from collections import deque

def main():

    m,n,k = map(int, sys.stdin.readline().split())
    re = [[0 for _ in range(m)] for _ in range(n)]
    for _ in range(k):
        a,b,c,d = map(int, sys.stdin.readline().split())
        for l in range(c-1,a-1,-1):
            for ll in range(d-1,b-1,-1):
                re[l][ll] = 1
    def bfs(x,y):
        ma = 1
        if re[x][y] != 0:
            return 0
        re[x][y] = 1
        dx = [-1,1,0,0]
        dy = [0,0,-1,1]

        q = deque()
        q.append((x,y))
        while(q):
            x,y = q.popleft()
            for i in range(4):
                nx = x+dx[i]
                ny = y+dy[i]

                if nx < 0 or ny < 0 or nx > n-1 or ny > m-1:
                    continue

                if re[nx][ny] == 0:
                    re[nx][ny] = 1
                    ma+=1
                    q.append((nx,ny))
        return ma

    result = []
    for i in range(n):
        for j in range(m):
            cnt = bfs(i,j)
            if cnt != 0:
                result.append(cnt)
    result.sort()
    print(len(result))
    for r in result:
        print(r, end=' ')

                

if __name__=='__main__':
    main()