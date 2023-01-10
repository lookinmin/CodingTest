# 안테나, 실버3, 그리디

from sys import stdin

n = int(stdin.readline())
arr = list(map(int, stdin.readline().split()))
num = []

arr.sort()
print(arr[(n-1)//2])        # 그저 중간값을 찾아주면 되는문제




# 완전 탐색 풀이 -> n이 200,000이 최대기 때문에 시간초과
val = 0
for i in range(1, max(arr)+1):        # i == 점의 위치
    for j in range(n):
        val += abs(arr[j] - i)
    num.append(val)
    val = 0

print(num.index(min(num))+1)

