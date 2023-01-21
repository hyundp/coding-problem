# 조건
# 1. 1과2의 조합으로 n을 만들 수 있는 경우의 수를 구하여라
# 2. 2개중에 하나를 선택하는 경우의 수 문제

# 방법1
# 1. 1과 2를 선택하는 경우를 재귀적으로 호출하여 0부터 시작하여 n으로 가는 모든 경우를 백트래킹한다.
# 2. 이때 한번 호출된 값은 vt에 저장하여 중복 계산을 피한다. -> 값을 더해서 n을 만드는 것이 아니고, 경우의 수를 모두 세는 방식이므로 중복 계산이 없음.
# 3. 중간에 n을 만들 수 없다고 판단되면 중단한다. -> n-1일때만 중단할 수 있어서 효과가 크지 않음

# 결론 : time limit exceeded

class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        cnt = 0
        vt = []
        def dfs(k):
            if k == n:
                return 1
            if k > n:
                return 0
            if k == n-1:
                return dfs(k+1)
            return dfs(k+1) + dfs(k+2)
        
        cnt = dfs(0)
        return cnt