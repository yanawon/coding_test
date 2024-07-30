import sys
sys.stdin = open("input.txt","r")

N, M = map(int, input().split()) #N,M 입력
# 현재 위치와 보는 방향 입력
hereY, hereX, where = map(int, input().split())
# 맵 입력
Map = []
for i in range(N):
    Map.append(list(map(int, input().split())))
# 방문한 위치 표시 하기 위한 맵
Visited = [[0]*M]*N
# 북, 동, 남, 서 방향 정의
dx, dy = [-1,0,1,0],[0,-1,0,1]

turn = 0

# 왼쪽으로 회전
def t_left():
    global where
    where -= 1
    if where == -1:
        where = 3


# 시뮬레이션 시작
ans = 1
while True:
    # 왼쪽으로 회전
    t_left()
    nx, ny = hereX+dx[where], hereY+dy[where]
    # 회전하고 정면에 이동 하지 않은 칸이 있는 경우 전진
    if Map[ny][nx] == 0 and Visited[ny][nx] == 0:
        Visited[ny][nx] = 1
        hereY, hereX = ny, nx
        turn = 0
        ans += 1
        continue
    # 그렇지 않은 경우, 혹은 정면이 바다인 경우 회전
    else:
        turn += 1
    # 네 방향 모두 갈 수 없는 경우
    if turn == 4:
        nx, ny = hereX - dx[where], hereY-dy[where]
        # 뒤로 갈 수 있으면 이동
        if Map[ny][nx] == 0:
            hereX = nx
            hereY = ny
        # 뒤가 바다로 막힌 경우
        else :
            break
        turn = 0

# 정답 출력
print(ans)