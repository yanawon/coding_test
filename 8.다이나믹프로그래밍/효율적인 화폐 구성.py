import sys
sys.stdin = open("input.txt",'r')

# 화폐의 개수 n과 목표 합 m 입력
n, m = map(int, input().split())
n_list = []
for i in range(n):
    n_list.append(int(input()))

# 메모이제이션 테이블
memo = [0]+[10001]*(m)

for i in n_list:
    for j in range(i,m+1):
        if memo[j-i] != 10001:
            memo[j] = min(memo[j], memo[j-i]+1)

if memo[m] == 10001:
    print(-1)
else: print(memo[m])


