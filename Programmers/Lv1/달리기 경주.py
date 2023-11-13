def solution(players, callings):
    player_dict = {player: idx for idx, player in enumerate(players)}
    # enumerate() 사용 알기

    # print(player_dict)
    for name in callings:
        idx = player_dict[name]
        players[idx], players[idx - 1] = players[idx - 1], players[idx]

        player_dict[players[idx]] = idx
        player_dict[players[idx - 1]] = idx - 1

    return players