import itertools

def solution(word):
    answer = 0
    words = ['A','E','I','O','U']
    result = set()
    for i in range(1, 6):
        tmp = list(itertools.product(words, repeat=i))
        for w in tmp:
            k = ''
            for j in range(len(w)):
                k += w[j]
            result.add(k)
    res = list(result)
    res.sort()
    cnt = 0
    for i in range(len(res)):
        cnt += 1
        if res[i] == word:
            return cnt