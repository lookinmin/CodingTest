from sys import stdin
n, k = map(int, stdin.readline().split())
line = list(map(str, stdin.readline().rstrip()))
# P 로봇, H 부품

res = 0
visited = [0] * n
for i in range(n):
    if line[i] == 'P':
        for val in range(i - k, i + k + 1):
            if n > val >= 0:
                if line[val] == 'H' and not visited[val]:
                    res += 1
                    visited[val] = 1
                    break
print(res)  