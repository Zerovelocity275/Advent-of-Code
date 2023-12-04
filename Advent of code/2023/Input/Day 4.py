with open('Input/Day 4.txt', 'r') as file:
   lis = file.read().split('\n')

win_nums = [[number for number in line.split('|')[0].split(':')[1].split(' ') if number != ''] for line in lis]
your_nums = [[number for number in line.split('|')[1].split(' ') if number != ''] for line in lis]
gamepoints, gamecards, points, cards_gained = 0, 0, 0, []

for game in range(len(your_nums)):
    for num in your_nums[game]:
        if num in win_nums[game]:
            if gamepoints == 0:
                gamepoints = 1
            else:
                gamepoints *= 2
            gamecards += 1
    cards_gained.append(gamecards)
    points += gamepoints
    gamepoints, gamecards = 0, 0

print(points)

cards_current = [1 for line in lis]

for i in range(len(cards_current)):
    for x in range(cards_current[i]):
        for n in range(cards_gained[i]):
            cards_current[i+n+1] += 1

print(sum(cards_current))