import sys
import math

def main():
    T = int(sys.stdin.readline())
    for i in range(T):
        cnt = 0
        x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
        dd = math.sqrt((x2-x1)**2 + (y2-y1)**2) # 출발점과 도착점 거리
        n = int(sys.stdin.readline())
        for i in range(n):
            px,py,r = map(int,sys.stdin.readline().split())
            dist1 = math.sqrt((px-x1)**2 + (py-y1)**2) # 출발점과 행성 거리
            dist2 = math.sqrt((px-x2)**2 + (py-y2)**2) # 도착점과 행성 거리
            if dist1 < r: # 출발점이 행성 안에 있는 경우
                if dist2 > r: #도착점은 행성 밖에 있는 경우
                    cnt+=1
            elif dist1 > r: # 출발점이 행성 밖에 있는 경우
                if dist2 < r: # 도착점은 행성 안에 있는 경우
                    cnt+=1
        print(cnt)
        
    
    
    
if __name__ == '__main__':
    main()