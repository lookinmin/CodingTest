# 치킨배달,G5,구현-백트래킹
# 0 빈칸, 1 집, 2 치킨집
# 치킨 거리 = 집과 가장 가까운 치킨집 사이 거리
# 도시의 치킨 거리 = 모든 집의 치킨 거리의 합

from sys import stdin
from itertools import combinations

n, m = map(int, stdin.readline().split())
city = []
for i in range(n):
    city.append(list(map(int,stdin.readline().split())))

house = []
chicken = []

for i in range(n):
    for j in range(n):
        if city[i][j] == 1:
            house.append([i,j])
        elif city[i][j] == 2:
            chicken.append([i,j])

res = 999999

for i in combinations(chicken, m):      # m개의 치킨집을 선택하는 모든 조합에 대해 도시의 치킨거리를 구합
    tmp = 0                             # 어떤 조합을 골랐을 때, 해당 조합에 대한 치킨거리의 합이 들어갈 임시변수
    for h in house:                     # 모든 집들에 대해
        chi_len = 999
        for j in range(m):              # m개의 치킨집에 대해
            chi_len = min(chi_len, abs(h[0] - i[j][0]) + abs(h[1]-i[j][1]))     # 각 집에 대해 가장 가까운 치킨 거리를 구함
        tmp += chi_len                  # 각 집의 치킨거리를 tmp에 더함 -> tmp는 모든 집들에 대한 치킨거리의 합
    res = min(res, tmp)                 # 모든 조합에 대해 비교해가면서 가장 작은 값을 res에 return

print(res)