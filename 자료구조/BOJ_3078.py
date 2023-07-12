# 좋은 친구, G4, 큐

from collections import deque
from sys import stdin

# 성적 차이가 K 이내, 이름 길이가 같아야 함

n, k = map(int, stdin.readline().split())
student = [0] * n
num = [0] * 21      # 이름의 길이수를 담을 배열, 길이 수의 최대는 20글자
# 이름이 4글자인 사람이 4명이면 num[4] = 4
res = 0

for i in range(n):
    student[i] = len(stdin.readline().rstrip())
    if i > k:       # 범위 밖
        num[student[i - k - 1]] -= 1

    res += num[student[i]]
    num[student[i]] += 1

print(res)