# ZOAC
word = list(input().rstrip())
res = [''] * len(word)

def dfs(start, word):
    if not word:
        return

    min_val = min(word)
    tmp = word.index(min_val)

    res[start + tmp] = min_val
    print("".join(res))

    dfs(start + tmp + 1, word[tmp + 1 :])
    dfs(start, word[:tmp])

dfs(0, word)