from collections import deque
def solution(bandage, health, attacks):
    answer = 0
    hp = health
    max_hp = health
    at_queue = deque(attacks)
    cnt = 0
    
    for time in range(1, attacks[-1][0] + 1):
        if time == at_queue[0][0]:
            hp -= at_queue[0][1]
            at_queue.popleft()
            cnt = 0
            if hp <= 0:
                return -1
        else:
            cnt += 1
            hp += bandage[1]
            if hp >= max_hp:
                hp = max_hp
            if cnt == bandage[0]:
                hp += bandage[2]
                if hp >= max_hp:
                    hp = max_hp
                cnt = 0
            else:
                continue
    return hp