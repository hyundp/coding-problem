def reverseWords(self, s):
    """
    :type s: str
    :rtype: str
    """
    result = ''
    s_list = s.strip("\"").split() # 양쪽 : strip(), 오른쪽 : rstrip(), 왼쪽 : lstrip(), 대입해줘야 적용됨
    for i in range(len(s_list)):
        temp = list(reversed(s_list[i]))
        s_str = ''.join(temp) # '구분자'.join()는 리스트를 받아서 구분자로 연결한 string을 만드는 함수

        result = result + s_str + " " # 그냥 string끼리 연결은 덧셈활용
    result = result.rstrip()
    return result