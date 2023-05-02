# 출석체크, S2, 누적합
# 번호는 3 ~ n+2
# 한 학생에게 출석 코드를 보내게 되면,
# 해당 학생은 본인의 입장 번호의 배수인 학생들에게 출석 코드를 보내어 해당 강의의 출석

from sys import stdin

n, k, q, m = map(int, stdin.readline().split())
sleep = [0] * (n+3)
attend = [0] * (n+3)

for i in map(int, stdin.readline().split()):
    sleep[i] = 1        # 자는 사람 체크

for i in map(int, stdin.readline().split()):
    if sleep[i] == 1:
        continue        # 자면 그새끼 건너뜀
    for j in range(i, n+3, i):      # 해당 사람부터 끝까지 배수로 진행
        if not sleep[j]:
            attend[j] = 1           # 안자면, 출석

psum = [attend[0]]        # 맨처음 출석자부터 시작

for i in range(1, n+3):
    psum.append(psum[-1] + attend[i])       # psum의 가장 마지막과 i까지 출석한 애들 합
                    # 출석했으면 1이라 1이 더해지고, 아니면 0이 더해짐
                    # 즉, 출석한 사람의 수를 알 수 있음

for _ in range(m):
    s, e = map(int, stdin.readline().split())
    res = e - s + 1 - (psum[e] - psum[s-1])     # 전체 - s~e까지 출석한 애들
    print(res)
