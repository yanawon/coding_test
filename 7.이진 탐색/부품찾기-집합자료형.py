import sys
sys.stdin = open("부품찾기.txt",'r')

# 가게의 부품 개수
N = int(input())
# 가게에 있는 전체 부품 번호를 집합 자료형에 기록
data = set(map(int, input().split()))

# 손님이 확인을 요청한 부품 개수
M = int(input())
# 손님이 확인을 요청한 부품 번호를 리스트에 기록
target_list = list(map(int,input().split()))

# 요청한 부품 번호 하나씩 확인
for i in target_list:
    if i in data:
        print("yes",end=" ")
    else: print("no", end=" ")
