# 조건
# 1. 1과2의 조합으로 n을 만들 수 있는 경우의 수를 구하여라
# 2. 2개중에 하나를 선택하는 경우의 수 문제

# 방법1
# 1. 1과 2를 선택하는 경우를 재귀적으로 호출하여 모든 경우를 백트래킹한다.

class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        cnt = 0
        def dfs(k, cnt):
            if k == n:
                return 1
            if k > n:
                return 0
            cnt += dfs(k+1, cnt)
            cnt += dfs(k+2, cnt)
        dfs(0, cnt)
        return cnt