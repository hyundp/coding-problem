def reverseString(self, s):
    """
    :type s: List[str]
    :rtype: None Do not return anything, modify s in-place instead.
    """
    # 만약 메모리 사용가능하다면 s = list(reversed(s)) 하면 됨
    n = len(s)
    for i in range(n//2): # 중간까지 서로 자리 바꿈
        s[i], s[n-1-i] = s[n-1-i], s[i]
