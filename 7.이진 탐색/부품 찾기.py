import sys
sys.stdin = open("부품찾기.txt",'r')

have = int(input())
have_data = list(map(int,input().split()))
find = int(input())
find_data = list(map(int, input().split()))
ans = []
have_data.sort()

def binary_search(data, target, start, end):
    does_have = False
    while start <= end:
        mid = (start+end)//2
        if data[mid] == target:
            does_have = True
            break
        elif data[mid] < target:
            start = mid+1
        else: end = mid-1

    if does_have==False:
        ans.append("no")
    else: ans.append("yes")

for i in find_data:
    binary_search(have_data,i,0,len(have_data))
print(*ans)
