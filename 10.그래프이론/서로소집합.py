# 서로소 부분 집합들로 나누어진 원소들의 데이터를 처리하기 위한 자료구조
# union과 find 연산으로 조작 가능
# 트리 자료구조를 이용하여 집합을 표현
# 1.union 연산을 확인하여 서로 연결된 두 노드 A,B를 확인
#   - A와 B의 루트 노드 A',B'를 각각 찾는다
#   - A'를 B'의 부모 노드로 설정(B'가 A'를 가리키도록 설정)
# 2.모든 union 연산을 처리할 때까지 1.번 과정을 반복.


# 특정 원소가 속한 집합을 찾기
def find_parent(parent, x):
    # 루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀적으로 호출
    if parent[x] != x:
        return find_parent(parent,parent[x])
    return x

# 두 원소가 속한 집합을 합치기
def union_parent(parent, a, b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)
    if a<b:
        parent[b] = a
    else : parent[a] = b

# 노드의 개수와 간선(union 연산)의 개수 입력받기
v, e = map(int, input().split())
parent_data = [0] * (v+1) # 부모 테이블 초기화

# 부모 테이블상에서 부모를 자기 자신으로 초기화
for i in range(1, v+1):
    parent_data[i] = i

# union연산을 각각 수행
for i in range(e):
    a, b = map(int, input().split())
    union_parent(parent_data, a,b)

# 각 원소가 속한 집합 출력
print('각 원소가 속한 집합: ', end=' ')
for i in range(1, v+1):
    print(find_parent(parent_data,i), end= ' ')

print()

# 부모 테이블 내용 출력
print("부모 테이블: ", end=' ')
for i in range(1, v+1):
    print(parent_data[i], end=' ')