# 나머지 합, G3, 누적합

from sys import stdin

n,m = map(int,stdin.readline().split())
arr = list(map(int, stdin.readline().split()))

psum = [0] * (n+1)

for i in range(1, n+1):
    psum[i] = psum[i-1] + arr[i-1]
cnt = 0
for i in range(n):
    for j in range(i+1, n+1):
        if (psum[j] - psum[i]) % m == 0:
            cnt += 1

# ----------------- 이렇게 풀면 시간초과 ------------------------------#
# ----------------- 나머지들에 대한 인덱스 배열 생성---------------------#

num_sum = 0
numRemainder = [0] * m

for i in range(n):
    num_sum += arr[i]
    numRemainder[num_sum % m] += 1          # 현재 값까지에 대한 누적합의 나머지 수 인덱스 증가

res = numRemainder[0]       # 나머지가 0인 값들은 2개의 수를 뽑지 않아도 0으로 나눠떨어짐

for i in numRemainder:
    res += i * (i-1) // 2       # 나머지가 같은 2개의 구간을 뽑음, iC2

print(res)