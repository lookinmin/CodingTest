# 영단어 암기는 괴로워, S3, 문자열-정렬
#자주 나오는 단어일수록 앞에 배치한다.
#해당 단어의 길이가 길수록 앞에 배치한다.
#알파벳 사전 순으로 앞에 있는 단어일수록 앞에 배치한다

from sys import stdin

n,m = map(int, stdin.readline().split())
words = {}

for i in range(n):
    word = str(stdin.readline().rstrip())

    if len(word) >= m:
        if word in words:
            words[word] += 1
        else:
            words[word] = 1

# res = set()     # 집합 쓰면 시간초과
# # 딕셔너리로 해결
#
#
# for word in words:
#     n = words.count(word)
#     res.add((word,n))
#
# ans = list(res)

ans = sorted(words.items(), key = lambda x : (-x[1], -len(x[0]), x[0]))

for i in ans:
    print(i[0])