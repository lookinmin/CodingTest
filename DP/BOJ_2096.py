# 내려가기, G5, DP
# 슬라이딩 윈도우

# 메모리 제한 4mb -> 슬라이딩 윈도우를 통해 메모리 사용량 제한
# DP에서 말하는 슬라이딩 윈도우 기법이란, 메모이제이션을 할 때 더 이상 사용하지 않는 값을 저장하지 않고 배열을 계속하여 갱신

from sys import stdin

n = int(stdin.readline())
board = list(map(int, stdin.readline().split()))

dp1 = board         # 최대값이 담길 배열, 마지막에서 해당 배열에서 가장 큰 값이 최대값이 된다
dp2 = board         # 최소값이 담길 배열

for _ in range(n-1):
    a, b, c = map(int, stdin.readline().split())        # 들어오는 수들을 받고
    dp1 = [a + max(dp1[0], dp1[1]), b+ max(dp1), c+ max(dp1[1], dp1[2])]        # 최대값을 갱신한다
    dp2 = [a + min(dp2[0], dp2[1]), b + min(dp2), c+ min(dp2[1], dp2[2])]       # 최소값을 갱신

print(max(dp1), min(dp2))
