class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        p = [[1], [1, 1]]
        if numRows == 1:
            return[[1]]
        elif numRows == 2:
            return p

        for i in range(2, numRows):
            tmp = [1 for _ in range(i + 1)]
            for idx in range(1, len(tmp) - 1):
                tmp[idx] = p[i-1][idx - 1] + p[i-1][idx]
            p.append(tmp)

        return p