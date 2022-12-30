# 누적합, 브론즈1, 슈퍼마리오
# 구간 쿼리가 아닌, 처음 부터 시작 하는 쿼리
# 누적합이 100개 가깝게

from sys import stdin
a = [0 for _ in range(11)]     # 입력될 배열
psum = [0 for _ in range(11)]  # 누적 합이 들어올 배열
res = 0
for i in range(1, 11):
    a[i] = int(stdin.readline())
    psum[i] = psum[i-1] + a[i]

for i in range(1, 11):
    if psum[i] == 100:
        res = psum[i]
        break
    elif psum[i] > 100:
        if psum[i] - 100 <= 100 - psum[i-1]:
            res = psum[i]
            break
        else :
            res = psum[i-1]
            break
    elif psum[i] < 100:
        res = psum[i]

print(res)