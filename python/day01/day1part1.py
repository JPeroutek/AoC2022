with open('./data/day1.dat', 'r') as f:
    lines = f.readlines()

groups = []
current_sum = 0
for x in lines:
    x = x.strip()
    if x != '':
        current_sum += float(x)
    else:
        groups.append(current_sum)
        current_sum = 0
print(max(groups))
    