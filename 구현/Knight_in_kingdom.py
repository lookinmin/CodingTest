# 왕실의 나이트, 시물레이션, 완전탐색
# 특정 위치에서 나이트가 이동가 능한 경우의 수 찾기
# 입력은(row, col)
a = input()
col = ['a', 'b', 'c', 'd', 'e', 'f','g','h']
r = int(col.index(a[0])+1)
c = int(a[1])

steps = [(-2, -1), (-1, -2), (1,-2),(2,-1), (2,1),(1,2),(-1,2),(-2,1)]
# 나이트가 이동할 수 있는 총 가짓 수

res = 0
for step in steps:
    next_row = r + step[0]
    next_col = c + step[1]
    if next_row >= 1 and next_row <= 8 and next_col >= 1 and next_col <= 8:
        res+=1

print(res)


