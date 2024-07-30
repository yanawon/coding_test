import sys
sys.stdin = open("개미 전사.txt",'r')

# 식량창고의 수
N = int(input())

# 각 식량창고에 저장된 식량의 개수
data = list(map(int,input().split()))

memo = [0]*100

memo[0] = data[0]
memo[1] = max(data[0],data[1])

# 답안
for i in range(2,N):
    memo[i] = max(memo[i-1],memo[i-2]+data[i])
print(memo[N-1])

# 내가 짠 코드
# for i in range(len(data)//2):
#     for j in range(i+2,len(data)):
#         memo.append(data[i]+data[j])
# print(max(memo))
