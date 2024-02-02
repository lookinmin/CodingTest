from sys import stdin
n = int(stdin.readline())
arr = list(map(int, stdin.readline().split()))

loca = [0] * n

for i in range(n):
    for j in range(n):
        # print(*arr)
        # print(*loca)
        # print("--------")
        if arr[i] == 0 and loca[j] == 0:
            loca[j] = i + 1
            break
        elif loca[j] == 0:
            arr[i] -= 1

print(*loca)

