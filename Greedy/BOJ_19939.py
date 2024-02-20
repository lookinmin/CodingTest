# 박 터뜨리기, S4, 그리디

N, K = map(int, input().split())

tmp = K * (K + 1) // 2
if tmp > N:
    print(-1)
else:
    if (N - tmp) % K == 0:
        print(K - 1)
    else:
        print(K)

