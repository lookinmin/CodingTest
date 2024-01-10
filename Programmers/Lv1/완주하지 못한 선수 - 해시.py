def solution(participant, completion):
    hashDict = {}
    sumHash = 0

    for name in participant:
        hashDict[hash(name)] = name
        sumHash += hash(name)

    for name in completion:
        sumHash -= hash(name)

    return hashDict[sumHash]