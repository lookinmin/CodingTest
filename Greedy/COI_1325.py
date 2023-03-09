# 커피박
# 1잔당 커피박 2개 무조건

from sys import stdin

n = int(stdin.readline())
coffee = n * 2
arr=[0,0,0]
while coffee > 0:
    if coffee // 4 > 0:
        arr[2] += 1
        coffee -= 4

    elif coffee // 3 > 0:
        arr[1] += 1
        coffee -= 3

    else:
        arr[0] += 1
        coffee -= 1


print(*arr)