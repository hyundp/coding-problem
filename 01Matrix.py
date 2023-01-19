# 조건 : 값은 1과 0만 존재한다, mat안에 적어도 한개의 0이 있다.


# 방법 1
# 1. 0이 존재한다면 4방위에 있는 친구들은 모두 그대로다.
# 2. 처리되지 않은 친구들은 가까운 처리된 친구들을 찾아서 갱신해준다? -> 다시 처리하는 방법을 모르겠다.
from itertools import product


def updateMatrix1(self, mat):
    """
    :type mat: List[List[int]]
    :rtype: List[List[int]]
    """
    

    m = len(mat)
    n = len(mat[0])


    vt = [[0]*n for _ in range(m)]
    for mm, nn in product(range(m), range(n)): # 그대로인 친구들 처리
        if vt[mm][nn] == 1:
            continue
        if mat[mm][nn] == 0:
            vt[mm][nn] = 1
            if mm>0:
                vt[mm-1][nn] = 1
            if mm < m-1:
                vt[mm+1][nn] = 1
            if nn>0:
                vt[mm][nn-1] = 1
            if nn < n-1:
                vt[mm][nn+1] = 1

    for mm, nn in product(range(m), range(n)): # 나머지 친구들 처리
        pass


# 방법2 
# 1. queue를 사용해서 bfs를 사용한다.
from collections import deque

def updateMatrix(self, mat):
    m, n = len(mat), len(mat[0])
    DIR = [0, 1, 0, -1, 0]

    q = deque([])
    for r in range(m):
        for c in range(n):
            if mat[r][c] == 0:
                q.append((r, c))
            else:
                mat[r][c] = -1  # Marked as not processed yet!

    while q:
        r, c = q.popleft()
        for i in range(4):
            nr, nc = r + DIR[i], c + DIR[i + 1]
            if nr < 0 or nr == m or nc < 0 or nc == n or mat[nr][nc] != -1: continue
            mat[nr][nc] = mat[r][c] + 1
            q.append((nr, nc))
    return mat


# 방법3
# 1. dp를 활용한다.
# 2. 