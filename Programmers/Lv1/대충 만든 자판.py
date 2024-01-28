def solution(keymap, targets):
    answer = []
    for target in targets:
        word_idx = 0  # 총 누른 수

        for word in target:
            flag = False
            cnt = 101       # 최대 101

            for key in keymap:
                if word in key:
                    cnt = min(key.index(word) + 1, cnt)
                    flag = True

            if not flag:
                word_idx = -1
                break
            word_idx += cnt

        answer.append(word_idx)

    return answer