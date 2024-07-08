def binary_search(data, target, start, end):
    while start<=end:
        mid = (start+end)//2
        # 중간값이 타겟과 일치하면 인덱스 반환
        if data[mid] == target:
            return mid
        # 중간값이 타겟보다 크면 왼쪽 탐색
        elif data[mid] > target:
            end = mid-1
        # 중간값이 타겟보다 작으면 오른쪽 탐색
        else:
            start = mid + 1
        return None