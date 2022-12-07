with open('./data/day2.dat', 'r') as f:
    lines = f.readlines()

def rotate(l, n):
    return l[-n:] + l[:-n]

lines = [x.strip() for x in lines]

opponent_choices = ['C', 'B', 'A']
result_choices = ['X', 'Y', 'Z']
results = [0, 3, 6]

total_score = 0
for round in lines:
    o, r = tuple(round.split())

    p = rotate(opponent_choices, result_choices.index(r)-1)[opponent_choices.index(o)]

    result_score = result_choices.index(r) * 3
    play_score = opponent_choices[::-1].index(p) + 1

    # this_round_score = player_choice_points[p] + win_outcomes[o][p]
    total_score += result_score + play_score

print(total_score)