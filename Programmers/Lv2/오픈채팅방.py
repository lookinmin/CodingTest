def solution(records):
    answer = []
    tmp = []
    dict = {}

    for record in records:
        arr = record.split(' ')
        if arr[0] == 'Enter':
            dict[arr[1]] = arr[2]
            tmp.append("{}님이 들어왔습니다.".format(arr[1]))
        elif arr[0] == 'Change':
            dict[arr[1]] = arr[2]
        elif arr[0] == 'Leave':
            tmp.append('{}님이 나갔습니다.'.format(arr[1]))

    for sen in tmp:
        k = sen.find('님')
        answer.append(dict[sen[:k]] + sen[k:])

    return answer