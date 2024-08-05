class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n = len(boxes)
        res = [0] * n

        leftCount, leftCost, rightCount, rightCost = 0, 0, 0, 0

        for i in range(1, n):   # 왼쪽으로 부터 오른쪽 순회
            if boxes[i - 1] == '1':
                leftCount += 1
            leftCost += leftCount
            res[i] = leftCost
        
        for i in range(n-2, -1, -1):
            if boxes[i + 1] == '1':
                rightCount += 1
            rightCost += rightCount
            res[i] += rightCost
        
        return res