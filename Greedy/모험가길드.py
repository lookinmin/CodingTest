# 모험가 길드
# 그리디 예제
# 공포도 X인 모험가 = X명 이상의 모험가 그룹에 참여
# 만들 수 있는 그룹의 최대 수
# 모든 모험가가 그룹에 속할 필요는 없다

from sys import stdin
n = int(stdin.readline())
arr = list(map(int, stdin.readline().split()))
arr.sort()

cnt = 0 # 총 그룹의 수
 # 현재 그룹의 모험가 수
group = 0
for i in arr:
    group += 1
    if group >= i:      # 현재 그룹에 포함된 모함가의 수 > 현재의 공포도 => 그룹 결성
        cnt += 1
        group = 0       # 그룹 구성했으면 초기화

print(cnt)
