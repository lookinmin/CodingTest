def solution(target):
    dp = [[float('inf'), 0] for _ in range(target + 1)]
    dp[0] = [0, 0]
    
    scores = [50] + [i for i in range(1, 21)] + [i*2 for i in range(1, 21)] + [i*3 for i in range(1, 21)]
    
    for i in range(1, target + 1):
        for score in scores:
            if i >= score:
                dart, single = dp[i - score]
                dart += 1
                single += (score in range(1, 21) or score == 50)
                
                if dart < dp[i][0] or (dart == dp[i][0] and single > dp[i][1]):
                    dp[i] = [dart, single]
    
    return dp[target]