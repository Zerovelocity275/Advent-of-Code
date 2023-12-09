with open('Input/Day 9.txt', 'r') as file:
   lis = file.read().split('\n')

predicted_values, predicted_values2 = [], []

for line in lis:
    history = [[int(value) for  value in line.split(' ')]]
    subhistory, i, prediction = [1], 0, 0
    while not all(value == 0 for value in subhistory):
        subhistory = []
        for x in range(len(history[i])-1):
            subhistory.append(history[i][x+1]-history[i][x])
        history.append(subhistory)
        i += 1
    for i in reversed(range(len(history)-1)):
        prediction = history[i][-1]+prediction
    predicted_values.append(prediction)

print(f'Answer for part 1: {sum(predicted_values)}')

for line in lis:
    history = [[int(value) for  value in line.split(' ')]]
    subhistory, i, prediction = [1], 0, 0
    while not all(value == 0 for value in subhistory):
        subhistory = []
        for x in range(len(history[i])-1):
            subhistory.append(history[i][x]-history[i][x+1])
        history.append(subhistory)
        i += 1
    for i in reversed(range(len(history)-1)):
        prediction = history[i][0]+prediction
    predicted_values2.append(prediction)

print(f'Answer for part 2: {sum(predicted_values2)}')