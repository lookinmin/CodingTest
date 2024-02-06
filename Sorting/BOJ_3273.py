from sys import stdin

n = int(stdin.readline())
arr = list(map(int, stdin.readline().split()))
x = int(stdin.readline())
arr.sort()

start = 0
end = n - 1

res = 0
while start < end:
    if arr[start] + arr[end] == x:
        res += 1
        start += 1
    elif arr[start] + arr[end] < x:
        start += 1
    else:
        end -= 1

print(res)
