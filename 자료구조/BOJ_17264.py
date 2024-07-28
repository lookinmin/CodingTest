from sys import stdin

n, p = map(int, stdin.readline().split())
win, lose, goal = map(int, stdin.readline().split())

players = dict()

for _ in range(p):
    name, state = map(str, stdin.readline().split())
    players[name] = state

score = 0

for _ in range(n):
    play = stdin.readline().rstrip()
    
    if play in players.keys():
        if players[play] == 'W':
            score += win
        else:
            if score - lose <= 0:
                score = 0
            else:
                score -= lose
    else:
        if score - lose <= 0:
            score = 0
        else:
            score -= lose
    if score >= goal:
        print("I AM NOT IRONMAN!!")
        exit()

print("I AM IRONMAN!!")