# 가로의 길이 n
n = int(input())

# 메모이제이션 테이블 초기화
memo = [0] * 1001

memo[1] = 1
memo[2] = 3
for i in range(3, n+1):
    memo[i] = memo[i-1]+memo[i-2]+memo[i-2] % 796796

print(memo[n])