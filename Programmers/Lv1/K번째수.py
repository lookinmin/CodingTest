def solution(array, commands):
    answer = []
    for command in commands:
        i, j, k = command[0], command[1], command[2]
        tmp = array[i-1 : j]
        tmp.sort()
        answer.append(tmp[k-1])
    return answer