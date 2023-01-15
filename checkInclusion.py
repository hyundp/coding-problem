# 투 포인터 알고리즘 : 두개의 포인터로 만들어지는 구간의 길이가 유동적이다.
# 슬라이딩 윈도우 알고리즘 : 두개의 포인터로 만들어지는 구간의 길이가 일정하다.

from collections import Counter
class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        n = len(s2)
        m = len(s1)
        vt = Counter(s1)
        for i in range(n):
            if s2[i] in vt:
                vt[s2[i]] -= 1 # 더 들어가면 음수로 표현, 덜 들어가면 양수로 표현
            if i>=m and s2[i-m] in vt: # window를 m만큼 고정해서 움직이는 것을 표현
                vt[s2[i-m]] += 1 
            if all([vt[k] == 0 for k in vt]): # 결과가 딱 맞게 모두 0일때 True
                return True
        return False