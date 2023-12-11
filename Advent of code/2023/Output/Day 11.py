with open('Input/Day 11.txt', 'r') as file:
   lis = file.read().split('\n')

space = [list(line) for line in lis]
galaxies = [[i, n] for i in range(len(space)) for n in range(len(space[0])) if space[i][n] == '#']
empty_rows = []
empty_columns = []

for i in reversed(range(len(space))):
    if '#' not in space[i]:
        empty_rows.append(i)

for i in reversed(range(len(space[0]))):
    expand = True
    for n in range(len(space)):
        if '#' == space[n][i]:
            expand = False
            break
    if expand:
        empty_columns.append(i)

def total_distance(rate):
    expanded_galaxies = [galaxy.copy() for galaxy in galaxies]
    distance = []

    for i in range(len(galaxies)):
        for column in empty_columns:
            if column < galaxies[i][1]:
                expanded_galaxies[i][1] += rate -1
        for row in empty_rows:
            if row < galaxies[i][0]:
                expanded_galaxies[i][0] += rate -1
                
    for i in range(len(galaxies)):
        for n in range(i+1, len(galaxies)):
            distance.append(abs(expanded_galaxies[i][0]-expanded_galaxies[n][0])+abs(expanded_galaxies[i][1]-expanded_galaxies[n][1]))
    
    return sum(distance)

print(f'Answer for part 1: {total_distance(2)}\nAnswer for part 2: {total_distance(1000000)}')