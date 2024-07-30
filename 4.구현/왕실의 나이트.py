# 8*8 좌표 평면상에서 주어진 시작위치로 부터 나이트가 이동할 수 있는 경우의 수를 출력하는 프로그램
import sys
sys.stdin=open("input.txt",'r')

St_pt = str(input())
St_row = int(St_pt[1])
St_col = int(ord(St_pt[0])) - int(ord('a'))+1

steps = [(-2,-1),(-1,-2),(1,-2),(2,-1),(1,2),(2,1),(-2,1),(-1,2)]
ans = 0
for i in steps:
    if St_col + i[1] >= 1 and St_row + i[0] >= 1 and St_row + i[0] <= 8 and St_col + i[1] <= 8:
        ans += 1

print(ans)