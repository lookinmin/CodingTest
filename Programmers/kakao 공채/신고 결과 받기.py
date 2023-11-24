def solution(id_list, report, k):
    answer = []

    userDic = {}
    for id in id_list:
        userDic[id] = []

    for s in report:
        user, re = s.split(' ')
        userDic[user].append(re)

    singo = {}
    for keyUser in list(userDic.keys()):
        li = userDic[keyUser]
        for i in range(len(li)):
            if li[i] in singo:
                singo[li[i]].add(keyUser)
            else:
                singo[li[i]]= {keyUser}


    on = []

    for id in singo.keys():
        if len(singo[id]) >= k:
            on.append(id)

    for id in userDic.keys():
        tmp = 0
        for report_id in on:
            if report_id in userDic[id]:
                tmp += 1
        answer.append(tmp)
    return answer

print(solution(["muzi", "frodo", "apeach", "neo"], ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"], 2))