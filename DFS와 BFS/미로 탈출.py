import sys
from collections import deque as dq
sys.stdin = open("input.txt","r")

N, M = map(int, input().split())
maze = []
for i in range(N):
    maze.append(list(map(int, input())))
dx, dy = [-1,1,0,0], [0,0,-1,1]

def BFS(y,x):
    myQ = dq()
    myQ.append((y,x))
    while myQ:
        y, x = myQ.popleft()
        for i in range(4):
            next_x, next_y = x+dx[i], y+dy[i]
            if M > next_x > -1 and N > next_y > -1 and maze[next_y][next_x] == 1:
                maze[next_y][next_x] = maze[y][x]+1
                myQ.append((next_y,next_x))
    return print(maze[N-1][M-1])
BFS(0,0)
