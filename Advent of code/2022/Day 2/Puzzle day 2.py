

with open('Day 2/Input day 2.txt', 'r') as file:
   list = file.read().split('\n')
P1 = []
P2 = []

for i in range(len(list)):
    P1.append(list[i].split(' ')[0])
    P2.append(list[i].split(' ')[1])

score_part1 = 0
score_part2 = 0

def RPS_part1(p1,p2):
    score = 0
    if p1 == 'A':
        if p2 == 'X':
            score += 4
        elif p2 == 'Y':
            score += 8
        else:
            score += 3
    elif p1 == 'B':
        if p2 == 'X':
            score += 1
        elif p2 == 'Y':
            score += 5
        else:
            score += 9
    else:
        if p2 == 'X':
            score += 7
        elif p2 == 'Y':
            score += 2
        else:
            score += 6
    return score

def RPS_part2(p1,p2):
    score = 0
    if p1 == 'A':
        if p2 == 'X':
            score += 3
        elif p2 == 'Y':
            score += 4
        else:
            score += 8
    elif p1 == 'B':
        if p2 == 'X':
            score += 1
        elif p2 == 'Y':
            score += 5
        else:
            score += 9
    else:
        if p2 == 'X':
            score += 2
        elif p2 == 'Y':
            score += 6
        else:
            score += 7
    return score

for i in range(len(P1)):
    score_part1 += RPS_part1(P1[i], P2[i])
    score_part2 += RPS_part2(P1[i], P2[i])

print('With the first method you scored ' + str(score_part1) + ' points.')
print('With the second method you scored ' + str(score_part2) + ' points.')