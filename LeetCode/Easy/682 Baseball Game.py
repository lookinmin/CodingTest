class Solution:
    def calPoints(self, operations: List[str]) -> int:
        records = []
        for op in operations:
            if op == '+':
                num1 = records[-1]
                num2 = records[-2]
                records.append(num1 + num2)
            elif op == 'D':
                num = records[-1]
                records.append(num * 2)
            elif op == 'C':
                records.pop()
            else:
                records.append(int(op))
        return sum(records)