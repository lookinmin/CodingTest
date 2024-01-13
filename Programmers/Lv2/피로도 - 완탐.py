from itertools import permutations
def solution(k, dungeons):
    answer = 0

    tmp = permutations(dungeons, len(dungeons))
    for route in tmp:
        now = 0
        hp = k
        for dungeon in route:
            if dungeon[0] <= hp:
                hp -= dungeon[1]
                now += 1
            else:
                continue
        answer = max(now, answer)

    return answer