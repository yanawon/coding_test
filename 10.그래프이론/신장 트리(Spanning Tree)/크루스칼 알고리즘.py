""" 신장 트리 중에서 최소 비용으로 만들 수 있는 신장 트리를 찾는 알고리즘"""
""" 1. 간선 데이터를 비용에 따라 오름차순으로 정렬
    2. 간선을 하나씩 확인하며 현재의 간선이 사이클을 발생시키는지 확인
        2-1 사이클이 발생하지 않는 경우 최소 신장 트리에 포함시킨다
        2-2 사이클이 발생하는 경우 최소 신장 트리에 포함시키지 않는다
    3. 모든 간선에 대하여 2번의 과정을 반복"""
# 특정 원소가 속한 집합을 찾기
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent,parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)
    if a<b:
        parent[b] = a
    else : parent[a] = b

node, edge = map(int, input().split())
parent_data = [0] * (node + 1)
for i in range(1, node+1):
    parent_data[i] = i

edges = []
ans = 0
for j in range(edge):
    From, To, cost = map(int, input().split())
    edges.append((cost,From,To))

edges.sort()

for edge in edges:
    cost, start, end = edge

    if find_parent(parent_data,start) != find_parent(parent_data,end):
        union_parent(parent_data,start,end)
        ans += cost

print(ans)