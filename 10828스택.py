# 스택의 명령어 처리는 stack class를 만드는지 함수로 하는지 
# -> input에서 가져온 string을 바로 명령어로 사용할 수 없다면 if elif else가 필연적일 수 밖에 없음.
# -> 할 수 있지만 가져온 string을 동적으로 함수 호출로 사용하는 것은 보안상 문제가 있음 
# push만 split을 사용해야하는데 이에 대한 효율적인 처리 방법이 있는지 -> 그냥 push면 무조건 split을 하면 된다.
# del하는 것과 pop 하는 것이 속도차이를 만드는가? -> 똑같다.
# 함수를 여러번 호출하는 것이 속도차이를 만드는가? -> 똑같다.
# if else 문을 한 줄 처리하는 것이 속도차이를 만드는가? -> 똑같다.
# if __name__ 문이 속도차이를 만드는가? -> 만든다!! 48ms -> 44ms
# strip 과 rstrip으로 인해 속도차이가 만들어지는가? -> 오히려 느려진다 44ms -> 48ms
# empty에서 0 or 1을 표현 방식을 바꾸면(if문 -> +(not stack)) 속도 차이가 있는가? -> 없다..
# 알고리즘과 아이디어의 문제가 아니라 그냥 서버 상태의 문제인거 같으므로 여기까지.

import sys

def main():
    n_input = int(sys.stdin.readline())
    stack = []
    for _ in range(n_input):
        c = sys.stdin.readline().strip()
        if c == 'pop':
            print(stack.pop() if stack else -1)
        elif c == 'size':
            print(len(stack))
        elif c == 'empty':
            print(+(not stack))
        elif c == 'top':
            print(stack[-1] if stack else -1)
        else:
            stack.append(c.split()[1])

main()