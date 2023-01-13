# DP 예제, 효율적인 화폐 구성
# N (화폐의 종류), M (총합)    N <= 100, M <= 10000
# N개의 화폐의 가치로 M 을 만들건데, 최소 가짓수 출력, 못 만들면 -1

from sys import stdin

n, m = map(int, stdin.readline().split())
arr = []
for i in range(n):
    arr.append((int(input())))

d = [10001] * (m+1)
d[0] = 0
for i in range(n):                      # 각각의 화폐 단위
    for j in range(arr[i], m+1):
        if d[j - arr[i]] != 10001:      # 만드는거 가능
            d[j] = min(d[j], d[j- arr[i]] + 1)

if d[m] == 10001:
    print(-1)
else:
    print(d[m])