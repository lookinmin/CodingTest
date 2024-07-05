class Solution:
    def countAndSay(self, n: int) -> str:
        origin = "1"
        for _ in range(n - 1):
            idx = 0
            tmp = ""
            while idx < len(origin):
                cnt = 1
                now = origin[idx]
                for i in range(idx + 1, len(origin)):
                    if origin[i] == now:
                        cnt += 1
                    else:
                        break
                tmp += "{}{}".format(cnt, now)
                idx += cnt
            origin = tmp
        return origin
