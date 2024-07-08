def binary_search(data, target, start, end):        # start = data의 시작점, end = data의 length
    if start > end:
        return None
    mid = (start+end)//2        #중간점 지정
    if data[mid] == target:     #중간점이 타겟과 일치할경우 인덱스 반환
        return mid
    # 중간점이 타겟보다 크면 왼쪽 확인
    elif data[mid] > target:
        binary_search(data,target,start,mid-1)
    # 중간점이 타겟보다 작으면 오른쪽 확인
    elif data[mid] < target:
        binary_search(data,target,mid+1,end)

