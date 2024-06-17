import sys
sys.stdin = open("input.txt",'r')

N, M, K = map(int, input().split())      # N,M,K를 구분하여 입력
data = list(map(int, input().split()))   # N개의 수를 구분하여 입력
data.sort()
max1 = data[-1]                          # 가장 큰 값
max2 = data[-2]                          # 두번째로 큰 값
mod = M%K                                # 두번째로 큰 값이 더해지는 횟수
ans = (max1 * (M-mod)) + (max2 * mod)

print(ans)                               # 최종 답안