# 수강신청, S3, 구현

from sys import stdin

k, l = map(int, stdin.readline().split())
nums = {}

for i in range(l):
    nums[stdin.readline().rstrip()] = i     # 해당 번호의 순서 부여

res = sorted(nums.items(), key=lambda x : x[1]) # 순서대로 오름차순 정렬

if k > len(res):
    k = len(res)
# for i in range(l):
#     tmp = stdin.readline().rstrip()
#     if tmp in nums:
#         nums.remove(tmp)      # 찾아야 해서 시간초과 걸림
#     nums.append(tmp)

for i in range(k):
    print(res[i][0])