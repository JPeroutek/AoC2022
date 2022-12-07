with open('./data/day2.dat', 'r') as f:
    lines = f.readlines()

def rotate(l, n):
    return l[-n:] + l[:-n]

lines = [x.strip() for x in lines]

opponent_choices = ['B', 'C', 'A']
player_choices = ['X', 'Y', 'Z']
results = [0, 3, 6]


total_score = 0
for round in lines:
    o, p = tuple(round.split())

    this_round_score = rotate(results, opponent_choices.index(o))[player_choices.index(p)]
    this_round_score += player_choices.index(p) + 1

    total_score += this_round_score

print(total_score)