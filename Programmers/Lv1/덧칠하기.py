# 덧칠하기, lv1

def solution(n, m, section):
    # n = 벽의 총 길이
    # m = 한번에 칠하는 벽의 길이
    # section = 칠해야 하는 인덱스

    wall = [1] * 100000
    for num in section:
        wall[num - 1] = 0

    answer = 0
    i = 0
    while 0 in wall:
        if wall[i] == 0:
            for j in range(m):
                wall[i + j] = 1
            answer += 1
        i += 1

    return answer

# 시간초과
# while로 찾는 과정에서 시간 초과가 나는듯


def solution(n, m, section):
    # n = 벽의 총 길이
    # m = 한번에 칠하는 벽의 길이
    # section = 칠해야 하는 인덱스
    answer = 1
    now = section[0]

    for i in range(1, len(section)):
        if section[i] - now >= m:       # section을 넘어가면서 테스트
            answer += 1
            now = section[i]
    return answer