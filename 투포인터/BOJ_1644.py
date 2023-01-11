# 소수의 연속합, 골드3, 수학-투포인터
import math

n = int(input())

arr = [True for i in range(n + 1)]
sosu = []
for i in range(2, int(math.sqrt(n)) + 1):
    if arr[i]:
        j = 2
        while i * j <= n:
            arr[i * j] = False
            j += 1

for i in range(2, n+1):
    if arr[i]:
        sosu.append(i)

# 배열에 소수만 집어넣기  ->  에라토스테네스의 체

# 연속되는 소수의 합인지 찾기 -> 투포인터
cnt = 0
start = 0
end = 0
while end <= len(sosu):
    temp_sum = sum(sosu[start : end])
    if temp_sum == n:
        cnt += 1
        end += 1
    elif temp_sum < n:
        end += 1
    else:
        start += 1

print(cnt)
