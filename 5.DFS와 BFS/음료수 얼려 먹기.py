import sys
sys.stdin = open("input.txt","r")

N, M = map(int,input().split())
graph = []
for i in range(N):
    graph.append(list(map(int,input())))
ans = 0
def DFS(x,y):
    if x <= -1 or x >= M or y <= -1 or y >= N:
        return False
    if graph[y][x] == 0:
        graph[y][x] = 1
        DFS(x,y-1)
        DFS(x-1,y)
        DFS(x,y+1)
        DFS(x+1,y)
        return True
    return False


for i in range(N):
    for j in range(M):
        if DFS(i,j) == True:
            ans += 1
print(ans)