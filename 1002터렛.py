import sys
import math

# 원이 만나지 않거나, 한 점에서 만나거나, 두 점에서 만나거나, 겹치거나.
def main():
    T = int(sys.stdin.readline())
    
    for _ in range(T):
        x1, y1, r1, x2, y2, r2 = map(int, sys.stdin.readline().split())
        
        diff_x = x1-x2
        diff_y = y1-y2
        
        r = math.sqrt(diff_x**2 + diff_y**2)
        
        # 중심까지의 거리가 거리합보다 큰 경우 -> 만나지 못한다.
        if r > r1+r2:
            print(0)
            continue
        # 중심까지의 거리와 거리합이 같은 경우 -> 한 점에서 만난다.
        elif r == r1+r2:
            print(1)
            continue
        
        # 중심까지의 거리보다 거리합이 더 큰 경우 (r < r1+r2) -> 모든 경우가 가능하다.
        else:
            # 하나의 원이 다른 원 안에 있는 경우
            if r + min(r1,r2) < max(r1,r2):
                print(0)
            # 하나의 원이 다른 원 안에서 맞닿는 경우
            elif r + min(r1,r2) == max(r1,r2):
                # 원이 일치하는 경우 -1처리
                if r1==r2:
                    print(-1)
                else:
                    print(1)
                
            # 두 점에서 만나는 경우
            else:        
                print(2)
            continue
                
        
        
    
if __name__=='__main__':
    main()