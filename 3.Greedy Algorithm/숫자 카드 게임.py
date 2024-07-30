import sys
sys.stdin = open("input.txt",'r')

ans = 0                             # 초기 답안 0으로 설정
N, M = map(int, input().split())    # N은 행의 갯수, M은 열의 갯수
for i in range(N):                  # 한 행씩 입력 받고, 각 행의 최솟값이 초기 답안보다 클 경우 답안으로 설정
    card = list(map(int, input().split()))
    if ans < min(card):
        ans = min(card)
print(ans)
