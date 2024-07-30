import sys
sys.stdin = open("input.txt",'r')

N, K = map(int, input().split())
ans = 0
def for_1(N, K):
    global ans
    if N == 1:
        return print(ans)
    if N % K != 0:
        ans += N % K
        N -= N % K
        for_1(N, K)
    else:
        N /= K
        ans += 1
        for_1(N, K)

for_1(N, K)