# Z, S1, 분할정복

from sys import stdin

N, r, c = map(int, stdin.readline().split())
# 분할 탐색 -> 재귀로 모든 부분을 분할 해 탐색하면 안된다. -> 시간복잡도의 개선이 없음

def dc(x, y, n):
    global cnt

    if x > r or x+n <= r or y > c or y+n <=c:       # 시작 지점에서(0,0) 2^N-1의 길이 안에 찾고자 하는 좌표(r, c)가 포함하지 않는다면
        cnt += n ** 2                               # Z 탐색을 하지 않고 칸 수를 한번에 계산한다
        return                                      # 변의길이의 제곱만큼 칸수가 증가하니까

    if n > 2:
        n //= 2
        dc(x, y, n)
        dc(x, y+n, n)
        dc(x+n, y, n)
        dc(x+n, y+n, n)
    else:
        if x == r and y == c:
            print(cnt)
        elif x == r and y+1 == c:
            print(cnt+1)
        elif x+1 == r and y == c:
            print(cnt + 2)
        else:
            print(cnt + 3)
        exit(0)

cnt = 0
dc(0, 0, 2**N)
