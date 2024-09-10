class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five = 0  # $5 지폐의 개수
        ten = 0   # $10 지폐의 개수
        
        for bill in bills:
            if bill == 5:
                five += 1  # $5 지폐를 받았을 때
            elif bill == 10:
                if five > 0:  # $5 지폐가 있어야 $10의 거스름돈을 줄 수 있음
                    five -= 1
                    ten += 1  # $10 지폐를 받은 경우
                else:
                    return False  # $5 지폐가 없다면 거스름돈을 줄 수 없음
            elif bill == 20:
                if ten > 0 and five > 0:  # $10 한 장과 $5 한 장으로 $15를 줄 수 있을 때
                    ten -= 1
                    five -= 1
                elif five >= 3:  # $5 지폐 세 장으로 $15를 줄 수 있을 때
                    five -= 3
                else:
                    return False  # 거스름돈을 줄 수 없으면 False 반환
                
        return True  # 모든 손님에게 거스름돈을 줄 수 있으면 True 반환
