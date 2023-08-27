# 햄버거 분배, S3, 그리디

from sys import stdin
n, k = map(int,stdin.readline().split())
arr=list(stdin.readline().rstrip())

cnt = 0

for i in range(n):
    if arr[i] == 'P':
        for j in range(max(i-k, 0), min(i + k + 1, n)):         # 범위 내 찾기하는 방법 알아두기
            if arr[j] == 'H':
                cnt += 1
                arr[j] = 'E'
                break

print(cnt)