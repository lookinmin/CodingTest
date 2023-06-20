# DNA 비밀번호, S2, 문자열-슬라이딩윈도우

from sys import stdin
from collections import deque

s, p = map(int, stdin.readline().split())
arr = list(stdin.readline().rstrip())
a, c, g, t = map(int, stdin.readline().split())

dic = {'A':0,'C':0,'G':0,'T':0}
cnt = 0

start = 0
end = p-1

tmp = deque(arr[start : end])

for i in tmp:
    dic[i] += 1

while end < s:
    dic[arr[end]] += 1          # 가장 오른쪽 원소 추가
    if dic['A'] >= a and dic['C'] >= c and dic['G'] >= g and dic['T'] >= t:
        cnt += 1

    dic[arr[start]] -= 1        # 가장 왼쪽 원소 제거
    start += 1
    end += 1

print(cnt)

# 시간초과 발생 -> while 안에서 count 세서 그럼
# while end <= s-1:
#     tmp = arr[start : end+1]
#     ka = tmp.count('A')
#     kc = tmp.count('C')
#     kg = tmp.count('G')
#     kt = tmp.count('T')
#
#     if a <= ka and c <= kc and g <= kg and t <= kt:
#         cnt += 1
#
#     start += 1
#     end += 1
