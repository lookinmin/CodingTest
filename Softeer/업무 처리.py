from sys import stdin
h, k, r = map(int, stdin.readline().split())

trees = []
for _ in range(2**h):
    trees.append(list(map(int, stdin.readline().split())))

def merge(arr1, arr2):
    tmp = []
    for i in range(len(arr1)):
        tmp.append(arr1[i])
        tmp.append(arr2[i])
    return tmp
    
for i in range(1, h+1):
    tasks = []
    for j in range(2**(h-i)):
        if i % 2 == 1:
            # 홀수
            tasks.append(merge(trees[2 * j + 1], trees[2 * j]))
        else:
            tasks.append(merge(trees[2 * j], trees[2 * j + 1]))
    trees = tasks

print(sum(trees[0][:r - h]))
