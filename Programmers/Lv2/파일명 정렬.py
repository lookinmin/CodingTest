import re

def solution(files):
    pattern = r"\d+"
    idx = {}
    for i in range(len(files)):
        idx[files[i]] = i

    files.sort(key=lambda x: (x[:x.find(re.findall(pattern, x)[0])].lower(), int(re.findall(pattern, x)[0]), idx[x]))
    return files
