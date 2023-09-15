import sys

sys.setrecursionlimit(10**6)
def main():
    T = int(sys.stdin.readline())
            
    visited = {}
    visited[0] = [1,0]
    visited[1] = [0,1]
    
    def pibo2(n): # dict + 재귀 + 메모이제이션
        if n in visited:
            return visited[n]
        
        if n >= 2:
            visited[n] = [pibo2(n-1)[i] + pibo2(n-2)[i] for i in range(2)] # list comprehension으로 변경
        return visited[n]
    
    for _ in range(T):
        N = int(sys.stdin.readline())
        a, b = pibo2(N)
        print(a, b)


    
    
if __name__=='__main__':
    main()