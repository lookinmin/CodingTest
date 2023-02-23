# 트리 나라 관광 가이드, S1, 트리
# 모든 도시의 부모도시를 찾아주기

from sys import stdin

N = int(stdin.readline())
city = list(map(int ,stdin.readline().split()))
visit = set()
visit.add(city[0])
parent = [0]*200001
parent[city[0]] = -1

for i in range(1, N):
    if city[i] not in visit:
        parent[city[i]] = city[i-1]     # 한번도 방문하지 않은 도시는 직전 방문 도시가 부모 노드
        visit.add(city[i])

print(len(visit))
for i in range(len(visit)):
    print(parent[i], end=" ")

# 전위 순회 탐색 pre_order
