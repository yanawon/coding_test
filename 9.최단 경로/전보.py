import sys
import heapq
sys.stdin = open("전보.txt",'r')

# 무한대 INF 설정
INF = (1e9)

# 도시의 개수 n, 통로의 개수 m, 메시지를 보내고자 하는 도시 c 입력
n, m, c = map(int, input().split())

# 지도 정보 data 입력
data = [[] for i in range(n+1)]
for i in range(m):
    # 출발하는 도시 x, 목적지 y, 소요시간 z 입력
    x, y, z = map(int, input().split())
    data[x].append((y, z))

# 경로의 가중치 초기화
distance = [INF] * (n+1)

def dijkstra(start):
    q = []
    heapq.heappush(q,(start,0))
    distance[start] = 0
    while q:
        here, dist = heapq.heappop(q)
        if distance[here] < dist:
            continue
        for i in data[here]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q,(i[0],cost))

dijkstra(c)

count = 0
max_distance = 0
for d in distance:
    if d != INF:
        count += 1
        max_distance = max(max_distance, d)

print(count-1, max_distance)