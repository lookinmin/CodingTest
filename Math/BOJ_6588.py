# 골드바흐의 추측, S1, 수학

from sys import stdin
# 4보다 큰 모든짝수는 두 홀수 소수의 합으로 나타낼 수 있다

arr = [False, False] + [True]*1000001
for i in range(3, int(1000001 ** 0.5) + 1, 2):
    if arr[i]:
        for j in range(i*2, 1000001, i):
            arr[j] = False

while 1:
    n = int(stdin.readline())
    if n == 0:
        break

    for i in range(3, int(n/2) + 1, 2):
        if arr[i] and arr[n - i]:   # 하나는 밑에서부터 하나는 위에서부터 -> 처음찾는 b-a가 무조건 최대
            print("{} = {} + {}".format(n, i, n-i))
            break
    else:
        print("Goldbach's conjecture is wrong.")



