# 후보 추천하기, S1, 구현

from sys import stdin
import heapq

n = int(stdin.readline())
m = int(stdin.readline())
arr = list(map(int, stdin.readline().split()))

student = {}
for i in arr:
    if i not in student:
        if len(student) >= n:
            a = heapq.nsmallest(min(student), student, key=student.get)
            student.pop(a[0])

        student[i] = 1
    else:
        student[i] += 1



print(*sorted(student.keys()))