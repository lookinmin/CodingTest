def solution(players, m, k):
    answer = 0
    # server: 각 개별 서버가 만료되는 시간(hour)을 저장하는 리스트.
    # 예를 들어, k=5이고 2시에 서버가 증설되면, 이 서버는 2,3,4,5,6시에 운영되고 7시에 만료됩니다.
    # 이 리스트에는 해당 서버의 만료 시간인 '7'이 저장됩니다.
    server = []

    for i in range(len(players)):    # i는 현재 시간
        needs = players[i] // m      # 지금 필요한 총 서버 수

        active_now = 0               # 현재 운영중인 서버 수
        still_active = []            # 현재 시간에도 살아있는 서버들의 만료 시간
        
        for expire in server:
            if i < expire:             # 현재 시간이 서버 만료 시간 이전이면, 서버는 아직 운영 중
                active_now += 1
                still_active.append(expire)
        server = still_active               # 운영 중인 서버 목록으로 최신화

        plus = 0                            # 이번 시간에 증설할 서버 수
        if active_now < needs:              # 필요한 서버보다 현재 운영 중인 서버가 적다면
            plus = needs - active_now       # 부족한 만큼 증설

        if plus > 0:                        # 증설할 서버가 있다면
            answer += plus                  # 총 증설 횟수에 더함
            for _ in range(plus):
                server.append(i + k)        # 현재 시간 i에 증설된 서버는 (i + k) 시간에 만료됩니다.

    return answer