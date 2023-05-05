# 부분수열의 합, S1, 백트래킹

from sys import stdin
from itertools import permutations


n = int(stdin.readline())
s = list(map(int, stdin.readline().split()))
s.sort()
cnt = 1

for i in s:
    if cnt < i:
        break
    cnt += i

print(cnt)



# 내 풀이
# 가능한 모든 조합을 구해서
# 해당합들을 리스트에 넣고 답을 구함
# -> 시간초과 발생
n = int(stdin.readline())
s = stdin.readline().rstrip()
s = s.replace(" ","")
nums = set()
for k in range(1, len(s)+1):
    for i in permutations(s, k):
        tmp = ''.join(i)
        if int(tmp) < 10:
            nums.add(int(tmp))
        else:
            a = 0
            for t in tmp:
                a += int(t)
            nums.add(a)


res = sorted(nums)
cnt = 1
while 1:
    if cnt not in res:
        print(cnt)
        exit(0)
    else:
        cnt += 1