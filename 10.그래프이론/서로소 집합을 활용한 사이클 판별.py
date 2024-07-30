""" 1. 각 간선을 확인하며 두 노드의 루트 노드를 확인
        - 루트 노드가 서로 다르면 두 노드에 대해 union연산을 수행
        - 루트 노드가 서로 같다면 사이클(Cycle)이 발생한 것
    2. 그래프에 포함되어 있는 모든 간선에 대하여 1번 과정을 반복
    (주의) 무방향 그래프에만 적용 가능"""
# 특정 원소가 속한 집합을 찾기
def find_parent(parent, x):
    # 루트 노드가 아니라면 루트 노드를 찾기 위해 재귀적으로 호출
    if parent[x] != x:
        parent[x] = find_parent(parent,parent[x])
    return parent[x]

# 두 원소가 속한 집합을 합치기
def union_parent(parent, a, b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)
    if a<b:
        parent[b] = a
    else: parent[a] = b

# 노드의 개수와 간선(union 연산)의 개수 입력받기
node, edge = map(int, input().split())
parent_data = [0] * (node + 1) #부모 테이블 초기화

# 부모 테이블상에서 자신의 부모를 자신으로 초기화
for i in range(1,node+1):
    parent_data[i] = i

cycle = False   # 사이클 발생 여부

for i in range(node):
    a, b = map(int, input().split())
    # 사이클이 발생한 경우 종료
    if find_parent(parent_data,a) == find_parent(parent_data,b):
        cycle = True
        break
    # 사이클이 발생하지 않은 경우 union 수행
    else:
        union_parent(parent_data,a,b)

if cycle: print("사이클이 발생했습니다.")
else : print("사이클이 발생하지 않았습니다.")