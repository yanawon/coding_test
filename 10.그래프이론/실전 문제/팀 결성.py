import sys
sys.stdin = open("팀 결성.txt", 'r')

N, M = map(int, input().split())
parent = [0] * (N+1)
for i in range(1, N+1):
    parent[i] = i

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def operation_0(parent,x, y):
    a = find_parent(parent,x)
    b = find_parent(parent,y)
    if a == b:
        print("YES")
    else: print("NO")

def union_parent(parent, x, y):
    a = find_parent(parent, x)
    b = find_parent(parent, y)
    if a > b:
        parent[a] = b
    else : parent[b] = a

for i in range(M):
    a, b, c = map(int, input().split())
    if a == 0:
        union_parent(parent, b, c)
    if a == 1:
        operation_0(parent, b, c)