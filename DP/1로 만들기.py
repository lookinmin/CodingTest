# DP 예제
# 1로 만들기
# 연산 4개
# 1. X가 5로 나누어 떨어지면 5로 나눈다
# 2. X가 3으로 나누어 떨어지면 3으로 나눈다
# 3. X가 2로 나누어 떨어지면 2로 나눈다
# 4. X - 1
# 연산의 최솟값 ?

# 2,3,5가 배수의 관계가 아니기 때문에 Greedy 방법으로 풀면 안됨!

x = int(input())
# ai = min(ai-1,ai/2, ai/3, ai/5) + 1
d = [0] * 30001

for i in range(2, x+1):
    d[i] = d[i-1] + 1   # 현재 수에서 -1하는 경우
    if i % 2 == 0:
        d[i] = min(d[i], d[i//2] + 1)   # 1빼는게 최소인지, 2로 나누는게 최소인지
    if i % 3 == 0:
        d[i] = min(d[i], d[i//3] + 1)
    if i % 5 == 0:
        d[i] = min(d[i], d[i//5] + 1)

print(d[x])