# 내 지금 선택에 따라 다음 기회가 달라지는 경우의 수 문제
# 해설 : https://leetcode.com/problems/stone-game/solutions/261718/step-by-step-recursive-topdown-bottomup-and-bottomup-using-o-n-space-in-java/?orderBy=most_votes

def stoneGame1(self, p): # 2D dp 
    n = len(p)
    dp = [[0] * n for i in range(n)]
    for i in range(n): 
        dp[i][i] = p[i]
    for d in range(1, n):
        for i in range(n - d):
            dp[i][i + d] = max(p[i] - dp[i + 1][i + d], p[i + d] - dp[i][i + d - 1])
    return dp[0][-1] > 0

def stoneGame2(self, p): # 1D dp
    n = len(p)
    dp = p[:]
    for d in range(1, n):
        for i in range(n - d):
            dp[i] = max(p[i] - dp[i + 1], p[i + d] - dp[i])
    return dp[0] > 0

def stoneGame3(self, piles): # normal recursion -> time exceed
    def playGame(piles, si, ei, turn):
        if si > ei:
            return 0
        if turn:
            l1 = piles[si] + playGame(piles, si+1, ei, False)
            r1 = piles[ei] + playGame(piles, si, ei-1, False)
            return max(l1,r1)
        else:
            l2 = playGame(piles, si+1, ei, True) - piles[si]
            r2 = playGame(piles, si, ei-1, True) - piles[ei]
            return min(l2,r2)

    return playGame(piles, 0, len(piles)-1, True)

def stoneGame4(self, piles): # recursion + 2D dp
    def playGame(piles, si, ei, turn, arr):
        if si > ei:
            return 0
        if arr[si][ei] > 0:
            return arr[si][ei]
        if turn:
            l1 = piles[si] + playGame(piles, si+1, ei, False, arr)
            r1 = piles[ei] + playGame(piles, si, ei-1, False, arr)
            arr[si][ei] = max(l1, r1)
            return arr[si][ei]
        else:
            l2 = playGame(piles, si+1, ei, True, arr) - piles[si]
            r2 = playGame(piles, si, ei-1, True, arr) - piles[ei]
            arr[si][ei] = min(l2, r2)
            return arr[si][ei]
    n = len(piles)
    arr = [[0]*n for _ in range(n)]
    return playGame(piles, 0, n-1, True, arr)