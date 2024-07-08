import sys
sys.stdin = open("떡볶이.txt",'r')

# 떡의 개수 N, 요청한 총 길이 M 설정
N, M = map(int,input().split())

# 떡의 길이 리스트
data = list(map(int,input().split()))


def HowLong(data,mid,target):
    dummy = 0       # 타겟값과 비교할 더미데이터
    for i in data:
        if i > mid:     # 잘랐을 때 떡의 양 계산
            dummy += i-mid
    if dummy == target:     # 더미데이터가 타겟값과 같으면 자른 길이 출력
        print(mid)
        return
    elif dummy > target:    # 더미데이터가 타겟보다 크면 길이를 1 늘림
        HowLong(data,mid+1,target)
    else: HowLong(data,mid-1,target)    # 더미데이터가 타겟보다 작으면 길이를 1 줄임

mid = max(data)//2      # 자를 길이를 가장 긴 떡의 절반 길이로 지정

HowLong(data,mid,M)