class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        seen = set()  # 이미 확인한 숫자들을 저장할 해시셋
        for num in arr:
            # num의 2배가 이미 있거나, num이 짝수이고 num/2가 있는지 확인
            if num * 2 in seen or (num % 2 == 0 and num // 2 in seen):
                return True
            seen.add(num)
        return False