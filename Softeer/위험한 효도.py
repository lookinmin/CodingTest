from sys import stdin

def calculate_cycle(a, b, d):
    cnt = 0
    now = 'back'

    while d > 0:
        if now == 'back':
            for i in range(a):
                d -= 1
                cnt += 1
                if d == 0:
                    return cnt
            now = 'front'
        elif now == 'front':
            cnt += b
            now = 'back'

    return cnt

a, b, d = map(int, stdin.readline().split())

# 첫 번째 순환
cnt = calculate_cycle(a, b, d)

# 매개변수 변경 후 두 번째 순환
a, b = b, a
cnt += calculate_cycle(a, b, d)

print(cnt)