import sys
sys.stdin = open("input.txt","r")

n = int(input())
data = dict()       # 딕셔너리로 4.구현
grades = []
for i in range(n):
    name, grade = input().split()   # 이름과 성적을 입력받음
    grades.append(grade)            # 성적 리스트를 만듬
    data[grade] = name              # 성적을 키로 하여 딕셔너리 4.구현
grades.sort()                       # 성적 리스트를 오름차순으로 6.정렬
for i in range(n):                  # 출력
    print(data[grades[i]],end=' ')
