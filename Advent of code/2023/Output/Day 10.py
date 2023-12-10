import numpy as np
import matplotlib.pyplot as plt

with open('Input/Day 10.txt', 'r') as file:
   lis = file.read().split('\n')

grid = [list(line) for line in lis]

for x in grid:
    try:
        start = [grid.index(x), x.index('S')]
    except ValueError:
        1

def adjacent(start):
    adjacent = []
    if grid[start[0]][start[1]+1] in ['-', 'J', '7'] and start[1] < len(grid[0]):
        adjacent.append([start[0], start[1]+1])
    if grid[start[0]-1][start[1]] in ['|', 'F', '7'] and start[0] > 0:
        adjacent.append([start[0]-1, start[1]])
    if grid[start[0]][start[1]-1] in ['-', 'F', 'L'] and start[1] > 0:
        adjacent.append([start[0], start[1]-1])
    if grid[start[0]+1][start[1]] in ['|', 'J', 'L'] and start[0] < len(grid):
        adjacent.append([start[0]+1, start[1]])
    return adjacent

def next(current, previous):
    if grid[current[0]][current[1]] == '|':
        if previous[0] < current[0]:
            return [current[0]+1, current[1]]
        else:
            return [current[0]-1, current[1]]
    if grid[current[0]][current[1]] == '-':
        if previous[1] < current[1]:
            return [current[0], current[1]+1]
        else:
            return [current[0], current[1]-1]
    if grid[current[0]][current[1]] == 'L':
        if previous[0] < current[0]:
            return [current[0], current[1]+1]
        else:
            return [current[0]-1, current[1]]
    if grid[current[0]][current[1]] == 'J':
        if previous[0] < current[0]:
            return [current[0], current[1]-1]
        else:
            return [current[0]-1, current[1]]
    if grid[current[0]][current[1]] == '7':
        if previous[1] < current[1]:
            return [current[0]+1, current[1]]
        else:
            return [current[0], current[1]-1]
    if grid[current[0]][current[1]] == 'F':
        if current[1] < previous[1]:
            return [current[0]+1, current[1]]
        else:
            return [current[0], current[1]+1]
        
current, previous, distance = adjacent(start), [start, start], 1
totalloop = [start.copy()]

while current[0] != current[1]:
    totalloop.append(current[0])
    totalloop.insert(0, current[1])
    next_ = next(current[0], previous[0])
    previous[0] = current[0].copy()
    current[0] = next_.copy()
    next_ = next(current[1], previous[1])
    previous[1] = current[1].copy()
    current[1] = next_.copy()
    distance += 1

print(f'Answer for part 1: {distance}')

# ---------------------------------- Part 2 ---------------------------------- #

totalloop.insert(0, current[1])
endloop = []

for x in reversed(range(totalloop.index(start), len(totalloop))):
    endloop.append(totalloop[x])

for x in endloop:
    totalloop.pop(totalloop.index(x))
    totalloop.insert(0, x)

totalloop.append(start)

x, y = [], []

for i in totalloop:
    x.append(i[1])
    y.append(i[0])

line_length = 0

for n in range(len(x)-1):
    line_length += np.sqrt((x[n+1] - x[n])**2 + (y[n+1] - y[n])**2)

x = np.array(x)
y = np.array(y)

areaplot = plt.fill(x, y)

x, y = (zip(*areaplot[0].xy))
area = 0.5 * np.abs(np.dot(x, np.roll(y, 1)) - np.dot(y, np.roll(x, 1)))

print(f'Answer for part 2: {area-0.5*line_length+1}')