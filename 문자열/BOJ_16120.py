# PPAP, G4, 문자열

from sys import stdin

s = list(stdin.readline().rstrip())
stack = []
ppap = ["P","P","A","P"]

for i in range(len(s)):
    stack.append(s[i])
    if stack[-4:] == ppap:        # 스택에 들어있는 4개의 값이 PPAP를 형성
        for i in range(4):
            stack.pop()             # 전부 다 빼고
        stack.append('P')           # P하나 넣음

if stack == ppap or stack == ["P"]: # 스택 내의 값이 P하나 이거나, PPAP가 남으면 PPAP 문자열임
    print("PPAP")
else:
    print("NP")


# origin = "PPAP"
# if s == 'P' or s == "PPAP":
#     print('PPAP')
# else:
#     for i in range(4):
#         if origin[i] == 'P':
#             origin[i] = "PPAP"
#             if origin == s:
#                 print('PPAP')
#                 break
#             else:
#                 origin[i]  = 'P'
#                 continue
