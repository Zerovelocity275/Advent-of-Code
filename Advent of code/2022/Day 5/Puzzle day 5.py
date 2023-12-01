import copy

D = str(5)
with open('Day '+D+'/Input day '+D+'.txt', 'r') as file:
   lis = file.read().split('\n\n')
   storage = lis[0].split('\n')
   instructions = lis[1].split('\n')

move, from_, to, crates_, spaces, crates, crates2 = [], [], [], {}, 0, {}, {}
for i in range(len(storage)):
   tempcrates = storage[i].split(' ')
   x = -1
   for n in range(len(tempcrates)):
      x += 1
      if x == len(tempcrates):
         break
      if tempcrates[x] == '':
         spaces += 1
      else:
         spaces = 0
      if spaces == 4:
         del tempcrates[x]
         del tempcrates[x-1]
         del tempcrates[x-2]
         spaces = 0
         x -= 3
   if i == 8:
      tempcrates = [crate for x,crate in enumerate(tempcrates) if crate!='']
   crates_['Storage ' + str(i+1)] = tempcrates
for x in range(9):
   tempcrate = []
   for i in range(8):
      if crates_['Storage ' + str(8-i)][x] == '':
         break
      tempcrate.append(crates_['Storage ' + str(8-i)][x])
   crates['Pile ' + str(x+1)] = tempcrate


for i in range(len(instructions)):
   move.append(int(instructions[i].split(' ')[1]))
   from_.append(int(instructions[i].split(' ')[3]))
   to.append(int(instructions[i].split(' ')[-1]))

crates2 = copy.deepcopy(crates)

for i in range(len(instructions)):
   for x in range(move[i]):
      crates['Pile ' + str(to[i])].append(crates['Pile ' + str(from_[i])][-1])
      del crates['Pile ' + str(from_[i])][-1]
      crates2['Pile ' + str(to[i])].append(crates2['Pile ' + str(from_[i])][x-move[i]])
      del crates2['Pile ' + str(from_[i])][x-move[i]]

answer, answer2 = '', ''
for i in range(len(crates)):
   answer = answer + (crates['Pile ' + str(i+1)][-1][1])
   answer2 = answer2 + (crates2['Pile ' + str(i+1)][-1][1])
print(answer)
print(answer2)