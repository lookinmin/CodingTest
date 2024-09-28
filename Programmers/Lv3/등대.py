from collections import defaultdict
import sys
sys.setrecursionlimit(10**6)

def solution(n, lighthouse):
    graph = defaultdict(list)
    
    for a, b in lighthouse:
        graph[a].append(b)
        graph[b].append(a)
    
    def dfs(node, parent):
        if not graph[node]:
            return 0, 1
    
        off, on = 0, 1
        
        for edj in graph[node]:
            if edj != parent:
                edj_off, edj_on = dfs(edj, node)
                off += edj_on
                # 나를 끄는 경우, 내 인접 등대는 무조건 켜져야함
                on += min(edj_on, edj_off)
                # 나를 키는 경우, 내 인접 등대를 키는 경우 중 더 최솟값
        
        return off, on
    
    return min(dfs(1, 0))