import sys
sys.stdin = open("미래 도시.txt",'r')
INF = (1e9)

# 회사의 개수 N, 경로의 개수 M 입력
N, M = map(int, input().split())

# 경로를 리스트에 저장
data = [[INF]*(N+1) for _ in range(N+1)]
for i in range(M):
    y, x = map(int, input().split())
    data[y][x], data[x][y] = 1,1

# 경유할 노드 X와 목적지 K를 입력
X, K = map(int, input().split())

# 점화식으로 플로이드워셜 실행
for i in range(1, N+1):
    for j in range(1, N+1):
        for k in range(1, N+1):
            data[i][j] = min(data[i][j], data[i][k]+data[k][j])

# 수행된 결과 출력
ans = data[1][K]+data[K][X]

# 도달 불가인 경우 -1을 출력
if ans >= INF:
    print("-1")
# 도달 가능한 경우 최단 거리를 출력
else:
    print(ans)