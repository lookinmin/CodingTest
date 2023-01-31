# BABBA, S5, DP
# 시작 상태 = A (고정)
# A -> BA -> BAB -> BABBA -> BABBABAB
# 1,0 -> 1,1 -> 1,2 -> 2,3 -> 3,5
# 피보나치 처럼 증가
K = int(input())
a = [1,0]
b = [0,1]
for i in range(2, K+1):
    cnt_a = a[i-1] + a[i-2]
    a.append(cnt_a)
    cnt_b = b[i-1] + b[i-2]
    b.append(cnt_b)
print("{} {}".format(a[K], b[K]))
