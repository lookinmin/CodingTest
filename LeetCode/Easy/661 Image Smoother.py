class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        n = len(img)
        m = len(img[0])
        res = [[0] * m for _ in range(n)]
        
        for i in range(n):
            for j in range(m):
                total = 0
                cnt = 0

                for x in range(max(0, i - 1), min(n, i + 2)):
                    for y in range(max(0, j - 1), min(m, j + 2)):
                        total += img[x][y]
                        cnt += 1
                
                res[i][j] = total // cnt
        return res