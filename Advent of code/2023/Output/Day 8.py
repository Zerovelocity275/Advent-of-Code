import math

with open('Input/Day 8.txt', 'r') as file:
   lis = file.read().split('\n\n')

instructions = [['L', 'R'].index(direction) for direction in lis[0]]
elements =  {line.split(' ')[0]:(line.split(' ')[2][1:4], line.split(' ')[-1][:3]) for line in lis[1].split('\n')}

def steps(start_location):
   steps = 0
   if len(start_location) == 1:
      locations = [location for location in elements if location[2] == start_location]
      steplis = []
      for i in range(len(locations)):
         steps = 0
         while locations[i][2] != 'Z':
            for direction in instructions:
               locations[i] = elements[locations[i]][direction]
               steps += 1
               if locations[i][2] == 'Z':
                  break
         steplis.append(steps)
      return steplis
   else:
      location = start_location
      while True:
         for direction in instructions:
            location = elements[location][direction]
            steps += 1
            if location == 'ZZZ':
               return steps

print(f'Answer for part 1: {steps('AAA')}')
print(f'Answer for part 2: {math.lcm(*steps('A'))}')