# 거짓말, G4, 그래프 - union find

# 파티에 진실을 아는 사람이 한명이라도 있다면, 모두 진실만
# 즉, truth와 party의 교집합 검사 -> 겹치는 번호 있는지 확인
# 위 과정을 파티의 수 만큼 반복(m)

from sys import stdin

n, m = map(int, stdin.readline().split())
truth = set(input().split()[1:])

parties = []        # 전체 파티
for _ in range(m):
    party = set(input().split()[1:])
    parties.append(party)

for _ in range(m):
    for party in parties:       # 모든 파티의 각 파티에 대해
        if party & truth:       # 교집합에 번호가 하나라도 있을 때
            truth = truth.union(party)          # 해당 파티의 인원(진실을 알고 있는 사람)을 집합에 추가

res = 0
for party in parties:
    if party & truth:       # 해당 파티에서 거짓말을 할 수 없을 경우, 건너뜀
        continue
    res += 1

print(res)
