from sys import stdin

n = int(stdin.readline())

# 총 합을 저장할 리스트
total = [0] * n
# 순위 계산 함수
def rank(arr):
    ranking = [0] * n
    ans = [0] * n
    for i in range(n):
        arr[i] = [arr[i], i]
    arr.sort(reverse = True)
    cnt = 1
    ranking[0] = 1

    for i in range(1, n):
        if arr[i][0] != arr[i - 1][0]:
            cnt = i + 1
        ranking[i] = cnt

    for i in range(n):
        ans[arr[i][1]] = ranking[i]
    print(*ans)

# 각 라운드에 대해 점수 입력 받기
for _ in range(3):
    scores = list(map(int, stdin.readline().split()))
    for i in range(n):
        total[i] += scores[i]
    rank(scores)

# 최종 합산 점수에 대한 순위 출력
rank(total)