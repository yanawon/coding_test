# 정수 N이 입력되면 00:00:00 부터 N:59:59 까지 중에 3이 하나라도 포함되는 모든 경우의 수를 구하는 프로그램
import sys
sys.stdin=open("input.txt",'r')

N = int(input())
# 모든 경우의 수
All = (N+1) * 60 * 60
# N의 크기에 따라 포함 되는 3의 갯수가 다르므로 N을 분류
if N < 13:
    N = N
elif 13 <= N <23:
    N = N-1
elif N >= 23:
    N = N-2
# 모든 경우의 수에서 3이 한개도 포함 되지 않는 경우의 수를 뺀다
print(All - (45*45*N))

