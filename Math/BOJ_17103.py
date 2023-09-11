# 골드바흐 파티션, S2, 수학

from sys import stdin

# 2보다 큰 짝수는 두 소수의 합으로 나타낼 수 있다.

T = int(stdin.readline())

arr = [True] * 1000001

for i in range(2, 1000001):
    if arr[i]:
        for j in range(i*2, 1000001, i):
            arr[j] = False


for _ in range(T):
    n = int(stdin.readline().rstrip())

    # 6 = 3 + 3, 8 = 3 + 5
    cnt = 0

    for i in range(2, n // 2 + 1):      # 제곱근 까지만 비교하면 쌍이 바껴서 들어갈 일이 없다
        if arr[i] and arr[n-i]:
            cnt += 1


    print(cnt)