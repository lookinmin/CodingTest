def solution(X, Y):
    answer = ""

    for i in range(9, -1, -1):
        answer += (str(i) * min(X.count(str(i)), Y.count(str(i))))

    if answer == "":
        return "-1"
    elif len(answer) == answer.count('0'):
        return "0"
    else:
        return answer

# 하나 알아감
# int() 를 통해 str->int 형 변환은 시간이 오래걸림