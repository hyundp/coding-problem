def lengthOfLongestSubstring(self, s): # time : O(n^2), space : O(n)
    """
    :type s: str
    :rtype: int
    """
    # 1. 마지막 것이 max 일때 업데이트 해줘야함
    # 2. 중복이 발생했을 때 -> 첫 중복문자 다음부터 이어서 진행
    max = 0
    temp = []
    for i in range(len(s)): # 직접 substring을 만들어서 최대 길이를 구하는 방식
        if s[i] in temp: # dict in 하면 key를 search한다.
            if max < len(temp):
                max = len(temp)
            for j in range(temp.index(s[i]) + 1):
                temp.remove(temp[0]) # remove는 값을 받는다.
        temp.append(s[i])
    if max < len(temp):
        max = len(temp)
    return max

def lengthOfLongestSubstring2(self, s: str) -> int: # time : O(n^3), space : O(min(m,n))
    def check(start, end):
        chars = set()
        for i in range(start, end + 1):
            c = s[i]
            if c in chars:
                return False
            chars.add(c)
        return True

    n = len(s)

    res = 0
    for i in range(n): # 모든 경우를 다 돌아보는 방식
        for j in range(i, n):
            if check(i, j):
                res = max(res, j - i + 1)
    return res

def lengthOfLongestSubstring4(self, s: str) -> int: # time : O(n), space O(min(m,n))
    n = len(s)
    ans = 0
    # mp stores the (current index  + 1) of a character -> 중복이 발생하면 첫 중복문자 다음 것부터 이어서 하라는 뜻
    mp = {}

    i = 0 # 실제 메모리를 사용하는 것이 아니라, 인덱스만으로 길이를 구함
    # try to extend the range [i, j]
    for j in range(n):
        if s[j] in mp:
            i = max(mp[s[j]], i)

        ans = max(ans, j - i + 1)
        mp[s[j]] = j + 1

    return ans