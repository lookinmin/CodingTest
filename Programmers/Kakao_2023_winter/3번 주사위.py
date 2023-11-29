def solution(dice):
    answer = []
    n = len(dice)
    score = {}
    for i in range(n):
        score[i+1] = 0


    for i in range(n):
        for j in range(n):
            if i != j:      # 지꺼랑 비교 X
                win = 0
                draw = 0
                lose = 0

                for a in dice[i]:
                    for b in dice[j]:
                        if a > b:
                            win += 1
                        elif a == b:
                            draw += 1
                        else:
                            lose += 1

                score[i+1] += (win / (win + draw + lose))     # 각 주사위의 승률
                score[i+1] -= ((draw + lose) / (win + draw + lose))
                score[j+1] += ((lose + draw) / (win + draw + lose))
                score[i+1] -= (win / (win + draw + lose))

    print(score)
    tmp = sorted(score.items(), key=lambda x: x[1], reverse=True)


    print(tmp)
    for i in range(n//2):
        answer.append(tmp[i][0])


    if len(answer) > 1:
        answer.sort()
        return answer
    else:
        return answer


print(solution(
[[40, 41, 42, 43, 44, 45], [43, 43, 42, 42, 41, 41], [1, 1, 80, 80, 80, 80], [70, 70, 1, 1, 70, 70]]))