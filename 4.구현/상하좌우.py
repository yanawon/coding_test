import sys
sys.stdin = open("input.txt", "r")

N = int(input())
cord = list(map(str, input().split()))

y = [-1, 1, 0, 0]
x = [0, 0, -1, 1]

st_pt = [1,1]

for i in cord:
    if i == "L":
        if st_pt[1] -1 == 0: continue
        else:
            st_pt[1] -= 1
    elif i == "R":
        if st_pt[1] +1 == N+1: continue
        else:
            st_pt[1] += 1
    elif i == "U":
        if st_pt[0] -1 == 0: continue
        else:
            st_pt[0] -= 1
    elif i == "D":
        if st_pt[0] +1 == N+1: continue
        else:
            st_pt[0] += 1
print(*st_pt)