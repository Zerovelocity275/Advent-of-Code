with open('Input/Day 2.txt', 'r') as file:
   lis = file.read().split('\n')

Games = {game.split(': ')[0]:game.split(':')[1].split(';') for game in lis}
blue, green, red, possible, power = {}, {}, {}, [], []

for game in Games:
   blue[game] = [int(colour.split(' blue')[0].split(' ')[-1]) for colour in Games[game] if 'blue' in colour]
   green[game] = [int(colour.split(' green')[0].split(' ')[-1]) for colour in Games[game] if 'green' in colour]
   red[game] = [int(colour.split(' red')[0].split(' ')[-1]) for colour in Games[game] if 'red' in colour]

for game in Games:
   if all(n <= 14 for n in blue[game]):
      if all(n <= 13 for n in green[game]):
         if all(n <= 12 for n in red[game]):
            possible.append(int(game.split(' ')[1]))
   
   power.append(max(blue[game])*max(green[game])*max(red[game]))

print(f"Sum of possible game ID's is: {sum(possible)}\nSum of each games' power is: {sum(power)}")