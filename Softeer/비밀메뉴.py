from sys import stdin

M, N, K = map(int, stdin.readline().split())
secret = list(map(int, stdin.readline().split()))
arr = list(map(int, stdin.readline().split()))

k = len(secret)

if len(arr) < len(secret):
    print("normal")
    exit()

for i in range(len(arr) - k + 1):
    tmp = arr[i : i + k]
    if tmp == secret:
        print("secret")
        exit()

print("normal")