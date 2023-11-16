def solution(n):
    ans = 0

    while 1:
        if n % 2 != 0:
            n -= 1
            ans += 1
        if n % 2 == 0:
            n //= 2

        if n == 0:
            break

    return ans

# 그리디
# 2의 배수임을 생각하자