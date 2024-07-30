"""위상 정렬 알고리즘
    1. 진입차수가 0인 노드를 큐에 삽입
    2. 큐가 빌 때까지 다음의 과정을 반복
        -1 큐에서 원소를 꺼내 해당 노드에서 출발하는 간선을 그래프에서 제거
        -2 새롭게 진입차수가 0이 된 노드를 큐에 삽입"""
from collections import deque
import sys
sys.stdin = open("tp_sort.txt", 'r')

# 노드의 개수와 간선의 개수를 입력
node, edge = map(int, input().split())
# 모든 노드에 대한 진입차수는 0으로 초기화
indegree = [0] * (node + 1)
# 각 노드에 연결된 간선 정보를 담기 위한 연결 리스트(그래프) 초기화
graph = [[]for i in range(node + 1)]

# 방향 그래프의 모든 간선 정보를 입력
for _ in range(edge):
    a, b = map(int, input().split())
    graph[a].append(b) # 정점 A에서 B로 이동하는 엣지
    # 진입차수를 1 증가
    indegree[b] += 1

# 위상 정렬 함수
def tp_sort():
    result = [] # 알고리즘 수행 결과를 담을 리스트
    q = deque() # 큐 기능을 위한 deque 라이브러리 사용

    # 처음 시작할 때는 진입차수가 0인 노드를 큐에 삽입
    for i in range(1, node+1):
        if indegree[i] == 0:
            q.append(i)

    # 큐가 빌 때까지 반복
    while q:
        # 큐에서 원소 꺼내기
        here = q.popleft()
        result.append(here)
        # 해당 원소와 연결된 노드들의 진입차수에서 1 빼기
        for i in graph[here]:
            indegree[i] -= 1
            # 새롭게 진입차수가 0이 되는 노드를 큐에 삽입
            if indegree[i] == 0:
                q.append(i)

    # 위상 정렬을 수행한 결과 출력
    for i in result:
        print(i ,end=' ')

tp_sort()