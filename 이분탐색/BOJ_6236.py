# 용돈 관리, S2, 이분탐색

from sys import stdin

n, m = map(int, stdin.readline().split())
day = list(int(stdin.readline().rstrip()) for _ in range(n))
start = min(day)
end = sum(day)

while start <= end:
    mid = (start + end) // 2

    charge = mid        # 현재 가진 돈, 처음 인출
    cnt = 1
    for i in range(n):
        if day[i] > charge:      # 가진 돈이 부족
            charge = mid
            cnt += 1             # 인출해야 함
        charge -= day[i]         # 처음 인출 한 돈에서 하루치 쓴만큼 뺌

    if cnt > m or mid < max(day):       # m번보다 더 많이 인출함 or 하루에 2번 인출해야함(인출 금액이 부족)
        start = mid + 1
    else:
        end = mid - 1
        res = mid

print(res)