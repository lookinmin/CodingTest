# 보석상자, S1, 이분탐색
# 보석을 n명의 학생에게, 한 학생은 항상 같은 색상만
# 질투심 = 가장 많은 보석을 가져간 학생의 보석 수

from sys import stdin
n, m = map(int, stdin.readline().split())
jewels = []

for _ in range(m):
    jewel = int(stdin.readline().rstrip())
    jewels.append(jewel)

start = 1
end = max(jewels)

res = end

# 찾고자 하는 최적의 값(몇개씩 나눠줘야 하는가) = x
# x 미만 = 보석이 남는 범위, x 이상 = 보석을 다 나눠준 범위
# x를 이동시키며 최적의 범위를 찾기

while start <= end:
    mid = (start+end) // 2
    p = 0               # 한 사람마다 줘야 할 보석의 수

    for jewel in jewels:
        q = jewel // mid
        r = jewel % mid

        p += q          # 인당 나눈 몫 만큼 가져갈 수 있음

        if r > 0:       # 나머지가 존재하면, 해당 보석을 다 나눠줘야 하므로 사람 수를 추가
            p += 1

    if p > n:           # 전체 사람수 보다 보석을 나눠 줘야 되는 사람 수가 많다면
        start = mid + 1
    else:
        res = min(res, mid)
        end = mid - 1

print(res)

