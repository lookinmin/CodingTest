from sys import stdin

P, N = map(int, stdin.readline().split())
arr = list(map(int, stdin.readline().split()))
res = 0

for num in arr:
    res *= P
    res %= 1000000007
    res += num
print(res)