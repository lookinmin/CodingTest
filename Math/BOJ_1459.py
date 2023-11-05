# 걷기, S3, 수학-다중조건분기

from sys import stdin
# ->, ↑, 대각선

x, y, w, s = map(int, stdin.readline().split())

# 가로, 세로로만 이동했을 때

tmp = w * x + w * y

# 대각선으로만

if(x + y) % 2 == 0:
    tmp2 = max(x, y) * s

else:   # 대각선 + 평행 이동 1번
    tmp2 = (max(x, y) - 1) * s + w      # 한칸 더 가서 뒤로 가도 됨

tmp3 = (min(x, y) * s) + (abs(x-y) * w) # 대각 + 평행 같이

print(min(tmp, tmp2, tmp3))