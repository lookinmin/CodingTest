class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        k = len(s)
        res = []

        # 구간은 4개
        if k < 4 or k > 12:
            return []

        def dfs(outs, start, dots):
            tmp = ""
            for i in range(start, min(k, start + 3)):
                outs.append(s[i])
                tmp += s[i]
                
                if (len(tmp) > 1 and tmp[0] == '0') or int(tmp) > 255:
                    for _ in range(len(tmp)):
                        outs.pop()
                    return

                if i + 1 == k and not dots:
                    res.append(''.join(outs)) 
                elif (k - 1) - i <= (dots - 1) * 3 + 3:
                    outs.append('.')
                    dfs(outs, i + 1, dots - 1)
                    outs.pop()  # 추가한 '.' 제거
                
            # 유효하지 않은 경우, outs에서 추가한 요소들을 제거
            for _ in range(len(tmp)):
                outs.pop()

        dfs([], 0, 3)
        return res
