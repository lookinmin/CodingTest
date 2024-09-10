# G5, 옥상 정원 꾸미기
from sys import stdin
n = int(input())
buildings = []
for i in range(n):
    buildings.append(int(stdin.readline().rstrip()))

stack = []
res = 0

for i in range(n):
    while stack and stack[-1] <= buildings[i]:
        stack.pop()
    
    res += len(stack)
    stack.append(buildings[i])

print(res)

# -------------------------- 시간초과 -----------------------
# buildings = []
# can = [True] * n
# see = [0] * n
# for i in range(n):
#     now = int(stdin.readline().rstrip())
#     for j in range(len(buildings)):
#         if buildings[j] > now and can[j]:
#             see[j] += 1
#         elif buildings[j] <= now:
#             can[j] = False
        
        
#     buildings.append(now)

# print(sum(see))
