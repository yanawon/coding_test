import sys
sys.stdin = open("input.txt","r")

N = int(input())
data = []
for i in range(N):
    data.append(int(input()))
data.sort(reverse=True)

print(*data)
